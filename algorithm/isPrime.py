def isPrime(list_a):
	list_prime=[]
	for x in list_a:
		if all(x%y!=0 for y in range(2,x)):
			list_prime.append(x)
	return list_prime

a=[12,13,7,9,19]
b=isPrime(a)
print(b)
