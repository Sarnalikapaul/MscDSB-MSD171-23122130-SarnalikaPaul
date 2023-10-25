class sportMart:
    def __init__(self):
        self.inventory={}
        self.orders={}

    def createorder(self,orderid,itemName,item_quantity,customer_name,customer_phonenumber,productId):
        temp={
           
        "orderid": orderid,
         "itemname":itemName,
         "item_quantity":item_quantity,
         "customer_name":customer_name,
         "customer_phone number":customer_phonenumber,
         "productId":productId
    
          }
        self.orders[orderid] = temp
    def createInventoryItem(self,ProductId,Productname,Quantity,Price):
        temp={
            "productid":ProductId,
            "productnamr":Productname,
            "quantity":Quantity,
            "price":Price

        }
        self.inventory[ProductId]=temp
    def printOrders(self):
        print(self.orders)
    def printInventory(self):
        print(self.inventory)


trinity= sportMart()
orders=open("orders.csv","r")
orders_header=orders.readline()
orders_orders=orders.readline()
for item in orders_orders:
    temp=item.strip().split(',')
    trinity.createorder(temp[0],temp[1],temp[2],temp[3],temp[4])

trinity.printOrders()
def menu():
    print("1.create new order ")
    print("2.update the inventory")
    print("3.print orders")
    print("4.print inventory")
    print("5.quit")
    print()

while True:
    menu()

    option = int(input("Enter an option"))

    if option ==1:
      orderid = input("enter the orderid: ")
      ItemName =input("enter item name: ")
      Quantity =int(input("enter item quantity: "))
      customer_name=input("enter name: ")
      customer_phonenumber=input("enter phone number: ")
      productId=input("enter product id: ")
      trinity.createorder(orderid,ItemName,Quantity,customer_name,productId)

    elif option==2:
      
      price=input("enter the price: ")
      ItemName=input("enter the item name: ")
      trinity.createInventoryItem(price,ItemName)

    elif option == 3:
        trinity.printOrders()

    elif option ==4:
        trinity.printInventory()

    else:
        
        break



    



    
   
    
