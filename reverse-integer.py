# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
#     Input: 123
#     Output: 321

# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        if x > 2147483648 or x < -2147483648:
            return 0
        
        temp = str(x)
        starting_pos = 0
        negative = False
        
        if temp[0] == "-":
            starting_pos = 1
            negative = True
        
        ending_pos = len(temp)
        
        # Find ending 0's
        for i in temp[::-1]:
            if i == "0":
                ending_pos = ending_pos - 1
            else:
                break
        
        if starting_pos == ending_pos:
            return 0
        
        new_str = temp[starting_pos:ending_pos][::-1]
        
        new_numb = int(new_str)
        
        if negative:
            new_numb = new_numb * -1
            
        if new_numb > 2147483648 or new_numb < -2147483648:
            return 0
        
        return new_numb