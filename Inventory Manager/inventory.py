#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        pass

        import re

        with open("inventory.txt", "r+") as inv:
            inv_viewer = ""
            for lines in inv:
                inv_viewer += lines
            all_inventory = inv_viewer
            shoe_list = re.split(r'[,\n]', all_inventory)
            product_list = shoe_list[7:len(shoe_list):5]
            cost_list = shoe_list[8:len(shoe_list):5]

            if self.product in product_list:
                product_pos = product_list.index(self.product)
                print(cost_list[product_pos])

            elif self.product not in product_list:
                print("Couldn't be found")

    def get_quantity(self):
        pass

        import re

        with open("inventory.txt", "r+") as inv:
            inv_viewer = ""
            for lines in inv:
                inv_viewer += lines
            all_inventory = inv_viewer
            shoe_list = re.split(r'[,\n]', all_inventory)
            product_list = shoe_list[7:len(shoe_list):5]
            quantity_list = shoe_list[9:len(shoe_list):5]

            if self.product in product_list:
                product_pos = product_list.index(self.product)
                print(quantity_list[product_pos])

            elif self.product not in product_list:
                print("Couldn't be found")

    def __str__(self):
        pass
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

#=============Shoe list===========
'''The list will be used to store a list of objects of shoes.'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''This will read all shoe data and append shoe objects into shoe list'''
    pass
    import re

    with open("inventory.txt", "r+") as inv:
        all_shoes = ""
        try:
            for lines in inv:
                all_shoes += lines
            all_inventory = all_shoes
            full_inv = re.split(r'[,\n]', all_inventory)
            country = full_inv[5:len(full_inv):5]
            code = full_inv[6:len(full_inv):5]
            product = full_inv[7:len(full_inv):5]
            cost = full_inv[8:len(full_inv):5]
            quantity = full_inv[9:len(full_inv):5]
            shoe_list = []

            for k in range(len(quantity)):
                shoes = Shoe(country[k], code[k], product[k], cost[k], quantity[k])
                shoe_list.append(shoes)
        except FileNotFoundError as file:
            print("No such file exists")



def capture_shoes():
    '''This is to capture new shoes'''
    pass
    new_item_country = input("What country will you sell it in? ")
    new_item_code = input("What is the shoes' code? ")
    new_item_product = input("What is the shoe called? ")
    new_item_cost = input("How much does it the shoe cost? ")
    new_item_quantity = input("How many of them are you ordering? ")
    shoe_list.append(f"\n{new_item_country},{new_item_code},{new_item_product},{new_item_cost},{new_item_quantity}")
    print("This has been added to the list.")

def view_all():
    '''This function will print the details of the shoe list'''
    pass

    import re
    from tabulate import tabulate

    with open("inventory.txt", "r+") as inv:
        Inv_viewer = ""
        for lines in inv:
            Inv_viewer += lines
        all_inventory = Inv_viewer
        shoe_list = re.split(r'[,\n]', all_inventory)
        country = shoe_list[0:len(shoe_list):5]
        code = shoe_list[1:len(shoe_list):5]
        product = shoe_list[2:len(shoe_list):5]
        cost = shoe_list[3:len(shoe_list):5]
        quantity = shoe_list[4:len(shoe_list):5]
        # Here I have read and wrote the data from inventory.txt into str,
        # split the str using the delimiters "," and "\n" and created lists to reach the requiste data easier.

        full_inv = []
        for numb in range(len(product)):
            grouping = [country[numb], code[numb], product[numb], cost[numb], quantity[numb]]
            full_inv.append(grouping)
        table = tabulate(full_inv, headers='firstrow')
        print(f"{table}\n")
        # This code is to put the information in the appropriate format so
        # I am able to tabulate the file and show it in a table.

def re_stock():
    '''This function finds the shoe with the lowest quantity, asks the usser if they want to restock and how many,
    then updates it in the original txt file.'''
    pass
    while True:
        import re

        with open("inventory.txt", "r") as inv:
            inv_viewer = ""
            for lines in inv:
                inv_viewer += lines
            all_inventory = inv_viewer
            shoe_list = re.split(r'[,\n]', all_inventory)
            country = shoe_list[0:len(shoe_list):5]
            code = shoe_list[1:len(shoe_list):5]
            product = shoe_list[2:len(shoe_list):5]
            cost = shoe_list[3:len(shoe_list):5]
            quantity = shoe_list[4:len(shoe_list):5]
            # Here I have read and wrote the data from inventory.txt into str,
            # split the str using the delimiters "," and "\n" and created lists to reach the requiste data easier.


            final_quantity = list(map(int, quantity[1:len(quantity):1]))
            index_min = min(range(len(final_quantity)), key=final_quantity.__getitem__) + 1
            # There is a plus 1 at the end because I am going to add back an item on the next line.
            final_quantity.insert(0, quantity[0])
            print(f"The shoe with the lowest quantity: {product[index_min]}\n"
                  f"There are only {final_quantity[index_min]} available.")
            # Here I have found converted my list from a list of str to ints and removed the first item as it cannot be
            # converted, found the location of the lowest value, added the first item back into the list and printed
            # text so the user knows what shoe has the lowest volume and it's quantity.

            restock_item = input("Would you like to restock this item? yes or no?").lower()
            if restock_item == "yes":
                try:
                    amount_restock = int(input("How many more shoes would you like to order? "))
                    with open("inventory.txt", "w+") as restock_update:
                        final_quantity[index_min] = amount_restock + final_quantity[index_min]
                        final_quantity = list(map(str, final_quantity))
                        for numb in range(len(quantity)):
                            grouping = [country[numb], code[numb], product[numb], cost[numb], final_quantity[numb]]
                            new_shoe_list = ",".join(grouping)
                            restock_update.write(f"{new_shoe_list}\n")
                        print(f"The inventory for the {product[index_min]} has been updated.\n"
                              f"There are now {final_quantity[index_min]} in inventory.")
                        break
                except ValueError as val:
                    print("\nSorry, there seems to be an issue with what you entered."
                          "\nPlease ensure that you only enter integers.\n")
                    continue
            if restock_item == "no":
                break
            if restock_item != "no" and restock_item != "yes":
                print("\nPlease enter a valid response.\n")
                continue
            # Here I have added a questions to understand if the user wants to restock shoes, and if so, how many.
            # I have ensured that if the appropriate answers aren't answered that the user will have to retry.
            # If the user wants to restock the shoe and gives a value, it will add the value to the stock, and format it
            # in the same way the information originally came. Once formatted, it will overwrite the previous
            # information in inventory.txt and give the updated values.

