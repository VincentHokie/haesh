haesh
=====

A Python implementation of a 2048 bit hash function based on the the AES block cipher algorithm in the CBC mode of operation.


Features
--------

* Supports 128 bit salt size
* Accepts file/ text input
* Single external dependency (pyaes, that is Pure-Python)
* Python 3.x support


Performance
-----------

There is a test case provided in _/tests/test-aes.py_ which does some basic performance testing (its primary purpose is moreso as a regression test).

Based on that test, in **CPython**, this library is about 30x slower than [PyCrypto](https://www.dlitz.net/software/pycrypto/) for CBC, ECB and OFB; about 80x slower for CFB; and 300x slower for CTR.

Based on that same test, in **Pypy**, this library is about 4x slower than [PyCrypto](https://www.dlitz.net/software/pycrypto/) for CBC, ECB and OFB; about 12x slower for CFB; and 19x slower for CTR.

The PyCrypto documentation makes reference to the counter call being responsible for the speed problems of the counter (CTR) mode of operation, which is why they use a specially optimized counter. I will investigate this problem further in the future.


FAQ
---

#### Why do this?

The short answer, *it's for a school thing.*

The longer answer,  it's for a school thing and it seemed like a cool thing to do :)
