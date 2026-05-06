class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = defaultdict(list)

        for s in strs:
            # Sort the characters of the string to create a key
            key = ''.join(sorted(s))
            # Add the original string to the list associated with this key
            grouping[key].append(s)

        # Convert the values of the defaultdict to a list
        return list(grouping.values())
