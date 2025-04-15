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