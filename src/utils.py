import random
def get_pos(state, element):
    for row, tile_row in enumerate(state):
        for col, tile in enumerate(tile_row):
            if tile == element:
                return row,col
    return None   

def get_adj_node(state):
    list_adj_node = []
    x, y = get_pos(state, 0)
    directions = { "Up": (-1,0), "Down": (1,0), "Left":(0,-1), "Right": (0,1)}
    
    for move, (dx, dy) in directions.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]#copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny],new_state[x][y]
            list_adj_node.append((new_state, move))
            
    return list_adj_node

def heuristic(state, target):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = get_pos(target, state[i][j])
                h += abs(goal_x - i) + abs(goal_y - j)
    return h 

def is_solvable(state):
    flat = [ num for row in state for num in row if num != 0]
    inv_count = sum( 1 for i in range(len(flat) - 1) for j in range(i + 1, len(flat)) if flat[i] > flat[j])
    return inv_count % 2 == 0

def generate_random_state():
    numbers = list(range(9))
    while True:
        random.shuffle(numbers)
        grid = [numbers[i:i+3] for i in range( 0, 9, 3)]
        if is_solvable(grid):
            return grid         
    
def is_solvable(state, target):
    flat = [x for row in state for x in row if x != 0]
    inversions = 0
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1
    target_flat = [x for row in target for x in row if x != 0]
    target_inversions = 0
    for i in range(len(target_flat)):
        for j in range(i + 1, len(target_flat)):
            if target_flat[i] > target_flat[j]:
                target_inversions += 1
    result = (inversions % 2) == (target_inversions % 2)
    return result

def get_adj_belief_states(belief_state):
    adj_belief_states = []
    possible_actions = ["Up", "Down", "Left", "Right"]
    
    for action in possible_actions:
        new_belief = set()
        for state in belief_state:
            adj_nodes = get_adj_node(state)
            for adj_state, move in adj_nodes:
                if move == action:
                    new_belief.add(tuple(map(tuple, adj_state)))
        if new_belief:
            new_belief_list = [list(map(list, state)) for state in new_belief]
            adj_belief_states.append((new_belief_list, action))
    
    return adj_belief_states

def create_observed_state(belief_state, blank_pos, observed_positions, partially_observable=False):
    observed = [['?' for _ in range(3)] for _ in range(3)]
    
    if not belief_state:
        return observed
    
    if blank_pos:
        row, col = blank_pos
        observed[row][col] = '0'
    
    if not partially_observable:
        for i in range(3):
            for j in range(3):
                values = {state[i][j] for state in belief_state if isinstance(state, list) and len(state) == 3 and all(isinstance(r, list) and len(r) == 3 for r in state)}
                if len(values) == 1:
                    observed[i][j] = str(values.pop())
    else:
        for row, col in observed_positions:
            values = {state[row][col] for state in belief_state if isinstance(state, list) and len(state) == 3 and all(isinstance(r, list) and len(r) == 3 for r in state)}
            if len(values) == 1:
                observed[row][col] = str(values.pop())
    
    return observed