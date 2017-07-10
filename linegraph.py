print("LINE GRAPH")
sc = 0
ft = 0
hc = 0
bs = 0
bk = 0
tn = 0
sw = 0
rn = 0
lc = 0
rg = 0
o = 0
input ("What sports do your friends like? This code will see how many like certain sports by creating it into a line graph.")
input("Remember: Type \n 'SOCCER' for Soccer/Football \n 'FOOTBALL' for American Football \n and Track as Running\n Also, if you don't input a sport, it will be called 'Other'")
donthavefriends = input("Type how many friends you have.")
donthavefriends = int(donthavefriends)

while donthavefriends > 0:
	if donthavefriends == 0:
		break
	else:
		input("Type the name of your friend.")
		count = input("Type a sport he/she/it likes.")
		count.lower()
		if count == 'soccer':
			sc += 1
		elif count == 'football':
			ft += 1
		elif count == 'hockey':
			hc += 1
		elif count == 'baseball':
			bs += 1
		elif count == 'basketball':
			bk += 1
		elif count == 'tennis':
			tn += 1
		elif count == 'rugby':
			rg += 1
		elif count == 'running':
			rn += 1
		elif count == 'lacrosse':
			lc += 1
		elif count == 'swimming':
			sw += 1
		else:
			o+= 1
		donthavefriends -= 1

print("Here is the LINE GRAPH")
print('Basketball: ', 'x'*bk)
print('Baseball:   ', 'x'*bs)
print('Football:   ', 'x'*ft)
print('Lacrosse:   ', 'x'*lc)
print('Swimming:   ', 'x'*sw)
print('Running:    ', 'x'*rn)	 
print('Hockey:     ', 'x'*hc)
print('Soccer:     ', 'x'*sc)
print('Tennis:     ', 'x'*tn)
print('Rugby:      ', 'x'*rg)
print('Other:      ', 'x'*o)
input()