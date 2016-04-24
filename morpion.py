
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

def grille (case1, case2, case3, case4, case5, case6, case7, case8, case9):
  print '|' + case1 + '|' + case2 + '|' + case3 + '|'
  print '|' + case4 + '|' + case5 + '|' + case6 + '|'
  print '|' + case7 + '|' + case8 + '|' + case9 + '|'
  return



for n in range(1,6):
    question1 = raw_input('ou veut tu jouer joueur1 ? ')
    if question1 == '1':
        case1 = 'X'
    if question1 == '2':
        case2 = 'X'
    if question1 == '3':
        case3 = 'X'
    if question1 == '4':
        case4 = 'X'
    if question1 == '5':
        case5 = 'X'
    if question1 == '6':
        case6 = 'X'
    if question1 == '7':
        case7 = 'X'
    if question1 == '8':
        case8 = 'X'
    if question1 == '9':
        case9 = 'X'
    grille (case1, case2, case3, case4, case5, case6, case7, case8, case9)
    if n == 5:
        break 
    question2 = raw_input('ou veut tu jouer joueur 2 ? ')
    if question2 == '1':
        case1 = 'O'
    if question2 == '2':
        case2 = 'O'
    if question2 == '3':
        case3 = 'O'
    if question2 == '4':
        case4 = 'O'
    if question2 == '5':
        case5 = 'O'
    if question2 == '6':
        case6 = 'O'
    if question2 == '7':
        case7 = 'O'
    if question2 == '8':
        case8 = 'O'
    if question2 == '9':
        case9 = 'O'
    grille (case1, case2, case3, case4, case5, case6, case7, case8, case9)

print 'End'

