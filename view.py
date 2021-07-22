import pygame


class View:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    
    def __init__(self, maze_rows, maze_cols, cell_edge_length):
        pygame.init()
        
        self.WIDTH = maze_cols * cell_edge_length
        self.HEIGHT = maze_rows * cell_edge_length
        self.DISPLAY = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.CAPTION = "Maze Generator"
        
        pygame.display.set_caption(self.CAPTION)
    
    def draw_display(self, maze, path):
        # Fill the entire screen with a white color
        self.DISPLAY.fill(View.WHITE)
        
        # Draw maze to the screen
        self.draw_maze(maze)
        
        # Draw path from start to the end
        self.draw_path(path)
        
        # Top line
        pygame.draw.line(self.DISPLAY, View.BLACK, (0, 0), (self.WIDTH, 0))
        
        # Left line
        pygame.draw.line(self.DISPLAY, View.BLACK, (0, 0), (0, self.HEIGHT))
        
        pygame.display.update()
    
    def draw_maze(self, maze):
        for row in maze:
            for cell in row:
                # Draw bottom line
                if cell.walls["bottom"]:
                    start_pos = cell.x, cell.y + cell.edge_length
                    end_pos = cell.x + cell.edge_length, cell.y + cell.edge_length
                    
                    pygame.draw.line(self.DISPLAY, View.BLACK, start_pos, end_pos, width=3)
                
                # Draw right line
                if cell.walls["right"]:
                    start_pos = cell.x + cell.edge_length, cell.y
                    end_pos = cell.x + cell.edge_length, cell.y + cell.edge_length
                    
                    pygame.draw.line(self.DISPLAY, View.BLACK, start_pos, end_pos, width=3)
    
    def draw_path(self, path):
        num_of_cells = len(path)
        
        for cell in range(num_of_cells - 1):
            start_cell = path[cell]
            end_cell = path[cell + 1]
            
            # Start drawing the line in the middle of the start cell
            start_pos = start_cell.x + (start_cell.edge_length / 2), start_cell.y + (start_cell.edge_length / 2)
            
            # End drawing the line in the middle of the end cell
            end_pos = end_cell.x + (end_cell.edge_length / 2), end_cell.y + (end_cell.edge_length / 2)
            
            pygame.draw.line(self.DISPLAY, View.RED, start_pos, end_pos, width=2)
