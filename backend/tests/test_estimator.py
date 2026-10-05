from decimal import Decimal

import pytest

from app.domain.estimator import InvalidSimulationError, compare_models, estimate


# Exemplos 1, 2 e 3 de specs/06-regras-de-estimativa.md
@pytest.mark.parametrize(
    "model, task, size, tokens_in, tokens_out, cost",
    [
        ("modus-economico", "summary", "small", 800, 150, "0.000625"),
        ("modus-equilibrado", "explanation", "medium", 500, 500, "0.006000"),
        ("modus-avancado", "code", "large", 700, 1000, "0.037000"),
    ],
)
def test_estimate_matches_spec_examples(model, task, size, tokens_in, tokens_out, cost):
    result = estimate(model, task, size)
    assert result.input_tokens == tokens_in
    assert result.output_tokens == tokens_out
    assert result.total_tokens == tokens_in + tokens_out
    assert result.cost == Decimal(cost)


def test_compare_models_matches_spec_table():
    results = compare_models("summary", "medium")
    assert [r.total_tokens for r in results] == [1300, 1300, 1300]
    assert [r.cost for r in results] == [
        Decimal("0.001150"),
        Decimal("0.006900"),
        Decimal("0.023000"),
    ]


def test_estimate_is_deterministic():
    assert estimate("modus-economico", "text", "small") == estimate(
        "modus-economico", "text", "small"
    )


@pytest.mark.parametrize(
    "args, code",
    [
        (("inexistente", "summary", "small"), "invalid_model"),
        (("modus-economico", "inexistente", "small"), "invalid_task_type"),
        (("modus-economico", "summary", "inexistente"), "invalid_response_size"),
    ],
)
def test_estimate_rejects_unknown_choices(args, code):
    with pytest.raises(InvalidSimulationError) as exc:
        estimate(*args)
    assert exc.value.code == code