def seach_shoe():
    '''This function will allow the user to search for a particular shoe.'''
    pass
    import re

    while True:
        product_code = input("What is the code for the item you are looking for? ")
        with open("inventory.txt", "r+") as inv:
            inv_viewer = ""
            for lines in inv:
                inv_viewer += lines
            all_inventory = inv_viewer
            shoe_list = re.split(r'[,\n]', all_inventory)
            code = shoe_list[6:len(shoe_list):5]
            product = shoe_list[7:len(shoe_list):5]
            # Here I have read and wrote the data from inventory.txt into str,
            # split the str using the delimiters "," and "\n" and created lists to reach the requiste data easier.

            if product_code in code:
                product_pos = code.index(product_code)
                print(f"We have found the item you have been searching for: \"{product[product_pos]}\"")
                break
            if product_code not in code:
                print(f"Sorry, we could not find the item you were looking for: \"{product_code}\"")
                break

def value_per_item():
    '''This function calculates the total value of each item and prints out the values.'''
    pass

    import re
    from tabulate import tabulate

    with open("inventory.txt", "r+") as inv:
        inv_viewer = ""
        for lines in inv:
            inv_viewer += lines
        all_inventory = inv_viewer
        shoe_list = re.split(r'[,\n]', all_inventory)
        product = shoe_list[7:len(shoe_list):5]
        cost = shoe_list[8:len(shoe_list):5]
        quantity = shoe_list[9:len(shoe_list):5]
        # Here I have read and wrote the data from inventory.txt into str,
        # split the str using the delimiters "," and "\n" and created lists to reach the requiste data easier.

        final_quantity = list(map(int, quantity))
        final_cost = list(map(int, cost))
        value = [a * b for a, b in zip(final_quantity, final_cost)]
        total_value = sum(value)
        # I have switched the values in the lists, quantity and cost to integers so I could do multiplication and sum.

        value_table = [['Product', 'Value']]  # This list will be the bases of my table.
        for numb in range(len(cost)):
            grouping = [product[numb], value[numb]]
            value_table.append(grouping)
        final_value_table = tabulate(value_table, headers='firstrow')
        print(f"The total value of the products is {total_value}.\n"
              f"Here is a table for each individual products value \n\n"
              f"{final_value_table}")

def highest_qty():
    '''This function will determine the product with the largest quantity and print this shoe as for sale.'''
    pass
    import re

    with open("inventory.txt", "r+") as inv:
        inv_viewer = ""
        for lines in inv:
            inv_viewer += lines
        all_inventory = inv_viewer
        shoe_list = re.split(r'[,\n]', all_inventory)
        product = shoe_list[7:len(shoe_list):5]
        quantity = shoe_list[9:len(shoe_list):5]
        # Here I have read and wrote the data from inventory.txt into str,
        # split the str using the delimiters "," and "\n" and created lists to reach the requiste data easier.

        final_quantity = list(map(int, quantity))
        # I changed the values from strings to ints so the min function would work
        index_min = max(range(len(quantity)), key=final_quantity.__getitem__)
        # I used this variable to locate the position of the shoe with the largest quantity
        print(f"The {product[index_min]} will be on sale from now on.")

#==========Main Menu=============

while True:
    try:
        menu = int(input('''Select one of the following Options below:
                        1 - Read shoe data
                        2 - Add new shoe data
                        3 - View all shoe data
                        4 - Restock shoes
                        5 - Search for specific shoe
                        6 - Find out the value of shoes
                        7 - Put shoe for sale
                        Any negative integer - Exit
                        : '''))
        if menu == 1:
            pass
            read_shoes_data()

        elif menu == 2:
            pass
            capture_shoes()

        elif menu == 3:
            pass
            view_all()

        elif menu == 4:
            pass
            re_stock()

        elif menu == 5:
            pass
            seach_shoe()

        elif menu == 6:
            pass
            value_per_item()

        elif menu == 7:
            pass
            highest_qty()

        elif menu > 7:
            print("Sorry, you have entered an incorrect value.\n")

        elif menu < 0:
            exit()

    except ValueError as val_error:
        print("Sorry, you have entered an incorrect value.\n")
        continue


