"""
TODO test microbatching performance - 100 at a time, 1000 at a time, streaming to dev/null, and many more test ideas which were lost to the ending of the hot water stream in the shower.
"""
import unittest
from read_from_BigQuery import get_data_from_big_query
from pprint import pprint
import timeit
import warnings



def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)
    return do_test



class test_read_from_BigQuery(unittest.TestCase):
    """
    Tests to verify that the reading from BigQuery is performant
    """
    def test_get_1000_transactions(self):
        start = timeit.default_timer()
        get_data_from_big_query(1000000,1000)
        print("10**3 elapsed ", timeit.default_timer() - start)
        assert(1==1)



    @ignore_warnings
    def test_get_100k_transactions(self):
        """
        Resource warning solved https://stackoverflow.com/a/26620811/
        """
        start = timeit.default_timer()
        get_data_from_big_query(0,10**5)
        elapsed = timeit.default_timer() - start
        print("10**5 elapsed ", elapsed)
        assert(elapsed < 12)


    @ignore_warnings
    def test_get_1m_trans(self):
        start = timeit.default_timer()
        get_data_from_big_query(0,10**6)
        elapsed = timeit.default_timer() - start
        print("10**5 elapsed ", elapsed)
        assert(elapsed < 95)



class test_experiments_IO(unittest.TestCase):
    def test_compare_linebyline_vs_microbatch(self):
        """
        Write a test to compare applying fns on every line (reading, writing, reformatting) vs. as a stream of microbatches.
        """
        pass
