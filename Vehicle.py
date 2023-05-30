class Vehicle:
    def __init__(self, pos) -> None:
        self.curr_pos = pos
        self.init_pos = pos
        self.path = [pos]

    def add_node(self,node_id):
        self.curr_pos = node_id
        self.path.append(node_id)

    def return_to_init(self):
        self.path.append(self.init_pos)