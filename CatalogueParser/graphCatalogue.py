import matplotlib.pyplot as plt
import networkx as nx
from CatalogueParser import CatalogueParser

uciCatalogue = CatalogueParser("catalog.txt")
uciCatalogue.parse()

# csCourses = [x for x in uciCatalogue.catalogue.keys() if "COMPSCI" == x.split()[0]]
csCourses = [x for x in uciCatalogue.catalogue.keys()]

courseGraph = nx.DiGraph()

for courseName in csCourses:
    course = uciCatalogue.catalogue[courseName]
    edges = zip([course.shortName for _ in course.getRequirementsList()], course.getRequirementsList())
    courseGraph.add_edges_from(edges)
node_labels = {}
for node in courseGraph:
    node_labels[node] = node

pos = nx.circular_layout(courseGraph)
nx.draw(courseGraph, pos)
nx.draw_networkx_labels(courseGraph, pos, labels=node_labels)

plt.show()
