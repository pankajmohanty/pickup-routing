import numpy as np
import matplotlib.pyplot as plt
import random
import copy 
from BaseWarehouse import BaseWarehouse
class Warehouse:
    def __init__(self, n_nodes, n_veh) -> None:
        self.env = BaseWarehouse(n_nodes, n_veh)
        self.map_size=(20, 20)
        self.n_nodes = n_nodes
        self.n_veh = n_veh
        self.reset()
    def reset(self):
        self.state, self.nodes = self.env.reset()
        self.curr_veh = 0
        self.info2map()

        return self.rack_map, self.unvis_map, self.vis_map, self.pickers_map, self.depot_map

    def step(self, v, n):
        self.state, self.nodes = self.env.step(v, n)


        if len(self.unvis_nodes)==0:
            done=True
            R = self.calculate_cost()

        # Updata Maps
        self.info2map()


        return self.rack_map, self.unvis_map, self.vis_map, self.pickers_map, self.depot_map, R, done, {}

    def calculate_cost(self):
        pass

    def warshell_cost_path(self, pos_a, pos_b):
        V = len()
        graph = self.get(graph)
    
    def prepare_for_Warshell(self):
        V=self.map_size[0]*self.map_size[1]
        INF = 10**7
        # Create Warshell Map
        N = self.map_size[0]
        M = N*N
        INF = 100*7
        Data = np.ones((M,M))*INF
        for i in range(M):
            print(i)
            Data[i,i]=0
            if(i%N==N-1):  # Right
                if(i != M-1):
                    Data[i, i+N] = 1 
                else:
                    pass

            elif(i+1>N*(N-1) and i!=M-1): # Down
                Data[i, i+1] = 1 

            else:             # Others
                Data[i, i+1] = 1
                Data[i, i+N] = 1 

            Data[:, i] = np.transpose(Data[i, :]) 
        ##########
        
        warshell_map = copy.deepcopy(Data)
        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                if(self.rack_map[i, j]==1):
                    warshell_map[i*N+j, :] = INF
                    warshell_map[:, i*N+j] = INF
                    warshell_map[i*N+j, i*N+j]=0
        return warshell_map
    def info2map(self):
        self.rack_map = np.zeros(self.map_size)
        self.unvis_map = np.zeros(self.map_size)
        self.vis_map = np.zeros(self.map_size)
        self.pickers_map = np.zeros(self.map_size)
        self.depot_map = np.zeros(self.map_size)

        # Rack Map
        for r in self.state["Nodes"].keys():
            x, y, _ = self.state["Nodes"][r]["pos"]
            self.rack_map[x, y] = 1

        # Unvisited and Visited nodes Map
        for node in self.nodes:
            x, y, t = self.state["Nodes"][node]["pos"]
            if(not self.state["Nodes"][node]["visited"]):
                self.unvis_map[x, y] = 1 
                if t=="left": 
                    self.unvis_map[x, y-1] = 1 
                else:
                    self.unvis_map[x, y+1] = 1 
                    
                # Visited nodes Map
            else:
                if t=="left": 
                    self.vis_map[x-1, y-1] = 1 
                    self.vis_map[x, y-1] = 1 
                    self.vis_map[x+1, y-1] = 1 
                else:
                    self.vis_map[x-1, y-1] = 1 
                    self.vis_map[x, y-1] = 1 
                    self.vis_map[x+1, y-1] = 1 

        # Current pickers Locations
        for v in self.state["Vehicles"].keys():
            p = self.state["Vehicles"][v]["pos"]
            if p==-1:
                x, y, t = self.env.depot
            else:
                x, y, t = self.state["Nodes"][p]["pos"]
            print(self.state["Vehicles"][v]["pos"])
            self.pickers_map[x-1, y] = 1 
            self.pickers_map[x, y-1] = 1 
            self.pickers_map[x, y] = 1 
            self.pickers_map[x, y+1] = 1 
            self.pickers_map[x+1, y] = 1 
            if self.curr_veh == v+1:
                self.pickers_map[x-1, y-1] = 1 
                self.pickers_map[x-1, y+1] = 1 
                self.pickers_map[x+1, y+1] = 1 
                self.pickers_map[x+1, y-1] = 1 


    def show(self):
        plt.figure(figsize=(10,10))
        plt.imshow(self.rack_map)
        plt.show()

        plt.figure(figsize=(10,10))
        plt.imshow(self.unvis_map)
        plt.show()

        plt.figure(figsize=(10,10))
        plt.imshow(self.vis_map)
        plt.show()

        plt.figure(figsize=(10,10))
        plt.imshow(self.pickers_map)
        plt.show()


