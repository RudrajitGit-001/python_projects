import time
my_time=int(input("Enter the time in seconds:"))

for x in range(my_time,0,-1):
    second= x%60
    minute=int(x/60)%60
    hour=int(x/3600)

    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)

print("TIMES UP!")

#x=my_time
#while x>0:
#    second= x%60
#     minute= int(x/60)%60
#     print(f"00:{minute}:{second}")
#     time.sleep(1)
#     x-=1
#print("TIMES UP!")
