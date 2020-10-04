graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
    
         
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for it in graph[vertex] - set(path):
            if it == goal:
                yield path + [it]
            else:
                stack.append((it, path + [it]))


def dfs_recursion(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for it in graph[start] - visited:
        dfs_recursion(graph, it, visited)
    return visited


def dfs_recursion_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for it in graph[start] - set(path):
        yield from dfs_recursion_paths(graph, next, goal, path + [it])
        

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def bfs_shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

if __name__ == '__main__':
	print(dfs(graph, 'A')) 
	print(list(dfs_paths(graph, 'A', 'F')))

	print(dfs_recursion(graph, 'C')) 
	print(list(dfs_paths(graph, 'C', 'F')))

	print(bfs(graph, 'A'))
	print(list(bfs_paths(graph, 'A', 'F')))
	print(bfs_shortest_path(graph, 'A', 'F'))
