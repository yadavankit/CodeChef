#Take Input for First Line (N, K)
[chef_street, k] = raw_input().split()

#Take Input for Second Line (Special Numbers for Streets)
special_token = raw_input().split()

#Integerify
chef_street = int(chef_street)
k = int(k)

#Assign product for first and last streets
product = int(special_token[0]) * int(special_token[chef_street-1])
#Initialise ProductMin List
product_min = []

#For Middle Addresses
for i in range(1, chef_street-1):
	product_temp = int(product) * int(special_token[i])
	product_min.append(product_temp)

#Print Minimum Answer
print (min(product_min)%1000000007)



