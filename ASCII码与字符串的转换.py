x = input("请输入一个字符串：")
y = int(input("请输入一个ASCII码："))
print(x,"的ASCII码为：")
z = map(ord,x)
for i in z:
    print(i,end=" ")
print("\n")
print(y,"的ASCII码为：",chr(y))