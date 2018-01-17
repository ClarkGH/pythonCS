ex_list = [1,2,3,4,5,6,7,8,9,10]

def binary_search(num, num_list, head=0, tail=None):
  if not num_list:
    return False
  if not tail:
    tail = (len(num_list) - 1)
  mid = tail + ((head - tail)// 2)
  if num_list[mid] == num:
    return num_list[mid]
  elif head > tail:
    return False
  elif num_list[mid] > num:
    return binary_search(num, num_list, head, mid)
  elif num_list[mid] < num:
    return binary_search(num, num_list, mid+1, tail)

print binary_search(5, ex_list) 
print binary_search(1, ex_list) 
print binary_search(10, ex_list) 
print binary_search(6, ex_list) 
print binary_search(5, ex_list) 
print binary_search(11, ex_list) 
