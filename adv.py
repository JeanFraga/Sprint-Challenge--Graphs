from room import Room
from player import Player
from world import World

from graph import Graph
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# global times_moved

# def append_path(move):
#     traversal_path.append(move)

# def exits():
#     return player.current_room.get_exits()

# def move(path):
#     player.travel(path[0])
#     traversal_path.append(path[0])
    # global times_moved += 1

# back = {
#     'n':'s',
#     's':'n',
#     'e':'w',
#     'w':'e'
# }
# def move_back(move):
#     player.travel(back[move])
    # for i in range(path[1]):
    #     player.travel(inverse[traversal_path[-i]])

# def next_id(move):
#     direction = {
#         'n':'n_to',
#         's':'s_to',
#         'e':'e_to',
#         'w':'w_to'
#     }
#     room = f"player.current_room.{direction[move]}.id"
#     return room


# ss = Stack()
# visited_rooms = [False] * 500

# while False in visited:
# times_moved = 0

# for exits in player.current_room.get_exits():
#     ss.push((exits, player.current_room.id))
#     # print(exits)
#     # print(len(player.current_room.get_exits()))
# path = ss.pop()
# while ss.size() > 0:
#     # player.travel(path[0])
#     # traversal_path.append(path[0])
#     move(path)
#     print(player.current_room.id)
#     # times_moved += 1
#     if len(player.current_room.get_exits()) > 1:
#         for exits in player.current_room.get_exits():
#             ss.push((exits, player.current_room.id))
#     else:
#         path = ss.pop()
#         i = -1
#         while path[1] != player.current_room.id:
#             move_back = traversal_path[i]
#             move_back(move_back)
#             # print(path[1], move)
#             i-=1

# print(next_id("n"))
# print(str(desc[0]))

# graph = Graph()
# visited = dict()
# for i in range(0, 500):
#     # visited[i] = False
#     graph.add_vertex(i)

# for i in graph.vertices:


# visited_rooms = [False] * 500

# while False in visited:
# for i in range(len(visited_rooms)):
#     # visited[i] = True
#     # print(i)
#     if visited_rooms[i] is False:
#         qq = Queue()
#         qq.enqueue(player.current_room)
#         visited = set()
#         traversed = []
#         while qq.size() > 0:
#             path = qq.dequeue()
#             # path = 
#             if path.id not in visited:
#                 if path == visited_rooms[i]:
#                     # print(path[-1])
#                     visited_rooms[i] = True
#                     traversal_path = traversal_path + traversed
#                     break

#                 visited.add(path)
#                 for next_vert in path.get_exits():
#                     traversed.append(next_vert)
#                     player.travel(next_vert)
#                     new_path = player.current_room
#                     # new_path.append(next_vert)
#                     qq.enqueue(new_path)
            

# print(player.current_room.id)

back = {
    'n':'s',
    's':'n',
    'e':'w',
    'w':'e'
}

# random.seed(1)
def move_back(move):
    player.travel(back[move])

traveled = []
def travel():
    moves = []
    # if len(moves) == 0:
    #     traveled = []
    directions = player.current_room.get_exits()
    # print(directions)
    random.shuffle(directions)
    # print(directions)

    for direction in directions:
        player.travel(direction)

        if player.current_room.id not in traveled:
            traveled.append(player.current_room.id)
            moves.append(direction)
            moves = moves + travel()
            player.travel(move_back(direction))
            # if len(directions) == 1:
            moves.append(back[direction])
            
        else:
            move_back(direction)
    
    return moves


traversal_path = travel()


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
