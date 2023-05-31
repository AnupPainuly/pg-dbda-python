#Fibonacci fibo_series using list
# Formula: Fn = Fn-1 + Fn-2, where n > 1
n=int(input("enter the number of terms: "))
if n<1:
    print("enter value more than 1: ")
#init list with first two elements 0,1
else:
    fibo_series=[0,1]
    while (len(fibo_series)<n):
        next_in_series=fibo_series[-1]+fibo_series[-2]
        fibo_series.append(next_in_series)
    print("Fibonacci series: ",fibo_series)
