n=int(input())
count = 0
while n > 0:
    count += n & 1
    n>>1
    if count==1:
        print("power of 2")
    else:
        print("not")
        
        
