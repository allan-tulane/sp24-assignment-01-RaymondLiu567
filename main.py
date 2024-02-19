"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  if x <= 1:
      return x
  else:
      ra = foo(x - 1)
      rb = foo(x - 2)
      return ra + rb

def longest_run(myarray, key):
  longest = 0
  current = 0
  for number in myarray:
    if number == key:
        current += 1
        longest = max(longest, current)
    else:
        current = 0
  return longest


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
  # Base case for empty list
  if not mylist:
      return Result(0, 0, 0, True)

  # Base case for single element list
  if len(mylist) == 1:
      if mylist[0] == key:
          return Result(1, 1, 1, True)
      else:
          return Result(0, 0, 0, False)

  # Recursive case: divide the list
  mid = len(mylist) // 2
  left_half = longest_run_recursive(mylist[:mid], key)
  right_half = longest_run_recursive(mylist[mid:], key)

  # Combine solutions
  if left_half.is_entire_range and right_half.is_entire_range and mylist[mid-1] == key:
      return Result(left_half.left_size + right_half.right_size, 
                    left_half.left_size + right_half.right_size, 
                    left_half.left_size + right_half.right_size, 
                    True)

  longest_run_across = left_half.right_size + right_half.left_size if mylist[mid-1] == mylist[mid] == key else 0
  longest_run = max(left_half.longest_size, right_half.longest_size, longest_run_across)
  left_size = left_half.left_size if mylist[0] == key else 0
  right_size = right_half.right_size if mylist[-1] == key else 0

  return Result(left_size, right_size, longest_run, False)



