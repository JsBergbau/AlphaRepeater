#!/bin/bash
echo "Wenn keine Daten ausgegeben werden, bitte prüfen, ob als root läuft und der AlphaReader eingeschaltet und in Empfangsreichweite ist"
hcitool lescan --duplicate > /dev/null &

#Setze den Namen richtig
hcitool -i hci0 cmd 0x08 0x0009 0c 0b 09 4d 49 34 30 31
sleep 0.1
#Starte mit dem Senden der Bluetooth LE Pakete
#Eigentlich müsste es der Typ leadv 3 sein, nicht verbindbar, aber aus unerklärlichen Gründen werden nach ein paar Sekunden keine Datenpakete mehr gesendet. Mit leadv 0 funktioniert es auch
hciconfig hci0 leadv 0
sleep 0.1
hcidump --raw hci | python3 repeater.py
#Stoppe das Senden der Bluetooth LE Pakete
hciconfig hci0 noleadv
echo Ende
