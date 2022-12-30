class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for  i in range(0,n):
            if I%5==0:
                answer.append("Buzz")
            elif i%3==0:
                answer.append("Fizz")
            elif i%3==0 and i%5==0:
                answer.append("FizzBuzz")
            else :
                 answer.append(str(i+1))
        return answer
