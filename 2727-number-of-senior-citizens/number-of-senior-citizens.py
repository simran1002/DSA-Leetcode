class Solution(object):
    def countSeniors(self, details):
        count=0
        for x in details:
            age= int(x[11:13])
            if age > 60:
                count=count+1
        return count

        