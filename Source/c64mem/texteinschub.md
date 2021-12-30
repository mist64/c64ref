# Texteinschub Nr. 1: Der USR-Befehl

Hand aufs Herz: Haben Sie USR schon einmal benutzt? Ohne Zweifel gehört dieser Befehl zu den seltenen. Ich will ihn daher hier kurz erläutern. USR hat dieselbe Funktion wie SYS, nämlich aus einem Basic-Programm direkt in ein Maschinenprogramm zu springen und dort solange weiterzufahren, bis mit dem Befehl RTS (entspricht dem Basic-Befehl RETURN) in das Basic-Programm zurückgesprungen wird. Die Sprungadresse in das Maschinenprogramm steht bei SYS gleich hinter dem Befehl.

Bei USR muß die Adresse zuerst in die Speicherzellen 1 und 2 (aha!!) gePOKEt werden.

Beispiel - Sprung auf 56524 ($DCCC):

* mit SYS: `SYS 56524`
* mit USR: `POKE 1,204:P0KE 2,220:X=USR(Y)`

Kein Wunder, daß USR selten benutzt wird. Aber erstens ist er durch das POKEn der Low-/High-Byte-Darstellung aufgebläht und zweitens hat er auch wesentlich mehr Fähigkeiten als SYS.

Sein Argument, im obigen Beispiel also das »Y«, wird nämlich zuerst in den »Fließkomma-Akkumulator« FAC 1 (Floating Point Accumulator Nr. 1) gebracht, der sich in den Speicherzellen 97 bis 102 ($61 bis $66) befindet. Da wir ihn auf unserer Reise durch den Speicher noch treffen werden, brauche ich jetzt nicht näher darauf einzugehen. Wichtig ist lediglich, daß der Wert von »Y« dann vom angesprungenen Maschinenprogramm verarbeitet werden kann. Das Resultat kommt dann wieder in diesen FAC 1 und steht als Wert von X (siehe Beispiel oben) dem Basic- Programm zur Verfügung.

Mit USR kann man also Variable ins Maschinenprogramm zur Bearbeitung und zurück transferieren - und das ist der Unterschied zum SYS-Befehl. Ich möchte das an einem kleinen Beispiel demonstrieren. Statt allerdings ein Maschinenprogramm selbst zu schreiben, verwende ich beziehungsweise springe ich auf eine Routine des Betriebssystems, welches Werte des FAC 1 für mathematische Operationen verwendet.

Als mathematische Operation wähle ich das eingebaute Programm für INT, welches im VC 20 ab Speicherzelle 56524 ($DCCC) steht, im C 64 steht es ab 48332 ($BCCC). Dieses wollen wir verwenden:

In Zeile 10 definieren wir einen Wert für die Variable X, der in das Maschinenprogramm gebracht werden soll. Mit Zeile 20 bringen wir die Startadresse des Maschinenprogramms in die Speicherzellen 1 und 2.

Laut Kochrezept teilen wir die Adresse 56524 auf in ein Low- Byte = 204 und ein High-Byte = 220.

Der Befehl in Zeile 30 löst den ganzen USR-Vorgang aus, Zeile 40 gibt uns das Resultat.

    10 Y=14.35
    20 POKE l,204:P0KE 2,220 30 X=USR(Y)
    40 PRINT X

Hinweis: Entsprechend der anderen Adresse 48332 lautet die Zeile 20 beim C 64:

    20 POKE 785,204:POKE 786,188

Nach RUN erhalten wirdas Resultat 14, wie das Gesetz für INT es befiehlt. Natürlich hätten wir gleich PRINT INT (14.35) schreiben können, aber ich wollte ja nur demonstrieren. Der eigentliche Wert des USR-Befehls kommt hauptsächlich bei selbstgeschriebenen Maschinenprogrammen zum Zuge.

Sie können zur Übung im obigen Programm statt INT auch COS verwenden, indem Sie auf die Adresse 57935 ($E261) beziehungsweise beim C 64 auf 57938 ($E264) springen. Der Vergleich mit dem Basic-Befehl COS muß dasselbe Resultat ergeben.

Wer hat gemerkt, daß wir überhaupt nichts mit der Speicherzelle 0 gemacht haben, obwohl sie doch beim USR angeblich beteiligt ist?

Sie ist es wirklich, doch ohne unser Zutun. In diese Adresse wird beim Einschalten des Computers die Zahl 76 ($4C) geschrieben. Das ist der Code für den Maschinenbefehl »JMP«, der soviel bedeutet wie GOTO. Bei USR springt nämlich das Programm auf die Speicherzelle 0, findet dort den Sprungbefehl und in den nachfolgenden Zellen 1 und 2 die Sprungadresse - und führt den Sprung auch gleich aus.

# Texteinschub Nr. 2: Die Low-/High-Byte-Darstellung

Eine Speicherzelle der kleinen Commodore-Computer VC 20 und C 64 hat eine Länge von 8 Bit = 1 Byte. Mit diesen 8 Bit können Zahlen von 0 bis 255 ($00FF) dargestellt werden. Zur Darstellung von Zahlen über 255 verwenden wir die Low-/High- Byte-Methode.

Wir hängen einfach zwei Speicherzellen zusammen, mit deren 16 Bit wir Zahlen bis maximal 65535 ($FFFF) darstellen können. Die maximale Zahl 65535 ist übrigens auch die höchste Adresse des gesamten Speichers - was natürlich kein Zufall ist.

Ich will Ihnen jetzt zeigen, wie eine Dezimalzahl auf zwei 8-Bit- Speicherzellen verteilt wird, und umgekehrt, wie aus 2 Byte eine Dezimalzahl gebildet wird.

Schauen Sie sich das folgende Beispiel an:

    DEZIMAL               47491
    DUALZAHL    1011 | 1001 | 1000 | 0011
    HEX $         B  |   9  |   8  |   3
    HIGH-BYTE       185     |      -       
    LOW-BYTE         -      |     131

Wir gehen von der Dezimalzahl 47491 aus. Ihre duale Darstellung mit 16 Bit - 1011100110000011 - teilen wir einfach in der Mitte und erhalten damit zwei neue Dual-Zahlen mit je 8 Bit = 1 Byte. Das linke Byte nennen wir »High-Byte«, da es den höheren Teil derGesamtzahl darstellt. Das rechte Byte heißt entsprechend »Low-Byte«.

Jedes der beiden Bytes kann für sich allein in einer Speicherzelle untergebracht werden, in der natürlich dann der dezimale Wert des Bytes steht.

In der Tabelle habe ich zur Vollständigkeit noch die hexadezimalen Werte eingefügt, die sehr schön zeigen, daß der Vorteil dieserZahlendarstellung darin liegt, daß jede Einzelziffer der 4-Bit-Dualzahl entspricht, genau so wie jede Zweiergruppe dem Byte (sowohl in Dual-, als auch in Dezimaldarstellung) und die vierstellige Zahl der großen Dezimal- und Dualzahl entspricht.

Zur Umrechnung der Low-/High-Bytes empfehle Ich folgende Kochrezepte:

## Dezimal in Low-/High-Byte

    47491:256 = 185 (High-Byte), Rest 131 (Low-Byte)

Der Rest fällt bei der Division per Hand automatisch an. Mit dem (Taschen-)Rechner erhält man den Rest durch:

    185*256-47491 = -131

## Low-/High-Byte in Dezimal

    High-Byte * 256 + Low Byte = Dezimal
    185       * 256 + 131      = 47491

Wichtige Regel: Die Mikroprozessoren von VC 20 und C64 verlangen, daß immer das Low-Byte vor dem High-Byte kommen muß. Die Zahl wird sozusagen von rechts nach links gelesen (131/185).

# Texteinschub Nr. 3: Manipuliertes Basic
Wie Sie durch PRINT PEEK (1) selbst leicht feststellen, steht nach dem Einschalten des Computers im Register 1 die Zahl 55. In dualer Darstellung ist das 110111. Das entspricht dem in der ersten Zeile derTabelle 2 dargestellten »Normalzustand« der einzelnen Bits.

