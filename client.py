import pygame
pygame.font.init()

screen_width =  750
screen_height = 750
window = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("test_client")

class Button:
    def __init__(self, x, y,text, color):
        self.x = x
        self.y = y
        self.text = text
        self.color = "#98FB98"
        self.width = 100
        self.height = 75

    def draw_button(self,window):
        pygame.draw.rect(window, self.color,(self.x,self.y,self.width,self.height))
        font = pygame.font.SysFont("Comic Sans Ms", 30)
        text = font.render(self.text, 1, (0,0,0))
        window.blit(text,(self + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))
    
    def click_on_button(self, position):
        x1 = position[0]
        y1 = position[1]

        if self.x <= x1 <= self.x +self.width and self.y <= y1 <= self.y1 + self.height:
            return True
        return False
    
