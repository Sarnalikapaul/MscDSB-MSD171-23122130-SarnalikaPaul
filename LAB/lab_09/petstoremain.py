from petstore import PetStore

def admin_menu(pet_store):
    while True:
        print("\nAdmin Menu:")
        print("1. Store a new pet")
        print("2. Search for a pet")
        print("3. Sell a pet")
        print("4. List all pets")
        print("5. Back to Main Menu")

        admin_choice = input("Select an option (1/2/3/4/5): ")

        if admin_choice == "1":
            name = input("Enter pet name: ")
            species = input("Enter species: ")
            age = input("Enter age: ")
            price = input("Enter price: ")
            pet_store.store_pet(name, species, age, price)
            print(f"{name} has been added to the inventory.")

        elif admin_choice == "2":
            name = input("Enter the pet name to search: ")
            pet_details = pet_store.search_pet(name)
            if pet_details:
                print(f"Details of {name}: {pet_details}")
            else:
                print(f"{name} is not found in the inventory.")

        elif admin_choice == "3":
            name = input("Enter the pet name to sell: ")
            if pet_store.sell_pet(name):
                print(f"{name} has been sold.")
            else:
                print(f"{name} is not found in the inventory.")

        elif admin_choice == "4":
            print("List of all pets in the inventory:")
            pets = pet_store.list_pets()
            for pet, details in pets.items():
                print(f"{pet}: {details}")

        elif admin_choice == "5":
            break

def user_menu(pet_store):
    while True:
        print("\nUser Menu:")
        print("1. List all pets")
        print("2. Buy a pet")
        print("3. Back to Main Menu")

        user_choice = input("Select an option (1/2/3): ")

        if user_choice == "1":
            print("List of all pets in the inventory:")
            pets = pet_store.list_pets()
            pet_found = False
            for pet, details in pets.items():
                print(f"{pet}: {details}")
                pet_found = True
            if not pet_found:
                print("No pets are currently available in the inventory.")

        elif user_choice == "2":
            name = input("Enter the name of the pet you want to buy: ")
            if pet_store.sell_pet(name):
                print(f"Congratulations! You've bought {name}.")
            else:
                print(f"{name} is not found in the inventory.")

        elif user_choice == "3":
            break

def main():
    pet_store = PetStore()

    while True:
        print("\nPet Store Menu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            admin_menu(pet_store)
        elif choice == "2":
            user_menu(pet_store)
        elif choice == "3":
            print("Exiting the Pet Store. Thank you!")
            break

if __name__ == "__main__":
    main()
