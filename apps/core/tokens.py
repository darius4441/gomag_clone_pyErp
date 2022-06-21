"""Generador del tokens para el registro de usuarios
"""
# Django Library
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class TokenGenerator(PasswordResetTokenGenerator):
    """Esta clase genera un token que se envía en correo para validadar el
    registro del usuario
    """

    def _make_hash_value(self, user, timestamp):
        return text_type(user.pk) + text_type(timestamp) + text_type(user.is_active)


ACCOUNT_ACTIVATION_TOKEN = TokenGenerator()

PASSWORD_RECOVERY_TOKEN = TokenGenerator()
