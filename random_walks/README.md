# Random Walks: Overview

A random walk is a path that has no clear direction but is determined by a series of random decisions, each of which is left entirely to chance. Random walks have practical applications in nature, physics, biology chemistry, and economics. For example, a pollen grain floating on a drop of water moves across the surface of the water because it’s constantly pushed around by water molecules. Molecular motion in a water drop is random, so the path a pollen grain traces on the surface is a random walk. The following code will try to model many real world situations.

## Example of Obtained Plots:

![alt text](https://github.com/paabes/Data-Science/blob/main/random_walks/render_extracts/random_n%3D5000.png "n = 5k")
![alt text](https://github.com/paabes/Data-Science/blob/main/random_walks/render_extracts/n%3D50k.png "n = 50k")
![alt text](https://github.com/paabes/Data-Science/blob/main/random_walks/render_extracts/random_walk.png "Random Walk")
![alt text](https://github.com/paabes/Data-Science/blob/main/random_walks/render_extracts/pollen_grain_randomPath.png "Molecular Motion")

# plotly_dice: Overview

 When one rolls single regular, six-sided die, it has an equal chance of rolling any of the numbers from 1 through 6. However, when you use two dice, you’re more likely to roll certain numbers rather than others.

* "plotly_dice.py" tries to determine which numbers are most likely to occur by generating a data set that represents rolling dice.

* Then it plots the results of a large number of rolls to determine which results are more likely than others.

* The code also compares dice of other sizes such as D6-D10

* Demonstrates how the result distribution changes when one rolls more than two dice

* Switches to using multiplication as a metric for obtaining result, instead of addition of individual outcomes.

### The results are plotted using oth pygal in the scalable vector graphics form and plotly, graphs can be seen in the plotly_output directory.









