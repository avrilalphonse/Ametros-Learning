nums = 6
# outer loop
for i in range(1,nums):
    # nested loop
    for j in range(i):
      print(i, end=' ') 
    for i in range(i+1,nums):
      print(i, end=' ')
    print('')