from typing import Dict

from rest_framework.authtoken.models import Token


def get_token_by_email(email: str) -> Dict[str, str]:
    """Gets user's authentication token key by email address.

    Args:
        email: Email to check for token

    Returns:
        User's token key.
    """
    return Token.objects.filter(user__email=email).values('key').first()


def get_token_by_id(id: int) -> Dict[str, str]:
    """Gets user's authentication token key by id.

    Args:
       id: ID to get token key.

    Returns:
        User's token key.
    """
    return Token.objects.filter(user__id=id).values('key').first()
