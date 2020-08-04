import random

def createBoard(board:dict):
    """
    A method used to create a board with snakes and ladders
    """
    arrOfSnakes = []
    for j in range(2):
        for _ in range(0,6):
            x = random.randint(0,100)
            y = random.randint(0,100 - x)
            while y == x: 
                y = random.randint(0,100)
            arrOfSnakes.append((x,y))

        if j == 1:
            board.update({'snakes':arrOfSnakes})
            x = 0
            arrOfSnakes = []
            y = []
        else:
            board.update({'ladders':arrOfSnakes})
            x = 0
            arrOfSnakes = []
            y = []
            
       

    return board

