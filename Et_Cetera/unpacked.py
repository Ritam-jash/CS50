# without used unpacked
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]))




# using unpacked in list
def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins))




# using dict
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons" : 100, "sickles" : 50, "knuts" : 25}

print(total(**coins))




# Now we using args & kwargs

def f(*args, **kwargs):
    print("position:", args)

f(100, 50, 25)




# now using kwargs
def f(*args, **kwargs):
    print("named:", kwargs)


f(galleons = 100, sickles = 50, knuts = 25)