Vergleichen Sie es bitte mit der Auflistung am Anfang der Beschreibung der Speicherzelle 1. Die in Tabelle 2 dargestellten Bits sind also die rechten drei Bits der Zelle 1.

Lassen wir die Bits 3, 4 und 5 unverändert, ergeben die acht Kombinationen der Tabelle 2 die Zahlen 55 bis 48. Durch den Befehl POKE 1,54 können wir nun den Basic-Übersetzer aus- schalten und 8 KByte Speicher gewinnen. Nur nutzt uns das nicht viel, denn was tun - ohne Basic! Es gibt aber doch eine Anwendung. Zuvor will ich Ihnen aber noch beweisen, daß wir tatsächlich den Block A auf RAM umschalten. Der Trick besteht darin, den Basic-Übersetzer vom ROM in den darunter liegenden RAM umzuladen. Wenn er tatsächlich in RAM steht, müßten wir ihn durch POKEn verändern können zu einem Privat-Basic. Geben Sie direkt ein:

    FOR J=40960 TO 49151: POKE J,PEEK(J): NEXT J

POKE J, PEEK (J) - das sieht dümmer aus als es ist. Die »Doppeldecker-Speicher« erlauben nämlich ein PEEKen nur aus dem ROM-Bereich. Ein hineinPOKEn dagegen geht nur in den RAM-Teil. Von dort aber kann er - wie gerade gesagt - nicht herausgelesen werden, es sei denn, wir schalten um!

Merken Sie was? Die Zeile oben liest also den Inhalt des Basic- ROMs und schreibt ihn in den RAM mit identischen Adressen. Die Ausführung der Zeile braucht einige Zeit. Wenn der Cursor wieder blinkt, schalten wir das RAM ein mit:

    POKE 1,54

Wir merken natürlich noch keinen Unterschied, denn das RAM-Basic ist ja noch dasselbe.

Doch nun werden wir es verändern. In der Speicherzelle 41220 steht das »P« für den Befehl PRINT mit dem ASCII-Codewert 80. Dieses P ersetzen wir durch ein »G« (ASCII-Code = 71).

    POKE41220,71

Versuchen Sie bitte, mit dem (nicht durch »?« abgekürzten) PRINT-Befehl ein Zeichen auf den Bildschirm zu drucken. Es wird Ihnen nicht gelingen, denn der Befehl heißt jetzt:

    GRINT "A"

was beweist, daß das Basic jetzt im RAM steht. Das Umdefinieren von Befehlen Ist natürlich wenig sinnvoll. Aber wer die Maschinenprogramme des Basic kennt, kann sie auf diese Weise ändern, erweitern, einschränken, solange er sich auf in sich geschlossene Teile beschränkt.

Eine inzwischen oft zitierte Anwendung stammt von Jim Butterfield, den es begreiflicherweise stört, daß der Befehl ASC, welcher den ASCII-Code eines Strings erzeugt, bei einem Null- String das Programm mit ILLEGAL QUANTITY ERROR beendet. Versuchen Sie es:

`PRINT ASC ("A")` ergibt die Zahl 65.

`PRINT ASC (" ")` hat die obige Fehlermeldung zur Folge.

Wenn Basic im RAM steht, können wir das ändern:

    POKE 46991,5

Die Wiederholung des Befehls PRINT ASC (””) ergibt jetzt 0 - und, was das Wichtige ist, das Programm läuft weiter.

Durch zusätzliches Umladen des Speicherblocks E und anschließendes Umschalten mit POKE 1,53 ist auch das Betriebssystem veränderbar - ein weites Feld für fortgeschrittene Programmierer in Maschinensprache.

Die wohl wichtigste Anwendung der Umschaltmethode wird den Maschinen-Programmierern geboten, die dadurch eine kostenlose Speichererweiterung von 16 KByte erhalten. Bei gleichzeitiger Verwendung von Basic und Maschinenprogramm kann die Umschaltung besonders vorteilhaft eingesetzt werden. Das Umschaltprogramm muß dann aber ebenfalls in Maschinensprache geschrieben sein und darf nicht im Umschaltbereich liegen.

Das Umschalten von den Ein-/Ausgabe-Registern des Blocks D mit POKE 1,51 erlaubt, die Bitmuster der fest programmierten Zeichen aus dem Zeichen-ROM auszulesen, in einen freien RAM-Bereich zu bringen und dort dann nach eigenen Vorstellungen zu verändern.


# Texteinschub Nr. 4: Zeiger, Vektoren und Flaggen

Zeiger und Vektoren sind Zahlenwerte, die jeweils in zwei benachbarten Speicherzellen stehen und in der Low-/High-Byte-Darstellung eine Adresse bilden.

Wir sprechen von einem »Zeiger«, wenn diese Adresse den Beginn von gespeicherten Daten angibt.

Ein »Vektor« zeigt ebenfalls auf eine Anfangsadresse, allerdings auf die eines Maschinenprogramms. Diese Unterscheidung wird leider nicht immer ganz eindeutig angewendet.

Eine »Flagge« besteht aus einem Zahlenwert in einer Speicherzelle, die von einem Programm dort abgelegt wird, um sich das Resultat einer Operation zu merken, beziehungsweise um es für eine spätere Verwendung bereitzuhalten.


# Texteinschub Nr. 5: Die Zahlendarstellung bei den Commodore-Computern

## Gleitkomma-Zahlen

Für diejenigen Leser, die das Thema der Zahlendarstellung in den Commodore-Handbüchern großzügig übersprungen haben, stelle ich es hier noch einmal vor.

Sie kennen die gängigen vier Zahlentypen:

* ganze Zahlen: 15, 21, 244
* Brüche; 2/3, 26/8, 15/14
* negative Zahlen: -15, -255
* positive Zahlen: 10, 5, 123

Ganze Zahlen bereiten uns und dem Computer keine Probleme.

Bei Brüchen sieht es schon anders aus. Erinnern Sie sich an
die Bruchrechnungsstunden in der Schule? Wieviel ist 51/52 + 3/4!!!

Ohne lange zu überlegen, rechnen wir natürlich um, 51/52 = 0,9807692 und 3/4 = 0,75; addiert ist das Resultat 1,7307692 - und schon sind Sie mitten in den Gleitkomma-Zahlen.

Bei obigem Beispiel gleitet allerdings noch nichts. Bei sehr großen oder aber auch sehr kleinen Bruch-Zahlen reicht uns - und einem Computer - nicht der Platz, um sie darzustellen. Die Zahl 0,000000000000000123 sprengt jeden normalen Rahmen.

Daher schreiben wir sie anders. Wir lassen das Komma nach rechts gleiten, bis es die erste Ziffer, die von 0 verschieden ist, findet und für jede Null, die es passiert, multiplizieren wir die Zahl mit 10.

Die Zahl oben sieht dann so aus: 0,123 x 10 hoch 15 (eine 1 mit 15 Nullen).

Die Grundzahl vorn heißt »Mantisse«, die 10 mit Hochzahl heißt »Exponent«.

Alle Commodore-Computer verarbeiten intern alle Zahlen in dieser Darstellung, also als Gleitkommazahl.


# Texteinschub Nr. 6: Was ist ein Stapelspeicher (Stack)?

Der normale Arbeitsspeicher des Computers, auf englisch »Random Access Memory« oder kurz RAM genannt, hat für jede Speicherzelle eine eigene Adresse, die beim Schreiben in den Speicher oder beim Lesen aus dem Speicher angegeben werden muß.

Als Analogie möge eine Aktenablage dienen, bei der jeder Akt (Brief, Papier, Zeichnung) in einen Ordner kommt, mit Nummer versehen.

Um einen Akt herauszuholen, muß man die Nummer (Adresse) kennen, unter der er abgelegt ist.

Ein Stapelspeicher, auf englisch »Stack« genannt, funktioniert wie eine Aktenablage, bel der jeder Akt einfach oben auf einen Stapel gelegt wird, daher der Name. Diese Ablage erfolgt ohne Kennzeichnung oder Nummer, einfach immer der Reihe nach.

