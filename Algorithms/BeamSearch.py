import os
import sys
import heapq
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.utils import *

class BeamSearch:
    def __init__(self, state, target):
        self.state = state
        self.target = target 
        self.beam_width = 2
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
    
    def beam_search(self):  
        open_list = [(self.state, heuristic(self.state, self.target), "Start")]
        step = 0

        while True:
            step += 1
            for state, h, move in open_list:
                if state == self.target:
                    return open_list + [(state, h, "Goal")], len(open_list), step

            next_states = []
            for state, h, move in open_list:
                neighbors = self.get_adj_node(state)
                for new_state, new_h, new_move in neighbors:
                    heapq.heappush(next_states,(new_state, new_h, new_move))
            open_list = heapq.nsmallest(self.beam_width, next_states)
         
        return open_list, len(open_list), step  
                    



