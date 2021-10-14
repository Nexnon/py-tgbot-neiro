

def reading_db():
    mass = [[[0] * 28 for i in range(0, 28)] for t in range(0, 9)]
    data_B = open('db2.txt', 'r')
    for n in range(0,9):
        line = data_B.readline().split()
        for x in range(0, 28):
            for y in range(0, 28):
                value = y + (x * 28)
                mass[n][x][y] = float(line[value])
    data_B.close()
    return mass

def writing_db(mass):
    data_B = open('db1.txt', 'w')
    for n in range(0,9):
        line = ''
        for x in range(0, 28):
            for y in range(0, 28):
                line += str(mass[n][x][y]) + ' '
             
    line += '\n'
    data_B.writelines(line)
    data_B.close()

weight = reading_db()