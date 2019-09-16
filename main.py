'''
this code is based off tech with tim's code found at https://techwithtim.net/tutorials/breadth-first-search/
all i did was change the logic behind finding the start of the maze so the start
could be anywhere in the maze and cleaned up the code so it's easier to understand
'''

import queue
import copy

'''
just to get the ol maze we wanna be solving
1 is a wall
0 is an empty space
O is the start point
X is the end point
'''
def getMaze():
    maze = [
        ["1", "1", "1", "1", "X", "1"],
        ["1", "0", "1", "1", "0", "1"],
        ["1", "0", "0", "0", "0", "1"],
        ["1", "1", "1", "0", "1", "1"],
        ["1", "0", "0", "0", "0", "1"],
        ["1", "O", "1", "1", "1", "1"]
    ]

    return maze

# get where the start is in the maze
def findStart(maze):
    for y, row in enumerate(maze): # go through each row
        for x, col in enumerate(row): # go through each column
            if col == 'O':
                return (x, y)

# travel through the path defined for this attempt
def traverse(maze, path):
    x, y = findStart(maze)
    for move in path:
        if move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        elif move == 'U':
            y -= 1
        elif move == 'D':
            y += 1

    return (x, y)

# just how we print out the maze
def printMaze(maze, path=''):
    print('path: ', path)
    x, y = findStart(maze)
    for move in path:
        if move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        elif move == 'U':
            y -= 1
        elif move == 'D':
            y += 1
        
        if maze[y][x] != 'X':
            maze[y][x] = 'o'
    
    for y in maze:
        row = ''
        for x in y:
            if x == '1': row += '#'
            elif x == '0': row += ' '
            else: row += x
        print(row)

# see if we are at the end of the maze
def checkEnd(maze, path):
    x, y = traverse(maze, path)
    if maze[y][x] == 'X':
        printMaze(maze, path)
        return True
    else:
        return False

def checkOpposite(move, newmove):
    if move == 'L':
        if newmove == 'R':
            return True
    elif move == 'R':
        if newmove == 'L':
            return True
    elif move == 'U':
        if newmove == 'D':
            return True
    elif move == 'D':
        if newmove == 'U':
            return True
    
    return False

# validate a potential path
def validPath(maze, path):
    x, y = traverse(maze, path)
    if not (0 <= x < len(maze[0]) and 0 <= y < len(maze)): # check the move is within the range of the maze
        return False
    elif maze[y][x] == '1': # check if the move lands on a wall
        return False
    elif len(path) > 1:
        if checkOpposite(path[-1], path[-2]): # make sure we're not going back on ourselves
            return False

    return True

def main():
    paths = queue.Queue()
    path = '' # our initial moves will be to do nothing
    paths.put(path)
    maze = getMaze()
    printMaze(maze)

    while not checkEnd(maze, path) and not paths.empty():
        path = paths.get()
        for j in ['L', 'R', 'U', 'D']:
            newpath = path + j
            if validPath(maze, newpath):
                paths.put(newpath)

if __name__ == '__main__':
    main()