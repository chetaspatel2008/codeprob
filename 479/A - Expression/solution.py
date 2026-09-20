a = int(input())
b = int(input())
c = int(input())
sum_ = a+b+c
mulb_sum = a*b +c
sum_mulb = a + b*c
mul_sum = a*(b+c)
mul = a*b*c
sumb_mul = (a + b)*c
x = max(sum_mulb, mul_sum, mul, sumb_mul, sum_, mulb_sum)
print(x)