"""
Tests for the ingest stage: aiconstructlexis.ingest.proceedings, .anthology
and .pmlr. Offline: the fixtures under tests/fixtures/ingest/ are trimmed
copies of real pages (Anthology volumes, a NeurIPS proceedings year, a PMLR
volume index).
"""
import json
import sys
import tempfile
import types
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup

from aiconstructlexis.ingest import anthology as acl
from aiconstructlexis.ingest import pmlr
from aiconstructlexis.ingest import proceedings as pro

FIX = Path(__file__).resolve().parent / "fixtures" / "ingest"
ACL = "2025.acl-long"
ECOM = ("EcomScriptBench: A Multi-task Benchmark for E-commerce Script Planning "
        "via Step-wise Intention-Driven Product Association")


def read(name: str) -> str:
    return (FIX / name).read_text(encoding="utf-8")


def acl_papers(vol: str = ACL):
    return acl.parse_volume_html(read(f"anthology_{vol}_excerpt.html"), vol)


def raises(exc, fn, *a, **kw):
    try:
        fn(*a, **kw)
    except exc as e:
        return e
    raise AssertionError(f"{fn.__name__} did not raise {exc.__name__}")


def no_network(*a, **kw):
    raise AssertionError("network used before the overwrite check")


# ---- ACL: title pairing ------------------------------------------------------

def test_each_title_pairs_with_its_own_pdf():
    papers, _ = acl_papers()
    by_id = {p["paper_id"]: p for p in papers}
    assert by_id[f"{ACL}.1"]["name"] == ECOM
    assert by_id[f"{ACL}.2"]["name"].startswith("GraphNarrator")
    assert by_id[f"{ACL}.3"]["name"].startswith("M-RewardBench")
    for p in papers:
        assert p["url"] == f"https://aclanthology.org/{p['paper_id']}.pdf"


def test_pdf_badge_precedes_the_title_so_titles_come_from_their_own_block():
    """On a volume page the PDF badge comes before the paper's title, so the
    nearest preceding <strong> is the previous paper's title (and the front
    matter's for paper .1); the parser must read each title from its own block."""
    soup = BeautifulSoup(read(f"anthology_{ACL}_excerpt.html"), "html.parser")
    badge1 = soup.find("a", href=f"https://aclanthology.org/{ACL}.1.pdf")
    badge2 = soup.find("a", href=f"https://aclanthology.org/{ACL}.2.pdf")
    assert badge1.find_previous("strong").get_text().startswith("Proceedings of the 63rd")
    assert badge2.find_previous("strong").get_text(strip=True).startswith("EcomScriptBench")
    new = {p["paper_id"]: p["name"] for p in acl_papers()[0]}
    assert new[f"{ACL}.1"] == ECOM
    assert new[f"{ACL}.2"].startswith("GraphNarrator")


def test_titles_keep_spaces_between_tags():
    by_id = {p["paper_id"]: p["name"] for p in acl_papers()[0]}
    assert "for E-commerce" in by_id[f"{ACL}.1"] and "forE-commerce" not in by_id[f"{ACL}.1"]
    assert by_id[f"{ACL}.111"].startswith("LLäMmlein: Transparent, Compact and Competitive German-Only")
    assert by_id[f"{ACL}.263"] == "L-CiteEval: A Suite for Evaluating Fidelity of Long-context Models"
    assert by_id[f"{ACL}.1225"].startswith("GeLLM³O: Generalizing")
    soup = BeautifulSoup(read(f"anthology_{ACL}_excerpt.html"), "html.parser")
    glued = soup.find("a", href=f"/{ACL}.1/").get_text(strip=True)
    assert "forE-commerce" in glued  # get_text(strip=True) glues the words; the parser must not


def test_front_matter_volume_pdf_and_attachments_are_skipped():
    expected = {
        "2025.acl-long": [1, 2, 3, 111, 263, 1225],
        "2025.emnlp-main": [1, 2, 3],
        "2025.naacl-long": [1, 2],
    }
    for vol, nums in expected.items():
        papers, stats = acl_papers(vol)
        assert [p["paper_id"] for p in papers] == [f"{vol}.{n}" for n in nums], vol
        assert stats["front_matter"] == 1
        for p in papers:
            assert "/attachments/" not in p["url"]
            assert p["url"] != f"https://aclanthology.org/{vol}.pdf"
            assert not p["name"].startswith("Proceedings of")
    assert acl_papers("2025.emnlp-main")[1]["attachments"] == 3   # checklists seen, not listed
    assert acl_papers("2025.naacl-long")[1]["volume_pdf"] >= 1     # whole-volume PDF seen, not listed


