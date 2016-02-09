import random
print (".DDDD.........++........DDDD.....")
print (".D...D........++........D...D....")
print (".D....D...+++++++++++...D....D...")
print (".D...D........++........D...D....")
print (".DDDD.........++........DDDD.....")
print ("")
print ("---Character Calculator---")
print ("")
roll_again= input("Calculate Character Stats? (y/n)")

while roll_again in ["Yes" , "yes" , "y" , "Y"]:
	roll1 = random.randint(1,6)
	roll2 = random.randint(1,6)
	roll3 = random.randint(1,6)
	roll4 = random.randint(1,6)
	if roll1 < roll2 and roll3 and roll4:
		roll = roll2 + roll3 + roll4
	if roll2 < roll1 and roll3 and roll4:
		roll = roll1 + roll3 + roll4
	if roll3 < roll2 and roll1 and roll4:
		roll = roll2 + roll1 + roll4
	if roll4 < roll2 and roll3 and roll1:
		roll = roll2 + roll3 + roll1
	rolla = random.randint(1,6)
	rollb = random.randint(1,6)
	rollc = random.randint(1,6)
	rolld = random.randint(1,6)
	if rolla < rollb and rollc and rolld:
		rolle = rollb + rollc + rolld
	if rollb < rolla and rollc and rolld:
		rolle = rolla + rollc + rolld
	if rollc < rollb and rolla and rolld:
		rolle = rollb + rolla + rolld
	if rolld < rollb and rollc and rolla:
		rolle = rollb + rollc + rolla
	rollf = random.randint(1,6)
	rollg = random.randint(1,6)
	rollh = random.randint(1,6)
	rolli = random.randint(1,6)
	if rollf < rollg and rollh and rolli:
		rollj = rollg + rollh + rolli
	if rollg < rollf and rollh and rolli:
		rollj = rollf + rollh + rolli
	if rollh < rollg and rollf and rolli:
		rollj = rollg + rollf + rolli
	if rolli < rollg and rollh and rollf:
		rollj = rollg + rollh + rollf
	rollk = random.randint(1,6)
	rolll = random.randint(1,6)
	rollm = random.randint(1,6)
	rolln = random.randint(1,6)
	if rollk < rolll and rollm and rolln:
		rolls = rolll + rollm + rolln
	if rolll < rollk and rollm and rolln:
		rolls = rollk + rollm + rolln
	if rollm < rolll and rollk and rolln:
		rolls = rolll + rollk + rolln
	if rolln < rolll and rollm and rollk:
		rolls = rolll + rollm + rollk
	rollo = random.randint(1,6)
	rollp = random.randint(1,6)
	rollq = random.randint(1,6)
	rollr = random.randint(1,6)
	if rollo < rollp and rollq and rollr:
		rollt = rollp + rollq + rollr
	if rollp < rollo and rollq and rollr:
		rollt = rollo + rollq + rollr
	if rollq < rollp and rollo and rollr:
		rollt = rollp + rollo + rollr
	if rollr < rollp and rollq and rollo:
		rollt = rollp + rollq + rollo
	rollu = random.randint(1,6)
	rollv = random.randint(1,6)
	rollw = random.randint(1,6)
	rollx = random.randint(1,6)
	if rollu < rollv and rollw and rollx:
		rolly = rollv + rollw + rollx
	if rollv < rollu and rollw and rollx:
		rolly = rollu + rollw + rollx
	if rollw < rollv and rollu and rollx:
		rolly = rollv + rollu + rollx
	if rollx < rollv and rollw and rollu:
		rolly = rollv + rollw + rollu
	print ("")
	print ("You rolled:",roll,",",rolle,",",rollj,",",rolls,",",rollt,",",rolly)
	print ("")
	avg = (roll + rolle + rollj + rolls + rollt + rolly)/6
	if avg >= 12:
		print ("-----Above average roll----")
	if avg < 12:
		print ("-----Below average roll----")
	print ("")
	roll_again = input ("Would you like to roll again?")
	print ("")
	print ("")
print (" ")
print ("Thanks for Playing!")