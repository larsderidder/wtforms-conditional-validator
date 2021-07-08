# WTForms Conditional Validator

A compact WTForms validator that requires a field when another field equals a given value.

## Install
```sh
pip install wtforms-conditional-validator
```

## Usage
```python
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired
from wtforms_conditional_validator import InputRequiredIfFieldEqualTo

class ExampleForm(FlaskForm):
    status = RadioField(choices=[("yes", "Yes"), ("no", "No")])
    notes = StringField(
        "Notes",
        validators=[InputRequiredIfFieldEqualTo("status", "yes")]
    )
```

## License
See `LICENSE`.

## Development
```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
pytest
```
