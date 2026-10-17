"""Project Two starter for the student's text-based adventure game."""

# Keith Mills


def show_instructions():
    """Display the game objective and available commands."""
    print ("Caretaker's Building Escape")
    print("Collect all six items before entering the Caretaker's Room.")
    print("Move with: go north, go south, go east, go west")
    print("Collect an item with: get <item name>")
    


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")
    if "item" in rooms[current_room]:
        print(f"You see {rooms[current_room]['item']}")
    
    


def main():
    """Run the main gameplay loop."""
    rooms = {
        "Entry Hall" : {"north": "Caretake's Room", "west": "Storage Room"},
        "Storage Room": {"north": "Workshop", "east": "Entry Hall", "item": "Flashlight"}
        "Workshop": {"north": "Security Office", "south": "Storage Room", "item": "Screwdriver"},
        "Security Office": {"east": "library", "south": "Workshop", "item": "Access Card"},
        "Library": {"west": "Security Office", "east": "Supply Closet", "item": "Code Note"},
        "Supply Closet": {"west": "Library": "south": "Manager's Office", "item": "Battery"}
        "Manager's Office": {"west": "Caretaker's Room", "north": "Supply Closet", "item": "Master Key"},
        "Caretake's Room": {"south": "Entry Hall", "east": "Manager's Office"}
    }


    current_room = "Entry Hall"

    inventory = []

    show_instructions()

    while True:

        show_status(current_room, inventory, rooms)

        command = input("Enter your command: ").strip().lower()

        if command.startswith("go "):

            direction = command[3:]

            if direction in ("north", "south", "east", "west") and direction in rooms[current_room]:

                current_room = rooms[current_room][direction]

                if current_room == "Caretaker's Room":

                    if len(inventory) == 6:

                        print("You collected all six items and escaped!")

                    else:

                        print("The Caretaker caught you. You lose!")

                    break

            else:

                print("You can't go that way.")

        elif command.startswith("get "):

            requested_item = command[4:].strip()

            if "item" in rooms[current_room] and requested_item == rooms[current_room]["item"].lower():

                inventory.append(rooms[current_room]["item"])

                del rooms[current_room]["item"]

                print(f"You collected the {inventory[-1]}.")

            else:

                print("That item is not available here.")

        else:

            print("Invalid command. Try a move or get an item.")


    



if __name__ == "__main__":
    main()
