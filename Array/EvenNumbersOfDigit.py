#Find Numbers with Even Number of Digits

class solution:
    def findNumbers(self,nums):
        counter=0
        for eachRound in range(len(nums)):
            n=str(nums[eachRound])
            if len(n)%2==0:
                counter+=1

        return counter


