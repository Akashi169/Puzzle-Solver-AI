import copy
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))
from src.utils import*
class DFS:
    def __init__(self, state, target):
        self.target = target
        self.state = state
    def dfs(self): 
        # current, prev, total_steps
        stack = [(self.state, [(self.state, "Start")], 0)]
        visited = set()
        while stack:
            current, path, step_count= stack.pop()
            if tuple(map(tuple, current)) in visited:
                continue
            visited.add(tuple(map(tuple,current)))
            if current == self.target:
                return path + [(current, "Goal")], step_count
            
            adj_nodes = get_adj_node(current)
            for adj, move in adj_nodes:
                if tuple(map(tuple,adj)) not in visited:
                    stack.append((adj, path + [(adj, move)], step_count + 1))
        return None, -1

