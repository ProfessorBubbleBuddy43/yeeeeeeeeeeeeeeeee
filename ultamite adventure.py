from room import Room

northwest1 = Room('northwest1', 'You are in north west section #1.', 'nw1')
northwest2 = Room('northwest2', 'You are in north west section #2.', 'nw2')
northeast1 = Room('northeast1', 'You are in north east section #1.', 'ne1')
northeast2 = Room('northeast2', 'You are in north east section #2.', 'ne2')
southeast1 = Room('southeast1', 'You are in south east section #1.', 'se1')
southeast2 = Room('southeast2', 'You are in south east section #2.', 'se2')
southwest1 = Room('southwest1', 'You are in south west section #1.', 'sw1')
southwest2 = Room('southwest2', 'You are in south west section #2.', 'sw2')
north = Room('north', 'You are in the north section.', 'n')
south = Room('south', 'You are in the south section.', 's')
east = Room('east', 'You are in the east section.', 'e')
west = Room('west', 'You are in the west section.', 'w')

northwest1.add_connection(northwest2, "passage", ["northwest", "nw"])
northwest1.add_connection(northeast1, "passage", ["east", "e"])
northwest1.add_connection(southwest1, "passage", ["south", "s"])
northwest1.add_connection(west, "passage", ["southwest", "sw"])
northwest1.add_connection(north, "passage", ["northeast", "ne"])
northwest2.add_connection(west, "passage", ["south", "s"])
northwest2.add_connection(north, "passage", ["east", "e"])
northwest2.add_connection(northwest1, "passage", ["southeast", "se"])

kitchen.add_connection(hallway, "passage", ["north", "n"])


current_room = northwest1
while True:
    current_room.enter_room()
    command = raw_input("What direction do you want to go?")
    if command in ["exit", "x", "quit", "q"]:
        break


    elif (current_room.is_valid_direction(command)):
        current_room = current_room.next_room(command)
        current_room.enter_room()

    else:
        print "Ouch! You ran into a wall."
