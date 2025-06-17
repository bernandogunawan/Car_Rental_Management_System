from tabulate import tabulate


# These variables are used to store the messages to be printed on the menus
welcome_message = """
===== Welcome to car rental center =====

What would you like to do:

1. Rent a car
2. Return a car
3. Add a car to car rental list
4. Remove a car from car rental list
5. Look at car rental list
6. Modify a car's data in car rental list
7. Reduce day
0. Exit the program
"""
rent_menu_message = """
=== Renting a car ===

Thank you for using our service

What would you like to do?

1. Rent a specific car
0. Back to main menu
"""
return_menu_message = """

=== Returning car ===

What would you like to do?

1. Returning a car
0. Back to main menu
"""
create_menu_message = """

=== Adding car to car rental list ===

What would you like to do:

1. Start entering car details
0. Go back to main menu
"""
read_menu_message = """
=== Showing car rental list ===

What would you like to do:

1. Look at list of cars
2. Filter list of cars
0. Go back to main menu
"""
stop_rent_menu_message = """
=== Removing a car from rental list ===

1. Remove a car
2. Remove batch cars
3. Remove all cars
0. Back to main menu
"""
Update_car_data_message = """
=== Updating car details ===

what would you like to do

1. Update a specific car
0. Back to main menu
"""
read_filter_message = """
=== Filtering ===

What would you like to do?

1. Filter cars
9. Reset filter
0. Back to read menu
"""
batch_delete_message = """
=== Batch deletion ===

What would you like to do?

1. Filter cars
2. Delete all filtered cars
9. Reset filter
0. Back to delete menu
"""
message_error = "Sorry, that input doesn't seem valid\n"
fuel_type_message = """
Input the index of your car fuel type 
1. Gasoline 
2. Diesel
"""
status_message = """
Input the index of your car status
1. Available 
2. Not available
"""
column_update_message = """
Insert the index of the column you want to update

1. License plate
2. Brand
3. Model
4. Fuel type
5. Price per day
"""
column_index_message = """
Insert the index of the column you want to update

1. License plate
2. Brand
3. Model
4. Fuel type
5. Price per day
6. Status
7. Days left
"""

# These variables are used to store the data and help to control the integrity of the data
db_column_names = ["License plate", "Brand", "Model", "Fuel type", "Price per day", "Status", "Days left"]
available_keys = {"B2233GH", "BE225YT", "A9876YH","BE5678HJ"}
not_available_keys = {"IC3133AR", "BE1234EF"}

database = {
    "B2233GH" : ["B2233GH", "Toyota", "Avanza", "Gasoline", "200,000", "Available", None],
    "BE225YT" : ["BE225YT", "Nissan", "Grand livina", "Diesel", "150,000", "Available", None],
    "IC3133AR" : ["IC3133AR", "Mitsubishi", "Triton", "Diesel", "300,000", "Not available", 5 ],
    "A9876YH" : ["A9876YH", "Audi", "Accord", "Gasoline", "400,000" , "Available", None],
    "BE1234EF" : ["BE1234EF", "Audi", "A3", "Gasoline", "350,000", "Not available", 3],
    "BE5678HJ" : ["BE5678HJ", "Toyota", "Accord", "Diesel", "375,000", "Available", None]
}


# On this section are helper functions that will be used throughout the program
def print_table(data):
    """
    Prints the data with a particular format

    args:
    data (list of list): the data to be printed
    """
    print("\n")
    print(tabulate(data, headers=db_column_names, tablefmt="pipe",showindex="always"))
    print("\n")

def check_limit(word):
    """
    Checks whether the length of the argument "word" is between 0 and 15

    args:
    word (str): the word that will be checked

    return:
    boolean value whether the "word" is between 0 and 15
    
    """
    if (0 <= len(word) <= 15):
        return True
    else:
        print("Sorry, the length of the word needs to be between 0 and 15")
        return False
    
