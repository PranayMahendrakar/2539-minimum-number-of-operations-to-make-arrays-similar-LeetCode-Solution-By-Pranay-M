class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        # Key insight: we can only change parity by +/- 2
        # So odd numbers stay odd and even numbers stay even
        # We need to match odd nums with odd targets, even with even
        
        # Separate by parity and sort
        nums_odd = sorted([x for x in nums if x % 2 == 1])
        nums_even = sorted([x for x in nums if x % 2 == 0])
        target_odd = sorted([x for x in target if x % 2 == 1])
        target_even = sorted([x for x in target if x % 2 == 0])
        
        # Calculate operations needed
        # Each +2 must be matched with a -2, so we only count positive differences
        operations = 0
        
        for n, t in zip(nums_odd, target_odd):
            diff = abs(n - t) // 2
            operations += diff
        
        for n, t in zip(nums_even, target_even):
            diff = abs(n - t) // 2
            operations += diff
        
        # Each operation affects two elements (one +2, one -2)
        # So total operations = sum of positive differences / 2
        return operations // 2