num_min = float(input())
while True:
    num = input()
    if num == '.':
        print(num_min)
        break
    else:
        num_min = float(num) if float(num) < num_min else num_min
