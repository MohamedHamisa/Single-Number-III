class Solution:
    def singleNumber(self, nums):
        s = reduce(xor, nums)
        nz = s & (s-1) ^ s
        num1 = reduce(xor, filter(lambda n: n & nz, nums))
        return(num1, s ^ num1)




        



#Complexity: time complexity is O(n), where we do 2 passes over data. Additional space complexity is O(1), we use just several additional variables.
