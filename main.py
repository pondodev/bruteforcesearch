from search import solve

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

def main():
    maze = getMaze()
    if solve(maze):
        print('maze is solvable')
    else:
        print('maze is not solvable')

if __name__ == '__main__':
    main()