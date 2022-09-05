"""
Conway's Game of Life

1) Any live cell with 2 or 3 live neighbors survives
2) Any dead cell with 3 live neighbors becomes alive
3) All other live cells die. All other dead cells stay dead.

"""

coords = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

class Game:
    def __init__(self, seed):
        self.tick = 0
        self.alive_cells = {s for s in seed}
        print(self)
        self.next_cells = set()

    def step(self):
        # calculate surviving cells
        self.next_cells = {c for c in self.alive_cells if self.is_alive(c)}

        self.calc_new_cells()

        self.alive_cells = self.next_cells
        print(self)
        self.tick += 1

    def is_alive(self, cell):
        x, y = cell
        is_alive = cell in self.alive_cells
        num_cells = sum(1 for dx, dy in coords if (x + dx, y + dy) in self.alive_cells)
        if is_alive and (num_cells == 2 or num_cells == 3):
            return True
        elif not is_alive and num_cells == 3:
            return True
        return False

    def calc_new_cells(self):
        checked_cells = set()
        for x, y in self.alive_cells:
            for dx, dy in coords: 
                neighbor = (x + dx, y + dy)
                if neighbor in self.next_cells: continue
                elif neighbor in checked_cells: continue
                if self.is_alive(neighbor):
                    self.next_cells.add(neighbor)    
                checked_cells.add(neighbor)


    def __repr__(self):
        board = f"tick: {self.tick}\n"
        for y in range(10, -10, -1):
            board += "".join('#' if (x, y) in self.alive_cells else '.' for x in range(-20, 20)) + "\n"
        print(self.alive_cells)
        return board

if __name__ == '__main__':
    seed = [(0, 0), (1, 0), (2, 0), (2, 1), (1, 2)]
    g = Game(seed)
    while True:
        input("Press Enter to continue.")
        g.step()

            









