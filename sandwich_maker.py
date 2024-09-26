class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        out_of_stock=""
        for ingredient, amount in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < amount:
                out_of_stock += ingredient.capitalize() + ','
        return out_of_stock[0:-2] if out_of_stock else False

    def make_sandwich(self, order_ingredients):
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount