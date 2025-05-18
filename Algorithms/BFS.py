import copy
from collections import deque
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))
from src.utils import *

class BFS:
    def __init__(self, state, target):
        self.state = state
        self.target = target

    def bfs(self, partially_observable=False):
        is_belief_state = (isinstance(self.state, list) and self.state and 
                          all(isinstance(s, list) and len(s) == 3 and 
                              all(isinstance(r, list) and len(r) == 3 for r in s) for s in self.state))

        if not is_belief_state:
            if not is_solvable(self.state, self.target):
                return [], 0, 0, [] if partially_observable else []
            blank_pos = get_pos(self.state, 0) if partially_observable else None 
            observed_positions = set() if partially_observable else {(i, j) for i in range(3) for j in range(3)}
            if partially_observable and blank_pos:
                row, col = blank_pos
                observed_positions.add((row, col))
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < 3 and 0 <= nc < 3:
                        observed_positions.add((nr, nc))
            queue = deque([(self.state, [(self.state, "Start")], 0, [self.state], blank_pos, observed_positions)])
            visited = set([tuple(map(tuple, self.state))])
        else:
            blank_pos = get_pos(self.state[0], 0) if partially_observable else None
            observed_positions = set() if partially_observable else {(i, j) for i in range(3) for j in range(3)}
            if partially_observable and blank_pos:
                row, col = blank_pos
                observed_positions.add((row, col))
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < 3 and 0 <= nc < 3:
                        observed_positions.add((nr, nc))
            queue = deque([(self.state, [[(s, "Start")] for s in self.state], 0, self.state, blank_pos, observed_positions)])
            visited = set([frozenset(tuple(map(tuple, state)) for state in self.state)])

        nodes_explored = 0
        max_steps = 10000

        while queue and nodes_explored < max_steps:
            current, path, depth, current_belief, blank_pos, observed_positions = queue.popleft()
            nodes_explored += 1
            
            if not is_belief_state:
                if current == self.target:
                    if partially_observable:
                        observed_states = []
                        temp_blank_pos = get_pos(self.state, 0)
                        temp_observed_positions = set([(temp_blank_pos[0], temp_blank_pos[1])])
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = temp_blank_pos[0] + dr, temp_blank_pos[1] + dc
                            if 0 <= nr < 3 and 0 <= nc < 3:
                                temp_observed_positions.add((nr, nc))
                        solution_path = path + [(current, "Goal")]
                        for state, _ in solution_path:
                            observed_states.append(create_observed_state([state], temp_blank_pos, temp_observed_positions, partially_observable))
                            temp_blank_pos = get_pos(state, 0)
                            temp_observed_positions.add((temp_blank_pos[0], temp_blank_pos[1]))
                            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nr, nc = temp_blank_pos[0] + dr, temp_blank_pos[1] + dc
                                if 0 <= nr < 3 and 0 <= nc < 3:
                                    temp_observed_positions.add((nr, nc))
                        return solution_path, depth, nodes_explored, observed_states
                    return path + [(current, "Goal")], depth, nodes_explored
            else:
                for i, state in enumerate(current):
                    if state == self.target:
                        path1 = path[0] + [(current[0], "Goal" if i == 0 else path[0][-1][1])]
                        path2 = path[1] + [(current[1], "Goal" if i == 1 else path[1][-1][1])] if len(path) > 1 else path[0]
                        if partially_observable:
                            observed_states = []
                            temp_blank_pos = get_pos(self.state[1], 0)  # Use state from path2 for initial blank_pos
                            temp_observed_positions = set([(temp_blank_pos[0], temp_blank_pos[1])])
                            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nr, nc = temp_blank_pos[0] + dr, temp_blank_pos[1] + dc
                                if 0 <= nr < 3 and 0 <= nc < 3:
                                    temp_observed_positions.add((nr, nc))
                            for state2, _ in path2:  # Iterate over path2 only
                                observed_states.append(create_observed_state([state2], temp_blank_pos, temp_observed_positions, partially_observable))
                                temp_blank_pos = get_pos(state2, 0)
                                temp_observed_positions.add((temp_blank_pos[0], temp_blank_pos[1]))
                                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                    nr, nc = temp_blank_pos[0] + dr, temp_blank_pos[1] + dc
                                    if 0 <= nr < 3 and 0 <= nc < 3:
                                        temp_observed_positions.add((nr, nc))
                            return [path1, path2], depth, nodes_explored, observed_states
                        return [path1, path2], depth, nodes_explored

            adj_nodes = get_adj_belief_states(current) if is_belief_state else get_adj_node(current)

            for adj, move in adj_nodes:
                adj_key = (frozenset(tuple(map(tuple, state)) for state in adj) 
                          if is_belief_state else tuple(map(tuple, adj)))
                
                if adj_key not in visited:
                    visited.add(adj_key)
                    new_blank_pos = get_pos(adj[0], 0) if partially_observable and is_belief_state else (get_pos(adj, 0) if partially_observable else None)
                    new_observed_positions = observed_positions.copy()
                    if partially_observable and blank_pos:
                        old_row, old_col = blank_pos
                        new_observed_positions.add((old_row, old_col))
                    if partially_observable and new_blank_pos:
                        row, col = new_blank_pos
                        new_observed_positions.add((row, col))
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < 3 and 0 <= nc < 3:
                                new_observed_positions.add((nr, nc))
                    
                    if is_belief_state:
                        new_path = []
                        for i in range(min(len(adj), len(path))):
                            if isinstance(adj[i], list) and len(adj[i]) == 3 and all(isinstance(r, list) and len(r) == 3 for r in adj[i]):
                                new_path.append(path[i] + [(adj[i], move)])
                            else:
                                new_path.append(path[i]) 
                        for i in range(len(adj) - len(new_path)):
                            new_path.append(new_path[-1] if new_path else path[0])
                        queue.append((adj, new_path, depth + 1, adj, new_blank_pos, new_observed_positions))
                    else:
                        queue.append((adj, path + [(adj, move)], depth + 1, [adj], new_blank_pos, new_observed_positions))

        if partially_observable:
            return [], 0, nodes_explored, []
        return [], 0, nodes_explored