# PythonProblem
Puzzle is a game which is a 5*5 matrix. All the blocks contains unique alphabets  except one block which is empty.The empty block can be moved either up, down, left, right as instructed by the player.
def puzzle(first):
    moves = ['A', 'B', 'L', 'R', 'O']
    above = [0, 1, 2, 3, 4]
    below = [20, 21, 22, 23, 24]
    left = [0, 5, 1., 15, 20]
    right = [4, 9, 14, 19, 24]
    liste = list(first) + list(input()) + list(input()) + list(input()) + list(input())
    instructions = list(input())
    for i in range(0, 25):
        if liste[i] == ' ':
            pos = i
            break
    for j in range(0, len(liste)):
         if instructions[j] not in moves:
            return "a"
         else:
            if instructions[j] != 'O':
                if instructions[j] == 'A':
                    if pos in above:
                        return False
                    else:
                        liste[pos], liste[pos - 5] = liste[pos - 5], liste[pos]
                        pos = pos - 5
                elif instructions[j] == 'B':
                    if pos in above:
                        return False
                    else:
                        liste[pos], liste[pos + 5] = liste[pos + 5], liste[pos]
                        pos = pos + 5
                elif instructions[j] == 'L':
                    if pos in above:
                        return False
                    else:
                        liste[pos], liste[pos - 1] = liste[pos - 1], liste[pos]
                        pos = pos - 1
                elif instructions[j] == 'R':
                    if pos in above:
                        return False
                    else:
                        liste[pos], liste[pos + 1] = liste[pos + 1], liste[pos]
                        pos = pos + 1
            else:
                return liste
l = []
first = input()
count = 0
while first != "Z":
    count += 1
    k = puzzle(first)
    if k != 0:
        l1, l2, l3, l4, l5 = k[0:5], k[5:10], k[10:15], k[15:20], k[20:25]
        la, lb, lc, ld, le = ' '.join(l1), ' '.join(l2), ' '.join(l3), ' '.join(l4), ' '.join(l5)
        print('Puzzle')
        print(la)
        print(lb)
        print(lc)
        print(ld)
        print(le)
    else:
        print('Puzzle')
        print("The puzzle has no final configuration")
    first = input()
