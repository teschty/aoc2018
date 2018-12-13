with open("input.txt") as f:
    text = f.read()

values = list(map(int, text.split()))

def read_node(it):
    num_children = next(it)
    num_metadata = next(it)

    children = [read_node(it) for _ in range(num_children)]
    metadata = [next(it) for _ in range(num_metadata)]

    return sum(children) + sum(metadata)

iterator = iter(values)
print(read_node(iterator))
