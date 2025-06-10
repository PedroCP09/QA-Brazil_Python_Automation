import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code
import data

class UrbanRoutesPage:
    #DE e PARA
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    #SELECIONAR O TAXI
    CALL_TAXI_BUTTON = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button')
    #TIPO COMFORT
    COMFORT_CAR_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]')
    COMFORT_CARD_ACTIVE = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    #ACRESCENTAR TELEFONE, CLICAR NO CÓDIGO SMS E CONFIRMAR
    BUTTON_PHONE_NUMBER = (By. XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div') #1ª etapa - logo após selecionar "Comfort"
    PHONE_NUMBER_CLICK = (By.CSS_SELECTOR, '#phone')#2ª etapa +clicar e inserir número de tel
    CLICK_NEXT_BUTTON = (By. XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button') #3ª etapa ok
    INSERT_CODE_BUTTON = (By. XPATH, '//*[@id="code"]')
    CONFIRM_SMS_BUTTON = (By. XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    #ADICIONAR MÉTODO DE PAGAMENTO COMPLETO (NÚMERO, CÓDIGO E FECHAR ABA)
    CLICK_PAYMENT_METHOD = (By. XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]') #Start def nº8 in order
    CLICK_ADD_CARD = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]')
    INSERT_CARD_NUMBER = (By.XPATH, '//*[@id="number"]')
    INSERT_CARD_CVV = (By.CSS_SELECTOR, 'input[name="code"]')
    BUTTON_ADD_CARD = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    #ENVIAR MENSAGEM PARA O MOTORISTA E FECHAR ABA
    SEND_TEXT_DRIVER = (By.XPATH, '//*[@id="comment"]')
    CLOSE_CARD_WINDOW = (By. XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    #SELECIONAR TRAVESSEIRO E LENÇOS E VERIFICAR A SELEÇÃO
    SELECT_BLANKET_HANDKERCHIEFS = (By.CLASS_NAME, "switch-input")
    SWITCH_BLANKET_HANDKERCHIEFS = (By.CLASS_NAME, "switch")
    SWITCHES_OPTION = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input')
    #ICE CREAMS
    ORDER_REQUIREMENTS = (By.XPATH, '// *[ @ id = "root"] / div / div[3] / div[3] / div[2] / div[2] / div[4] / div[1] / div[1]')
    SELECT_ICE_CREAMS = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    COUNTER_ICE_CREAM_2 = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    #PEDIR TAXI
    SELECT_ORDER_TAXI = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')
    WINDOW_ORDER = (By.CLASS_NAME, '//*[@id="root"]/div/div[5]/div[2]')
    DRIVER_NAME = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]')
    DRIVER_TIME = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[2]')
    DRIVER_RATING = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/div')
    CANCEL_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[2]/button')
    IMG_DRIVER= (By. XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/img')


    def __init__(self, driver):
        self.driver = driver

    def wait_for_ec(self, locator):
        WebDriverWait(self.driver, 45).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def set_from_locator(self, from_address):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_address)

    def set_to_locator(self, to_address)   :
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_address)

    def get_from(self):
        return self.wait_for_ec(self.FROM_LOCATOR).get_property('value')

    def get_to(self):
        return self.wait_for_ec(self.TO_LOCATOR).get_property('value')

    def select_taxi(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def set_destiny(self, from_address, to_address):
        self.set_from_locator(from_address)
        self.set_to_locator(to_address)

    def select_call_taxi(self):
        self.wait_for_ec(self.CALL_TAXI_BUTTON).click()

    def select_comfort_car(self):
        time.sleep(2)
        self.wait_for_ec(self.COMFORT_CAR_BUTTON).click()
        return self.check_if_tariff_is_active()

    def taxi_and_comfort_steps(self):
        self.wait_for_ec(self.CALL_TAXI_BUTTON).click()
        self.wait_for_ec(self.COMFORT_CAR_BUTTON).click()

    def check_if_tariff_is_active(self):
        return self.wait_for_ec(self.COMFORT_CARD_ACTIVE).text

    def click_phone_number_camp(self):
        self.wait_for_ec(self.BUTTON_PHONE_NUMBER).click()
        time.sleep(2)

    def insert_phone_number_and_next(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_CLICK)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PHONE_NUMBER_CLICK))
        self.driver.find_element(*self.PHONE_NUMBER_CLICK).send_keys(phone_number)
        self.driver.find_element(*self.CLICK_NEXT_BUTTON).click()

    def phone_code_sms(self):
        code = retrieve_phone_code(self.driver)
        self.wait_for_ec(self.INSERT_CODE_BUTTON).send_keys(code)
        self.wait_for_ec(self.CONFIRM_SMS_BUTTON).click()

    def add_credit_card(self):
        self.wait_for_ec(self.CLICK_PAYMENT_METHOD).click()
        self.wait_for_ec(self.CLICK_ADD_CARD).click()
        time.sleep(1)
        self.wait_for_ec(self.INSERT_CARD_NUMBER).send_keys(data.CARD_NUMBER)
        time.sleep(1)
        self.wait_for_ec(self.INSERT_CARD_CVV).click()
        time.sleep(1)
        self.wait_for_ec(self.INSERT_CARD_CVV).send_keys(data.CARD_CODE)
        time.sleep(1)
        self.wait_for_ec(self.BUTTON_ADD_CARD).click()
        self.wait_for_ec(self.CLOSE_CARD_WINDOW).click()

    def message_to_driver(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'overlay')))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SEND_TEXT_DRIVER)).send_keys(
                data.MESSAGE_FOR_DRIVER)

    def get_message_for_driver(self):
        return self.wait_for_ec(self.SEND_TEXT_DRIVER).get_property('value')

    def blanket_and_handkerchiefs_option(self):
        switches = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.SWITCH_BLANKET_HANDKERCHIEFS)
        )
        switches[0].click()
        self.blanket_and_handkerchiefs_selected()

    def blanket_and_handkerchiefs_selected(self):
        switches = WebDriverWait(self.driver, 5).until(
        EC.presence_of_all_elements_located(self.SELECT_BLANKET_HANDKERCHIEFS))
        return switches[0].get_property('checked')

    def wait_for_ec_all(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(locator))

    def order_ice_creams(self):
        self.wait_for_ec(self.SELECT_ICE_CREAMS).click()
        time.sleep(2)
        self.wait_for_ec(self.SELECT_ICE_CREAMS).click()

    def order_car(self):
        self.wait_for_ec(self.SELECT_ORDER_TAXI).click()

    def wait_info_popup(self):
        WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'overlay'))
        )
        pass
        self.wait_for_ec(self.DRIVER_RATING)
        self.wait_for_ec(self.IMG_DRIVER)
        self.wait_for_ec(self.DRIVER_NAME)

    def get_popup_info(self):
        rating = self.wait_for_ec(self.DRIVER_RATING).text
        image = self.wait_for_ec(self.IMG_DRIVER).get_property('src')
        name = self.wait_for_ec(self.DRIVER_NAME).text
        return name, rating, image





