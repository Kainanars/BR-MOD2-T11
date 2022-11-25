from dino_runner.utils.constants import POKEBALL, CHARMANDER_TYPE, POKEBALL2, CHARIZARD_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Pokemon1(PowerUp):
    def __init__(self):
        self.image = POKEBALL
        self.type = CHARMANDER_TYPE
        super().__init__(self.image, self.type)


class Pokemon2(PowerUp):
    def __init__(self):
        self.image = POKEBALL2
        self.type = CHARIZARD_TYPE
        super().__init__(self.image, self.type)
    
    