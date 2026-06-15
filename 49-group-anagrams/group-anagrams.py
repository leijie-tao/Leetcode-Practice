class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if len(strs) <= 1:
        #     return [strs]
        
        # record = defaultdict(list)      #Create a map with default value []
        # for s in strs:
        #     key = "".join(sorted(s))    # Take the same string as the key.    Notice: sorted() needs klogk
        #     record[key].append(s)       # Record the value with the same string
        
        # return list(record.values())




        if len(strs) <= 1:
            return [strs]
        
        record = defaultdict(list)     
        for s in strs:
            count = [0] * 26        # Refine the way of key. Loop through each element and record the count list.
            for c in s:
                count[ord(c) - ord("a")] += 1  
            record[tuple(count)].append(s)      # Transfer list into tuple to be used as a key
        
        return list(record.values())