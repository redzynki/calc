# this method will sum multiples of 3 and 5 up to x
def sum_of_multiples(x):
  numbers = range(0,x+1)
  elements_to_print = [element for element in numbers if element % 3 == 0 or element % 5 == 0]
  return sum(elements_to_print)