from time import sleep
print("COUNTDOWN TIMER\n")

sec=int(input("Enter Seconds: "))
if sec>0:
    while sec>=0:
        minutes,seconds=divmod(sec,60)
        time="    {:02d}:{:02d}".format(minutes,seconds)
        print(time,end="\r")
        sleep(1)
        sec-=1 
        
else:
    print("Seconds should be greater than zero!")