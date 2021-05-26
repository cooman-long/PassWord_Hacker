import itertools

for i in range(1, 4):
    for flower in itertools.combinations(flower_names, i):
        print(flower)
