import unittest
import connecttoapi


class ConnectoapiTest(unittest.TestCase):
    def setUp(self):
        self.connect = connecttoapi.fetchdata_giosg_api()


def main():
    """ Run all tests in this file.
    """
    fetchdata_giosg_api_test1()
    fetchdata_giosg_api_test2()


def fetchdata_giosg_api_test1():
    #testing for dates
    start_date = '2017-05-05'
    assert(start_date)


def fetchdata_giosg_api_test2():
    #testing for dates
    end_date = '2017-05-14'
    assert(end_date)


if __name__ == "__main__":
    main()
    print("All test passed.")
    pass
