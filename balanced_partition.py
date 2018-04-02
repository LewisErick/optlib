from collections import namedtuple
import math

Rule = namedtuple('Rule', ['heuristic',
                           'feature_vector'])

class BalancedPartition:

    def __init__(self, container1=[], container2=[]):
        self.container1 = container1
        self.container2 = container2
        self.featureIDs = self.default_features()
        self.rules = self.default_rules()
        self.distance_callback = self.default_distance

    def default_features(self):
        return [1]

    def default_rules(self):
        rule = Rule(1, [1])
        return [rule]

    '''
        Heuristics:
            1. Max
            2. Min
    '''
    def apply_heuristic(self, heuristic=1):
        if heuristic == 1:
            max_element = max(self.container1)
            self.container1.remove(max(self.container1))
            self.container2.append(max_element)
        elif heuristic == 2:
            min_element = min(self.container1)
            self.container1.remove(min(self.container1))
            self.container2.append(min_element)

    '''
     Features:
        1. Balance between the two containers.
    '''
    def feature_vector(self):
        f_vector = []
        for feature in self.featureIDs:
            if feature == 1:
                f_vector.append(sum(self.container2) / (sum(self.container1) + sum(self.container2)))
        return f_vector

    def default_distance(self, vector1=[], vector2=[]):
        dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
        dist = math.sqrt(sum(dist))
        return dist

    def select_heuristic(self, feature_vector=[]):
        heuristic = 1;
        min_dist = 9999999;
        for rule in self.rules:
            if self.distance_callback(feature_vector, rule.feature_vector) < min_dist:
                heuristic = rule.heuristic;
                min_dist = self.distance_callback(feature_vector, rule.feature_vector)
        return heuristic

    def solve(self):
        f_vector = self.feature_vector()
        while f_vector[0] < 0.5 and len(self.container1) > 0:
            heuristic = self.select_heuristic(f_vector)

            self.apply_heuristic(heuristic)
            f_vector = self.feature_vector()
