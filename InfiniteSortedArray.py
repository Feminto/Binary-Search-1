# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader == None:
            return -1

        low = 0
        high = 1

        while low <= high:
            mid = (low + high) //2

            if reader.get(mid) == target:
                return mid

            if reader.get(high) <= target:
                low += 1
                high *= 2
            else:
                if reader.get(mid) > target:
                    high = mid -1
                else:
                    low = mid + 1
        
        return -1