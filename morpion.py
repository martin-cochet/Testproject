
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

pion = (raw_input('quel pion veut tu prendre joueur1 (O/X)? '))
if pion == 'X':
        pion2 = 'O'
        print 'joueur 2 prend les O'
else:
		print 'joueur 2 prend les X'


def grille (case1, case2, case3, case4, case5, case6, case7, case8, case9):
  print '|' + case1 + '|' + case2 + '|' + case3 + '|'
  print '|' + case4 + '|' + case5 + '|' + case6 + '|'
  print '|' + case7 + '|' + case8 + '|' + case9 + '|'
  return

for n in range(1,6):
    question1 = raw_input('ou veut tu jouer joueur1 ? ')
    if question1 == '1':
        case1 = pion
    if question1 == '2':
        case2 = pion
    if question1 == '3':
        case3 = pion
    if question1 == '4':
        case4 = pion
    if question1 == '5':
        case5 = pion
    if question1 == '6':
        case6 = pion
    if question1 == '7':
        case7 = pion
    if question1 == '8':
        case8 = pion
    if question1 == '9':
        case9 = pion
    grille (case1, case2, case3, case4, case5, case6, case7, case8, case9)
    if n == 5:
        break 
    question2 = raw_input('ou veut tu jouer joueur 2 ? ')
    if question2 == '1':
        case1 = pion2
    if question2 == '2':
        case2 = pion2
    if question2 == '3':
        case3 = pion2
    if question2 == '4':
        case4 = pion2
    if question2 == '5':
        case5 = pion2
    if question2 == '6':
        case6 = pion2
    if question2 == '7':
        case7 = pion2
    if question2 == '8':
        case8 = pion2
    if question2 == '9':
        case9 = pion2
    grille (case1, case2, case3, case4, case5, case6, case7, case8, case9)

print 'End'

sortie = raw_input('appuie sur une touche pour quitter le programme ')


