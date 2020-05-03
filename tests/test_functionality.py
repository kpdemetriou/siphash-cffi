import pytest
import siphash


@pytest.mark.parametrize("key_size", [8, 16])
def test_00_64(key_size, case_key, case_data):
    siphash.siphash_64(case_key[:key_size], case_data, 0, 0)


@pytest.mark.parametrize("key_size", [8, 16])
def test_255255_64(key_size, case_key, case_data):
    siphash.siphash_64(case_key[:key_size], case_data, 255, 255)


@pytest.mark.parametrize("key_size", [8, 16])
def test_00_128(key_size, case_key, case_data):
    siphash.siphash_128(case_key[:key_size], case_data, 0, 0)


@pytest.mark.parametrize("key_size", [8, 16])
def test_255255_128(key_size, case_key, case_data):
    siphash.siphash_128(case_key[:key_size], case_data, 255, 255)


@pytest.mark.parametrize("key_size", [4, 8])
def test_half_00_32(key_size, case_key, case_data):
    siphash.half_siphash_32(case_key[:key_size], case_data, 0, 0)


@pytest.mark.parametrize("key_size", [4, 8])
def test_half_255255_32(key_size, case_key, case_data):
    siphash.half_siphash_32(case_key[:key_size], case_data, 255, 255)


@pytest.mark.parametrize("key_size", [4, 8])
def test_half_00_64(key_size, case_key, case_data):
    siphash.half_siphash_64(case_key[:key_size], case_data, 0, 0)


@pytest.mark.parametrize("key_size", [4, 8])
def test_half_255255_64(key_size, case_key, case_data):
    siphash.half_siphash_64(case_key[:key_size], case_data, 255, 255)
