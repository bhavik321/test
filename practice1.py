s=input()
max_count=0
for i in range(len(s)):
	count=1
	for j in range(i+1,len(s)):
		str=s[j:count+1]
		count1=0
		if(str[i] == str[j]):
			count1=count1
		else:
			count1=count1+1
	max_count=count1
	count=count+1
print(max_count)		

