import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print ("Conectado ao servidor Urban Routes")
        else:
            print ("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(3)

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        from_address = data.ADDRESS_FROM
        to_address = data.ADDRESS_TO
        urban_routes_page.set_destiny(from_address, to_address)
        assert urban_routes_page.get_from() == from_address
        assert urban_routes_page.get_to() == to_address

    def test_select_plan(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.select_call_taxi()
        time.sleep(1)
        urban_routes_page.select_comfort_car()
        time.sleep(3)
        print("Plano retornado:", urban_routes_page.check_if_tariff_is_active())
        assert urban_routes_page.check_if_tariff_is_active() == 'Comfort'
        print("Função criada para definir o plano")


    def test_fill_phone_number(self):
        print("Função criada para definir o número de telefone")
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_phone_number_camp()
        time.sleep(1)
        urban_routes_page.insert_phone_number_and_next(data.PHONE_NUMBER)
        urban_routes_page.phone_code_sms()

        #urban_routes_page.phone_code_sms()

    def test_fill_card(self):
        print("Função criada para definir o cartão")
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.add_credit_card()
        time.sleep(1)

    def test_comment_for_driver(self):
        print("Função criada para definir o motorista")
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.message_to_driver()
        assert urban_routes_page.get_message_for_driver() == 'Pare no bar de sucos'

    def test_order_blanket_and_handkerchiefs(self):
        print("Função criada para solicitar blanket e handkerchiefs")
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.blanket_and_handkerchiefs_option()
        assert urban_routes_page.blanket_and_handkerchiefs_selected()

    def test_order_2_ice_creams(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.order_ice_creams()
        time.sleep(2)