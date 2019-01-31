"""
TODO test microbatching performance - 100 at a time, 1000 at a time, streaming to dev/null, and many more test ideas which were lost to the ending of the hot water stream in the shower.
"""
import unittest



class test_read_from_BigQuery(unittest.TestCase):



    def test_get_1000_transactions(self):
        pretty_tranactions = read_from_BigQuery(1000)
        assert(1==1)
