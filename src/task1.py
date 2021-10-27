# out_contig.fa
# out_scaffold.fa
count = 0
length = 0
array = []
for line in open("out_scaffold.fa"):
    if(line[0] == '>'):
        count+=1
        data = int(line.split('_')[1][3:])
        length += data
        array.append(data)

print("Общее количество: ", count)
print("Общая длина: ",  length)
print("Длина самого динного: ", max(array))

summa = 0
N50 =0
array.sort(reverse=True)
for num in array:
    summa += num
    if (summa <= length/2):
        N50 = num

print("N50: ", N50)