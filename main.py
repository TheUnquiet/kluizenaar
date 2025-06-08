from Kluizenaar import Kluizenaar

spel = Kluizenaar(4)
print(spel)

print(sorted(spel.posities((0,0), 'H')))

print(spel.isGeldig('R', (0,0)))

print(spel.isGeldig('R', (0,1)))

print(spel.zet('R', (0, 0), 'H'))

print(spel.zet('R', (1, 2), 'V'))
