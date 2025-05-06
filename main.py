import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print ("Conectado ao servidor Urban Routes")
        else:
            print ("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        print("Função criada para definir a rota")
        pass
        # Adicionar em S8
    def test_select_plan(self):
        print("Função criada para definir o plano")
        pass
        # Adicionar em S8
    def test_fill_phone_number(self):
        print("Função criada para definir o número de telefone")
        pass
        # Adicionar em S8
    def test_fill_card(self):
        print("Função criada para definir o cartão")
        pass
        # Adicionar em S8
    def test_comment_for_driver(self):
        print("Função criada para definir o motorista")
        pass
        # Adicionar em S8
    def test_order_blanket_and_handkerchiefs(self):
        print("Função criada para solicitar blanket e handkerchiefs")
        pass
        # Adicionar em S8
    def test_order_2_ice_creams(self):
        for _ in range(2):
            print("Função criada para solicitar 2(dois) sorvetes")
        pass
        # Adicionar em S8
    def test_car_search_model_appears(self):
        print("Função criada para definir o modelo do carro")
        pass
        # Adicionar em S8