def keep_asking(message_input, message_error = message_error, valid_input = None, type = None, repeat = True):
    """
    asks user repeatedly until a valid answer is entered

    args:
    message_input (str): text to be printed while asking user
    message_error (str): optional
                        text to be printed when the input is not valid
    valid_input (list): list of valid value
    type (str or int) : the intended data type for the answer
    repeat (bool): boolean value to decide if the code need to be repeated

    return:
    the inputted value from user
    """
    valid = False
    while True:
        command = input(message_input)
        if valid_input:
            if command.isdigit():
                valid = int(command) in valid_input
            else:
                valid = command.capitalize() in valid_input

        elif not valid_input:
            if type == int:
                valid = command.isdigit()
            elif type == str:
                bool_check = check_limit(command)
                if not bool_check:
                    continue
                else:
                    valid = command.replace(" ","").isalnum()
            
        if not valid:
            print(message_error)
            if not repeat:
                return None
        else:
            break

    return command

def payment(total_price):
    """
    Simulates the payment process
    
    args:
    total_price (int): price to be paid by user
    """
    # keep asking money until user can pay it full
    while total_price > 0:
        print(f"\nYour total price is Rp. {total_price:,}")
        money = int(keep_asking("Please insert your money: ","Sorry, please insert a positive number\n",type = int))
        
        # only reduce the remaining bill, if user input a positive number
        if money > 0:
            total_price -= money
        else:
            print("Sorry, please insert an amount bigger than 0")
    
    # give money back if user pay more than required
    if total_price < 0:
        print(f"Your change is Rp.{abs(total_price):,}")


# function for main menu
def main_menu():
    """
    Prints the main menu and ask for valid choice

    return:
    a valid choice from user
    """
    print(welcome_message)
    return int(keep_asking("Please enter your selection (0-7): ",valid_input=[1, 2, 3, 4, 5, 6, 7,0]))


# 1. function to rent a car
def renting_process(car):
    """
    Simulates and updates the process of renting a car

    args:
    car (list): the car's data
    """
    print_table([car])
    sure_command = keep_asking("Do you want to rent this car? (Y or N): ",valid_input=["Y","N"]).capitalize()

    if sure_command == "Y":
        # Calculate total price and start payment process
        days_left = int(keep_asking("How many days do you want to rent?: ", "Sorry, please insert an integer\n", type = int))
        daily_price = int(car[4].replace(",",""))
        payment(daily_price * days_left)

        # updating database after renting process is confirmed
        license_plate = car[0]
        database[license_plate][5] = "Not available"
        database[license_plate][6] = days_left
        available_keys.remove(license_plate)
        not_available_keys.add(license_plate)

        print("Thank you, come again")
    else:
        print("Your request for renting a car has been cancelled")

def rent_car():
    """
    menu of renting a car
    """
    # Using a loop to open an opportunity for futher options
    while True:

        # The main loop for renting a car
        print(rent_menu_message)
        command = int(keep_asking("Please enter your selection (1 or 0): ", valid_input=[1,0]))

        if command == 1:
            temp_list = [] # used to store only available car

            for keys in available_keys:
                temp_list.append(database[keys])
            
            if len(temp_list) == 0:
                print("Sorry, currently there is no car available")
                continue

            print_table(temp_list)
            temp_index = keep_asking("Please insert index of the car you want to rent: ",
                                         valid_input=list(range(len(temp_list))),
                                         repeat=False)

            if temp_index != None:
                renting_process(temp_list[int(temp_index)])
            continue

        elif command == 0:
            break


