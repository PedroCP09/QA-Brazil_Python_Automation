class Cake:
    recipe_type = "Bolo básico"
    baking_temperature = 180
    baking_time = 30

    def __init__(self, flour, sugar, milk, eggs):
        self.cake_flour = flour
        self.cake_sugar = sugar
        self.cake_milk = milk
        self.cake_eggs = eggs

    # Adiciona um enfeite ao bolo
    def decorate(self, topping):
        print(f"Adicionando {topping} à parte de cima do bolo de {self.cake_flour} para fins de decoração.")

bolo_de_laranja = Cake("laranja", "100g", "200ml", 4)
bolo_de_chocolate = Cake("chocolate", "100g", "200ml", 4)
bolo_de_chocolate.decorate("granulado")



class User():
    is_registered = True

    def __init__(self, name, login):
        self.user_name = name
        self.user_login = login

    def describe(self):
        return f'Nome: {self.user_name}, login {self.user_login}'


class Group():
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, user):
        if user not in self.members:
            print(f'Uma nova pessoa foi adicionada ao grupo {self.name}')
            self.members.append(user)

    def print_member_descriptions(self):  # O método exibe as informações de todos os integrantes do grupo
        print(f"Informações sobre integrantes do grupo {self.name}:")
        for member in self.members:
            print(member.describe())

    def is_user_in_group(self, user):
        if user in self.members:
            print(f'{user.user_name} está no grupo')

user1 = User('Marcos', 'supermarcos94')
group1 = Group('Eu adoro cachorros')
group1.add_member(user1)
group1.is_user_in_group(user1)