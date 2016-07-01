 
# -*- coding utf-8 -*-

case1 = ' '
case2 = ' '
case3 = ' '
case4 = ' '
case5 = ' '
case6 = ' '
case7 = ' '
case8 = ' '
case9 = ' '
cases = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
pion = (raw_input('quel pion veut tu prendre joueur1 (O/X)? '))
if pion == 'X':
        pion2 = 'O'
        print 'joueur 2 prend les O'
else:
		pion2 = 'X' #Il faut que pion2 soit defini dans tous les cas
		print 'joueur 2 prend les X'


def grille (cases):
  print '|' + cases[1] + '|' + cases[2] + '|' + cases[3] + '|'
  print '|' + cases[4] + '|' + cases[5] + '|' + cases[6] + '|'
  print '|' + cases[7] + '|' + cases[8] + '|' + cases[9] + '|'
  return

for n in range(1,6):
    question1 = int(raw_input('ou veut tu jouer joueur1 ? '))
    cases[question1]=pion
    grille (cases)
    if n == 5:
        break 
    question2 = int(raw_input('ou veut tu jouer joueur 2 ? '))
    cases[question2]=pion2
    grille (cases)

print 'End'

sortie = raw_input('appuie sur une touche pour quitter le programme ')


