from src.objects.portal import Portal  # Import portal class
from .level import Level


class Level1_1(Level):
    def __init__(self):
        imgArr = [f"{i}-riv.png" for i in range(1, 6)]
        super().__init__(
            level=1,
            music_file="Messmer, The Impaler - Elden Ring Shadow Of The Erdtree OST Official Soundtrack Original Score [ ezmp3.cc ].mp3",
            imgArr=imgArr
        )

    def add_portal(self):
        # Add portal at specific coordinates
        self.portal = Portal(3500, 400, "assets/backgrounds/portal.png", 150, 150)
        self.portals.add(self.portal)
        self.objects.add(self.portals)
