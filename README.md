# SipHash CFFI

[SipHash](https://131002.net/siphash/) is a family of pseudorandom functions (i.e. keyed hash functions) optimized for speed on short messages, designed by [Jean-Philippe Aumasson](https://131002.net/) and [Daniel J. Bernstein](https://cr.yp.to/).

This package provides tested, performant **Python 3** CFFI bindings to the [SipHash 2-4 reference implementation](https://github.com/veorq/SipHash) by [Jean-Philippe Aumasson](https://github.com/veorq) (including support for double-output-size and half-word variants) along with extensions to support tweakable numbers of compression and finalization rounds.

# Installation

You can install this package using `pip` or the included `setup.py` script:

    # Using pip
    pip install siphash-cffi
    
    # Using setup.py
    python setup.py install

# Usage

```python
from siphash import *

# Demonstration key and data
key = b"\0" * 16
data = b"\0" * 64

# SipHash-2-4 working with 64-bit words and a 64-bit output length
output = siphash_64(key, data)

# SipHash-2-4 working with 64-bit words and a 128-bit output length
output = siphash_128(key, data)

# SipHash-2-4 working with 32-bit words and a 32-bit output length
output = half_siphash_32(key, data)

# SipHash-2-4 working with 32-bit words and a 64-bit output length
output = half_siphash_64(key, data)

# SipHash-4-8 working with 64-bit words and a 64-bit output length
output = siphash_64(key, data, 4, 8)

# SipHash-4-8 working with 64-bit words and a 128-bit output length
output = siphash_128(key, data, 4, 8)

# SipHash-4-8 working with 32-bit words and a 32-bit output length
output = half_siphash_32(key, data, 4, 8)

# SipHash-4-8 working with 32-bit words and a 64-bit output length
output = half_siphash_64(key, data, 4, 8)
```

# License
```text
BSD 3-Clause License

Copyright (c) 2018, Phil Demetriou
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```