class petStore:
    def __init__(self):
        self.pet_Dict={"details":[]}
    
    def storePetDetails(self,id,species,comName,age,price):
        sub_pet_Dict={"id":id,"species":species,"comName":comName,"age":age,"price":price}
        self.pet_Dict["details"].append(sub_pet_Dict)
        print("Pet stored successfully!")
    
    def searchPet(self,comName):
        flag=0
        for i in self.pet_Dict["details"]:
            if i["comName"]==comName:
                print("ID:",i["id"])
                print("Species:",i["species"])
                print("Common Name:",i["comName"])
                print("Age:",i["age"])
                print("Price:",i["price"])
                flag=1
        if flag==0:
            print("Pet is not available")

    def sellPet(self,id):
        for i in range(0,len(self.pet_Dict["details"])):
            if self.pet_Dict["details"][i]["id"]==id:
                del self.pet_Dict["details"][i]
    def listAllPet(self):
        for i in self.pet_Dict["details"]:
            print("ID:",i["id"])
            print("Species:",i["species"])
            print("Common Name:",i["comName"])
            print("Age:",i["age"])
            print("Price:",i["price"])
    