Einen Akt kann man aus einem Stapelspeicher nicht beliebig herausholen, da immer nur der oberste Akt zugänglich ist.

Die Methode der Stapelspeicher bietet sich überall dort an, wo es auf die Reihenfolge der gespeicherten Daten ankommt. Basic merkt sich zum Beispiel der Reihe nach die Adressen, von denen aus mit GOSUB ein Unterprogramm angesprungen wird. Wenn mehrere GOSUBs hintereinander eingesetzt werden, liegt auf dem Stapel Immer die letzte Absprungadresse bereit zum Rücksprung.

Ein Stapelspeicher hat demnach nur eine einzige Adresse, die sowohl zum Abspeichern als auch zum Auslesen dieselbe Ist.

Voraussetzung eines Stapelspeichers ist natürlich eine Routine, welche alle gespeicherten Daten im Stapelspeicher um einen Platz weiterschiebt, wenn eine neue Information »oben auf den Stapel gelegt wird«.

Das Basic der Commodore-Computer verwendet mehrere dieser Stapelspeicher.
Die Programmiersprache Forth ist völlig auf dem Prinzip des Stapelspeichers aufgebaut.


# Texteinschub Nr. 7: Der sichtbare Basic-Speicher

Wenn wir den Variablen A die Adresse des Speicherbeginns der Basic-Programme zuordnen und dann mit einer FOR..NEXT- Schleife den Inhalt dieser und der nächsten 100 Speicherplätze ausdrucken, sehen wir in dezimaler Darstellung die ersten 101 Zahlenwerte, mit denen der Computer ein Basic-Programm speichert.

Ein Verbiegen des Zeigers in Speicherzelle 43/44 kann auf diese Weise in seiner Wirkung sichtbar gemacht werden.

Als Demo-Programm wähle ich zwei Zeilen, welche die Zahlen 1 bis 9 und die Buchstaben A bis I ausdrucken.

    10 PRINT "123456789"
    20 PRINT "ABCDEFGHI"
    100 A=2049 : REM*C 64
          4097 : REM*VC 20 ohne Erweiterung
          1025 : REM*VC 20 mit 3 KByte
          4609 : REM*VC 20 mit 8 KByte oder mehr
    110 PRINT CHR$(l47)

Zeile 100 definiert den Speicheranfang. Zeile 110 löscht den Bildschirm.

    120 FOR J=A T0 A+100
    130 PRINT PEEK (J);
    140 NEXT J

Die Befehle in den Zeilen 120 bis 140 drucken den Inhalt der ersten 101 Zellen dieses Basic-Programms aus. SAVEn Sie bitte dieses kleine Programm, denn wir brauchen es noch einmal. Dann geht es los mit RUN. In Bild 3 ist der Bildschirm-Ausdruck des VC 20 mit 8 KByte dargestellt, der des C 64 zeigt praktisch dieselbe Information.
Überspringen Sie bitte zunächst die ersten beiden Zahlen. Die dritte und vierte Zahl ist 10 und 0. Das ist (als Low- und High- Byte) die Nummer der ersten Zeile des Basic-Programms. Dann folgt 153, das ist der interne Codewert für PRINT. Diese Codes für alle Basic-Befehlswörter heißen »TOKEN«, sie sind im Texteinschub Nr. 32 angegeben.

Die nächste Zahl auf dem Bildschirm ist die 34, sie ist der ASCII*Code für den Gänsefuß. Danach folgen in aufsteigender Reihenfolge die ASCII-Codes der Ziffern 1 (48) bis 9 (57). Danach sehen Sie wieder den Gänsefuß (34). Schließlich kommt eine Null als Abstandszeichen zur nächsten Basic-Zeile.

Machen Sie bitte folgendes Experiment: Ausgehend von der Adresse der ersten auf dem Bildschirm ausgedruckten Speicherzellen - zum Beispiel 4609 beim VC 20 mit 8 KByte - zählen Sie die Zellen weiter bis zur Abgrenzungs-Null. In meinem Beispiel steht die Null in Zeile 4625. Das heißt, daß die nächste Basic-Zeile in 4626 anfängt. Und das ist genau die Zahl, die in den ersten beiden Zellen steht, die wir vorhin übersprungen haben; in meinem Beispiel steht da 18 18. Machen wir die Probe: 18 + 256 * 18 = 4626.

Jede Basic-Zeile im Speicher beginnt also mit der Adresse der nächsten Zeile (sie heißt Koppeladresse) und endet mit einer Null.

Ab 4626 folgt dann die nächste Koppeladresse, danach mit 20 0 die Zeilennummer, und Sie erkennen jetzt sicher die Codes der Angaben von Zeile 20 wieder.

So, jetzt wollen wir den Zeiger in 43 und 44 verbiegen. Ich schlage vor, daß wir den Basic-Beginn um zehn Adressen höher schieben. Sie müssen jetzt die in Zeile 100 oben verwendete Zahl für A in die High-/Low-Byte-Darstellung umrechnen und das Low-Byte um 10 erhöhen. Dieses Zahlenpaar POKEn wir in die Zellen 43 und 44. Vorher müssen wir aber noch in Zelle (A + 10) -1 eine Abstands-Null POKEn.

Wir geben diese Befehlssequenz im Direktmodus ein:

* für den C 64:

        POKE 2058,0:POKE 43,11:POKE 44,8:NEW

* für den VC 20 (GV):

        POKE 5006,0:P0KE 43,143:POKE 44,19:NEW

* für den VC 20 (= 3 KByte):

        POKE 1034,0:P0KE 43,11:POKE 44,4:NEW

* für den VC 20(> 8KByte)

        POKE 4618,0:P0KE 43,H:POKE 44,18: NEW

Jetzt ist der Anfang des Basic-Speichers versetzt. Um das zu prüfen, geben wir das kleine Programm von oben nochmal ein und lassen es mit RUN laufen. Der resultierende Bildschirmausdruck ist in Bild 4 dargestellt.

Die ersten Zahlen sind genauso wie vorher. Es sind auch die Reste von vorher, da wir den Speicher nicht auf Null gesetzt haben. Aber zählen Sie bitte die ersten zehn Adressen hoch. Da finden Sie unser Programm von vorhin genau wieder, beginnend mit der Abstands-Null. Aber Vorsicht, lassen Sie sich nicht verwirren, denn die Koppeladressen sind natürlich jetzt auch jeweils um 10 höher. Aber hinter den Koppeladressen finden wir wieder unser Programm, in gleicher Weise dargestellt wie beim ersten Mal. Da der Zeiger in 43 und 44 von allen entsprechenden Routinen des Übersetzers und des Betriebssystems abgefragt wird, läuft ein verschobenes Programm fehlerfrei, solange natürlich der Zeiger nicht wieder verändert wird.


# Texteinschub Nr. 8: Normale Variable in Basic

Alle Daten, die in einem Basic-Programm nicht in Form von READ-DATA-Anweisungen vorkommen, werden als »Variable« unmittelbar nach dem Basic-Programm abgespeichert. Wir unterscheiden dabei zwei Typen:

* normale Variable
* Felder (Arrays)

Wir betrachten hier nur die »normalen« Variablen.

Sie erscheinen in dem Speicherbereich, dessen Beginn durch den Zeiger in den Zellen 45 und 46 und dessen Ende durch den Zeiger in 47 und 48 angegeben wird, in derselben Reihenfolge, in welcher sie während des Ablaufes des Basic-Programms auf- treten. Wenn Basic dann auf eine der bereits definierten (und abgespeicherten) Variablen zurückgreifen soll, muß es den gesamten Variablenbereich von Anfang an absuchen, bis es den Namen der gesuchten Variablen gefunden hat. Wenn diese Variable ganz am Ende des Bereiches steht, kann dieser Suchprozeß recht lange dauern.

## Regel 1:

