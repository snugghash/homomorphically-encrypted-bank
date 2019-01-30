20190122 
- 1630; Testing out the speed of the C library HELib.
- 1704; Tested out SEAL, fastest is CKKS with 
    Average add: 972 microseconds
    Average multiply: 5951 microseconds
  at 16384 poly modulus degree.
- 1800; HELib was a pain to install with many C++ libraries, but also doesn't have much in the way of dev support. The examples they have are hard but offer no statistical result. Have to implement main programs and link with this using `make`.
20190123
- 0603; [GPGPU accelerated partially homom](https://github.com/vernamlab/cuHE). Perhaps we can build THIS out for the latest CKKS, on for use on edge GPUs or Paperspace or AWS GPUs.
20190124
- Wrote python script to retrive XBT blockchain data from BigQuery, to be converted to Kafka producer. Skipping S3 storage, as BigQuery just as reliable as S3.
- Found PySEAL.
20190126
- Lost the producer and several days to hard disk failure. Rewrote, more modular now.
20190129
- 1200; Testing [PySEAL](https://github.com/Lab41/PySEAL) locally.
- 1600; Spark+Kafka worked on Friday, seems like the tear down process and using new VPC+SG screwed up something. Debugging communication for both services.


