"""The two prompt sets: both load by name, the earlier revision differs from the default
only in the two extraction prompts, and the revision of 29 April added the instrument-to-
instrument relationship pattern."""
from aiconstructlexis.prompts import REQUIRED_NAMES, load_prompts


def test_earlier_revision_differs_from_the_default_only_in_the_extraction_prompts():
    default = load_prompts("default")
    earlier = load_prompts("aiconstructlexis.prompts.earlier")
    for name in REQUIRED_NAMES:
        assert hasattr(earlier, name)
    changed = {"EXTRACT_ENTITIES_PROMPT", "EXTRACT_RELATIONSHIPS_PROMPT"}
    for name in changed:
        assert getattr(earlier, name) != getattr(default, name)
    for name in set(REQUIRED_NAMES) - changed:
        assert getattr(earlier, name) == getattr(default, name)
    pattern = "measurement instrument ↔ measurement instrument"
    assert pattern in default.EXTRACT_RELATIONSHIPS_PROMPT
    assert pattern not in earlier.EXTRACT_RELATIONSHIPS_PROMPT
    assert "{entities_json}" in earlier.EXTRACT_RELATIONSHIPS_PROMPT
    assert "Spatial reasoning" in earlier.EXTRACT_ENTITIES_PROMPT   # the example network is embedded
