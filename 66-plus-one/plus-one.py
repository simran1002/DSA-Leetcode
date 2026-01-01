class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits











        # number = 0
        # for i in digits:
        #     number = number*10+i
        # number+=1
        # result = []
        # while number >0:
        #     num = number%10
        #     result.append(num)
        #     number = number//10
        # return result[::-1]