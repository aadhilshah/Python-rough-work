#num=(input("Enter the numbr: "))
#revnum=num[::-1]
#print(revnum)

num=int(input("Enter the number:"))
rev_num=0
while num>0:
    digit=num%10
    rev_num=rev_num*10+digit
    num//=10

print(rev_num)
