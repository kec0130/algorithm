data = [int(input()) % 42 for _ in range(10)]
count = len(set(data))
print(count)