import gym
from gym import error, spaces, utils
from gym.utils import seeding

class GrandTour_MIT(gym.Env):
    metadata = {'render.modes': ['human']}


    def __init__(self):
        self.state = [[0]*12 for n in range(0,12)]
        close=[[0,4],[0,7],[1,2],[2,11],[3,1],[6,8],[6,11],[8,0],[10,4],[11,8]]
        for i in close:
            row=i[0]
            column=i[1]
            self.state[row][column]=99
        default_state_row=5
        default_state_column=5
        self.state[default_state_row][default_state_column]='i'
        
        self.row=default_state_row
        self.column=default_state_column

        self.reward=0
        self.counter = 0
        self.done = 0
        self.add = [0, 0]

#     def check(self):
#         if self.row<0 or self.column<0 or self.row>11 or self.column>11:
#             return 0
#         elif self.state[self.row][self.column]!=0:
#             return 0
#         else:
#             return 1         

    def step(self, action):
        if self.done == 1:
            print("Game Over")
            return [self.state, self.reward, self.done, self.add]
        elif action=='w':
            if self.row-1<0:
                print("invalid step")
                self.reward-=1
            elif self.state[self.row-1][self.column]!=0:
                print("invalid step")
                self.reward-=1
            else:
                self.reward+=1
                self.state[self.row-1][self.column]=action
                self.row-=1                
        elif action=='s':
            if self.row+1>11:
                print("invalid step")
                self.reward-=1
            elif self.state[self.row+1][self.column]!=0:
                print("invalid step")
                self.reward-=1
            else:
                self.reward+=1
                self.state[self.row+1][self.column]=action
                self.row+=1
        elif action=='a':
            if self.column-1<0:
                print("invalid step")
                self.reward-=1
            elif self.state[self.row][self.column-1]!=0:
                print("invalid step")
                self.reward-=1
            else:
                self.reward+=1
                self.state[self.row][self.column-1]=action
                self.column-=1                
        elif action=='d':
            if self.column+1>11:
                print("invalid step")
                self.reward-=1
            elif self.state[self.row][self.column+1]!=0:
                print("invalid step")
                self.reward-=1
            else:
                self.reward+=1
                self.state[self.row][self.column+1]=action
                self.column+=1                               
            self.render()

#         win = self.check()
#         if(win==0):
#             self.done = 1;
#             print("Game over \n")
#             self.reward = -1000
#         else:
#             self.reward = -100
        return [self.state, self.reward, self.done, {}]

#     def step(self, action):
#         if self.done == 1:
#             print("Game Over")
#             return [self.state, self.reward, self.done, self.add]
#         elif self.state[int(target/3)][target%3] != "-":
# 			print("Invalid Step")
# 			return [self.state, self.reward, self.done, self.add]
# 		else:
# 			if(self.counter%2 == 0):
# 				self.state[int(target/3)][target%3] = "o"
# 			else:
# 				self.state[int(target/3)][target%3] = "x"
# 			self.counter += 1
# 			if(self.counter == 9):
# 				self.done = 1;
# 			self.render()

# 		win = self.check()
# 		if(win):
# 			self.done = 1;
# 			print("Player ", win, " wins.", sep = "", end = "\n")
# 			self.add[win-1] = 1;
# 			if win == 1:
# 				self.reward = 100
# 			else:
# 				self.reward = -100

# 		return [self.state, self.reward, self.done, self.add]    
    
    def reset(self):
        self.state = [[0]*12 for n in range(0,12)]
        close=[[0,4],[0,7],[1,2],[2,11],[3,1],[6,8],[6,11],[8,0],[10,4],[11,8]]
        for i in close:
            row=i[0]
            column=i[1]
            self.state[row][column]=99
        default_state_row=5
        default_state_column=5
        self.state[default_state_row][default_state_column]='i'

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
