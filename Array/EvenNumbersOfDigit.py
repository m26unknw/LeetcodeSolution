#Find Numbers with Even Number of Digits
#In this solution I i did not count the digit of numbers by doing the divide remainder method i just convert the number into string
# And then just checking with length whether it is even or not:


class solution:
    def findNumbers(self,nums):
        counter=0
        for eachRound in range(len(nums)):
            n=str(nums[eachRound])
            if len(n)%2==0:
                counter+=1

        return counter

#Second Method

class solution_2:
    def findNumbers(self,nums):
        result=0
        for eachRound in range(len(nums)):
            counter=0
            while eachRound:
                eachRound//10
                counter+=1
            
            if eachRound%2==0:
                result+=1

        return result

