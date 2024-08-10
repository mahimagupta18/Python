#Numbers that are divisible only by themselves and 1 are called the prime number
#It is always greater than 1.Example , 2, 3, 5, 7, 11, 19.

num = 3
count = 0
if num > 1:
    for i in range(1,num+1):
        if(num%i)==0:
            count=count + 1
        if count ==2:
            print("Number is Prime")
        else:
            print("Number is not Prime")