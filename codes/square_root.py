import math
n = 2
epsilon = 1e-9
p_knot = 0
p_new = p_knot
p_old = p_knot
error = math.fabs(n-p_new*p_new)
counter = 0
max_iter = 10000
while(error > epsilon):
    print(f'iteration {counter:10d}'f', error: {error:.11f}.')
    p_new = (n*p_old+n)/(p_old+n)
    error = error = math.fabs(n-p_new*p_new)
    p_old = p_new
    counter = counter+1
    if counter > max_iter:
        break

print("\n")
print("congrats!!! you calculated the square root of: ", n, " which is approximately:", p_new)
