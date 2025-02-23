class IceCreamMachine:
    def _init_(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        # If either ingredients or toppings are empty, return an empty list
        if not self.ingredients or not self.toppings:
            return []
        
        # Generate all combinations of ingredients and toppings
        return [[ingredient, topping] for ingredient in self.ingredients for topping in self.toppings]

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops())  # Should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]