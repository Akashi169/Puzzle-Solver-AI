import heapq
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.utils import *

class GBF:
    def __init__(self, state, target):
        self.target = target
        self.state = state
    
    def get_adj_node(self, state):
        list_adj_node = []
        x, y = get_pos(state, 0)
        directions = {"Up": (-1,0), "Down": (1,0), "Left":(0,-1), "Right": (0,1)}
        
        for move, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy 
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                list_adj_node.append((new_state, move, heuristic(new_state, self.target)))
        
        return list_adj_node
    
    def gbf(self):
        open_list = []
        heapq.heappush(open_list, (heuristic(self.state, self.target), self.state, [], 0))
        visited = set()
        step = 0
        state_visited = []
        
        while open_list:
            h, current, path, step_count = heapq.heappop(open_list)
            
            if tuple(map(tuple, current)) in visited:
                continue 
            
            visited.add(tuple(map(tuple, current)))
            move = path[-1] if path else "Start"
            state_visited.append((step, current, h, move))
            step += 1
            
            if current == self.target:
                return state_visited, path, step_count 
            
            for adj, move, h_new in self.get_adj_node(current):
                if tuple(map(tuple, adj)) not in visited:
                    heapq.heappush(open_list, (h_new, adj, path + [move], step))
                    
        return None, None, -1
