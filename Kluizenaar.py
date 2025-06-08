class Kluizenaar:
    def __init__(self, n):
        self.n = n
        self.board = [['.' for i in range(n)] for i in range(n)]

    def __str__(self):
        return '\n'.join(' '.join(rij) for rij in self.board)
    
    def posities(self, pos, plaatsing):
        r, k = pos
        if plaatsing == 'U':
            return {(r, k)}
        elif plaatsing == 'H':
            return {(r, k), (r, k+1)}
        elif plaatsing == 'V':
            return {(r, k), (r+1, k)}
        else:
            raise ValueError("Plaatsing is ongeldig")
    
    def isGeldig(self, kleur, pos):
        r, k = pos
        if self.board[r][k] != '.': # 'B'
            return False
        if not r < self.n and k < self.n:
            return False
        for diagonaal_r in [-1, 0, 1]:
            for diagonaal_k in [-1, 0, 1]:
                nr, nk = r + diagonaal_r, k + diagonaal_k
                if 0 < nr < self.n and 0 < nk < self.n:
                    if self.board[nr][nk] == kleur:
                        return False
        return True
    
    def zet(self, kleur, pos, plaatsing):
        posities = self.posities(pos, plaatsing)

        for (r, k) in posities:
            if not self.isGeldig(kleur, (r, k)):
                raise AssertionError("Ongeldige zet")
            
        for (r, k) in posities:
            self.board[r][k] = kleur # 'B'
        return self

