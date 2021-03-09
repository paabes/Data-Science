from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline
import matplotlib.pyplot as plt
import seaborn as sns
import pygal

# When one rolls single regular, six-sided die, it has an equal chance of rolling any of the numbers
# from 1 through 6. However, when you use two dice, you’re more likely to roll certain numbers
# rather than others. This code tries to determine which numbers are most likely to occur by
# generating a data set that represents rolling dice. Then it plots the results of a large number
# of rolls to determine which results are more likely than others.

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)



if __name__ == '__main__':

    die = Die()
    results = []

    for roll_num in range(1000):
        results.append(die.roll())

    # Analysing results
    frequencies = []
    for val in range(1, die.num_sides + 1):
        frequency = results.count(val)
        frequencies.append(frequency)

    # Visualising frequencies
    x_values = list(range(1, die.num_sides + 1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result'}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config,
                       yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='plotly_output/d6.html')


    # Rolling two dice results in larger numbers and a different distribution of results:

    die_1 = Die()
    die_2 = Die()
    results = []

    for roll_num in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # Analysing results
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for val in range(2, max_result+1):
        frequency = results.count(val)
        frequencies.append(frequency)

    # Visualising frequencies
    x_values = list(range(2, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
                       xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='plotly_output/d6_d6.html')

    # As you can see, you’re least likely to roll a 2 or a 12 and most likely to roll a 7.
    # This happens because there are six ways to roll a 7, namely: 1 and 6, 2 and 5, 3 and 4, 4 and 3,
    # 5 and 2, or 6 and 1.


    ####################################################
    # Rolling Dice of Different Sizes
    ####################################################

    die_1 = Die() # Regular D-6
    die_2 = Die(10)
    results = []

    for roll_num in range(50000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for val in range(2, max_result + 1):
        frequency = results.count(val)
        frequencies.append(frequency)

    # Visualising frequencies
    x_values = list(range(2, max_result + 1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Results of rolling D6 and D10 dice 50,000 times',
                       xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='plotly_output/d6_d10.html')


    ####################################################
    # Rolling Three Dice + Pygal
    ####################################################

    # Create three D6 dice.
    die_1 = Die()
    die_2 = Die()
    die_3 = Die()

    results = []
    for roll_num in range(1000000):
        result = die_1.roll() + die_2.roll() + die_3.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
    for value in range(3, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # Visualize the results.
    hist = pygal.Bar()

    hist.title = "Results of rolling three D6 dice 1,000,000 times."
    hist.x_labels = [str(x) for x in range(3, max_result + 1)]
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add('D6 + D6 + D6', frequencies)
    hist.render_to_file('plotly_output/three_dice_visual.svg')


    ####################################################
    # Multiplication instead of addition
    ####################################################

    die_1 = Die()
    die_2 = Die()

    results = []
    for roll_num in range(1000000):
        result = die_1.roll() * die_2.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides * die_2.num_sides
    for value in range(1, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    hist = pygal.Bar()

    hist.title = "Results of multiplying two D6 dice. (1,000,000 rolls)"
    hist.x_labels = [str(x) for x in range(1, max_result + 1)]
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add('D6 * D6', frequencies)
    hist.render_to_file('plotly_output/dice_multiplication.svg')































































