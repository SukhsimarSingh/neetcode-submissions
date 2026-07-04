class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        store = {}
        
        for val in nums:

            if str(val) not in store.keys():
                store[str(val)] = 1
            else:
                return True

        return False