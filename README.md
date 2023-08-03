<p align="center">
<img width="634" alt="HyperionDev-Thumbnail-Image" src="https://github.com/Taharqua/Bootcamp/assets/56850203/7aeecac0-e7f7-4be5-9623-030e5aac82ae">
</p>

## Introduction
I created this repository to showcase exactly what I learned during my bootcamp.
This is more compressed version of my bootcamp as I am only displaying my capstone projects.

## Overview of the HyperionDev
HyperionDev's Software Engineering Bootcamp is a rigorous and immersive 12-week program that I successfully completed, equipping me with the skills and expertise needed to excel in the dynamic field of software development. Throughout the bootcamp, I gained comprehensive knowledge of software engineering concepts and best practices, allowing me to contribute effectively to real-world projects and collaborative development teams.

## Curriculum
The bootcamp's curriculum covered a wide range of topics, including programming languages such as Python, JavaScript, and Java, data structures, algorithms, object-oriented programming, web development, databases, version control, and software testing. Each module was carefully designed to provide a solid foundation in various technical areas.

## Capstone Projects
A key highlight of the bootcamp were the Capstone Projects as they were a great platform to apply my knowledge in practical scenarios. These projects allowed me to develop problem-solving skills, improve my coding proficiency, and gain valuable experience working on real-world challenges.

## [Finance Calculator](https://github.com/Taharqua/Bootcamp/blob/main/Project%201/finance_calculator.py)

In my first Capstone Project, I was tasked with creating a program that allows the user to calculate their interest on an investment or calculate the amount that should be repaid on a home loan each month.

