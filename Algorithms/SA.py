import os
import sys
import random
import math
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.utils import *

class SimulatedAnnealing:
    def __init__(self, state, target, T = 1000, alpha = 0.95):
        self.state = state 
        self.target = target 
        self.T = T
        self.alpha = alpha 
    
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
    
    def simulated_annealing_hc(self):  
        open_list = [(self.state, heuristic(self.state, self.target), "Start")]
        current_state = [row[:] for row in self.state]
        step = 0

        while self.T > 0.01:
            step += 1

            if current_state == self.target:
                open_list.append((current_state, heuristic(current_state, self.target), "Goal"))
                return open_list, len(open_list), step
            
            neighbors = self.get_adj_node(current_state)
            if not neighbors:
                break 
            
            new_state, move, new_h = random.choice(neighbors)
            current_h = heuristic(self.state, self.target)
            delta_e = new_h - current_h
            
            if delta_e < 0 or random.uniform(0,1) < math.exp(-delta_e /self.T):
                current_state = new_state
                open_list.append((current_state, current_h, move))
                
            self.T *= self.alpha 
        open_list.append((current_state, heuristic(current_state, self.target),"Stuck"))
        return open_list, len(open_list), step

