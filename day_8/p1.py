with open("input.txt") as f:
    text = f.read()

values = list(map(int, text.split()))

def read_node(i):
    num_children = next(i)
    num_metadata = next(i)

    children = [read_node(i) for _ in range(num_children)]
    metadata = [next(i) for _ in range(num_metadata)]

    return sum(children) + sum(metadata)

iterator = iter(values)
print(read_node(iterator))
