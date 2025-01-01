import pytest

from pydistributedcache.service.cache import LRUCache


def test_lru_cache_put_and_get(lru_cache):
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    assert lru_cache.get(1) == 1
    lru_cache.put(3, 3)
    assert lru_cache.get(2) == -1  # As 2 should be evicted
    lru_cache.put(4, 4)
    assert lru_cache.get(1) == -1  # As 1 should be evicted
    assert lru_cache.get(3) == 3
    assert lru_cache.get(4) == 4


def test_lru_cache_eviction(lru_cache):
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    assert lru_cache.get(1) == 1
    lru_cache.put(3, 3)  # Evicts key 2
    assert lru_cache.get(2) == -1
    lru_cache.put(4, 4)  # Evicts key 1
    assert lru_cache.get(1) == -1
    assert lru_cache.get(3) == 3
    assert lru_cache.get(4) == 4


def test_lru_cache_update(lru_cache):
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(1, 10)  # Update value for key 1
    assert lru_cache.get(1) == 10
    assert lru_cache.get(2) == 2
