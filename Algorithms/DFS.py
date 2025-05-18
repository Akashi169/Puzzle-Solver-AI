import copy
import os
import sys
from collections import deque
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))
from src.utils import*
class DFS:
    def __init__(self, state, target):
        self.target = target
        self.state = state
        self.variables = list(range(9))
        self.domain = {var: list(range(9)) for var in self.variables}
        
    def dfs(self): 
        stack = [(self.state, [(self.state, "Start")], 0)]
        visited = set()
        while stack:
            current, path, step_count = stack.pop()
            if tuple(map(tuple, current)) in visited:
                continue
            visited.add(tuple(map(tuple, current)))
            if current == self.target:
                return path + [(current, "Goal")], step_count
            
            adj_nodes = get_adj_node(current)
            for adj, move in adj_nodes:
                if tuple(map(tuple, adj)) not in visited:
                    stack.append((adj, path + [(adj, move)], step_count + 1))
        return None, -1
    
    def all_different_constraint(self, var, value, assignment):
        return value not in assignment.values()
        
    def select_unassigned_variable(self, assignment):
        for var in self.variables:
            if var not in assignment:
                return var 
        return None 
    
    def backtracking_search(self):
        assignment = {}
        history = []  
        step = 0  

        def create_grid(assignment):
            grid = [[0] * 3 for _ in range(3)]
            for var in assignment:
                row, col = var // 3, var % 3
                grid[row][col] = assignment[var]
            return grid

        def recursive_backtrack(assignment, history, step): 
            if len(assignment) == len(self.variables):
                grid = create_grid(assignment)
                history.append(copy.deepcopy(grid))  
                return step, history

            var = self.select_unassigned_variable(assignment)
            for value in self.domain[var]:
                if self.all_different_constraint(var, value, assignment):
                    assignment[var] = value
                    step += 1 
     
                    current_grid = create_grid(assignment)
                    history.append(copy.deepcopy(current_grid))
                    result_step, result_history = recursive_backtrack(assignment, history, step)
                    if result_step is not None:
                        return result_step, result_history
                    del assignment[var] 
                    history.pop()  
                    step -= 1 
            return None, None

        step, history = recursive_backtrack(assignment, history, step)
        return step, history if step is not None else (0, [])
    
    def dfs_with_forward_checking(self):
        def manhattan_distance(state):
            distance = 0
            for i in range(3):
                for j in range(3):
                    value = state[i][j]
                    if value != 0:
                        ti, tj = get_pos(state, value)
                        distance += abs(i - ti) + abs(j - tj)
            return distance

        def tiles_out_of_place(state):
            count = 0
            for i in range(3):
                for j in range(3):
                    if state[i][j] != self.target[i][j] and state[i][j] != 0:
                        count += 1
            return count
        

    
        if not is_solvable(self.state, self.target):
 
            return None, -1, 0

        stack = [(self.state, [(self.state, "Start")], 0, manhattan_distance(self.state), tiles_out_of_place(self.state))]
        visited = set()
        nodes_explored = 0
        solvable_check_interval = 100  
        
        while stack:
            current, path, step_count, current_heuristic, current_tiles = stack.pop()
            state_tuple = tuple(map(tuple, current))
            if state_tuple in visited:
                continue
            visited.add(state_tuple)
            nodes_explored += 1
            
            if current == self.target:
                return path + [(current, "Goal")], step_count, nodes_explored
            
 
            if nodes_explored % solvable_check_interval == 0 and not is_solvable(current, self.target):
                continue
            
            adj_nodes = get_adj_node(current)
            if not adj_nodes:
                continue
            
            valid_adj_nodes = []
            for adj, move in adj_nodes:
                adj_tuple = tuple(map(tuple, adj))
                if adj_tuple not in visited:
                    heuristic = manhattan_distance(adj)
                    tiles_heuristic = tiles_out_of_place(adj)
                    if heuristic <= current_heuristic + 1 and tiles_heuristic <= current_tiles + 1:
                        valid_adj_nodes.append((adj, move, heuristic, tiles_heuristic))
            
            for adj, move, heuristic, tiles_heuristic in valid_adj_nodes:
                stack.append((adj, path + [(adj, move)], step_count + 1, heuristic, tiles_heuristic))
        
        return None, -1, nodes_explored
                    
        
        

    def ac3(self, domains, arcs):
        queue = deque(arcs)
        while queue:
            (xi, xj) = queue.popleft()
            removed = False 
            new_domain = domains[xi][:]
            for x in domains[xi]:
                if not any(x != y for y in domains[xj]):
                    new_domain.remove(x)
                    removed = True 
            domains[xi] = new_domain 
            if removed:
                if not domains[xi]:
                    return False 
                
                for xk in [v for v in self.variables if v != xi and v!= xj]:
                    queue.append((xk, xi))
        return True 
    def dfs_with_ac3(self):
                    
        if not is_solvable(self.state, self.target):
            return None, -1, 0    
    
        stack = [(self.state, [(self.state, "Start")], 0)]
        visited = set()
        nodes_explored = 0
        ac3_interval = 50 
        
        while stack:
            current, path, step_count = stack.pop()
            state_tuple = tuple(map(tuple, current))
            if state_tuple in visited:
                continue
            visited.add(state_tuple)
            nodes_explored += 1 
            
            if current == self.target:
                return path + [(current, "Goal")], step_count, nodes_explored 
            
            adj_nodes = get_adj_node(current)
            if not adj_nodes:
                continue 
            
            valid_adj_nodes = []
            
            domains = { var: [] for var in self.variables}
            for i in range(3):
                for j in range(3):
                    var = i * 3 + j 
                    domains[var] = [current[i][j]]
            arcs = [(i,j) for i in self.variables for j in self.variables if i < j]
            
            for adj, move in adj_nodes: 
                adj_tuple = tuple(map(tuple, adj))
                if adj_tuple not in visited: 
                    if nodes_explored % ac3_interval == 0:
                        adj_domains = copy.deepcopy(domains)
                        for i in range(3):
                            for j in range(3):
                                var = i*3 + j
                                adj_domains[var] = [adj[i][j]]
                                
                        if self.ac3(adj_domains, arcs):
                            valid_adj_nodes.append((adj, move))
                    else:
                        valid_adj_nodes.append((adj, move))
            for adj, move in valid_adj_nodes:
                stack.append((adj, path + [(adj, move)], step_count + 1))
        
        return None, -1, nodes_explored
            