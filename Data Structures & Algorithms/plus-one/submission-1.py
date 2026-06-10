class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        length = len(digits)
        carry = 1
        for i in range(length):
            if digits[length - i - 1] + carry > 9:
                digits[length - i - 1] = (digits[length - i - 1] + carry) % 10
            else:
                digits[length - i - 1] = digits[length - i - 1] + carry
                carry = 0
                break
        if carry != 0:
            digits = [carry] + digits
        return digits