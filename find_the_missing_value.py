n=int(input("Enter the total no : "))
num=[1,2,4]
expectedsum=n*(n+1)/2
actsum=sum(num)
missing=expectedsum-actsum
print(missing)