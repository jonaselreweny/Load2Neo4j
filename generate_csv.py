import csv
import random

# 1000000 and 52 == roughly 1GB (WARNING TAKES a while, 30s+)
# 10000000 and 3 == roughly 657MB
rows = 10000000
columns = 3
print_after_rows = 1000000

def generate_random_row(col):
    a = []
    l = [i]
    for j in range(col):
        l.append(random.random())
    a.append(l)
    return a

if __name__ == '__main__':
    f = open('sample.csv', 'w')
    w = csv.writer(f, lineterminator='\n')
    for i in range(rows):
        if i % print_after_rows == 0:
            print(".", end="", flush=True)
        w.writerows(generate_random_row(columns))
    f.close()