# 2. function to return a car
def returning_process(car):
    """
    Simulates and updates the process of returning a car

    args:
    car (list): the car's data
    """

    print_table([car])
    confirmation_return = keep_asking("Do you want to return the car? (Y or N): ",valid_input=["Y","N"]).capitalize()
    if confirmation_return == "Y":
        # check if the customer return a car too late, and then ask for the extra cost
        if car[6] < 0:
            print("You returned it late. Additional cost need to be paid")
            daily_price = int(car[4].replace(",",""))
            payment(abs(car[6]) * daily_price)

        # update the database after the returning process
        license_plate = car[0]
        database[license_plate][6] = None
        database[license_plate][5] = "Available"
        available_keys.add(license_plate)
        not_available_keys.remove(license_plate)

        print("Thank you, the car has been returned successfully")
    else:
        print("Your car return request has been cancelled")

def return_car():
    """
    menu of returning a car
    """
    # Using a loop to open an opportunity for futher options
    while True:

        # The main loop for returning a car
        print(return_menu_message)
        command = int(keep_asking("Please enter your selection (1 or 0): ", valid_input=[1, 0]))

        if command == 1:
            temp_list = [] # used to store only available car

            for keys in not_available_keys:
                temp_list.append(database[keys])

            if len(temp_list) == 0:
                print("Sorry, currently there is no car available")
                continue

            print_table(temp_list)
            temp_index = keep_asking("Please insert the index of the car you want to return: ",
                                         valid_input=list(range(len(temp_list))),
                                         repeat=False)
            if temp_index != None:
                returning_process(temp_list[int(temp_index)])
            break

        elif command == 0:
            break


# 3. function for create feature
def add_car_to_db():
    """
    Simulates the whole process of adding a car to the main database
    """
    while True:

        # the main loop of adding process
        print(create_menu_message)
        command = int(keep_asking("Please enter your selection (1 or 0): ", valid_input=[1, 0]))

        if command == 1:

            # asking user for the car's detail
            car_license_plate = keep_asking("\nPlease insert the license plate of the car you want to add: ",type = str).replace(" ","").upper()
            if car_license_plate in database.keys():
                print("Sorry, that license plate already exists")
                continue

            car_brand = keep_asking("Input your car brand: ", type = str).capitalize()
            car_model = keep_asking("Input your car model: ", type = str).capitalize()
            car_fuel_type = int(keep_asking( fuel_type_message,
                                        valid_input=[1,2]))
            car_price = int(keep_asking("Input how much you want to charge per day: ", "Sorry, please insert an integer\n", type = int))

            # Change 'car_fuel_type' from index to fuel type in string
            if car_fuel_type == 1:
                car_fuel_type = "Gasoline"
            else:
                car_fuel_type = "Diesel"

            # add the details to a list for printing and adding to database
            new_car = [
                car_license_plate,
                car_brand,
                car_model,
                car_fuel_type,
                f"{car_price:,}",
                "Available",
                None
            ]

            print_table([new_car])
            
            command_verification = keep_asking("Do you want to add this car? (Y or N): ",valid_input=["Y","N"]).capitalize()
            
            if command_verification == "Y":
                # add the car to database
                database[car_license_plate] = new_car
                available_keys.add(car_license_plate)
                print("Thank you, the car has been successfully added to car rental list")
            else:
                print("Your request for adding a car has been cancelled")
                continue

        elif command == 0:
            break


# 4. function for read feature
def filtering_process_str(index, value, table_copy):
    """
    helper function to filter a dataset

    args:
    index (int): index of the column that want to be filtered
    value (str): intended value to be filtered
    table_copy (dict): the dataset to be filtered

    return:
    the filtered dataset
    """
    temp_table = {}

    # check the original dictionary, if the car value (which is in a list) in a certain column 
    # is equal to the intended value
    for key, car in table_copy.items():
        if car[index] == value:
            temp_table[key] = car

    return temp_table

