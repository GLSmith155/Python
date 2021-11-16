# Print out the destination city in each array, where paths[CityA, CityB] has A as an outgoing city and B as a destination city.
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Creates an empty dictionary for city a and city b.
        outgoing_count = {}
        # Increases count when it has an outgoing city. Time Complexity is at O(N) to iterate over each path for path in paths[].
        for path in paths:
            city_a, city_b = path
            outgoing_count[city_a] = outgoing_count.get(city_a, 0) + 1
            outgoing_count[city_b] = outgoing_count.get(city_b, 0)
       # The second iteration over the dictionary does not increase the runtime complexity, as 2N is reduced to O(N).
        for city in outgoing_count:
            if outgoing_count[city] == 0:
                return city
