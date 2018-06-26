import pytest
import siphash


def test_invalid_key_type(case_data):
    with pytest.raises(TypeError):
        siphash.siphash_64("", case_data)


def test_invalid_data_type(case_key):
    with pytest.raises(TypeError):
        siphash.siphash_64(case_key, "")


def test_invalid_key_length(case_key, case_data):
    with pytest.raises(ValueError):
        siphash.siphash_64(case_key + b"\0", case_data)


def test_invalid_c_rounds_type(case_key, case_data):
    with pytest.raises(TypeError):
        siphash.siphash_64(case_key, case_data, c_rounds=1.00)


def test_invalid_d_rounds_type(case_key, case_data):
    with pytest.raises(TypeError):
        siphash.siphash_64(case_key, case_data, d_rounds=1.00)


def test_invalid_c_rounds_value_low(case_key, case_data):
    with pytest.raises(ValueError):
        siphash.siphash_64(case_key, case_data, c_rounds=-256)


def test_invalid_c_rounds_value_high(case_key, case_data):
    with pytest.raises(ValueError):
        siphash.siphash_64(case_key, case_data, c_rounds=256)


def test_invalid_d_rounds_value_low(case_key, case_data):
    with pytest.raises(ValueError):
        siphash.siphash_64(case_key, case_data, d_rounds=-256)


def test_invalid_d_rounds_value_high(case_key, case_data):
    with pytest.raises(ValueError):
        siphash.siphash_64(case_key, case_data, d_rounds=256)
