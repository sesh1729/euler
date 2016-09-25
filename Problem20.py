
# Problem 29 of Project Euler
# Distinct powers

powers = []

for i in range(2,101):
    for j in range(2,101):
        powers.append(pow(i,j))
print len(set(powers))

