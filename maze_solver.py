class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class FrontierStack():
    def __init__(self): self.frontier = []
    def isEmpty(self): return len(self.frontier) == 0
    def addNode(self, node): self.frontier.append(node)
    def containsState(self, state): return any(node.state == state for node in self.frontier)
    def returnStatesInFrontier(self): return (node.state for node in self.frontier)
    def popNode(self): 
        if self.isEmpty(): raise Exception("Frontier Stack is Empty")
        else: return self.frontier.pop()


class FrontierQueue(FrontierStack): # just inherit everything from FrontierStack to FrontierQueue
    def popNode(self): 
        if self.isEmpty(): raise Exception("Frontier Stack is Empty")
        else:
            poppedNode = self.frontier[0]
            self.frontier = self.frontier[1:]
            return poppedNode


class Maze():
    def __init__(self, filename, algo="DFS", debug=False):
        self.algo = algo
        self.debug = debug

        with open(filename) as f: contents = f.read()

        if contents.count("A") != 1: raise Exception("Error: Multiple or No Starting Point")
        if contents.count("B") != 1: raise Exception("Error: Multiple or No Ending Point")

        contents = contents.splitlines() # convert contents str to list of str lines (split by \n)
        self.height = len(contents)
        self.width = max(len(row) for row in contents)

        self.contents = contents

        # Identifying co-ordinates of walls
        self.walls = []   # is true if wall is present, else false
        for r in range(self.height):
            row = []
            for c in range(self.width):
                try:
                    if contents[r][c] == "A":
                        row.append(False)
                        self.start = r,c
                    elif contents[r][c] == "B":
                        row.append(False)
                        self.goal = r,c
                    elif contents[r][c] == " ": row.append(False)
                    else: row.append(True)
                except IndexError: row.append(False)
            self.walls.append(row)
        self.solution = None

    def printMaze(self):
        solution = self.solution[1] if self.solution else None     # solution = (actions, cells)
        for r in range(self.height):
            for c in range(self.width):
                try:
                    if self.contents[r][c] == " " and solution and (r,c) in solution: print("*", end='')
                    else: print(self.contents[r][c], end="")
                except IndexError: pass 
            print()
    
    def neighbors(self, state):
        row, col = state
        Neighbours = {
            "UP"   : (row-1, col), 
            "DOWN" : (row+1, col), 
            "LEFT" : (row, col-1), 
            "RIGHT": (row, col+1)
        }

        result = []
        for action, (r, c) in Neighbours.items():
            if r in range(self.height) and c in range(self.width) and not(self.walls[r][c]): result.append((action, (r, c)))
        return result
    
    def solve(self):
        self.countExploredNodes = 0   # Number of nodes explored

        # Initialization for solving
        start = Node(state=self.start, parent=None, action=None)
        frontier = FrontierStack() if self.algo == "DFS" else FrontierQueue()
        frontier.addNode(start)
        self.exploredStates = set()

        # Keep looping until we find a solution
        while True:
            if frontier.isEmpty(): raise Exception("No Solution")
            
            node = frontier.popNode()
            if self.debug: print("\t\tNode Popped", node.state)
            self.countExploredNodes += 1

            # if we found a solution, retrace the path and save the solution
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            
            # if node is explored, add it to explored set
            self.exploredStates.add(node.state)   # Here state means co-ordinates

            # add nodes to frontier
            for action, state in self.neighbors(node.state):
                if not frontier.containsState(state) and state not in self.exploredStates:
                    childNode = Node(state=state, parent=node, action=action)
                    frontier.addNode(childNode)
                    if self.debug: print("\t Added Child to frontier", childNode.state)

import sys
if __name__ == "__main__":
    if len(sys.argv) == 2: 
        m = Maze(filename = sys.argv[1], debug = False)
        print("Usage: python maze_solver.py file.maze algo \n Algorithm not specified! Default Selected: DFS \n\n Supported Algos: BFS, DFS\n\n") 
    elif len(sys.argv) != 3: raise Exception("Usage: python maze_solver.py file.maze algo")
    else: m = Maze(filename = sys.argv[1], algo = sys.argv[2], debug = False)

    print("1.\t Input Maze:")
    m.printMaze()
    print("2.\t Solving...")
    m.solve()
    print("3.\t States Explored:", m.countExploredNodes)
    print("4.\t Solution:")
    m.printMaze()