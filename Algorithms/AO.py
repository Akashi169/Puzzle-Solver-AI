import heapq
import os
import sys 
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))
from src.utils import*

class AndOrSearch:
    def __init__(self, state, target):
        self.state = state 
        self.target = target 
        self.plan = []
        self.visited = set()
        self.step = 0
    
    def or_search(self, state, path):
        if state == self.target:
            return True 
        
        if tuple(map(tuple, state)) in path:
            return False 
        
        for (s, action) in get_adj_node(state): 
            self.step += 1 
            if self.and_search(s, path + [tuple(map(tuple, state))]):
                self.plan.append(action)
                return True 
        return False 

    def and_search(self, state, path):
        return self.or_search(state, path)
    
    def search(self):
        found = self.or_search(self.state, [])
        self.plan.reverse()
        return found, self.plan, self.step 
    