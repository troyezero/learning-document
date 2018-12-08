# 字符串与ASCII码的转换学习总结

## 代码

<pre name="code" class="python">
x = input("请输入一个字符串：")
y = int(input("请输入一个ASCII码："))
print(x,"的ASCII码为：")
z = map(ord,x)
for i in z:
    print(i,end=" ")
print("\n")
print(y,"的ASCII码为：",chr(y))
</pre>

## map()函数

### 语法

map(function, iterable,  ...)

- function -- 函数
- iterable -- 一个或多个序列

使用方法

\>\>\>def  square(x) : \# 计算平方数

```
           return  x \*\* 2
```

\>\>\>map(square, \[1,2,3,4,5\])  \# 计算列表各个元素的平方

\[1, 4, 9, 16, 25\]

\>\>\>map(lambda  x: x \*\* 2, \[1, 2, 3, 4, 5\])  \# 使用 lambda 匿名函数

\[1, 4, 9, 16, 25\]

\#提供了两个列表，对相同位置的列表数据进行相加

\>\>\>map(lambda  x, y: x \+ y, \[1, 3, 5, 7, 9\], \[2, 4, 6, 8, 10\])

\[3, 7, 11, 15, 19\]

## 输出列表元素，以空格/逗号为分隔符

```python
l=[1,2,3,4]
for i in l:    
    print(i)
```

输出结果一行一个元素：

1

2

3

4

```python
l=[1,2,3,4]
for i in l:    
    print(i,end=' ')#以空格为分隔符
```

输出结果为：1 2 3 4 （注意，此时4后面还有一个空格）

```python
l=[1,2,3,4]
for i in l:    
    print(i,end=', ')#以逗号为分隔符
```

输出结果为：1,2,3,4, （注意，此时4后面还有一个空格）

```python
l = [1,2,3,4]  
print(" ".join(str(i) for i in l))
```

输出结果为：1 2 3 4（注意，此时4后面没有空格啦）

```python
l = [1,2,3,4]  
print(",".join(str(i) for i in l))
```

输出结果为：1,2,3,4（注意，此时4后面没有逗号）

### 转换

ASCII码转字符 chr(num) //num代表ASCII码，其大小应为0~255

字符转ASCII码 ord(ch) // ch表示字符

ord函数要传字符进去，chr函数要传一个整数进去，而input函数，默认的是使用字符串。
