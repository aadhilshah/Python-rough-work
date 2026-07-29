#num=[2,7,11,15]
#target=9
#for i in range(len(num)):
  #  for j in range(i+1,len(num)):
   #     if num[i]+num[j]==target:
    #        print([i,j])
    

def twoSum(nums,target):
    seen={}
    for i, num in enumerate(nums):
        complement=target-num
        if complement in seen:
            return[seen[complement],i]
        seen[num]=i
    return[]
num=[2,7,11,15]
target=9
number=twoSum(num,target)
print(number)