from random import choice
import matplotlib.pyplot as plt

# A random walk is a path that has no clear direction but is determined by a series of random decisions, each of which
# is left entirely to chance. Random walks have practical applications in nature, physics, biology
# chemistry, and economics. For example, a pollen grain floating on a drop of water moves across the surface of
# the water because it’s constantly pushed around by water molecules. Molecular motion in a water drop is random, so
# the path a pollen grain traces on the surface is a random walk. The following code weill try to
# model many real world situations.

class RandomWalk:
    """ Class For Generating Random Walks"""

    def __init__(self, num_points=5000):
        """ Initiate attributes for a walk"""
        self.num_points = num_points

        # All walks start at X=0 and Y=0 i.e (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine the direction and distance for a step."""

        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        """calculate all the points of walk"""

        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # ignore steps that lead nowhere
            if x_step == 0 and y_step == 0:
                continue

            # new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


if __name__ == '__main__':

    # plot the locations on plane
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('seaborn-dark')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens,
               edgecolors='none', s=15)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.title('A Random Walk With 5000 Points (with cmap)')
    plt.show()

    # In addition to coloring points to show their position along the walk, it would be useful to see
    # where each walk begins and ends.

    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('seaborn-dark')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)

    # Emphasize the first and last points.
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens,
               edgecolors='none', s=15)
    ax.scatter(0, 0, c='blue', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.title('Random Walk with Start-Finish Points')
    plt.show()

    # trying with more points
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.style.use('seaborn-dark')
    fig, ax = plt.subplots(dpi=227)
    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens,
               edgecolors='none', s=1)
    ax.scatter(0, 0, c='blue', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.title('Random Walk with n=50,000')
    plt.show()


    # Simulating Molecular Motion: the path of a pollen grain on the surface of a drop of water

    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('seaborn-dark')
    fig, ax = plt.subplots(dpi=227)
    point_numbers = range(rw.num_points)

    # The scatter plots appear behind the lines. To place them on top of the lines, we can use the zorder argument.
    # Plot elements with higher zorder values are placed on top of elements with lower zorder values.

    plt.plot(rw.x_values, rw.y_values, linewidth=1, color='deepskyblue', zorder=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100, zorder=2)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.title('Path of a pollen grain on the surface of a drop of water')
    plt.show()











































































