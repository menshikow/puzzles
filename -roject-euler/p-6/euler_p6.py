# brute force solution

sum_list = [n for n in range(101)]
sum = sum(sum_list)
sum = sum**2

dum = 0
for i in range(101):
    dum += i**2

sol = sum - dum

print(sol)