def filtering_process_int(index, value, query, table_copy):
    """
    helper function to filter a dataset

    args:
    index (int): index of the column that want to be filtered
    value (int): intended value to be filtered
    query (str): criteria of the filter (Bigger, smaller, or equal)
    table_copy (dict): the dataset to be filtered

    return:
    the filtered dataset
    """
    temp_table = {}

    # check and insert car based on the car price
    if index == 4:
        for key, car in table_copy.items():
            price = int(car[4].replace(",",""))
            if query == "Bigger" and price > value:
                temp_table[key] = car
            elif query == "Smaller" and price < value:
                temp_table[key] = car
            elif query == "Equal" and price == value:
                temp_table[key] = car
    
    # check and insert car based on the days left
    elif index == 6:
        for key, car in table_copy.items():
            if car[6] == None:
                continue
            if query == "Bigger" and car[6] > value:
                temp_table[key] = car
            elif query == "Smaller" and car[6] < value:
                temp_table[key] = car
            elif query == "Equal" and car[6] == value:
                temp_table[key] = car

    return temp_table

def filtering(table_copy):
    """
    Simulates the process of filtering based on the intended value from one column

    args:
    table_copy {dict}: the base data that we want to filter from

    return:
    temp_table {dict}: the data after being filtered
    """

    column_filter = int(keep_asking(column_index_message,valid_input=list(range(1,8))))
    
    # starts checking which column to filter and calls the filtering_process for filtering process
    if column_filter == 1:
        value = keep_asking("Please insert the license plate of the car:",type = str).replace(" ","").upper()
        temp_table = filtering_process_str(0,value,table_copy)
        
    elif column_filter == 2:
        value = keep_asking("Please insert the car brand: ", type= str).capitalize()
        temp_table = filtering_process_str(1,value,table_copy)
    
    elif column_filter == 3:
        value = keep_asking("Please insert the car model:", type= str).capitalize()
        temp_table = filtering_process_str(2,value,table_copy)

    elif column_filter == 4:
        value = int(keep_asking(fuel_type_message, valid_input=[1,2]))
        if value == 1:
            value = "Gasoline"
        else:
            value = "Diesel"
        temp_table = filtering_process_str(3,value,table_copy)

    elif column_filter == 5:
        query = keep_asking("How do you want to filter? (Bigger, Smaller, or Equal): ",valid_input=["Bigger","Smaller","Equal"]).capitalize()
        value = int(keep_asking("Please insert the car price:", "Sorry, please insert an integer\n", type = int))
        temp_table = filtering_process_int(4,value,query,table_copy)

    elif column_filter == 6:
        value = int(keep_asking(status_message, valid_input=[1,2]))
        if value == 1:
            value = "Available"
        else:
            value = "Not available"
        temp_table = filtering_process_str(5,value,table_copy)

    elif column_filter == 7:
        query = keep_asking("How do you want to filter? (Bigger, Smaller, or Equal): ",valid_input=["Bigger","Smaller","Equal"]).capitalize()
        value = int(keep_asking("Please insert the remaining rental days:", "Sorry, please insert an integer\n",type = int))
        temp_table = filtering_process_int(6,value,query,table_copy)

    return temp_table

def read_filter():
    """
    simulates the menu for filtering
    """
    table_copy = database.copy()
    while True:
        print(read_filter_message)
        command_filter = int(keep_asking("Please enter your selection (0,1 or 9): ",valid_input=[1, 9, 0]))
        
        # start the filtering process and get the result after filtering
        if command_filter == 1:
            temp_table = filtering(table_copy)
            table_copy = temp_table.copy()
            if len(table_copy) > 0:
                print_table(table_copy.values())
            else:
                print("Sorry, we couldn't find a car that matches your request. Maybe reset the filter first?")

        # reset the filter query
        elif command_filter == 9:
            table_copy = database.copy()

        elif command_filter == 0:
            break

def read_menu():
    """
    simulates the read menu
    """
    while True:

        # here is the main loop
        if len(database) == 0:
            print("Sorry, currently there is no car available")
            break

        print(read_menu_message)
        command = int(keep_asking("Please enter your selection (1,2, or 0) : ", valid_input=[1, 2, 0]))
        
        if command == 0:
            break
        elif command == 1:
            print_table(database.values())
        elif command == 2:
            read_filter()


