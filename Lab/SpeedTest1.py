import time
start = time.time()

a = range(100000)
b = []
for i in a:
    b.append(i*2)

end = time.time()
print(end - start)