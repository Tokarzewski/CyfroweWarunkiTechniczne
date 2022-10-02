from przepisy_ogolne import grupa_wysokosci

# 1. jaką grupę wysokości będzie miał budynek mieszkalny o wysokosci 12 m mający 5 kondygnacji nadziemnych?
case1 = grupa_wysokosci(True, 12, 5)

# 2. jaką grupę wysokości będzie miał budynek mieszkalny o wysokosci 30 m mający 6 kondygnacji nadziemnych?
case2 = grupa_wysokosci(True, 30, 6)

# 3. jaką grupę wysokości będzie miał budynek mieszkalny o wysokosci 60 m mający 15 kondygnacji nadziemnych?
case3 = grupa_wysokosci(True, 60, 15)

print("case1:", case1)
print("case2:", case2)
print("case3:", case3)