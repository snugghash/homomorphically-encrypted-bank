"""
Homomorphic encryption implemented by using existing PySEAL. Horizontal scaling. 

Sources: Spark quickstart
https://www.rittmanmead.com/blog/2017/01/getting-started-with-spark-streaming-with-python-and-kafka/
"""
from pyspark.sql import SparkSession
# SparkSession is newer, recommended API over SparkContext
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from kafka_consumer import kafka_consumer_gen
import seal
from seal import ChooserEvaluator, \
	Ciphertext, \
	Decryptor, \
	Encryptor, \
	EncryptionParameters, \
	Evaluator, \
	IntegerEncoder, \
	FractionalEncoder, \
	KeyGenerator, \
	MemoryPoolHandle, \
	Plaintext, \
	SEALContext, \
	EvaluationKeys, \
	GaloisKeys, \
	PolyCRTBuilder, \
	ChooserEncoder, \
	ChooserEvaluator, \
	ChooserPoly


# Streaming test
sc = SparkContext(appName="simply_parallel_HE")
sc.setLogLevel("WARN")

ssc = StreamingContext(sc, 10)
kafkaStream = KafkaUtils.createStream(ssc, 'ec2-52-11-165-61.us-west-2.compute.amazonaws.com:2181', 'spark-streaming', {'eth-old':1})

#parsed = kafkaStream.map(lambda datapoint: dict(datapoint))
kafkaStream..pprint()

ssc.start()
ssc.awaitTermination()


parms = EncryptionParameters()
parms.set_poly_modulus("1x^2048 + 1")
parms.set_coeff_modulus(seal.coeff_modulus_128(2048))

parms.set_plain_modulus(1 << 8)

context = SEALContext(parms)

print_parameters(context);
# Here we choose to create an IntegerEncoder with base b=2.
encoder = IntegerEncoder(context.plain_modulus())

# To create a fresh pair of keys one can call KeyGenerator::generate() at any time.
keygen = KeyGenerator(context)
public_key = keygen.public_key()
secret_key = keygen.secret_key()

encryptor = Encryptor(context, public_key)

# Computations on the ciphertexts are performed with the Evaluator class.
evaluator = Evaluator(context)

decryptor = Decryptor(context, secret_key)

value1 = 5;
plain1 = encoder.encode(value1);
print("Encoded " + (str)(value1) + " as polynomial " + plain1.to_string() + " (plain1)")

value2 = -7;
plain2 = encoder.encode(value2);
print("Encoded " + (str)(value2) + " as polynomial " + plain2.to_string() + " (plain2)")

# Encrypting the values is easy.
encrypted1 = Ciphertext()
encrypted2 = Ciphertext()
print("Encrypting plain1: ")
encryptor.encrypt(plain1, encrypted1)
print("Done (encrypted1)")

print("Encrypting plain2: ")
encryptor.encrypt(plain2, encrypted2)
print("Done (encrypted2)")

# To illustrate the concept of noise budget, we print the budgets in the fresh
# encryptions.
print("Noise budget in encrypted1: " + (str)(decryptor.invariant_noise_budget(encrypted1)) + " bits")
print("Noise budget in encrypted2: " + (str)(decryptor.invariant_noise_budget(encrypted2)) + " bits")

# As a simple example, we compute (-encrypted1 + encrypted2) * encrypted2.

# Negation is a unary operation.
evaluator.negate(encrypted1)

# Negation does not consume any noise budget.
print("Noise budget in -encrypted1: " + (str)(decryptor.invariant_noise_budget(encrypted1)) + " bits")

evaluator.add(encrypted1, encrypted2)

print("Noise budget in -encrypted1 + encrypted2: " + (str)(decryptor.invariant_noise_budget(encrypted1)) + " bits")

evaluator.multiply(encrypted1, encrypted2)

print("Noise budget in (-encrypted1 + encrypted2) * encrypted2: " + (str)(decryptor.invariant_noise_budget(encrypted1)) + " bits")

# Now we decrypt and decode our result.
plain_result = Plaintext()
print("Decrypting result: ")
decryptor.decrypt(encrypted1, plain_result)
print("Done")

# Print the result plaintext polynomial.
print("Plaintext polynomial: " + plain_result.to_string())

# Decode to obtain an integer result.
print("Decoded integer: " + (str)(encoder.decode_int32(plain_result)))
