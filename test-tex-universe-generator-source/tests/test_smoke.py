from test_tex_generator.config import GenerationConfig
from test_tex_generator.generator import UniverseTestGenerator
from test_tex_generator.state import GeneratorState


def test_generates_unique_syntactically_intended_cases():
    config = GenerationConfig(count=20, seed=10)
    state = GeneratorState()
    cases = UniverseTestGenerator(config, state).generate()
    assert len(cases) == 20
    assert len({case.rendering_hash for case in cases}) == 20
    assert all(case.expected["syntactically_intended_valid"] for case in cases)
    assert any("Suppose that" in case.tex or "Assume that" in case.tex for case in cases)
