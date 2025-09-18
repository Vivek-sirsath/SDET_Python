# Collections vs Generators w.r.t performance and memory usage.
import sys
import time

n = 10**6   # 1 million numbers.

print("================== Generate numbers Using Normal Collection --> List =====================")

start_time = time.time()
numbers_list = [i for i in range(n)]   # List Comprehension # stores all value in memory
end_time = time.time()
print(f"Time taken by normal collection : {end_time-start_time:.6f}")
# Print size of memory occupied in bytes.
print("Size of numbers_list in bytes - " ,sys.getsizeof(numbers_list))

print("================== Generate numbers Using Generator =====================")
# If we try to create a tuple by tuple comprehension, then it will not create a tuple. Rather it will create a generator.
# It returns a generator object.

start_time = time.time()
numbers_generator = (i for i in range(n))     # generator object
end_time = time.time()
print(f"Time taken by generator: {end_time-start_time:.6f}")
# Print size of memory occupied in bytes.
print("Size of generator_list in bytes - " ,sys.getsizeof(numbers_generator))




