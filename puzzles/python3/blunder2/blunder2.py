import heapq
from typing import List


EXIT_NUMBER = -1  # room number for the exit
START_NUMBER = 0  # index of the start room


class Room:
    """Each room is a node of the tree"""
    def __init__(self, number: int, money: int, door1: str, door2: str):
        self.number = number
        self.money = money
        self.depth = -1
        self.doors: List[int] = []
        self.read_door(door1)
        self.read_door(door2)

    def read_door(self, door: str):
        if door == "E":
            self.doors.append(EXIT_NUMBER)
        else:
            self.doors.append(int(door))

    def __lt__(self, other):
        """Reversed operator for max heap"""
        return other.depth < self.depth


class Building:
    """Tree representation of the building"""
    def __init__(self):
        self.rooms: List[Room] = []

    def read_rooms(self):
        nb_rooms = int(input())
        for _ in range(nb_rooms):
            number, money, door1, door2 = input().split()
            room = Room(int(number), int(money), door1, door2)
            self.rooms.append(room)

    def max_money(self) -> int:
        """Find the path with the max total money (inspired by Dijkstra's algorithm)"""
        unvisited: List[Room] = []  # heap used as a priority queue
        money: List[int] = []  # maximum known money earnings down each path
        for number in range(len(self.rooms)):
            money.append(0)  # initial money earnings
            heapq.heappush(unvisited, self.rooms[number])

        # loop through each depth level of the tree in descending order
        while unvisited:
            # pick the room with the max depth
            max_room = heapq.heappop(unvisited)
            # find the best path for each subproblem
            next_number = self.next_door(max_room.number, money)
            money[max_room.number] = max_room.money
            if next_number != EXIT_NUMBER:
                money[max_room.number] += money[next_number]
        return money[START_NUMBER]

    def next_door(self, max_number: int, money: List[int]) -> int:
        door1 = self.rooms[max_number].doors[0]
        door2 = self.rooms[max_number].doors[1]
        if door1 == EXIT_NUMBER:
            return door2
        if door2 == EXIT_NUMBER:
            return door1
        if money[door1] >= money[door2]:
            return door1
        else:
            return door2


def calc_max_depth(building: Building, room: Room, parent_depth: int):
    room.depth = parent_depth + 1
    for door in room.doors:
        if door != EXIT_NUMBER:
            neighbor = building.rooms[door]
            if neighbor.depth <= room.depth:
                calc_max_depth(building, neighbor, room.depth)


if __name__ == "__main__":
    building = Building()
    building.read_rooms()
    # Calculate the max depth of each room reachable from the start with DFS
    calc_max_depth(building, building.rooms[START_NUMBER], -1)
    print(building.max_money())
