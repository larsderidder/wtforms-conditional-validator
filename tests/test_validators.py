from wtforms import Form, StringField

from wtforms_conditional_validator import InputRequiredIfFieldEqualTo


class SampleForm(Form):
    mode = StringField()
    notes = StringField(validators=[InputRequiredIfFieldEqualTo("mode", "yes")])


def test_required_when_condition_matches():
    form = SampleForm(data={"mode": "yes", "notes": ""})
    assert form.validate() is False
    assert "notes" in form.errors


def test_not_required_when_condition_does_not_match():
    form = SampleForm(data={"mode": "no", "notes": ""})
    assert form.validate() is True


def test_raises_when_other_field_missing():
    class BadForm(Form):
        field = StringField(
            validators=[InputRequiredIfFieldEqualTo("missing", "yes")]
        )

    form = BadForm(data={"field": ""})
    try:
        form.validate()
    except Exception as exc:
        assert 'no field named "missing"' in str(exc)
    else:
        raise AssertionError("Expected exception for missing field")
