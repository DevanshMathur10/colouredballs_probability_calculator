# Coloured Balls probability calculator
### Assignment

Suppose there is a box containing 4 white balls, 2 yellow balls, and 5 black balls. What is the probability that a random draw of 8 balls will contain at least 3 white balls and 1 yellow ball? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a box. 

First, create a `Box` class in `probability_calculator.py`. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:
```
box1 = Box(red=6,blue=5,green=10)
box2 = Box(yellow=7,black=1 orange=4)
box3 = Box(red=5, orange=4, black=1, blue=10 ,white=3)
```

A box will always be created with at least one ball. The arguments passed into the box object upon creation should be converted to a `colourlist` instance variable. `colourlist` should be a list of strings containing one item for each ball in the box. Each item in the list should be a color name representing a single ball of that color. For example, if your box is `{"red": 2, "blue": 1}`, `contents` should be `["red", "red", "blue"]`.

The `Box` class should have a `draw` method that accepts an argument indicating the number of balls to draw from the box. This method should remove balls at random from `colourlist` and return those balls as a list of strings. The balls should not go back into the box during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

Next, create an `experiment` function in `probability_calculator.py` (not inside the `Box` class). This function should accept the following arguments:
* `box`: A box object containing balls that should be copied inside the function.
* `expected_balls`: An object indicating the exact group of balls to attempt to draw from the box for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the box, set `expected_balls` to `{"blue":2, "red":1}`.
* `balls_drawn`: The number of balls to draw out of the box in each experiment.
* `num_experiments`: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The `experiment` function should return a probability. 

For example, let's say that you want to determine the probability of getting at least 1 black ball, 3 blue balls, 2 red balls, 4 yellow balls and 2 white balls when you draw 20 balls from from a box containing 6 red balls, 5 blue balls, 10 green balls, 7 yellow balls, 1 black ball and 3 white balls. To do this, we perform `N` experiments, count how many times `M` we get at least 2 red balls and 1 green ball, and estimate the probability as `M/N`. Each experiment consists of starting with a box containing the specified balls, drawing a number of balls, and checking if we got the balls we were attempting to draw.

Here is how you would call the `experiment` function based on the example above with 1000 experiments:

```
box=probability_calculator.Box(red=6,blue=5,green=10,yellow=7,black=1,white=3)
probability = probability_calculator.experiment(box=box, 
                  expected_balls={'black':1,'blue':3,'red':2,'yellow':4,'white':2},
                  balls_drawn=20,
                  num_experiments=1000)
```

Since this is based on random draws, the probability will be slightly different each time the code is run.

*Hint: Consider using the modules that are already imported at the top of `probability_calculator.py`.*

### Development

Write your code in `probability_calculator.py`. For development, you can use `main.py` to test your code. Click the "run" button and `main.py` will run.

### Testing 

The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

