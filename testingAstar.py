#TASK1-a :Develop code to implement the A* algorithm in order to find the optimal path in the Travel
# in Romania problem. Use the heuristic given in the text above.
from queue import Queue, PriorityQueue
graph = {
    'Arad': ['Zerind', 'Timisoara','Sibiu'],
    'Zerind': ['Arad', 'Oradea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Sibiu': ['Oradea','Arad','Fagaras','Rimincu_Vilcea'],
    'Oradea': ['Zerind','Sibiu'],
    'Lugoj': ['Timisoara','Mehadia'],
    'Fagaras':['Sibiu','Bucharest'],
    'Rimincu_Vilcea':['Sibiu','Pitesti','Craiova'],
    'Mehadia':['Lugoj','Dobreta'],
    'Bucharest':['Fagaras','Pitesti','Urziceni','Giurgia'],
    'Pitesti':['Rimincu_Vilcea','Craiova','Bucharest'],
    'Craiova':['Pitesti','Rimincu_Vilcea','Dobreta'],
    'Dobreta':['Mehadia','Craiova'],
    'Urziceni':['Hirsova','Bucharest','Vaslui'],
    'Giurgia':['Bucharest'],
    'Hirsova':['Eforle','Urziceni'],
    'Vaslui':['Lasi','Urziceni'],
    'Eforle':['Hirsova'],
    'Lasi':['Neamt','Vaslui'],
    'Neamt':['Lasi']
}

cost = {
    ('Arad', 'Zerind'): 75,  # tuple
    ('Arad', 'Timisoara'): 118,
    ('Arad','Sibiu'):140,

    ('Zerind', 'Arad'): 75,
    ('Zerind', 'Oradea'): 71,

    ('Timisoara', 'Arad'): 118,
    ('Timisoara', 'Lugoj'): 111,

    ('Oradea', 'Zerind'): 71,
    ('Oradea', 'Sibiu'): 151,

    ('Lugoj', 'Timisoara'): 111,
    ('Lugoj', 'Mehadia'): 70,

    ('Sibiu', 'Arad'): 140,
    ('Sibiu', 'Fagaras'): 99,
    ('Sibiu', 'Oradea'): 151,
    ('Sibiu', 'Rimincu_Vilcea'): 80,

    ('Mehadia', 'Lugoj'): 70,
    ('Mehadia', 'Dobreta'): 75,

    ('Fagaras', 'Sibiu'): 99,
    ('Fagaras', 'Bucharest'): 211,

    ('Rimincu_Vilcea', 'Sibiu'): 80,
    ('Rimincu_Vilcea', 'Pitesti'): 97,
    ('Rimincu_Vilcea', 'Craiova'): 146,

    ('Dobreta', 'Mehadia'): 75,
    ('Dobreta', 'Craiova'): 120,

    ('Bucharest', 'Pitesti'): 101,
    ('Bucharest', 'Fagaras'): 211,
    ('Bucharest', 'Giurgia'): 90,
    ('Bucharest', 'Urziceni'): 85,

    ('Pitesti', 'Bucharest'): 101,
    ('Pitesti', 'Craiova'): 138,
    ('Pitesti', 'Rimincu_Vilcea'): 97,

    ('Craiova', 'Rimincu_Vilcea'): 146,
    ('Craiova', 'Pitesti'): 138,
    ('Craiova', 'Dobreta'): 120,

    ('Giurgia', 'Bucharest'): 90,

    ('Urziceni', 'Bucharest'): 85,
    ('Urziceni', 'Hirsova'): 98,
    ('Urziceni', 'Vaslui'): 142,

    ('Hirsova', 'Eforle'): 86,
    ('Hirsova', 'Urziceni'): 98,

    ('Vaslui', 'Urziceni'): 142,
    ('Vaslui', 'Lasi'): 92,

    ('Eforle', 'Hirsova'): 86,

    ('Lasi', 'Neamt'): 87,
    ('Lasi', 'Vaslui'): 92,

    ('Neamt', 'Lasi'): 87
}
heur={
    'Arad':366,
    'Bucharest':0,
    'Craiova':160,
    'Dobreta':242,
    'Eforle':161,
    'Fagaras':176,
    'Giurgia':77,
    'Hirsova':151,
    'Lasi':226,
    'Lugoj':244,
    'Mehadia':241,
    'Neamt':234,
    'Oradea':380,
    'Pitesti':10,
    'Rimincu_Vilcea':193,
    'Sibiu':253,
    'Timisoara':329,
    'Urziceni':80,
    'Vaslui':199,
    'Zerind':374
}

def aStar_Cost(from_node, to_node, cost=None):
    return cost.get((from_node, to_node), 10e100)  # func. for getting the cost (Reference:Python book)


def aStar(graph, heur,start, goal, cost=None):
    fringe = PriorityQueue()  # setting my fringe as a priority queue
    fringe.put((0, start))  # (cost, node)  #giving zero cost to the root node
    explored = []  # for explored node

    while fringe:
        astarC, current_node = fringe.get() #starting cost,start state
        explored.append(current_node) #appending in explored queue to keep the track of explored node

        if current_node == goal:  # goal test
            return explored

        for leaves in graph[current_node]:  # generate child
            if leaves not in explored:  # always check the node, beacuse we dont explored the node again in Astar
                h_value=heur[leaves]
                fringe.put((astarC +h_value+ aStar_Cost(current_node, leaves, cost), leaves))


print(aStar(graph, heur,'Arad', 'Bucharest', cost))