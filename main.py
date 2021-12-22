import probability_calculator
from unittest import main


box=probability_calculator.Box(red=6,blue=5,green=10,yellow=7,black=1,white=3)
probability = probability_calculator.experiment(box=box, 
                  expected_balls={'black':1,'blue':3,'red':2,'yellow':4,'white':2},
                  balls_drawn=20,
                  num_experiments=1000)

print("Probability",probability)

main(module='test_module', exit=False)