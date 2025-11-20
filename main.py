from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    dist = {v: (float('inf'), float('inf')) for v in graph}
    dist[source] = (0,0)
    pq = []
    heappush(pq, (0,0,source))

    while pq:
        w, edges, u = heappop(pq)
        if(w,edges) != dist[u]:
          continue
        for v,weight_uv in graph[u]:
            new_w = w + weight_uv
            new_edges = edges + 1
            
            if(new_w, new_edges) < dist[v]:
                dist[v] = (new_w, new_edges)
                heappush(pq, (new_w, new_edges, v))
    return dist

    pass
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parents = {}
    visited = {source}
    q = deque([source])

    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parents[v] = u
                q.append(v)
    return parents
    pass

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    curr = destination
    while curr in parents:
        parent = parents[curr]
        path.append(parent)
        curr = parent
    path.reverse()
    return ''.join(path)
    pass

