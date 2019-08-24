num = input()
one_two = 0
two_one = 0
# 예외 21212 << 해당 과정에 대한 내용 안나옴
for i in range(len(num)):
    if num[i] == '1' or num[i] == '2':
        num = num[i:]
        break

for i in range(0,len(num)-1,2):
    if one_two > 0 and two_one > 0:
        break
    else:
        if num[i] == '1' and num[i+1] == '2':
            one_two += 1
        if num[i] == '2' and num[i+1] == '1':
            two_one += 1

if one_two == 1 and two_one == 1:
    print("Yes")
else:
    print("No")