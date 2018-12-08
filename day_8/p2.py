with open("input.txt") as f:
    text = f.read()

values = list(map(int, text.split()))

def read_node(it):
    num_children = next(it)
    num_metadata = next(it)

    children = [read_node(it) for _ in range(num_children)]
    metadata = [next(it) for _ in range(num_metadata)]

    if len(children) == 0:
        return sum(metadata)

    return sum([children[i - 1] for i in metadata if i > 0 and i <= len(children)])

iterator = iter(values)
print(read_node(iterator))