def test_block_whose_pdf_link_names_another_paper_is_rejected():
    html = read(f"anthology_{ACL}_excerpt.html").replace(
        f"href=https://aclanthology.org/{ACL}.2.pdf", f"href=https://aclanthology.org/{ACL}.3.pdf", 1)
    err = raises(ValueError, acl.parse_volume_html, html, ACL)
    assert f"{ACL}.2" in str(err)


def test_other_years_and_relative_pdf_links():
    assert acl.volume_id("acl", 2026) == "2026.acl-long"
    assert acl.volume_id("emnlp", 2026) == "2026.emnlp-main"
    html = (read(f"anthology_{ACL}_excerpt.html").replace(ACL, "2026.acl-long")
            .replace("https://aclanthology.org/2026.acl-long.", "/2026.acl-long."))
    papers, _ = acl.parse_volume_html(html, "2026.acl-long")
    assert len(papers) == 6
    assert papers[0] == {"name": ECOM, "url": "https://aclanthology.org/2026.acl-long.1.pdf",
                         "paper_id": "2026.acl-long.1"}


# ---- ACL: BibTeX ---------------------------------------------------------------

def test_bibtex_parser_handles_both_delimiters_and_latex():
    bt = acl.bib_titles(read("anthology_2025_excerpt.bib"))
    assert f"{ACL}.0" not in bt and len(bt) == 11
    assert bt[f"{ACL}.1"] == ECOM
    assert bt[f"{ACL}.111"].startswith("LLäMmlein: Transparent")   # title = {...}
    assert bt[f"{ACL}.1225"].startswith("GeLLM³O:")                 # \textthreesuperior
    assert bt[f"{ACL}.263"].startswith("L-CiteEval: A Suite")       # $\textit{...}$
    c = acl.clean_bib_title
    assert c(r"D{\'e}j{\`a} Vu? Decoding") == "Déjà Vu? Decoding"
    assert c(r"Think{\&}Cite") == "Think&Cite"
    assert c(r"Top-$n\sigma$: Eliminating") == "Top-nσ: Eliminating"
    assert c(r"From $\log \pi$ to $\pi$: Taming") == "From log π to π: Taming"
    assert c(r"({RSA}){\texttwosuperior}: A") == "(RSA)²: A"
    assert c(r"Doesn{'}t Stop") == "Doesn't Stop"


def test_bib_cross_check_passes_and_catches_a_shift():
    papers, _ = acl_papers()
    bt = {k: v for k, v in acl.bib_titles(read("anthology_2025_excerpt.bib")).items()
          if k.startswith(ACL + ".")}
    rep = acl.check_against_bib(papers, bt)
    assert rep["match"] == rep["papers"] == 6 and not rep["mismatch"]
    assert not rep["missing_in_bib"] and not rep["missing_on_page"]
    shifted = [dict(p, name=papers[i - 1]["name"]) for i, p in enumerate(papers)]
    assert len(acl.check_against_bib(shifted, bt)["mismatch"]) == 6


def test_list_volume_stops_on_a_bib_disagreement():
    html, bib = read(f"anthology_{ACL}_excerpt.html"), read("anthology_2025_excerpt.bib")
    assert len(acl.list_volume(ACL, None, html=html, bib_text=bib)) == 6
    bad = html.replace("Explanations for Graph Neural Networks</a>", "Explanation for Graph Neural Networks</a>", 1)
    assert bad != html
    raises(RuntimeError, acl.list_volume, ACL, None, html=bad, bib_text=bib)
    assert len(acl.list_volume(ACL, None, check=False, html=bad)) == 6


# ---- lists are never silently overwritten ------------------------------------------

def test_guard_refuses_existing_list_without_force():
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "x_papers.json"
        out.write_text("[]")
        err = raises(FileExistsError, pro.guard_lists, [out], False)
        assert "--force" in str(err)
        pro.guard_lists([out], True)
        pro.guard_lists([Path(d) / "new_papers.json"], False)


