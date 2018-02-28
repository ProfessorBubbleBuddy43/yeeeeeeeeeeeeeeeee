class Room():
    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id
        self.connectors = []
        self.items = []
        self.rooms = {}

    def add_item(self, item):
        self.items.append(item)

    def add_room(self, direction, room):
        self.rooms[direction] = room

    def add_connection(self, room, connector, actions):
        for direction in actions:
            self.rooms[direction] = room
        self.connectors.append((connector, actions[0]))

    def enter_room(self):
        print self.name
        print
        print self.description
        print
        if len(self.connectors) > 0:
            for connector in self.connectors:
                print "There is a " + connector[0] + \
                      " that goes " + connector[1]

    def get_name(self):
        return self.name

    def is_valid_direction(self, direction):
        return direction in self.rooms.keys()

    def next_room(self, direction):
        return self.rooms[direction]

