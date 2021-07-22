import pygame


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.clock = pygame.time.Clock()
        self.FPS = 60
    
    def game_loop(self):
        running = True
        
        while running:
            self.clock.tick(self.FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            maze = self.model.maze
            path = self.model.path
            self.view.draw_display(maze, path)