def test_write_list_is_exclusive_without_force():
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "x_papers.json"
        pro.write_list(out, [{"name": "a"}], force=False)
        raises(FileExistsError, pro.write_list, out, [{"name": "b"}], False)
        assert json.loads(out.read_text()) == [{"name": "a"}]
        pro.write_list(out, [{"name": "b"}], force=True)
        assert json.loads(out.read_text()) == [{"name": "b"}]


def test_every_cli_refuses_before_fetching():
    saved = (pro.http_get, acl.http_get, pmlr.http_get)
    pro.http_get = acl.http_get = pmlr.http_get = no_network
    try:
        with tempfile.TemporaryDirectory() as d:
            logs = ["--log-dir", str(Path(d) / "logs")]
            out = Path(d) / "existing_papers.json"
            out.write_text("[]")
            runs = [
                lambda: pro.main(["--conference", "neurips", "--year", "2025", "--out", str(out)] + logs),
                lambda: acl.main(["--venue", "acl", "--year", "2026", "--out", str(out)] + logs),
                lambda: acl.main(["--volume", "2026.emnlp-main", "--metadata-only", "--out", str(out)] + logs),
                lambda: pmlr.main(["--volume", "306", "--conference", "icml", "--year", "2026",
                                   "--out", str(out)] + logs),
                lambda: pro.download_venue("iclr", 2026, out, Path(d) / "pdf"),
                lambda: acl.download_anthology("acl", 2026, out, Path(d) / "pdf"),
                lambda: pmlr.download_pmlr(306, "icml", 2026, out, Path(d) / "pdf"),
            ]
            for run in runs[:4]:
                err = raises(SystemExit, run)
                assert "Refusing to overwrite" in str(err)
                assert out.read_text() == "[]"
            for run in runs[4:]:
                err = raises(FileExistsError, run)
                assert "Refusing to overwrite" in str(err)
                assert out.read_text() == "[]"
            sample_out = Path(d) / "fresh_papers.json"
            pro.sample_list_path(sample_out).write_text("[]")   # only the sample list exists
            err = raises(SystemExit, lambda: pmlr.main(
                ["--volume", "306", "--conference", "icml", "--year", "2026",
                 "--sample", "3", "--out", str(sample_out)] + logs))
            assert "fresh_papers.sample.json" in str(err)
    finally:
        pro.http_get, acl.http_get, pmlr.http_get = saved


def test_pdf_dir_defaults_next_to_the_list():
    out, pdf_dir = pro.resolve_outputs("work/iclr26/papers.json", None)
    assert out == Path("work/iclr26/papers.json")
    assert pdf_dir == Path("work/iclr26/papers")
    out, pdf_dir = pro.resolve_outputs("work/iclr26/papers.json", "elsewhere/pdfs")
    assert pdf_dir == Path("elsewhere/pdfs")
    assert pro.default_pdf_dir(Path("work/list")) == Path("work/list_pdfs")


# ---- seeded sampling -------------------------------------------------------------

def entries(n):
    return [{"name": f"Paper number {i}", "url": f"https://x.org/{i}.pdf"} for i in range(n)]


def test_sample_is_reproducible_and_independent_of_listing_order():
    es = entries(500)
    a = pro.select_sample(es, 20, seed=7)
    assert len(a) == 20
    assert a == pro.select_sample(list(reversed(es)), 20, seed=7)
    assert a == pro.select_sample(es[250:] + es[:250], 20, seed=7)
    assert a != pro.select_sample(es, 20, seed=8)
    assert pro.select_sample(es, 900, seed=0) == {e["url"] for e in es}
    # Pinned so any change to the sampling scheme is noticed.
    assert pro.select_sample(entries(50), 3, seed=0) == {
        "https://x.org/30.pdf", "https://x.org/32.pdf", "https://x.org/8.pdf"}


def fake_fetch(fail=()):
    calls = []

    def fetch(url, path):
        calls.append(url)
        if url in fail:
            return "HTTP 404"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"%PDF-1.4\n" + b"0" * 2000)
        return None
    return fetch, calls


