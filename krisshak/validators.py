import re
from django.core.exceptions import ValidationError

class ComplexPasswordValidator:
    def validate(self, password, user=None):
        if not re.findall(r'[A-Za-z]', password) or not re.findall(r'[0-9]', password) or not re.findall(r'[@$!%*#?&]', password):
            raise ValidationError(
                "Password must contain at least one letter, one number, and one special character."
            )

    def get_help_text(self):
        return "Your password must contain at least one letter, one number, and one special character."