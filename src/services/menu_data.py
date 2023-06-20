from models.dish import Dish
from models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.open_csv_file(source_path)

    def open_csv_file(self, source_path):
        with open(source_path, mode="r") as file:
            csv_file = csv.DictReader(file)
            dishes = []
            add_dish = ""
            for data_dishes in csv_file:
                if add_dish != data_dishes["dish"]:
                    add_dish = data_dishes["dish"]
                    new_dish = Dish(
                        data_dishes["dish"], float(data_dishes["price"])
                    )
                    new_dish.add_ingredient_dependency(
                        Ingredient(data_dishes["ingredient"]),
                        int(data_dishes["recipe_amount"]),
                    )
                    dishes.append(new_dish)
                if add_dish == data_dishes["dish"]:
                    dishes[-1].add_ingredient_dependency(
                        Ingredient(data_dishes["ingredient"]),
                        int(data_dishes["recipe_amount"]),
                    )
            for dish_dependency in dishes:
                self.dishes.add(dish_dependency)
