class ship:
    def __init__(self,name,x,y) :
        self.name = name
        self.x = x
        self.y = y

def are_adjacent(ship1,ship2):
    return abs(ship1.x -ship2.x) <=1 and (ship1.y-ship2.y)<=1

def bfs(ship,ships,visited):
    queue = [ship]
    visited.add(ship)

    while queue:
        current_ship = queue.pop(0)
        current_ship.name = current_ship.name.lower()

        for other_ship in ships:
            if other_ship not in visited and are_adjacent(current_ship,other_ship):
                queue.append(other_ship)
                visited.add(other_ship)

def process_ship(ships):
    visited = set()
    for ship in ships :
        if ship not in visited :
            bfs(ship,ships,visited)
    
    for ship in ships :
        print(f"ship: name = {ship.name},position = (x={ship.x},y = {ship.y})")


# example usage
ship1 = ship("A",3,4)
ship2 = ship("Z",4,4)
ship3 = ship("Z",5,6)

ships = [ship1,ship2,ship3]
process_ship(ships) 


