ex_list = [1,2,3,4,5,6,7,8,9,10]

def binary_search(num, num_list, head=0, tail=None):
  if not num_list:
    return None

  tail = (len(num_list) - 1) if tail is None else tail
  mid = (head + tail) // 2

  if num_list[mid] == num:
    return num_list[mid]
  elif num_list[mid] < num:
    head = mid
    return binary_search(num, num_list, head, tail)
  elif num_list[mid] > num:
    tail = mid
    return binary_search(num, num_list, head, tail)
  elif head >= tail:
    return None

print binary_search(1, ex_list) 
# print binary_search(10, ex_list) 
# print binary_search(4, ex_list) 
# print binary_search(6, ex_list) 
# print binary_search(5, ex_list) 
# print binary_search(11, ex_list) 
