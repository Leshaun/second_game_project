class CharacterTemplate:
    def __init__(self, name, hitpoints, move1, move2, move3, weakness):
        self.name = name
        self.hitpoints = hitpoints
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.weakness = weakness


class CharacterMove:
    def __init__(self, name, min_dmg, max_dmg, move_type, recoil):
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.type = move_type
        self.recoil = recoil


