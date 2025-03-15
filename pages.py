from selenium.webdriver.common.by import By
from helpers import retrieve_phone_code



class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON = (By.XPATH, '//button[@class= "button round"]')
    SUPPORTIVE_ICON_LOCATOR = (By. XPATH, '// div[contains(@class, "tcard")][5]')
    ASSERT_SUPPORT_TITLE = (By.XPATH, '(//div[@class="tcard-title"])[5]')
    PHONE_NUMBER_BOX = (By.XPATH, '//div[@class="np-button"]')
    PHONE_NUMBER_INPUT = (By.ID, 'phone')
    PHONE_BUTTON = (By.XPATH, '(//button[@class="button full"])[1]')
    SMS_CODE_LOCATOR = (By.ID, 'code')
    SMS_BUTTON = (By.XPATH, '(//button[@class="button full"])[2]')
    PHONE_NUMBER_BOX_ASSERT = (By.XPATH, '//div[@class="np-text"]')
    CREDIT_CARD_LOCATOR = (By.XPATH, '//div[@class="pp-button filled"]')
    CREDIT_CARD_OPTION = (By.XPATH, '//div[@class="pp-row disabled"]')
    CREDIT_CARD_NUMBER = (By.ID, 'number')
    CREDIT_CARD_CODE = (By.XPATH, '(//input[@class="card-input"])[2]')
    CARD_OUTSIDE_BOX = (By.XPATH, '//div[@class="card-wrapper"]')
    CARD_LINK_BUTTON = (By.XPATH, '(//button[@class="button full"])[4]')
    ASSERT_CARD = (By.ID, 'card-1')
    COMMENT_FOR_DRIVER = (By.ID, 'comment')
    ASSERT_COMMENT = (By.XPATH, '(//input[@class="input"])[5]')
    BLANKET_HANDKERCHIEFS_ON = (By.XPATH, '//div[@class="r-sw"]')
    ICE_CREAM_COUNTER = (By.XPATH, '//div[@class="counter-plus"]')
    SMART_BUTTON_TO_BOOK = (By.XPATH, '//button[@class="smart-button"]')
    BLANKET_HANDKERCHIEFS_CHECK = (By.XPATH, '//input[@class="switch-input"]')
    ASSERT_ICE_CREAM = (By.XPATH, '//div[@class="counter-value"]')
    ASSERT_ORDER = (By.XPATH, '//div[@class="order-header-title"]')



    def set_addresses(self, from_address, to_address):
        #This is setting the address in the beginning
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_address)
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_address)
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def selecting_supportive_plan(self):
        #This selects the supportive car option
        self.driver.find_element(*self.SUPPORTIVE_ICON_LOCATOR).click()

    def filling_in_the_phone_number(self, phone_number):
        #Filling in the phone number inbox
        self.driver.find_element(*self.PHONE_NUMBER_BOX).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone_number)
        self.driver.find_element(*self.PHONE_BUTTON).click()
        self.driver.find_element(*self.SMS_CODE_LOCATOR).send_keys(retrieve_phone_code(self.driver))
        self.driver.find_element(*self.SMS_BUTTON).click()

    def adding_a_credit_card(self, card_number, card_code):
        #This sequence adds an credit card
        self.driver.find_element(*self.CREDIT_CARD_LOCATOR).click()
        self.driver.find_element(*self.CREDIT_CARD_OPTION).click()
        self.driver.find_element(*self.CREDIT_CARD_NUMBER).send_keys(card_number)
        self.driver.find_element(*self.CREDIT_CARD_CODE).send_keys(card_code)
        self.driver.find_element(*self.CARD_OUTSIDE_BOX).click()
        self.driver.find_element(*self.CARD_LINK_BUTTON).click()

    def writing_a_comment_for_the_driver(self, message_for_driver):
        #This code creates a comment for the driver
        self.driver.find_element(*self.COMMENT_FOR_DRIVER).send_keys(message_for_driver)

    def assert_comment_driver(self):
        return self.driver.find_element(*self.ASSERT_COMMENT).get_attribute("value")


    def ordering_blanket_and_handkerchiefs(self):
        #ordering the blanket and handkerchiefs
        self.driver.find_element(*self.BLANKET_HANDKERCHIEFS_ON).click()

    def blanket_handkerchiefs_check(self):
        return self.driver.find_element(*self.BLANKET_HANDKERCHIEFS_CHECK).get_property("checked")


    def ordering_ice_cream(self):
        #orderes ice cream
        self.driver.find_element(*self.ICE_CREAM_COUNTER).click()
        self.driver.find_element(*self.ICE_CREAM_COUNTER).click()

    def assert_ice_cream(self):
        return self.driver.find_element(*self.ASSERT_ICE_CREAM).text


    def booking_taxi(self):
        #booking taxi
        self.driver.find_element(*self.SMART_BUTTON_TO_BOOK).click()

    def asserting_supportive(self):
        #asserting the support option
        return self.driver.find_element(*self.ASSERT_SUPPORT_TITLE).text

    def assert_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_BOX_ASSERT).text

    def assert_card(self):
        return self.driver.find_element(*self.ASSERT_CARD).get_property("checked")

    def assert_taxi_order(self):
        return self.driver.find_element(*self.ASSERT_ORDER).text





