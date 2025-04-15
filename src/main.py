#import pygame
import sys 
import os
import tracemalloc 
import time
import pygame
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from Algorithms.AStar import *
from Algorithms.AID import *
from Algorithms.DFS import*
from Algorithms.BFS import*
from Algorithms.UCS import*
from Algorithms.IDS import*
from Algorithms.GBF import*
from Algorithms.SHC import*
from Algorithms.SAHC import*
from Algorithms.StochasticHC import *
from Algorithms.SA import *
from Algorithms.BeamSearch import*
from Algorithms.AO import*
from src.Settings import*
from Graphics.Button import*
#puzzle_start = [[2, 6, 5], [0, 8, 7], [4, 3, 1]]
#puzzle_start = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
puzzle_start = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
#puzzle_start = [[1, 2, 3], [4, 5, 6], [8, 0, 7]]
#puzzle_start = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
width_button = 150
x_button = 50
buttons = {
    "IDS": Button(x_button, tile_size*1.5, width_button, tile_size*0.4, r"Graphics\assets\images\ids.png", button_algorithm),
    "UCS": Button(x_button, tile_size*2.1, width_button, tile_size*0.4, r"Graphics\assets\images\ucs.png", button_algorithm),
    "IDA": Button(x_button, tile_size*2.7, width_button, tile_size*0.4, r"Graphics\assets\images\ida.png", button_algorithm),
    "AStar": Button(x_button, tile_size*3.3, width_button, tile_size*0.4, r"Graphics\assets\images\astar.png", button_algorithm),
    "BFS": Button(x_button, tile_size*3.9, width_button, tile_size*0.4, r"Graphics\assets\images\bfs.png", button_algorithm),
    "DFS": Button(x_button + 200, tile_size*1.5, width_button, tile_size*0.4, r"Graphics\assets\images\dfs.png", button_algorithm),
    "GBF": Button(x_button + 200, tile_size*2.1, width_button, tile_size*0.4, r"Graphics\assets\images\gs.png", button_algorithm),
    "SHC": Button(x_button + 200, tile_size*2.7, width_button, tile_size*0.4, r"Graphics\assets\images\shc.png", button_algorithm),
    "SAHC": Button(x_button + 200, tile_size*3.3, width_button, tile_size*0.4, r"Graphics\assets\images\sahc.png", button_algorithm),
    "StochasticHC":Button(x_button + 200, tile_size*3.9, width_button, tile_size*0.4, r"Graphics\assets\images\stochastichc.png", button_algorithm),
    "SA": Button(x_button + 200, tile_size*4.5, width_button, tile_size*0.4, r"Graphics\assets\images\sa.png", button_algorithm),
    "BS": Button(x_button, tile_size*4.5, width_button, tile_size*0.4, r"Graphics\assets\images\bs.png", button_algorithm),
    "AO": Button(x_button + 200, tile_size*5.1, width_button, tile_size*0.4, r"Graphics\assets\images\bs.png", button_algorithm)
}
button_detail = Button(x_button, tile_size*5.1, width_button*0.8, tile_size*0.3, r"Graphics\assets\images\detail.png", button_algorithm)
solution_path = []
threshold_list = []
state_visited = []
state = puzzle_start
total_steps = 0
lv_current_state = 0
current_depth, move, cost = 0, 0, 0
peak_mem = 0
around_time = 0
algorithms = ""
lv_current_thres = 0
pressed_detail = False

scroll_offset = 0
scroll_speed = 150

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("8 Puzzle")
font = pygame.font.Font(None, 36)


                


