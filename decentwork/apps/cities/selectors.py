from django.db.models.query import QuerySet

from decentwork.apps.cities.models import City


def select_cities_starts_with_query_limit_5(query: str) -> QuerySet:
    """Selects cities which name starts with specific query string.

    Args:
        query - Lookup string.

    Returns:
        Cities started with entered query string.
    """
    # istartswith - case insensitive
    return City.objects.filter(name__istartswith=query)[:5]
