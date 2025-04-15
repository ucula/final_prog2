import pygame as pg

class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def get_image1(self, cords: tuple, frame, width, height, scale, color):
        image = pg.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, cords, (0, (frame * width), width, height))

        # Make image larger
        image = pg.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image
    
    def get_image2(self, cords: tuple, frame, width, height, scale, color):
        image = pg.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, cords, (24, (frame * width), width, height))

        # Make image larger
        image = pg.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image
    
    def get_image3(self, cords: tuple, frame, width, height, scale, color):
        image = pg.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, cords, (48, (frame * width), width, height))

        # Make image larger
        image = pg.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image
