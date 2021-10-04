A=((1),[2,3],[4])
print(A[2])
bool = '1' in {'1','2'}
#print(bool)

print(True or False)

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)