import time
i = 10
for i in range(5, -1, -1):
    print(i)
    time.sleep(1) 
    if(i==0):
        print("BUUUM")