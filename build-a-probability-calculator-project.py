import random

class Hat:
    def __init__(self, **kwargs):
        # Populate the contents list with the number of balls specified for each color
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # If num_balls exceeds the number of available balls, return all balls and empty the contents
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents = []  # All balls have been drawn
            return drawn_balls
        
        # Randomly select balls without replacement
        drawn_balls = random.sample(self.contents, num_balls)
        
        # Remove drawn balls from contents
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        # Create a copy of the hat contents to ensure experiments don't interfere with each other
        hat_copy = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count occurrences of each ball color in the drawn balls
        drawn_count = {color: drawn_balls.count(color) for color in expected_balls}

        # Check if all expected balls' requirements are satisfied
        if all(drawn_count.get(color, 0) >= count for color, count in expected_balls.items()):
            successful_experiments += 1

    # Return the probability as the ratio of successful experiments
    return successful_experiments / num_experiments

# Example Usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(probability)  # Output: Approx. 0.356 (varies slightly due to randomness)
