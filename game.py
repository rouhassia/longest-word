import random,string

def random_grid():
    grid=[]
    for  i in range (1,10):
        r_c=random.choice(string.ascii_letters)
        grid.append(r_c)
    return grid

class Game():

    def  __init__(self):
        self.grid=random_grid()


    def  is_valid(self,word):
        grid=self.grid
        for  c  in word:
            if  c not  in grid:
                return False
            grid.remove(c)
        return True




