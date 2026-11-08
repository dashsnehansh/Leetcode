class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647   # 2^31 - 1
        MIN_INT = -2147483648  # -2^31
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        is_negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            current_divisor = divisor
            multiple = 1
            while dividend >= (current_divisor << 1):
                current_divisor <<= 1
                multiple <<= 1
            dividend -= current_divisor
            quotient += multiple
        return -quotient if is_negative else quotient


