class Recks:
    def __init__(self, pos) -> None:
        self.pos_coord = pos
        self.visited= False
        self.available = False
        self.veh_id = -1

    def set_avail(self):
        self.available = True

    def set_visit(self, v):
        self.visited = True
        self.veh_id = v