import random,string

def random_grid():
    grid=[]
    for  i in range (1,10):
        r_c=random.choice(string.ascii_letters)
        r_c=r_c.lower()
        grid.append(r_c)
    return grid

class Game():

    def  __init__(self):
        self.grid=random_grid()


    def  is_valid(self,word):
        word=word.lower()
        for  c  in word:
            if  c not  in self.grid:
                return False
        return True




