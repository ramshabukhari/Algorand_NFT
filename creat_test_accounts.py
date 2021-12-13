import json
from algosdk import account, mnemonic

acct = account.generate_account()
address1 = acct[1]
print("Account 1")
print(address1)
mnemonic1 = mnemonic.from_private_key(acct[0])

print("Account 2")
acct = account.generate_account()
address2 = acct[1]
print(address2)
mnemonic2 = mnemonic.from_private_key(acct[0])

print("Account 3")
acct = account.generate_account()
address3 = acct[1]
print(address3)
mnemonic3 = mnemonic.from_private_key(acct[0])
print ("")
print("Copy off accounts above and add TestNet Algo funds using the TestNet Dispenser at https://bank.testnet.algorand.network/")
print("copy off the following mnemonic code for use later")
print("")
print("mnemonic1 = \"{}\"".format(mnemonic1))
print("mnemonic2 = \"{}\"".format(mnemonic2))
print("mnemonic3 = \"{}\"".format(mnemonic3))

#Account 1
#Y3GMBWMJ5LOKK27HYXC4IL66VL5K656MF4YFCOBI3RSZONQT5CICVDGVA4
#Account 2
#OH5MZZCP2QNYW463FDHOE6SLJ6MTJ6O3TRCADIIOU2DKKHRDEIWTUEDJXY
#Account 3
#IMXPY7EX3JBNAVHUGHOESB6HRVUKN4KW4PCM57OUOLLFY6WE52ALYXDJD4

#Copy off accounts above and add TestNet Algo funds using the TestNet Dispenser at https://bank.testnet.algorand.network/
#copy off the following mnemonic code for use later

#mnemonic1 = "baby already laundry venture session dinosaur engage flag match fan ginger suffer over result method fruit busy divide scan story sunset lock space about repair"
#mnemonic2 = "diamond diesel today fruit gun point auto casual distance inspire place tank consider slow dust pear where foot shiver budget myth jump glove absorb soup"
#mnemonic3 = "choice auto sausage ring later mesh chuckle salon sting lady upgrade lecture lumber celery spare pulp nephew airport final today problem enhance behind absorb wait"
