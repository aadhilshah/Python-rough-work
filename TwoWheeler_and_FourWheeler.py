v=input("Total no of vechicles: ")
w=input("Total no of wheeels")
if w<2 or w%2 !=0 or v>=w:
    print("invalid input")
else:
    fw=(w-2*v)//2
    tw=v-fw
    print(f'tow wheel={tw} and four wheel={fw}')