def draw_puzzle(state, screen, tile_size, x, y, size, type):
    for row, tiles in enumerate(state):
        for col, tile in enumerate(tiles):
            if type == 1 and (row,col) in [(0,1),(1,0),(1,2),(2,1)]:               
                pygame.draw.rect(screen, (255,242,0), [col * tile_size + x, row * tile_size + y, tile_size, tile_size])  
            elif type == 1:
                pygame.draw.rect(screen, (42,131,233), [col * tile_size + x, row * tile_size + y, tile_size, tile_size])  
            else:
                pygame.draw.rect(screen, 'red', [col * tile_size + x, row * tile_size + y, tile_size, tile_size])
            
            if tile != 0:
                font = pygame.font.Font(None, size)
                color = (255, 255, 255) if type != 1 else (0,0,0)
                text_surface = font.render(str(tile), True, color)
                text_rect = text_surface.get_rect(center=(col * tile_size + tile_size // 2 + x, row * tile_size + tile_size // 2+y))
                screen.blit(text_surface, text_rect)
    
    for row in range(3):
        for col in range(3):
            pygame.draw.line(screen, 'white', (col * tile_size + x, y), (col * tile_size + x, 3 * tile_size + y))
            pygame.draw.line(screen, 'white', (x, row * tile_size + y), (3 * tile_size + x, row * tile_size + y))


def draw_history_view(screen, solution_path, tile_size=50, margin_x=30, margin_y=30): 
    screen.fill("#3B4046")
    grid_width = tile_size * 3
    grid_height = tile_size * 3
    spacing = 20
    
    max_grids_per_row = max((screen_width - 2 * margin_x) // (grid_width + spacing), 1)
    
    num_rows = math.ceil(len(solution_path)/max_grids_per_row)
    content_height = num_rows * (grid_height + spacing)
    max_scroll = max(0, content_height - screen_height + 2 * margin_y)
    
    for i, item in enumerate(solution_path):
        if algorithms in ["BFS", "DFS", "AStar", "IDA"]:
            state, move = item 
        elif algorithms in ["UCS"]:
            state, cost, move = item 
        elif algorithms in [ "SAHC", "StochasticHC", "SA", "BS", "SHC"]:
            state, h, move = item
        else:
            continue
        row = i // max_grids_per_row
        col = i % max_grids_per_row
        x = margin_x + col * (grid_width + spacing)
        y = margin_y + row * (grid_height + spacing) - scroll_offset     
        
            
    if algorithms in ["BFS", "DFS", "AStar", "IDA"]:
        for i, (state,move) in enumerate(solution_path):
            row = i // max_grids_per_row
            col = i % max_grids_per_row
            x = margin_x + col * (grid_width + spacing)
            y = margin_y + row * (grid_height + spacing) - scroll_offset
            
            if 0 <= y < screen_height - margin_y:
                draw_puzzle(state, screen, tile_size, x, y, size=36, type=1)
    
    #state, cost, move 
    elif algorithms in ["UCS"]:
        for i, (state, cost, move) in enumerate(solution_path):
            row = i // max_grids_per_row
            col = i % max_grids_per_row
            x = margin_x + col * (grid_width + spacing)
            y = margin_y + row * (grid_height + spacing) - scroll_offset
            
            if 0 <= y < screen_height - margin_y:
                draw_puzzle(state, screen, tile_size, x, y, size=36, type=1)
    elif algorithms in [ "SAHC", "StochasticHC", "SA", "BS", "SHC"]:

        for i, (state, h, move) in enumerate(solution_path):
            row = i // max_grids_per_row
            col = i % max_grids_per_row
            x = margin_x + col * (grid_width + spacing)
            y = margin_y + row * (grid_height + spacing) - scroll_offset
            
            if 0 <= y < screen_height - margin_y:
                draw_puzzle(state, screen, tile_size, x, y, size=36, type=1)
        
counter, lv_current_state = 0, 0
clock = pygame.time.Clock()
running = True
is_start_count = False
while running:
    clock.tick(2)
    screen.fill("#3B4046")
    if pressed_detail == False:
        button_algorithm.draw(screen)
        screen.blit(img_tile,(0,0))
        # if button_detail.is_pressed() == True:
        #     draw_history_view(screen, solution_path)
        screen.blit(img_start,(tile_size*0.8,540))
        screen.blit(img_target,(tile_size*2.7,545))
        pygame.draw.rect(screen, 'black',[450, 600, 450, 125], border_radius = 20)
        font = pygame.font.Font(None, 28)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for algo, button in buttons.items():
                    if button.is_pressed():
                        algorithms = algo
                        tracemalloc.start()
                        start_time = time.time()
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
                            solver = BFS(puzzle_start, target)
                            solution_path, solution_depth, total_steps = solver.bfs()                   
                        elif algo == "DFS":
                            solver = DFS(puzzle_start, target)
                            solution_path, total_steps = solver.dfs()                      
                        elif algo == "GBF":
                            solver = GBF(puzzle_start, target)
                            state_visited ,solution_path, total_steps = solver.gbf()
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
                            solution_path, plan, total_steps = solver.search()
                        is_start_count = True
                            
                        end_time = time.time()
                        around_time = end_time - start_time
                        current_mem, peak_mem = tracemalloc.get_traced_memory()
                        tracemalloc.stop()     
                
        if is_start_count:
            counter += 1
        if counter >= 80:
            counter = 0
            is_start_count = False
        if lv_current_state < len(solution_path) - 1 and algorithms != "GBF":
            lv_current_state += 1
        if algorithms == "GBF" and lv_current_state < len(state_visited) - 1:
            lv_current_state += 1       
            
        if algorithms == "IDS":
            state, current_depth, move = solution_path[lv_current_state] 
            screen.blit(font.render(f"Current depth: {current_depth}", True, "white"), (690,685))
            
        elif algorithms == "UCS":
            state, cost, move = solution_path[lv_current_state] 
            screen.blit(font.render(f"Current depth: {current_depth}", True, "white"), (690,615))
            screen.blit(font.render(f"Cost: {cost}", True, "white"), (690,650))
            
        elif algorithms == "IDA": 
            if lv_current_thres < len(threshold_list) - 1 and lv_current_state >= threshold_list[lv_current_thres]:
                lv_current_thres += 1   
            screen.blit(font.render(f"Solution threshold: {threshold_list[lv_current_thres]}",True, "white"), (690,615))
            state, move = solution_path[lv_current_state]

        elif algorithms in ["DFS", "BFS", "AStar"] :
            state, move = solution_path[lv_current_state]
        elif algorithms == "GBF":
            step, state, h, move = state_visited[lv_current_state]
            
        elif algorithms in [ "SAHC", "StochasticHC", "SA", "BS", "SHC"]:
            state, h, move = solution_path[lv_current_state]
            screen.blit(font.render(f"Expanded nodes: {expanded_nodes}",True,"white"),(690,615))
            screen.blit(font.render(f"Current h:{h}",True,"White"),(690,650))
                
        #screen.blit(font.render(f"Memory: {round(peak_mem/(1024*1024),2)} MB", True, "white"), (465,615))
        screen.blit(font.render(f"Runtime: {round((around_time)*1000,3)} ms", True, "white"), (465,650))
        screen.blit(font.render(f"Total step: {total_steps}", True, "white"), (465,685))
        
        draw_puzzle(state, screen, tile_size*1.5, 450, 125, 54, 1) 
        draw_puzzle(puzzle_start, screen, tile_size*0.5, 50, 575, 36, 0)
        draw_puzzle(target, screen, tile_size*0.5, 250, 575, 36, 0)
        if button_detail.is_pressed() == True:
            pressed_detail = True
            
    else:
        draw_history_view(screen, solution_path)
        #button_detail.draw(screen)
        if scroll_offset < (len(solution_path) // 4) * (tile_size + 20) - screen_height + 30:
            scroll_offset += scroll_speed / 60
        else:
            scroll_offset = 0
        
        
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()

pygame.quit()
# Luu y total step va goal
