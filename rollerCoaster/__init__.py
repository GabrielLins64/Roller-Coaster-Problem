import json
from .instances import MontanhaRussa

CONFIG_FILE = "rollerCoaster/configs.json"

with open(CONFIG_FILE) as file:
    configs = json.load(file)

montanhaRussa = MontanhaRussa(
    configs["n"],
    configs["m"],
    configs["C"],
    configs["Te"],
    configs["Tm"],
    configs["Tp"]
)
