import math
print("Pi is " + str (math.pi))
# Pi is 3.141592653589793

print("Pi is approx %0.2f" % (math.pi))
# Pi is approx 3.14

print("Pos or Neg: %+d %+d" % (-5,3)) 
# Pos or Neg: -5 +3

tmp_str = "Pos or Neg"
print("%s: %+d %+d" % (tmp_str,-5,3)) 
# Pos or Neg: -5 +3