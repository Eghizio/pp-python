bank = {
    "adam": 1337,
    "beth": 420,
    "cecil": 0,
}


print(bank)
print(bank["adam"])
print(bank["beth"])
print(bank["cecil"])



print(bank.keys())
print(bank.values())

print( list( bank.keys() ) )
print( list( bank.values() ) )



bank["cecil"] = 800
print(bank)

bank["beth"] += 300
print(bank)



for key, value in bank.items():
    print(f"{key} == {value}")
