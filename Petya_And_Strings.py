# Letter case does not matter => Tp vjg visu lowercase sataisit
# Ja vienādi print 0
# Ja pirmais ir mazāk nekā otrais print -1
# Ja otrais ir mazāk kā pirmais print 1

FstStrng = input()
SndStrng = input()

FstStrng = FstStrng.lower()
SndStrng = SndStrng.lower()

if FstStrng == SndStrng :
    print(0)

if FstStrng > SndStrng :
    print(1)

if SndStrng > FstStrng :
    print(-1)