coins=[1,5,10]
amount=16

coins=sorted(coins,reverse=True)
print(coins)

i=0
total=0
result=[]
change=0
for coin in coins:
    print(coin)
    print(amount,change,total)
    if amount>0 and amount>=coin:

        change=amount //coin
        result.append(change)
        total=total+change
  
        amount=amount-(change*coin)
      

print(total)
print(result)