Häufig vorkommende Variable sollen am Anfang des Variablenbereichs stehen. Das wird dadurch erreicht, daß sie als erste Variable in einem Programm »definiert« werden. Falls sie erst später im Programm gebraucht werden (aber dann häufig), werden sie trotzdem am Anfang des Programms angegeben, notfalls mit einem beliebigen Wert, der später dann keine Rolle mehr spielt und ersetzt wird. Man nennt das einen »Dummy«-Wert.

Die Felder-Variablen stehen direkt nach den »normalen« Variablen. Auch hier kann der gewiefte Programmierer Gutes tun. Wenn nämlich nach einer Definition eines Feldes später im Programm noch normale Variable dazukommen, ist natürlich zuerst kein Platz für sie da. Das Betriebssystem des Computers muß erst alle Felder-Variablen weiterschieben, bevor die Neuankömmlinge in dem dadurch erweiterten Variablenbereich gespeichert werden können. Auch das kostet unnötig viel Zeit.

## Regel 2:

Alle normalen Variablen sollen als erste in einem Programm definiert werden. Wer also drauflos programmiert, sollte zumindest am Ende das Programm so umbauen, daß diese simple Regel erfüllt wird.


# Texteinschub Nr. 9: Darstellung der normalen Variablen im Speicher

Die normalen Variablen kommen in drei Arten vor:

* ganzzahlige Variablen
* Gleitkomma-Variablen
* String-Variablen (Zeichenketten)

Der Unterschied zwischen den drei Typen ist in den Commodore-Handbüchern gut erklärt, und ich verzichte hier auf eine Wiederholung. Ich will vielmehr direkt zeigen, wie die Variablen im Speicher abgelegt sind.

Wir können den Speicher direkt sichtbar machen.

Einmal geht das in Maschinencode mittels eines Monitors beziehungsweise Disassemblers.

Zum anderen aber geht das auch in Basic und zwar mit folgendem Trick, den ich Th. und M.L. Beyer (MC 10/1983) abgeschaut habe.

Wir verlegen den Beginn des Basic-Variablenspeichers einfach auf den Beginn des Bildschirmspeichers. Auf diese Weise können wir zwar kein vernünftiges Programm laufen lassen, aber alle direkt eingegebenen Variablen-Definitionen werden sofort sichtbar, weil sie eben im Bildschirmspeicher stehen.

Wir erreichen die Verlegung des Speichers durch »Verbiegen« der Zeiger in den Zellen 45 und 46 und 47 und 48. Die Bedeutung dieser Zeiger ist ja im Kurs erklärt.

Die Speicherverlegung beziehungsweise die Methode dazu ist für den C 64 anders als für den VC 20.

##  VC 20:

Alle Angaben gelten für den VC 20 ohne Speichererweiterung, also ziehen Sie bitte alle Speichermodule heraus. Der Speicherbereich für Programme und deren Variablen beginnt jetzt ab Adresse 4096, das ist Block 1 im Bild 5. Der Bildschirmspeicher beginnt ab 7680. Wir verlegen jetzt den Bildschirmspeicher in den Block 1, so daß er ebenfalls ab Adresse 4096 beginnt. Danach müssen wir noch eine Farbe - am besten Schwarz - in den Farbspeicher POKEn, der in dieser neuen Konfiguration von 37888 bis 38399 liegt. Warum das so Ist, erklärt Christoph Sauer in seinem Aufsatz »Der gläserne VC 20«, Teil 4, im 64'er 1/85, Seite 131.

Das High-Byte der Adresse, in welcher der Bildschirmspeicher beginnt, steht in der Speicherzelle 648. Sie können das jederzeit mit PRINT PEEK(648) nachprüfen. Umgekehrt können wir eine Zahl hineinPOKEn, wodurch der Bildschirmspeicher verschoben wird. In unserem Fall erhalten wir das High-Byte für 4096 durch 4096/256 = 16.

Machen Sie jetzt bitte folgende Schritte:

1) direkt eingeben: POKE 648,l6(RETURN),
2) RUN/STOP und RESTORE drücken, bis der Cursor wieder da ist,
3) direkt eingeben:

        FOR J = 37888 TO 38399: POKE J,0: NEXT J (RETURN),

4) mit der DELETE-Taste (nicht mit CLR !) den ganzen Text des Bildschirms löschen,
5) mit dem Cursor etwa acht Zeilen nach unten gehen,
6) mit der Commodore- und SHIFT-Taste zusammen auf die Groß- und Kleinschrift umstellen.

Schritt 1 und 3 habe ich oben schon erklärt. Schritt 4 ist nicht absolut notwendig, aber ein leerer Bildschirm ist für uns besser. Die CLR-Taste würde Schritt 3 zunichte machen. Schritt 5 erlaubt uns, weiter unter auf dem Bildschirm Variablen einzugeben, ohne den oberen Teil vollzuschreiben. Schritt 6 schließlich erleichtert das Erkennen der Variablen-Darstelllung.

## C 64:

Beim C 64 beginnt der Bildschirmspeicher ab 1024. In Low-/ High-Byte-Darstellung ist das 0/4 (1024/256=4, Rest 0). Geben Sie bitte direkt ein:

    POKE 46,4 :POKE 48,4

Das Low-Byte in 45 und 47 können wir weglassen, da es ja in beiden Fällen 0 ist. Diese Methode gilt für alle neueren C 64, bei denen direkt ein Zeichen in den Bildschirmspeicher gePOKEt werden kann, ohne sich um die Zeichenfarbe kümmern zu müssen. Es gibt noch einige C 64 mit älteren Betriebssystemen, bei denen die Zeichenfarbe auch angegeben werden muß. Hier gilt:

    FOR J = 0 TO 1000:POKE 55296*3,14:NEXT J

## Alles weitere gilt für beide Computertypen gleich

Wenn Sie jetzt den Bildschirm löschen, den Cursor ungefähr in die Mitte des Bildschirms fahren und wiederum direkt eingeben:

`VARIABLE = 3` und die RETURN-Taste drücken, dann erscheinen oben sieben Zeichen. Bitte schalten Sie mit der SHIFT- und Commodore-Taste auf den zweiten Zeichensatz um, jetzt können wir besser lesen.

Aus anderen Kursen wissen Sie wahrscheinlich, daß Variable mit 7 Byte dargestellt werden. In der Tat sehen wir oben die ersten beiden Buchstaben des Variablennamens VA und fünf weitere Zeichen. Wir wollen aber systematisch vorgehen und uns zuerst die ganzzahligen Variablen anschauen.

### Ganzzahl-Variable

Wiederholen Sie bitte den Vorgang (Löschen, Cursor auf Mitte, 2. Zeichensatz). Jetzt geben Sie eine Ganzzahl-Variable ein:

    VA%=3

Nach RETURN sehen wir als erstes Zeichen ein reverses V, dann ein reverses A, den Klammeraffen @, das kleine c und nochmals drei @. Die beiden ersten Zeichen des Variablennamens (besteht er nur aus einem Zeichen, wird mit einer 0 aufgefüllt) werden mit ihrem ASCII-Code eingegeben, zu dem bei Ganzzahl-Variablen zur Kennzeichnung einer solchen die Zahl 128 addiert wird.

Schauen Sie in einer ASCII-Tabelle (64’er, Ausgabe 7/84) nach: Das V hat 86, um 128 erhöht gibt das 214. Wir arbeiten hier aber im Bildschirmspeicher, der die Zahlen auf seine eigene Weise interpretiert, nämlich als Bildschirmcode. Der Bildschirmcode-Tabelle entnehmen wir das Zeichen für den Wert 214 und das ist das invertierte V. Für das A können Sie das selbst nachvollziehen.

Also: In unserer Darstellung erkennen wir Ganzzahl-Variable an den invertierten Zeichen des Namens.

Das 3. und 4. Zeichen sind das High- und Low-Byte des Variablenwertes und zwar im Bildschirmcode. In unserem Beispiel der 3 ist das High-Byte 0, also der Klammeraffe @, das Low-Byte 3, also das c. Die restlichen drei Byte sind mit 0 aufgefüllt.

