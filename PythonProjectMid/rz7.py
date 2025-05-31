from statistics import mean, median, mode
n = list(map(int,input("enter number: ").split()))

print("median", median(n))
print("mean", mean(n))
try:
    print("mode", mode(n))
except:
    print("no mode")
