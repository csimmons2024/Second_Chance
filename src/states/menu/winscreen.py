import pygame as pg

from ..state import State


class WinScreen(State):
    """State for the win screen."""

    def __init__(self):
        super().__init__("background.png")

    def handle_events(self, events: list[pg.event.Event]):
        #import your level here I guess
        #if more levels wanted to be made there would have to be a global counter that is accessed here
        #there would have to be imports for all levels....loops? no it would prob be a switch under the return key stuff
        #will test soon....
        from .title_screen import TitleScreen
        from ..levels.level2_1 import Level2_1
        for event in events:
            if event.type != pg.KEYDOWN:
                return
            if event.key == pg.K_RETURN:


                #add the new level in here Andrew this will make the game go to the next level
                #instead of back to the title screen pretty sure...
                self.manager.set_state(Level2_1)

    def draw(self):
        super().draw()
        self.screen.blit(
            pg.font.Font(None, 36).render("You win!", True, "black"),
            (self.screen.get_width() / 2, self.screen.get_height() - 100)
        )
