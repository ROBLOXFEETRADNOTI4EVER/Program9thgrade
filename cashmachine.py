from time import sleep
import random
#tomroow i must add an edit option so i can edit prices and change name of the product and remove function aswell
money_spent_by_npc = 0

def eneringproducts():
    global buyingdata
    global money_spent_by_npc
    buyingdata = {'Test': {'quantity': 3300, 'price': 0.99}}
    eneterdetails = True
    while eneterdetails:
        details = input(f"(Income {money_spent_by_npc}) Press A to List a product, B To wiew Stock, C To Sell, Q to quit:").upper()
        if details == 'A':
            product = input("Enter Product: ")

            while True:
                quantity = input("Enter a quantity: ")
                if quantity.isdigit():
                    quantity = int(quantity)
                    break
                else:
                    print("invaild input quanity must be a number (exmaple 3, 4, 6, 19)Please try again Thanks.")
            while True:
                eachprice = input(f"Enter a price for 1 single unit of the {product}: ")
                try:
                    eachprice = float(eachprice)
                    break
                except ValueError:
                    print("invalid input price must be a valid number (example 2, 3, 6, 8, 3835)")
            #storing the data inside the {} buyingdata
            buyingdata[product] = {'quantity': quantity, 'price': eachprice}
            print(f"You entered : {product} with the quanitity {quantity}, and with unit price of {eachprice}: ")

        elif details == 'B':
            if not buyingdata: #nothing in buying data 
                print("no products have beeen added we reccomend addin something ")
            else:
                print(buyingdata)



        elif details == 'Q':
            eneterdetails = False

        elif details == 'C':
            if not buyingdata:
                print("we can't sell anything since we have nothing")
            else:
                product = random.choice(list(buyingdata.keys())) #this thng picks a random product
                avalible_quantity = buyingdata[product]['quantity'] #avalible quantity in stock

                if avalible_quantity > 0:
                    random_quantity = random.randint(1, 4)
                    #doing the part where we do'Nt buy more then we have
                    quanitity_to_buy = min(random_quantity, avalible_quantity)
                    buyingdata[product]['quantity'] -= quanitity_to_buy #removes the quanity it chocee
                    for_price = buyingdata[product]['price'] * random_quantity
                    money_spent_by_npc += for_price
                    gainmoney = money_spent_by_npc
                    print(f"Npc bught {quanitity_to_buy} of {product}. for {for_price}$")

                    if buyingdata[product]['quantity'] == 0:
                        del buyingdata[product]
                        print(f"{product} is now out of stock removed it from the list so npc can't complain ")


        else:
            print("Plese select an option from A B Q ")
        
    return buyingdata
eneringproducts()

