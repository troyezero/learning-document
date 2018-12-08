print("在1到10000的范围内，阿姆斯特朗数为：")
for num in range(1,10000) :
  sum = 0
  i = 0
  n=len(str(num))
  temp = num
  while temp > 0:
	  digit = temp % 10
	  sum +=digit ** n
	  temp //= 10
	  i = i+1
	  if num == sum:
	    if i == n:		
	      print(num,end=" ")