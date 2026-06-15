class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        record = defaultdict(list)      #Create a map with default value []
        for s in strs:
            key = "".join(sorted(s))    # Take the same string as the key
            record[key].append(s)       # Record the value with the same string
        
        return list(record.values())