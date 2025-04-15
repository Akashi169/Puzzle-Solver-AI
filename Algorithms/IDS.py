from copy import deepcopy
import os
import sys 
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))
from src.utils import*
class IDS:
    def __init__(self, state, target):
        self.state = state 
        self.target = target
                
    def depth_bounded_search(self,depth_limit):
        visited = set()
        step = 0
        # current, prev, depth
        stack = [(self.state, [(self.state,0,"Start")], 0, 0)]
        while stack:
            current, path, depth, step_count = stack.pop()
            state_tuple = tuple(map(tuple, current))
            step += 1
            if current == self.target:
                return path + [(current, depth,"Goal")], depth + 1, step
            if state_tuple in visited:
                continue
            
            visited.add(state_tuple)
            
            if depth < depth_limit:
                adj_node = get_adj_node(current)
                for adj, move in adj_node:
                    if tuple(map(tuple, adj)) not in visited:
                        stack.append((adj, path + [(adj, depth + 1,move)], depth + 1,step_count + 1))
        
        return None, -1, step

    def ids(self):
        for depth in range(20):
            result, max_current_depth, steps = self.depth_bounded_search(depth)
            if result:
                return result, max_current_depth, steps
        return None, -1, -1

            
        
                