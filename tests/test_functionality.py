import siphash


def test_00_64(case_key_16, case_data):
    siphash.siphash_64(case_key_16, case_data, 0, 0)


def test_255255_64(case_key_16, case_data):
    siphash.siphash_64(case_key_16, case_data, 255, 255)


def test_00_128(case_key_16, case_data):
    siphash.siphash_128(case_key_16, case_data, 0, 0)


def test_255255_128(case_key_16, case_data):
    siphash.siphash_128(case_key_16, case_data, 255, 255)


def test_half_00_32(case_key_8, case_data):
    siphash.half_siphash_32(case_key_8, case_data, 0, 0)


def test_half_255255_32(case_key_8, case_data):
    siphash.half_siphash_32(case_key_8, case_data, 255, 255)


def test_half_00_64(case_key_8, case_data):
    siphash.half_siphash_64(case_key_8, case_data, 0, 0)


def test_half_255255_64(case_key_8, case_data):
    siphash.half_siphash_64(case_key_8, case_data, 255, 255)
