import heapq
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))
from src.utils import *

class AndOrSearch:
    def __init__(self, state, target):
        self.state = state
        self.target = target
        self.plan = []
        self.visited = set()
        self.step = 0
        # Lưu target_pos để tối ưu manhattan_distance
        self.target_pos = {}
        for i in range(3):
            for j in range(3):
                if target[i][j] != 0:
                    self.target_pos[target[i][j]] = (i, j)

    def manhattan_distance(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = state[i][j]
                if value != 0:
                    ti, tj = self.target_pos[value]
                    distance += abs(i - ti) + abs(j - tj)
        return distance

    def is_solvable(self, state):
        flat = [x for row in state for x in row if x != 0]
        inversions = 0
        for i in range(len(flat)):
            for j in range(i + 1, len(flat)):
                if flat[i] > flat[j]:
                    inversions += 1
        target_flat = [x for row in self.target for x in row if x != 0]
        target_inversions = 0
        for i in range(len(target_flat)):
            for j in range(i + 1, len(target_flat)):
                if target_flat[i] > target_flat[j]:
                    target_inversions += 1
        return (inversions % 2) == (target_inversions % 2)

    def or_search(self, state, path, depth=0):
        if depth > 1000:  # Giới hạn độ sâu đệ quy
            return False
        
        state_tuple = tuple(map(tuple, state))
        if state == self.target:
            return True
        
        if state_tuple in self.visited:
            return False
        self.visited.add(state_tuple)

        # Sắp xếp trạng thái lân cận theo manhattan_distance
        adj_nodes = sorted(get_adj_node(state), key=lambda x: self.manhattan_distance(x[0]))
        for s, action in adj_nodes:
            self.step += 1
            if self.and_search(s, path + [state_tuple], depth + 1):
                self.plan.append((s, action))
                return True
        return False

    def and_search(self, state, path, depth=0):
        return self.or_search(state, path, depth)

    def search(self):
        if not self.is_solvable(self.state):
            return False, [], 0
        
        self.plan = []
        self.visited = set()
        self.step = 0
        found = self.or_search(self.state, [], 0)
        if not found:
            self.plan = []
            return False, [], self.step
        
        self.plan.reverse()
        return [(self.state, "Start")] + self.plan + [(self.target, "Goal")], self.step