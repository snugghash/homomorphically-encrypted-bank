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
- 1730: Kafka's broken without specifically installing things.
- 1746; tip: that `bc` missing error? That breaks zookeeper, prevents it from running. EIther way, kafka is a add-on for me, not par tof MVP. Focusing on spark.
- 1750; tip: Use different keys and sec groups for all clusters so we can work with the parallely.
- 1920; Depending upon parameters of encryption, there's a certain noise budget associated with each ciphertext. Each comupation reduces it, addition is negligible compared to multiplication. Once used up, the ciphertexts then become undecryptable, they're garbage.
- 1922; idea; implement private set intersection as a continuous stream for drivers on freeway, no one knows their whereabouts except the people who match with then, then they send over an E2E profile, they accept/deny, then they pick up along route. Talk with the guy implementing the other part.
20190130
- 0900; TODO PRs to PySEAL to print noise budgets in beginning, fix some typos.
- 1018; No luck getting spark to accept a job
- 1118; "There is no such a thing as a temporary change or workaround: In most cases, workarounds are tech debt."
- 1200; Done with rebuilding ingestion, possibly direct to spark as a batch this time.
20190131
- 0908; Switching to ETH blockchain to simulate transaction as the protocol has an address-transaction model as opposed to BTC's address-changes-every-transaction privacy model.
20190201
- 1107; AWS lambda fn for HE? But no parallelization, no joy.
- 1850; Three TODOs - Implement Big Poly Array, conversion from ciphertext to it, then the addition. Interprocess communication/savings = nil.
20190204
- 1339: Reasons to use Kafka+Spark: good integrations and docuemntation, support present
20190206
- 1548; Kafka consumer - timing out when connecting to kafka. Is 9092 the default port?
