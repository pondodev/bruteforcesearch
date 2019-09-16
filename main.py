from search import solve
from copy import deepcopy

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
        ["1", "1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "0", "1"],
        ["1", "O", "1", "1", "1", "1"]
    ]

    return maze

def printMaze(maze):
    print('----')
    for y in maze:
        line = ''
        for x in y:
            line += str(x)
        print(line)
    print('----')

def main():
    maze = getMaze()
    width = len(maze[0])
    fulllen = len(maze) * len(maze[0])

    for i in range(fulllen):
        x = i % width
        y = int(i / width)
        if maze[y][x] == '1':
            mazecopy = deepcopy(maze)
            mazecopy[y][x] = 0
            if solve(mazecopy):
                print('remove wall at index ', str(y), ', ', str(x))
                printMaze(mazecopy)
                break

if __name__ == '__main__':
    main()