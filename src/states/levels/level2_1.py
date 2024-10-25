from src.objects.portal import Portal  # Import portal class
from .level import Level

class Level2_1(Level):
    def __init__(self):
        imgArr = [f"plx-red-1.jpg"]
        super().__init__(
            level=2,
            music_file="levelmusic.mp3",
            imgArr=imgArr
        )

    def add_portal(self):
        # Add portal at specific coordinates
        self.portal = Portal(2500, 700, "assets/backgrounds/portal.png", 150, 150)
        self.portals.add(self.portal)
        self.objects.add(self.portals)
