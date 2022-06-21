# Funktion, die bestimmt, ob n eine Primzahl ist
def primzahl(n):
	# die 0 ist ein Ausnahmefall und wird daher gesondert behandelt
	if n == 0:
		return False
	else:
		# Variable zum Zählen der Teiler von n
		teiler = 0
		# Schleife, die alle Teiler von n zwischen 2 und n-1 zählt
		for j in range(2,n):
			if n % j == 0:
				teiler += 1
		# wenn keine Teiler gefunden wurden, n somit nur durch 1 und sich selbst teilbar ist, handelt es sich um eine Primzahl
		if teiler == 0:
			return True

# Funktion, die alle Primzahlen zwischen s und e (inklusiv) zurückgibt
# dabei wird vorausgesetzt, dass es sich bei s und e um positive ganze Zahlen handelt
def primzahlen(s, e):
	liste = []
	# wenn das Ende unter dem Anfang liegt, gibt es keine Primzahlen dazwischen
	if e < s:
		return liste
	# es wird für jede Zahl zwischen s und e geprüft, ob sie eine Primzahl ist
	else:
		for i in range(s, e+1):
			# wenn ja, wird die Zahl an die Rückgabeliste angehängt
			if primzahl(i):
				liste.append(i)		
		return liste

# Start- und Endwert abfragen und als Integer abspeichern
start = int(input("Bitte gib den Startwert ein! "))
ende = int(input("Bitte gib den Endwert ein! "))

# Primzahlen zwischen Start und Ende bestimmen und abspeichern
ergebnisliste = primzahlen(start, ende)

# Ergebnisse ausgeben (Primzahlen zwischen Start und Ende als Liste)
print(ergebnisliste)