Here is a link to my [Finance Calculator](https://github.com/Taharqua/Bootcamp/blob/main/Project%201/finance_calculator.py)

## [Task Manager Application](https://github.com/Taharqua/Bootcamp/blob/main/Project%202/task_manager.py)

In my second Capstone Project, I was tasked with creating a [Task Management Application](https://github.com/Taharqua/Bootcamp/blob/main/Project%202/task_manager.py).

In creating the Task Management Application, I had to use my understanding of string handling and working with external data sources.

Here is an example of both concepts:

```python
with open('tasks.txt', "a+") as f3:
  Add_task_Username = input("What is your username: ")
  Task_title = input("Enter the title of the task: ")
  Description_Task = input("Enter a description of the task: ")
  Due_Date = input("Enter the due date in \"dd mmm yyyy\" format: ")
  Task_completed = input("Has the task been completed? Yes or No? ")
  today = date.today()
  Today = today.strftime("%d %b %Y")
  f3.write(f"\n{Add_task_Username}, {Task_title}, {Description_Task}, "
    f"{Today}, {Due_Date},{Task_completed}")
  f3.close()
```

## [Updated Task Manager Application](https://github.com/Taharqua/Bootcamp/blob/main/Project%203/task_manager.py)

The third Capstone Project is just a continuation of my second Capstone Project, making improvements on the [Task Management Application](https://github.com/Taharqua/Bootcamp/blob/main/Project%203/task_manager.py).

Example:

I was tasked with modifying the register user function so that it doesn't allow any add duplicates, and if a user tries to add a username to it tells a relevant error message and allow them to try to add user with a different username.

From how the function looked in the second Capstone Project:
```python
with open('user.txt', "a+") as f2:
NewUser_Username = str(input("Enter the username: "))
NewUser_Password = str(" ")
NewUser_Password_Confirmation = str()
    while NewUser_Password != NewUser_Password_Confirmation:
    NewUser_Password = str(input("Enter your password: "))
        NewUser_Password_Confirmation = str(input("Confirm your password: "))
        if NewUser_Password != NewUser_Password_Confirmation:
            print("The two passwords do not match, please re-enter them")
        else:
            f2.write(f"\n{NewUser_Username}, {NewUser_Password}")
            f2.close()
            print("Thank you for entering your details!"
                "\nThey have been added to our system!")
```
To how it looks in the third Capstone Project:

```python
def reg_user():
    """This is to add a new user using a series of for and while loops"""
    import re
    while True:
        with open('user.txt', "r+") as file:
            username = str(input("Enter the username: "))
            ru_login_details = ""
            entire_usernames_list = []
            for ru_lines in file:
                ru_login_details += ru_lines
            all_login_details_str = ru_login_details
            all_login_details_list = re.split(r'[,\n]', all_login_details_str)
            for i in range(len(all_login_details_list)):
                if i % 2 == 0:
                    entire_usernames_list.append(all_login_details_list[i])
                else:
                    pass
            if username in entire_usernames_list:
                print("Error: This username has already been entered. Please try another.")
                continue
            else:
                password = str(" ")
                password_confirmation = str()
                while password != password_confirmation:
                    password = str(input("Enter your password: "))
                    password_confirmation = str(input("Confirm your password: "))
                    if password != password_confirmation:
                        print("The two passwords do not match, please re-enter them")
                        continue
                    else:
                        file.write(f"\n{username}, {password}")
                        file.close()
                        print("Thank you for entering your details!"
                              "\nThey have been added to our system!")
                        break
            break
```

## [Inventory Manager](https://github.com/Taharqua/Bootcamp/blob/main/Project%204/inventory.py)

The fourth Capstone Project is using my knowledge of object oriented programming to create a real-world solution.
In this Project, I will be pretending I am a Nike warehouse manager and creating a platform for [Inventory Manager](https://github.com/Taharqua/Bootcamp/blob/main/Project%204/inventory.py).

An example of some functions I have created are:

```python
def re_stock():
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

            final_quantity = list(map(int, quantity[1:len(quantity):1]))
            index_min = min(range(len(final_quantity)), key=final_quantity.__getitem__) + 1
            final_quantity.insert(0, quantity[0])
            print(f"The shoe with the lowest quantity: {product[index_min]}\n"
                  f"There are only {final_quantity[index_min]} available.")

            restock_item = input("Would you like to restock this item? yes or no?").lower()
            if restock_item == "yes":
                try:
                    amount_restock = int(input("How many more shoes would you like to order? "))
                    with open("inventory.txt", "w+") as restock_update:
                        final_quantity[index_min] = amount_restock + final_quantity[index_min]
                        final_quantity = list(map(str, final_quantity))
                        for numb in range(len(quantity)):
                            grouping = [country[numb], code[numb], product[numb], cost[numb],
                            final_quantity[numb]]
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
```

## [Bookstore Database](https://github.com/Taharqua/Bootcamp/blob/main/Project%205/task48.py)

The fifth project was to create a [bookstore database](https://github.com/Taharqua/Bootcamp/blob/main/Project%205/task48.py) using my knowledge of Python and libraries such as SQLite.

Example of using SQLite:

```python
while True:
    try:
        menu = int(input('''Select one of the following Options below:
                        1 - Add book
                        2 - Update book information
                        3 - Delete books from the database
                        4 - Search the database to find a specific book
                        5 - Exit
                        : '''))
        if menu == 1:
            pass
            title_new = input("What is the title of the book? ")
            author_new = input("Who is the author")
            qty_new = input("how many books are being added? ")

            books_ = [(title_new, author_new, qty_new)]

            cursor.executemany(''' INSERT INTO ebookstore(title, author, qty) VALUES(?,?,?)''', books_)

            db.commit()
```

## Outcome

Upon completing the Software Engineering Bootcamp at HyperionDev, I managed to finish within the the top 5% of my cohort averaging over 95% on all technical tasks. I gained a strong foundation in software development and a portfolio of projects that showcased my abilities to potential employers. I am now well-prepared to pursue a rewarding career as a software engineer and contribute my skills to innovative projects in the tech industry.

## Conclusion

HyperionDev Software Engineering Bootcamp was a transformative experience that has significantly shaped my career trajectory. I am grateful for the invaluable knowledge, practical skills, and industry exposure I gained throughout the program, and I am excited to embark on new challenges and opportunities in the software engineering field.