Wenn Sie mit dem Cursor auf die 3 fahren, es mit einer 5 überschreiben und RETURN drücken, verwandelt sich das c in ein e. Beim Überschreiben mit 255 erscheint als 4. Byte das Zeichen für den Bildschirmcode 255. Beim Überschreiben mit 257 ändern sich beide Bytes. Das 3. (High-)Byte springt auf a (=1), das 4. (Low-)Byte ebenfalls auf a. Nun, 1 * 256+1 = 257.

Während, wie bewiesen, das Low-Byte von 0 bis 255 gehen kann, sind beim High-Byte nur Werte zwischen 0 und 127 zugelassen. Die Werte ab 128 signalisieren negative Zahlen. Probieren Sie es aus:

    127 * 256+255=32767

Ein Überschreiben mit 32767 resultiert in einer Darstellung der Zeichen für den Bildschirmcode 127 und 255. Der Wert 32768 wird nicht mehr akzeptiert. Dasselbe machen wir noch schnell für negative Zahlen.

Überschreiben Sie bitte die letzte Zahl mit 0. Wie zu erwarten war, sind Byte 4 und 5 jetzt 0 (Klammeraffe).

Wenn Sie jetzt mit -1 überschreiben, erscheint für beide Bytes das Zeichen mit dem Bildschirmcode 255. Bei -2 sehen wir die Zeichen mit den Code-Werten 255 und 254.

Sie sehen also, daß die negativen Zahlen für ganzzahlige Variable sozusagen vom Ende der Tabelle her dargestellt werden, wobei die höchste negative Zahl wieder 32767 ist. Diese »Rückwärtszählung« ist bedingt durch die Methode der negativen Zahlendarstellung im Zweierkomplement. Der Platz und die Gelegenheit verbieten es mir, näher darauf einzugehen. Aber ich glaube, unser kleines Experiment hat Ihnen zumindest von der Darstellung her den Zusammenhang gezeigt. In Bild 6 ist diese Darstellung der ganzzahligen Variablen im Speicher wiedergegeben.

    | 1       | 2       | 3      | 4      | 5  6  7 |
    |---------|---------|--------|--------|---------|
    | Erstes  | Zweites | High-  | Low-   |         |
    |-------------------|-----------------|---------|
    | Zeichen des       | Byte des Varia- | 0  0  0 |
    | Variablen-Namens  | blenwertes      |         |
    | (ASCII-Wert + 128)|                 |         |
    
    Bild 6. So stehen ganzzahlige Variable im Speicher

### Gleitkomma-Variable

Ich hoffe, Sie verzeihen mir, wenn ich diese Darstellung an dieser Stelle überspringe. Sie ist nämlich nicht ganz leicht zu verstehen, und ich möchte sie lieber dann im Detail erklären, wenn wir zur Diskussion der Speicherzellen 97 bis 101, nämlich des Gleitkomma-Akkumulators kommen. Da geht es in einem Stück. Als Vorgeschmack gebe ich jetzt in Bild 7 nur die Zusammenfassung an.

    | 1       | 2       | 3        | 4      5      6      7   |
    |---------|---------|----------|--------------------------|
    | Erstes  | Zweites |          |                          |
    |-------------------|          | Mantisse mit Genauig-    |
    | Zeichen des       | Exponent | keit von 32 Dualstellen, |
    | Variablen-Namens  | + 129    | 1. Bit des 1. Bytes ist  |
    | (ASCII-Wert)      |          | das Vorzeichen           |
    
    Bild 7. Gleitkomma-Variable

### String-Variable

Zuerst ist es erforderlich, den Computer in den Anfangszustand zurückzusetzen. Wenn Sie einen RESET-Schalter haben, bitte diesen drücken, sonst aber aus- und einschalten. Wir geben nach Löschen des Bildschirms in der unteren Hälfte direkt ein:

    ZX$="A" <RETURN>

Wir erhalten ein Z, ein invertiertes X, ein kleines a, ein grafisches Zeichen, eine Leerstelle und zwei Klammeraffen.

Fahren Sie bitte jetzt mit dem Cursor auf das A und ändern den String um in BC. Nach RETURN verwandelt sich das a in das b, das 4. Zeichen ändert sich ebenfalls. Die ersten beiden Zeichen sind also wieder der Name der Variable.

Um zu kennzeichnen, daß es eine String-Variable ist, erscheint das 2. Zeichen des Namens invertiert. Wie oben entsteht es dadurch, daß zum ASCII-Code die Zahl 128 addiert wird. Diese Zahl wird aber wieder als Bildschirmcode interpretiert und entsprechend angezeigt (vergleichen Sie es mit den ASCII- und Bildschirmcode-Tabellen).

Das 3. Zeichen gibt die Länge des Strings an, also im ersten Fall mit a (=1 im Bildschirmcode), im 2. Fall mit b (=2). Zeichen 4 und 5 geben als Low- und High-Byte die Adresse an, bei der begonnen wird, den Text des Strings zu speichern. Das können wir nachprüfen.

Wir hatten die beiden Fälle:

1. ZX$ = ”A": 4. Zeichen: (Bildschirmcode: 255) und 5. Zeichen: (Bildschirmcode 156) ergibt als Adresse 40959.
2. ZX$ = ”BC": 4. Zeichen: (Bildschirmcode 253) und 5. Zeichen: (Bildschirmcode 156) ergibt als Adresse 40957.

Der Text der Zeichenketten wird am Ende des Arbeitsspeichers (40959 beim C 64, 7679 beim VC 20 ohne Erweiterung) abgelegt und zwar von hinten nach vorn.

Mit `PRINT PEEK(40957);PEEK(40958);PEEK(40959)` drucken wir den Inhalt dieser Speicherzellen aus und erhalten: 66 67 65. Im ASCII-Code ist das: B C A. Die Zusammenfassung für String-Variable (Bild 8) sieht so aus:

    | 1       | 2       | 3       | 4       | 5       | 6  7 |
    |---------|---------|---------|---------|---------|------|
    | Erstes  | Zweites |         | High-   | Low-    | 0  0 |
    |-------------------| Anzahl  |---------|---------|      |
    | Zeichen des       | der     | Byte der Adresse, |      |
    | Variablen-Namens  | Zeichen | ab welcher der    |      |
    | ASCII-  | ASCII-  | des     | Text des Strings  |      |
    | Wert    | Wert+128| Strings | abgespeichert ist |      |
    
    Bild 8. String-Variable

## Texteinschub Nr. 10: Felder in Basic

Zur Wiederholung: Es gibt zwei Arten von Variablen, normale Variable und Felder. Jede der beiden Arten ihrerseits kann aus Gleitkomma-Zahlen, ganzen Zahlen oder Zeichenketten bestehen.

Eine normale Variable kann immer nur einen Wert haben, ein Feld enthält gleichzeitig viele Werte, alle unter demselben Variablen-Namen.

Wir können uns ein Feld mit dem Namen KARLSTRASSE als eine Liste vorstellen, in der jedes Element zwar auch den Namen Karlstraße hat, sich aber von den anderen Elementen durch eine eigene Hausnummer unterscheidet. Jede Variable in einer Hausnummer hat einen bestimmten Wert.

Während eine normale Variable einfach mit A=3 einen Wert zugewiesen bekommt, muß ein Feld erst definiert werden, nämlich wie viele Elemente es enthält. Wir machen das mit dem Befehl

    DIM KARLSTRASSE (12)

Dieses Feld hat 13 Elemente (von 0 bis 12). Jedem Element kann nun ein Variablenwert zugewiesen werden durch

    KARLSTRASSE (0)=25
    KARLSTRASSE (1)=56

Das Feld KARLSTRASSE hat in der Klammer nur eine Zahl, man sagt, es hat nur eine Dimension.

Ein zweidimensionales Feld entspricht einem Schachbrett, mit Zahlen in der einen und Buchstaben in der anderen Dimension. Wir definieren es mit:

    DIM AX (7,7)

AX ist der Name, jede Dimension hat acht Elemente, insgesamt kann das Feld 64 Werte enthalten.

