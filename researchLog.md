20190122 
- 1630; Testing out the speed of the C library HELib.
- 1704; Tested out SEAL, fastest is CKKS with 
    Average add: 972 microseconds
    Average multiply: 5951 microseconds
  at 16384 poly modulus degree.
- 1800; HELib was a pain to install with many C++ libraries, but also doesn't have much in the way of dev support. The examples they have are hard but offer no statistical result. Have to implement main programs and link with this using `make`.
20190123
- 0603; [GPGPU accelerated partially homom](https://github.com/vernamlab/cuHE). Perhaps we can build THIS out for the latest CKKS, on for use on edge GPUs or Paperspace or AWS GPUs.

