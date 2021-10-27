
# out_scaffold.fa
# out_gapClosed.fa
data = 0
array = []
check = 0
for line in open("out_gapClosed.fa"):
    if(line[0] != '>'):
        data += len(line.strip())
    else:
        if (check != 0):
            array.append(data)
        data = 0
        check = 1
array.append(data)

maxim = -100
position = 0
for num in array:
    if maxim < num:
        maxim = num
        position_max = position
    position+=1

print("Номер самого длинного: ", position_max + 1)

c = -1
text = ""
for line in open("out_gapClosed.fa"):
    if (line[0] == '>'):
        c+=1
    elif (c == position_max):
        text += line.strip()

lenN = 0
countgap = 0
bool = False
for letter in text:
    if(letter == 'N'):
        lenN +=1
        if (bool == False):
            countgap += 1
        bool = True
    else:
        bool = False

print("Количетво гэпов: ", countgap)
print("Общая длина: ", lenN)