Ein dreidimensionales Feld entspricht einem Quader, oder bei gleicher Elementenzahl pro Dimension (Seite) einem Würfel. Dieses wird dimensioniert mit

    DIM BY (125,6,2)

Die Anzahl der Dimensionen wird nur begrenzt durch den verfügbaren Speicherplatz. Wieviel Bytes pro Feld gebraucht wer- den, entnehmen Sie bitte der Erklärung bei der Darstellung der Feld-Variablen (Texteinschub Nr. 11).

Ein Feld, das wie bisher gezeigt dimensioniert wird, enthält Gleitkomma-Zahlen.

Ein Feld mit ganzen Zahlen wird durch das Zeichen % nach dem Namen gekennzeichnet, also:

    DIM CZ%(.,.,.)

Ein Feld mit Zeichenketten dagegen hat nach dem Namen das übliche Zeichen $, also:

    DIM DT$(..,..,..)

»Wozu brauche ich Felder, wenn ich auch normale Variable verwenden kann?«, werden Sie vielleicht noch fragen.

Felder haben den großen Vorteil, daß immer dann, wenn viele Variable in einem Programm vorkommen, die alle einen gewissen Zusammenhang haben, viel Speicherplatz gespart werden kann.

Eine normale Variable braucht 7 Byte, eine Feld-Variable nur 5 oder bei ganzen Zahlen sogar nur 2 Byte. Zugegeben, vorher steht noch ein längerer Kopf, aber halt nur einmal. Und das zahlt sich bei vielen Variablen sehr rasch aus.

Und schließlich muß ich noch darauf hinweisen, daß die »Hausnummern« oder Indizes der Elemente innerhalb eines Programms durch mathematische Operationen verändert und manipuliert werden können. Aber das ist natürlich höhere Programmierkunst und geht über diese kurze Einführung hinaus.


# Texteinschub Nr. 11: Darstellung der Felder-(Array-)Variablen im Speicher

Die Felder-Variablen kommen in drei Arten vor:

* als ganze Zahlen,
* als Gleitkomma-Zahlen,
* als Zeichenketten.

Sie sind in dem Texteinschub Nr. 10 »Felder in Basic« kurz beschrieben.

Wir wollen sie uns hier mit den Methoden anschauen, welche ich für den C 64 und für den VC 20 in dem Texteinschub Nr. 9 »Darstellung der normalen Variablen im Speicher« beschrieben habe.

Beim C 64 ist allerdings ein Zusatz dabei. Sie müssen, am besten gleich am Anfang, noch eingeben:

    POKE 44,4:NEW

Ein eventuell auftretender SYNTAX ERROR soll uns nicht weiter stören.

Wenn Sie also das jeweilige Kochrezept ausgeführt und damit den Bildschirm- und den Variablenspeicher auf dieselbe Adresse gelegt haben, können wir anfangen.

## Gleitkomma-Feld

Geben Sie direkt ein:

    DIM AB(1,2,3)

Wir dimensionieren also ein Feld mit dem Namen AB, es hat drei Dimensionen, die erste Dimension hat zwei (0,1) Werte, die zweite hat drei und die dritte hat vier Werte. Sobald Sie die RETURN-Taste drücken, erscheint das Feld auf dem Bildschirm. Wir sehen folgende Zeichen: A, B, invertiertesC , @ c @ d @ c @ b plus 120 Klammeraffen @.

Die ersten zwei Stellen sind der Name des Feldes in der Darstellung für Gleitkomma-Variable, wie in der letzten Folge beschrieben wurde. Die dritte und vierte Stelle geben im Bildschirmcode als Low- und High-Byte die Länge des Feldes an (das inverse C = 131, das © = 0, bitte nachzählen). Die fünfte Stelle zeigt die Anzahl der Dimensionen (c = 3) an. Ab der sechsten Stelle stehen die Anzahl der Elemente der Dimension (diesmal als High- und Low-Byte) und zwar beginnend mit der letzten Dimension. In unserem Falle ist das also in Stelle 6 und 7 ein @ und d (0 - 3 =4=d), Stelle 8 und 9 sind dasselbe für die zweite Dimension und schließlich Stelle 10 und 11 für die erste Dimension (0 - 1=2=b). Danach folgen entsprechend der Anzahl der dimensionierten Elemente (2*3*4=24) 6 Byte pro Element (24*5=120), die vorerst auf 0 = @ stehen, die aber mit den Werten der Elemente aufgefüllt werden.

Dieses Auffüllen wollen wir nachvollziehen. Geben Sie bitte direkt ein:

    AB(0,0,0)=5

Wir weisen damit dem allerersten Element des Feldes den Wert 5 zu.

In der oberen Darstellung des Feldes AB ändern sich dadurch Byte 12 und 13. Das neu erschienene inverse C und die Leerstelle mit den drei nachfolgenden @ ist die Gleitkomma- Darstellung (Mantisse und Exponent) der Zahl 5. Auf diese Darstellung werde ich später im Verlauf dieses Kurses bei der Besprechung der Speicherzelle 97 noch genauer eingehen.

Wenn wir jetzt (durch Überschreiben der vorigen Anweisung) zusätzlich noch eingeben:

    AB(1,0,0)=6

erreichen wir eine entsprechende Änderung der Bytes 17 und 18, also des zweiten Elements des Feldes.

In Bild 9 sind die Stellen eines Gleitkomma-Feldes grafisch dargestellt.

      1         2         3      4      5        6      7      /                 a         b   c   d   e
    |---------|---------|------|------|--------|------|------|-\ |------|------|---------|---|---|---|---|-->
    | Erstes  | Zweites | Low  | High |        | High | Low  | / | High | Low  |                         |
    |                   |     Byte    | Anzahl |     Byte    | \ |     Byte    |Exponent      Mantisse   |
    |    Zeichen des    |-------------| der    |-------------| / |-------------|  +125                   |
    |    Feld-Namens    |  Länge des  | Dimen- | Anzahl der  | \ | Anzahl der  |          des 1. Elements| des 2. Elements
    |                   |    Feldes   | sionen | Elemente    | / | Elemente    |                         |
    |                   |             |        | der letzten | \ | der ersten  |                         |
    |                   |             |        | Dimension   | / | Dimension   |                         |
    |---------|---------|------|------|--------|-------------|-\-|-------------|---------|---|---|---|---|-->
    |<-----------------------  KOPF  ----------------------->| /
    
    Bild 9. Gleitkomma-Feld

## Ganzzahliges Feld

Im Vergleich zu dem Gleitkomma-Feld dimensionieren wir als nächstes ein ganzzahliges Feld:

    DIM AB%(l,2,3)

Jetzt erscheint auf dem Bildschirm gleich anschließend an das erste Feld eine neue Darstellung: invertiertes A, invertiertes B, ;, @, c@, d, @, c, @b plus 48 Klammeraffen @.

Die ersten 11 Byte haben dieselbe Bedeutung wie beim Gleitkomma-Feld, aber nur deswegen, weil wir dieselben drei Dimensionen mit identischer Elementenzahl dimensioniert haben. Bei mehr Dimensionen wäre dieser Kopf natürlich länger. Die inverse Darstellung des Feldnamens signalisiert ein ganzzahliges Feld. Die dritte Stelle zeigt das »;« - im Bildschirmcode ist das die 59. In der Tat ist das Feld nur 59 Byte lang, also wesentlich weniger als das Gleitkomma-Feld. Die 2 * 3 * 4=24 Elemente benötigen in der Ganzzahl-Darstellung nur je 2 Byte (24*2=48+11=59). Womit bewiesen ist, daß eine Ganzzahl- Darstellung mit dem Zeichen % erheblich Speicherplatz spart - allerdings nur bei Feldern!

Jetzt wollen wir noch den Inhalt des Feldes füllen, so wie vorher mit:

    AB%(0,0,0)=5

... und prompt ändert sich Byte Nummer 13 in ein e (e = 5).

Eine Eingabe für das zweite Element:

    AB$(1,0,0)=6

verändert das 15. Byte in ein f.

