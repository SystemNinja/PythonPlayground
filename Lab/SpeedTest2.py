import time
start = time.time()

a = range(100000)
b = [i*2 for i in a]

end = time.time()
print(end - start)