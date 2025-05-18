import os
import sys
import heapq
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.utils import *

class BeamSearch:
    def __init__(self, state, target):
        self.state = state
        self.target = target 
        self.beam_width = 5
        self.visited = set() 
    
    def beam_search(self):  
        if not is_solvable(self.state, self.target):
            print("BeamSearch: Initial state not solvable")
            return [], 0, 0
        
        open_list = [(heuristic(self.state, self.target), self.state, "Start", [(self.state, heuristic(self.state, self.target), "Start")])]
        self.visited.add(tuple(map(tuple, self.state)))
        step = 0
        max_steps = 10000
        
        while open_list and step < max_steps:
            step += 1
            next_states = []
            for h, state, move, path in open_list:
                if state == self.target:
                    return path + [(state, heuristic(state, self.target), "Goal")], len(path), step

                for new_state, new_move in get_adj_node(state):
                    state_tuple = tuple(map(tuple, new_state))
                    if state_tuple not in self.visited:
                        self.visited.add(state_tuple)
                        new_h = heuristic(new_state, self.target)
                        new_path = path + [(new_state, new_h, new_move)]
                        heapq.heappush(next_states, (new_h, new_state, new_move, new_path))
            
            open_list = heapq.nsmallest(self.beam_width, next_states)
         
        print("BeamSearch: No solution found")
        return [], 0, step

    
        
        
        
                    



