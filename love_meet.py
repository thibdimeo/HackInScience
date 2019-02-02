alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']

bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']

silvester = ['XVIII', 'XIX', 'III', 'I', 'III', 'XVIII']

def love_meet(bob, alice):
    aliceset = set(alice)
    bobset = set(bob)
    return(aliceset&bobset)


def affair_meet(bob,alice,silvester):
    aliceset = set(alice)
    bobset = set(bob)
    silvesterset = set(silvester)
    return(aliceset&silvesterset-bobset)

print(affair_meet(alice,bob,silvester))