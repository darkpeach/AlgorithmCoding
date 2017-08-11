from _029_DivideTwoInteger import Solution
result = Solution()

########
a = [1,2,3,4]
b = [5,6,7,8]
c = a+b
print(c)
temp = c[3+1:]
temp.reverse()
print(c[:3+1]+temp)
#print(c[:3+1]+c[3+1:].reverse())