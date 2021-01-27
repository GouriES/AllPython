i = int(input("Enter the size you want:"))
lst=[]
for j in range(i):
    element = input()
    lst.append(element)
print(lst)
while True:
    choice=int(input("Choose any one Data Structure enter number (1. List , 2. Dict, 3. Set) or enter 0 to exit :-"))

    if choice == 1:
        print(lst)

    elif choice == 2:
        nums=[]
        for num in range(i):
            nums.append(num)
        Dict=zip(nums,lst)    
        print(dict(Dict))

    elif choice == 3:
        Sets=set(lst)
        print(Sets)

    elif choice == 0:
        print("Thanks For Using.................")
        break
