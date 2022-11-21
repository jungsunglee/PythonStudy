'''
1) Print odd numbers from 1 to N.
2) Calculate the sum from 1 to N.
3) Print divisor of N.
'''

N = int(input('Please input the count number : '))
result_1 = []
for i in range(1,N+1):
    if i%2==1:
        result_1.append(i)
print('Odd Number : ' + ','.join(str(e) for e in result_1))

result_2 : int = 0
for i in range(1,N+1):
    result_2 +=i
print('Sum :', result_2)

result_3 : list= []
for i in range(1, N+1):
    if N%i==0:
        result_3.append(i)
print('Divisor of {} : '.format(N) + ','.join(str(e) for e in result_3))
