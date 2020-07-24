theboard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ',
            'low-M': ' ', 'low-R': ' '}


def printtheboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'
for i in range(9):
    printtheboard(theboard)
    print('Turn for the ' + turn + '. Move on which space?')
    move = input()
    theboard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printtheboard(theboard)
