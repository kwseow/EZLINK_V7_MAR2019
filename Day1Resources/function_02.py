def identCar(car=None, colour="red"):
  if car == None:
    print("You have to give me a car name")
    return
  print("Car %s has colour %s" % (car, colour))
  
identCar(colour="blue")
# You have to give me a car name

identCar(car="toyota")
# Car toyota has colour red