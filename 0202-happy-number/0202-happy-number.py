class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        
        # Keep looping until n becomes 1 or we detect a cycle
        while n != 1 and n not in seen:
            seen.add(n)
            
            # 1. Convert to string and list to isolate digits
            digits = list(str(n))
            
            # 2. Reset our sum tracker to 0 for this round
            current_sum = 0
            
            # 3. Convert each character back to int, square it, and sum it
            for i in digits:
                current_sum += int(i) ** 2
                
            # 4. Update n with the new sum for the next iteration
            n = current_sum
            
        # If we exited the loop because n became 1, it's a happy number
        return n == 1

               