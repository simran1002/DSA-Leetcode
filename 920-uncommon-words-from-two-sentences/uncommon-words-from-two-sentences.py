class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l=list()
        s1=s1.split()
        s2=s2.split()
        for i in s1:
            if s1.count(i)==1:
                if i not in s2:
                    l.append(i)
        for j in s2:
            if s2.count(j)==1:
                if j not in s1:
                    l.append(j)
        return(l)