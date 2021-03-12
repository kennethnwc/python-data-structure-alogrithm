def binary_search(array):
  def condition(value):
    pass
  
  left = 0
  right = len(array)
  
  while left < right:
    mid = left + (right - left) // 2
    if condition(mid):
      right = mid
    else:
      left = mid + 1
   
  return left
