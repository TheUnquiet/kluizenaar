from Kluizenaar import Kluizenaar

spel = Kluizenaar(4)
print(spel)

print(sorted(spel.posities((0,0), 'H')))

print(spel.isGeldig('R', (0,0)))

print(spel.isGeldig('R', (0,1)))

print(spel.zet('R', (0, 0), 'H'))

#print(spel.zet('R', (1, 2), 'V'))

print(spel.zet('B', (0, 2), 'U').zet('Y', (1, 2), 'U'))

print(spel.zet('R', (3, 1), 'U').zet('Y', (3, 2), 'H'))

print(spel.zet('R', (1, 3), 'V').zet('B', (2, 0), 'H'))

#print(spel.mogelijke_zetten())