In Bild 10 ist der Inhalt eines Ganzzahl-Feldes grafisch dargestellt.

      1   2   3   4    \    a      b      c      d
    |---|---|---|---|--/--|------|------|------|------|-->
    |                  \  | Low  | High | Low  | High |
    |                  /  |    Byte     |    Byte     |
    |      KOPF        \  |-------------|-------------|
    | (wie in Bild 2)  /  |             |             |
    |                  \  |     des     |     des     |     des
    |                  /  | 1. Elements | 2. Elements | 2. Elements
    |                  \  |             |             |
    |---|---|---|---|--/--|------|------|------|------|->
                       \

    Bild 10. Ganzzahliges Feld
    
## Felder mit Zeichenketten

Die Dimensionierung eines Feldes mit Zeichenketten sieht so aus:

    DIM AB$(1,2,3)

Auf dem Bildschirm erscheint jetzt ein Feld:

Auch hier zeigen die ersten elf Stellen dieselbe Information wie bei den anderen Feldern. Zur Kennzeichnung des Zeichenketten-Feldes ist das zweite Zeichen des Feldnamens invers dargestellt. Zeichen 3 und 4 geben wieder die Länge des Feldes an. Das S hat den Bildschirmcode 83. (Vorsicht! Da wir im Groß-/Kleinbuchstaben-Modus sind, müssen wir die jeweils rechte Seite der Spalten in der Code-Tabelle nehmen). Die Länge 83 minus 11 Kopfstellen ergibt 72 Byte, geteilt durch 24 (2*3*4 = 24 Elemente) erhalten wir 3 Byte zur Darstellung eines Elements.

Das erste Byte gibt die Länge der Zeichenkette an, das zweite und dritte Byte (Low-/High-Byte) die Adresse, ab der die Zeichenkette im vierten Block gespeichert ist.

Die Methode ist also dieselbe wie bei den »normalen« Zeichenketten-Variablen. Das wollen wir uns auch noch ansehen. Geben Sie direkt ein:

    AB$(0,0,0) = "AAAAAA"

In der Darstellung des Feldes ändern sich dadurch die Stellen 12, 13 und 14 und wir sehen

* beim C 64:
* beim VC 20:

Im Bildschirm steht dafür:

* C 64: 6 250 159 das heißt 6 Zeichen, ab Adresse 250+159*256=40959
* VC 20: 6 250 29 das heißt 6 Zeichen, ab Adresse 250+29*256=7674

Jetzt weisen wir dem letzten Element auch noch eine Zeichenkette zu:

    AB$(1,2,3)="BB"

Die letzten drei Stellen des Feldes ändern sich ebenfalls, wobei die erste mit dem b eine Zeichenkettenlänge von 2 angibt, dementsprechend muß die Anfangsadresse um 2 niedriger sein als die vorher definierte Kette: Das Low-Byte 250 - 2 = 248, in der Codetabelle finden wir dafür das, was auch im Feld steht. Das High-Byte bleibt unverändert.

Bild 11 zeigt die grafische Darstellung des Zeichenketten-Feldes.

Als letztes zeige ich Ihnen noch die im vierten Block gespeicherten Zeichenketten. Wir drucken einfach den CHR$-Wert der in den betreffenden Speicherzellen stehenden Codezahlen aus mit:

* VC 20:

        FOR I=248 TO 255:PRINT CHR$(PEEK(29*256+I));:NEXT

* C 64:

        FOR I=248 TO 255:PRINTCHR$(PEEK(159*256+I));:NEXT
        
... und wir erhalten die beiden Zeichenketten in umgekehrter Reihenfolge, also vom Speicherende her eingespeichert. Interessant ist, daß sich vor die Felder - wenn Sie sie noch auf dem Bildschirm hatten - die neu definierte Gleitkomma-Variable l@ geschoben hat. Auch das ist eine Demonstration des Speicherverfahrens der Variablen, genauso wie ich es Ihnen in der letzten Folge erklärt habe.

      1   2   3   4    \    a          b       c       d     e     f
    |---|---|---|---|--/--|----------|-------|-------|-----|-----|-----|-->
    |                  \  | Länge    | Low   | High  |                 |
    |                  /  | der      |     Byte      |                 |
    |      KOPF        \  | Zeichen- |---------------|                 |
    | (wie in Bild 2)  /  | kette      der Adresse,  |                 |
    |                  \  |            ab der der    |                 |
    |                  /  |            String ge-    |                 |
    |                  \  |          | speichert ist |                 |
    |---|---|---|---|--/--|--------------------------|-----------------|-->
                       \  |<---    1. Element    --->|<- 2. Element  ->|
    
    Bild 11. Zeichenketten-Feld


## Texteinschub Nr. 12: Darstellung der Variablen einer selbstdefinierten Funktion

Ich habe Ihnen gezeigt, wie im Programmspeicher abgelegte normale Variablen und Felder-Variablen sichtbar gemacht werden können. Damit konnten wir den Aufbau und die Darstellung der einzelnen Variablenarten studieren.

Heute will ich einen weiteren Variablentyp vorstellen, nämlich den der selbstdefinierten Funktionen.

Sie erinnern sich vielleicht, mit dem Basic-Befehl »DEF FN (Name)(Variable)« können wir komplizierte Funktionen selbst erfinden, definieren und später als »FN (Name)(Variable)< weiter verarbeiten. Diesen Typ wollen wir uns anschauen, wie er im Speicher steht.

Im Prinzip verwenden wir dieselben Methoden zur Sichtbarmachung wie die letzten Male.

Aber ein Unterschied kommt noch dazu. Der Befehl DEF kann leider nicht direkt eingegeben werden, sondern muß immer als Teil einer Programmzeile mit einer Zeilennummer versehen sein.

Deshalb schreiben wir zuerst ein kleines Programm zur Definition der Funktion plus Variable, bevor wir den Variablenspeicher mit dem Bildschirmspeicher zusammenlegen:

    10 DEF FNAA(X)=3*SIN(X)+COS(X)
    20 X=5
    30 PRINT FNAA(X)

Die Funktion hat also den Namen »AA«. Bevor wir weitermachen, überprüfen Sie bitte mit RUN, ob alles stimmt. Nun wird der Speicher verschoben.

**Für den C 64 gilt:**

1. POKE 46,4:POKE 48,4
2. Bildschirm löschen mit CLR-Taste
3. Cursor auf die Mitte fahren
4. LIST (es erscheint das Programm)
5. auf den 2. Zeichensatz umschalten (mit C= und SHIFTTaste)
6. RUN

**Für den VC 20 (ohne. Erweiterung) gilt:**

Nur den Bildschirm auf 4096 zu verschieben, wie das letzte Mal, geht diesmal nicht, da wir ja für DEF ein kleines Programm schreiben müssen.

Also legen wir Bild- und Variablenspeicher ab Adresse 5120 (5120/256=20).

1. POKE 46,20:CLR
2. POKE 648,20
3. STOP/RESTORE-Tasten, bis Cursor wieder da ist
4. Bildschirm löschen mit CLR-Taste
5. dfe ersten vier bis sechs Zeilen mit SPACE-Taste überfahren
6. Cursor ein paar Zeilen nach unten
7. LIST (es erscheint das Programm)
8. mit Commodore- und SHIFTTaste auf 2. Zeichensatz umschalten
9. RUN

Wir sehen jetzt oben zwei Gruppen mit je sieben Zeichen, wie üblich.

Die erste Gruppe stellt die Funktion FNAA(x) dar. Sie ist gekennzeichnet durch das invertierte erste Zeichen des Namens, während das zweite Zeichen normal erscheint.

Das dritte und vierte Zeichen gibt in Low-/High-Byte- Darstellung (im Bildschirmcode) die Adresse an, ab der die Funktion FNAA(x) im Programmspeicher abgelegt ist. Mit `PEEK (3. Zeichen)+256*PEEK (4. Zeichen)` kann das abgefragt werden.

