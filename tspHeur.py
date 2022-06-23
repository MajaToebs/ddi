# heuristischer Ansatz mit nearest neighbour zum Finden einer optimalen Route, die alle Orte besucht und am selben Ort endet und anfängt
# Voraussetzung: gerichteter Graf mit Verbindungen zwischen allen Orten in einer csv-Datei

#import csv
import numpy 

with open("tsp_test_data.csv") as csv_file:
    data = numpy.loadtxt(csv_file, dtype='str', delimiter=',')

print("Folgende Daten wurden eingelesen: ")
print(data)

# für Entfernungsdaten die erste Zeile und Spalte löschen und den Rest von str in int konvertieren
dist = numpy.delete(data, 0, axis = 1)
dist = numpy.delete(dist, 0, axis = 0)
dist = dist.astype('int')
# mit n bestimmen wir die Anzahl der Orte
n = dist.shape[0]

# kürzesten Weg abspeichern
shortest_path = []

# jede Zeile (jeder Ort)  wird als Startort für nearest-neighbour ausprobiert
for i in range(dist.shape[0]):
    # Kopie erstellen, in der dokumentiert wird, welche Orte bereits besucht wurden
    unvisited_places = numpy.copy(dist)
    # Entferungssumme berechnen
    dist_sum = 0
    # Pfad abspeichern
    path = [i]
    # aktuellen Ort mit Index abspeichern
    current = i
    # Spalte vom Startort i 0en, damit sie erst als letzte besucht wird
    unvisited_places[:,i] = 0
    # solange nicht alle Orte besucht wurden, wird weitergegangen
    while not(numpy.all(unvisited_places[current,:] == 0)):
        # als nächster Punkt wird der Nachbar mit der niedrigsten Entfernung gewählt, seine Entfernung (nearest) und sein Index bestimmt
        nearest = numpy.min(unvisited_places[current,:][numpy.nonzero(unvisited_places[current,:])])
        next_ind = numpy.where(unvisited_places[current,:] == nearest)[0][0]
        # an den Pfad wird der Ort angehängt
        path.append(next_ind)
        # zur zurückgelegten Strecke wird die Distanz zum Nachbarn dazugerechnet
        dist_sum += nearest
        # damit klar ist, dass von diesem Ort nirgendwohin mehr gegangen werden kann, setzen wir die Zeile auf 0
        unvisited_places[current,:] = 0
        # damit der Nachfolger nicht mehr besucht wird, setzen wir seine Spalte auf 0
        unvisited_places[:,next_ind] = 0
        # damit weitergegangen werden kann, muss current auf next gesetzt werden
        current = next_ind
    # zuletzt muss wieder zum Anfangspunkt gegangen werden und auch diese Entfernung hinzuaddiert werden
    dist_sum += dist[path[-1],i]
    # dann muss der Ort noch dem Pfad angehängt werrden
    path.append(i)

    # beim ersten Versuch und wenn ein kürzerer Pfad gefunden wurde, wird der Pad mit Entfernung abgespeichert
    if len(shortest_path) == 0 or dist_sum < shortest_path[0]:
        shortest_path = [dist_sum, path]

# nachdem alle Orte als Anfangsorte mit den nearest-neighbour-Prinzip ausprobiert wurden, wird der kürzeste Pfad mit Entfernung ausgegeben
print("Der kürzeste Weg ist: ")
# der kürzeste Pfad wird übersetzt in eine Liste von Städten statt Indizes
shortest_connection = []
for i in range(len(shortest_path[1])):
    shortest_connection.append(data[1+shortest_path[1][i],0])
print(shortest_connection)
print("Die zurückgelegte Entfernung beträgt dabei " + str(shortest_path[0]) + " km.")
