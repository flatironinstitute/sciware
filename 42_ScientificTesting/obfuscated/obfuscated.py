import math

# This is an artificially hard example, not least because it lacks
# the context of a real task or any code that calls it.

### TODO: How would you approach testing this code?
#
#  - Would you test it as-is?
#  - Do you understand what it's supposed to be doing?
#  - How would you discover the expected properties and invariants
#    of the system?

class Complicated():
    def __init__(self, points, weights):
        # "points" defines the x & y values of a point grid.
        # "weights" are the weights for those points, for a weighted integration scheme
        self.points = points
        self.sqrt_weights = [math.sqrt(x) for x in weights]
        self.attenuation_rate = 0.5


    def set_left_comparator(self, points, point_values):
        point_distances = []
        for (i, point) in enumerate(points):
            dist = math.hypot(self.points[i][0] - point[0], self.points[i][1] - point[1])
            point_distances.append(dist)
        
        effective_point_values = []
        for (i, d) in point_distances:
            weighted_value = point_values[i] - self.attenuation_rate * d
            effective_point_values.append(weighted_value * self.sqrt_weights[i])
        
        self.left_val = effective_point_values


    def compare(self, right_point_values):
        # right points must all be on-grid
        weighted_right_points = [x[0] * x[1] for x in zip(right_point_values, self.sqrt_weights)]
        prods = [x[0] * x[1] for x in zip(weighted_right_points, self.left_val)]
        return sum(prods)
