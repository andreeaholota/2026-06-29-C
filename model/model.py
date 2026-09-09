import networkx as nx
from database.DAO import DAO
from itertools import combinations

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    def creaGrafo(self):
        self._graph.clear()
        self._idMap.clear()

        vertici = DAO.getAllArtists()
        for artist in vertici:
            artist.listBrani = DAO.getAllTracks(artist.id)
            artist.setPlaylist = DAO.getAllPlaylists(artist.id)

            self._idMap[artist.id] = artist
        self._graph.add_nodes_from(vertici)

        for a1, a2 in combinations(vertici, 2):
            comuni = a1.setPlaylist & a2.setPlaylist
            if comuni:
                self._graph.add_edge(a1, a2, weight=len(comuni))

    def getNumberNodes(self):
        return self._graph.number_of_nodes()

    def getNumberEdges(self):
        return self._graph.number_of_edges()

    def getGradoMassimo(self):
        return max(self._graph.degree(), key=lambda x:x[1])

    def getSommaPesiMax(self):
        somme = {n:sum(d["weight"] for _,_,d in self._graph.edges(n, data=True)) for n in self._graph.nodes()}
        return max(somme.items(), key=lambda x: x[1])

    def getSortedEdges(self):
        edges = list(self._graph.edges(data=True))
        edges.sort(key=lambda e: (-e[2]["weight"], e[0].name, e[1].name))
        return edges[:10]



