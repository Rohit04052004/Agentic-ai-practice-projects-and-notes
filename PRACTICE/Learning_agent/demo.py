import pygame  
import random  
import numpy as np  

# Initialize pygame
pygame.init()

WIDTH = 300
HEIGHT = 300
GRID_SIZE = 5  
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 5  

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#Actions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
ACTIONS = [UP, DOWN, LEFT, RIGHT]


# Initialize the game window
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rohit's Q-learning Snake")
ui_font = pygame.font.SysFont(None, 24)


# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

    def randomize(self):
        self.position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        
        

# Snake class
class Snake:
    def __init__(self):
        self.positions = [(2, 2)]
        self.direction = random.choice(ACTIONS)

    def move(self, action):
        self.direction = action
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.positions = [new_head] + self.positions[:-1]

    def grow(self):
        tail = self.positions[-1]
        self.positions.append(tail)

    def collision(self):
        head = self.positions[0]
        return (
            head in self.positions[1:] or
            head[0] < 0 or head[0] >= GRID_SIZE or
            head[1] < 0 or head[1] >= GRID_SIZE
        )
        
        

# Initialize the Q-table with zeros
q_learning_table = np.zeros((GRID_SIZE, GRID_SIZE, 4))

# Hyperparameters for Q-learning
learning_rate = 0.1  # Alpha
discount_factor = 0.9  # Gamma
exploration_rate = 0.1  # Epsilon
num_episodes = 100  



def get_state(snake):
    return snake.positions[0]


def get_reward(snake, food):
    if snake.positions[0] == food.position:
        return 10
    elif snake.collision():
        return -100
    else:
        return -1
        
        
        
        
# Main training loop
clock = pygame.time.Clock()

for episode in range(1, num_episodes + 1): 
    snake = Snake() 
    food = Food()
    done = False 
    total_reward = 0 

    while not done:  
        clock.tick(FPS) 

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        current_state = get_state(snake) 
        
        if random.uniform(0, 1) < epsilon: 
            action_idx = random.randint(0, 3)
        else:
            action_idx = np.argmax(q_learning_table[current_state[0], current_state[1]]) 
            
        action = ACTIONS[action_idx] 
        snake.move(action) 

        reward = get_reward(snake, food)  
        total_reward += reward 

        next_state = get_state(snake) 


        
        if 0 <= next_state[0] < GRID_SIZE and 0 <= next_state[1] < GRID_SIZE:
            q_learning_table[current_state[0], current_state[1], action_idx] = q_learning_table[current_state[0], current_state[1], action_idx] + learning_rate * (reward + discount_factor * np.max(q_learning_table[next_state[0], next_state[1]]) - q_learning_table[current_state[0], current_state[1], action_idx])

        if snake.positions[0] == food.position: 
            snake.grow() 
            food.randomize() 

        # Draw everything
        win.fill(WHITE) 
        for i in range(GRID_SIZE): 
            for j in range(GRID_SIZE):
                pygame.draw.rect(win, BLACK, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1) ## Draw the black grid lines.


        for pos in snake.positions:
            pygame.draw.rect(win, GREEN, (pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            label = font.render("Snake", True, BLACK)
            win.blit(label, (pos[0] * CELL_SIZE + 5, pos[1] * CELL_SIZE + 5))

        pygame.draw.rect(win, RED, (food.position[0] * CELL_SIZE, food.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        label = font.render("Food", True, BLACK)
        win.blit(label, (food.position[0] * CELL_SIZE + 5, food.position[1] * CELL_SIZE + 5))

        pygame.display.update()

        if snake.collision(): 
            done = True

    print(f"Episode {episode} finished with Total Reward: {total_reward}")
    