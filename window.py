
class Window:

    def __init__(self, surface, player, inky, blinky, pinky, clyde, map):
        self.surface = surface
        self.player = player
        self.inky = inky
        self.blinky = blinky
        self.pinky = pinky
        self.clyde = clyde
        self.map = map

    def switch_color(self, mode, window):
        inky = window.inky
        blinky = window.blinky
        pinky = window.pinky
        clyde = window.clyde
        if mode:
            inky.color = (0, 0, 255)
            blinky.color = (0, 0, 255)
            pinky.color = (0, 0, 255)
            clyde.color = (0, 0, 255)
        else:
            window.player.eats = False
            inky.color = (0, 255, 255)
            blinky.color = (255, 0, 0)
            pinky.color = (255, 102, 255)
            clyde.color = (255, 128, 0)