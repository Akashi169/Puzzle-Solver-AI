#from src.main import*
import copy
import os
import sys
import heapq
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))
from src.utils import*
class AStar:
    def __init__(self,state,target):
        self.state = state
        self.target = target         
                      
    def a_star(self):
        #f, g, current, prev, total_steps
        open_list = []
        heapq.heappush(open_list, (0 + heuristic(self.state, self.target), 0, self.state, [(self.state, "Start")], 0))

        visited = set()
        while open_list:
            f,g, current, path, step_count = heapq.heappop(open_list)
            
            if current == self.target:
                return path + [(current, "Goal")], step_count
            
            if tuple(map(tuple,current)) in visited:
                continue
            
            visited.add(tuple(map(tuple,current)))
            
            for adj, move in get_adj_node(current):
                #print(f"Checking move: {move}, State: {adj}")
                if tuple(map(tuple,adj)) not in visited:
                    heapq.heappush(open_list,(g + 1 + heuristic(adj, self.target), g + 1, adj, path + [(adj, move)], step_count + 1))
                    
        return None, -1
                          
                
                 
                