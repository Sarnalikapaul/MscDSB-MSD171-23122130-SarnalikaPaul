class PetStore:
    def __init__(self):
        self.pet_inventory = {}

    def store_pet(self, name, species, age, price):
        pet_details = {"Species": species, "Age": age, "Price": price}
        self.pet_inventory[name] = pet_details

    def search_pet(self, name):
        return self.pet_inventory.get(name, None)

    def sell_pet(self, name):
        if name in self.pet_inventory:
            del self.pet_inventory[name]
            return True
        else:
            return False

    def list_pets(self):
        return self.pet_inventory