Das fünfte und sechste Zeichen nennt die Adresse, an welcher der Zahlenwert der Funktions-Variablen X anfängt. Das siebente Zeichen schließlich ist das erste Zeichen der Funktion selbst (in unserem Beispiel die 3).

Die zweite Gruppe beschreibt die Variable X der Funktion. Die normale Darstellung der beiden ersten Zeichen, die den Namen darstellen, gibt uns an, daß es sich um eine Gleitkomma-Variable handelt, deren Wert als Mantisse und Exponent dargestellt ist. Der Aufbau einer Funktion ist in Bild 12 zusammengefaßt:

    | 1       | 2       | 3       | 4       | 5        | 6        | 7       |
    |---------|---------|---------|---------|----------|----------|---------|
    | Erstes  | Zweites | Low-    | High-   | Low-     | High-    |         |
    |-------------------|---------|---------|----------|----------|---------|
    | Zeichen des       | Byte der Adresse, | Byte der Adresse,   | 1. Zei- |
    | Funktionsnamens   | ab der die        | ab dem der jewei-   | chen    |
    |---------|---------| Funktion abge-    | lige Wert der Funk- | der     |
    | ASCII-  | ASCII-  | speichert ist     | tionsvariablen X    | Funk-   |
    | Wert+128| Wert    |                   | abgespeichert ist   | tion    |

    Bild 12. Selbstdefinierte Funktion


# Texteinschub Nr. 13: Wie zufällig sind Zufallszahlen?

Der Befehl RND(X) ergibt eine Zufallszahl zwischen 0 und 1 - so steht es im Commodore-Handbuch.

Eine Zufallszahl ist definitionsgemäß rein dem Zufall überlassen. Ihr Wert kann nicht vorhergesehen werden. Wie kann aber ein Computer, in dem alle Vorgehensweisen und Arbeitsschritte fest vorprogrammiert sind, eine zufällige Zahl erzeugen? Die Commodore-Computer machen das so:

Der Befehl RND nimmt eine bestimmte Ausgangszahl (auf die ich noch näher eingehen werde), auf englisch »seed« = Samen genannt, multipliziert sie mit 11879546.4 und zählt 3.92767778 * 10^8 dazu. Die 5 Byte der resultierenden Gleitkommazahl werden miteinander vertauscht und in einen positiven Bruch umgewandelt. Diese Manipulation ergibt die »Zufallszahl«, die als neuer »Samen« in den Speicherzellen 139 bis 143 gespeichert wird.

Es ist sicher einzusehen, daß die Zufälligkeit nicht sehr hoch sein kann, es sei denn, die oben genannte und noch nicht erklärte Ausgangszahl ist zufällig.

Die erste Ausgangszahl hängt vom »Argument« des RND(X)-Befehls ab, das heißt vom Wert X, der in der Klammer dahinter steht. Es gibt drei Möglichkeiten für das Argument:

* eine positive Zahl (egal, welcher Wert)
* eine negative Zahl
* die Zahl 0

## Eine positive Zahl

zum Beispiel RND (1) oder RND(56) nimmt als Samen die Zahl 0.811635157, die beim Einschalten des Computers als 5-Byte- Gleitkommazahl in die Speicherzellen 139 bis 143 geschrieben worden ist. In den fünf Zellen stehen die Zahlen 128, 79, 199, 82, 88.

Daraus folgt aber, daß nach dem Einschalten des Computers mit RND(1) immer dieselbe Sequenz von Zufallszahlen erzeugt wird. Schalten Sie bitte den Computer aus und ein und geben Sie ein:

    10 PRINT RND(1):G0T0 10

Notieren Sie die ersten paar Zahlen und wiederholen Sie mit Aus-/Einschalten die Prozedur. Sie werden immer dieselben Zahlen sehen.

Zum Austesten von Programmen mit bekannten Zahlensequenzen ist diese Methode sicher wichtig, aber echte Zufallszahlen sind das nicht!

## Eine negative Zahl

zum Beispiel RND(-1)oder RND(-95) bringt als erstes das Argument selbst (in meinem Beispiel -1 oder -95) als Gleitkommazahl in die Speicherzellen 139 bis 143, von wo sie als Samen den schon beschriebenen Manipulationen unterworfen wird. Nur - mit einem bestimmten negativen Argument erhalten Sie immer dieselbe Zufallszahl. Probieren Sie es aus: PRINT RND(-2) ergibt immer dieselbe Zahl.

Es mag Fälle geben, wo die Vorgabe des allerersten Samens wünschenswert ist. Ich will aber von zufälligen Zählen sprechen. Wir können diese Methode des negativen Arguments dadurch verbessern, daß wir als Argument selbst eine Zufallszahl nehmen.

Als derartige Zahl bietet sich der Wert der inneren Uhr TI an, die beim Einschalten des Computers losläuft und 60mal in der Sekunde weitergestellt wird. Da kein Mensch wissen kann, welchen Wert die UhrTI gerade hat, kommt der Befehl RND(-TI) dem absoluten Zufall schon sehr nahe.

## Das Argument (0)

verwendet eine andere Methode. Als Samen nimmt er eine sich ständig ändernde Zahl, die beim VC 20 aus vier Registerinhalten des VIC-lnterface-Bausteins genommen werden. Beim C 64 wird es ähnlich gemacht, nur ist der VIC-Baustein ein anderer Typ.

Mit derselben Methode nach dem Einschalten wie im ersten Fall oben können Sie das leicht überprüfen.

Ich habe eingangs zitiert, daß RND(X) eine Zahl zwischen 0 und 1 erzeugt; das gilt aber nur für ein positives Argument. Wenn Sie hingegen eine Zufallszahl innerhalb eines ganz bestimmten Bereiches brauchen, müssen Sie anders vorgehen.

## Kochrezept Nr. 1

Mit folgender Formel ist derZahlenbereich beliebig vorgebbar: `X=(RND(1)*A)+B`

* Die Zahl A gibt einen Bereich von 0 bis A vor.
* Die Zahl B legt den untersten Wert des Bereiches fest.

Beispiele:

* `10 PRINT (RND(1)*6)+1:GOTO 10` erzeugt Zahlen von 1 bis 6
* `10 PRINT (RND(1)*52)+1:G0T0 10` erzeugt Zahlen von 1 bis 52
* `10 PRINT (RND(1)*6)+10:G0T0 10` erzeugt Zahlen von 10 bis 16

Mit dem Vorschalten der Funktion INT vor den Befehl RND werden die Zufallszahlen auf ganze Zahlen beschränkt.

    10 PRINT INT (RND(1)*6)+10:GOTO 10

Noch einmal: Zufallszahlen innerhalb bestimmter Zahlenbereiche sind gekoppelt mit einem positiven Argument. Wir haben aber gesehen, daß gerade so keine echten Zufallszahlen erzeugt werden. Deshalb brauchen wir noch ein zweites Kochrezept.

## Kochrezept Nr. 2

Wenn Sie in einem Programm nach dem Einschalten des Computers immer neue Zufallszahlen brauchen, ist es empfehlenswert, für die allererste Zufallszahl RND(-TI) oder RND(0) zu verwenden, dann aber mit RND(1) fortzufahren.

Dasselbe gilt, wenn ein Programm wegen INPUT oder WAIT eine Pause hat. Nach der Pause sollte zuerst ein neuer Ausgangswert genommen werden.

Als letztes will ich noch beschreiben, wie man Zufallszahlen innerhalb von Maschinenprogrammen erzeugen kann.

Im Betriebssystem steht natürlich eine Routine für den Befehl RND. Im C 64 beginnt sie ab 57495 ($E097), im VC 20 ab 57492 ($E094).

Der Ausgangswert (Samen) wird dabei aus dem Gleitkomma-Akkumulator Nr. 1 geholt, dessen Vorzeichen oder Wert 0 das weitere Vorgehen der Routine bestimmt.

Sie müssen also den Samen in den Akkumulator Nr. 1 laden und dann mit JSR auf die RND-Routine springen. Als Resultat können Sie einen oder mehrere Werte der Zellen 140 bis 143 verwenden und nach Belieben weiterverarbeiten.
