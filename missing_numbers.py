def missing_numbers(num_list):
      original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
      num_list = set(num_list)
      return (list(num_list ^ set(original_list)))

print(missing_numbers([1,2,3,4,7,10]))
print(missing_numbers([10,11,12,17]))