#from src.main import*
import copy
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))
from src.utils import*
class IDA:
    def __init__(self,state,target):
        self.state = state
        self.target = target  
    
    def heuristic(self,state):
        h = 0 
        #Tong so buoc di chuyen cua cac o de dat duoc target
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    goal_x, goal_y = get_pos(self.target,state[i][j])
                    h += abs(goal_x-i) + abs(goal_y - j) 
        return h                    


    def ida_star(self):
        threshold = self.heuristic(self.state)
        total_steps = 0
        threshold_list = []
        while True:     
            threshold_list.append(threshold)
            visited = set()
            result, new_threshold, step_count, depth = self.ida_search(self.state, 0, threshold, visited, [(self.state, "Start")],total_steps)
            total_steps += step_count
            if result is not None:
                return result + [(self.target, "Goal")], depth, total_steps, threshold_list
            if new_threshold == float('inf'):
                return None, -1, -1, threshold_list
            threshold = new_threshold       


    def ida_search(self, current, g, threshold, visited, path, steps):
        f = g + self.heuristic(current)      
        if f > threshold:
            return None, f, steps, g     
        if current == self.target:
            return path, threshold, steps, g
        
        visited.add(tuple(map(tuple, current)))
        min_threshold = float('inf')
        steps += 1
        
        for adj, move in get_adj_node(current):
            if tuple(map(tuple,adj)) not in visited:
                result, new_threshold, new_steps, depth = self.ida_search(adj, g + 1, threshold, visited, path + [(adj, move)], steps)
                steps = new_steps
                if result is not None:
                    return result, threshold, steps, depth
                
                min_threshold = min(min_threshold, new_threshold)
        if tuple(map(tuple, current)) in visited:
            visited.remove(tuple(map(tuple, current)))

        return None, min_threshold, steps, g
                          
                
                 
                