import sys 
import os
import tracemalloc 
import time
import io
import pygame
import math
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from Algorithms.AStar import *
from Graphics.BarChart import *
from Algorithms.AID import *
from Algorithms.DFS import *
from Algorithms.BFS import *
from Algorithms.UCS import *
from Algorithms.IDS import *
from Algorithms.GBF import *
from Algorithms.SHC import *
from Algorithms.SAHC import *
from Algorithms.StochasticHC import *
from Algorithms.SA import *
from Algorithms.BeamSearch import *
from Algorithms.AO import *
from Algorithms.GeneticAlgorithm import *
from Algorithms.RL import *

from src.Settings import *
from Graphics.Button import *
from initial_varible import *
from src.utils import get_adj_node, get_pos, create_observed_state

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("8 Puzzle")
font = pygame.font.Font(None, 36)
another_font = pygame.font.Font(None, 28)

def draw_puzzle(state, screen, tile_size, x, y, size, type):
    for row, tiles in enumerate(state): 
        for col, tile in enumerate(tiles):
            if type == 1 and (row,col) in [(0,1),(1,0),(1,2),(2,1)]:               
                pygame.draw.rect(screen, (255,242,0), [col * tile_size + x, row * tile_size + y, tile_size, tile_size])  
            elif type == 1:
                pygame.draw.rect(screen, (42,131,233), [col * tile_size + x, row * tile_size + y, tile_size, tile_size])  
            else:
                pygame.draw.rect(screen, 'red', [col * tile_size + x, row * tile_size + y, tile_size, tile_size])
            
            if tile is not None and tile != -1:  # Handle None or placeholder
                font = pygame.font.Font(None, size)
                color = (255, 255, 255) if type != 1 else (0,0,0)
                text_surface = font.render(str(tile), True, color)
                text_rect = text_surface.get_rect(center=(col * tile_size + tile_size // 2 + x, row * tile_size + tile_size // 2 + y))
                screen.blit(text_surface, text_rect)
    
    for row in range(3):
        for col in range(3):
            pygame.draw.line(screen, 'white', (col * tile_size + x, y), (col * tile_size + x, 3 * tile_size + y))
            pygame.draw.line(screen, 'white', (x, row * tile_size + y), (3 * tile_size + x, row * tile_size + y))

def draw_history_view(screen, solution_path, tile_size=50, margin_x=30, margin_y=30): 
    screen.fill("#3B4046")
    if not solution_path or (belief_state_mode and solution_path == [[], []]):
        font = pygame.font.Font(None, 36)
        screen.blit(font.render("No solution found", True, "White"), (screen_width // 2 - 100, screen_height // 2))
        return 0
    
    grid_width = tile_size * 6.2 if belief_state_mode else tile_size * 3.1
    grid_height = tile_size * 3
    spacing = 30
    
    max_grids_per_row = max((screen_width - 2 * margin_x) // (grid_width + spacing), 1)
    num_rows = math.ceil((len(solution_path[0]) if belief_state_mode else len(solution_path)) / max_grids_per_row)
    content_height = num_rows * grid_height + (num_rows - 1) * spacing + 2 * margin_y
    max_scroll = max(0, content_height - screen_height)
    
    for i in range(len(solution_path[0]) if belief_state_mode else len(solution_path)):
        if algorithms in ["BFS", "DFS", "AStar", "IDA", "BacktrackingFC"]:
            if belief_state_mode:
                state1, move1 = solution_path[0][i]
                state2, move2 = solution_path[1][i]
                state = [state1, state2]
            else:
                state, move = solution_path[i]
        elif algorithms in ["UCS"]:
            state, cost, move = solution_path[i]
        elif algorithms in ["SAHC", "StochasticHC", "SA", "BS", "SHC"]:
            state, h, move = solution_path[i]
        elif algorithms == "GeneticAlgorithm":
            step, state, h = solution_path[i]
        elif algorithms == "BSA":
            step, state = solution_path[i]
        
        row = i // max_grids_per_row
        col = i % max_grids_per_row
        x = margin_x + col * (grid_width + spacing)
        y = margin_y + row * (grid_height + spacing) - scroll_offset     
        
        if y + grid_height >= 0 and y < screen_height:
            if belief_state_mode:
                draw_puzzle(state1, screen, tile_size, x, y, size=36, type=1)
                draw_puzzle(state2, screen, tile_size, x + tile_size * 3 + 10, y, size=36, type=1)
            else:
                draw_puzzle(state, screen, tile_size, x, y, size=36, type=1)
    return max_scroll          

counter, lv_current_state = 0, 0
lv_current_state1, lv_current_state2 = 0, 0
clock = pygame.time.Clock()
running = True
is_start_count = False
state1, state2 = puzzle_start, puzzle_start
observed_states = []
prev_blank_pos = None
last_update = 0
update_interval = 500  # milliseconds

while running:
    current_time = pygame.time.get_ticks()
    clock.tick(2)
    screen.fill("#3B4046")
    if not history_mode:
        button_algorithm.draw(screen)
        screen.blit(img_tile, (0, 0))
        pygame.draw.rect(screen, 'black', [450 + 25, 600, 500 if (belief_state_mode or partially_observable) else 450, 125], border_radius=20)
        font = pygame.font.Font(None, 28)

        if solution_path and lv_current_state < (len(solution_path[0]) if belief_state_mode else len(solution_path)):
            if algorithms == "IDS":
                state, current_depth, move = solution_path[lv_current_state] 
                screen.blit(font.render(f"Current depth: {current_depth}", True, "white"), (690 + 25, 685))
            elif algorithms == "UCS":
                state, cost, move = solution_path[lv_current_state] 
                screen.blit(font.render(f"Current depth: {current_depth}", True, "white"), (690 + 25, 615))
                screen.blit(font.render(f"Cost: {cost}", True, "white"), (690 + 25, 650))
            elif algorithms == "IDA": 
                if lv_current_thres < len(threshold_list) - 1 and lv_current_state >= threshold_list[lv_current_thres]:
                    lv_current_thres += 1   
                screen.blit(font.render(f"Solution threshold: {threshold_list[lv_current_thres]}", True, "white"), (690 + 25, 615))
                state, move = solution_path[lv_current_state]
            elif algorithms in ["DFS", "BFS", "AStar", "DFSFC", "DFSAC3", "RL"]:
                if belief_state_mode:
                    if lv_current_state1 < len(solution_path1) and lv_current_state2 < len(solution_path2):
                        state1, move1 = solution_path1[lv_current_state1]
                        state2, move2 = solution_path2[lv_current_state2]
                        screen.blit(another_font.render(f"Step: {lv_current_state1}", True, "White"), (690 + 25, 615))
                        screen.blit(another_font.render(f"Move: {move1}", True, "White"), (690 + 25, 650))
                        screen.blit(another_font.render(f"Step: {lv_current_state2}", True, "White"), (690 + 160, 615))
                        screen.blit(another_font.render(f"Move: {move2}", True, "White"), (690 + 160, 650))
                else:
                    state, move = solution_path[lv_current_state]
                    screen.blit(font.render(f"Step: {lv_current_state}", True, "White"), (690 + 25, 615))
                    screen.blit(font.render(f"Move: {move}", True, "White"), (690 + 25, 650))
            elif algorithms == "GBF":
                step, state, h, move = state_visited[lv_current_state]
            elif algorithms in ["SAHC", "StochasticHC", "SA", "SHC", "BS"]:
                state, h, move = solution_path[lv_current_state]
                screen.blit(font.render(f"Expanded nodes: {expanded_nodes}", True, "white"), (690 + 25, 615))
                screen.blit(font.render(f"Current h: {h}", True, "White"), (690 + 25, 650))
            elif algorithms == "GeneticAlgorithm":
                step, state, h = solution_path[lv_current_state]
                screen.blit(font.render(f"Generation: {step}", True, "White"), (690 + 25, 615))
                screen.blit(font.render(f"Fitness: {h}", True, "white"), (690 + 25, 650))
            elif algorithms == "BSA":
                state = solution_path[lv_current_state]
                screen.blit(font.render(f"Step: {step}", True, "White"), (690 + 25, 615))
            elif algorithms == "AO":
                state, step = solution_path[lv_current_state]
                screen.blit(font.render(f"Step: {step}", True, "White"), (690 + 25, 615))
        else:
            state = puzzle_start if not belief_state_mode else [state1, state2]

        screen.blit(font.render(f"Memory: {round(peak_mem/(1024*1024), 2)} MB", True, "white"), (465 + 25, 615))
        screen.blit(font.render(f"Runtime: {round((around_time)*1000, 3)} ms", True, "white"), (465 + 25, 650))
        screen.blit(font.render(f"Total step: {total_steps}", True, "white"), (465 + 25, 685))
        
        if not belief_state_mode and not partially_observable:
            draw_puzzle(state, screen, tile_size*1.5, 450 + 25, 135, 54, 1)
            if algorithms not in ["GeneticAlgorithm", "BSA"]:
                draw_puzzle(puzzle_start, screen, tile_size*0.5, 50, 575, 36, 0)
                screen.blit(img_start, (tile_size*0.8, 540))
        if belief_state_mode or partially_observable:
            draw_puzzle(state1, screen, tile_size*0.8, 450 + 25, 135, 54, 1)
            draw_puzzle(state2, screen, tile_size*0.8, 700 + 25, 135, 54, 1)
        if partially_observable and observed_states and lv_current_state1 < len(observed_states):
            screen.blit(img_observed_state, (tile_size*0.8, 540))
            draw_puzzle(observed_states[lv_current_state1], screen, tile_size*0.5, 50, 575, 36, 0)
        
        if algorithms not in ["BSA"]:
            draw_puzzle(target, screen, tile_size*0.5, 250, 575, 36, 0)
            screen.blit(img_target, (tile_size*2.7, 545))
        
        if button_detail.is_pressed():
            history_mode = True
            scroll_offset = 0
        elif button_skip.is_pressed():
            lv_current_state = len(solution_path) - 1
        elif button_reset.is_pressed():
            algorithms = ""
            belief_state_mode = False
            partially_observable = False
            state = puzzle_start
            state1, state2 = puzzle_start, puzzle_start
            solution_path = []
            solution_path1, solution_path2 = [], []
            lv_current_state = 0
            lv_current_state1, lv_current_state2 = 0, 0
            total_steps = 0
            peak_mem = 0
            around_time = 0
            observed_states = []
            prev_blank_pos = None
        elif button_belief.is_pressed():
            belief_state_mode = True
            partially_observable = False
            adj_state = get_adj_node(puzzle_start)
            belief_state = [puzzle_start]
            if adj_state:
                belief_state.append(adj_state[0][0])
            puzzle = belief_state
            state1, state2 = puzzle[0], puzzle[1]
            solution_path = []
            solution_path1, solution_path2 = [], []
            lv_current_state = 0
            lv_current_state1, lv_current_state2 = 0, 0
            observed_states = []
        elif button_partially_observable.is_pressed():
            partially_observable = True
            belief_state_mode = True
            adj_state = get_adj_node(puzzle_start)
            belief_state = [puzzle_start]
            if adj_state:
                belief_state.append(adj_state[0][0])
            puzzle = belief_state
            state1, state2 = puzzle[0], puzzle[1]
            solution_path = []
            solution_path1, solution_path2 = [], []
            lv_current_state = 0
            lv_current_state1, lv_current_state2 = 0, 0
            observed_states = []
            prev_blank_pos = None
    elif history_mode:
        max_scroll = draw_history_view(screen, solution_path, tile_size=50, margin_x=30, margin_y=30)
    if button_chart.is_pressed():
        #print("True")
        is_chart = True
    
    if is_chart:
        
        screen_rect = screen.get_rect()
        #screen.fill("#3B4046")
        type = data if not is_chart_time else times
        value = 0 if not is_chart_time else 1
        screen.blit(draw_char(value, type, algorithms_name), screen_rect.topleft)
        if button_back.is_pressed():
            is_chart = False
            is_chart_time = False
        screen.blit(button_back.image, (button_back.x, button_back.y))
        screen.blit(button_time.image, (button_time.x, button_time.y))
        pygame.display.flip()
    if button_time.is_pressed():
        is_chart_time = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for algo, button in buttons.items():
                if button.is_pressed():
                    algorithms = algo
                    tracemalloc.start()
                    start_time = time.time()
                    lv_current_state = 0
                    lv_current_state1, lv_current_state2 = 0, 0
                    if algo == "IDS":
                        solver = IDS(puzzle_start, target)
                        solution_path, solution_depth, total_steps = solver.ids()
                    elif algo == "UCS":
                        solver = UCS(puzzle_start, target)
                        solution_path, (solution_depth, solution_cost), total_steps = solver.ucs()                        
                    elif algo == "IDA":
                        solver = IDA(puzzle_start, target)
                        solution_path, solution_depth, total_steps, threshold_list = solver.ida_star()                       
                    elif algo == "AStar":
                        solver = AStar(puzzle_start, target)
                        solution_path, total_steps = solver.a_star()                      
                    elif algo == "BFS":
                        solver = BFS(puzzle_start, target) if not belief_state_mode else BFS(puzzle, target)
                        result = solver.bfs(partially_observable=partially_observable)
                        if belief_state_mode:
                            if partially_observable:
                                solution_path, solution_depth, total_steps, observed_states = result
                            else:
                                solution_path, solution_depth, total_steps = result
                            if solution_path and solution_path != [[], []]:
                                solution_path1, solution_path2 = solution_path[0], solution_path[1]
                            else:
                                solution_path1, solution_path2 = [], []
                        else:
                            if partially_observable:
                                solution_path, solution_depth, total_steps, observed_states = result
                            else:
                                solution_path, solution_depth, total_steps = result
                            solution_path1, solution_path2 = [], []
                    elif algo == "DFS":
                        solver = DFS(puzzle_start, target)
                        solution_path, total_steps = solver.dfs()                      
                    elif algo == "GBF":
                        solver = GBF(puzzle_start, target)
                        state_visited, solution_path, total_steps = solver.gbf()
                    elif algo == "SHC":
                        solver = SHC(puzzle_start, target)
                        solution_path, (expanded_nodes, final_h), total_steps = solver.shc()
                    elif algo == "SAHC":
                        solver = SteepestAscentHC(puzzle_start, target)
                        solution_path, expanded_nodes, total_steps = solver.steepest_ascent_hc()
                    elif algo == "StochasticHC":
                        solver = StochasticHC(puzzle_start, target)
                        solution_path, expanded_nodes, total_steps = solver.stochastic_hc() 
                    elif algo == "BS":
                        solver = BeamSearch(puzzle_start, target)
                        solution_path, expanded_nodes, total_steps = solver.beam_search()   
                    elif algo == "SA":
                        solver = SimulatedAnnealing(puzzle_start, target)
                        solution_path, expanded_nodes, total_steps = solver.simulated_annealing_hc()  
                    elif algo == "AO":
                        solver = AndOrSearch(puzzle_start, target)
                        solution_path, total_steps = solver.search()
                    elif algo == "GeneticAlgorithm":
                        solver = GeneticAlgorithm(target)
                        result = solver.run() 
                        solution_path, fitness, status, generations, total_steps = result['solution_path'], result['fitness'], result['status'], result['generations'], result['total_steps']
                    elif algo == "BSA":
                        solver = DFS(puzzle_start, target)
                        step, solution_path = solver.backtracking_search()   
                    elif algo == "DFSFC":
                        solver = DFS(puzzle_start, target)
                        result = solver.dfs_with_forward_checking()
                        if result is not None and result[0] is not None:
                            solution_path, total_steps, nodes_explored = result
                        else:
                            solution_path, total_steps, nodes_explored = [], 0, 0
                    elif algo == "DFSAC3":
                        solver = DFS(puzzle_start, target)
                        result = solver.dfs_with_ac3()
                        if result is not None and result[0] is not None:
                            solution_path, total_steps, nodes_explored = result
                        else:
                            solution_path, total_steps, nodes_explored = [], 0, 0
                    elif algo == "RL":
                        solver = RLSolver(puzzle_start, target)
                        result = solver.solve()
                        if result is not None and result[0] is not None:
                            solution_path, total_steps, nodes_explored = result
                        else:
                            solution_path, total_steps, nodes_explored = [], 0, 0
                    is_start_count = True
                    end_time = time.time()
                    around_time = end_time - start_time
                    current_mem, peak_mem = tracemalloc.get_traced_memory()
                    tracemalloc.stop()     
        elif event.type == pygame.MOUSEWHEEL and history_mode:
            scroll_offset -= event.y * scroll_speed 
            scroll_offset = max(0, min(scroll_offset, max_scroll))
        elif event.type == pygame.KEYDOWN and solution_path:
            if event.key == pygame.K_SPACE and lv_current_state < (len(solution_path[0]) if belief_state_mode else len(solution_path)) - 1:
                lv_current_state += 1
                lv_current_state1 += 1
                lv_current_state2 += 1
                last_update = current_time

    if is_start_count:
        counter += 1
    if counter >= 80:
        counter = 0
        is_start_count = False   
    
    if solution_path and current_time - last_update > update_interval and not history_mode:
        if belief_state_mode:
            if lv_current_state1 < len(solution_path1) - 1:
                lv_current_state1 += 1
            if lv_current_state2 < len(solution_path2) - 1:
                lv_current_state2 += 1
            lv_current_state = min(lv_current_state1, lv_current_state2)
        elif lv_current_state < len(solution_path) - 1 and algorithms != "GBF":
            lv_current_state += 1
        if algorithms == "GBF" and lv_current_state < len(state_visited) - 1:
            lv_current_state += 1
        last_update = current_time
            
    pygame.display.flip()

pygame.quit()