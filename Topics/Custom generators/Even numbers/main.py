n = int(input())


def even():
    for _ in range(n):
        yield _ * 2


# Don't forget to print out the first n numbers one by one here
even_generator = even()
for i in even_generator:
    print(i)
