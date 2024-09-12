import tkinter
import random
ROWS = 24
COLS = 24
TILE_SIZE = 24
WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

# tile class

class Tile:
    def __init__(self, x, y, ):
        self.x = x
        self.y = y

        
# GSME WINDOW IN HERE
window = tkinter.Tk()
window.title("Snake Game by using python : developer abdella dawud ")
window.resizable(True, True)
canvas = tkinter.Canvas(
    window, bg = "blue", 
    width = WINDOW_WIDTH, 
    height = WINDOW_HEIGHT,
    borderwidth = 0,
    highlightthickness = 0)
canvas.pack()
window.update()

# cenetr the window 
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# formate " (w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# initialize the game
snake = Tile(4*TILE_SIZE, 4*TILE_SIZE)
apple_food = Tile(11*TILE_SIZE, 11*TILE_SIZE)
# for eat food
snake_body = []  # multiple snake tiles
velocityX = 0
velocityY = 0

#game over
finsh_game = False
score = 0
def change_direction(e): #e = event
    #print(e)
    #
    # print(e.keysym)
    global velocityX, velocityY
    if (finsh_game):
         return
    
    if (e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0
        
def move():
            global snake, apple_food, snake_body, finsh_game, score
            if (finsh_game):
                 return
            if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y >= WINDOW_HEIGHT):
                 finsh_game = True
                 return
            
            for tile in snake_body:
                 if (snake.x == tile.x and snake.y == tile.y):
                      finsh_game = True
                      return
            #collision
            if (snake.x == apple_food.x and snake.y == apple_food.y):
                 snake_body.append(Tile(apple_food.x, apple_food.y))
                 apple_food.x = random.randint(0, COLS-1) * TILE_SIZE
                 apple_food.y = random.randint(0, ROWS-1) * TILE_SIZE
                 score += 1

            # update snak body
            for i in range(len(snake_body)-1, -1, -1):
                tile  = snake_body[i]
                if(i == 0):
                    tile.x = snake.x
                    tile.y = snake.y
                else:
                    prev_tile = snake_body[i-1]
                    tile.x =prev_tile.x
                    tile.y =prev_tile.y          
                      
            snake.x += velocityX * TILE_SIZE
            snake.y += velocityY * TILE_SIZE 


def draw():
    global snake, apple_food, snake_body, finsh_game, score
    move()
    canvas.delete("all")
    
    # draw applefood
    canvas.create_oval(apple_food.x, apple_food.y, 
                            apple_food.x + TILE_SIZE, 
                            apple_food.y + TILE_SIZE, 
                            fill = "red")
    #draw snak
    canvas.create_rectangle(snake.x, snake.y, 
                            snake.x + TILE_SIZE, 
                            snake.y + TILE_SIZE, 
                           fill="lime green", outline="dark green",  width = 8)
    for tile in snake_body:
         canvas.create_rectangle(tile.x, tile.y, 
                                 tile.x + TILE_SIZE,
                                 tile.y + TILE_SIZE,
                                 fill = "lime green")
    if (finsh_game):
         canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
                            font = "Arial 25", 
                            text = f"finsh game: Your score is {score}", 
                            fill = "white") 

    else:
         canvas.create_text(26, 18, font = "Arial 12", text = f"The Score is : {score}",
                                                                fill = "white")         
    
    
    window.after(100, draw) 
draw()

window.bind("<KeyRelease>", change_direction)

window.mainloop()