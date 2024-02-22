#/usr/bin/env python

class CoffeeMachine:
    def init(self):
        self.coffees = {
            'Латте': 3.50,
            'Капучино': 3.00,
            'Американо': 2.50,
            'Эспрессо': 2.00
        }

    def display_menu(self):
        print("Меню кофе:")
        for coffee, price in self.coffees.items():
            print(f"{coffee}: ${price}")

    def make_coffee(self, choice):
        if choice in self.coffees:
            print(f"Готовим {choice}... Ваш кофе готов! Пожалуйста, внесите оплату: ${self.coffees[choice]}")
        else:
            print("Извините, выбранного кофе нет в нашем ассортименте.")

if name == "main":
    machine = CoffeeMachine()
    machine.display_menu()
    choice = input("Выберите вид кофе: ")
    machine.make_coffee(choice)