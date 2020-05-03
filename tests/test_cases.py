import binascii
import siphash


def test_64(case_key, case_data, cases_siphash24_64):
    for i, case in enumerate(cases_siphash24_64):
        output = siphash.siphash_64(case_key, case_data[:i], 2, 4)
        hex_output = binascii.hexlify(output).decode("utf8")

        assert case == hex_output


def test_128(case_key, case_data, cases_siphash24_128):
    for i, case in enumerate(cases_siphash24_128):
        output = siphash.siphash_128(case_key, case_data[:i], 2, 4)
        hex_output = binascii.hexlify(output).decode("utf8")

        assert case == hex_output


def test_half_32(case_key, case_data, cases_half_siphash24_32):
    for i, case in enumerate(cases_half_siphash24_32):
        output = siphash.half_siphash_32(case_key[:8], case_data[:i], 2, 4)
        hex_output = binascii.hexlify(output).decode("utf8")

        assert case == hex_output


def test_half_64(case_key, case_data, cases_half_siphash24_64):
    for i, case in enumerate(cases_half_siphash24_64):
        output = siphash.half_siphash_64(case_key[:8], case_data[:i], 2, 4)
        hex_output = binascii.hexlify(output).decode("utf8")

        assert case == hex_output