def test_sample_mode_downloads_only_the_sample_and_marks_it():
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        es = entries(30)
        pro.assign_paths(es, d / "pdfs")
        chosen = pro.select_sample(es, 4, seed=3)
        failing = sorted(chosen)[0]
        fetch, calls = fake_fetch(fail={failing})
        out = d / "v_papers.json"
        summary = pro.finish(es, out, metadata_only=False, sample=4, seed=3, force=False, fetch=fetch)
        assert set(calls) == chosen
        full = json.loads(out.read_text())
        assert len(full) == 30 and sum(p["sampled"] for p in full) == 4
        for p in full:
            if p["url"] == failing:
                assert p["sampled"] and "path" not in p and p["download_error"] == "HTTP 404"
            elif p["sampled"]:
                assert Path(p["path"]).is_file()
            else:
                assert "path" not in p and "download_error" not in p
        sample = json.loads(pro.sample_list_path(out).read_text())
        assert [p["url"] for p in sample] == [p["url"] for p in full if p["sampled"] and "path" in p]
        assert len(sample) == 3 and all(Path(p["path"]).is_file() for p in sample)
        assert summary["downloaded"] == 3 and summary["failed"] == 1
        assert len(list((d / "pdfs").glob("*.pdf"))) == 3
        raises(FileExistsError, pro.finish, entries(30), out, metadata_only=True, sample=None,
               seed=0, force=False)


def test_metadata_only_and_full_runs_keep_a_path_on_every_entry():
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        es = entries(5)
        pro.assign_paths(es, d / "pdfs")
        pro.finish(es, d / "m.json", metadata_only=True, sample=None, seed=0, force=False)
        meta = json.loads((d / "m.json").read_text())
        assert all("path" in p and "sampled" not in p for p in meta)
        assert not (d / "pdfs").exists()
        es = entries(5)
        pro.assign_paths(es, d / "pdfs")
        fetch, calls = fake_fetch()
        pro.finish(es, d / "f.json", metadata_only=False, sample=None, seed=0, force=False, fetch=fetch)
        assert len(calls) == 5 and all(Path(p["path"]).is_file()
                                       for p in json.loads((d / "f.json").read_text()))


def test_assign_paths_never_shares_a_file():
    es = [{"name": n, "url": str(i)} for i, n in
          enumerate(["Same Title", "Same Title", "same title", "Other: Title"])]
    pro.assign_paths(es, Path("/tmp/p"))
    paths = [e["path"] for e in es]
    assert len({p.lower() for p in paths}) == 4
    assert paths[0].endswith("/Same_Title.pdf") and paths[3].endswith("/Other_Title.pdf")
    es = [{"name": "x", "url": "1", "paper_id": "2026.acl-long.7"}]
    pro.assign_paths(es, Path("/tmp/p"), stem=lambda e: e["paper_id"])
    assert es[0]["path"] == "/tmp/p/2026.acl-long.7.pdf"


# ---- NeurIPS / ICLR proceedings: tracks ---------------------------------------------

YEAR_URL = "https://proceedings.neurips.cc/paper_files/paper/2025"
PAGES = {YEAR_URL: "proceedings_neurips2025_year.html",
         YEAR_URL + "/vol38-main-conference": "proceedings_neurips2025_main.html"}


def fetch_page(url):
    return read(PAGES[url.rstrip("/")])


def test_neurips_default_tracks_follow_see_also_and_filter():
    papers = pro.list_proceedings_cc("neurips", 2025, pro.parse_tracks(None, "neurips"), fetch=fetch_page)
    assert Counter(p["track"] for p in papers) == {"Conference": 2, "Datasets_and_Benchmarks_Track": 2}
    db = [p for p in papers if p["track"] == "Datasets_and_Benchmarks_Track"][0]
    assert db["url"].endswith("-Paper-Datasets_and_Benchmarks_Track.pdf")
    assert "/paper_files/paper/2025/file/" in db["url"]
    everything = pro.list_proceedings_cc("neurips", 2025, pro.parse_tracks("all", "neurips"),
                                        fetch=fetch_page)
    assert Counter(p["track"] for p in everything) == {
        "Conference": 2, "Datasets_and_Benchmarks_Track": 2,
        "Position_Paper_Track": 2, "Creative_AI_Track": 2}
    only = pro.list_proceedings_cc("neurips", 2025, pro.parse_tracks("main,position", "neurips"),
                                  fetch=fetch_page)
    assert Counter(p["track"] for p in only) == {"Conference": 2, "Position_Paper_Track": 2}
    err = raises(ValueError, pro.list_proceedings_cc, "neurips", 2025,
                 pro.parse_tracks("main,oral", "neurips"), fetch=fetch_page)
    assert "oral" in str(err)  # a typo must not fall through to OpenReview


