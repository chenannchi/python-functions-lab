def sum_to(n):
  total = 0
  for i in range(n+1):
    total+=i
  return total

print(sum_to(6))  # returns 21
print(sum_to(10)) # returns 55

def largest(arr):
  return max(arr)

print(largest([1, 2, 3, 4, 0]))  # returns 4
print(largest([10, 4, 2, 231, 91, 54]))  # returns 231

def occurrences(str1, str2):
  return str1.count(str2)

print(occurrences('fleep floop', 'e'))     # returns 2
print(occurrences('fleep floop', 'p'))     # returns 2
print(occurrences('fleep floop', 'ee'))    # returns 1
print(occurrences('fleep floop', 'fe'))    # returns 0

def product(*args):
  total = 1
  for arg in args:
    total*=arg
  return total

print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))
