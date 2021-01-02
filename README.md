# AlphaRepeater
Nach dem AlphaDecoder https://github.com/JsBergbau/AlphaDecoder kommt jetzt ein AlphaRepeater

Reicht die Reichweite eines Grundfos Alpha Readers nicht aus, kann man sie mit einem weiteren Alpha Reader erhöhen. Nachdem diese nicht billig sind, zeigt diese Lösung, dass es auch deutlich günstiger geht. Diese Software einfach auf einem Raspberry PI Zero W ausführen und man hat einen Repeater für weniger als 20 €.

Der Code ist nur Proof of Concept und wurde nicht ausführlich getestet. Er ist ausdrücklich als Betaversion zu verstehen.
Hinweis: Die Reichweite des Alpha Readers ist bereits erstaunlich hoch. Ein Raspberry PI4 brachte leider kaum eine Reichweitenerhöhung. Im Vergleich zu einem Raspberry PI Zero W ist die Bluetooth Reichweite deutlich geringer (ausprobiert).

Es gelten dieselben Vorraussetzungen wie für den AlphaDecoder https://github.com/JsBergbau/AlphaDecoder

## Hydraulischer Abgleich mit Grundfos Alphapumpen auch ohne AlphaRepeater

Leider funktioniert dieser Repeater nicht für Grundfos Alpha 3 Pumpen. Sie verwenden ein anderes Datenformat. Aber man braucht dennoch keinen teuren AlphaReader als Repeater kaufen. Es gibt Software mit denen man das Handy fernsteueren kann. Das Handy verbleibt in der Nähe der Pumpe, während man mit dem Laptop auf dieses zugreift und von Heizkörper zu Heizkörper geht um den hydraulischen Abgleich durchzuführen. Es gibt verschiedene Softwarelösungen, einen Überblick gibt es z.B. hier https://www.gottabemobile.com/best-apps-to-control-any-android-device-from-your-pc/ 

Einen positiven Erfahrungsbericht für diesen Weg des hydraulischen Abgleichs findet sich hier https://github.com/JsBergbau/AlphaRepeater/issues/1#issuecomment-753525450