def test_track_option_parsing():
    assert pro.parse_tracks(None, "neurips") == ["Conference", "Datasets_and_Benchmarks_Track"]
    assert pro.parse_tracks(None, "iclr") is None
    assert pro.parse_tracks("all", "neurips") is None
    assert pro.parse_tracks("main, db,creative", "neurips") == [
        "Conference", "Datasets_and_Benchmarks_Track", "Creative_AI_Track"]
    assert pro.parse_tracks("Position_Paper_Track", "neurips") == ["Position_Paper_Track"]


# ---- PMLR ---------------------------------------------------------------------------

def test_pmlr_index_parse():
    papers = pro.parse_pmlr_index(read("pmlr_v306_excerpt.html"))
    assert [p["name"] for p in papers] == [
        "TUR-DPO: Topology- and Uncertainty-Aware Direct Preference Optimization",
        "What Preferences Can\u2014and Cannot\u2014Predict in Multi-Agent Online Learning"]
    assert papers[0]["url"] == "https://raw.githubusercontent.com/mlresearch/v306/main/assets/abas26a/abas26a.pdf"


def test_pmlr_cli_and_entry_write_the_list():
    seen = []
    saved = pmlr.list_pmlr_volume

    def fake(volume):
        seen.append(volume)
        return pro.parse_pmlr_index(read("pmlr_v306_excerpt.html"))
    pmlr.list_pmlr_volume = fake
    try:
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            assert pmlr.main(["--volume", "306", "--conference", "icml", "--year", "2026",
                              "--metadata-only", "--max-workers", "4", "--out", str(d / "a.json"),
                              "--pdf-dir", str(d / "pdf"), "--log-dir", str(d / "logs")]) == 0
            written = pmlr.download_pmlr(306, "icml", 2026, d / "b.json", d / "pdf", metadata_only=True)
            assert written == d / "b.json" and seen == [306, 306]
            b = json.loads((d / "b.json").read_text())
            assert b == json.loads((d / "a.json").read_text())
            assert b[0] == {"name": "TUR-DPO: Topology- and Uncertainty-Aware Direct Preference Optimization",
                            "url": "https://raw.githubusercontent.com/mlresearch/v306/main/assets/abas26a/abas26a.pdf",
                            "path": str(d / "pdf" / "TUR_DPO_Topology_and_Uncertainty_Aware_Direct_Preference_Optimization.pdf")}
            # the default PDF directory sits next to the list
            pmlr.download_pmlr(306, "icml", 2026, d / "c.json", metadata_only=True)
            c = json.loads((d / "c.json").read_text())
            assert c[0]["path"].startswith(str(d / "c") + "/")
    finally:
        pmlr.list_pmlr_volume = saved


# ---- entry functions end to end (offline) -------------------------------------------

class FakeResponse:
    def __init__(self, text):
        self.text = text


def fake_http_get(pages):
    def http_get(url, timeout=60, retries=3):
        key = url.rstrip("/")
        if key not in pages:
            raise AssertionError(f"unexpected request: {url}")
        return FakeResponse(read(pages[key]))
    return http_get


def test_download_venue_lists_proceedings_and_returns_the_list_path():
    saved = pro.http_get
    pro.http_get = fake_http_get(PAGES)
    try:
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            out = pro.download_venue("neurips", 2025, d / "papers.json", d / "pdfs",
                                     source="proceedings", metadata_only=True)
            assert out == d / "papers.json"
            papers = json.loads(out.read_text())
            assert Counter(p["track"] for p in papers) == {"Conference": 2, "Datasets_and_Benchmarks_Track": 2}
            assert all(p["path"].startswith(str(d / "pdfs")) for p in papers)
            assert set(papers[0]) == {"name", "url", "track", "path"}
            # the list is never overwritten, even with the same content
            raises(FileExistsError, pro.download_venue, "neurips", 2025, d / "papers.json", d / "pdfs",
                   source="proceedings", metadata_only=True)
            out2 = pro.download_venue("neurips", 2025, d / "papers.json", d / "pdfs", source="proceedings",
                                      tracks=["main", "position"], metadata_only=True, force=True)
            assert Counter(p["track"] for p in json.loads(out2.read_text())) == {
                "Conference": 2, "Position_Paper_Track": 2}
            raises(ValueError, pro.download_venue, "neurips", 2025, d / "other.json", d / "pdfs",
                   source="nowhere")
    finally:
        pro.http_get = saved