# 5. function for update feature
def data_update_process(car):
    """
    ask user for update confirmation, then process it when they confirm

    arg:
    car (list): the car's detail that is being updated
    """
    command_confirmation = keep_asking("Do you want to update? (Y or N): ",valid_input=["Y","N"]).capitalize()
    
    if command_confirmation == "Y":
        database[car[0]] = car
        print("Thank you, the update is successful")
    else:
        print("Your update request has been cancelled")

def column_update_func(car, column):
    """
    Simulates the process of updating a car data
    
    args:
    car (list): car's detail that is being updated
    column (int): the column that wanted to be updated
    """
    # updates the license plate column
    if column == 1:
        value_update = keep_asking("Please insert the license plate of the car: ", type = str).replace(" ","").upper()
        
        if value_update in database.keys():
            print("Sorry, that license plate is already in use")
        else:
            license_plate = car[0]
            car[0] = value_update
            print_table([car])

            command_confirmation = keep_asking("Do you want to update? (Y or N): ",valid_input=["Y", "N"]).capitalize()
            
            # updates the database with the license plate given by user
            if command_confirmation == "Y":

                if license_plate in available_keys:
                    available_keys.remove(license_plate)
                    available_keys.add(value_update)

                elif license_plate in not_available_keys:
                    not_available_keys.remove(license_plate)
                    not_available_keys.add(value_update)

                del database[license_plate]
                database[value_update] = car

                print("Thank you, the update is successful")
    
    # updates the "Fuel type" column
    elif column == 4:

        value_update = int(keep_asking(fuel_type_message, valid_input=[1,2]))

        # change the index given by user to str form
        if value_update == 1:
            value_update = "Gasoline"
        else:
            value_update = "Diesel"

        car[3] = value_update
        print_table([car])
        data_update_process(car)
        
    # updates the "Price per day" column
    elif column == 5:

        value_update = keep_asking("Please insert the new value: ","Sorry, please insert an integer\n", type = int)
        car[4] = f"{int(value_update):,}"

        print_table([car])
        data_update_process(car)

    # updates the "brand" or "model" column
    else:
        value_update = keep_asking("Please insert the new value: ",type = str)
        
        # check if column is equal 2 (for brand) or 3 (for model) and updates the value
        if column == 2:
            car[1] = value_update
        elif column == 3:
            car[2] = value_update

        print_table([car])
        data_update_process(car)

def update_car_db():
    """
    Simulates the menu of updating car details
    """
    while True:
        print(Update_car_data_message)
        command = int(keep_asking("Please enter your selection (1 or 0): ",valid_input=[1,0]))

        if command == 1:
            # Shows only the available cars
            temp_list = []
            for key in available_keys:
                temp_list.append(database[key])

            if len(temp_list) == 0:
                print("Sorry, currently there is no car available")
                continue

            print_table(temp_list)
            
            index_license = keep_asking("Please insert index of the car you want to update: ",
                                valid_input=list(range(len(temp_list))),
                                repeat=False)
            
            # Check if index_license is not empty and print the car details
            if index_license != None:
                car = temp_list[int(index_license)]
                print_table([car])
            else:
                continue
            command_verification = keep_asking("Do you want to update this car? (Y or N): ", valid_input=["Y","N"]).capitalize()
            
            # ask the user which column to update by index and call 'column_update_func'
            if command_verification == "Y":
                column_update = int(keep_asking(column_update_message, valid_input=list(range(1,6))))
                column_update_func(car, column_update)
                continue
            else:
                print("Your requests to update a car has been cancelled")

        elif command == 0:
            break
            

