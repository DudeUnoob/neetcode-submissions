import math
from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x, y):

            originX = 0
            originY = 0

            return math.sqrt(((0 - x) ** 2) + ((0 - y) ** 2))


        dictionary = {}
        
        
        # maybe make the key the euclidean distance -> points themselves

        for i in range(len(points)):

            x, y = points[i][0], points[i][1]

            dictionary[tuple(points[i])] = distance(x, y)


        sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=False))
        
        
        res = []

        for i in list(sorted_dict.keys())[:k]:
            print(list(i))

            res.append(list(i))

        return res

            
        