def test_download_anthology_checks_bibtex_and_returns_the_list_path():
    saved = acl.http_get
    acl.http_get = fake_http_get({
        f"https://aclanthology.org/volumes/{ACL}": f"anthology_{ACL}_excerpt.html",
        f"https://aclanthology.org/volumes/{ACL}.bib": "anthology_2025_excerpt.bib",
    })
    try:
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            out = acl.download_anthology(None, None, d / "papers.json", d / "pdfs", volume=ACL,
                                         bib_cache=d / "bib", metadata_only=True)
            assert out == d / "papers.json"
            assert (d / "bib" / f"{ACL}.bib").is_file()           # BibTeX cached for the next run
            papers = json.loads(out.read_text())
            assert [p["paper_id"] for p in papers] == [f"{ACL}.{n}" for n in (1, 2, 3, 111, 263, 1225)]
            assert papers[0]["path"] == str(d / "pdfs" / f"{ACL}.1.pdf")
            assert set(papers[0]) == {"name", "url", "paper_id", "path"}
            assert acl.resolve_volume("acl", 2025, None) == ("acl", 2025, ACL)
            assert acl.resolve_volume(None, None, "2026.emnlp-main") == ("emnlp", 2026, "2026.emnlp-main")
            raises(ValueError, acl.resolve_volume, None, None, None)
            raises(ValueError, acl.resolve_volume, "workshop", 2026, None)
    finally:
        acl.http_get = saved


# ---- OpenReview: acceptance from the venue string ------------------------------

ACCEPTED_VENUES = ["ICLR 2025 Poster", "ICLR 2025 Spotlight", "ICLR 2025 Oral", "Accept (poster)",
                   "NeurIPS 2025 accept"]
NOT_ACCEPTED_VENUES = ["Submitted to ICLR 2025", "ICLR 2025 Conference Withdrawn Submission",
                       "ICLR 2025 Conference Rejected Submission", "ICLR 2025 Conference Desk Rejected Submission",
                       "ICLR 2025", "ICLR 2025 Conference Submission", "", "Submitted to ICLR 2025 (poster track)"]


def test_venue_string_accepted_needs_a_decision_word_and_no_rejection_word():
    assert all(pro.venue_string_accepted(v) for v in ACCEPTED_VENUES)
    assert not any(pro.venue_string_accepted(v) for v in NOT_ACCEPTED_VENUES)


def fake_openreview(notes):
    """An ``openreview`` module whose client returns the given notes for every query."""
    class Client:
        def __init__(self, baseurl):
            self.baseurl = baseurl

        def get_all_notes(self, invitation, details):
            assert invitation == "ICLR.cc/2025/Conference/-/Submission" and details == "directReplies"
            return notes

    mod = types.ModuleType("openreview")
    mod.api = types.SimpleNamespace(OpenReviewClient=Client)
    return mod


def note(nid, venue, decision=None, venueid=""):
    replies = [{"invitation": "ICLR.cc/2025/Conference/-/Decision", "content": {"decision": {"value": decision}}}] if decision else []
    return types.SimpleNamespace(id=nid, details={"directReplies": replies},
                                 content={"title": {"value": f"Paper {nid}"}, "venue": {"value": venue},
                                          "venueid": {"value": venueid}})


def test_list_openreview_keeps_only_accepted_submissions():
    notes = [note("d", "ICLR 2025", decision="Accept (Poster)"),
             note("v", "ICLR 2025", venueid="ICLR.cc/2025/Conference/Accept")]
    notes += [note(f"a{i}", v) for i, v in enumerate(ACCEPTED_VENUES)]
    notes += [note(f"n{i}", v) for i, v in enumerate(NOT_ACCEPTED_VENUES)]
    saved = sys.modules.get("openreview")
    sys.modules["openreview"] = fake_openreview(notes)
    try:
        papers = pro.list_openreview("iclr", 2025)
    finally:
        if saved is None:
            sys.modules.pop("openreview", None)
        else:
            sys.modules["openreview"] = saved
    assert [p["name"] for p in papers] == ["Paper d", "Paper v"] + [f"Paper a{i}" for i in range(len(ACCEPTED_VENUES))]
    assert papers[0]["url"] == "https://openreview.net/pdf?id=d"
