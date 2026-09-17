class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        freq = dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))

        for i in range(k):
            result.append(list(freq)[i])
        return result