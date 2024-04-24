class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        print(properties.sort(key = lambda x:(-x[0],x[1])))
        max_defense = 0
        weak_count = 0

        for a,d in properties:
            if d < max_defense:
                weak_count += 1
            else:
                max_defense = d
        return weak_count