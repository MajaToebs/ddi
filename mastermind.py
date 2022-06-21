# Modul einbinden, das für zufällige Auswahl nötig ist
import random

# eine Liste mit den vier möglichen Farben wird festgelegt
farben = ["r","g","o","b"]

# Funktion, die berechnet, wie viele Steckplätze richtig in Position und Farbe sind (s) und wie viele Farben außerdem richtig sind, aber in der falschen Position stehen
def farbe_pos_richtig(v, m):
	s = 0
	w = 0
	# Index, um über das Muster zu gehen
	i = 0
	while i < len(m):
		# wenn Versuch und Muster an der Stelle dasselbe Zeichen haben, wird 2 erhöht und das Zeichen gelöscht
		if v[i] == m[i]:
			s += 1
			# entferne den richtigen Buchstaben lokal aus den beiden Zeichenketten, damit er nicht mehr für w mitgezählt wird
			m = m[0 : i : ] + m[i + 1 : :]
			v = v[0 : i : ] + v[i + 1 : :]
		# nur wenn gerade kein Zeichen gelöscht wurde, muss der Index inkrementiert werden
		else:
			i += 1
	for farbe in farben:
		# zähle für das Muster und den Versuch die Häufigkeit der Farbe
		echte_anzahl = m.count(farbe)
		vermutete_anzahl = v.count(farbe)
		if vermutete_anzahl > 0:
			# wenn die Farbe häufiger vorkommt als vermutet, zählt die vermutete Anzahl zu w
			if echte_anzahl >= vermutete_anzahl:
				w += vermutete_anzahl
			# wenn die Farbe seltener vorkommt als vermutet, zählt die echte Anzahl zu w
			else:
				w += echte_anzahl
	return s, w



print("Willkommen zu Mastermind!\nDu wirst gleich gegen den Computer spielen. Es gibt vier Farben (r = rot, g = gelb, o = orange, b = blau), vier Steckplätze und du hast maximal 12 Versuche frei, um das Muster zu erraten.\nWenn du im Spiel abbrechen möchtest, gib qqqq ein!")

muster = ""

# Computer legt das Muster randomisiert fest
for i in range(0,4):
	muster += farben[random.randint(0,3)]
	
#löschen
print("geheimes Muster: " + muster)

# Variable iniitieren, die anzeigt, ob das Muster erraten wurde
richtig = False
# Variable initiieren, die die Runden zählt
runde = 0

# solange das Muster noch nicht erraten wurde und die 12. Runde noch nicht gespielt wurde
while not(richtig) and runde < 12:
	runde += 1
	print("\nRunde " + str(runde) + " beginnt...")
	versuch = ""
	while len(versuch) != 4:
		# Abspeichern der Nutzereingabe. Wir ignorieren mögliche Fehler des Nutzers falsche Buchstaben oder Zahlen einzugeben
		versuch = input("Bitte gib ein Muster mit vier Zeichen (nur r, g, o, b) ein! ")
		# wenn die Nutzerin qqqq eingibt, gibt sie auf
		if versuch == "qqqq":
			print("Spiel absichtlich beendet.")
			quit()
	# wenn richtig getippt wurde, wird die solange-Schleife verlassen
	if versuch == muster:
		richtig = True
	# ansonsten werden s und w berechnet und ausgegeben, damit die Nutzerin daraus lernen kann
	else:
		schwarz, weiß = farbe_pos_richtig(versuch, muster)
		print("Steckplätze mit richtiger Farbe und richtiger Position: " + str(schwarz) + "\nSteckplätze mit richtiger Farbe, aber falscher Position: " + str(weiß))
		
# falls das Muster erraten wurde
if richtig:
	print("Super, du hast das Muster in " + str(runde) + " Runde(n) erraten.")
# falls das Muster nicht erraten wurde, aber die 12 Runden rum sind
else:
	print("Schade, diesmal hast du es nicht geschafft, in 12 Runden das richtige Muster zu erraten.\nDas richtige Muster war " + muster)
