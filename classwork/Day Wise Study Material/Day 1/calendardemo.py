#accept number of days in a month from user
#it can be either 30,31,28,29
# accept start day 0 for monday 1 for tuesday 2 for wednesday

#and display the calender of the month

days=int(input("enter number of days in a month"))
if days==30 or days==31 or days==29 or days==28:
    startday=int(input("enter the startday monday-0 tuesday-1 ...."))
    print("Mon\ttue\twed\tThru\tFri\tsat\tsun")
    cnt=startday
    print("   \t"*startday,end="")
    for i in range(1,days+1):
        print(f"{i}\t",end="")
        cnt=cnt+1
        if cnt%7==0:
            print()
            cnt=0
            
    
