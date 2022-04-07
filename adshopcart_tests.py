import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods

class MoodleAppPositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest that this is a function inside class (vs @classmethod)
    def test_create_new_user(): # test_ in the name is mandatory
        methods.setUp()
        methods.signup()
        methods.check_full_name()
        methods.check_orders()
        methods.log_out()
        methods.log_in()
        methods.delete_test_account()
        methods.verify_account_deleted()
        methods.check_home_page()
        methods.tearDown()
