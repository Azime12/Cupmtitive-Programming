class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        qu = deque()
        lst=[]
        changed.sort()
        for i in changed :
            if len(qu)> 0 and i == qu[0] :
                qu.popleft()
                continue
            else :
                qu.append(i*2)
                lst.append(i)
        
        if qu==deque([])  :
            return lst
        return []
                
