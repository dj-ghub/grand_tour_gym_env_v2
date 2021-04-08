import gym
from gym import error, spaces, utils
from gym import Env
from gym.spaces import Discrete, Box
from gym.utils import seeding

class GrandTour_MIT(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.state = [[0]*12 for n in range(0,12)]
        close=[[0,4],[0,7],[1,2],[2,11],[3,1],[6,8],[6,11],[8,0],[10,4],[11,8]]
        for i in close:
            row=i[0]
            column=i[1]
            self.state[row][column]=9
        default_state_row=5
        default_state_column=5
        self.state[default_state_row][default_state_column]=5
        
        self.row=default_state_row
        self.column=default_state_column
        
        self.action_space = [1,2,3,4]

        self.reward=0
        self.counter = 0
        self.done = 0
        self.add = [0, 0]
        
    def check_done(self):
        if self.state[self.row-1][self.column]!=0 & self.state[self.row+1][self.column]!=0 & self.state[self.row][self.column-1]!=0 & self.state[self.row][self.column+1]!=0:
            return 1
        else:
            return 0

    def step(self, action):
        # Action = 1 - Up, 2 - Right, 3 - Down, 4 - Left
        if self.done == 1:
            print("Game Over")
            return [self.state, self.reward, self.done, self.add]
        elif action==1:
            if self.row-1<0:
                print("invalid step")
                self.reward-=1
            elif self.state[self.row-1][self.column]!=0:
                print("invalid step")
                self.reward-=1
            else:
                self.reward+=1
                self.state[self.row][self.column]=action
                self.row-=1                
        elif action==3:
            if self.row+1>11:
                print("invalid step")
                self.reward-=1
            elif self.state[self.row+1][self.column]!=0:
                print("invalid step")
                self.reward-=1
            else:
                self.reward+=1
                self.state[self.row][self.column]=action
                self.row+=1
        elif action==4:
            if self.column-1<0:
                print("invalid step")
                self.reward-=1
            elif self.state[self.row][self.column-1]!=0:
                print("invalid step")
                self.reward-=1
            else:
                self.reward+=1
                self.state[self.row][self.column]=action
                self.column-=1                
        elif action==2:
            if self.column+1>11:
                print("invalid step")
                self.reward-=1
            elif self.state[self.row][self.column+1]!=0:
                print("invalid step")
                self.reward-=1
            else:
                self.reward+=1
                self.state[self.row][self.column]=action
                self.column+=1                               
        self.render()
        self.done=check_done(self)
        return [self.state, self.reward, self.done, {}]
    
    def reset(self):
        self.state = [[0]*12 for n in range(0,12)]
        close=[[0,4],[0,7],[1,2],[2,11],[3,1],[6,8],[6,11],[8,0],[10,4],[11,8]]
        for i in close:
            row=i[0]
            column=i[1]
            self.state[row][column]=9
        default_state_row=5
        default_state_column=5
        self.state[default_state_row][default_state_column]=5

        self.counter = 0
        self.done = 0
        self.add = [0, 0]
        self.reward = 0
        return self.state

    def render(self):
        for i in range(12):
            for j in range(12):
                print(self.state[i][j],end=" ")
            print("")
