import heapq
import os
import sys 
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))
from src.utils import*
class UCS:
    def __init__(self, state, target):
        self.state = state 
        self.target = target

    def get_adj_node(self,state):
        list_adj_node = []
        x, y = get_pos(state, 0)
        direction = { "Up": (-1,0,1), "Down":(1,0,1), "Left":(0,-1,2), "Right": (0,1,2)}
        
        for move, (dx, dy, cost) in direction.items():
            nx, ny = dx + x, dy + y
            if 0 <= dx + x < 3 and 0 <= dy + y < 3:
                new_state = [row[:] for row in state] #copy.deepcopy(state)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                list_adj_node.append((new_state,move, cost))
                
        return list_adj_node
    
    def ucs(self):

        open_list = []
        #cost, state, path, depth, total_step
        heapq.heappush(open_list,(0, self.state, [(self.state, 0, "Start")], 0,0))
        visited = set()
        step = 0
        while open_list:
            cost, current, path, depth, step_count = heapq.heappop(open_list)
            state_tuple = tuple(map(tuple, current))
            step += 1
            if current == self.target:
                return path + [(current, cost, "Goal")], (depth, cost), step
            if state_tuple in visited:
                continue
            visited.add((state_tuple))
                   
            for new_state,move, step_cost in self.get_adj_node(current):
                heapq.heappush(open_list, (cost + step_cost, new_state, path + [(new_state, cost + step_cost, move)], depth + 1, step_count + 1))
  
        return None, (-1, -1), -1



        
        