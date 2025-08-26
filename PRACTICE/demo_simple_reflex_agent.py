import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

# Define the environment with four rooms
environment_state = {
    "Room1": "Clean",
    "Room2": "Dirty",   # Start with dirt here
    "Room3": "Clean",
    "Room4": "Clean"
}

# Define the grid positions for each room
room_coordinates = {
    "Room1": (0, 1),  # Top-left
    "Room2": (1, 1),  # Top-right
    "Room3": (0, 0),  # Bottom-left
    "Room4": (1, 0)   # Bottom-right
}

room_names = list(environment_state.keys())  
agent_location_index = 0  

# Define the simple reflex agent's logic
def simple_reflex_agent(status):
    if status == "Dirty":
        return "Clean_Room"
    else:
        return "Move_To_Next_Room"
        
        



# Function to visualize the environment and agent
def visualize_environment(env, agent_idx, current_step):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 2) 
    ax.set_ylim(0, 2) 
    ax.set_xticks([])
    ax.set_yticks([]) 
    ax.set_title(f"Step {current_step} — Agent in {room_names[agent_idx]}")

    for room, pos in room_coordinates.items():  
        x, y = pos
        color = 'red' if env[room] == "Dirty" else 'green'  
        rect = patches.Rectangle((x, y), 1, 1, facecolor=color, edgecolor='black') 
        ax.add_patch(rect)
        ax.text(x + 0.5, y + 0.5, room, ha='center', va='center', color='white', fontsize=10) # "Room1"

    # Draw the agent in its current room
    agent_x, agent_y = room_coordinates[room_names[agent_idx]] # Finds the agent's current position.
    agent_patch = patches.Circle((agent_x + 0.5, agent_y + 0.5), 0.1, color='blue') #blue circle
    ax.add_patch(agent_patch)

    plt.pause(1) 
    plt.close() 
     
     
     
# --- Simulation Loop ---
plt.ion()  
total_steps = 10  


for step in range(total_steps):
    current_room_name = room_names[agent_location_index] 
    room_status = environment_state[current_room_name] 
    agent_action = simple_reflex_agent(room_status) 

    visualize_environment(environment_state, agent_location_index, step + 1) 

    if agent_action == "Clean_Room": # If the agent decides to clean, this line updates the environment, marking the room as "Clean".
        environment_state[current_room_name] = "Clean"
    else:
        agent_location_index = (agent_location_index + 1) % len(room_names) 


plt.ioff() 
print("✅ Simulation complete!")