class Sauce:
    def __init__(self, flavor, additive=None):
        self.flavor = flavor
        self.additive = additive

    def show_my_sauce(self):
        if self.additive:
            print(f"Соус {self.flavor} с {self.additive}")
        else:
            print("Майонез")


class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus

    def get_total_salary(self):
        return self.__salary + self.__bonus


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print("Ингредиенты для приготовления блюда:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def cook(self):
        print(f"Рецепт: {self.name}")
        print("Блюдо готово!")