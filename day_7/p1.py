with open("input.txt") as f:
    lines = f.readlines()

graph = {}

for line in lines:
    step = line[5]
    dependency = line[36]

    vals = graph.get(dependency, [])
    vals.append(step)
    graph[dependency] = vals

    # make sure every key has some list
    graph[step]= graph.get(step, [])

order = ""

while True:
    # if a step has no dependency in it's list, it's available
    available = sorted([key for key in graph.keys() if len(graph[key]) == 0])

    if len(available) == 0:
        break

    step = available[0]

    # "complete" step by adding it to order
    order += step

    graph.pop(step)

    # delete step from all keys
    for key in graph.keys():
        if step in graph[key]:
            graph[key].remove(step)

print(order)
