"""Tests of aiconstructlexis.harmonize.batching: signatures, signature groups and batch packing."""
from aiconstructlexis.harmonize import batching
from aiconstructlexis.harmonize.batching import group_by_token_signature, head_noun, make_batches, signature


def test_signature_folds_surface_variants():
    assert signature("Reasoning") == signature("Reasoning ability") == signature("Reasoning capabilities") == "reasoning"
    assert signature("Mathematical reasoning") == signature("Math reasoning") == "math reasoning"
    assert signature("Multi-modal reasoning") == signature("Cross-modal reasoning") == "multimodal reasoning"
    assert signature("Reading comprehension") == signature("Reading understanding")
    assert signature("") == ""


def test_head_noun():
    assert head_noun("Mathematical reasoning") == "reasoning"
    assert head_noun("Hallucination") == "hallucination"
    assert head_noun("") == ""


def test_group_only_identical_signatures():
    names = ["Reasoning", "Reasoning ability", "Mathematical reasoning", "Hallucination", "", "-"]
    ids = group_by_token_signature(names)
    assert ids[0] == ids[1]
    assert len({ids[0], ids[2], ids[3]}) == 3
    assert ids[4] != ids[5]  # names without content tokens stay apart


def test_make_batches_covers_every_index_once_and_keeps_variants_together():
    names = ["Hallucination", "Reasoning", "Code generation", "Reasoning ability", "Output quality",
             "Reasoning skills", "Image quality", "Programming ability"]
    batches = make_batches(names, batch_size=4)
    flat = sorted(i for b in batches for i in b)
    assert flat == list(range(len(names)))
    assert all(len(b) <= 4 for b in batches)
    variants = {names.index("Reasoning"), names.index("Reasoning ability"), names.index("Reasoning skills")}
    assert any(variants <= set(b) for b in batches)


def test_make_batches_splits_oversized_groups():
    names = ["Reasoning", "Reasoning ability", "Reasoning skills", "Reasoning capability"]
    batches = make_batches(names, batch_size=2)
    assert sorted(len(b) for b in batches) == [2, 2]
    assert sorted(i for b in batches for i in b) == [0, 1, 2, 3]


def test_cli_prints_one_json_line_per_batch(tmp_path, capsys):
    names_file = tmp_path / "names.txt"
    names_file.write_text("Reasoning\nReasoning ability\nHallucination\n")
    assert batching.main([str(names_file), "--batch-size", "2"]) == 0
    lines = capsys.readouterr().out.strip().splitlines()
    assert len(lines) == 2