# 6. function for delete feature
def delete_car_from_db():
    """
    simulates the deletion process of cars from the database.
    It also includes options for one, multiple, and all cars deletion
    """
    while True:

        print(stop_rent_menu_message)
        command = int(keep_asking("Please enter your selection (1, 2, 3 or 0): ",valid_input=[1,2,3, 0]))

        # run the command to delete a specific car
        if command == 1:

            temp_list = []
            for car in database.values():
                temp_list.append(car)

            if len(temp_list) == 0:
                print("Sorry, currently there is no car available")
                continue

            print_table(temp_list)

            index_license = keep_asking("Please insert index of the car you want to delete: ",
                                valid_input=list(range(len(temp_list))),
                                repeat=False)
            
            # Check if index_license is not empty and print the car details
            if index_license != None: 
                car = temp_list[int(index_license)]
                license_plate = car[0]
                print_table([car])
            else:
                continue

            command_verify = keep_asking("Do you want to remove the car? (Y or N): ",valid_input=["Y","N"]).capitalize()
            
            if command_verify == "Y":
                # delete the car's data in databases
                del database[license_plate]

                if license_plate in available_keys:
                    available_keys.remove(license_plate)
                elif license_plate in not_available_keys:
                    not_available_keys.remove(license_plate)

                print("Thank you, the car has been removed")
            else:
                print("Your request to delete a car has been cancelled")
                continue
        
        #run the command to delete batch of cars
        elif command == 2:
            table_copy = database.copy()

            while True:

                print(batch_delete_message)
                command_filter = int(keep_asking("Please enter your selection (0,1,2 or 9): ",valid_input=[1, 2, 9, 0]))
                
                # run the command to filter the cars
                if command_filter == 1:
                    temp_table = filtering(table_copy)
                    table_copy = temp_table.copy()

                    if len(table_copy) > 0:
                        print_table(table_copy.values())
                    else:
                        print("Sorry, we couldn't find a car that matches your request. Maybe reset the filter first?")
                
                # run the command to delete the filtered data       
                elif command_filter == 2:

                    if len(table_copy) > 0:
                        print_table(table_copy.values())
                    else:
                        print("Sorry, there is no car selected to be deleted. Maybe reset the filter first?")
                        continue

                    command_verify = keep_asking("Are you sure you want to delete these cars? (Y or N): ",valid_input=["Y","N"]).capitalize()
                    
                    if command_verify == "Y":

                        # delete the filtered cars
                        for key in table_copy.keys():
                            del database[key]

                            if key in available_keys:
                                available_keys.remove(key)
                            else:
                                not_available_keys.remove(key)

                        table_copy = database.copy()
                        print("Thank you, the cars have been removed")
                    else:
                        print("The cars removal request has been cancelled")
                        continue

                # run the command to reset the filter
                elif command_filter == 9:
                    table_copy = database.copy()

                elif command_filter == 0:
                    break

        # run the command to delete all cars from database
        elif command == 3:
            confirmation = keep_asking("Are you sure you want to clear all the data? (Y or N): ",valid_input=["Y","N"]).capitalize()
            
            # deletes all cars from database
            if confirmation == "Y":
                database.clear()
                available_keys.clear()
                not_available_keys.clear()
                print("Thank you, all cars have been removed")
            else:
                print("The cars removal request has been cancelled")
                continue

        elif command == 0:
            break


def reduce_day():
    """
    reduces the value in column "Days left" by one
    """
    for license_plate in not_available_keys:
        database[license_plate][6] = database[license_plate][6]-1

    if len(not_available_keys) == 0:
        print("There is currently no rented car to reduce the day from")
    else:
        print("Thank you, the remaining days have been reduced by 1")


# function to control the flow of program
def start_program():
    while True:
        command = main_menu()
        if command == 1: # rent a car
            rent_car()
        elif command == 2: # return a car
            return_car()
        elif command == 3: # add a car to database
            add_car_to_db()
        elif command == 4: # remove a car from database
            delete_car_from_db()
        elif command == 5: # list car
            read_menu()
        elif command == 6: # update car details
            update_car_db()
        elif command == 7: # reduce the remaining time of rented car
            reduce_day()
        elif command == 0: # exit
            print("Thank you, have a great day!")
            break


start_program()