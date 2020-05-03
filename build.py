import os
from cffi import FFI


source_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sources")
source_file_siphash = os.path.join(source_directory, "siphash.c")
source_file_siphash_variable = os.path.join(source_directory, "siphash_variable.c")
source_file_halfsiphash = os.path.join(source_directory, "halfsiphash.c")
source_file_halfsiphash_variable = os.path.join(source_directory, "halfsiphash_variable.c")

siphash_ffi, siphash_variable_ffi, halfsiphash_ffi, halfsiphash_variable_ffi = FFI(), FFI(), FFI(), FFI()

siphash_ffi.cdef(
    "int siphash(const uint8_t *in, const size_t inlen, const uint8_t *k, uint8_t *out, const size_t outlen);"
)

siphash_variable_ffi.cdef(
    "int siphash_variable(const uint8_t *in, const size_t inlen, const uint8_t *k, uint8_t *out,"
    "const size_t outlen, uint8_t c_rounds, uint8_t d_rounds);"
)

halfsiphash_ffi.cdef(
    "int halfsiphash(const uint8_t *in, const size_t inlen, const uint8_t *k, uint8_t *out, const size_t outlen);"
)

halfsiphash_variable_ffi.cdef(
    "int halfsiphash_variable(const uint8_t *in, const size_t inlen, const uint8_t *k, uint8_t *out,"
    "const size_t outlen, uint8_t c_rounds, uint8_t d_rounds);"
)

with open(source_file_siphash) as source_siphash:
    siphash_ffi.set_source("siphash._siphash", source_siphash.read())

with open(source_file_siphash_variable) as source_siphash_variable:
    siphash_variable_ffi.set_source("siphash._siphash_variable", source_siphash_variable.read())

with open(source_file_halfsiphash) as source_halfsiphash:
    halfsiphash_ffi.set_source("siphash._halfsiphash", source_halfsiphash.read())

with open(source_file_halfsiphash_variable) as source_halfsiphash_variable:
    halfsiphash_variable_ffi.set_source("siphash._halfsiphash_variable", source_halfsiphash_variable.read())

if __name__ == "__main__":
    siphash_ffi.compile(verbose=True)
    siphash_variable_ffi.compile(verbose=True)
    halfsiphash_ffi.compile(verbose=True)
    halfsiphash_variable_ffi.compile(verbose=True)
