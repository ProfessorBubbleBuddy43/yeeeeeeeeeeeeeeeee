class Room():
    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id
        self.items = []
        self.rooms = {}

    def add_item(self, item):
        self.items.append(item)

    def add_room(self, direction, room):
        self.rooms[direction] = room

    def connect_rooms(self, direction, room):
        opposite_direction = {'n': 's','s': 'n','e': 'w','w': 'e'}
        self.add_room(direction, room)
        room.add_room(opposite_direction[direction], self)

    def enter_room(self):
        print self.name
        print
        print self.description
        print
        for direction in self.rooms.keys():
            print "To the " + direction + " is a " + self.rooms[direction].get_name()

    def get_name(self):
        return self.name

    def is_valid_direction(self, direction):
        return direction in self.rooms.keys()

    def next_room(self, direction):
        return self.rooms[direction]


kitchen = Room('kitchen', 'You are in the kitchen.', 'k')
dining = Room('dining', 'You are in the dining room.', 'd')
hallway = Room('hallway', 'You are in the hallway.', 'h')
hallway2 = Room('hallway', 'You are in the hallway.', 'uh')
bedroom1 = Room('bedroom', 'You are in the bedroom.', 'b1')
bedroom2 = Room('bedroom', 'You are in the bedroom.', 'b2')
bedroom3 = Room('bedroom', 'You are in the bedroom.', 'b3')
living = Room('living room', 'You are in the living room.', 'l')

kitchen.connect_rooms('n', dining)

kitchen.add_room('n', dining)
dining.add_room('s', kitchen)
dining.add_room('n', hallway)
hallway.add_room('s', dining)
hallway.add_room('u', hallway2)
hallway.add_room('e', living)
living.add_room('w', hallway)
hallway2.add_room('d', hallway)
hallway2.add_room('n', bedroom1)
hallway2.add_room('e', bedroom2)
hallway2.add_room('w', bedroom3)
bedroom1.add_room('s', hallway2)
bedroom2.add_room('w', dining)
bedroom3.add_room('e', dining)

current_room = dining
dining.enter_room()

while True:
    direction = raw_input("What direction do you want to go?")
    if direction == 'x':
        break
    elif (current_room.is_valid_direction(direction)):
        current_room = current_room.next_room(direction)
        current_room.enter_room()

    else:
        print "Ouch! You ran into a wall."
