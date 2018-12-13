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

class Worker:
    def __init__(self, name):
        self.done()
        self.name = name
    
    def next(self):
        if self.time_left > 0:
            self.time_left -= 1
    
    def done(self):
        self.time_left = -1
        self.step = None

    def is_done(self):
        return self.time_left == 0

    def start(self, step, time):
        print(f"Worker {self.name} working on {step}")
        self.step = step
        self.time_left = time

workers = [Worker(1), Worker(2), Worker(3), Worker(4), Worker(5)]
time = 0

while True:
    if len(graph.keys()) == 0: 
        break
            
    available = sorted([key for key in graph.keys() if len(graph[key]) == 0])

    for step in available:
        available_workers = [worker for worker in workers if worker.step == None]
        if len(available_workers) == 0:
            break

        available_workers[0].start(step, 60 + (ord(step) - ord('A') + 1))
        graph.pop(step)
        
    for worker in workers:
        if worker.is_done():
            for key in graph.keys():
                if worker.step in graph[key]:
                    graph[key].remove(worker.step)
            
            worker.done()
        else:
            worker.next()

    time += 1

print(time)
