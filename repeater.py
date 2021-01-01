#!/usr/bin/python3
import re
import os
import fileinput
from collections import deque
import threading
import time
import signal
import sys


def signal_handler(sig, frame):
        os._exit(0)

KommandoWarteschlange=deque()

def thread_sendeDaten():
	while True:
		try:
			cmd=KommandoWarteschlange.popleft()
			#print(cmd)
			print("Repeating...")
			os.system(cmd)
		except IndexError:
			time.sleep(0.05)

def verarbeiteDatenpaket(datenpaket):
	#print(datenpaket)
	
	regex=re.compile("(>.*)[\r\n][ ](.*)")		
	datenpaket=regex.sub(r'\1\2',datenpaket)
	datenpaket=regex.sub(r'\1\2',datenpaket)
	datenpaket=re.sub(r'>|[ ]','',datenpaket)
	#Ab hier haben wir die Daten Zeile für Zeile
	
	datenpaket=datenpaket.rstrip()
	
	kommandofix="hcitool -i hci0 cmd 0x08 0x0008 1e "
	
	
	
	if re.match(r'[A-F0-9]{32}4D493430',datenpaket):#prüfen ob wir Daten eines Alpha Readers empfangen
		#print("ok")
		#print("Datenpaket:" + datenpaket)
		datenpaket=re.search(r'06084D49.*',datenpaket).group(0)
		datenpaket=re.sub(r'[A-F0-9]{2}$','',datenpaket) #Signalstärke entfernen
		datenpaket=re.sub(r'([0-9A-F]{2})',r'\1 ',datenpaket)
		kommando = kommandofix + datenpaket + " > /dev/null"
		KommandoWarteschlange.append(kommando)
		#print("Warteschlangenlänge: " + str(len(KommandoWarteschlange)))
		if(len(KommandoWarteschlange)>=5): #Vermeide, dass sich eine Verzögerung aufbaut
			KommandoWarteschlange.clear()
		#print(kommando)
		#os.system(kommando)

def main():
	signal.signal(signal.SIGINT, signal_handler)
	skip=0
	ersteZeile=True
	datenpaket=""
	thread = threading.Thread(target=thread_sendeDaten)
	thread.start()
	continued=False
	for line in fileinput.input():
		#Überspringe die ersten beiden Zeilen ohne sinnvolle Daten
		# HCI sniffer - Bluetooth packet analyzer ver 5.50
		# device: hci0 snap_len: 1500 filter: 0x2
		if(skip<2):
			skip += 1
			continue
		if ersteZeile:
			datenpaket+=line
			ersteZeile=False
			continue
		
		#Nach dieser Logik braucht es mindestens 2 DatenKommandoWarteschlange, da die Verarbeitung des ersten erst beginnt, wenn das nächste schon eintrifft. Hier unerheblich
		#Da die eigenen Änderungen/Pakete bei hcidump mit auftauchen, braucht es mehr Logik um diese zu filtern
		if(line[0]=='<'):
			continued=True
			continue
		if(continued==True and line[0]!='>'): #Glücklicherweise sind bisher nur 2 zeilige "<" Pakete aufgetaucht, ansonsten weiterer Check erforderlich
			continued=False
			continue
		if(line[0]=='>'):
			verarbeiteDatenpaket(datenpaket)
			datenpaket=line
			continued=False
		else:
			datenpaket+=line		
	
	
if __name__=="__main__":
	main()
