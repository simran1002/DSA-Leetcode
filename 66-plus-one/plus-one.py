class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in digits:
            number = number*10+i
        number+=1
        result = []
        while number >0:
            num = number%10
            result.append(num)
            number = number//10
        return result[::-1]