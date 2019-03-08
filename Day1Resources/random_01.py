import random

# random.randint(a,b)
# return a randmon integer N such that a <= N <= b
print(random.randint(1,10))
  
# random.random()
# Return the next random floating point number 
# in the range [0.0, 1.0]
print(random.random())

# shuffle a list
my_list=[1,2,3,4,5]
random.shuffle(my_list)
print(my_list)

# randomly chose from a list
print(random.choice(my_list))

