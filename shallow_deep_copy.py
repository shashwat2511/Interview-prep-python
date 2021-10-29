####### shallow copy & deep copy #######
# xs = [10, [1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ys = list(xs)
# xs.append(['new sublist'])

# xs[1][2] = 'X'
# xs[0] = 11
# ys[0] = 12

xs = [0, 1, [2, 3], 4, 5]
ys = list(xs)
# ys = xs

print(id(xs))
print(id(ys))
print("----------------------------")
xs.append(['new sublist'])
xs[3] = 3
xs[2][1] = 4

print(id(xs[2]))
print(id(ys[2]))

print(xs)
print(ys)