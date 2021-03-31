data='''My name is saurabh'''

inc='''1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.+-@$()#:'/ *=!?
'''

inc2='''1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.+-@$()#:'/ *=!?
'''
s=inc2[::-1]

dic = {}
newdata=''''''

ii=0
for i in inc :
	dic[i]=s[ii]
	ii=ii+1
	


for i in data:
	try:
		d1=dic[i]
		newdata = newdata+d1
	except:
		newdata=newdata+i


print(newdata)
