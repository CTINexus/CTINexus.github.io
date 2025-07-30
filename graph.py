def component(edges, n):
    # edge_dict = {i:[i] for i in range(n)}
    # for s, t in edges:
    #     edge_dict[s] += [t]
    #     edge_dict[t] += [s]
    
    # result = n
    # for node in range(n):
    #     for v in edge_dict[node]:
    #         if node not in edge_dict[v]:
    #             result -= 1

    #     result -= (len(edge_dict[node]) - 1)

    return result

input = [[0,1],[0,2],[1,2],[3,4]]
print(component(input, 6))