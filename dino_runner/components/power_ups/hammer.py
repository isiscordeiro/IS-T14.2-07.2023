
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER

class Hammer(PowerUp):
    def __init__(self):
        super().__init__(HAMMER)
        