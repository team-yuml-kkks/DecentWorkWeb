from django.db.models.query import QuerySet

from decentwork.apps.professions.models import Profession


def select_professions_starts_with_query_limit_5(query: str) -> QuerySet:
    """Selects professions which name starts with specific query string.

    Args:
        query - Lookup string.

    Returns:
        Professions started with entered query string.
    """
    return Profession.objects.filter(name__istartswith=query)[:5]
