import pygame
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))

# pygame.init()
# screen = pygame.display.set_mode((300, 300))
# pygame.display.set_caption("8 Puzzle - A* Search")
# font = pygame.font.Font(None, 36)
# tile_size = 100

# def draw_puzzle(state):
#     for row in range(3):
#         for col in range(3):   
#             pygame.draw.rect(screen, 'red', [col * tile_size, row * tile_size, tile_size, tile_size])
#             if state[row][col] != 0: 
#                 text_surface = font.render(str(state[row][col]), True, (255, 255, 255))
#                 text_rect = text_surface.get_rect(center=(col * tile_size + tile_size // 2, row * tile_size + tile_size // 2))
#                 screen.blit(text_surface, text_rect)
#     for i in range(4):
#         pygame.draw.line(screen, 'white', (i * tile_size, 0), (i * tile_size, 3 * tile_size))
#         pygame.draw.line(screen, 'white', (0, i * tile_size), (3 * tile_size, i * tile_size))
        


# counter, current_state = 0, 0
# clock = pygame.time.Clock()
# running = True

# while running:
#     clock.tick(60)
#     screen.fill((0, 0, 0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     counter += 1
#     if counter == 80:
#         counter = 0
#         if current_state < len(br) - 1:
#             current_state += 1


#     draw_puzzle(state['node'], screen, tile_size, 300, 500)    
#     draw_puzzle(a,screen, tile_size, 100, 75)
#     draw_puzzle(target,screen, tile_size, 400, 75)
#     pygame.display.flip()

# pygame.quit()