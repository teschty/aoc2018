with open("input.txt") as f:
    lines = f.readlines()

graph = {}

for line in lines:
    first = line[5]
    second = line[36]

    vals = graph.get(second, [])
    vals.append(first)
    graph[second] = vals

    # make sure every key has some list
    graph[first]= graph.get(first, [])

order = ""

while True:
    # if 
    available = sorted([key for key in graph.keys() if len(graph[key]) == 0])

    if len(available) == 0:
        break

    step = available[0]

    # "complete" step by adding it to order
    order += step

    graph.pop(step)

    # delete step from all keys
    for key in graph.keys():
        x = []

        if step in graph[key]:
            graph[key].remove(step)

print(order)
