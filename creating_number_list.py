number = int(input("Enter a number: "))
number_list = [i for i in range(1, number+1)]

for i in number_list:
    for j in range(1, i+1):
        print(i*j, end='\t')

        print(end='\n')

number_list = number_list[::-1]


for i in number_list[1:]:
    for j in range(1, i+1):
        print(i*j, end='\t')
        print(end='\n')
