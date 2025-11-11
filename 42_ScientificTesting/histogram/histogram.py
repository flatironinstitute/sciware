import math

### TODO: Write a set of narrowly focused tests for the code in this file.
#  Be sure to cover all its important properties.
#  You can make whatever changes you want to the code, but be sure
#  not the change the user-facing interface of the histogram function.
#
#    Hint:
#  When you're thinking about the important properties of the function,
#  think about whether its operations have a natural grouping.
#  How can you make it easier to test those individually?


def histogram(file, max_width = 76):
    data = {}
    total_data = 0
    with open(file, 'r') as f:
        for line in f:
            l = line.rstrip()
            for t in l.split():
                if t in data:
                    data[t] += 1
                else:
                    data[t] = 1
                total_data += 1

    sorted_data = sorted(data, key=lambda x: data[x], reverse=True)

    for i in range(12):
        e = sorted_data[i]
        n = data[e]
        width = min(math.floor(max_width * n * 9/total_data), max_width)
        label = f"{e}:"
        print(f"{label:<4}{'#' * width}")


if __name__ == '__main__':
    histogram('histogram.data', 100)
