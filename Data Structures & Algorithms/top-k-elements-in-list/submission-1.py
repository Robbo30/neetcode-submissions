class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        
        sorted_nums = sorted(freqs.keys(), key=freqs.get, reverse=True)

        return sorted_nums[:k]
