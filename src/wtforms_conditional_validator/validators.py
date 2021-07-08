from typing import Any, Optional

import wtforms


class InputRequiredIfFieldEqualTo(wtforms.validators.InputRequired):
    """Require a field when another field matches a specific value.

    Sources:
        - http://wtforms.simplecodes.com/docs/1.0.1/validators.html
        - http://stackoverflow.com/questions/8463209/how-to-make-a-field-conditionally-optional-in-wtforms
    """

    field_flags = {"requiredif": True}

    def __init__(
        self,
        source_key: str,
        trigger_value: Any,
        message: Optional[str] = None,
        *args,
        **kwargs,
    ):
        self.source_key = source_key
        self.trigger_value = trigger_value
        self.message = message

    def __call__(self, form, field) -> None:
        other_field = self._lookup_source(form)
        if self._should_enforce(other_field):
            super(InputRequiredIfFieldEqualTo, self).__call__(form, field)

    def _lookup_source(self, form):
        if self.source_key in form:
            return form[self.source_key]
        raise Exception(
            'no field named "%s" in form' % self.source_key
        )

    def _should_enforce(self, other_field) -> bool:
        return other_field.data == self.trigger_value
