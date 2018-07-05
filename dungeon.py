import random as r
from gm import TOADCell
from termcolor import colored, cprint

class Tile():
    def __init__(self, char):
        self.char = char

class Entity():
    def __init__(self, char, x, y):
        self.char = char

class Room():
    def __init__(self, x, y, end_x, end_y, tile):
        self.x = x
        self.y = y
        self.end_x = end_x
        self.end_y = end_y
        self.tile = tile

class Generator():
    def __init__(self, rooms):
        self.rooms = rooms
        self.map = [[],[]]

    def extend(self):
        placeholder = 1

    def paint(self, map, room_list, entity_list):
        placeholder = 1

    def left_right(self, prev, current):
        return location

    def connector(self, start, end):
        x, y = None

        # Check if it's horizontal of vertical
        if(start[0] == end[0]): # Vertical, by checking x coordinates
            x = start[0]
            y = r.randint(start[1] + 1, end[1] - 1)
        elif(start[1] == end[1]): # Horizontal, by checking y coordinates
            x = r.randint(start[0] + 1, end[0] - 1)
            y = start[1]

        return [x, y]

    def generate(self, rooms):
        room_list = []
        connector_list = []
        room_count = 0

        # Starting Area
        roll = r.randint(1, 10)
        roll = 1
        x = 0
        y = 0
        if(roll == 1):
            new_room = Room(x, y, x + 3, y + 3, '.')
            room_list.append(new_room)
            room_count += 1

            # Top Side
            connector_list.append(connector([new_room.x, new_room.y], [new_room.end_x, new_room.y]))

            # Bottom Side
            connector_list.append(connector([new_room.x, new_room.end_y], [new_room.end_x, new_room.end_y]))

            # West Side
            connector_list.append(connector([new_room.x, new_room.y], [new_room.x, new_room.end_y]))

            # East Side
            connector_list.append(connector([new_room.end_x, new_room.y], [new_room.end_x, new_room.end_y]))

        # Passage to Room Loop
        done = False
        while done == False:
            # Pick a connector to generate a passage
            placeholder = 1
