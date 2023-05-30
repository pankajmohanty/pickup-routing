import numpy as np
import matplotlib.pyplot as plt
import random
import copy 
from Recks import Recks
from Vehicle import Vehicle
from utils import FloydWarshel
class BaseWarehouse:
    def __init__(self, n_nodes, n_veh):

        self.map_size=(20, 20)
        self.n_nodes = n_nodes
        self.n_veh = n_veh
        self.floyd = FloydWarshel()
        self.reset()

    def _init_base_info(self):
        self.depot =[1, int(self.map_size[1]/2), "left"]
        # 1. Racks
        self.racks = dict()
        stepx = (self.map_size[0]-6)/2
        id = 0
        for i in range(6, self.map_size[0]-2, int((self.map_size[0]-6)/2)):
            for j in range(3, self.map_size[1]-2, 4):
                for k in range(i, int(i+stepx)-2):
                    self.racks[id]=Recks((k, j, 'left'))
                    self.racks[id+1]=Recks((k, j+1, 'right'))
                    id+=2
        # 2. Nodes
        print(self.racks.keys())
        ln = [i for i in range(len(self.racks.keys()))]
        random.shuffle(ln)
        self.nodes = ln[:self.n_nodes]
        for n in self.nodes:
            self.racks[n].set_avail()

        # 3. Vehicles Paths 
        self.veh={}
        for v in range(self.n_veh):
            self.veh[v] = Vehicle(-1) 

    def get_state_info(self):
        state=dict()
        state["Vehicles"]=dict()
        for i in range(self.n_veh):
            state["Vehicles"][i] = {'pos': self.veh[i].curr_pos, 'path': self.veh[i].path}
        state["Nodes"]=dict()
        for i in range(len(self.racks.keys())):
            state["Nodes"][i] = {'pos': self.racks[i].pos_coord, 
                                'available': self.racks[i].available,
                                'visited': self.racks[i].visited,
                                'vehicle': self.racks[i].veh_id}
        return state

    def reset(self):
        self.curr_veh = 1
        self._init_base_info()
        return self.get_state_info(), self.nodes

    def step(self, v, n):
        # Update Vehicle
        if(self.racks[n].available):
            if(self.racks[n].visited):
                # Update Vehicle
                self.veh[v].add_node(n)
                # Update Nodes List
                self.nodes[n].set_visit(v)
            else:
                print("Node already Visited")
        else:
            print("Node not available")
        
    
        return self.get_state_info(), self.nodes


