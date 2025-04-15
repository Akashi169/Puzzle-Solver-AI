import os
import sys
import random
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.utils import *

class StochasticHC:
    def __init__(self, state, target):
        self.state = state
        self.target = target 
        
    def get_adj_node(self, state):
        list_adj_node = []
        x, y = get_pos(state, 0)
        directions = {"Up": (-1,0), "Down": (1,0), "Left": (0,-1), "Right" : (0,1)}
        
        for move, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy 
            if 0 <= nx < 3 and 0 <= ny <3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                list_adj_node.append((new_state, move, heuristic(new_state, self.target)))
        
        return list_adj_node  
    
    def stochastic_hc(self):  
        open_list = [(self.state, heuristic(self.state, self.target), "Start")]
        current_state = [row[:] for row in self.state]
        visited = set()
        step = 0

        while True:
            step += 1
            if tuple(map(tuple, current_state)) in visited:
                open_list.append((current_state, heuristic(current_state, self.target), "Stuck"))
                return open_list, len(open_list), step
            
            visited.add(tuple(map(tuple, current_state)))
            if current_state == self.target:
                open_list.append((current_state, heuristic(current_state, self.target), "Goal"))
                return open_list, len(open_list), step
            
            neighbors = self.get_adj_node(current_state)
            better_neighbor = []

            for new_state, move, h in neighbors:
                if h < heuristic(current_state, self.target):
                    better_neighbor.append((new_state, move, h))

            if not better_neighbor:  
                open_list.append((current_state, heuristic(current_state, self.target), "Stuck"))
                return open_list, len(open_list), step
            
            
            best_neighbor, best_move, best_h = random.choice(better_neighbor)
            current_state = best_neighbor
            #current_state = random.choice(best_neighbor)
            open_list.append((current_state, best_h, best_move))
