import time

from selenium import webdriver
import data
import helpers
import pages


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
                print("Connected to the Urban Routes server")
        else:
                print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        #setting the address DONE
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        actual_value = data.ADDRESS_FROM
        actual_value_1 = data.ADDRESS_TO
        expected_value = "East 2nd Street, 601"
        expected_value_1 = "1300 1st St"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        assert expected_value_1 in actual_value_1, f"Expected '{expected_value_1}', but got '{actual_value_1}'"

    def test_select_plan(self):
        #selecting the plan DONE
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.selecting_supportive_plan()
        actual_value = page.asserting_supportive()
        expected_value = "Supportive"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"



    def test_fill_phone_number(self):
        #entering and verifying the phone number DONE
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.selecting_supportive_plan()
        page.filling_in_the_phone_number(data.PHONE_NUMBER)
        actual_value = page.assert_phone_number()
        expected_value = "+1 123 123 12 12"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_fill_card(self):
        #entering card info DONE
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.adding_a_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        assert page.assert_card()

    def test_comment_for_driver(self):
        #leaving a comment for the driver DONE
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.writing_a_comment_for_the_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        actual_value = page.assert_comment_driver()
        expected_value = "Stop at the juice bar, please"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_order_blanket_and_handkerchiefs(self):
        #verifiying the slide works DONE
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.selecting_supportive_plan()
        page.ordering_blanket_and_handkerchiefs()
        assert page.blanket_handkerchiefs_check()

    def test_order_2_ice_creams(self):
        #verifying that 2 ice creams are chosen DONE
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.selecting_supportive_plan()
        page.ordering_ice_cream()
        actual_value = page.assert_ice_cream()
        expected_value = "2"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"


    def test_car_search_model_appears(self):
        #verifying that the car search is activated DONE
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.set_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.selecting_supportive_plan()
        page.writing_a_comment_for_the_driver(data.MESSAGE_FOR_DRIVER)
        page.booking_taxi()
        actual_value = page.assert_taxi_order()
        expected_value = "Car search"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"



# ✅ Ensure this code is OUTSIDE the class (after its definition)
if __name__ == "__main__":
    test = TestUrbanRoutes()  # Create an instance of the class
    test.test_set_route()
    test.test_select_plan()
    test.test_fill_phone_number()
    test.test_fill_card()
    test.test_comment_for_driver()
    test.test_order_blanket_and_handkerchiefs()
    test.test_order_2_ice_creams()

@classmethod
def teardown_class(cls):
    cls.driver.quit()
