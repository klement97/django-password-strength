import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class UppercaseValidator(object):

    @staticmethod
    def validate(password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
            )

    @staticmethod
    def get_help_text():
        return _(
            "Your password must contain at least 1 uppercase letter, A-Z."
        )


class LowercaseValidator(object):

    @staticmethod
    def validate(password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code='password_no_lower',
            )

    @staticmethod
    def get_help_text():
        return _(
            "Your password must contain at least 1 lowercase letter, a-z."
        )


class SymbolValidator(object):

    @staticmethod
    def validate(password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("The password must contain at least 1 symbol: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    @staticmethod
    def get_help_text():
        return _(
            "Your password must contain at least 1 symbol: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )
