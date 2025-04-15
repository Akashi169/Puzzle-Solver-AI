import copy
from collections import deque
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))
from src.utils import*
class BFS:
    def __init__(self, state, target):
        self.target = target
        self.state = state
    def bfs(self):    
        #current, path, depth, total_steps
        queue = deque([(self.state, [(self.state, "Start")], 0, 0)])
        visited = set()
        step = 0
        while queue:
            current, path, depth, step_count = queue.popleft()
     
            if current == self.target:
                return path + [(current, "Goal")], depth, step
            if tuple(map(tuple,current)) in visited:
                continue
            visited.add(tuple(map(tuple,current)))
            step += 1
            adj_nodes = get_adj_node(current)
            for adj, move in adj_nodes:
                if tuple(map(tuple,adj)) not in visited:
                    queue.append((adj, path + [(adj, move)], depth + 1, step_count + 1))
        return None, -1, -1

