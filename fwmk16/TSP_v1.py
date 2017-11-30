### TSP

routes = []


def find_paths(node, cities, path, distance):
    # Add way point
    path.append(node)

    # Calculate path length from current to last node
    if len(path) > 1:
        distance += cities[path[-2]][node]

    # If path contains all cities and is not a dead end,
    # add path from last to first city and return.
    if (len(cities) == len(path)) and (cities[path[-1]].has_key(path[0])):
        global routes
        path.append(path[0])
        distance += cities[path[-2]][path[0]]
        print path, distance
        routes.append([distance, path])
        return

    # Fork paths for all possible cities not yet used
    for city in cities:
        if (city not in path) and (cities[city].has_key(node)):
            find_paths(city, dict(cities), list(path), distance)



cities = {
        'A': {'D': 195, 'B': 86, 'C': 178, 'I': 180, 'K': 91},
        'B': {'A': 86, 'D': 107, 'E': 171, 'C': 123},
        'C': {'A': 178, 'B': 123, 'E': 170},
        'D': {'A': 195, 'B': 107, 'E': 210, 'F': 210, 'G': 135, 'H': 64},
        'E': {'D': 210, 'B': 171, 'C': 170, 'G': 230, 'F': 230},
        'F': {'E': 230, 'D': 210, 'G': 85},
        'G': {'F': 85, 'E': 230, 'D': 135, 'H': 67},
        'H': {'G': 67, 'D': 64, 'I': 191},
        'I': {'H': 191, 'A': 180, 'K': 85, 'J': 91},
        'J': {'I': 91, 'K': 120},
        'K': {'I': 120, 'J': 85, 'A': 91}
    }

print "Start: A"
find_paths('A', cities, [], 0)
print "\n"
routes.sort()
if len(routes) != 0:
    print "Shortest route: %s" % routes[0]
else:
    print "FAIL!"