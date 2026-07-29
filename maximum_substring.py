def maximumsubarray(arr):
    max_sum=arr[0]
    current_sum=arr[0]
    list=[]
    for i in range(1,len(arr)):
        current_sum=max(arr[i],current_sum+arr[i])
        max_sum=max(max_sum,current_sum)
        list.append(arr[i])

    return max_sum,list
print(maximumsubarray([-2,1,-3,4,-1,2,1,-5,4]))
print(list)