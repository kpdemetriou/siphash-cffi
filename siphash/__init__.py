from ._siphash import ffi as __siphash_ffi, lib as __siphash_lib
from ._siphash_variable import ffi as __siphash_variable_ffi, lib as __siphash_variable_lib
from ._halfsiphash import ffi as __halfsiphash_ffi, lib as __halfsiphash_lib
from ._halfsiphash_variable import ffi as __halfsiphash_variable_ffi, lib as __halfsiphash_variable_lib


def __process_in(key, data, c_rounds, d_rounds):
    if not isinstance(key, bytes):
        raise TypeError("'key' must be of type 'bytes'")

    if not isinstance(data, bytes):
        raise TypeError("'data' must be of type 'bytes'")

    if len(key) != 16:
        raise ValueError("'key' must be of length '16'")

    if not isinstance(c_rounds, int):
        raise TypeError("'c_rounds' must be of type 'int'")

    if not isinstance(d_rounds, int):
        raise TypeError("'d_rounds' must be of type 'int'")

    if c_rounds < 0 or c_rounds > 255:
        raise ValueError("'c_rounds' must between 0 and 255")

    if d_rounds < 0 or d_rounds > 255:
        raise ValueError("'d_rounds' must between 0 and 255")

    return key, data, c_rounds, d_rounds


def __process_out(code, digest):
    if code == 0:
        return digest

    raise RuntimeError("Processing failed with error code '{}'".format(code))


def __compute_siphash24(key, data, output_length):
    buffer = __siphash_ffi.new("uint8_t[{}]".format(output_length))

    code = __siphash_lib.siphash(data, len(data), key, buffer, output_length)

    return code, bytes(__siphash_ffi.buffer(buffer, output_length))


def __compute_half_siphash24(key, data, output_length):
    buffer = __halfsiphash_ffi.new("uint8_t[{}]".format(output_length))

    code = __halfsiphash_lib.halfsiphash(data, len(data), key, buffer, output_length)

    return code, bytes(__halfsiphash_ffi.buffer(buffer, output_length))


def __compute_siphash(key, data, output_length, c_rounds, d_rounds):
    buffer = __siphash_variable_ffi.new("uint8_t[{}]".format(output_length))

    code = __siphash_variable_lib.siphash_variable(data, len(data), key, buffer, output_length, c_rounds, d_rounds)

    return code, bytes(__siphash_variable_ffi.buffer(buffer, output_length))


def __compute_half_siphash(key, data, output_length, c_rounds, d_rounds):
    buffer = __halfsiphash_variable_ffi.new("uint8_t[{}]".format(output_length))

    code = __halfsiphash_variable_lib.halfsiphash_variable(
        data, len(data), key, buffer, output_length, c_rounds, d_rounds
    )

    return code, bytes(__halfsiphash_variable_ffi.buffer(buffer, output_length))


def siphash_64(key, data, c_rounds=2, d_rounds=4):
    key, data, c_rounds, d_rounds = __process_in(key, data, c_rounds, d_rounds)

    if c_rounds == 2 and d_rounds == 4:
        code, digest = __compute_siphash24(key, data, 8)
    else:
        code, digest = __compute_siphash(key, data, 8, c_rounds, d_rounds)

    return __process_out(code, digest)


def siphash_128(key, data, c_rounds=2, d_rounds=4):
    key, data, c_rounds, d_rounds = __process_in(key, data, c_rounds, d_rounds)

    if c_rounds == 2 and d_rounds == 4:
        code, digest = __compute_siphash24(key, data, 16)
    else:
        code, digest = __compute_siphash(key, data, 16, c_rounds, d_rounds)

    return __process_out(code, digest)


def half_siphash_32(key, data, c_rounds=2, d_rounds=4):
    key, data, c_rounds, d_rounds = __process_in(key, data, c_rounds, d_rounds)

    if c_rounds == 2 and d_rounds == 4:
        code, digest = __compute_half_siphash24(key, data, 4)
    else:
        code, digest = __compute_half_siphash(key, data, 4, c_rounds, d_rounds)

    return __process_out(code, digest)


def half_siphash_64(key, data, c_rounds=2, d_rounds=4):
    key, data, c_rounds, d_rounds = __process_in(key, data, c_rounds, d_rounds)

    if c_rounds == 2 and d_rounds == 4:
        code, digest = __compute_half_siphash24(key, data, 8)
    else:
        code, digest = __compute_half_siphash(key, data, 8, c_rounds, d_rounds)

    return __process_out(code, digest)
