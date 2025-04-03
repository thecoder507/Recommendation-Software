from data import *
from welcome import *
from linkedlist import *

print_pizza_radar_design()

# Write code to insert districts into a data structure (LinkedList) here. The data is in data.py
def insert_distritos():
    distritos_pty_list = Linkedlist()
    for distrito in distritos_pty:
        distritos_pty_list.insert_beginning(distrito)
    return distritos_pty_list

# Write code to insert pizzerias data into a data structure (LinkedList of LinkedLists) here. The data is in data.py
def insert_pizzerias_data():
    pizzeria_data_list = Linkedlist()
    for distrito in distritos_pty:
        pizzeria_sublist = Linkedlist()
        for pizzeria in pizzerias_por_distrito:
            if pizzeria[0] == distrito:
                pizzeria_sublist.insert_beginning(pizzeria)
        pizzeria_data_list.insert_beginning(pizzeria_sublist)
    return pizzeria_data_list

my_distritos_list = insert_distritos()
my_pizzeria_list = insert_pizzerias_data()

chosen_distrito = ""

# Write code for user interaction here
while len(chosen_distrito) == 0:
    user_input = str(input(
        "\nIn which district of Panama City are you located? "
    "\nStart typing the name of the district and press Enter to confirm or press Enter to see the districts.")).lower()
    
    # Search for user_input in districts data structure here
    matching_types = []
    distrito_list_head = my_distritos_list.get_head_node()
    while (distrito_list_head.get_value()) is not None:
        if str(distrito_list_head.get_value()).startswith(user_input):
            matching_types.append(distrito_list_head.get_value())
        distrito_list_head = distrito_list_head.get_next_node()

    for distrito in matching_types:
        print(distrito)
    
    # Check if only one type of district was found, ask user if they would like to select this type
    if len(matching_types) == 1:
        select_type = str(input(
            "\nThe only matching type for the specified input is " + matching_types[0] + ". \nDo you want to look pizzerias at " +
            matching_types[0] + " Enter y for yes and n for no\n")).lower()
        
        # After finding district write code for retrieving pizzeria data here
        if select_type == "y":
            selected_district = matching_types[0]
            print("\nSelected district: " + selected_district)
            restaurant_list_head = my_pizzeria_list.get_head_node()
            while restaurant_list_head.get_next_node() is not None:
                sublist_head = restaurant_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_district:
                    while sublist_head.get_next_node() is not None:
                          print("--------------------------")
                          print("Name: " + sublist_head.get_value()[1])
                          print("Address: " + sublist_head.get_value()[2])
                          print("--------------------------")
                          sublist_head = sublist_head.get_next_node()
                restaurant_list_head = restaurant_list_head.get_next_node()
            
            # Ask user if they would like to search pizzerias for other districts
            repeat_loop = str(input("\nDo you want to search other destrict? enter y for yes and n for no.\n")).lower()
            if repeat_loop == "n":
                break

