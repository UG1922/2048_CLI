import random

def new_grid(empty=False):
    new = []
    if empty:
        for i in range(0,4):
            new.append([])
    else:
        for i in range(0,4):
            new.append([0]*4)
    return new
    

def add_new():
    get = False
    while not get:
        row , col = random.randrange(0,4) , random.randrange(0,4)
        if sqr[row][col] == 0:
            sqr[row][col] = 2
            get = True

   
def move():
    new = new_grid()
    for u in range(0,4):
        count = 0
        for v in range(0,4):
            if sqr[u][v] != 0:
                new[u][count] = sqr[u][v]
                count += 1
    return new
    
def reverse():
    new = new_grid(True)
    for u in range(0,4):
        for v in range(0,4):
            new[u].append(sqr[u][3-v])
    return new


def transverse():
    new = new_grid(True)
    for u in range(0,4):
        for v in range(0,4):
            new[u].append(sqr[v][u])
    return new

def merge():
    for u in range(0,4):
        for v in range(0,3):
            if sqr[u][v] == sqr[u][v+1]:
                sqr[u][v] *= 2
                sqr[u][v+1] = 0

def merging():
    for u in range(0,4):
        for v in range(0,3):
            if sqr[u][v] == sqr[u][v+1]:
                return True

def is_any_empty():
    for u in range(0,4):
        for v in range(0,4):
            if sqr[u][v] == 0:
                return True

def game_over_check():
    if not is_any_empty():
        if merging():
            return False
        else:
            return True
    else:
        return False

def win_check():
    for u in range(0,4):
        for v in range(0,4):
            if sqr[u][v] == 2048:
                return True

def move_left():
    global sqr
    sqr = move()
    merge()
    sqr = move()
    add_new()


def move_right():
    global sqr
    sqr = reverse()
    sqr = move()
    merge()
    sqr = move()
    sqr = reverse()
    add_new()

def move_up():
    global sqr
    sqr = transverse()
    sqr = move()
    merge()
    sqr = move()
    sqr = transverse()
    add_new()

def move_down():
    global sqr
    sqr = transverse()
    sqr = reverse()
    sqr = move()
    merge()
    sqr = move()
    sqr = reverse()
    sqr = transverse()
    add_new()

running = True
while running:
    global sqr
    sqr = new_grid()
    sqr[3][2] = 2
    sqr[3][0] = 2
    print("\n\t\t\t\tINSTRUCTIONS\n\t\t\t1)Use w to move up\n\t\t\t2)Use s to move down\n\t\t\t3)Use a to move left\n\t\t\t4)Use d to move right")
    print("\n\t\tTO win you have to make 2048 in any cell\n")
    play = True
    while play:
        for i in range(0,4):
            print(sqr[i])
        comnd = input("Enter the commmnad")
        if comnd == "a" or comnd == "A":
            move_left()
        elif comnd == "d" or comnd == "D":
            move_right()
        elif comnd == "w" or comnd == "W":
            move_up()
        elif comnd == "s" or comnd == "S":
            move_down()
        else:
            print("\n\t\t\t\t\t WRONG Input")

        if win_check() == True:
            print("You win")
            play = False
        
        elif game_over_check() == True:
            print("Game over")
            play = False
            running = False
