import pytest

from pydistributedcache.service.cache import LRUCache


@pytest.fixture
def lru_cache(capacity=2):
    return LRUCache(capacity=capacity)
