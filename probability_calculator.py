import random
import copy

class Box:

    def __init__(self,**colours):
        self.colourlist=[]
        for key,value in colours.items():
            for i in range(value):
                self.colourlist.append(key)

    def __repr__(self):
        return f"{self.colourlist}"
        
    #function to get entered number of balls from colourlist
    def draw(self,balls):
        drawlist=[]
        if balls>=len(self.colourlist):
            return self.colourlist
        for i in range(balls):
            name=self.colourlist.pop(random.randrange(len(self.colourlist)))
            drawlist.append(name)
        return drawlist

#function to get probability
def experiment(box,expected_balls,balls_drawn,num_experiments):
    final_count=0
    for num in range(num_experiments):
        copybox=copy.deepcopy(box)
        temp_list=copybox.draw(balls_drawn)
        success=True
        for key,value in expected_balls.items():  
            if temp_list.count(key)<value:
                success=False
                break
        if success:
            final_count+=1
    return final_count/num_experiments
    



