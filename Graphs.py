#http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    #print visited
    for next in graph[start]:
        print graph[start]
        if next not in visited:
            print next
            dfs(graph, next, visited)
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs2(graph, start):
    i = 0
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        print queue
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

visited_dfs =  dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}

visited_bfs =  bfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
print('---------------------')
visited_bfs2 =  bfs2(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}

print('---------------------')
print graph
print visited_dfs
print visited_bfs
print visited_bfs2