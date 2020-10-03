N = int(raw_input(''))

count = [0, 2, 3]

for i in range(3, N + 1):
    count.append(count[i - 1] + count[i - 2])

print count[N] * N
