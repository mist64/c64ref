- Fully Commented Commodore 64 ROM Disassembly (German)
-
- CBMBASIC and KERNAL
-
- The comments have been taken from
-    Baloui, Said. 
-    Das neue Commodore-64-intern-Buch.
-    Düsseldorf: Data-Becker, 1990.
-    ISBN 3890113079
-
- The ROM is the 901227-02 version ($FF80 = 0), except for the
- area $E57C-$E599, which is taken from the 901227-03 version
- ($FF80 = 3).
-
- OCRed and formatted by Michael Steil <mist64@mac.com>
-
- Corrections (typos as well as content), translations etc.
- welcome at: https://github.com/mist64/c64disasm
-
------------------------------------------------------------
-
# This plain text file is formatted so that it can be automatically
# parsed in order to create cross-references etc.
# * Lines starting with "-" is top-level information. The first line
#   is the title. Lines starting with "--" are separators.
# * Lines starting with "#" are internal comments.
# * Lines starting with ".," indicate code to be disassembled.
# * Lines starting with ".:" indicate bytes to be dumped.
# * Comments start at the 33rd column.
# * 32 leading spaces and "***" indicate a heading. (Please leave one
#   line blank above every heading.)
# * Otherwise, 32 leading spaces indicate an overflow comment.
# The encoding is UTF-8.

.:A000 94 E3                    Start-Vektor $E394
.:A002 7B E3                    NMI-Vektor $E37B

.:A004 43 42 4D 42 41 53 49 43  'cbmbasic'

                                *** Adressen der BASIC-Befehle -1
                                *** (Interpreterkode Adresse Befehl)
.:A00C 30 A8                    $80 $A831 END
.:A00E 41 A7                    $81 $A742 FOR
.:A010 1D AD                    $82 $AD1E NEXT
.:A012 F7 A8                    $83 $A8F8 DATA
.:A014 A4 AB                    $84 $ABA5 INPUT#
.:A016 BE AB                    $85 $ABBF INPUT
.:A018 80 B0                    $86 $B081 DIM
.:A01A 05 AC                    $87 $AC06 READ
.:A01C A4 A9                    $88 $A9A5 LET
.:A01E 9F A8                    $89 $A8A0 GOTO
.:A020 70 A8                    $8A $A871 RUN
.:A022 27 A9                    $8B $A928 IF
.:A024 1C A8                    $8C $A81D RESTORE
.:A026 82 A8                    $8D $A883 GOSUB
.:A028 D1 A8                    $8E $A8D2 RETURN
.:A02A 3A A9                    $8F $A93B REM
.:A02C 2E A8                    $90 $A82F STOP
.:A02E 4A A9                    $91 $A94B ON
.:A030 2C B8                    $92 $B82D WAIT
.:A032 67 E1                    $93 $E168 LOAD
.:A034 55 E1                    $94 $E156 SAVE
.:A036 64 E1                    $95 $E165 VERIFY
.:A038 B2 B3                    $96 $B3B3 DEF
.:A03A 23 B8                    $97 $B824 POKE
.:A03C 7F AA                    $98 $AA80 PRINT#
.:A03E 9F AA                    $99 $AAA0 PRINT
.:A040 56 A8                    $9A $A857 CONT
.:A042 9B A6                    $9B $A69C LIST
.:A044 5D A6                    $9C $A65E CLR
.:A046 85 AA                    $9D $AA86 CMD
.:A048 29 E1                    $9E $E12A SYS
.:A04A BD E1                    $9F $E1BE OPEN
.:A04C C6 E1                    $A0 $E1C7 CLOSE
.:A04E 7A AB                    $A1 $AB7B GET
.:A050 41 A6                    $A2 $A642 NEW

                                *** Adressen der BASIC-Funktionen
.:A052 39 BC                    $B4 $BC39 SGN
.:A054 CC BC                    $B5 $BCCC INT
.:A056 58 BC                    $B6 $BC58 ABS
.:A058 10 03                    $B7 $0310 USR
.:A05A 7D B3                    $B8 $B37D FRE
.:A05C 9E B3                    $B9 $B39E POS
.:A05E 71 BF                    $BA $BF71 SQR
.:A060 97 E0                    $BB $E097 RND
.:A062 EA B9                    $BC $B9EA LOG
.:A064 ED BF                    $BD $BFED EXP
.:A066 64 E2                    $BE $E264 COS
.:A068 6B E2                    $BF $E26B SIN
.:A06A B4 E2                    $C0 $E2B4 TAN
.:A06C 0E E3                    $C1 $E30E ATN
.:A06E 0D B8                    $C2 $B80D PEEK
.:A070 7C B7                    $C3 $B77C LEN
.:A072 65 B4                    $C4 $B465 STR$
.:A074 AD B7                    $C5 $B7AD VAL
.:A076 8B B7                    $C6 $B78B ASC
.:A078 EC B6                    $C7 $B6EC CHR$
.:A07A 00 B7                    $C8 $B700 LEFT$
.:A07C 2C B7                    $C9 $B72C RIGHT$
.:A07E 37 B7                    $CA $B737 MID$

                                *** Hierarchiecodes und
                                *** Adressen-1 der Operatoren
.:A080 79 69 B8                 $79, $B86A Addition
.:A083 79 52 B8                 $79, $B853 Subtraktion
.:A086 7B 2A BA                 $7B, $BA2B Multiplikation
.:A089 7B 11 BB                 $7B, $BB12 Division
.:A08C 7F 7A BF                 $7F, $BF7B Potenzierung
.:A08F 50 E8 AF                 $50, $AFE9 AND
.:A092 46 E5 AF                 $46, $AFE6 OR
.:A095 7D B3 BF                 $7D, $BFB4 Vorzeichenwechsel
.:A098 5A D3 AE                 $5A, $AED4 NOT
.:A09B 64 15 B0                 $64, $B016 Vergleich


                                *** BASIC-Befehlsworte
.:A09E 45 4E                    end
.:A0A0 C4 46 4F D2 4E 45 58 D4  for next
.:A0A8 44 41 54 C1 49 4E 50 55  data input#
.:A0B0 54 A3 49 4E 50 55 D4 44  input dim
.:A0B8 49 CD 52 45 41 C4 4C 45  read let
.:A0C0 D4 47 4F 54 CF 52 55 CE  goto run
.:A0C8 49 C6 52 45 53 54 4F 52  if restore
.:A0D0 C5 47 4F 53 55 C2 52 45  gosub return
.:A0D8 54 55 52 CE 52 45 CD 53  rem stop
.:A0E0 54 4F D0 4F CE 57 41 49  on wait
.:A0E8 D4 4C 4F 41 C4 53 41 56  load save
.:A0F0 C5 56 45 52 49 46 D9 44  verify def
.:A0F8 45 C6 50 4F 4B C5 50 52  poke print#
.:A100 49 4E 54 A3 50 52 49 4E  print
.:A108 D4 43 4F 4E D4 4C 49 53  cont list
.:A110 D4 43 4C D2 43 4D C4 53  clr cmd sys
.:A118 59 D3 4F 50 45 CE 43 4C  open close
.:A120 4F 53 C5 47 45 D4 4E 45  get new
.:A128 D7 54 41 42 A8 54 CF 46  tab( to
.:A130 CE 53 50 43 A8 54 48 45  spc( then
.:A138 CE 4E 4F D4 53 54 45 D0  not step
.:A140 AB AD AA AF DE 41 4E C4  + - * / ' and
.:A148 4F D2 BE BD BC 53 47 CE  or <=> sgn
.:A150 49 4E D4 41 42 D3 55 53  int abs usr
.:A158 D2 46 52 C5 50 4F D3 53  fre pos sqr
.:A160 51 D2 52 4E C4 4C 4F C7  rnd log
.:A168 45 58 D0 43 4F D3 53 49  exp cos sin
.:A170 CE 54 41 CE 41 54 CE 50  tan atn peek
.:A178 45 45 CB 4C 45 CE 53 54  len str$
.:A180 52 A4 56 41 CC 41 53 C3  val asc
.:A188 43 48 52 A4 4C 45 46 54  chr$ left$
.:A190 A4 52 49 47 48 54 A4 4D  right$ mid$
.:A198 49 44 A4 47 CF 00        go

                                *** BASIC-Fehlermeldungen
.:A1A0 54 4F                    1 too many files
.:A1A0 4F 20 4D 41 4E 59 20 46
.:A1A8 49 4C 45 D3 46 49 4C 45  2 file open
.:A1B0 20 4F 50 45 CE 46 49 4C  3 file not open
.:A1B8 45 20 4E 4F 54 20 4F 50
.:A1C0 45 CE 46 49 4C 45 20 4E  4 file not found
.:A1C8 4F 54 20 46 4F 55 4E C4  5 device not present
.:A1D0 44 45 56 49 43 45 20 4E
.:A1D8 4F 54 20 50 52 45 53 45
.:A1E0 4E D4 4E 4F 54 20 49 4E  6 not input file
.:A1E8 50 55 54 20 46 49 4C C5
.:A1F0 4E 4F 54 20 4F 55 54 50  7 not output file
.:A1F8 55 54 20 46 49 4C C5 4D
.:A200 49 53 53 49 4E 47 20 46  8 missing filename
.:A208 49 4C 45 20 4E 41 4D C5
.:A210 49 4C 4C 45 47 41 4C 20  9 illegal device number
.:A218 44 45 56 49 43 45 20 4E
.:A220 55 4D 42 45 D2 4E 45 58  10 next without for
.:A228 54 20 57 49 54 48 4F 55
.:A230 54 20 46 4F D2 53 59 4E  11 syntax
.:A238 54 41 D8 52 45 54 55 52  12 return without gosub
.:A240 4E 20 57 49 54 48 4F 55
.:A248 54 20 47 4F 53 55 C2 4F  13 out of data
.:A250 55 54 20 4F 46 20 44 41
.:A258 54 C1 49 4C 4C 45 47 41  14 illegal quantity
.:A260 4C 20 51 55 41 4E 54 49
.:A268 54 D9 4F 56 45 52 46 4C  15 overflow
.:A270 4F D7 4F 55 54 20 4F 46  16 out of memory
.:A278 20 4D 45 4D 4F 52 D9 55  17 undef'd statement
.:A280 4E 44 45 46 27 44 20 53
.:A288 54 41 54 45 4D 45 4E D4
.:A290 42 41 44 20 53 55 42 53  18 bad subscript
.:A298 43 52 49 50 D4 52 45 44  19 redim'd array
.:A2A0 49 4D 27 44 20 41 52 52
.:A2A8 41 D9 44 49 56 49 53 49  20 division by zero
.:A2B0 4F 4E 20 42 59 20 5A 45
.:A2B8 52 CF 49 4C 4C 45 47 41  21 illegal direct
.:A2C0 4C 20 44 49 52 45 43 D4
.:A2C8 54 59 50 45 20 4D 49 53  22 type mismatch
.:A2D0 4D 41 54 43 C8 53 54 52  23 string too long
.:A2D8 49 4E 47 20 54 4F 4F 20
.:A2E0 4C 4F 4E C7 46 49 4C 45  24 file data
.:A2E8 20 44 41 54 C1 46 4F 52  25 formula too complex
.:A2F0 4D 55 4C 41 20 54 4F 4F
.:A2F8 20 43 4F 4D 50 4C 45 D8
.:A300 43 41 4E 27 54 20 43 4F  26 can't continue
.:A308 4E 54 49 4E 55 C5 55 4E  27 undef'd function
.:A310 44 45 46 27 44 20 46 55
.:A318 4E 43 54 49 4F CE 56 45  28 verify
.:A320 52 49 46 D9 4C 4F 41 C4  29 load

                                *** Adressen der Fehlermeldungen
.:A328 9E A1 AC A1 B5 A1 C2 A1
.:A330 D0 A1 E2 A1 F0 A1 FF A1
.:A338 10 A2 25 A2 35 A2 3B A2
.:A340 4F A2 5A A2 6A A2 72 A2
.:A348 7F A2 90 A2 9D A2 AA A2
.:A350 BA A2 C8 A2 D5 A2 E4 A2
.:A358 ED A2 00 A3 0E A3 1E A3
.:A360 24 A3 83 A3

                                *** Meldungen des Interpreters
.:A364 0D 4F 4B 0D              OK
.:A368 00 20 20 45 52 52 4F 52  ERROR
.:A370 00 20 49 4E 20 00 0D 0A  IN
.:A378 52 45 41 44 59 2E 0D 0A  READY.
.:A380 00 0D 0A 42 52 45 41 4B  BREAK
.:A388 00 A0

                                *** Stapelsuch-Routine für
                                *** FOR-NEXT- und GOSUB-Befehl
.,A38A BA       TSX             Stapelzeiger in X-Register
.,A38B E8       INX             4 mal erhöhen
.,A38C E8       INX             (nächsten zwei Rücksprung-
.,A38D E8       INX             adressen, Interpreter und
.,A38E E8       INX             Routine, übergehen)
.,A38F BD 01 01 LDA $0101,X     nächstes Byte hoten
.,A392 C9 81    CMP #$81        Ist es FOR-Code ?
.,A394 D0 21    BNE $A3B7       Nein: dann RTS
.,A396 A5 4A    LDA $4A         Variablenzeiger holen
.,A398 D0 0A    BNE $A3A4       keine Variable (NEXT):$A3A4
.,A39A BD 02 01 LDA $0102,X     Variablenzeiger aus
.,A39D 85 49    STA $49         Stapel nach $49/4A
.,A39F BD 03 01 LDA $0103,X     (Variablenzeiger)
.,A3A2 85 4A    STA $4A         holen
.,A3A4 DD 03 01 CMP $0103,X     Mit Zeiger im Stapel vergl.
.,A3A7 D0 07    BNE $A3B0       Ungleich: nächste Schleife
.,A3A9 A5 49    LDA $49         Zeiger wieder holen
.,A3AB DD 02 01 CMP $0102,X     Mit Zeiger im Stapel vergl.
.,A3AE F0 07    BEQ $A3B7       Gleich: Schleife gefunden,RTS
.,A3B0 8A       TXA             Suchzeiger in Akku
.,A3B1 18       CLC             Carry für Addition löschen
.,A3B2 69 12    ADC #$12        Suchzeiger um 18 erhöhen
.,A3B4 AA       TAX             und wieder zurück ins X-Rg.
.,A3B5 D0 D8    BNE $A38F       nächste Schleife prüfen
.,A3B7 60       RTS             Rücksprung

                                *** Block-Verschiebe-Routine
.,A3B8 20 08 A4 JSR $A408       prüft auf Platz im Speicher
.,A3BB 85 31    STA $31         Ende des Arraybereichs
.,A3BD 84 32    STY $32         als Beginn für freien Platz
.,A3BF 38       SEC             Carry setzen (Subtraktion)
.,A3C0 A5 5A    LDA $5A         Startadresse von Endad. des
.,A3C2 E5 5F    SBC $5F         Bereichs abziehen (LOW)
.,A3C4 85 22    STA $22         Ergebnis (=Länge) speichern
.,A3C6 A8       TAY             Gleiches System für HIGH:
.,A3C7 A5 5B    LDA $5B         Altes Blockende (HIGH) und
.,A3C9 E5 60    SBC $60         davon alter Blockanfang sub
.,A3CB AA       TAX             Länge nach X bringen
.,A3CC E8       INX             Ist ein Rest ( Länge nicht
.,A3CD 98       TYA             256 Bytes)?
.,A3CE F0 23    BEQ $A3F3       Nein: dann nur ganze Blöcke
.,A3D0 A5 5A    LDA $5A         Alte Endadresse (LOW) und
.,A3D2 38       SEC             davon Länge des Restab-
.,A3D3 E5 22    SBC $22         schnitts subtrahieren ergibt
                                Adresse des
.,A3D5 85 5A    STA $5A         Restabschnitts
.,A3D7 B0 03    BCS $A3DC       Berechnung für HIGH umgehen
.,A3D9 C6 5B    DEC $5B         Dasselbe System für HIGH
.,A3DB 38       SEC             Carry setzen (Subtraktion)
.,A3DC A5 58    LDA $58         Alte Endadresse (HIGH) und
.,A3DE E5 22    SBC $22         davon Länge des Rests sub-
.,A3E0 85 58    STA $58         trahieren ergibt neue Adresse
.,A3E2 B0 08    BCS $A3EC       Unbedingter Sprung zur
.,A3E4 C6 59    DEC $59         Kopierroutine für ganze
.,A3E6 90 04    BCC $A3EC       Blöcke
.,A3E8 B1 5A    LDA ($5A),Y     Kopierroutine für Rest-
.,A3EA 91 58    STA ($58),Y     abschnitt
.,A3EC 88       DEY             Zähler vermindern
.,A3ED D0 F9    BNE $A3E8       Alles? wenn nicht: weiter
.,A3EF B1 5A    LDA ($5A),Y     Kopierroutine für ganze
.,A3F1 91 58    STA ($58),Y     Blöcke
.,A3F3 C6 5B    DEC $5B         Adresszähler vermindern
.,A3F5 C6 59    DEC $59         Adresszähler vermindern
.,A3F7 CA       DEX             Zähler vermindern
.,A3F8 D0 F2    BNE $A3EC       Alles? Wenn nicht: weiter
.,A3FA 60       RTS             sonst Rücksprung

                                *** Prüfung auf Platz im Stapel
.,A3FB 0A       ASL             Akku muß die halbe Zahl an
.,A3FC 69 3E    ADC #$3E        erforderlichem Platz haben
.,A3FE B0 35    BCS $A435       gibt 'OUT OF MEMORY'
.,A400 85 22    STA $22         Wert merken
.,A402 BA       TSX             Ist Stapelzeiger kleiner
.,A403 E4 22    CPX $22         (2 * Akku + 62)?
.,A405 90 2E    BCC $A435       Wenn ja, dann OUT OF MEMORY
.,A407 60       RTS             Rücksprung

                                *** Schafft Platz im Speicher
.,A408 C4 34    CPY $34         für Zeileneinfügung
.,A40A 90 28    BCC $A434       und Variablen
.,A40C D0 04    BNE $A412       A/Y = Adresse, bis zu der
.,A40E C5 33    CMP $33         Platz benötigt wird.
.,A410 90 22    BCC $A434       Kleiner als Stringzeiger
.,A412 48       PHA             Akku Zwischenspeichern
.,A413 A2 09    LDX #$09        Zähler setzen
.,A415 98       TYA             Y-Register auf
.,A416 48       PHA             Stapel retten
.,A417 B5 57    LDA $57,X       Ab $57 Zwischenspeichern
.,A419 CA       DEX             Zähler vermindern
.,A41A 10 FA    BPL $A416       Alle? sonst weiter
.,A41C 20 26 B5 JSR $B526       Garbage Collection
.,A41F A2 F7    LDX #$F7        Zähler setzen, um
.,A421 68       PLA             Akku, Y-Register und andere
.,A422 95 61    STA $61,X       Register zurückholen
.,A424 E8       INX             Zähler vermindern
.,A425 30 FA    BMI $A421       Fertig? Nein, dann weiter
.,A427 68       PLA             Y-Register von Stapel
.,A428 A8       TAY             zurückholen
.,A429 68       PLA             Akku holen
.,A42A C4 34    CPY $34         Ist jetzt genügend Platz?
.,A42C 90 06    BCC $A434       Ja, dann Rücksprung
.,A42E D0 05    BNE $A435       kein Platz, dann Fehler-
.,A430 C5 33    CMP $33         meldung 1 out of memory 1
.,A432 B0 01    BCS $A435       ausgeben
.,A434 60       RTS             Rücksprung
.,A435 A2 10    LDX #$10        Fehlernummer 'out of memory'

                                *** Fehlereinsprung
.,A437 6C 00 03 JMP ($0300)     Zum BASIC-Warmstart ($E38B)

                                *** Fehlermeldung ausgeben
.,A43A 8A       TXA             Fehlernummer im X-Register
.,A43B 0A       ASL             Akku * 2
.,A43C AA       TAX             Akku als Zeiger nach X
.,A43D BD 26 A3 LDA $A326,X     und Adresse der
.,A440 85 22    STA $22         Fehlernummer aus Tabelle
.,A442 BD 27 A3 LDA $A327,X     holen und
.,A445 85 23    STA $23         abspeichern
.,A447 20 CC FF JSR $FFCC       I/O Kanäle zurücksetzen
.,A44A A9 00    LDA #$00        und Eingabekanal auf
.,A44C 85 13    STA $13         Tastatur setzen
.,A44E 20 D7 AA JSR $AAD7       (CR) und (LF) ausgeben
.,A451 20 45 AB JSR $AB45       '?' ausgeben
.,A454 A0 00    LDY #$00        Zeiger setzen
.,A456 B1 22    LDA ($22),Y     Fehlermeldungstext holen
.,A458 48       PHA             Akku retten
.,A459 29 7F    AND #$7F        Bit 7 löschen und
.,A45B 20 47 AB JSR $AB47       Fehlermeldung ausgeben
.,A45E C8       INY             Zähler vermindern
.,A45F 68       PLA             Akku zurückholen
.,A460 10 F4    BPL $A456       Fertig? Nein, dann weiter
.,A462 20 7A A6 JSR $A67A       BASIC-Zeiger initialisieren
.,A465 A9 69    LDA #$69        Zeiger A/Y auf Error-
.,A467 A0 A3    LDY #$A3        meldung stellen
.,A469 20 1E AB JSR $AB1E       String ausgeben
.,A46C A4 3A    LDY $3A         Auf Programmodus
.,A46E C8       INY             (prog/direkt) prüfen
.,A46F F0 03    BEQ $A474       Direkt: dann ausgeben
.,A471 20 C2 BD JSR $BDC2       'in Zeilennummer' ausgeben
.,A474 A9 76    LDA #$76        Zeiger auf Ready-Modus
.,A476 A0 A3    LDY #$A3        setzen und
.,A478 20 1E AB JSR $AB1E       String ausgeben
.,A47B A9 80    LDA #$80        Wert für Direktmodus laden
.,A47D 20 90 FF JSR $FF90       und Flag setzen

                                *** Eingabe-Warteschleife
.,A480 6C 02 03 JMP ($0302)     JMP $A483
.,A483 20 60 A5 JSR $A560       BASIC-Zeile nach
                                Eingabepuffer
.,A486 86 7A    STX $7A         CHRGET Zeiger auf
.,A488 84 7B    STY $7B         Eingabepuffer
.,A48A 20 73 00 JSR $0073       nächstes Zeichen holen
.,A48D AA       TAX             Puffer leer?
.,A48E F0 F0    BEQ $A480       Ja: dann weiter warten
.,A490 A2 FF    LDX #$FF        Wert für
.,A492 86 3A    STX $3A         Kennzeichen für Direktmodus
.,A494 90 06    BCC $A49C       Ziffer? als Zeile einfügen
.,A496 20 79 A5 JSR $A579       BASIC-Zeile in Code wandeln
.,A499 4C E1 A7 JMP $A7E1       Befehl ausführen

                                *** Löschen und Einfügen von
                                *** Programmzeilen
.,A49C 20 6B A9 JSR $A96B       Zeilenr. nach Adressformat
.,A49F 20 79 A5 JSR $A579       BASIC-Zeile in Code wandeln
.,A4A2 84 0B    STY $0B         Zeiger in Eingabepuffer
.,A4A4 20 13 A6 JSR $A613       Zeilenadresse berechnen
.,A4A7 90 44    BCC $A4ED       Vorhanden? Ja: löschen

                                *** Programmzeile löschen
.,A4A9 A0 01    LDY #$01        Zeiger setzen
.,A4AB B1 5F    LDA ($5F),Y     Startadresse der nächsten
.,A4AD 85 23    STA $23         Zeile (HIGH) setzen
.,A4AF A5 2D    LDA $2D         Variablenanfangszeiger
.,A4B1 85 22    STA $22         (LOW) setzen
.,A4B3 A5 60    LDA $60         Startadresse der zu
.,A4B5 85 25    STA $25         löschenden Zeile (HIGH)
.,A4B7 A5 5F    LDA $5F         Startadresse der zu
.,A4B9 88       DEY             löschenden Zeile (LOW)
.,A4BA F1 5F    SBC ($5F),Y     Startadresse der nächsten
.,A4BC 18       CLC             Zeile (LOW)
.,A4BD 65 2D    ADC $2D         Variablenanfangszeiger (LOW)
.,A4BF 85 2D    STA $2D         ergibt neuen Variablenan-
.,A4C1 85 24    STA $24         fangszeiger (LOW)
.,A4C3 A5 2E    LDA $2E         Gleiches System für
.,A4C5 69 FF    ADC #$FF        HIGH-Byte des Variablenan-
.,A4C7 85 2E    STA $2E         fangszeigers
.,A4C9 E5 60    SBC $60         minus Startadresse der zu
.,A4CB AA       TAX             löschenden Zeile (LOW) ergibt
.,A4CC 38       SEC             die zu verschiebenden Blöcke
.,A4CD A5 5F    LDA $5F         Startadresse (LOW) minus
.,A4CF E5 2D    SBC $2D         Variablenanfangszeiger (LOW)
.,A4D1 A8       TAY             ergibt Länge des Restabschn.
.,A4D2 B0 03    BCS $A4D7       Größer als 255? Nein: $A4D7
.,A4D4 E8       INX             Zähler für Blöcke erhöhen
.,A4D5 C6 25    DEC $25         Transportzeiger vermindern
.,A4D7 18       CLC             Carry löschen
.,A4D8 65 22    ADC $22         Anfangszeiger (LOW)
.,A4DA 90 03    BCC $A4DF       Verminderung überspringen
.,A4DC C6 23    DEC $23         Zeiger um 1 vermindern
.,A4DE 18       CLC             Carry löschen
.,A4DF B1 22    LDA ($22),Y     Verschiebeschleife
.,A4E1 91 24    STA ($24),Y     Wert abspeichern
.,A4E3 C8       INY             Zähler um 1 erhöhen
.,A4E4 D0 F9    BNE $A4DF       Block fertig? Nein: weiter
.,A4E6 E6 23    INC $23         1.Adreßzeiger erhöhen (LOW)
.,A4E8 E6 25    INC $25         2.Adreßzeiger erhöhen (LOW)
.,A4EA CA       DEX             Blockzähter um 1 vermindern
.,A4EB D0 F2    BNE $A4DF       Alle Blöcke? Nein: weiter

                                *** Programmzeile einfügen
.,A4ED 20 59 A6 JSR $A659       CLR-Befehl
.,A4F0 20 33 A5 JSR $A533       Programmzeilen neu binden
.,A4F3 AD 00 02 LDA $0200       Zeichen im Puffer ?
.,A4F6 F0 88    BEQ $A480       nein, dann zur Warteschleife
.,A4F8 18       CLC             Carry löschen
.,A4F9 A5 2D    LDA $2D         Variablenanfangszeiger (LOW)
.,A4FB 85 5A    STA $5A         als Endadresse (Quellbereich)
.,A4FD 65 0B    ADC $0B         + Länge der Zeile als End-
.,A4FF 85 58    STA $58         adresse des Zielbereichs LOW
.,A501 A4 2E    LDY $2E         Variablenanfangszeiger als
.,A503 84 5B    STY $5B         Endadr. des Quellbereichs LOW
.,A505 90 01    BCC $A508       Kein Übertrag? dann $A508
.,A507 C8       INY             Übertrag addieren
.,A508 84 59    STY $59         Als Endadresse
                                des Zielbereichs
.,A50A 20 B8 A3 JSR $A3B8       BASIC-Zeilen verschieben
.,A50D A5 14    LDA $14         Zeilennummer aus
.,A50F A4 15    LDY $15         $14/15 vor
.,A511 8D FE 01 STA $01FE       BASIC-Eingabepuffer setzen
.,A514 8C FF 01 STY $01FF       (ab $0200)
.,A517 A5 31    LDA $31         Neuer Variablen-
.,A519 A4 32    LDY $32         endzeiger
.,A51B 85 2D    STA $2D         als Zeiger auf Programm-
.,A51D 84 2E    STY $2E         ende speichern
.,A51F A4 0B    LDY $0B         Zeilenlänge holen
.,A521 88       DEY             und um 1 vermindern
.,A522 B9 FC 01 LDA $01FC,Y     Zeile aus Eingabepuffer
.,A525 91 5F    STA ($5F),Y     ins Programm kopieren
.,A527 88       DEY             Schon alle Zeichen?
.,A528 10 F8    BPL $A522       Nein: dann weiterkopieren
.,A52A 20 59 A6 JSR $A659       CLR-Befehl
.,A52D 20 33 A5 JSR $A533       Programmzeilen neu binden
.,A530 4C 80 A4 JMP $A480       zur Eingabe-Warteschleife

                                *** BASIC-Zeilen neu binden
.,A533 A5 2B    LDA $2B         Zeiger auf BASIC-Programm-
.,A535 A4 2C    LDY $2C         start holen und
.,A537 85 22    STA $22         und als Suchzeiger nach
.,A539 84 23    STY $23         $22/23 speichern
.,A53B 18       CLC             Carry löschen
.,A53C A0 01    LDY #$01        Zeiger laden
.,A53E B1 22    LDA ($22),Y     Zeilenadresse holen
.,A540 F0 1D    BEQ $A55F       =0? Ja: dann RTS
.,A542 A0 04    LDY #$04        Zeiger auf erstes BASIC-
.,A544 C8       INY             zeichen setzen
.,A545 B1 22    LDA ($22),Y     Zeichen holen
.,A547 D0 FB    BNE $A544       =0? (Zeilenende) nein: weiter
.,A549 C8       INY             Zeilenlänge nach
.,A54A 98       TYA             Akku schieben
.,A54B 65 22    ADC $22         + Zeiger auf aktuelle Zeile
.,A54D AA       TAX             (LOW) ins X-Register
.,A54E A0 00    LDY #$00        Zeiger laden
.,A550 91 22    STA ($22),Y     Akku als Adr.zeiger (LOW)
.,A552 A5 23    LDA $23         Zeiger auf aktuelle
                                Zeile (HIGH)
.,A554 69 00    ADC #$00        Übertrag addieren
.,A556 C8       INY             Zähler um 1 erhöhen
.,A557 91 22    STA ($22),Y     Adresszeiger (HIGH) speichern
.,A559 86 22    STX $22         Startadresse der nächsten
.,A55B 85 23    STA $23         Zeile abspeichern
.,A55D 90 DD    BCC $A53C       Zum Zeilenanfang
.,A55F 60       RTS             Rücksprung

                                *** Eingabe einer Zeile
.,A560 A2 00    LDX #$00        Zeiger setzen
.,A562 20 12 E1 JSR $E112       ein Zeichen holen
.,A565 C9 0D    CMP #$0D        RETURN-Taste ?
.,A567 F0 0D    BEQ $A576       ja, dann Eingabe beenden
.,A569 9D 00 02 STA $0200,X     Zeichen nach Eingabepuffer
.,A56C E8       INX             Zeiger um 1 erhöhen
.,A56D E0 59    CPX #$59        89. Zeichen ?
.,A56F 90 F1    BCC $A562       nein, weitere Zeichen holen
.,A571 A2 17    LDX #$17        Nummer für 'string too long'
.,A573 4C 37 A4 JMP $A437       Fehlermeldung ausgeben
.,A576 4C CA AA JMP $AACA       Puffer mit $0 abschließen, CR

                                *** Umwandlung einer Zeile in den
                                *** Interpreter-Code
.,A579 6C 04 03 JMP ($0304)     JMP $A57C
.,A57C A6 7A    LDX $7A         Zeiger setzen, erstes Zeichen
.,A57E A0 04    LDY #$04        Wert für codierte Zeile
.,A580 84 0F    STY $0F         Flag für Hochkomma
.,A582 BD 00 02 LDA $0200,X     Zeichen aus Puffer holen
.,A585 10 07    BPL $A58E       kein BASIC-Code ? kleiner 128
.,A587 C9 FF    CMP #$FF        Code für Pi ?
.,A589 F0 3E    BEQ $A5C9       Ja: dann speichern
.,A58B E8       INX             Zeiger erhöhen
.,A58C D0 F4    BNE $A582       nächstes Zeichen überprüfen
.,A58E C9 20    CMP #$20        ' ' Leerzeichen?
.,A590 F0 37    BEQ $A5C9       Ja: dann speichern
.,A592 85 08    STA $08         in Hochkomma-Flag speichern
.,A594 C9 22    CMP #$22        "'" Hochkomma?
.,A596 F0 56    BEQ $A5EE       Ja: dann speichern
.,A598 24 0F    BIT $0F         Überprüft auf Bit 6
.,A59A 70 2D    BVS $A5C9       gesetzt: ASCII speichern
.,A59C C9 3F    CMP #$3F        '?' Fragezeichen?
.,A59E D0 04    BNE $A5A4       Nein: dann weiter prüfen
.,A5A0 A9 99    LDA #$99        PRINT-Code für ? laden
.,A5A2 D0 25    BNE $A5C9       und abspeichern
.,A5A4 C9 30    CMP #$30        Kleiner $30 ? (Code für 0)
.,A5A6 90 04    BCC $A5AC       Ja: dann $A5AC
.,A5A8 C9 3C    CMP #$3C        Mit $3C vergleichen
.,A5AA 90 1D    BCC $A5C9       wenn größer, dann $A5C9
.,A5AC 84 71    STY $71         Zeiger Zwischenspeichern
.,A5AE A0 00    LDY #$00        Zähler für Tokentabelle
.,A5B0 84 0B    STY $0B         initialisieren
.,A5B2 88       DEY
.,A5B3 86 7A    STX $7A         Zeiger auf Eingabepuffer
.,A5B5 CA       DEX             zwischenspeichern
.,A5B6 C8       INY             X- und Y-Register
.,A5B7 E8       INX             um 1 erhöhen
.,A5B8 BD 00 02 LDA $0200,X     Zeichen aus Puffer laden
.,A5BB 38       SEC             Carry für Subtr. löschen
.,A5BC F9 9E A0 SBC $A09E,Y     Zeichen mit Befehlswort vergleichen
.,A5BF F0 F5    BEQ $A5B6       Gefunden? Ja: nächstes Zeich.
.,A5C1 C9 80    CMP #$80        mit $80 (128) vergleichen
.,A5C3 D0 30    BNE $A5F5       Befehl nicht gefunden: $A5F5
.,A5C5 05 0B    ORA $0B         BASIC-Code gleich Zähler +$80
.,A5C7 A4 71    LDY $71         Zeiger auf cod. Zeile holen
.,A5C9 E8       INX
.,A5CA C8       INY             Zeiger erhöhen
.,A5CB 99 FB 01 STA $01FB,Y     BASIC-Code speichern
.,A5CE B9 FB 01 LDA $01FB,Y     und Statusregister setzen
.,A5D1 F0 36    BEQ $A609       =0 (Ende): dann fertig
.,A5D3 38       SEC             Carry setzen (Subtraktion)
.,A5D4 E9 3A    SBC #$3A        ':' Trennzeichen?
.,A5D6 F0 04    BEQ $A5DC       Ja: dann $A5DC
.,A5D8 C9 49    CMP #$49        DATA-Code ?
.,A5DA D0 02    BNE $A5DE       Nein: Speichern überspringen
.,A5DC 85 0F    STA $0F         nach Hochkomma-Flag speichern
.,A5DE 38       SEC             Carry setzen
.,A5DF E9 55    SBC #$55        REM-Code ?
.,A5E1 D0 9F    BNE $A582       Nein: zum Schleifenanfang
.,A5E3 85 08    STA $08         0 in Hochkomma-Flag
.,A5E5 BD 00 02 LDA $0200,X     nächstes Zeichen holen
.,A5E8 F0 DF    BEQ $A5C9       =0 (Ende)? Ja: dann $A5C9
.,A5EA C5 08    CMP $08         Als ASCII speichern?
.,A5EC F0 DB    BEQ $A5C9       Nein: dann $A5C9
.,A5EE C8       INY             Zeiger erhöhen
.,A5EF 99 FB 01 STA $01FB,Y     Code abspeichern
.,A5F2 E8       INX             Zeiger erhöhen
.,A5F3 D0 F0    BNE $A5E5       Zum Schleifenanfang
.,A5F5 A6 7A    LDX $7A         Zeiger wieder auf Eingabep.
.,A5F7 E6 0B    INC $0B         Suchzähler erhöhen
.,A5F9 C8       INY             Zähler erhöhen
.,A5FA B9 9D A0 LDA $A09D,Y     nächsten Befehl suchen
.,A5FD 10 FA    BPL $A5F9       Gefunden? Nein: weitersuchen
.,A5FF B9 9E A0 LDA $A09E,Y     Ende der Tabelle?
.,A602 D0 B4    BNE $A5B8       Nein: dann weiter
.,A604 BD 00 02 LDA $0200,X     nächstes Zeichen holen
.,A607 10 BE    BPL $A5C7       kleiner $80? Ja: $A5C7
.,A609 99 FD 01 STA $01FD,Y     im Eingabepuffer speichern
.,A60C C6 7B    DEC $7B         CHRGET-Zeiger zurücksetzen
.,A60E A9 FF    LDA #$FF        Zeiger auf Eingabepuffer -1
.,A610 85 7A    STA $7A         setzen (LOW)
.,A612 60       RTS             Rücksprung

                                *** Startadresse einer
                                *** Programmzeile berechnen
.,A613 A5 2B    LDA $2B         Zeiger auf BASIC-
.,A615 A6 2C    LDX $2C         Programmstart laden
.,A617 A0 01    LDY #$01        Zähler setzen
.,A619 85 5F    STA $5F         BASIC-Programmstart als
.,A61B 86 60    STX $60         Zeiger nach $5F/60
.,A61D B1 5F    LDA ($5F),Y     Link-Adresse holen (HIGH)
.,A61F F0 1F    BEQ $A640       gleich null: dann Ende
.,A621 C8       INY             Zähler 2 mal erhöhen ( LOW-
.,A622 C8       INY             Byte übergehen)
.,A623 A5 15    LDA $15         gesuchte Zeilennummer (HIGH)
.,A625 D1 5F    CMP ($5F),Y     mit aktueller vergleichen
.,A627 90 18    BCC $A641       kleiner: dann nicht gefunden
.,A629 F0 03    BEQ $A62E       gleich: Nummer LOW prüfen
.,A62B 88       DEY             Zähler um 1 vermindern
.,A62C D0 09    BNE $A637       unbedingter Sprung
.,A62E A5 14    LDA $14         gesuchte Zeilennummer (LOW)
.,A630 88       DEY             Zeiger um 1 vermindern
.,A631 D1 5F    CMP ($5F),Y     Zeilennummer LOW vergleichen
.,A633 90 0C    BCC $A641       kleiner: Zeile nicht gefunden
.,A635 F0 0A    BEQ $A641       oder gleich: C=1 und RTS
.,A637 88       DEY             Y-Register auf 1 setzen
.,A638 B1 5F    LDA ($5F),Y     Adresse der nächsten Zeile
.,A63A AA       TAX             in das X-Register laden
.,A63B 88       DEY             Register vermindern (auf 0)
.,A63C B1 5F    LDA ($5F),Y     Link-Adresse holen (LOW)
.,A63E B0 D7    BCS $A617       weiter suchen
.,A640 18       CLC             Carry löschen
.,A641 60       RTS             Rücksprung

                                *** BASIC-Befehl NEW
.,A642 D0 FD    BNE $A641       Kein Trennzeichen: SYNTAX
                                ERROR
.,A644 A9 00    LDA #$00        Nullcode laden
.,A646 A8       TAY             und als Zähler ins Y-Reg.
.,A647 91 2B    STA ($2B),Y     Nullcode an Programmanfang
.,A649 C8       INY             Zähler erhöhen
.,A64A 91 2B    STA ($2B),Y     noch einen Nullcode dahinter
.,A64C A5 2B    LDA $2B         Zeiger auf Programmst. (LOW)
.,A64E 18       CLC             Carry löschen
.,A64F 69 02    ADC #$02        Programmstart + 2 ergibt
.,A651 85 2D    STA $2D         neuen Variablenstart (LOW)
.,A653 A5 2C    LDA $2C         Zeiger auf Programmst. (HIGH)
.,A655 69 00    ADC #$00        + Übertrag ergibt neuen
.,A657 85 2E    STA $2E         Variablenstart (HIGH)
.,A659 20 8E A6 JSR $A68E       CHRGET, Routine neu setzen
.,A65C A9 00    LDA #$00        Zero-Flag für CLR = 1 setzen

                                *** BASIC-Befehl CLR
.,A65E D0 2D    BNE $A68D       Kein Trennzeichen: SYNTAX
                                ERROR
.,A660 20 E7 FF JSR $FFE7       alle I/O Kanäle zurücksetzen
.,A663 A5 37    LDA $37         Zeiger auf BASIC-RAM-Ende
.,A665 A4 38    LDY $38         (LOW/HIGH) laden
.,A667 85 33    STA $33         String-Start auf BASIC-
.,A669 84 34    STY $34         RAM-Ende setzen
.,A66B A5 2D    LDA $2D         Zeiger auf Variablen-
.,A66D A4 2E    LDY $2E         start laden
.,A66F 85 2F    STA $2F         und in Array-Anfangs-
.,A671 84 30    STY $30         zeiger setzen
.,A673 85 31    STA $31         und in Zeiger auf Array-
.,A675 84 32    STY $32         Ende speichern
.,A677 20 1D A8 JSR $A81D       RESTORE-Befehl
.,A67A A2 19    LDX #$19        Wert laden und String-
.,A67C 86 16    STX $16         Descriptor-Index zurücksetzen
.,A67E 68       PLA             2 Bytes vom Stapel in das
.,A67F A8       TAY             Y-Register und den
.,A680 68       PLA             Akku holen
.,A681 A2 FA    LDX #$FA        Wert laden und damit
.,A683 9A       TXS             Stapelzeiger initialisieren
.,A684 48       PHA             2 Bytes aus dem Y-Register
.,A685 98       TYA             und dem Akku wieder auf
.,A686 48       PHA             den Stapel schieben
.,A687 A9 00    LDA #$00        Wert laden und damit
.,A689 85 3E    STA $3E         CONT sperren
.,A68B 85 10    STA $10         und in FN-Flag speichern
.,A68D 60       RTS             Rücksprung

                                *** Programmzeiger auf
                                *** BASIC-Start
.,A68E 18       CLC             Carry löschen (Addition)
.,A68F A5 2B    LDA $2B         Zeiger auf Programmstart (LOW)
.,A691 69 FF    ADC #$FF        minus 1 ergibt
.,A693 85 7A    STA $7A         neuen CHRGET-Zeiger (LOW)
.,A695 A5 2C    LDA $2C         Programmstart (HIGH)
.,A697 69 FF    ADC #$FF        minus 1 ergibt
.,A699 85 7B    STA $7B         CHRGET-Zeiger (HIGH)
.,A69B 60       RTS             Rücksprung

                                *** BASIC Befehl LIST
.,A69C 90 06    BCC $A6A4       Ziffer ? (Zeilennummer)
.,A69E F0 04    BEQ $A6A4       nur LIST ?
.,A6A0 C9 AB    CMP #$AB        Code für '-'?
.,A6A2 D0 E9    BNE $A68D       anderer Code, dann SYNTAX ERR
.,A6A4 20 6B A9 JSR $A96B       Zeilennummer holen
.,A6A7 20 13 A6 JSR $A613       Startadresse berechnen
.,A6AA 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,A6AD F0 0C    BEQ $A6BB       keine Zeilennummer
.,A6AF C9 AB    CMP #$AB        Code für '-'?
.,A6B1 D0 8E    BNE $A641       nein: SYNTAX ERROR
.,A6B3 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,A6B6 20 6B A9 JSR $A96B       Zeilennummer holen
.,A6B9 D0 86    BNE $A641       kein Trennzeichen: SYNTAX ERR
.,A6BB 68       PLA             2 Bytes von Stapel holen
.,A6BC 68       PLA             (Rücksprungadresse übergehen)
.,A6BD A5 14    LDA $14         zweite Zeilennummer laden
.,A6BF 05 15    ORA $15         gleich null ?
.,A6C1 D0 06    BNE $A6C9       Nein: $A6C9
.,A6C3 A9 FF    LDA #$FF        Wert laden und
.,A6C5 85 14    STA $14         zweite Zeilennummer Maximal-
.,A6C7 85 15    STA $15         wert $FFFF (65535)
.,A6C9 A0 01    LDY #$01        Zeiger setzen
.,A6CB 84 0F    STY $0F         und Quote Modus abschalten
.,A6CD B1 5F    LDA ($5F),Y     Linkadresse HIGH holen
.,A6CF F0 43    BEQ $A714       Ja: dann fertig
.,A6D1 20 2C A8 JSR $A82C       prüft auf Stop-Taste
.,A6D4 20 D7 AA JSR $AAD7       "CR" ausgeben, neue Zeile
.,A6D7 C8       INY             Zeiger erhöhen
.,A6D8 B1 5F    LDA ($5F),Y     Zeilenadresse holen (LOW)
.,A6DA AA       TAX             und in das X-Reg. schieben
.,A6DB C8       INY             Zeiger erhöhen
.,A6DC B1 5F    LDA ($5F),Y     Zeilenadresse holen (HIGH)
.,A6DE C5 15    CMP $15         mit Endnummer vergleichen
.,A6E0 D0 04    BNE $A6E6       Gleich? Nein: $A6E6
.,A6E2 E4 14    CPX $14         LOW-Nummer vergleichen
.,A6E4 F0 02    BEQ $A6E8       Gleich? Ja: $A6E8
.,A6E6 B0 2C    BCS $A714       Größer: dann fertig
.,A6E8 84 49    STY $49         Y-Reg. Zwischenspeichern
.,A6EA 20 CD BD JSR $BDCD       Zeilennnummer ausgeben
.,A6ED A9 20    LDA #$20        ' ' Leerzeichen
.,A6EF A4 49    LDY $49         Y-Reg. wiederholen
.,A6F1 29 7F    AND #$7F        Bit 7 löschen
.,A6F3 20 47 AB JSR $AB47       Zeichen ausgeben
.,A6F6 C9 22    CMP #$22        '"' Hochkomma ?
.,A6F8 D0 06    BNE $A700       Nein: $A700
.,A6FA A5 0F    LDA $0F         Hochkomma-Flag laden,
.,A6FC 49 FF    EOR #$FF        umdrehen (NOT)
.,A6FE 85 0F    STA $0F         und wieder abspeichern
.,A700 C8       INY             Zeilenende nach 255 Zeichen ?
.,A701 F0 11    BEQ $A714       Nein: dann aufhören
.,A703 B1 5F    LDA ($5F),Y     Zeichen holen
.,A705 D0 10    BNE $A717       kein Zeilenende, dann listen
.,A707 A8       TAY             Akku als Zeiger nach Y
.,A708 B1 5F    LDA ($5F),Y     Startadresse der nächsten
.,A70A AA       TAX             Zeile holen (LOW) und nach X
.,A70B C8       INY             Zeiger erhöhen
.,A70C B1 5F    LDA ($5F),Y     Adresse der Zeile (HIGH)
.,A70E 86 5F    STX $5F         als Zeiger merken
.,A710 85 60    STA $60         (speichern nach $5F/60) und
.,A712 D0 B5    BNE $A6C9       weitermachen
.,A714 4C 86 E3 JMP $E386       zum BASIC-Warmstart

                                *** BASIC Code in Klartext
                                *** umwandlen
.,A717 6C 06 03 JMP ($0306)     JMP $A71A
.,A71A 10 D7    BPL $A6F3       kein Interpretercode:ausgeben
.,A71C C9 FF    CMP #$FF        Code für Pi?
.,A71E F0 D3    BEQ $A6F3       Ja: so ausgeben
.,A720 24 0F    BIT $0F         Hochkommamodus ?
.,A722 30 CF    BMI $A6F3       dann Zeichen so ausgeben
.,A724 38       SEC             Carry setzen (Subtraktion)
.,A725 E9 7F    SBC #$7F        Offset abziehen
.,A727 AA       TAX             Code nach X
.,A728 84 49    STY $49         Zeichenzeiger merken
.,A72A A0 FF    LDY #$FF        Zeiger auf Befehlstabelle
.,A72C CA       DEX             erstes Befehlswort?
.,A72D F0 08    BEQ $A737       Ja: ausgeben
.,A72F C8       INY             Zeiger erhöhen
.,A730 B9 9E A0 LDA $A09E,Y     Offset für X-tes Befehlswort
.,A733 10 FA    BPL $A72F       alle Zeichen bis zum letzen
.,A735 30 F5    BMI $A72C       überlesen (Bit 7 gesetzt)
.,A737 C8       INY             Zeiger erhöhen
.,A738 B9 9E A0 LDA $A09E,Y     Befehlswort aus Tabelle holen
.,A73B 30 B2    BMI $A6EF       letzter Buchstabe: fertig
.,A73D 20 47 AB JSR $AB47       Zeichen ausgeben
.,A740 D0 F5    BNE $A737       nächsten Buchstaben ausgeben

                                *** BASIC-Befehl FOR
.,A742 A9 80    LDA #$80        Wert laden und
.,A744 85 10    STA $10         Integer sperren
.,A746 20 A5 A9 JSR $A9A5       LET, setzt FOR-Variable
.,A749 20 8A A3 JSR $A38A       sucht offene FOR-NEXT-Schlei.
.,A74C D0 05    BNE $A753       nicht gefunden: $A753
.,A74E 8A       TXA             X-Reg. nach Akku
.,A74F 69 0F    ADC #$0F        Stapelzejger erhöhen
.,A751 AA       TAX             Akku zurück nach X-Reg. und
.,A752 9A       TXS             in den Stapelzeiger
.,A753 68       PLA             Rücksprungadresse vom Stapel
.,A754 68       PLA             holen (LOW und HIGH)
.,A755 A9 09    LDA #$09        Wert für Prüfung laden
.,A757 20 FB A3 JSR $A3FB       prüft auf Platz im Stapel
.,A75A 20 06 A9 JSR $A906       sucht nächstes BAS.-Statement
.,A75D 18       CLC             Carry löschen (Addition)
.,A75E 98       TYA             CHRGET-Zeiger und Offset
.,A75F 65 7A    ADC $7A         = Startadresse der Schleife
.,A761 48       PHA             auf Stapel speichern
.,A762 A5 7B    LDA $7B         HIGH-Byte holen und
.,A764 69 00    ADC #$00        Übertrag addieren und
.,A766 48       PHA             auf den Stapel legen
.,A767 A5 3A    LDA $3A         Aktuelle
.,A769 48       PHA             Zeilennummer laden und auf
.,A76A A5 39    LDA $39         den Stapel schieben
.,A76C 48       PHA             (LOW und HIGH-Byte)
.,A76D A9 A4    LDA #$A4        'TO' - Code
.,A76F 20 FF AE JSR $AEFF       prüft auf Code
.,A772 20 8D AD JSR $AD8D       prüft ob numerische Variable
.,A775 20 8A AD JSR $AD8A       numerischer Ausdruck nach FAC
.,A778 A5 66    LDA $66         Vorzeichenbyte von FAC holen
.,A77A 09 7F    ORA #$7F        Bit 0 bis 6 setzen
.,A77C 25 62    AND $62         mit $62 angleichen
.,A77E 85 62    STA $62         und abspeichern
.,A780 A9 8B    LDA #$8B        Rücksprungadresse laden
.,A782 A0 A7    LDY #$A7        (LOW und HIGH)
.,A784 85 22    STA $22         und Zwischenspeichern
.,A786 84 23    STY $23         (LOW und HIGH)
.,A788 4C 43 AE JMP $AE43       Schleifenendwert auf Stapel
.,A78B A9 BC    LDA #$BC        Zeiger auf Konstante 1 setzen
.,A78D A0 B9    LDY #$B9        (Ersatzwert für STEP)
.,A78F 20 A2 BB JSR $BBA2       als Default-STEP-Wert in FAC
.,A792 20 79 00 JSR $0079       CHRGOT: letztes Zeichen holen
.,A795 C9 A9    CMP #$A9        'STEP' - Code?
.,A797 D0 06    BNE $A79F       kein STEP-Wert: $A79F
.,A799 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,A79C 20 8A AD JSR $AD8A       numerischer Ausdruck nach FAC
.,A79F 20 2B BC JSR $BC2B       holt Vorzeichenbyte
.,A7A2 20 38 AE JSR $AE38       Vorz. und STEP-Wert auf Stack
.,A7A5 A5 4A    LDA $4A         Zeiger auf Variablenwert
.,A7A7 48       PHA             (LOW) auf den Stapel
.,A7A8 A5 49    LDA $49         Zeiger (HIGH)
.,A7AA 48       PHA             auf den Stapel
.,A7AB A9 81    LDA #$81        und FOR-Code
.,A7AD 48       PHA             auf den Stapel legen

                                *** Interpreterschleife
.,A7AE 20 2C A8 JSR $A82C       prüft auf Stop-Taste
.,A7B1 A5 7A    LDA $7A         CHRGET Zeiger (LOW und HIGH)
.,A7B3 A4 7B    LDY $7B         laden
.,A7B5 C0 02    CPY #$02        Direkt-Modus?
.,A7B7 EA       NOP             No OPeration
.,A7B8 F0 04    BEQ $A7BE       ja: $A7BE
.,A7BA 85 3D    STA $3D         als Zeiger für CONT
.,A7BC 84 3E    STY $3E         merken
.,A7BE A0 00    LDY #$00        Zeiger setzen
.,A7C0 B1 7A    LDA ($7A),Y     laufendes Zeichen holen
.,A7C2 D0 43    BNE $A807       nicht Zeilenende?
.,A7C4 A0 02    LDY #$02        Zeiger neu setzen
.,A7C6 B1 7A    LDA ($7A),Y     Programmende?
.,A7C8 18       CLC             Flag für END setzen
.,A7C9 D0 03    BNE $A7CE       Kein Programmende: $A7CE
.,A7CB 4C 4B A8 JMP $A84B       ja: dann END ausführen
.,A7CE C8       INY             Zeiger erhöhen
.,A7CF B1 7A    LDA ($7A),Y     laufende Zeilennummer
.,A7D1 85 39    STA $39         (LOW) nach $39
.,A7D3 C8       INY             Zeiger auf nächstes Byte
.,A7D4 B1 7A    LDA ($7A),Y     laufende Zeilennummer
.,A7D6 85 3A    STA $3A         (HIGH) nach $3A
.,A7D8 98       TYA             Zeiger nach Akku
.,A7D9 65 7A    ADC $7A         Programmzeiger auf
.,A7DB 85 7A    STA $7A         Programmzeile setzen
.,A7DD 90 02    BCC $A7E1       C=0: Erhöhung umgehen
.,A7DF E6 7B    INC $7B         Programmzeiger (HIGH) erhöhen
.,A7E1 6C 08 03 JMP ($0308)     Statement ausführen
.,A7E4 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,A7E7 20 ED A7 JSR $A7ED       Statement ausführen
.,A7EA 4C AE A7 JMP $A7AE       zurück zur Interpreterschlei.

                                *** BASIC-Statement ausführen
.,A7ED F0 3C    BEQ $A82B       Zeilenende, dann fertig
.,A7EF E9 80    SBC #$80        Token?
.,A7F1 90 11    BCC $A804       nein: dann zum LET-Befehl
.,A7F3 C9 23    CMP #$23        NEW?
.,A7F5 B0 17    BCS $A80E       Funktions-Token oder GO TO
.,A7F7 0A       ASL             BASIC-Befehl, Code mal 2
.,A7F8 A8       TAY             als Zeiger ins Y-Reg.
.,A7F9 B9 0D A0 LDA $A00D,Y     Befehlsadresse (LOW und
.,A7FC 48       PHA             HIGH) aus Tabelle
.,A7FD B9 0C A0 LDA $A00C,Y     holen und als
.,A800 48       PHA             Rücksprungadresse auf Stapel
.,A801 4C 73 00 JMP $0073       Zeichen und Befehl ausführen
.,A804 4C A5 A9 JMP $A9A5       zum LET-Befehl
.,A807 C9 3A    CMP #$3A        ':' ist es Doppelpunkt?
.,A809 F0 D6    BEQ $A7E1       ja: $A7E1
.,A80B 4C 08 AF JMP $AF08       sonst 'SYNTAX ERROR'

                                *** prüft auf 'GO' 'TO' Code
.,A80E C9 4B    CMP #$4B        'GO' (minus $80)
.,A810 D0 F9    BNE $A80B       nein: 'SYNTAX ERROR'
.,A812 20 73 00 JSR $0073       nächstes Zeichen holen
.,A815 A9 A4    LDA #$A4        'TO'
.,A817 20 FF AE JSR $AEFF       prüft auf Code
.,A81A 4C A0 A8 JMP $A8A0       zum GOTO-Befehl

                                *** BASIC-Befehl RESTORE
.,A81D 38       SEC             Carry setzen (Subtraktion)
.,A81E A5 2B    LDA $2B         Programmstartzeiger (LOW)
.,A820 E9 01    SBC #$01        laden und davon 1 abziehen
.,A822 A4 2C    LDY $2C         und HIGH-Byte holen
.,A824 B0 01    BCS $A827
.,A826 88       DEY             LOW-Byte -1
.,A827 85 41    STA $41         als DATA-Zeiger
.,A829 84 42    STY $42         abspeichern
.,A82B 60       RTS             Rücksprung

                                *** prüft auf Stop-Taste
.,A82C 20 E1 FF JSR $FFE1       Stop-Taste abfragen

                                *** BASIC-Befehl STOP
.,A82F B0 01    BCS $A832       C=1: Flag für STOP

                                *** BASIC-Befehl END
.,A831 18       CLC             C=0 Flag für END
.,A832 D0 3C    BNE $A870       RUN/STOP nicht gedrückt: RTS
.,A834 A5 7A    LDA $7A         Programmzeiger laden
.,A836 A4 7B    LDY $7B         (LOW und HIGH-Byte)
.,A838 A6 3A    LDX $3A         Direkt-Modus?
.,A83A E8       INX             (Zeilennummer -1)
.,A83B F0 0C    BEQ $A849       ja: $A849
.,A83D 85 3D    STA $3D         als Zeiger für CONT setzen
.,A83F 84 3E    STY $3E         (LOW und HIGH)
.,A841 A5 39    LDA $39         Nummer der laufenden Zeile
.,A843 A4 3A    LDY $3A         holen (LOW und HIGH)
.,A845 85 3B    STA $3B         und als Zeilennummer für
.,A847 84 3C    STY $3C         CONT merken
.,A849 68       PLA             Rücksprungadresse
.,A84A 68       PLA             vom Stapel entfernen
.,A84B A9 81    LDA #$81        Zeiger auf Startadresse
.,A84D A0 A3    LDY #$A3        BREAK setzen
.,A84F 90 03    BCC $A854       END Flag?
.,A851 4C 69 A4 JMP $A469       nein: 'BREAK IN XXX' ausgeben
.,A854 4C 86 E3 JMP $E386       zum BASIC-Warmstart

                                *** BASIC-Befehl CONT
.,A857 D0 17    BNE $A870       Kein Trennzeichen: SYNTAX ERR
.,A859 A2 1A    LDX #$1A        Fehlernr. für 'CAN'T CONTINUE
.,A85B A4 3E    LDY $3E         CONT gesperrt?
.,A85D D0 03    BNE $A862       nein: $A862
.,A85F 4C 37 A4 JMP $A437       Fehlermeldung ausgeben
.,A862 A5 3D    LDA $3D         CONT-Zeiger (LOW) laden
.,A864 85 7A    STA $7A         und CONT-Zeiger als Programm-
.,A866 84 7B    STY $7B         zeiger abspeichern
.,A868 A5 3B    LDA $3B         und
.,A86A A4 3C    LDY $3C         Zeilennummer wieder
.,A86C 85 39    STA $39         setzen
.,A86E 84 3A    STY $3A         (LOW- und HIGH-Byte)
.,A870 60       RTS             Rücksprung

                                *** BASIC-Befehl RUN
.,A871 08       PHP             Statusregister retten
.,A872 A9 00    LDA #$00        Wert laden und
.,A874 20 90 FF JSR $FF90       Flag für Programmodus setzen
.,A877 28       PLP             Statusregister zurückholen
.,A878 D0 03    BNE $A87D       weitere Zeichen (Zeilennr.)?
.,A87A 4C 59 A6 JMP $A659       Programmzeiger setzen, CLR
.,A87D 20 60 A6 JSR $A660       CLR-Befehl
.,A880 4C 97 A8 JMP $A897       GOTO-Befehl

                                *** BASIC-Befehl GOSUB
.,A883 A9 03    LDA #$03        Wert für Prüfung
.,A885 20 FB A3 JSR $A3FB       prüft auf Platz im Stapel
.,A888 A5 7B    LDA $7B         Programmzeiger (LOW-
.,A88A 48       PHA             und HIGH-Byte) laden
.,A88B A5 7A    LDA $7A         und auf den
.,A88D 48       PHA             Stapel retten
.,A88E A5 3A    LDA $3A         Zeilennummer laden (HIGH)
.,A890 48       PHA             und auf den Stapel legen
.,A891 A5 39    LDA $39         Zeilennummer LOW laden
.,A893 48       PHA             und auf den Stapel legen
.,A894 A9 8D    LDA #$8D        'GOSUB'-Code laden
.,A896 48       PHA             und auf den Stapel legen
.,A897 20 79 00 JSR $0079       CHRGOT: letztes Zeichen holen
.,A89A 20 A0 A8 JSR $A8A0       GOTO-Befehl
.,A89D 4C AE A7 JMP $A7AE       zur Interpreterschleife

                                *** BASIC-Befehl GOTO
.,A8A0 20 6B A9 JSR $A96B       Zeilennummer nach $14/$15
.,A8A3 20 09 A9 JSR $A909       nächsten Zeilenanfang suchen
.,A8A6 38       SEC             Carry setzen (Subtraktion)
.,A8A7 A5 39    LDA $39         aktuelle Zeilennummer (LOW)
.,A8A9 E5 14    SBC $14         kleiner als laufende Zeile?
.,A8AB A5 3A    LDA $3A         aktuelle Zeilennummer (HIGH)
.,A8AD E5 15    SBC $15         kleiner als laufende Zeile?
.,A8AF B0 0B    BCS $A8BC       nein: $A8BC
.,A8B1 98       TYA             Differenz in Akku
.,A8B2 38       SEC             Carry setzen (Addition)
.,A8B3 65 7A    ADC $7A         Programmzeiger addieren
.,A8B5 A6 7B    LDX $7B         sucht ab laufender Zeile
.,A8B7 90 07    BCC $A8C0       unbedingter
.,A8B9 E8       INX             Sprung
.,A8BA B0 04    BCS $A8C0       zu $A8C0
.,A8BC A5 2B    LDA $2B         sucht ab Programmstart
.,A8BE A6 2C    LDX $2C
.,A8C0 20 17 A6 JSR $A617       sucht Programmzeile
.,A8C3 90 1E    BCC $A8E3       nicht gefunden: 'undef'd st.'
.,A8C5 A5 5F    LDA $5F         von der Startadresse (Zeile)
.,A8C7 E9 01    SBC #$01        eins subtrahieren und als
.,A8C9 85 7A    STA $7A         Programmzeiger (LOW)
.,A8CB A5 60    LDA $60         HIGH-Byte der Zeile laden
.,A8CD E9 00    SBC #$00        Übertrag berücksichtigen
.,A8CF 85 7B    STA $7B         und als Programmzeiger
.,A8D1 60       RTS             Rücksprung

                                *** BASIC-Befehl RETURN
.,A8D2 D0 FD    BNE $A8D1       Kein Trennzeichen: SYNTAX ERR
.,A8D4 A9 FF    LDA #$FF        Wert laden und
.,A8D6 85 4A    STA $4A         FOR-NEXT-ZEIGER neu setzen
.,A8D8 20 8A A3 JSR $A38A       GOSUB-Datensatz suchen
.,A8DB 9A       TXS
.,A8DC C9 8D    CMP #$8D        'GOSUB'-Code?
.,A8DE F0 0B    BEQ $A8EB       ja: $A8E8
.,A8E0 A2 0C    LDX #$0C        Nr für 'return without gosub’
.:A8E2 2C       .BYTE $2C       BIT-Befehl um folgenden Befehl auszulassen
.,A8E3 A2 11    LDX #$02        Nr für 'undef'd statement'
.,A8E5 4C 37 A4 JMP $A437       Fehlermeldung ausgeben
.,A8E8 4C 08 AF JMP $AF08       'syntax error' ausgeben
.,A8EB 68       PLA             GOSUB-Code vom Stapel holen
.,A8EC 68       PLA             Zeilennummer (LOW) wieder-
.,A8ED 85 39    STA $39         holen und abspeichern
.,A8EF 68       PLA             Zeilennummer (HIGH) holen
.,A8F0 85 3A    STA $3A         und abspeichern
.,A8F2 68       PLA             Programmzeiger (LOW) wieder-
.,A8F3 85 7A    STA $7A         holen und abspeichern
.,A8F5 68       PLA             Programmzeiger (HIGH) holen
.,A8F6 85 7B    STA $7B         abspeichern

                                *** BASIC-Befehl DATA
.,A8F8 20 06 A9 JSR $A906       nächstes Statement suchen
.,A8FB 98       TYA             Offset
.,A8FC 18       CLC             Carry löschen (Addition)
.,A8FD 65 7A    ADC $7A         Programmzeiger addieren
.,A8FF 85 7A    STA $7A         und wieder abspeichern
.,A901 90 02    BCC $A905       Verminderung übergehen
.,A903 E6 7B    INC $7B         Programmzeiger vermindern
.,A905 60       RTS             Rücksprung

                                *** Offset des nächsten
                                *** Trennzeichens finden
.,A906 A2 3A    LDX #$3A        ':' Doppelpunkt
.:A908 2C       .BYTE $2C
.,A909 A2 00    LDX #$00        $0 Zeilenende
.,A90B 86 07    STX $07         als Suchzeichen
.,A90D A0 00    LDY #$00        Zähler
.,A90F 84 08    STY $08         initialisieren
.,A911 A5 08    LDA $08         Speicherzelle $7
.,A913 A6 07    LDX $07         gesuchtes Zeichen
.,A915 85 07    STA $07         mit $8
.,A917 86 08    STX $08         vertauschen
.,A919 B1 7A    LDA ($7A),Y     Zeichen holen
.,A91B F0 E8    BEQ $A905       Zeilenende, dann fertig
.,A91D C5 08    CMP $08         = Suchzeichen?
.,A91F F0 E4    BEQ $A905       ja: $A905
.,A921 C8       INY             Zeiger erhöhen
.,A922 C9 22    CMP #$22        "" Hochkomma?
.,A924 D0 F3    BNE $A919       nein: $A919
.,A926 F0 E9    BEQ $A911       sonst $7 und $8 vertauschen

                                *** BASIC-Befehl IF
.,A928 20 9E AD JSR $AD9E       FRMEVL Ausdruck berechnen
.,A92B 20 79 00 JSR $0079       CHRGOT letztes Zeichen
.,A92E C9 89    CMP #$89        'GOTO'-Code?
.,A930 F0 05    BEQ $A937       ja: $A937
.,A932 A9 A7    LDA #$A7        'THEN'-Code
.,A934 20 FF AE JSR $AEFF       prüft auf Code
.,A937 A5 61    LDA $61         Ergebnis des IF-Ausdrucks
.,A939 D0 05    BNE $A940       Ausdruck wahr?

                                *** BASIC-Befehl REM
.,A93B 20 09 A9 JSR $A909       nein, Zeilenanfang suchen
.,A93E F0 BB    BEQ $A8FB       Programmz. auf nächste Zeile
.,A940 20 79 00 JSR $0079       CHRGOT: letztes Zeichen holen
.,A943 B0 03    BCS $A948       keine Ziffer?
.,A945 4C A0 A8 JMP $A8A0       zum GOTO-Befehl
.,A948 4C ED A7 JMP $A7ED       Befehl dekodieren, ausführen

                                *** BASIC-Befehl ON
.,A94B 20 9E B7 JSR $B79E       Byte-Wert (0 bis 255) holen
.,A94E 48       PHA             Code merken
.,A94F C9 8D    CMP #$8D        'GOSUB'-Code?
.,A951 F0 04    BEQ $A957       ja: $A957
.,A953 C9 89    CMP #$89        'GOTO'-Code?
.,A955 D0 91    BNE $A8E8       nein: dann 'SYNTAX ERROR'
.,A957 C6 65    DEC $65         Zähler vermindern
.,A959 D0 04    BNE $A95F       noch nicht null?
.,A95B 68       PLA             ja: Code zurückholen
.,A95C 4C EF A7 JMP $A7EF       und Befehl ausführen
.,A95F 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,A962 20 6B A9 JSR $A96B       Zeilennummer holen
.,A965 C9 2C    CMP #$2C        ',' Komma?
.,A967 F0 EE    BEQ $A957       ja: dann weiter
.,A969 68       PLA             kein Sprung: Code zurückholen
.,A96A 60       RTS             Rücksprung

                                *** Zeilennummer nach $14/$15
.,A96B A2 00    LDX #$00        Wert Laden und
.,A96D 86 14    STX $14         Vorsetzen
.,A96F 86 15    STX $15         (für Zeilennummer gleich 0)
.,A971 B0 F7    BCS $A96A       keine Ziffer, dann fertig
.,A973 E9 2F    SBC #$2F        '0'-1 abziehen, gibt Hexwert
.,A975 85 07    STA $07         merken
.,A977 A5 15    LDA $15         HIGH-Byte holen
.,A979 85 22    STA $22         Zwischenspeichern
.,A97B C9 19    CMP #$19        Zahl bereits größer 6400?
.,A97D B0 D4    BCS $A953       dann 'SYNTAX ERROR'
.,A97F A5 14    LDA $14         Zahl * 10 (= *2*2+Zahl*2)
.,A981 0A       ASL             Wert und Zwischenwert je
.,A982 26 22    ROL $22         2 mal um 1 Bit nach
.,A984 0A       ASL             links rollen
.,A985 26 22    ROL $22         (entspricht 2 * 2)
.,A987 65 14    ADC $14         plus ursprünglicher Wert
.,A989 85 14    STA $14         und abspeichern
.,A98B A5 22    LDA $22         Zwischenwert zu
.,A98D 65 15    ADC $15         zweitem Wert addieren
.,A98F 85 15    STA $15         und wieder abspeichern
.,A991 06 14    ASL $14         Speicherzelle $14 und
.,A993 26 15    ROL $15         $15 verdoppeln
.,A995 A5 14    LDA $14         Wert wieder laden
.,A997 65 07    ADC $07         und Einerziffer addieren
.,A999 85 14    STA $14         wieder speichern
.,A99B 90 02    BCC $A99F       Carry gesetzt? (Übertrag)
.,A99D E6 15    INC $15         Übertrag addieren
.,A99F 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,A9A2 4C 71 A9 JMP $A971       und weiter machen

                                *** BASIC-Befehl LET
.,A9A5 20 8B B0 JSR $B08B       sucht Variable hinter LET
.,A9A8 85 49    STA $49         und Variablenadresse
.,A9AA 84 4A    STY $4A         merken (LOW- und HIGH-Byte)
.,A9AC A9 B2    LDA #$B2        '=' - Code
.,A9AE 20 FF AE JSR $AEFF       prüft auf Code
.,A9B1 A5 0E    LDA $0E         Integer-Flag
.,A9B3 48       PHA             auf Stapel retten
.,A9B4 A5 0D    LDA $0D         und Typ-Flag
.,A9B6 48       PHA             (String/numerisch) retten
.,A9B7 20 9E AD JSR $AD9E       FRMEVL: Ausdruck holen
.,A9BA 68       PLA             Typ-Flag wiederholen
.,A9BB 2A       ROL             und Bit 7 ins Carry schieben
.,A9BC 20 90 AD JSR $AD90       auf richtigen Typ prüfen
.,A9BF D0 18    BNE $A9D9       String? ja: $A9D9
.,A9C1 68       PLA             Integer-Flag zurückholen
.,A9C2 10 12    BPL $A9D6       INTEGER? ja: $A9D6

                                *** Wertzuweisung INTEGER
.,A9C4 20 1B BC JSR $BC1B       FAC runden
.,A9C7 20 BF B1 JSR $B1BF       und nach INTEGER wandlen
.,A9CA A0 00    LDY #$00        Zeiger setzen
.,A9CC A5 64    LDA $64         HIGH-Byte holen und
.,A9CE 91 49    STA ($49),Y     Wert in Variable bringen
.,A9D0 C8       INY             Zeiger erhöhen
.,A9D1 A5 65    LDA $65         LOW-Byte holen und
.,A9D3 91 49    STA ($49),Y     Wert in Variable bringen
.,A9D5 60       RTS             Rücksprung

                                *** Wertzuweisung REAL
.,A9D6 4C D0 BB JMP $BBD0       FAC nach Variable bringen

                                *** Wertzuweisung String
.,A9D9 68       PLA             Akku vom Stapel holen
.,A9DA A4 4A    LDY $4A         Variablenadresse (HIGH) holen
.,A9DC C0 BF    CPY #$BF        ist Variable TI$?
.,A9DE D0 4C    BNE $AA2C       nein: $AA2C
.,A9E0 20 A6 B6 JSR $B6A6       FRESTR
.,A9E3 C9 06    CMP #$06        Stringlänge gleich 6
.,A9E5 D0 3D    BNE $AA24       nein: 'illegal quantity'
.,A9E7 A0 00    LDY #$00        Wert holen
.,A9E9 84 61    STY $61         und damit FAC
.,A9EB 84 66    STY $66         initialisieren
.,A9ED 84 71    STY $71         (Akku, Vorzeichen und Zeiger)
.,A9EF 20 1D AA JSR $AA1D       prüft nächstes Z. auf Ziffer
.,A9F2 20 E2 BA JSR $BAE2       FAC = FAC * 10
.,A9F5 E6 71    INC $71         Stellenzähler erhöhen
.,A9F7 A4 71    LDY $71         und ins Y-Reg. bringen
.,A9F9 20 1D AA JSR $AA1D       prüft nächstes Z. auf Ziffer
.,A9FC 20 0C BC JSR $BC0C       FAC nach ARG kopieren
.,A9FF AA       TAX             FAC gleich 0?
.,AA00 F0 05    BEQ $AA07       ja: $AA07
.,AA02 E8       INX             Exponent von FAC erhöhen
.,AA03 8A       TXA             (FAC *2) und in den Akku
.,AA04 20 ED BA JSR $BAED       FAC = FAC + ARG
.,AA07 A4 71    LDY $71         Stellenzähler
.,AA09 C8       INY             erhöhen
.,AA0A C0 06    CPY #$06        schon 6 Stellen?
.,AA0C D0 DF    BNE $A9ED       nein: nächstes Zeichen
.,AA0E 20 E2 BA JSR $BAE2       FAC = FAC * 10
.,AA11 20 9B BC JSR $BC9B       FAC rechtsbündig machen
.,AA14 A6 64    LDX $64         Werte für
.,AA16 A4 63    LDY $63         eingegebene Uhrzeit
.,AA18 A5 65    LDA $65         holen und
.,AA1A 4C DB FF JMP $FFDB       Time setzen

                                *** Zeichen auf Ziffer prüfen
.,AA1D B1 22    LDA ($22),Y     Zeichen holen (aus String)
.,AA1F 20 80 00 JSR $0080       auf Ziffer prüfen
.,AA22 90 03    BCC $AA27       Ziffer: $AA27
.,AA24 4C 48 B2 JMP $B248       sonst: 'illegal quantity'
.,AA27 E9 2F    SBC #$2F        von ASCII nach HEX umwandeln
.,AA29 4C 7E BD JMP $BD7E       in FAC und ARG übertragen

                                *** Wertzuweisung an normalen
                                *** String
.,AA2C A0 02    LDY #$02        Zeiger setzen
.,AA2E B1 64    LDA ($64),Y     Stringadresse HIGH mit
.,AA30 C5 34    CMP $34         Stringanfangsadr. vergleichen
.,AA32 90 17    BCC $AA4B       kleiner: String im Programm
.,AA34 D0 07    BNE $AA3D       größer: $AA3D
.,AA36 88       DEY             Zeiger vermindern
.,AA37 B1 64    LDA ($64),Y     Stringadresse (LOW) holen
.,AA39 C5 33    CMP $33         und vergleichen
.,AA3B 90 0E    BCC $AA4B       kleiner: String im Programm
.,AA3D A4 65    LDY $65         Zeiger auf Stringdescriptor
.,AA3F C4 2E    CPY $2E         mit Variablenstart vergl.
.,AA41 90 08    BCC $AA4B       kleiner: $AA4B
.,AA43 D0 0D    BNE $AA52       größer: $AA52
.,AA45 A5 64    LDA $64         Stringdiscriptorzeiger (LOW)
.,AA47 C5 2D    CMP $2D         mit Variablenstart vergl.
.,AA49 B0 07    BCS $AA52       größer: $AA52
.,AA4B A5 64    LDA $64         Zeiger in Akku und Y-Reg.
.,AA4D A4 65    LDY $65         auf Stringdescriptor setzen
.,AA4F 4C 68 AA JMP $AA68       bis $AA68 überspringen
.,AA52 A0 00    LDY #$00        Zeiger setzen
.,AA54 B1 64    LDA ($64),Y     Länge des Strings holen
.,AA56 20 75 B4 JSR $B475       prüft Platz, setzt Stringz.
.,AA59 A5 50    LDA $50         Zeiger auf Stringdescriptor
.,AA5B A4 51    LDY $51         holen (LOW- und HIGH-Byte)
.,AA5D 85 6F    STA $6F         und
.,AA5F 84 70    STY $70         speichern
.,AA61 20 7A B6 JSR $B67A       String in Bereich übertragen
.,AA64 A9 61    LDA #$61        Werte laden
.,AA66 A0 00    LDY #$00        und damit
.,AA68 85 50    STA $50         Stringdiscriptor
.,AA6A 84 51    STY $51         neu setzen
.,AA6C 20 DB B6 JSR $B6DB       Descriptor löschen
.,AA6F A0 00    LDY #$00        Zeiger setzen
.,AA71 B1 50    LDA ($50),Y     Länge des Descriptors holen
.,AA73 91 49    STA ($49),Y     und abspeichern
.,AA75 C8       INY             Zeiger erhöhen
.,AA76 B1 50    LDA ($50),Y     Adresse (LOW) holen
.,AA78 91 49    STA ($49),Y     und speichern
.,AA7A C8       INY             Zeiger erhöhen
.,AA7B B1 50    LDA ($50),Y     und Adresse (HIGH)
.,AA7D 91 49    STA ($49),Y     in Variable bringen
.,AA7F 60       RTS             Rücksprung

                                *** BASIC-Befehl PRINT#
.,AA80 20 86 AA JSR $AA86       CMD-Befehl
.,AA83 4C B5 AB JMP $ABB5       und CLRCH

                                *** BASIC-Befehl CMD
.,AA86 20 9E B7 JSR $B79E       holt Byte-Ausdruck
.,AA89 F0 05    BEQ $AA90       Trennzeichen: $AA90
.,AA8B A9 2C    LDA #$2C        ',', Wert laden
.,AA8D 20 FF AE JSR $AEFF       prüft auf Komma
.,AA90 08       PHP             Statusregister merken
.,AA91 86 13    STX $13         Nr. des Ausgabegeräts merken
.,AA93 20 18 E1 JSR $E118       CKOUT, Ausgabegerät setzen
.,AA96 28       PLP             Statusregister wiederholen
.,AA97 4C A0 AA JMP $AAA0       zum PRINT-Befehl
.,AA9A 20 21 AB JSR $AB21       String drucken
.,AA9D 20 79 00 JSR $0079       CHRGOT letztes Zeichen

                                *** BASIC-Befehl PRINT
.,AAA0 F0 35    BEQ $AAD7       Trennzeichen: $AAD7
.,AAA2 F0 43    BEQ $AAE7       Trennz. (TAB, SPC): RTS
.,AAA4 C9 A3    CMP #$A3        'TAB('-Code?
.,AAA6 F0 50    BEQ $AAF8       ja: $AAF8
.,AAA8 C9 A6    CMP #$A6        'SPC('-Code?
.,AAAA 18       CLC             Flag für SPC setzen
.,AAAB F0 4B    BEQ $AAF8       SPC-Code: $AAF8
.,AAAD C9 2C    CMP #$2C        ','-Code? (Komma)
.,AAAF F0 37    BEQ $AAE8       ja: $AAE8
.,AAB1 C9 3B    CMP #$3B        ';'-Code? (Semikolon)
.,AAB3 F0 5E    BEQ $AB13       ja: nächstes Zeichen, weiter
.,AAB5 20 9E AD JSR $AD9E       FRMEVL: Term holen
.,AAB8 24 0D    BIT $0D         Typflag
.,AABA 30 DE    BMI $AA9A       String?
.,AABC 20 DD BD JSR $BDDD       FAC in ASCII-String wandeln
.,AABF 20 87 B4 JSR $B487       Stringparameter holen
.,AAC2 20 21 AB JSR $AB21       String drucken
.,AAC5 20 3B AB JSR $AB3B       Cursor right bzw. Leerzeichen
.,AAC8 D0 D3    BNE $AA9D       weiter machen
.,AACA A9 00    LDA #$00        Eingabepuffer
.,AACC 9D 00 02 STA $0200,X     mit $0 abschließen
.,AACF A2 FF    LDX #$FF        Zeiger auf
.,AAD1 A0 01    LDY #$01        Eingabepuffer ab $0200 setzen
.,AAD3 A5 13    LDA $13         Nummer des Ausgabegeräts
.,AAD5 D0 10    BNE $AAE7       Tastatur? nein: RTS
.,AAD7 A9 0D    LDA #$0D        'CR' carriage return
.,AAD9 20 47 AB JSR $AB47       ausgeben
.,AADC 24 13    BIT $13         logische Filenummer
.,AADE 10 05    BPL $AAE5       kleiner 128?
.,AAE0 A9 0A    LDA #$0A        'LF' line feed
.,AAE2 20 47 AB JSR $AB47       ausgeben
.,AAE5 49 FF    EOR #$FF        NOT
.,AAE7 60       RTS             Rücksprung
.,AAE8 38       SEC             Zehner-Tabulator mit Komma
.,AAE9 20 F0 FF JSR $FFF0       Cursorposition holen
.,AAEC 98       TYA             Spalte ins Y-Reg.
.,AAED 38       SEC             Carry setzen (Subtr.)
.,AAEE E9 0A    SBC #$0A        10 abziehen
.,AAF0 B0 FC    BCS $AAEE       nicht negativ?
.,AAF2 49 FF    EOR #$FF        invertieren
.,AAF4 69 01    ADC #$01        +1 (Zweierkomplement)
.,AAF6 D0 16    BNE $AB0E       unbedingter Sprung

                                *** TAB( (C=1) und SPC( (C=0)
.,AAF8 08       PHP             Flags merken
.,AAF9 38       SEC             Carry setzen
.,AAFA 20 F0 FF JSR $FFF0       Cursorposition holen
.,AAFD 84 09    STY $09         und Spalte merken
.,AAFF 20 9B B7 JSR $B79B       Byte-Wert holen
.,AB02 C9 29    CMP #$29        ')' Klammer zu?
.,AB04 D0 59    BNE $AB5F       nein: 'SYNTAX ERROR'
.,AB06 28       PLP             Flags wiederherstellen
.,AB07 90 06    BCC $AB0F       zu SPC(
.,AB09 8A       TXA             TAB-Wert in Akku
.,AB0A E5 09    SBC $09         mit Cursorspalte vergleichen
.,AB0C 90 05    BCC $AB13       kleiner Cursor-Position: RTS
.,AB0E AA       TAX             Schritte bis zum Tabulator
.,AB0F E8       INX             aus Zähler initialisieren
.,AB10 CA       DEX             um 1 vermindern
.,AB11 D0 06    BNE $AB19       =0? nein: Cursor right
.,AB13 20 73 00 JSR $0073       nächstes Zeichen holen
.,AB16 4C A2 AA JMP $AAA2       und weitermachen
.,AB19 20 3B AB JSR $AB3B       Cursor right bzw. Leerzeichen
.,AB1C D0 F2    BNE $AB10       zum Schleifenanfang

                                *** String ausgeben
.,AB1E 20 87 B4 JSR $B487       Stringparameter holen
.,AB21 20 A6 B6 JSR $B6A6       FRESTR
.,AB24 AA       TAX             Stringlänge
.,AB25 A0 00    LDY #$00        Zeiger für Stringausgabe
.,AB27 E8       INX             erhöhen
.,AB28 CA       DEX             vermindern
.,AB29 F0 BC    BEQ $AAE7       String zu Ende?
.,AB2B B1 22    LDA ($22),Y     Zeichen des Strings
.,AB2D 20 47 AB JSR $AB47       ausgeben
.,AB30 C8       INY             Zeiger erhöhen
.,AB31 C9 0D    CMP #$0D        'CR' carriage return?
.,AB33 D0 F3    BNE $AB28       nein: weiter
.,AB35 20 E5 AA JSR $AAE5       Fehler ! Test auf LF-Ausgabe
.,AB38 4C 28 AB JMP $AB28       und weitermachen

                                *** Ausgabe eines Leerzeichens
                                *** bzw. Cursor right
.,AB3B A5 13    LDA $13         Ausgabe in File?
.,AB3D F0 03    BEQ $AB42       Bildschirm: dann Cursor right
.,AB3F A9 20    LDA #$20        ' ' Leerzeichencode laden
.:AB41 2C       .BYTE $2C
.,AB42 A9 1D    LDA #$1D        Cursor right Code laden
.:AB44 2C       .BYTE $2C
.,AB45 A9 3F    LDA #$3F        '?' Fragezeichencode laden
.,AB47 20 0C E1 JSR $E10C       Code ausgeben
.,AB4A 29 FF    AND #$FF        Flags setzen
.,AB4C 60       RTS             Rücksprung

                                *** Fehlerbehandlung bei Eingabe
.,AB4D A5 11    LDA $11         Flag für INPUT / GET / READ
.,AB4F F0 11    BEQ $AB62       INPUT: $AB62
.,AB51 30 04    BMI $AB57       READ: $AB57
.,AB53 A0 FF    LDY #$FF        GET:
.,AB55 D0 04    BNE $AB5B       unbedingter Sprung

                                *** Fehler bei READ
.,AB57 A5 3F    LDA $3F         DATA-Zeilennummer
.,AB59 A4 40    LDY $40         holen (LOW- und HIGH-Byte)

                                *** Fehler bei GET
.,AB5B 85 39    STA $39         gleiche Zeilennummer
.,AB5D 84 3A    STY $3A         des Fehlers
.,AB5F 4C 08 AF JMP $AF08       'SYNTAX ERROR'

                                *** Fehler bei INPUT
.,AB62 A5 13    LDA $13         Nummer des Eingabegeräts
.,AB64 F0 05    BEQ $AB6B       Tastatur: 'REDO FROM START'
.,AB66 A2 18    LDX #$18        Nummer für 'FILE DATA'
.,AB68 4C 37 A4 JMP $A437       Fehlermeldung ausgeben
.,AB6B A9 0C    LDA #$0C        Zeiger in Akku und Y-Reg.
.,AB6D A0 AD    LDY #$AD        auf '?REDO FROM START'
.,AB6F 20 1E AB JSR $AB1E       String ausgeben
.,AB72 A5 3D    LDA $3D         Werte holen und
.,AB74 A4 3E    LDY $3E         Programmzeiger
.,AB76 85 7A    STA $7A         zurücksetzen
.,AB78 84 7B    STY $7B         auf INPUT-Befehl
.,AB7A 60       RTS             Rücksprung

                                *** BASIC-Befehl GET
.,AB7B 20 A6 B3 JSR $B3A6       Testet auf Direkt-Modus
.,AB7E C9 23    CMP #$23        folgt '#’?
.,AB80 D0 10    BNE $AB92       nein: $AB92
.,AB82 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,AB85 20 9E B7 JSR $B79E       Byte-Wert holen
.,AB88 A9 2C    LDA #$2C        ',' Komma
.,AB8A 20 FF AE JSR $AEFF       prüft auf Code
.,AB8D 86 13    STX $13         Filenummer
.,AB8F 20 1E E1 JSR $E11E       CHKIN, Eingabe vorbereiten
.,AB92 A2 01    LDX #$01        Zeiger auf
.,AB94 A0 02    LDY #$02        Pufferende = $201 ein Zeichen
.,AB96 A9 00    LDA #$00        Wert laden und
.,AB98 8D 01 02 STA $0201       Puffer mit $0 abschließen
.,AB9B A9 40    LDA #$40        GET-Flag
.,AB9D 20 0F AC JSR $AC0F       Wertzuweisung an Variable
.,ABA0 A6 13    LDX $13         Eingabegerät
.,ABA2 D0 13    BNE $ABB7       nicht Tastatur, dann CLRCH
.,ABA4 60       RTS             Rücksprung

                                *** BASIC-Befehl INPUT#
.,ABA5 20 9E B7 JSR $B79E       holt Byte-Wert
.,ABA8 A9 2C    LDA #$2C        ',' Code für Komma
.,ABAA 20 FF AE JSR $AEFF       prüft auf Komma
.,ABAD 86 13    STX $13         Eingabegerät
.,ABAF 20 1E E1 JSR $E11E       CHKIN, Eingabe vorbereiten
.,ABB2 20 CE AB JSR $ABCE       INPUT ohne Dialogstring
.,ABB5 A5 13    LDA $13         Eingabegerät im Akku
.,ABB7 20 CC FF JSR $FFCC       setzt Eingabegerät zurück
.,ABBA A2 00    LDX #$00        Wert laden und
.,ABBC 86 13    STX $13         Eingabegerät wieder Tastatur
.,ABBE 60       RTS             Rücksprung

                                *** BASIC-Befehl INPUT
.,ABBF C9 22    CMP #$22        '"' Hochkomma?
.,ABC1 D0 0B    BNE $ABCE       nein: $ABDE
.,ABC3 20 BD AE JSR $AEBD       Dialogstring holen
.,ABC6 A9 3B    LDA #$3B        ';' Semikolon
.,ABC8 20 FF AE JSR $AEFF       prüft auf Code
.,ABCB 20 21 AB JSR $AB21       String ausgeben
.,ABCE 20 A6 B3 JSR $B3A6       prüft auf Direkt-Modus
.,ABD1 A9 2C    LDA #$2C        ',' Komma
.,ABD3 8D FF 01 STA $01FF       an Pufferstart
.,ABD6 20 F9 AB JSR $ABF9       Fragezeichen ausgeben
.,ABD9 A5 13    LDA $13         Nummer des Eingabegeräts
.,ABDB F0 0D    BEQ $ABEA       Tastatur? ja: $ABEA
.,ABDD 20 B7 FF JSR $FFB7       Status holen
.,ABE0 29 02    AND #$02        Bit 1 isolieren (Tineout R.)
.,ABE2 F0 06    BEQ $ABEA       Time-out?
.,ABE4 20 B5 AB JSR $ABB5       ja: CLRCH,Tastatur aktivieren
.,ABE7 4C F8 A8 JMP $A8F8       nächstes Statement ausführen
.,ABEA AD 00 02 LDA $0200       erstes Zeichen holen
.,ABED D0 1E    BNE $AC0D       Ende?
.,ABEF A5 13    LDA $13         ja: Eingabegerät
.,ABF1 D0 E3    BNE $ABD6       nicht Tastatur: $ABD6
.,ABF3 20 06 A9 JSR $A906       Offset (Statement) suchen
.,ABF6 4C FB A8 JMP $A8FB       Programmzeiger auf Statement
.,ABF9 A5 13    LDA $13         Eingabegerät holen
.,ABFB D0 06    BNE $AC03       nicht Tastatur: $AC03
.,ABFD 20 45 AB JSR $AB45       '?' ausgeben
.,AC00 20 3B AB JSR $AB3B       ' ' Leerzeichen ausgeben
.,AC03 4C 60 A5 JMP $A560       Eingabezeile holen

                                *** BASIC-Befehl READ
.,AC06 A6 41    LDX $41         DATA-Zeiger nach
.,AC08 A4 42    LDY $42         $41/42 holen
.,AC0A A9 98    LDA #$98        READ-Flag
.:AC0C 2C       .BYTE $2C
.,AC0D A9 00    LDA #$00        Flagwert laden
.,AC0F 85 11    STA $11         und INPUT-Zeiger setzen
.,AC11 86 43    STX $43         INPUT-Zeiger auf
.,AC13 84 44    STY $44         Eingabequelle setzen
.,AC15 20 8B B0 JSR $B08B       sucht Variable
.,AC18 85 49    STA $49         Vari ablenadresse
.,AC1A 84 4A    STY $4A         speichern
.,AC1C A5 7A    LDA $7A         LOW- und HIGH-Byte des
.,AC1E A4 7B    LDY $7B         Programmzeigers
.,AC20 85 4B    STA $4B         in $4B/$4C
.,AC22 84 4C    STY $4C         Zwischenspeichern
.,AC24 A6 43    LDX $43         INPUT-Zeiger
.,AC26 A4 44    LDY $44         (LOW und HIGH)
.,AC28 86 7A    STX $7A         als Programmzeiger
.,AC2A 84 7B    STY $7B         abspeichern
.,AC2C 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,AC2F D0 20    BNE $AC51       Endzeichen? nein: $AC51
.,AC31 24 11    BIT $11         Eingabeflag
.,AC33 50 0C    BVC $AC41       kein GET: $AC41
.,AC35 20 24 E1 JSR $E124       GETIN
.,AC38 8D 00 02 STA $0200       Zeichen in Puffer schreiben
.,AC3B A2 FF    LDX #$FF        Zeiger auf
.,AC3D A0 01    LDY #$01        Puffer setzen
.,AC3F D0 0C    BNE $AC4D       unbedingter Sprung
.,AC41 30 75    BMI $ACB8       READ: $ACB8
.,AC43 A5 13    LDA $13         Eingabegerät holen
.,AC45 D0 03    BNE $AC4A       nicht Tastatur: $AC4A
.,AC47 20 45 AB JSR $AB45       Fragezeichen ausgeben
.,AC4A 20 F9 AB JSR $ABF9       zweites Fragezeichen ausgeben
.,AC4D 86 7A    STX $7A         Programmzeiger setzen
.,AC4F 84 7B    STY $7B         (LOW und HIGH)
.,AC51 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,AC54 24 0D    BIT $0D         Typ-Flag
.,AC56 10 31    BPL $AC89       kein String: $AC89
.,AC58 24 11    BIT $11         Eingabeflag
.,AC5A 50 09    BVC $AC65       kein GET: $AC65
.,AC5C E8       INX             Programmzeiger erhöhen
.,AC5D 86 7A    STX $7A         und neu setzen ($0200)
.,AC5F A9 00    LDA #$00        Wert laden und
.,AC61 85 07    STA $07         Trennzeichen setzen
.,AC63 F0 0C    BEQ $AC71       unbedingter Sprung
.,AC65 85 07    STA $07         nächstes Zeichen
.,AC67 C9 22    CMP #$22        '"' Hochkomma?
.,AC69 F0 07    BEQ $AC72       ja: $AC72
.,AC6B A9 3A    LDA #$3A        ':' Doppelpunktcode laden
.,AC6D 85 07    STA $07         und abspeichern
.,AC6F A9 2C    LDA #$2C        ',' Kommacode (Endzeichen
.,AC71 18       CLC             für Stringübertragung)
.,AC72 85 08    STA $08         abspeichern
.,AC74 A5 7A    LDA $7A         Programmzeiger laden
.,AC76 A4 7B    LDY $7B         (LOW und HIGH)
.,AC78 69 00    ADC #$00        und Übertrag addieren
.,AC7A 90 01    BCC $AC7D       C = 0: $AC7D
.,AC7C C8       INY             bei "'" um 1 erhöhen
.,AC7D 20 8D B4 JSR $B48D       String übernehmen
.,AC80 20 E2 B7 JSR $B7E2       Programmzeiger hinter String
.,AC83 20 DA A9 JSR $A9DA       String an Variable zuweisen
.,AC86 4C 91 AC JMP $AC91       weiter machen
.,AC89 20 F3 BC JSR $BCF3       Ziffernstring in FAC holen
.,AC8C A5 0E    LDA $0E         INTEGER/REAL-Flag
.,AC8E 20 C2 A9 JSR $A9C2       FAC an numerische Variable
.,AC91 20 79 00 JSR $0079       CHRGOT: letztes Zeichen holen
.,AC94 F0 07    BEQ $AC9D       Ende?
.,AC96 C9 2C    CMP #$2C        ',' Code?
.,AC98 F0 03    BEQ $AC9D       ja: $AC9D
.,AC9A 4C 4D AB JMP $AB4D       zur Fehlerbehandlung
.,AC9D A5 7A    LDA $7A         Programmzeiger
.,AC9F A4 7B    LDY $7B         holen und
.,ACA1 85 43    STA $43         in DATA-Zeiger
.,ACA3 84 44    STY $44         abspeichern
.,ACA5 A5 4B    LDA $4B         ursprüngliche
.,ACA7 A4 4C    LDY $4C         Programmzeiger
.,ACA9 85 7A    STA $7A         wieder zurückholen
.,ACAB 84 7B    STY $7B         und speichern
.,ACAD 20 79 00 JSR $0079       CHRGOT: letztes Zeichen holen
.,ACB0 F0 2D    BEQ $ACDF       Trennzeichen: $ACDF
.,ACB2 20 FD AE JSR $AEFD       CKCOM: prüft auf Komma
.,ACB5 4C 15 AC JMP $AC15       weiter
.,ACB8 20 06 A9 JSR $A906       nächstes Statement suchen
.,ACBB C8       INY             Offset erhöhen
.,ACBC AA       TAX             Zeilenende?
.,ACBD D0 12    BNE $ACD1       nein: $ACD1
.,ACBF A2 0D    LDX #$0D        'OUT OF DATA' Code
.,ACC1 C8       INY             Zeiger erhöhen
.,ACC2 B1 7A    LDA ($7A),Y     Programmende?
.,ACC4 F0 6C    BEQ $AD32       ja: 'OUT OF DATA', X = 0
.,ACC6 C8       INY             Zeiger erhöhen
.,ACC7 B1 7A    LDA ($7A),Y     Zeilennummer (LOW) holen
.,ACC9 85 3F    STA $3F         und abspeichern
.,ACCB C8       INY             Zeiger erhöhen
.,ACCC B1 7A    LDA ($7A),Y     Zeilenummer (HIGH)
.,ACCE C8       INY             Zeiger erhöhen
.,ACCF 85 40    STA $40         Zeilennummer speichern
.,ACD1 20 FB A8 JSR $A8FB       Programmz. auf Statement
.,ACD4 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,ACD7 AA       TAX             und ins X-Reg.
.,ACD8 E0 83    CPX #$83        'DATA' Code?
.,ACDA D0 DC    BNE $ACB8       nein: weitersuchen
.,ACDC 4C 51 AC JMP $AC51       Daten lesen
.,ACDF A5 43    LDA $43         LOW- und HIGH-Byte des
.,ACE1 A4 44    LDY $44         Input-Zeigers
.,ACE3 A6 11    LDX $11         Eingabe-Flag
.,ACE5 10 03    BPL $ACEA       kein DATA: $ACEA
.,ACE7 4C 27 A8 JMP $A827       DATA-Zeiger setzen
.,ACEA A0 00    LDY #$00        Zeiger setzen
.,ACEC B1 43    LDA ($43),Y     nächstes Zeichen holen
.,ACEE F0 0B    BEQ $ACFB       Endzeichen: $ACFB
.,ACF0 A5 13    LDA $13         Eingabe über Tastatur?
.,ACF2 D0 07    BNE $ACFB       nein: $ACFB
.,ACF4 A9 FC    LDA #$FC        Zeiger auf
.,ACF6 A0 AC    LDY #$AC        '?extra ignored' setzen
.,ACF8 4C 1E AB JMP $AB1E       String ausgeben
.,ACFB 60       RTS             Rücksprung

.:ACFC 3F 45 58 54 52 41 20 49  '?extra ignored'
.:AD04 47 4E 4F 52 45 44 0D 00
.:AD0C 3F 52 45 44 4F 20 46 52  '?redo from start'
.:AD14 4F 4D 20 53 54 41 52 54
.:AD1C 0D 00

                                *** BASIC-Befehl NEXT
.,AD1E D0 04    BNE $AD24       folgt Variablenname? ja:$AD24
.,AD20 A0 00    LDY #$00        Variablenzeiger = 0
.,AD22 F0 03    BEQ $AD27       unbedingter Sprung
.,AD24 20 8B B0 JSR $B08B       sucht Variable
.,AD27 85 49    STA $49         Adresse der
.,AD29 84 4A    STY $4A         Variablen speichern
.,AD2B 20 8A A3 JSR $A38A       sucht FOR-NEXT-Schleife
.,AD2E F0 05    BEQ $AD35       gefunden: $AD35
.,AD30 A2 0A    LDX #$0A        Nummer für 'next without for'
.,AD32 4C 37 A4 JMP $A437       Fehlermeldung ausgeben
.,AD35 9A       TXS             X-Reg. retten
.,AD36 8A       TXA             X-Register nach Akku
.,AD37 18       CLC             Carry löschen (Addition)
.,AD38 69 04    ADC #$04        Zeiger auf Exponenten des
.,AD3A 48       PHA             STEP-Wert + 4 und retten
.,AD3B 69 06    ADC #$06        Zeiger auf Exponent des TO-
.,AD3D 85 24    STA $24         Wert und retten
.,AD3F 68       PLA             Akku wieder vom Stapel holen
.,AD40 A0 01    LDY #$01        Zeiger für Konstante setzen
.,AD42 20 A2 BB JSR $BBA2       Variable vom Stapel nach FAC
.,AD45 BA       TSX             Stapelzeiger als Zeiger h.
.,AD46 BD 09 01 LDA $0109,X     Vorzeichenbyte holen und
.,AD49 85 66    STA $66         für FAC speichern
.,AD4B A5 49    LDA $49         Variablenadresse für
.,AD4D A4 4A    LDY $4A         FOR-NEXT holen
.,AD4F 20 67 B8 JSR $B867       addiert STEP-Wert zu FAC
.,AD52 20 D0 BB JSR $BBD0       FAC nach Variable bringen
.,AD55 A0 01    LDY #$01        Zeiger auf Konstante setzen
.,AD57 20 5D BC JSR $BC5D       FAC mit Schleifenendwert vergleichen
.,AD5A BA       TSX             Stapelzeiger als Zeiger h.
.,AD5B 38       SEC             Carry setzen (Subtraktion)
.,AD5C FD 09 01 SBC $0109,X     Stapelwert größer?
.,AD5F F0 17    BEQ $AD78       ja: Schleife verlassen
.,AD61 BD 0F 01 LDA $010F,X     Zeilennummer des Schleifen-
.,AD64 85 39    STA $39         anfangs holen (LOW- und
.,AD66 BD 10 01 LDA $0110,X     HIGH-Byte) und als aktuelle
.,AD69 85 3A    STA $3A         BASIC-Zeilennummer speichern
.,AD6B BD 12 01 LDA $0112,X     Schleifenanfang holen (LOW-
.,AD6E 85 7A    STA $7A         und HIGH-Byte) und
.,AD70 BD 11 01 LDA $0111,X     als neuen Programmzeiger
.,AD73 85 7B    STA $7B         abspeichern
.,AD75 4C AE A7 JMP $A7AE       zur Interpreterschleife
.,AD78 8A       TXA             Zeiger in Akku holen
.,AD79 69 11    ADC #$11        (Werte der Schleife aus
.,AD7B AA       TAX             Stapel entfernen)
.,AD7C 9A       TXS             neuen Stapelzeiger setzen
.,AD7D 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,AD80 C9 2C    CMP #$2C        ',' Komma?
.,AD82 D0 F1    BNE $AD75       nein: dann fertig
.,AD84 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,AD87 20 24 AD JSR $AD24       nächste NEXT-Variable

                                *** FRMNUM Ausdruck holen und
                                *** auf numerisch prüfen
.,AD8A 20 9E AD JSR $AD9E       FRMEVL Term holen

                                *** prüft auf numerisch
.,AD8D 18       CLC             Flag für Test auf numerisch
.:AD8E 24       .BYTE $24       BIT-Befehl um folgenden Befehl auszulassen

                                *** prüft auf String
.,AD8F 38       SEC             Flag für Test auf String
.,AD90 24 0D    BIT $0D         Typflag testen
.,AD92 30 03    BMI $AD97       gesetzt: $AD97
.,AD94 B0 03    BCS $AD99       C=1: 'TYPE MISMATCH'
.,AD96 60       RTS             Rücksprung
.,AD97 B0 FD    BCS $AD96       C=1: RTS
.,AD99 A2 16    LDX #$16        Nummer für 'TYPE MISMATCH'
.,AD9B 4C 37 A4 JMP $A437       Fehlermeldung ausgeben

                                *** FRMEVL auswerten eines
                                *** beliebigen Ausdrucks
.,AD9E A6 7A    LDX $7A         Programmzeiger (LOW) = 0?
.,ADA0 D0 02    BNE $ADA4       ja: HIGH-B. nicht vermindern
.,ADA2 C6 7B    DEC $7B         HIGH-Byte vermindern
.,ADA4 C6 7A    DEC $7A         LOW-Byte vermindern
.,ADA6 A2 00    LDX #$00        Prioritätswert laden
.:ADA8 24       .BYTE $24
.,ADA9 48       PHA             Operatormaske retten
.,ADAA 8A       TXA             Prioritätswert in Akku
.,ADAB 48       PHA             schieben und retten
.,ADAC A9 01    LDA #$01        2 Bytes
.,ADAE 20 FB A3 JSR $A3FB       prüft auf Platz im Stapel
.,ADB1 20 83 AE JSR $AE83       Nächstes Element holen
.,ADB4 A9 00    LDA #$00        Wert laden und
.,ADB6 85 4D    STA $4D         Maske für Vergleichsoperator
.,ADB8 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,ADBB 38       SEC             Carry setzen (Subtraktion)
.,ADBC E9 B1    SBC #$B1        $B1 von Operatorcode subtr.
.,ADBE 90 17    BCC $ADD7       C=0: $ADD7
.,ADC0 C9 03    CMP #$03        mit $3 vergleichen
.,ADC2 B0 13    BCS $ADD7       =3: $ADD7
.,ADC4 C9 01    CMP #$01
.,ADC6 2A       ROL             Maske für kleiner
.,ADC7 49 01    EOR #$01        gleich und größer
.,ADC9 45 4D    EOR $4D         für Bits 0,1 und 2
.,ADCB C5 4D    CMP $4D         in $40 erstellen
.,ADCD 90 61    BCC $AE30       (Wenn Codes von 177
.,ADCF 85 4D    STA $4D         bis 179 folgen)
.,ADD1 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,ADD4 4C BB AD JMP $ADBB       nächstes Zeichen auswerten
.,ADD7 A6 4D    LDX $4D         Operatormaske holen
.,ADD9 D0 2C    BNE $AE07       gleich 0? nein: $AE07
.,ADDB B0 7B    BCS $AE58       Code größer oder gleich 180?
.,ADDD 69 07    ADC #$07        Code kleiner 170?
.,ADDF 90 77    BCC $AE58       ja: $AE58
.,ADE1 65 0D    ADC $0D         Stringaddition?
.,ADE3 D0 03    BNE $ADE8       nein: Verkettung umgehen
.,ADE5 4C 3D B6 JMP $B63D       Stringverkettung
.,ADE8 69 FF    ADC #$FF        Code-$AA (wiederherstellen)
.,ADEA 85 22    STA $22         und speichern
.,ADEC 0A       ASL             verdoppeln
.,ADED 65 22    ADC $22         + Wert (also mal 3)
.,ADEF A8       TAY             als Zeiger ins Y-Register
.,ADF0 68       PLA             bisheriger Prioritätswert
.,ADF1 D9 80 A0 CMP $A080,Y     mit Prioritätsw. vergleichen
.,ADF4 B0 67    BCS $AE5D       größer: $AE5D
.,ADF6 20 8D AD JSR $AD8D       prüft auf numerisch
.,ADF9 48       PHA             Prioritätswert retten
.,ADFA 20 20 AE JSR $AE20       Operatoradr. und Operanden r.
.,ADFD 68       PLA
.,ADFE A4 4B    LDY $4B         Operator?
.,AE00 10 17    BPL $AE19       ja: $AE19
.,AE02 AA       TAX             weitere Operation?
.,AE03 F0 56    BEQ $AE5B       nein: RTS
.,AE05 D0 5F    BNE $AE66       ARG vom Stapel holen
.,AE07 46 0D    LSR $0D         Stringflag löschen
.,AE09 8A       TXA             Operatormaske nach
.,AE0A 2A       ROL             links schieben
.,AE0B A6 7A    LDX $7A         Programmzeiger holen (LOW)
.,AE0D D0 02    BNE $AE11       =0: HIGH-Byte vermindern
.,AE0F C6 7B    DEC $7B         HIGH-Byte vermindern
.,AE11 C6 7A    DEC $7A         LOW-Byte vermindern
.,AE13 A0 1B    LDY #$1B        Offset des Hierarchieflags
.,AE15 85 4D    STA $4D         Flag setzen
.,AE17 D0 D7    BNE $ADF0       unbedingter Sprung
.,AE19 D9 80 A0 CMP $A080,Y     mit Hierarchieflag vergl.
.,AE1C B0 48    BCS $AE66       größer: $AE66
.,AE1E 90 D9    BCC $ADF9       sonst weiter
.,AE20 B9 82 A0 LDA $A082,Y     Operationsadresse (HIGH)
.,AE23 48       PHA             auf Stapel retten
.,AE24 B9 81 A0 LDA $A081,Y     Operationsadresse (LOW)
.,AE27 48       PHA             auf Stapel retten
.,AE28 20 33 AE JSR $AE33       Operanden auf Stapel retten
.,AE2B A5 4D    LDA $4D         Operatormaske laden
.,AE2D 4C A9 AD JMP $ADA9       zum Schleifenanfang
.,AE30 4C 08 AF JMP $AF08       gibt 'SYNTAX ERROR'
.,AE33 A5 66    LDA $66         Vorzeichen von FAC
.,AE35 BE 80 A0 LDX $A080,Y     Hierarchieflag
.,AE38 A8       TAY             Vorzeichen ins Y-Reg.
.,AE39 68       PLA             Rücksprungadresse holen
.,AE3A 85 22    STA $22         und merken
.,AE3C E6 22    INC $22         Rücksprungadresse erhöhen
.,AE3E 68       PLA             nächstes Adressbyte holen
.,AE3F 85 23    STA $23         und speichern
.,AE41 98       TYA             Vorzeichen wieder in Akku
.,AE42 48       PHA             und auf Stapel legen
.,AE43 20 1B BC JSR $BC1B       FAC runden
.,AE46 A5 65    LDA $65         FAC auf Stapel legen
.,AE48 48       PHA             1. Byte retten
.,AE49 A5 64    LDA $64         2. Byte holen
.,AE4B 48       PHA             und retten
.,AE4C A5 63    LDA $63         3. Byte holen
.,AE4E 48       PHA             und retten
.,AE4F A5 62    LDA $62         4. Byte holen
.,AE51 48       PHA             und retten
.,AE52 A5 61    LDA $61         5. Byte holen
.,AE54 48       PHA             und retten
.,AE55 6C 22 00 JMP ($0022)     Sprung auf Operation
.,AE58 A0 FF    LDY #$FF        Flagwert für Operator
.,AE5A 68       PLA             Prioritätsflag retten
.,AE5B F0 23    BEQ $AE80       =0? ja: $AE80
.,AE5D C9 64    CMP #$64        =$64?
.,AE5F F0 03    BEQ $AE64       ja: $AE64
.,AE61 20 8D AD JSR $AD8D       prüft auf numerisch
.,AE64 84 4B    STY $4B         flag fur Operator
.,AE66 68       PLA             Akku vom Stapel holen
.,AE67 4A       LSR             halbieren
.,AE68 85 12    STA $12         und abspeichern
.,AE6A 68       PLA             ARG von Stapel holen
.,AE6B 85 69    STA $69         1. Byte speichern
.,AE6D 68       PLA             2. Byte holen
.,AE6E 85 6A    STA $6A         und speichern
.,AE70 68       PLA             3. Byte holen
.,AE71 85 6B    STA $6B         und speichern
.,AE73 68       PLA             4. Byte holen
.,AE74 85 6C    STA $6C         und speichern
.,AE76 68       PLA             5. Byte holen
.,AE77 85 6D    STA $6D         und speichern
.,AE79 68       PLA             6. Byte (Vorzeichen holen
.,AE7A 85 6E    STA $6E         und speichern
.,AE7C 45 66    EOR $66         Vorzeichen von ARG und FAC
.,AE7E 85 6F    STA $6F         verknüpfen und speichern
.,AE80 A5 61    LDA $61         Exponentbyte von FAC laden
.,AE82 60       RTS             Rücksprung

                                *** Nächstes Element eines
                                *** Ausdrucks holen
.,AE83 6C 0A 03 JMP ($030A)     JMP $AE86
.,AE86 A9 00    LDA #$00        Wert laden und damit
.,AE88 85 0D    STA $0D         Typflag auf numerisch setzen
.,AE8A 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,AE8D B0 03    BCS $AE92       Ziffer? nein: $AE92
.,AE8F 4C F3 BC JMP $BCF3       Variable nach FAC holen
.,AE92 20 13 B1 JSR $B113       Buchstabe?
.,AE95 90 03    BCC $AE9A       nein: JMP umgehen
.,AE97 4C 28 AF JMP $AF28       Variable holen
.,AE9A C9 FF    CMP #$FF        BASIC-Code für Pi?
.,AE9C D0 0F    BNE $AEAD       nein: $AEAD
.,AE9E A9 A8    LDA #$A8        Zeiger auf Konstante Pi
.,AEA0 A0 AE    LDY #$AE        (LOW und HIGH-Byte)
.,AEA2 20 A2 BB JSR $BBA2       Konstante in FAC holen
.,AEA5 4C 73 00 JMP $0073       CHRGET nächstes Zeichen holen

.:AEA8 82 49 0F DA A1           Konstante Pi 3.14159265

.,AEAD C9 2E    CMP #$2E        '.' Dezimalpunkt?
.,AEAF F0 DE    BEQ $AE8F       ja: $AE8F
.,AEB1 C9 AB    CMP #$AB        '-'?
.,AEB3 F0 58    BEQ $AF0D       zum Vorzeichenwechsel
.,AEB5 C9 AA    CMP #$AA        '+'?
.,AEB7 F0 D1    BEQ $AE8A       ja: $Ae8A
.,AEB9 C9 22    CMP #$22        '"'?
.,AEBB D0 0F    BNE $AECC       nein: $AECC
.,AEBD A5 7A    LDA $7A         LOW- und HIGH-Byte des
.,AEBF A4 7B    LDY $7B         Programmzeigers holen
.,AEC1 69 00    ADC #$00        und Übertrag addieren
.,AEC3 90 01    BCC $AEC6       C=0: $AEC6
.,AEC5 C8       INY             HIGH-Byte erhöhen
.,AEC6 20 87 B4 JSR $B487       String übertragen
.,AEC9 4C E2 B7 JMP $B7E2       Programmz. auf Stringende +1
.,AECC C9 A8    CMP #$A8        'NOT'-Code?
.,AECE D0 13    BNE $AEE3       nein: $AEE3
.,AED0 A0 18    LDY #$18        Offset des H.Flags in Tabelle
.,AED2 D0 3B    BNE $AF0F       unbedingter Sprung

                                *** BASIC-Befehl NOT
.,AED4 20 BF B1 JSR $B1BF       FAC nach INTEGER wandeln
.,AED7 A5 65    LDA $65         HIGH-Byte holen
.,AED9 49 FF    EOR #$FF        alle Bits umdrehen
.,AEDB A8       TAY             und ins Y-Reg.
.,AEDC A5 64    LDA $64         LOW-Byte holen
.,AEDE 49 FF    EOR #$FF        alle Bits invertieren
.,AEE0 4C 91 B3 JMP $B391       nach Fließkomma wandeln
.,AEE3 C9 A5    CMP #$A5        'FN'-Code?
.,AEE5 D0 03    BNE $AEEA       nein: $AEEA
.,AEE7 4C F4 B3 JMP $B3F4       FN ausführen
.,AEEA C9 B4    CMP #$B4        'SGN'-Code
.,AEEC 90 03    BCC $AEF1       kleiner (keine Stringfunkt.)?
.,AEEE 4C A7 AF JMP $AFA7       holt String ,ersten Parameter

                                *** holt Term in Klammern
.,AEF1 20 FA AE JSR $AEFA       prüft auf Klammer auf
.,AEF4 20 9E AD JSR $AD9E       FRMEVL holt Term

                                *** prüft auf Zeichen im B.-Text
.,AEF7 A9 29    LDA #$29        ')' Klammer zu
.:AEF9 2C       .BYTE $2C
.,AEFA A9 28    LDA #$28        '(' Klammer auf
.:AEFC 2C       .BYTE $2C
.,AEFD A9 2C    LDA #$2C        ',' Komma
.,AEFF A0 00    LDY #$00        Zeiger setzen
.,AF01 D1 7A    CMP ($7A),Y     mit laufendem Zeichen vergl.
.,AF03 D0 03    BNE $AF08       keine Übereinstimmung?
.,AF05 4C 73 00 JMP $0073       CHRGET nächstes Zeichen holen
.,AF08 A2 0B    LDX #$0B        Nummer für 'SYNTAX ERROR'
.,AF0A 4C 37 A4 JMP $A437       Fehlermeldung ausgeben
.,AF0D A0 15    LDY #$15        Offset Hierachie-Code für VZW
.,AF0F 68       PLA             nächsten 2 Bytes vom
.,AF10 68       PLA             Stapel entfernen
.,AF11 4C FA AD JMP $ADFA       zur Auswertung

                                *** prüft auf Variable
.,AF14 38       SEC             innerhalb des BASICs
.,AF15 A5 64    LDA $64         Carry setzen (Subtr.)
.,AF17 E9 00    SBC #$00        Descriptor holen
.,AF19 A5 65    LDA $65         liegt Descriptor ($64/$65)
.,AF1B E9 A0    SBC #$A0        zwischen $A000 und $E32A?
.,AF1D 90 08    BCC $AF27       ja: dann C=1, sonst RTS
.,AF1F A9 A2    LDA #$A2        1. Wert laden
.,AF21 E5 64    SBC $64         1. Descriptorbyte abziehen
.,AF23 A9 E3    LDA #$E3        2. Wert laden
.,AF25 E5 65    SBC $65         und Descriptorwert abziehen
.,AF27 60       RTS             Rücksprung

                                *** Variable holen
.,AF28 20 8B B0 JSR $B08B       Variable suchen
.,AF2B 85 64    STA $64         Zeiger auf Variable
.,AF2D 84 65    STY $65         bzw. Stringdescriptor
.,AF2F A6 45    LDX $45         als
.,AF31 A4 46    LDY $46         Variablenname speichern
.,AF33 A5 0D    LDA $0D         Typflag holen
.,AF35 F0 26    BEQ $AF5D       numerisch?
.,AF37 A9 00    LDA #$00        Wert laden und
.,AF39 85 70    STA $70         in Rundungsbyte fur FAC
.,AF3B 20 14 AF JSR $AF14       Descriptor im Interpreter?
.,AF3E 90 1C    BCC $AF5C       nein
.,AF40 E0 54    CPX #$54        'T'? (von TI$)
.,AF42 D0 18    BNE $AF5C       nein: $AF5C
.,AF44 C0 C9    CPY #$C9        'I$'? (von TI$)
.,AF46 D0 14    BNE $AF5C       nein: $AF5C
.,AF48 20 84 AF JSR $AF84       Zeit nach FAC holen
.,AF4B 84 5E    STY $5E         Flag für Exponentialdarst. =0
.,AF4D 88       DEY             vermindern (=$FF)
.,AF4E 84 71    STY $71         Zeiger für Stringstartadresse
.,AF50 A0 06    LDY #$06        Länge 6 für TI$
.,AF52 84 5D    STY $5D         speichern
.,AF54 A0 24    LDY #$24        Zeiger auf Stellenwert
.,AF56 20 68 BE JSR $BE68       erzeugt String TI$
.,AF59 4C 6F B4 JMP $B46F       bringt String in Str.bereich
.,AF5C 60       RTS             Rücksprung
.,AF5D 24 0E    BIT $0E         INTEGER/ REAL Flag
.,AF5F 10 0D    BPL $AF6E       REAL? ja: $AF6E

                                *** Integervariable holen
.,AF61 A0 00    LDY #$00        Zeiger setzen
.,AF63 B1 64    LDA ($64),Y     Intgerzahl holen (1. Byte)
.,AF65 AA       TAX             ins X-Reg.
.,AF66 C8       INY             Zeiger erhöhen
.,AF67 B1 64    LDA ($64),Y     2. Byte holen
.,AF69 A8       TAY             ins Y-Register
.,AF6A 8A       TXA             1. Byte in Akku holen
.,AF6B 4C 91 B3 JMP $B391       und nach Fließkomma wandeln

                                *** REAL-Variable holen
.,AF6E 20 14 AF JSR $AF14       Descriptor im Interpreter?
.,AF71 90 2D    BCC $AFA0       nein
.,AF73 E0 54    CPX #$54        'T'? (von TI)
.,AF75 D0 1B    BNE $AF92       nein: $AF92
.,AF77 C0 49    CPY #$49        'I'? (von TI)
.,AF79 D0 25    BNE $AFA0       nein: $AFA0
.,AF7B 20 84 AF JSR $AF84       TIME in FAC holen
.,AF7E 98       TYA             Akku =0 setzen
.,AF7F A2 A0    LDX #$A0        Exponentbyte für FAC
.,AF81 4C 4F BC JMP $BC4F       FAC linksbündig machen

                                *** Zeit holen
.,AF84 20 DE FF JSR $FFDE       TIME holen
.,AF87 86 64    STX $64         1. Byte nach FAC
.,AF89 84 63    STY $63         2. Byte nach FAC
.,AF8B 85 65    STA $65         3. Byte nach FAC
.,AF8D A0 00    LDY #$00        Wert laden (0) und
.,AF8F 84 62    STY $62         als 4. Byte nach FAC
.,AF91 60       RTS             Rücksprung
.,AF92 E0 53    CPX #$53        'S'?
.,AF94 D0 0A    BNE $AFA0       nein: $AFA0
.,AF96 C0 54    CPY #$54        'T'?
.,AF98 D0 06    BNE $AFA0       nein: $AFA0
.,AF9A 20 B7 FF JSR $FFB7       Status holen
.,AF9D 4C 3C BC JMP $BC3C       Byte in Fließkommaformat

                                *** REAL-Variable holen
.,AFA0 A5 64    LDA $64         LOW- und HIGH-Byte der
.,AFA2 A4 65    LDY $65         Variablenadresse
.,AFA4 4C A2 BB JMP $BBA2       Variable in FAC holen

                                *** Funktionsberechnung
.,AFA7 0A       ASL             Funktionscode mal 2
.,AFA8 48       PHA             auf den Stapel retten
.,AFA9 AA       TAX             und ins X-Register
.,AFAA 20 73 00 JSR $0073       CHRGET nächstes Zeichen
.,AFAD E0 8F    CPX #$8F        numerische Funktion?
.,AFAF 90 20    BCC $AFD1       ja: $AFD1

                                *** Stringfunktion, String und
                                *** ersten Parameter
.,AFB1 20 FA AE JSR $AEFA       prüft auf Klammer auf
.,AFB4 20 9E AD JSR $AD9E       FRMEVL holen beliebigen Term
.,AFB7 20 FD AE JSR $AEFD       prüft auf Komma
.,AFBA 20 8F AD JSR $AD8F       prüft auf String
.,AFBD 68       PLA             Funktionstoken left$, r$, m$
.,AFBE AA       TAX             Akku nach X holen
.,AFBF A5 65    LDA $65         Adresse des
.,AFC1 48       PHA             Stringdescriptors
.,AFC2 A5 64    LDA $64         holen und auf den Stapel
.,AFC4 48       PHA             retten (LOW und HIGH)
.,AFC5 8A       TXA             Akku wiederholen
.,AFC6 48       PHA             Token auf den Stapel retten
.,AFC7 20 9E B7 JSR $B79E       holt Byte-Wert (2. Parameter)
.,AFCA 68       PLA             Token zurückholen
.,AFCB A8       TAY             und ins Y-Reg.
.,AFCC 8A       TXA             2. Bytewert in den Akku laden
.,AFCD 48       PHA             und auf den Stapel retten
.,AFCE 4C D6 AF JMP $AFD6       Routine ausführen

                                *** numerische Funktion auswerten
.,AFD1 20 F1 AE JSR $AEF1       holt Term in Klammern
.,AFD4 68       PLA             BASIC-Code für Funktion holen
.,AFD5 A8       TAY             und als Zeiger ins Y-Reg.
.,AFD6 B9 EA 9F LDA $9FEA,Y     Vektor für Funktionsbe-
.,AFD9 85 55    STA $55         rechnung holen und speichern
.,AFDB B9 EB 9F LDA $9FEB,Y     2.Byte holen
.,AFDE 85 56    STA $56         und speichern
.,AFE0 20 54 00 JSR $0054       Funktion ausführen
.,AFE3 4C 8D AD JMP $AD8D       prüft auf numerisch

                                *** BASIC-Befehl OR
.,AFE6 A0 FF    LDY #$FF        Flag für OR
.:AFE8 2C       .BYTE $2C

                                *** BASIC-Befehl AND
.,AFE9 A0 00    LDY #$00        Flag fur AND
.,AFEB 84 0B    STY $0B         Flag setzen
.,AFED 20 BF B1 JSR $B1BF       FAC nach INTEGER wandeln
.,AFF0 A5 64    LDA $64         ersten Wert holen
.,AFF2 45 0B    EOR $0B         mit Flag verknüpfen
.,AFF4 85 07    STA $07         und speichern
.,AFF6 A5 65    LDA $65         zweiten Wert holen
.,AFF8 45 0B    EOR $0B         mit Flag verknüpfen
.,AFFA 85 08    STA $08         und speichern
.,AFFC 20 FC BB JSR $BBFC       ARG nach FAC
.,AFFF 20 BF B1 JSR $B1BF       FAC nach Integer
.,B002 A5 65    LDA $65         zweites Byte holen
.,B004 45 0B    EOR $0B         mit Flag verknüpfen
.,B006 25 08    AND $08         logische AND-Verknüpfung
.,B008 45 0B    EOR $0B         mit Flag verknüpfen
.,B00A A8       TAY             ins Y-Reg. retten
.,B00B A5 64    LDA $64         erstes Byte holen
.,B00D 45 0B    EOR $0B         mit Flag verknüpfen
.,B00F 25 07    AND $07         logische AND-Verknüpfung
.,B011 45 0B    EOR $0B         mit Flag verknüpfen
.,B013 4C 91 B3 JMP $B391       wieder in Fließkomma wandeln

                                *** Vergleich
.,B016 20 90 AD JSR $AD90       prüft auf identischen Typ
.,B019 B0 13    BCS $B02E       String: dann weiter
.,B01B A5 6E    LDA $6E         Wert holen
.,B01D 09 7F    ORA #$7F        ARG in Speicherformat
.,B01F 25 6A    AND $6A         wandeln und
.,B021 85 6A    STA $6A         wieder abspeichern
.,B023 A9 69    LDA #$69        Adresse von ARG
.,B025 A0 00    LDY #$00        (LOW- und HIGH-Byte)
.,B027 20 5B BC JSR $BC5B       Vergleich ARG mit FAC
.,B02A AA       TAX
.,B02B 4C 61 B0 JMP $B061       Ergebnis in FAC holen

                                *** Stringvergleich
.,B02E A9 00    LDA #$00        Wert laden und damit
.,B030 85 0D    STA $0D         Stringflag löschen
.,B032 C6 4D    DEC $4D         Operatormaske - 1
.,B034 20 A6 B6 JSR $B6A6       FRLSTR
.,B037 85 61    STA $61         Stringlänge holen
.,B039 86 62    STX $62         LOW- und HIGH-Byte der
.,B03B 84 63    STY $63         Stringadresse speichern
.,B03D A5 6C    LDA $6C         LOW- und HIGH-Byte des
.,B03F A4 6D    LDY $6D         Zeigers auf zweiten String
.,B041 20 AA B6 JSR $B6AA       FRESTR
.,B044 86 6C    STX $6C         Adresse des
.,B046 84 6D    STY $6D         2. Strings
.,B048 AA       TAX             Länge des 2.Strings merken
.,B049 38       SEC             Carry setzen (Subtraktion)
.,B04A E5 61    SBC $61         Längen vergleichen
.,B04C F0 08    BEQ $B056       gleich: $B056
.,B04E A9 01    LDA #$01        Wert für: 1.String länger
.,B050 90 04    BCC $B056       2.String kürzer
.,B052 A6 61    LDX $61         Länge des 1.Strings
.,B054 A9 FF    LDA #$FF        Wert für: 1.String kürzer
.,B056 85 66    STA $66         Flag für gleichen String,
.,B058 A0 FF    LDY #$FF        wenn beide Strings identisch aber
.,B05A E8       INX             ungleich lang sind
.,B05B C8       INY             Zeiger erhöhen
.,B05C CA       DEX             Stringende?
.,B05D D0 07    BNE $B066       nein: weiter
.,B05F A6 66    LDX $66         Vorzeichenbyte holen
.,B061 30 0F    BMI $B072       negativ: $B072
.,B063 18       CLC             Carry löschen
.,B064 90 0C    BCC $B072       unbedingter Sprung
.,B066 B1 6C    LDA ($6C),Y     Vergleich der Strings
.,B068 D1 62    CMP ($62),Y     zeichenweise
.,B06A F0 EF    BEQ $B05B       gleiche Zeichen: weiter
.,B06C A2 FF    LDX #$FF        Wert laden
.,B06E B0 02    BCS $B072       und Vergleich beenden
.,B070 A2 01    LDX #$01        Wert laden
.,B072 E8       INX             und um 1 erhöhen
.,B073 8A       TXA             Wert in den Akku
.,B074 2A       ROL             linksverschieben, Bit 1, 2=$1
.,B075 25 12    AND $12         mit Vorzeichen verknüpfen
.,B077 F0 02    BEQ $B07B       =0: $B07B
.,B079 A9 FF    LDA #$FF
.,B07B 4C 3C BC JMP $BC3C       Ergebnis nach FAC holen
.,B07E 20 FD AE JSR $AEFD       CHKCOM prüft auf Komma

                                *** BASIC-Befehl DIM
.,B081 AA       TAX             nächstes Zeichen
.,B082 20 90 B0 JSR $B090       Variable dimensionieren
.,B085 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,B088 D0 F4    BNE $B07E       nicht Ende: zur nächsten Var.
.,B08A 60       RTS             Rücksprung

                                *** Variable holen
.,B08B A2 00    LDX #$00        Flag für nicht dimensionieren
.,B08D 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,B090 86 0C    STX $0C         DIM-Flag setzen
.,B092 85 45    STA $45         Variablenname
.,B094 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,B097 20 13 B1 JSR $B113       prüft auf Buchstabe
.,B09A B0 03    BCS $B09F       ja: $B09F
.,B09C 4C 08 AF JMP $AF08       'SYNTAX ERROR'
.,B09F A2 00    LDX #$00        Wert laden und damit
.,B0A1 86 0D    STX $0D         Stringflag löschen
.,B0A3 86 0E    STX $0E         Integerflag löschen
.,B0A5 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,B0A8 90 05    BCC $B0AF       Ziffer?
.,B0AA 20 13 B1 JSR $B113       prüft auf Buchstabe
.,B0AD 90 0B    BCC $B0BA       nein: $B0BA
.,B0AF AA       TAX             zweiter Buchstabe des Names
.,B0B0 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,B0B3 90 FB    BCC $B0B0       Ziffer?
.,B0B5 20 13 B1 JSR $B113       prüft auf Buchstabe
.,B0B8 B0 F6    BCS $B0B0       ja: weitere Zeichen überlesen
.,B0BA C9 24    CMP #$24        '$' Code?
.,B0BC D0 06    BNE $B0C4       nein: $B0C4
.,B0BE A9 FF    LDA #$FF        Wert laden und
.,B0C0 85 0D    STA $0D         Stringflag setzen
.,B0C2 D0 10    BNE $B0D4       Sprung
.,B0C4 C9 25    CMP #$25        '%' Code?
.,B0C6 D0 13    BNE $B0DB       nein: $B0DB
.,B0C8 A5 10    LDA $10         Integer erlaubt?
.,B0CA D0 D0    BNE $B09C       nein: 'SYNTAX ERROR'
.,B0CC A9 80    LDA #$80        Wert für Integer laden
.,B0CE 85 0E    STA $0E         und Integerflag setzen
.,B0D0 05 45    ORA $45         Bit 7 im 1.Zeichen setzen und
.,B0D2 85 45    STA $45         speichern (Bit7=1: Integer)
.,B0D4 8A       TXA             X nach Akku speichern
.,B0D5 09 80    ORA #$80        Bit 7 im 2.Buchstaben setzen
.,B0D7 AA       TAX             X-Reg. zurückholen
.,B0D8 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,B0DB 86 46    STX $46         zweiten Buchstaben speichern
.,B0DD 38       SEC             Feldvariablen erlaubt?
.,B0DE 05 10    ORA $10         wenn nicht, Bit7 setzen
.,B0E0 E9 28    SBC #$28        '('-Wert abziehen
.,B0E2 D0 03    BNE $B0E7       nicht Klammer auf?
.,B0E4 4C D1 B1 JMP $B1D1       dimensionierte Variable holen
.,B0E7 A0 00    LDY #$00        Wert laden und
.,B0E9 84 10    STY $10         FN-Flag = 0 setzen
.,B0EB A5 2D    LDA $2D         Zeiger auf Variablenanfang
.,B0ED A6 2E    LDX $2E         holen (LOW und HIGH)
.,B0EF 86 60    STX $60         und zum
.,B0F1 85 5F    STA $5F         Suchen merken
.,B0F3 E4 30    CPX $30         Suchzeiger = Variablenanfang
.,B0F5 D0 04    BNE $B0FB       nein: $B0FB
.,B0F7 C5 2F    CMP $2F         Ende der Variablen erreicht?
.,B0F9 F0 22    BEQ $B11D       ja: nicht gefunden, anlegen
.,B0FB A5 45    LDA $45         ersten Buchstaben des Namens
.,B0FD D1 5F    CMP ($5F),Y     mit Tabelle vergleichen
.,B0FF D0 08    BNE $B109       nein: weitersuchen
.,B101 A5 46    LDA $46         zweiten Buchstaben
.,B103 C8       INY             Zeiger erhöhen
.,B104 D1 5F    CMP ($5F),Y     vergleichen
.,B106 F0 7D    BEQ $B185       gleich: gefunden
.,B108 88       DEY             Zeiger vermindern
.,B109 18       CLC             Carry setzen (Addition)
.,B10A A5 5F    LDA $5F         Zeiger um 7
.,B10C 69 07    ADC #$07        erhöhen (2+5 Byte REAL Var.)
.,B10E 90 E1    BCC $B0F1       (Länge eines V.-Eintrags)
.,B110 E8       INX             Übertrag addieren
.,B111 D0 DC    BNE $B0EF       weiter suchen

                                *** prüft auf Buchstabe
.,B113 C9 41    CMP #$41        'A'-Code? (Buchstabencode)
.,B115 90 05    BCC $B11C       wenn kleiner: RTS mit C = 0
.,B117 E9 5B    SBC #$5B        'Z' + 1
.,B119 38       SEC             wenn größer 'Z': C = 0
.,B11A E9 A5    SBC #$A5        sonst: C = 1 = Buchstabe
.,B11C 60       RTS             Rücksprung

                                *** Variable anlegen
.,B11D 68       PLA
.,B11E 48       PHA             Aufrufadresse prüfen
.,B11F C9 2A    CMP #$2A        Aufruf von FRMEVL?
.,B121 D0 05    BNE $B128       nein: dann neu anlegen
.,B123 A9 13    LDA #$13        Zeiger auf Konstante 0
.,B125 A0 BF    LDY #$BF        (LOW und HIGH)
.,B127 60       RTS             Rücksprung
.,B128 A5 45    LDA $45         LOW- und HIGH-Byte
.,B12A A4 46    LDY $46         des Variablennames
.,B12C C9 54    CMP #$54        'T'-Code?
.,B12E D0 0B    BNE $B13B       nein: $B13B
.,B130 C0 C9    CPY #$C9        'I$'-Code?
.,B132 F0 EF    BEQ $B123       ja: TI$
.,B134 C0 49    CPY #$49        'I'-Code?
.,B136 D0 03    BNE $B13B       nein: $B13B
.,B138 4C 08 AF JMP $AF08       'SYNTAX ERROR'
.,B13B C9 53    CMP #$53        'S'-Code?
.,B13D D0 04    BNE $B143       nein: $B143
.,B13F C0 54    CPY #$54        'T'-Code?
.,B141 F0 F5    BEQ $B138       ST, dann 'SYNTAX ERROR'
.,B143 A5 2F    LDA $2F         LOW- und HIGH-Byte des
.,B145 A4 30    LDY $30         Zeigers auf Arraytabelle
.,B147 85 5F    STA $5F         laden und
.,B149 84 60    STY $60         merken
.,B14B A5 31    LDA $31         LOW- und HIGH-Byte des
.,B14D A4 32    LDY $32         Zeigers auf Ende der
.,B14F 85 5A    STA $5A         Arraytabelle
.,B151 84 5B    STY $5B         merken
.,B153 18       CLC             Carry für Addition setzen
.,B154 69 07    ADC #$07        um 7 verschieben für Anlage
.,B156 90 01    BCC $B159       einer neuen Variablen
.,B158 C8       INY             Übertrag addieren
.,B159 85 58    STA $58         LOW- und HIGH-Byte des
.,B15B 84 59    STY $59         neuen Blockendes speichern
.,B15D 20 B8 A3 JSR $A3B8       Block verschieben
.,B160 A5 58    LDA $58         Werte
.,B162 A4 59    LDY $59         wiederholen
.,B164 C8       INY             und damit
.,B165 85 2F    STA $2F         Zeiger auf Arraytabelle
.,B167 84 30    STY $30         neu setzen
.,B169 A0 00    LDY #$00        Zeiger setzen
.,B16B A5 45    LDA $45         erster Buchstabe des Namens
.,B16D 91 5F    STA ($5F),Y     und speichern
.,B16F C8       INY             Zeiger erhöhen,
.,B170 A5 46    LDA $46         zweiten Buchstaben holen
.,B172 91 5F    STA ($5F),Y     und abspeichern
.,B174 A9 00    LDA #$00        Nullwert laden
.,B176 C8       INY             Zeiger erhöhen
.,B177 91 5F    STA ($5F),Y     nächsten 5 Werte
.,B179 C8       INY             der Variable auf 0 setzen
.,B17A 91 5F    STA ($5F),Y     2. Byte speichern
.,B17C C8       INY             Zeiger erhöhen
.,B17D 91 5F    STA ($5F),Y     3. Byte speichern
.,B17F C8       INY             Zeiger erhöhen
.,B180 91 5F    STA ($5F),Y     4. Byte speichern
.,B182 C8       INY             Zeiger erhöhen
.,B183 91 5F    STA ($5F),Y     5. Byte speichern
.,B185 A5 5F    LDA $5F         Zeiger auf Variablenwert
.,B187 18       CLC             Carry löschen (Addition)
.,B188 69 02    ADC #$02        zwei für Namen addieren
.,B18A A4 60    LDY $60         in Zeiger auf Variable
.,B18C 90 01    BCC $B18F       Zeiger auf erstes Byte
.,B18E C8       INY             High-Byte $48 erhöhen
.,B18F 85 47    STA $47         als Variablenzeiger
.,B191 84 48    STY $48         nach $47/48 speichern
.,B193 60       RTS             Rücksprung

                                *** berechnet Zeiger auf erstes
                                *** Arrayelement
.,B194 A5 0B    LDA $0B         Anzahl der Dimensionen
.,B196 0A       ASL             mal 2
.,B197 69 05    ADC #$05        plus 5
.,B199 65 5F    ADC $5F         zu $5F und
.,B19B A4 60    LDY $60         $60 addieren
.,B19D 90 01    BCC $B1A0       Erhöhung umgehen
.,B19F C8       INY             Übertrag addieren
.,B1A0 85 58    STA $58         Ergebnis-Zeiger nach
.,B1A2 84 59    STY $59         $58/59 speichern
.,B1A4 60       RTS             Rücksprung

.:B1A5 90 80 00 00 00           Konstante -32768

                                *** Umwandlung FAC nach Integer
.,B1AA 20 BF B1 JSR $B1BF       FAC nach Integer wandeln
.,B1AD A5 64    LDA $64         LOW-Byte
.,B1AF A4 65    LDY $65         HIGH-Byte
.,B1B1 60       RTS             Rücksprung

                                *** Ausdruck holen und
                                *** nach Integer
.,B1B2 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,B1B5 20 9E AD JSR $AD9E       FRMEVL, Ausdruck auswerten
.,B1B8 20 8D AD JSR $AD8D       prüft auf numerisch
.,B1BB A5 66    LDA $66         Vorzeichen?
.,B1BD 30 0D    BMI $B1CC       negativ: dann 'ILLEGAL QUANT'
.,B1BF A5 61    LDA $61         Exponent
.,B1C1 C9 90    CMP #$90        Betrag größer 32768?
.,B1C3 90 09    BCC $B1CE       nein: $B1CE
.,B1C5 A9 A5    LDA #$A5        Zeiger auf
.,B1C7 A0 B1    LDY #$B1        Konstante -32768 setzen
.,B1C9 20 5B BC JSR $BC5B       Vergleich FAC mit Konstante
.,B1CC D0 7A    BNE $B248       ungleich: 'ILLEGAL QUANT'
.,B1CE 4C 9B BC JMP $BC9B       wandelt Fließkomma in Integer

                                *** dimensionierte Variable holen
.,B1D1 A5 0C    LDA $0C         DIM Flag
.,B1D3 05 0E    ORA $0E         Integer Flag
.,B1D5 48       PHA             auf Stapel retten
.,B1D6 A5 0D    LDA $0D         String Flag
.,B1D8 48       PHA             auf Stapel retten
.,B1D9 A0 00    LDY #$00        Anzahl der Indizes
.,B1DB 98       TYA             in Akku und
.,B1DC 48       PHA             auf Stapel retten
.,B1DD A5 46    LDA $46         2. Buchstabe des Variablenn.
.,B1DF 48       PHA             und retten
.,B1E0 A5 45    LDA $45         1. Buchstabe der Variablenn.
.,B1E2 48       PHA             retten
.,B1E3 20 B2 B1 JSR $B1B2       Index holen und nach Integer
.,B1E6 68       PLA             die zwei
.,B1E7 85 45    STA $45         Bytes des
.,B1E9 68       PLA             Variablennamens zurückholen
.,B1EA 85 46    STA $46         und wieder abspeichern
.,B1EC 68       PLA             Anzahl der Indizes
.,B1ED A8       TAY             holen und ins Y-Reg.
.,B1EE BA       TSX             Stapelzeiger als Zeiger setzen
.,B1EF BD 02 01 LDA $0102,X     Variablenflags
.,B1F2 48       PHA             aus dem Stapel kopieren
.,B1F3 BD 01 01 LDA $0101,X     und oben auf den
.,B1F6 48       PHA             Stapel legen
.,B1F7 A5 64    LDA $64         anstelle der
.,B1F9 9D 02 01 STA $0102,X     Variablenflags
.,B1FC A5 65    LDA $65         Index LOW und HIGH in
.,B1FE 9D 01 01 STA $0101,X     den Stapel kopieren
.,B201 C8       INY             Anzahl der Indizes erhöhen
.,B202 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,B205 C9 2C    CMP #$2C        ',' Komma?
.,B207 F0 D2    BEQ $B1DB       ja: dann nächsten Index
.,B209 84 0B    STY $0B         Anzahl der Indizes speichern
.,B20B 20 F7 AE JSR $AEF7       prüft auf Klammer zu
.,B20E 68       PLA             Flags vom
.,B20F 85 0D    STA $0D         Stapel
.,B211 68       PLA             zurückholen
.,B212 85 0E    STA $0E         und abspeichern
.,B214 29 7F    AND #$7F        Integerflag herstellen
.,B216 85 0C    STA $0C         und abspeichern
.,B218 A6 2F    LDX $2F         LOW- und HIGH-Byte des
.,B21A A5 30    LDA $30         Zeigers auf Arraytabelle
.,B21C 86 5F    STX $5F         holen und
.,B21E 85 60    STA $60         Zeiger merken
.,B220 C5 32    CMP $32         Ende erreicht?
.,B222 D0 04    BNE $B228       nein: weiter
.,B224 E4 31    CPX $31         mit Tabellenende vergleichen
.,B226 F0 39    BEQ $B261       ja: nicht gefunden, anlegen
.,B228 A0 00    LDY #$00        Zeiger setzen
.,B22A B1 5F    LDA ($5F),Y     Namen aus Tabelle holen
.,B22C C8       INY             Zeiger erhöhen
.,B22D C5 45    CMP $45         mit ges. Namen vergleichen
.,B22F D0 06    BNE $B237       ungleich: $B237
.,B231 A5 46    LDA $46         Vergleich mit
.,B233 D1 5F    CMP ($5F),Y     zweitem Buchstaben
.,B235 F0 16    BEQ $B24D       gefunden: $B24D
.,B237 C8       INY             Zeiger erhöhen
.,B238 B1 5F    LDA ($5F),Y     Suchzeiger zur
.,B23A 18       CLC             Feldlänge
.,B23B 65 5F    ADC $5F         Addieren
.,B23D AA       TAX             ergibt Zeiger auf
.,B23E C8       INY             nächstes Array
.,B23F B1 5F    LDA ($5F),Y     gleiches System
.,B241 65 60    ADC $60         mit zweitem Byte
.,B243 90 D7    BCC $B21C       und weiter suchen
.,B245 A2 12    LDX #$12        Nummer für 'bad subscript'
.:B247 2C       .BYTE $2C
.,B248 A2 0E    LDX #$0E        Nummer für 'illegal quanti.'
.,B24A 4C 37 A4 JMP $A437       Fehlermeldung ausgeben
.,B24D A2 13    LDX #$13        Nummer für 'redim'd array'
.,B24F A5 0C    LDA $0C         DIM-Flag null?
.,B251 D0 F7    BNE $B24A       nein: dann Fehlermeldung
.,B253 20 94 B1 JSR $B194       Zeiger auf 1.Arrayelement
.,B256 A5 0B    LDA $0B         Zahl der gefundenen Dimensio.
.,B258 A0 04    LDY #$04        Zeiger setzen
.,B25A D1 5F    CMP ($5F),Y     mit Dimensionen des Arrays
                                vergleichen
.,B25C D0 E7    BNE $B245       ungleich: 'bad subscript'
.,B25E 4C EA B2 JMP $B2EA       sucht gewünschtes Element

                                *** Arrayvariable anlegen
.,B261 20 94 B1 JSR $B194       Länge des Arraykopfs
.,B264 20 08 A4 JSR $A408       prüft auf genügend Platz
.,B267 A0 00    LDY #$00        Zeiger für Polynom-
.,B269 84 72    STY $72         auswertung neu setzen
.,B26B A2 05    LDX #$05        Wert für Variablenlänge(REAL)
.,B26D A5 45    LDA $45         erster Buchstabe des Namens
.,B26F 91 5F    STA ($5F),Y     in Arraytabelle
.,B271 10 01    BPL $B274       kein Integer?
.,B273 CA       DEX             bei Integerzahl
.,B274 C8       INY             Bytes vermindern
.,B275 A5 46    LDA $46         zweiter Buchstabe
.,B277 91 5F    STA ($5F),Y     in Tabelle schreiben
.,B279 10 02    BPL $B27D       kein String oder Integer?
.,B27B CA       DEX             entgültige
.,B27C CA       DEX             Variablenlänge herstellen
.,B27D 86 71    STX $71         und speichern (2, 3 oder 5)
.,B27F A5 0B    LDA $0B         Anzahl der Dimensionen holen
.,B281 C8       INY             Zeiger
.,B282 C8       INY             um 3
.,B283 C8       INY             erhöhen
.,B284 91 5F    STA ($5F),Y     im Arrayheader speichern
.,B286 A2 0B    LDX #$0B        11, Defaultwert für
.,B288 A9 00    LDA #$00        Dimensionierung
.,B28A 24 0C    BIT $0C         Aufruf durch DIM-Befehl?
.,B28C 50 08    BVC $B296       nein: $B296
.,B28E 68       PLA             Dimension vom Stapel holen
.,B28F 18       CLC             Carry löschen (Addition)
.,B290 69 01    ADC #$01        eins addieren
.,B292 AA       TAX             und ins X-Reg.
.,B293 68       PLA             2.Wert holen
.,B294 69 00    ADC #$00        Übertrag addieren
.,B296 C8       INY             Zeiger erhöhen
.,B297 91 5F    STA ($5F),Y     und speichern
.,B299 C8       INY             Zeiger erhöhen
.,B29A 8A       TXA             1.Wert wieder in den Akku
.,B29B 91 5F    STA ($5F),Y     und ebenfalls speichern
.,B29D 20 4C B3 JSR $B34C       Platz für Dimensionen berech.
.,B2A0 86 71    STX $71         LOW- und HIGH-Byte des
.,B2A2 85 72    STA $72         Variablenende-Zeigers merken
.,B2A4 A4 22    LDY $22         Zeiger auf Arrayheader
.,B2A6 C6 0B    DEC $0B         weitere Dimensionen?
.,B2A8 D0 DC    BNE $B286       ja: $B286 (Schleifenbeginn)
.,B2AA 65 59    ADC $59         Feldlänge plus Startadresse
.,B2AC B0 5D    BCS $B30B       Überlauf: 'OUT OF MEMORY'
.,B2AE 85 59    STA $59         Wert wieder speichern
.,B2B0 A8       TAY             und ins Y-Reg. bringen
.,B2B1 8A       TXA             Variablenendzeiger in Akku
.,B2B2 65 58    ADC $58         2.Zeichen addieren
.,B2B4 90 03    BCC $B2B9       Überlauf: Platz prüfen
.,B2B6 C8       INY             Endadresse erhöhen
.,B2B7 F0 52    BEQ $B30B       Überlauf: 'OUT OF MEMORY'
.,B2B9 20 08 A4 JSR $A408       prüft auf Speicherplatz
.,B2BC 85 31    STA $31         Zeiger auf Ende
.,B2BE 84 32    STY $32         der Arraytabelle setzen
.,B2C0 A9 00    LDA #$00        Array mit Nullen füllen
.,B2C2 E6 72    INC $72         Schleifenzähler high um 1 erhöhen
.,B2C4 A4 71    LDY $71         Schleifenzähler low
.,B2C6 F0 05    BEQ $B2CD       wenn null: $B2CD
.,B2C8 88       DEY             Zeiger vermindern
.,B2C9 91 58    STA ($58),Y     Nullwert setzen
.,B2CB D0 FB    BNE $B2C8       solang Y <>0: $B2C8
.,B2CD C6 59    DEC $59         High-Byte STA-Ziel verringern
.,B2CF C6 72    DEC $72         Schleifenzähler high verringern
.,B2D1 D0 F5    BNE $B2C8       solang <>0: $B2C8
.,B2D3 E6 59    INC $59         High-Byte STA-Ziel erhöhen
.,B2D5 38       SEC             Carry setzen (Subtr.)
.,B2D6 A5 31    LDA $31         Zeiger auf Feldende
.,B2D8 E5 5F    SBC $5F         - Zeiger auf Arrayheader
.,B2DA A0 02    LDY #$02        Zeiger setzen
.,B2DC 91 5F    STA ($5F),Y     Arraylänge LOW
.,B2DE A5 32    LDA $32         Zeiger auf Feldende
.,B2E0 C8       INY             Zeiger erhöhen
.,B2E1 E5 60    SBC $60         - Zeiger auf Arrayheader
.,B2E3 91 5F    STA ($5F),Y     Arraylänge HIGH
.,B2E5 A5 0C    LDA $0C         Aufruf vom DIM-Befehl?
.,B2E7 D0 62    BNE $B34B       ja: RTS

                                *** Arrayelement suchen
.,B2E9 C8       INY             Zeiger erhöhen
.,B2EA B1 5F    LDA ($5F),Y     Zahl der Dimensionen
.,B2EC 85 0B    STA $0B         speichern
.,B2EE A9 00    LDA #$00        Nullwert laden und
.,B2F0 85 71    STA $71         Zeiger auf Polynom-
.,B2F2 85 72    STA $72         auswertung löschen
.,B2F4 C8       INY             Zeiger erhöhen
.,B2F5 68       PLA             1. Indexwert vom Stapel
.,B2F6 AA       TAX             holen und ins X-Reg. bringen
.,B2F7 85 64    STA $64         Wert speichern
.,B2F9 68       PLA             2. Indexwert holen
.,B2FA 85 65    STA $65         und speichern
.,B2FC D1 5F    CMP ($5F),Y     mit Wert im Array vergleichen
.,B2FE 90 0E    BCC $B30E       kleiner?
.,B300 D0 06    BNE $B308       größer: 'bad subscript'
.,B302 C8       INY             Zeiger erhöhen
.,B303 8A       TXA             1.Wert zurückholen
.,B304 D1 5F    CMP ($5F),Y     LOW-Byte vergleichen
.,B306 90 07    BCC $B30F       kleiner: dann weiter
.,B308 4C 45 B2 JMP $B245       'bad subscript'
.,B30B 4C 35 A4 JMP $A435       'out of memory'

                                *** Berechnung der Adresse
                                *** eines Arrayelements
.,B30E C8       INY             Zeiger erhöhen
.,B30F A5 72    LDA $72         Zeiger auf Polynomausw.(HIGH)
.,B311 05 71    ORA $71         Zeiger auf Polynomausw.(LOW)
.,B313 18       CLC             Carry löschen
.,B314 F0 0A    BEQ $B320       Multiplikation umgehen
.,B316 20 4C B3 JSR $B34C       Multiplikation
.,B319 8A       TXA             (X/Y)=($71/72)*(($5F/60),Y)
.,B31A 65 64    ADC $64
.,B31C AA       TAX             Akku zurück ins X-Reg.
.,B31D 98       TYA
.,B31E A4 22    LDY $22         Zeiger in Arrayheader
.,B320 65 65    ADC $65
.,B322 86 71    STX $71
.,B324 C6 0B    DEC $0B         Anzahl der Dimensionen
.,B326 D0 CA    BNE $B2F2       mit nächstem Index weiter
.,B328 85 72    STA $72
.,B32A A2 05    LDX #$05        Variablenlänge (5, REAL)
.,B32C A5 45    LDA $45         erster Buchstabe des Namens
.,B32E 10 01    BPL $B331       Integer? nein: $B331
.,B330 CA       DEX             Länge vermindern
.,B331 A5 46    LDA $46         zweiter Buchstabe des Namens
.,B333 10 02    BPL $B337       FLP? ja: $B337
.,B335 CA       DEX             Länge 2 mal
.,B336 CA       DEX             vermindern
.,B337 86 28    STX $28         Länge der Variablen 2,3 oder5
.,B339 A9 00    LDA #$00        Wert laden und damit
.,B33B 20 55 B3 JSR $B355       Offset im Array berechnen
.,B33E 8A       TXA             zur Adresse des ersten
.,B33F 65 58    ADC $58         Elements addieren
.,B341 85 47    STA $47         ergibt Variablenadresse
.,B343 98       TYA             2.Byte in Akku holen
.,B344 65 59    ADC $59         addieren, ergibt
.,B346 85 48    STA $48         HIGH-Byte der Adresse
.,B348 A8       TAY             ins Y-Reg. bringen und
.,B349 A5 47    LDA $47         1.Byte wieder in Akku holen
.,B34B 60       RTS             Rücksprung

                                *** Hilfsroutine für
                                *** Arrayberechnung
.,B34C 84 22    STY $22         Register merken
.,B34E B1 5F    LDA ($5F),Y     1. Wert holen
.,B350 85 28    STA $28         und abspeichern
.,B352 88       DEY             Zeiger vermindern
.,B353 B1 5F    LDA ($5F),Y     2. Wert holen
.,B355 85 29    STA $29         und abspeichern
.,B357 A9 10    LDA #$10        Wert laden und damit
.,B359 85 5D    STA $5D         Verschiebezähler setzen
.,B35B A2 00    LDX #$00        LOW- und HIGH-Byte des Er-
.,B35D A0 00    LDY #$00        gebnisregisters auf 0 setzen
.,B35F 8A       TXA             LOW-Byte in Akku holen und
.,B360 0A       ASL             um 1 Bit nach links schieben
.,B361 AA       TAX             Byte zurück ins X-Reg.
.,B362 98       TYA             HIGH-Byte in den Akku holen,
.,B363 2A       ROL             um 1 Bit nach links rotieren
.,B364 A8       TAY             und zurückbringen
.,B365 B0 A4    BCS $B30B       Überlauf: 'out of memory'
.,B367 06 71    ASL $71         nächstes Bit aus
.,B369 26 72    ROL $72         $71/72 herausholen
.,B36B 90 0B    BCC $B378       =0? ja: Addition umgehen
.,B36D 18       CLC             Carry setzen (Addition)
.,B36E 8A       TXA             LOW-Byte holen
.,B36F 65 28    ADC $28         1. Wert addieren
.,B371 AA       TAX             LOW-Byte zurückbringen
.,B372 98       TYA             HIGH-Byte holen
.,B373 65 29    ADC $29         2. Wert addieren
.,B375 A8       TAY             HIGH-Byte zurückholen
.,B376 B0 93    BCS $B30B       Überlauf: 'out of memory'
.,B378 C6 5D    DEC $5D         nächstes Bit holen
.,B37A D0 E3    BNE $B35F       alle 16 Bits? nein: weiter
.,B37C 60       RTS             Rücksprung

                                *** BASIC-Funktion FRE
.,B37D A5 0D    LDA $0D         Typflag
.,B37F F0 03    BEQ $B384       kein String
.,B381 20 A6 B6 JSR $B6A6       FRESTR
.,B384 20 26 B5 JSR $B526       Garbage Collection
.,B387 38       SEC             Carry setzen (Subtr.)
.,B388 A5 33    LDA $33         Stringanfang (LOW)
.,B38A E5 31    SBC $31         - Variablenende (LOW)
.,B38C A8       TAY             ergibt freien Speicher
.,B38D A5 34    LDA $34         Stringanfang (HIGH)
.,B38F E5 32    SBC $32         - Variablenende (HIGH)
.,B391 A2 00    LDX #$00        Wert laden und
.,B393 86 0D    STX $0D         Flag auf numerisch setzen
.,B395 85 62    STA $62         LOW- und HIGH-Byte des
.,B397 84 63    STY $63         Ergebnisses merken
.,B399 A2 90    LDX #$90        und nach
.,B39B 4C 44 BC JMP $BC44       Fließkomma wandlen

                                *** BASIC-Funktion POS
.,B39E 38       SEC             C=1 Cursorposition holen
.,B39F 20 F0 FF JSR $FFF0       Cursorposition holen
.,B3A2 A9 00    LDA #$00        Z=1
.,B3A4 F0 EB    BEQ $B391       unbedingter Sprung

                                *** Test auf Direkt-Modus
.,B3A6 A6 3A    LDX $3A         Flag laden (Direktm. = $FF)
.,B3A8 E8       INX             testen
.,B3A9 D0 A0    BNE $B34B       nein: dann RTS
.,B3AB A2 15    LDX #$15        Nummer für 'illegal direct'
.:B3AD 2C       .BYTE $2C
.,B3AE A2 1B    LDX #$1B        Nummer für 'undef'd function'
.,B3B0 4C 37 A4 JMP $A437       Fehlermeldung ausgeben

                                *** BASIC-Befehl DEF FN
.,B3B3 20 E1 B3 JSR $B3E1       prüft FN-Syntax
.,B3B6 20 A6 B3 JSR $B3A6       testet auf Direkt-Modus
.,B3B9 20 FA AE JSR $AEFA       prüft auf 'Klammer auf
.,B3BC A9 80    LDA #$80        Wert laden
.,B3BE 85 10    STA $10         sperrt INTEGER-Variable
.,B3C0 20 8B B0 JSR $B08B       sucht Variable
.,B3C3 20 8D AD JSR $AD8D       prüft auf numerisch
.,B3C6 20 F7 AE JSR $AEF7       prüft auf 'Klammer zu'
.,B3C9 A9 B2    LDA #$B2        '=' BASIC-Code
.,B3CB 20 FF AE JSR $AEFF       prüft auf '='
.,B3CE 48       PHA             erstes Zeichen auf Stapel
.,B3CF A5 48    LDA $48         LOW- und HIGH-Byte der
.,B3D1 48       PHA             FN-Variablen-Adresse
.,B3D2 A5 47    LDA $47         auf den Stapel
.,B3D4 48       PHA             legen
.,B3D5 A5 7B    LDA $7B         LOW- und HIGH-Byte
.,B3D7 48       PHA             des Programmzeigers
.,B3D8 A5 7A    LDA $7A         auf den Stapel
.,B3DA 48       PHA             legen
.,B3DB 20 F8 A8 JSR $A8F8       Programmzeiger auf Statement
.,B3DE 4C 4F B4 JMP $B44F       FN-Variable vom Stapel holen

                                *** prüft FN-Syntax
.,B3E1 A9 A5    LDA #$A5        FN-Code
.,B3E3 20 FF AE JSR $AEFF       prüft auf FN-Code
.,B3E6 09 80    ORA #$80        Wert laden
.,B3E8 85 10    STA $10         sperrt INTEGER-Variable
.,B3EA 20 92 B0 JSR $B092       sucht Variable
.,B3ED 85 4E    STA $4E         LOW- und HIGH-Byte
.,B3EF 84 4F    STY $4F         FN-Variablenzeiger setzen
.,B3F1 4C 8D AD JMP $AD8D       prüft auf numerisch

                                *** BASIC-Funktion FN
.,B3F4 20 E1 B3 JSR $B3E1       prüft FN-Syntax
.,B3F7 A5 4F    LDA $4F         LOW- und HiGH-Byte des
.,B3F9 48       PHA             FN-Variablenzeigers
.,B3FA A5 4E    LDA $4E         auf den Stapel
.,B3FC 48       PHA             legen
.,B3FD 20 F1 AE JSR $AEF1       holt Term in Klammern
.,B400 20 8D AD JSR $AD8D       prüft auf numerisch
.,B403 68       PLA             LOW- und HIGH-Byte
.,B404 85 4E    STA $4E         des
.,B406 68       PLA             FN-Variablenzeigers wieder-
.,B407 85 4F    STA $4F         holen und speichern
.,B409 A0 02    LDY #$02        Zeiger setzen
.,B40B B1 4E    LDA ($4E),Y     Zeiger (LOW) auf FN-Variable
.,B40D 85 47    STA $47         in Variablenadresszeiger
.,B40F AA       TAX             und ins X-Reg.
.,B410 C8       INY             Zeiger erhöhen
.,B411 B1 4E    LDA ($4E),Y     Zeiger (HIGH) laden
.,B413 F0 99    BEQ $B3AE       gibt 'undef'd function'
.,B415 85 48    STA $48         in Variablenadresse
.,B417 C8       INY             Zeiger erhöhen
.,B418 B1 47    LDA ($47),Y     FN-Variablenwert holen
.,B41A 48       PHA             und auf Stapel retten
.,B41B 88       DEY             Zeiger vermindern
.,B41C 10 FA    BPL $B418       fertig? nein: nächster Wert
.,B41E A4 48    LDY $48
.,B420 20 D4 BB JSR $BBD4       FAC in FN-Variable übertragen
.,B423 A5 7B    LDA $7B         Programmzeiger (LOW)
.,B425 48       PHA             auf Stapel
.,B426 A5 7A    LDA $7A         Programmzeiger (HIGH)
.,B428 48       PHA             auf Stapel
.,B429 B1 4E    LDA ($4E),Y     LOW und HIGH-Byte
.,B42B 85 7A    STA $7A         des
.,B42D C8       INY             Programmzeigers auf
.,B42E B1 4E    LDA ($4E),Y     FN-Ausdruck
.,B430 85 7B    STA $7B         speichern
.,B432 A5 48    LDA $48         Zeiger auf FN-Variable
.,B434 48       PHA             holen und
.,B435 A5 47    LDA $47         auf den Stapel
.,B437 48       PHA             retten
.,B438 20 8A AD JSR $AD8A       numerischen Ausdruck holen
.,B43B 68       PLA             LOW- und HIGH-Byte
.,B43C 85 4E    STA $4E         des Zeigers auf FN-
.,B43E 68       PLA             Variable vom Stapel holen
.,B43F 85 4F    STA $4F         und in FN-Zeiger speichern
.,B441 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,B444 F0 03    BEQ $B449       keine weiteren Zeichen?
.,B446 4C 08 AF JMP $AF08       gibt 'SYNTAX ERROR'
.,B449 68       PLA             LOW- und HIGH-Byte
.,B44A 85 7A    STA $7A         des
.,B44C 68       PLA             Programmzeigers
.,B44D 85 7B    STA $7B         zurückholen
.,B44F A0 00    LDY #$00        Zeiger setzen
.,B451 68       PLA             FN-Variable vom Stapel
.,B452 91 4E    STA ($4E),Y     zurückholen
.,B454 68       PLA             und abspeichern
.,B455 C8       INY             Zeiger erhöhen
.,B456 91 4E    STA ($4E),Y     2. Wert abspeichern
.,B458 68       PLA             3. Wert vom Stapel holen
.,B459 C8       INY             Zeiger erhöhen
.,B45A 91 4E    STA ($4E),Y     und abspeichern
.,B45C 68       PLA             4. Wert vom Stapel holen
.,B45D C8       INY             Zeiger erhöhen
.,B45E 91 4E    STA ($4E),Y     und abspeichern
.,B460 68       PLA             5. Wert vom Stapel holen
.,B461 C8       INY             Zeiger erhöhen
.,B462 91 4E    STA ($4E),Y     und abspeichern
.,B464 60       RTS             Rücksprung

                                *** BASIC-Funktion STR$
.,B465 20 8D AD JSR $AD8D       prüft auf numerisch
.,B468 A0 00    LDY #$00        Wert laden und
.,B46A 20 DF BD JSR $BDDF       FAC nach ASCII umwandeln
.,B46D 68       PLA             Rücksprungadresse vom
.,B46E 68       PLA             Stapel entfernen
.,B46F A9 FF    LDA #$FF        LOW-Byte
.,B471 A0 00    LDY #$00        Startadresse des Strings=$FF
.,B473 F0 12    BEQ $B487

                                *** Stringzeiger berechnen
.,B475 A6 64    LDX $64         Zeiger in
.,B477 A4 65    LDY $65         $64/65 in
.,B479 86 50    STX $50         Zeiger auf Stringdescriptor
.,B47B 84 51    STY $51         speichern
.,B47D 20 F4 B4 JSR $B4F4       Platz für String, Länge in A
.,B480 86 62    STX $62         Adresse LOW
.,B482 84 63    STY $63         Adresse HIGH
.,B484 85 61    STA $61         Länge
.,B486 60       RTS

                                *** String holen, Zeiger in A/Y
.,B487 A2 22    LDX #$22        '"'-Code
.,B489 86 07    STX $07         nach Suchzeichen
.,B48B 86 08    STX $08         und Hochkommaflag
.,B48D 85 6F    STA $6F         Startadresse des Strings
.,B48F 84 70    STY $70         nach $6F/70
.,B491 85 62    STA $62         und $62/63
.,B493 84 63    STY $63         speichern
.,B495 A0 FF    LDY #$FF        Zeiger setzen
.,B497 C8       INY             Zeiger erhöhen
.,B498 B1 6F    LDA ($6F),Y     nächstes Zeichen des Strings
.,B49A F0 0C    BEQ $B4A8       Endekennzeichen?
.,B49C C5 07    CMP $07         Suchzeichen?
.,B49E F0 04    BEQ $B4A4       ja: $B4A4
.,B4A0 C5 08    CMP $08         = Zeichen in Hochkommaflag
.,B4A2 D0 F3    BNE $B497       nein: $B497
.,B4A4 C9 22    CMP #$22        '"'-Code?
.,B4A6 F0 01    BEQ $B4A9       ja: $B4A9
.,B4A8 18       CLC             Carry löschen (Addition)
.,B4A9 84 61    STY $61         Länge des Str. speichern und
.,B4AB 98       TYA             in Akku holen
.,B4AC 65 6F    ADC $6F         und zur Startadresse addieren
.,B4AE 85 71    STA $71         ergibt Endadresse LOW + 1
.,B4B0 A6 70    LDX $70         Übertrag
.,B4B2 90 01    BCC $B4B5       Addition umgehen
.,B4B4 E8       INX             Übertrag addieren
.,B4B5 86 72    STX $72         Endadresse HIGH + 1
.,B4B7 A5 70    LDA $70         Startadresse HIGH
.,B4B9 F0 04    BEQ $B4BF       null?
.,B4BB C9 02    CMP #$02        zwei?
.,B4BD D0 0B    BNE $B4CA       nein: $B4CA
.,B4BF 98       TYA             Länge in Akku
.,B4C0 20 75 B4 JSR $B475       Stringzeiger berechnen
.,B4C3 A6 6F    LDX $6F         LOW- und HIGH-Byte der
.,B4C5 A4 70    LDY $70         Startadresse holen
.,B4C7 20 88 B6 JSR $B688       String in Bereich kopieren

                                *** Stringzeiger in
                                *** Descriptorstapel bringen
.,B4CA A6 16    LDX $16         Stringdescriptor-Zeiger
.,B4CC E0 22    CPX #$22        Stringstapel voll?
.,B4CE D0 05    BNE $B4D5       nein: $B4D5
.,B4D0 A2 19    LDX #$19        Nr für 'formula too complex'
.,B4D2 4C 37 A4 JMP $A437       Fehlermeldung ausgeben
.,B4D5 A5 61    LDA $61         Stringlänge holen und
.,B4D7 95 00    STA $00,X       Stringstapel speichern
.,B4D9 A5 62    LDA $62         LOW- und HIGH-Byte der
.,B4DB 95 01    STA $01,X       Adresse holen
.,B4DD A5 63    LDA $63         und in
.,B4DF 95 02    STA $02,X       Stringstapel bringen
.,B4E1 A0 00    LDY #$00        Nullwert laden
.,B4E3 86 64    STX $64         und Zeiger
.,B4E5 84 65    STY $65         jetzt auf Descriptor setzen
.,B4E7 84 70    STY $70         Zeiger für Polynomauswertung
.,B4E9 88       DEY             Register vermindern
.,B4EA 84 0D    STY $0D         Stringflag setzen $FF
.,B4EC 86 17    STX $17         Index des letzten
.,B4EE E8       INX             Stringdescriptors
.,B4EF E8       INX             um drei erhöhen
.,B4F0 E8       INX             und als
.,B4F1 86 16    STX $16         neuen Index merken
.,B4F3 60       RTS             Rücksprung

                                *** Platz für String reservieren,
                                *** Länge in A
.,B4F4 46 0F    LSR $0F         Flag für Garbage Collection
                                zurücksetzen
.,B4F6 48       PHA             Stringlänge
.,B4F7 49 FF    EOR #$FF        Alle Bits umdrehen
.,B4F9 38       SEC             mit HIGH-Byte des
.,B4FA 65 33    ADC $33         Stringanfangs-Zeigers addieren
.,B4FC A4 34    LDY $34         LOW-Byte ins Y-Reg.
.,B4FE B0 01    BCS $B501       Carry gesetzt ? dann weiter
.,B500 88       DEY             ansonsten LOW-Byte erniedrigen
.,B501 C4 32    CPY $32         Zu wenig Platz, dann
.,B503 90 11    BCC $B516       Garbage Collection durchführen
.,B505 D0 04    BNE $B50B       alles ok ?
.,B507 C5 31    CMP $31         Ende der Arrays, dann
.,B509 90 0B    BCC $B516       Garbage Collect durchführen
.,B50B 85 33    STA $33         ansonsten
.,B50D 84 34    STY $34         alle
.,B50F 85 35    STA $35         Zeiger
.,B511 84 36    STY $36         neu
.,B513 AA       TAX             setzen
.,B514 68       PLA             Stringlänge zurückholen
.,B515 60       RTS             Rücksprung
.,B516 A2 10    LDX #$10        Nummer für 'OUT OF MEMORY'
.,B518 A5 0F    LDA $0F         Flag für Garbage Collection
.,B51A 30 B6    BMI $B4D2       durchgeführt? 'OUT OF MEMORY'
.,B51C 20 26 B5 JSR $B526       Garbage Collection
.,B51F A9 80    LDA #$80        Flag setzen
.,B521 85 0F    STA $0F         und speichern
.,B523 68       PLA             Stringlänge
.,B524 D0 D0    BNE $B4F6       String nochmals einbauen

                                *** Garbage Collection
.,B526 A6 37    LDX $37         LOW-Byte Basic-RAM-Zeiger
.,B528 A5 38    LDA $38         HIGH-Byte Basic-RAM-Zeiger
.,B52A 86 33    STX $33         in Stringzeiger
.,B52C 85 34    STA $34         speichern
.,B52E A0 00    LDY #$00        LOW- und HIGH-Byte
.,B530 84 4F    STY $4F         der FN Zeiger
.,B532 84 4E    STY $4E         auf Null setzen
.,B534 A5 31    LDA $31         LOW- und HIGH-Byte der
.,B536 A6 32    LDX $32         Array-Zeiger laden
.,B538 85 5F    STA $5F         und in die Arithmetikregister
.,B53A 86 60    STX $60         speichern
.,B53C A9 19    LDA #$19        Startadresse
.,B53E A2 00    LDX #$00        der Descriptorentabelle
.,B540 85 22    STA $22         als Suchzeiger nach
.,B542 86 23    STX $23         $22 und $23 bringen
.,B544 C5 16    CMP $16         identisch mit String-Zeiger?
.,B546 F0 05    BEQ $B54D       wenn ja, dann weiter
.,B548 20 C7 B5 JSR $B5C7       Stringposition feststellen
.,B54B F0 F7    BEQ $B544       unbedingter Sprung
.,B54D A9 07    LDA #$07        Schrittweite für die Suche
.,B54F 85 53    STA $53         in Variablentabelle
.,B551 A5 2D    LDA $2D         Tabellenzeiger
.,B553 A6 2E    LDX $2E         laden
.,B555 85 22    STA $22         und als Suchzeiger nach
.,B557 86 23    STX $23         $22 und $23 bringen
.,B559 E4 30    CPX $30         Am Ende der Tabelle angelangt
.,B55B D0 04    BNE $B561       wenn nicht, dann zu $B561
.,B55D C5 2F    CMP $2F         ansonsten Sprung zur
.,B55F F0 05    BEQ $B566       Array-Behandlung
.,B561 20 BD B5 JSR $B5BD       Stringposition feststellen
.,B564 F0 F3    BEQ $B559       unbedingter Sprung
.,B566 85 58    STA $58         Zeiger in die
.,B568 86 59    STX $59         Array-Tabelle speichern
.,B56A A9 03    LDA #$03        Schrittweite für Suche
.,B56C 85 53    STA $53         innerhalb des Arrays festlegen
.,B56E A5 58    LDA $58         Am Ende
.,B570 A6 59    LDX $59         der
.,B572 E4 32    CPX $32         Arraytabelle angelangt, dann
.,B574 D0 07    BNE $B57D       Sprung zu $B57D
.,B576 C5 31    CMP $31         Vergleich mit HIGH-Byte
.,B578 D0 03    BNE $B57D       Sprung zu $B57D
.,B57A 4C 06 B6 JMP $B606       ansonsten Transfer
.,B57D 85 22    STA $22         Zeiger auf Array-Header
.,B57F 86 23    STX $23         stellen
.,B581 A0 00    LDY #$00        Zähler auf Null setzen
.,B583 B1 22    LDA ($22),Y     Variablenname erstes Zeichen
.,B585 AA       TAX             ins X-Reg übertragen
.,B586 C8       INY             Zähler erhöhen
.,B587 B1 22    LDA ($22),Y     Variablenname zweites Zeichen
.,B589 08       PHP             Statusregister retten
.,B58A C8       INY             Zähler erhöhen
.,B58B B1 22    LDA ($22),Y     Die Länge
.,B58D 65 58    ADC $58         des Arrays
.,B58F 85 58    STA $58         zu
.,B591 C8       INY             Zeiger
.,B592 B1 22    LDA ($22),Y     auf
.,B594 65 59    ADC $59         Arraytabelle
.,B596 85 59    STA $59         addieren
.,B598 28       PLP             Statusregister wiederholen
.,B599 10 D3    BPL $B56E       keine Stringvariable ?
.,B59B 8A       TXA             dann weitersuchen
.,B59C 30 D0    BMI $B56E       Stringvariable, nein, weiter
.,B59E C8       INY             Zähler erhöhen
.,B59F B1 22    LDA ($22),Y     Dimensionenanzahl holen
.,B5A1 A0 00    LDY #$00        Zähler wieder Null
.,B5A3 0A       ASL             mal 2
.,B5A4 69 05    ADC #$05        plus 5
.,B5A6 65 22    ADC $22         zum Zeiger addieren
.,B5A8 85 22    STA $22         und speichern
.,B5AA 90 02    BCC $B5AE       wenn ungleich, dann zu $B5AE
.,B5AC E6 23    INC $23         Zeiger erhöhen
.,B5AE A6 23    LDX $23         und in Array schieben
.,B5B0 E4 59    CPX $59         auf nächstes Feld vergleichen
.,B5B2 D0 04    BNE $B5B8       wenn ungleich, dann zu $B5B8
.,B5B4 C5 58    CMP $58         wenn gleich, dann
.,B5B6 F0 BA    BEQ $B572       zu $B572
.,B5B8 20 C7 B5 JSR $B5C7       Stringposition feststellen
.,B5BB F0 F3    BEQ $B5B0       unbedingter Sprung

                                *** prüft Beseitigungsmöglichkeit
.,B5BD B1 22    LDA ($22),Y     Variablenname erstes Zeichen
.,B5BF 30 35    BMI $B5F6       Integer o. Funktion ?
.,B5C1 C8       INY             Zähler erhöhen
.,B5C2 B1 22    LDA ($22),Y     Variablenname zweites Zeichen
.,B5C4 10 30    BPL $B5F6       wenn Real, dann $B5F6
.,B5C6 C8       INY             Zähler erhöhen
.,B5C7 B1 22    LDA ($22),Y     holt Stringlänge
.,B5C9 F0 2B    BEQ $B5F6       wenn Stringlänge=0,dann $B5F6
.,B5CB C8       INY             Zähler erhöhen
.,B5CC B1 22    LDA ($22),Y     holt Startadresse des Strings
.,B5CE AA       TAX             schiebt ins X-Reg
.,B5CF C8       INY             Zähler erhöhen
.,B5D0 B1 22    LDA ($22),Y     holt Sringzeiger
.,B5D2 C5 34    CMP $34         Vergleich mit $34
.,B5D4 90 06    BCC $B5DC       wenn gleich, dann $B5DC
.,B5D6 D0 1E    BNE $B5F6       wenn größer, dann $B5F6
.,B5D8 E4 33    CPX $33         mit $33 vergleichen
.,B5DA B0 1A    BCS $B5F6       wenn gleich, dann $B5F6
.,B5DC C5 60    CMP $60         Vergleich mit $60
.,B5DE 90 16    BCC $B5F6       wenn gleich, dann $B5F6
.,B5E0 D0 04    BNE $B5E6       wenn größer, dann $B5E6
.,B5E2 E4 5F    CPX $5F         Vergleich mit $5F
.,B5E4 90 10    BCC $B5F6       wenn gleich, dann $B5F6
.,B5E6 86 5F    STX $5F         Startadresse des
.,B5E8 85 60    STA $60         Strings speichern
.,B5EA A5 22    LDA $22         Stringdescriptor
.,B5EC A6 23    LDX $23         laden
.,B5EE 85 4E    STA $4E         und
.,B5F0 86 4F    STX $4F         speichern
.,B5F2 A5 53    LDA $53         Tabellen Schrittweite laden
.,B5F4 85 55    STA $55         und speichern
.,B5F6 A5 53    LDA $53         und zum
.,B5F8 18       CLC             Suchzeiger
.,B5F9 65 22    ADC $22         addieren
.,B5FB 85 22    STA $22         und wieder
.,B5FD 90 02    BCC $B601       speichern
.,B5FF E6 23    INC $23         Zeiger erhöhen
.,B601 A6 23    LDX $23         und laden
.,B603 A0 00    LDY #$00        Zähler löschen
.,B605 60       RTS             Rücksprung

                                *** Strings zusammenfügen
.,B606 A5 4F    LDA $4F         String zwischen Tabellenende
.,B608 05 4E    ORA $4E         und dem oberen RAM-Bereich
.,B60A F0 F5    BEQ $B601       gefunden ? nein, dann RTS
.,B60C A5 55    LDA $55         Arraysuchlauf, dann $55=03
.,B60E 29 04    AND #$04        ansonsten $55=07
.,B610 4A       LSR             wenn Einzelvariable, dann
.,B611 A8       TAY             Y-Reg =2 und 0 bei Array
.,B612 85 55    STA $55         Wert sichern
.,B614 B1 4E    LDA ($4E),Y     Stringlänge holen
.,B616 65 5F    ADC $5F         zum LOW-Byte der Stringanfangs-
.,B618 85 5A    STA $5A         adresse Add., =Endadresse +1
.,B61A A5 60    LDA $60         auf gleiche
.,B61C 69 00    ADC #$00        Weise das
.,B61E 85 5B    STA $5B         HIGH-Byte berechnen
.,B620 A5 33    LDA $33         Zielbereich
.,B622 A6 34    LDX $34         für den
.,B624 85 58    STA $58         Transfer
.,B626 86 59    STX $59         holen
.,B628 20 BF A3 JSR $A3BF       Strings verschieben
.,B62B A4 55    LDY $55         LOW-Byte
.,B62D C8       INY             der
.,B62E A5 58    LDA $58         Anfangsadresse in
.,B630 91 4E    STA ($4E),Y     Descriptor speichern
.,B632 AA       TAX             HIGH-Byte
.,B633 E6 59    INC $59         der Anfangsadresse
.,B635 A5 59    LDA $59         in
.,B637 C8       INY             Descriptor
.,B638 91 4E    STA ($4E),Y     bringen
.,B63A 4C 2A B5 JMP $B52A       nicht alles ?, dann weiter
                                Stringverknüpfung '+'
.,B63D A5 65    LDA $65         HIGH-Byte des Descriptors vom
.,B63F 48       PHA             ersten String auf Stack
.,B640 A5 64    LDA $64         LOW-Byte
.,B642 48       PHA             in Stack
.,B643 20 83 AE JSR $AE83       zweiten String holen
.,B646 20 8F AD JSR $AD8F       prüft auf Stringvariable
.,B649 68       PLA             Descriptorzeiger des ersten
.,B64A 85 6F    STA $6F         Strings wiederholen
.,B64C 68       PLA             und
.,B64D 85 70    STA $70         speichern
.,B64F A0 00    LDY #$00        Zähler auf Null
.,B651 B1 6F    LDA ($6F),Y     Länge des ersten Strings
.,B653 18       CLC             plus Länge
.,B654 71 64    ADC ($64),Y     des zweiten Strings
.,B656 90 05    BCC $B65D       kleiner als 256
.,B658 A2 17    LDX #$17        Nummer für 'STRING TOO LONG'
.,B65A 4C 37 A4 JMP $A437       Fehlermeldung ausgeben
.,B65D 20 75 B4 JSR $B475       Platz für verknüpften String
.,B660 20 7A B6 JSR $B67A       ersten String übertragen
.,B663 A5 50    LDA $50         Zeiger auf
.,B665 A4 51    LDY $51         zweiten Stringdescriptor
.,B667 20 AA B6 JSR $B6AA       FRESTR
.,B66A 20 8C B6 JSR $B68C       2. String an 1. anhängen
.,B66D A5 6F    LDA $6F         Descriptorzeiger des
.,B66F A4 70    LDY $70         zweiten Strings
.,B671 20 AA B6 JSR $B6AA       FRESTR
.,B674 20 CA B4 JSR $B4CA       Descriptor in Stringstack
.,B677 4C B8 AD JMP $ADB8       zurück zur Formelauswertung

                                *** String in reserv. Bereich
.,B67A A0 00    LDY #$00        Zähler auf Null
.,B67C B1 6F    LDA ($6F),Y     Stringlänge holen
.,B67E 48       PHA             und merken
.,B67F C8       INY             Zähler erhöhen
.,B680 B1 6F    LDA ($6F),Y     LOW-Byte der Stringadresse
.,B682 AA       TAX             ins X-Reg
.,B683 C8       INY             Zähler erhöhen
.,B684 B1 6F    LDA ($6F),Y     HIGH-Byte der Stringadresse
.,B686 A8       TAY             ins Y-Reg und
.,B687 68       PLA             Stack
.,B688 86 22    STX $22         Zeiger auf
.,B68A 84 23    STY $23         String speichern
.,B68C A8       TAY             Länge null ?
.,B68D F0 0A    BEQ $B699       dann fertig
.,B68F 48       PHA             wieder in Stack
.,B690 88       DEY             Zähler erniedrigen
.,B691 B1 22    LDA ($22),Y     String
.,B693 91 35    STA ($35),Y     in den
.,B695 98       TYA             Stringbereich
.,B696 D0 F8    BNE $B690       übertragen
.,B698 68       PLA             Den
.,B699 18       CLC             Zeiger
.,B69A 65 35    ADC $35         um
.,B69C 85 35    STA $35         die
.,B69E 90 02    BCC $B6A2       Stringlänge
.,B6A0 E6 36    INC $36         erhöhen
.,B6A2 60       RTS             Rücksprung

                                *** Stringverwaltung FRESTR
.,B6A3 20 8F AD JSR $AD8F       prüft auf Stringvariable
.,B6A6 A5 64    LDA $64         Zeiger auf
.,B6A8 A4 65    LDY $65         Stringdescriptor
.,B6AA 85 22    STA $22         nach
.,B6AC 84 23    STY $23         $22 und $23 bringen
.,B6AE 20 DB B6 JSR $B6DB       Descriptor vom Stringstack
.,B6B1 08       PHP             Statusregister retten
.,B6B2 A0 00    LDY #$00        Zähler auf Null
.,B6B4 B1 22    LDA ($22),Y     Stringlänge holen
.,B6B6 48       PHA             und in Stack schieben
.,B6B7 C8       INY             Zähler erhöhen
.,B6B8 B1 22    LDA ($22),Y     LOW-Byte der Anfangsadresse
.,B6BA AA       TAX             ins X-Reg schieben
.,B6BB C8       INY             Zähler erhöhen
.,B6BC B1 22    LDA ($22),Y     HIGH-Byte der Anfangsadresse
.,B6BE A8       TAY             ins Y-Reg schieben
.,B6BF 68       PLA             Stringlänge wieder aus Stack
.,B6C0 28       PLP             Statusreg. wieder aus Stack
.,B6C1 D0 13    BNE $B6D6       Neustring=Altstring nein? RTS
.,B6C3 C4 34    CPY $34         Stringadresse identisch mit
.,B6C5 D0 0F    BNE $B6D6       Zeiger auf Stringende?
.,B6C7 E4 33    CPX $33         nein, dann
.,B6C9 D0 0B    BNE $B6D6       zu $B6D6
.,B6CB 48       PHA             String-Anfangszeiger
.,B6CC 18       CLC             auf Länge
.,B6CD 65 33    ADC $33         des
.,B6CF 85 33    STA $33         Strings
.,B6D1 90 02    BCC $B6D5       hinaufsetzen
.,B6D3 E6 34    INC $34         Stringlänge
.,B6D5 68       PLA             holen
.,B6D6 86 22    STX $22         LOW-Byte der Startadresse
.,B6D8 84 23    STY $23         HIGH-Byte der Startadresse
.,B6DA 60       RTS             Rücksprung

                                *** Stringzeiger aus
                                *** Descriptorstack entfernen
.,B6DB C4 18    CPY $18         Zeiger auf Stringdescriptor
.,B6DD D0 0C    BNE $B6EB       identisch mit $18, nicht? RTS
.,B6DF C5 17    CMP $17         identisch mit 17
.,B6E1 D0 08    BNE $B6EB       wenn nicht, dann RTS
.,B6E3 85 16    STA $16         Zeiger nach $16 speichern
.,B6E5 E9 03    SBC #$03        Von Adresse $17
.,B6E7 85 17    STA $17         3 abziehen
.,B6E9 A0 00    LDY #$00        Zähler auf Null
.,B6EB 60       RTS             Rücksprung

                                *** BASIC-Funktion CHR$
.,B6EC 20 A1 B7 JSR $B7A1       holt Byte-Wert (0 bis 255)
.,B6EF 8A       TXA             Kode in Akku
.,B6F0 48       PHA             Akkuinhalt in Stack
.,B6F1 A9 01    LDA #$01        Länge des Strings gleich 1
.,B6F3 20 7D B4 JSR $B47D       Platz für String freimachen
.,B6F6 68       PLA             ASCII-Kode zurückholen
.,B6F7 A0 00    LDY #$00        Zähler auf Null
.,B6F9 91 62    STA ($62),Y     als Stringzeichen speichern
.,B6FB 68       PLA             Rücksprungadresse aus
.,B6FC 68       PLA             Stack entfernen
.,B6FD 4C CA B4 JMP $B4CA       Descriptor in Stringstack

                                *** BASIC-Funktion LEFT$
.,B700 20 61 B7 JSR $B761       Stringadresse & Länge
                                aus Stack holen
.,B703 D1 50    CMP ($50),Y     Länge mit LEFT$-Parameter
                                vergleichen
.,B705 98       TYA             LEFT$-Parameter
.,B706 90 04    BCC $B70C       kleiner als Stringlänge ?
.,B708 B1 50    LDA ($50),Y     Stringlänge holen
.,B70A AA       TAX             und ins X-Reg schieben
.,B70B 98       TYA             Stringlänge und
.,B70C 48       PHA             Parameter für LEFT$
.,B70D 8A       TXA             in Stack
.,B70E 48       PHA             schieben
.,B70F 20 7D B4 JSR $B47D       Platz für neuen String
                                reservieren
.,B712 A5 50    LDA $50         Zeiger auf Stringdescriptor
.,B714 A4 51    LDY $51         laden
.,B716 20 AA B6 JSR $B6AA       FRESTR
.,B719 68       PLA             Länge des neuen Strings aus
.,B71A A8       TAY             Stack holen und ins X-Reg
.,B71B 68       PLA             alte
.,B71C 18       CLC             Stringadresse
.,B71D 65 22    ADC $22         entsprechend
.,B71F 85 22    STA $22         erhöhen
.,B721 90 02    BCC $B725       und speichern
.,B723 E6 23    INC $23         HIGH-Byte erhöhen
.,B725 98       TYA             neue Stringlänge holen
.,B726 20 8C B6 JSR $B68C       neuen String in
                                Stringbereich übertragen
.,B729 4C CA B4 JMP $B4CA       Descriptor in Stringstack
                                bringen

                                *** BASIC-Funktion RIGHT$
.,B72C 20 61 B7 JSR $B761       Stringparameter und Länge
                                vom Stack holen
.,B72F 18       CLC             von Stringlänge
.,B730 F1 50    SBC ($50),Y     abziehen
.,B732 49 FF    EOR #$FF        Nummer des ersten Elements
                                im alten String
.,B734 4C 06 B7 JMP $B706       weiter wie LEFT$

                                *** BASIC-Funktion MID$
.,B737 A9 FF    LDA #$FF        Ersatzwert für den zweiten
.,B739 85 65    STA $65         Zahlenparameter
.,B73B 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,B73E C9 29    CMP #$29        ')' Klammer zu
.,B740 F0 06    BEQ $B748       wenn ja, dann kein zweiter
                                Parameter, weiter bei $B748
.,B742 20 FD AE JSR $AEFD       prüft auf Komma
.,B745 20 9E B7 JSR $B79E       holt Byte-Wert des zweiten
                                Parameters
.,B748 20 61 B7 JSR $B761       Stringparameter und
                                Startposition holen
.,B74B F0 4B    BEQ $B798       1. Parameter null, 'ILLEGAL
                                QUANTITY'
.,B74D CA       DEX             erste Elementposition
.,B74E 8A       TXA             innerhalb
.,B74F 48       PHA             des alten Strings
.,B750 18       CLC             im Stack ablegen
.,B751 A2 00    LDX #$00        Zähler setzen
.,B753 F1 50    SBC ($50),Y     alte Stringlänge kleiner als
                                erster Parameter ?
.,B755 B0 B6    BCS $B70D       wenn ja, dann zu LEFT$
.,B757 49 FF    EOR #$FF        Berechnen der neuen Länge
.,B759 C5 65    CMP $65         wenn kleiner als zweiter
.,B75B 90 B1    BCC $B70E       Parameter, dann zu LEFT$
.,B75D A5 65    LDA $65         Zweitparameter als 'rechte'
                                Stringbegrenzung
.,B75F B0 AD    BCS $B70E       unbedingter Sprung

                                *** Stringparameter numerischer Wert
                                *** vom Stack holen
.,B761 20 F7 AE JSR $AEF7       prüft auf Klammer zu
.,B764 68       PLA             LOW-Byte der
.,B765 A8       TAY             Aufrufadresse merken
.,B766 68       PLA             HIGH-Byte der
.,B767 85 55    STA $55         Aufrufadresse merken
.,B769 68       PLA             LOW-und HIGH-Byte der
.,B76A 68       PLA             Aufrufadresse merken
.,B76B 68       PLA             1. Parameter holen
.,B76C AA       TAX             und ins X-Reg
.,B76D 68       PLA             LOW- und HIGH-Byte
.,B76E 85 50    STA $50         des
.,B770 68       PLA             Stringdescriptors
.,B771 85 51    STA $51         nach
.,B773 A5 55    LDA $55         $51 und $52 speichern
.,B775 48       PHA             Aufrufadresse
.,B776 98       TYA             wieder auf
.,B777 48       PHA             Stack
.,B778 A0 00    LDY #$00        Zähler auf Null
.,B77A 8A       TXA             Länge, zweiter Parameter
.,B77B 60       RTS             Rücksprung

                                *** BASIC-Funktion LEN
.,B77C 20 82 B7 JSR $B782       FRESTR, Stringlänge holen
.,B77F 4C A2 B3 JMP $B3A2       Byte-Wert nach
                                Fließkommaformat wandeln

                                *** Stringparameter holen
.,B782 20 A3 B6 JSR $B6A3       FRESTR, String holen, Länge
                                in A
.,B785 A2 00    LDX #$00        Typeflag
.,B787 86 0D    STX $0D         auf numerisch setzen
.,B789 A8       TAY             Länge in Y
.,B78A 60       RTS             Rücksprung

                                *** BASIC-Funktion ASC
.,B78B 20 82 B7 JSR $B782       String holen, Zeiger in
                                $22/$23, Länge in Y
.,B78E F0 08    BEQ $B798       Länge gleich null,
                                'ILLEGAL QUANTITY'
.,B790 A0 00    LDY #$00        Zähler auf Null
.,B792 B1 22    LDA ($22),Y     erstes Zeichen holen
.,B794 A8       TAY             ASCII-Kode
.,B795 4C A2 B3 JMP $B3A2       nach Fließkomma wandeln
.,B798 4C 48 B2 JMP $B248       'ILLEGAL QUANTITY'

                                *** holt Byte-Wert nach X
.,B79B 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,B79E 20 8A AD JSR $AD8A       FRMNUM numerischen Wert
                                nach FAC holen
.,B7A1 20 B8 B1 JSR $B1B8       prüft auf Bereich und
                                wandelt nach Integer
.,B7A4 A6 64    LDX $64         HIGH-Byte
.,B7A6 D0 F0    BNE $B798       ungleich null, dann
                                'ILLEGAL QUANTITY'
.,B7A8 A6 65    LDX $65         LOW-Byte des geholten
                                Ausdrucks ins X-Reg
.,B7AA 4C 79 00 JMP $0079       CHRGOT letztes Zeichen holen

                                *** BASIC-Funktion VAL
.,B7AD 20 82 B7 JSR $B782       Stringadresse und Länge holen
.,B7B0 D0 03    BNE $B7B5       Stringlänge ungleich Null ?
.,B7B2 4C F7 B8 JMP $B8F7       Null in FAC
.,B7B5 A6 7A    LDX $7A         Programmzeiger
.,B7B7 A4 7B    LDY $7B         holen
.,B7B9 86 71    STX $71         und
.,B7BB 84 72    STY $72         speichern
.,B7BD A6 22    LDX $22         Stringanfangsadresse
.,B7BF 86 7A    STX $7A         in Stringzeiger bringen
.,B7C1 18       CLC             LOW-Byte des
.,B7C2 65 22    ADC $22         ersten Zeichens
.,B7C4 85 24    STA $24         nach dem String speichern
.,B7C6 A6 23    LDX $23         HIGH-Byte
.,B7C8 86 7B    STX $7B         des ersten
.,B7CA 90 01    BCC $B7CD       Zeichens
.,B7CC E8       INX             nach dem String
.,B7CD 86 25    STX $25         speichern
.,B7CF A0 00    LDY #$00        Zähler auf Null
.,B7D1 B1 24    LDA ($24),Y     erstes Byte nach String
.,B7D3 48       PHA             auf Stack
.,B7D4 98       TYA             speichern
.,B7D5 91 24    STA ($24),Y     und durch null ersetzen
.,B7D7 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,B7DA 20 F3 BC JSR $BCF3       String in Fließkommazahl
                                umwandeln
.,B7DD 68       PLA             Zeichen nach String
.,B7DE A0 00    LDY #$00        Zähler auf Null
.,B7E0 91 24    STA ($24),Y     wieder zurücksetzen
.,B7E2 A6 71    LDX $71         Die
.,B7E4 A4 72    LDY $72         Programmzeiger
.,B7E6 86 7A    STX $7A         wieder
.,B7E8 84 7B    STY $7B         zurückholen
.,B7EA 60       RTS             Rücksprung

                                *** GETADR und GETBYT holt
                                *** 16-Bit und 8-Bit-Wert
.,B7EB 20 8A AD JSR $AD8A       FRMNUM holt numerischen Wert
.,B7EE 20 F7 B7 JSR $B7F7       FAC in Adressformat wandlen
                                $14/$15
.,B7F1 20 FD AE JSR $AEFD       CHKCOM prüft auf Komma
.,B7F4 4C 9E B7 JMP $B79E       holt Byte-Wert nach X

                                *** GETADR FAC in positive
                                *** 16-Bit-Zahl wandeln
.,B7F7 A5 66    LDA $66         Vorzeichen
.,B7F9 30 9D    BMI $B798       negativ, dann
                                'ILLEGAL QUANTITY'
.,B7FB A5 61    LDA $61         Exponent
.,B7FD C9 91    CMP #$91        Zahl mit 65536 vergleichen
.,B7FF B0 97    BCS $B798       größer, dann
.,B801 20 9B BC JSR $BC9B       'ILLEGAL QUANTITY'
                                FAC in Adressformat wandeln
.,B804 A5 64    LDA $64         Wert
.,B806 A4 65    LDY $65         holen
.,B808 84 14    STY $14         und nach $14/$15
.,B80A 85 15    STA $15         speichern
.,B80C 60       RTS             Rücksprung

                                *** BASIC-Funktion PEEK
.,B80D A5 15    LDA $15         $15 und $16
.,B80F 48       PHA             in
.,B810 A5 14    LDA $14         Stack
.,B812 48       PHA             sichern
.,B813 20 F7 B7 JSR $B7F7       FAC nach Adressformat
                                wandeln
.,B816 A0 00    LDY #$00        Zähler auf Null
.,B818 B1 14    LDA ($14),Y     Peek-Wert holen
.,B81A A8       TAY             nach Y-Reg
.,B81B 68       PLA             $15 und $16
.,B81C 85 14    STA $14         wieder
.,B81E 68       PLA             vom Stack
.,B81F 85 15    STA $15         zurückholen
.,B821 4C A2 B3 JMP $B3A2       Y nach Fließkommaformat

                                *** BASIC-Befehl POKE
.,B824 20 EB B7 JSR $B7EB       Poke-Adrefcse und Wert holen
.,B827 8A       TXA             Poke-Wert in Akku
.,B828 A0 00    LDY #$00        Zähler auf Null
.,B82A 91 14    STA ($14),Y     und in Speicher schreiben
.,B82C 60       RTS             Rücksprung

                                *** BASIC-Befehl WAIT
.,B82D 20 EB B7 JSR $B7EB       Adresse und Wert holen
.,B830 86 49    STX $49         zweiter Parameter nach $49
.,B832 A2 00    LDX #$00        Default für dritten Parameter
.,B834 20 79 00 JSR $0079       CHRGOT letztes Zeichen
.,B837 F0 03    BEQ $B83C       kein dritter Parameter ?
.,B839 20 F1 B7 JSR $B7F1       prüft auf Komma und holt
                                Parameter
.,B83C 86 4A    STX $4A         dritter Parameter nach $4A
.,B83E A0 00    LDY #$00        Zähler auf Null
.,B840 B1 14    LDA ($14),Y     Wait-Adresse
.,B842 45 4A    EOR $4A         logisch
.,B844 25 49    AND $49         verknüpfen
.,B846 F0 F8    BEQ $B840       weiter warten
.,B848 60       RTS             Rücksprung

                                *** Arithmetik-Routinen

                                *** FAC = FAC + 0.5
.,B849 A9 11    LDA #$11        Zeiger auf
.,B84B A0 BF    LDY #$BF        Konstante 0.5
.,B84D 4C 67 B8 JMP $B867       FAC = FAC + Konstante (A/Y)

                                *** Minus FAC = Konstante
                                *** (A/Y) - FAC
.,B850 20 8C BA JSR $BA8C       Konstante (A/Y) nach ARG

                                *** Minus FAC = ARG - FAC
.,B853 A5 66    LDA $66         Die
.,B855 49 FF    EOR #$FF        Vorzeichen
.,B857 85 66    STA $66         umdrehen
.,B859 45 6E    EOR $6E         mit Vorzeichen von FAC
.,B85B 85 6F    STA $6F         verknüpfen
.,B85D A5 61    LDA $61         Exponent von FAC
.,B85F 4C 6A B8 JMP $B86A       FAC = FAC + ARG
.,B862 20 99 B9 JSR $B999       Exponenten von FAC und ARG
.,B865 90 3C    BCC $B8A3       angleichen

                                *** Plus FAC = Konstante (A/Y) +
                                *** FAC
.,B867 20 8C BA JSR $BA8C       Konstante (A/Y) nach ARG

                                *** Plus FAC = FAC + ARG
.,B86A D0 03    BNE $B86F       FAC ungleich null ?
.,B86C 4C FC BB JMP $BBFC       nein, dann FAC = ARG
.,B86F A6 70    LDX $70         Rundungsbyte für FAC
.,B871 86 56    STX $56         in $56 speichern
.,B873 A2 69    LDX #$69        Offset-Zeiger für ARG laden
.,B875 A5 69    LDA $69         Exponent von ARG laden
.,B877 A8       TAY             in Y-Reg schieben
.,B878 F0 CE    BEQ $B848       wenn ARG=0, dann RTS
.,B87A 38       SEC             Exponent von
.,B87B E5 61    SBC $61         FAC subtrahieren
.,B87D F0 24    BEQ $B8A3       wenn Exponent gleich, dann zu
                                $B8A3
.,B87F 90 12    BCC $B893       wenn Exponent von FAC größer,
                                dann zu $B893
.,B881 84 61    STY $61         FAC-Exponent durch
                                ARG-Vorzeichen ersetzen
.,B883 A4 6E    LDY $6E         FAC-Vorzeichen durch
.,B885 84 66    STY $66         ARG-Vorzeichen ersetzen
.,B887 49 FF    EOR #$FF        Vorzeichen wechseln
.,B889 69 00    ADC #$00        Carry ist schon 1
.,B88B A0 00    LDY #$00        Rundungsstelle
.,B88D 84 56    STY $56         löschen
.,B88F A2 61    LDX #$61        Offset-Zeiger für FAC laden
.,B891 D0 04    BNE $B897       unbedingter Sprung
.,B893 A0 00    LDY #$00        FAC-Rundungsstelle
.,B895 84 70    STY $70         löschen
.,B897 C9 F9    CMP #$F9        wenn Exponentdifferenz
.,B899 30 C7    BMI $B862       größer als 7, dann zu $B862
.,B89B A8       TAY             Akku löschen
.,B89C A5 70    LDA $70         FAC-Rundungsstelle
.,B89E 56 01    LSR $01,X       laden
.,B8A0 20 B0 B9 JSR $B9B0       Mantisse verschieben
.,B8A3 24 6F    BIT $6F         wenn FAC- und ARG-Vorzeichen
.,B8A5 10 57    BPL $B8FE       identisch, dann zu $B8FE
.,B8A7 A0 61    LDY #$61        Offset-Zeiger für FAC laden
.,B8A9 E0 69    CPX #$69        wenn Offset-Zeiger für ARG
.,B8AB F0 02    BEQ $B8AF       initialisiert, dann zu $B8AF
.,B8AD A0 69    LDY #$69        Offset-Zeiger laden
.,B8AF 38       SEC             Carryflag für Subtraktion
                                setzen
.,B8B0 49 FF    EOR #$FF        Alle Bits umdrehen
.,B8B2 65 56    ADC $56         Rundungsstelle addieren
.,B8B4 85 70    STA $70         und speichern
.,B8B6 B9 04 00 LDA $0004,Y     viertes Byte
.,B8B9 F5 04    SBC $04,X       subtrahieren und in
.,B8BB 85 65    STA $65         FAC speichern
.,B8BD B9 03 00 LDA $0003,Y     drittes Byte
.,B8C0 F5 03    SBC $03,X       subtrahieren und in
.,B8C2 85 64    STA $64         FAC speichern
.,B8C4 B9 02 00 LDA $0002,Y     zweites Byte
.,B8C7 F5 02    SBC $02,X       subtrahieren und in
.,B8C9 85 63    STA $63         FAC speichern
.,B8CB B9 01 00 LDA $0001,Y     erstes Byte
.,B8CE F5 01    SBC $01,X       subtrahieren und in
.,B8D0 85 62    STA $62         FAC speichern
.,B8D2 B0 03    BCS $B8D7       wenn Übertrag negativ, dann
                                weiter
.,B8D4 20 47 B9 JSR $B947       Mantisse von FAC invertieren
.,B8D7 A0 00    LDY #$00        Y-Reg und
.,B8D9 98       TYA             Akku löschen
.,B8DA 18       CLC             Carry löschen
.,B8DB A6 62    LDX $62         wenn $62=0 dann,
.,B8DD D0 4A    BNE $B929       zu $B929
.,B8DF A6 63    LDX $63         Das
.,B8E1 86 62    STX $62         gesamte
.,B8E3 A6 64    LDX $64         FAC
.,B8E5 86 63    STX $63         wieder
.,B8E7 A6 65    LDX $65         norma-
.,B8E9 86 64    STX $64         lisieren
.,B8EB A6 70    LDX $70         Rundungsstelle
.,B8ED 86 65    STX $65         wieder
.,B8EF 84 70    STY $70         löschen
.,B8F1 69 08    ADC #$08        Zähler um 8 Bits verschieben
.,B8F3 C9 20    CMP #$20        wenn 32 Bits verschoben,
.,B8F5 D0 E4    BNE $B8DB       dann weiter
.,B8F7 A9 00    LDA #$00        Mantisse =0
.,B8F9 85 61    STA $61         FAC =0
.,B8FB 85 66    STA $66         Exponent =0
.,B8FD 60       RTS             Rücksprung
.,B8FE 65 56    ADC $56         Rundungsstelle addieren
.,B900 85 70    STA $70         und speichern
.,B902 A5 65    LDA $65         FAC
.,B904 65 6D    ADC $6D         und ARG
.,B906 85 65    STA $65         addieren
.,B908 A5 64    LDA $64         FAC
.,B90A 65 6C    ADC $6C         und ARG
.,B90C 85 64    STA $64         addieren
.,B90E A5 63    LDA $63         FAC
.,B910 65 6B    ADC $6B         und ARG
.,B912 85 63    STA $63         addieren
.,B914 A5 62    LDA $62         FAC
.,B916 65 6A    ADC $6A         und ARG
.,B918 85 62    STA $62         addieren
.,B91A 4C 36 B9 JMP $B936       Überlaufbit in Mantisse
                                zurückshiften
.,B91D 69 01    ADC #$01        Zähler erhöhen
.,B91F 06 70    ASL $70         FAC solange
.,B921 26 65    ROL $65         nach links
.,B923 26 64    ROL $64         verschieben bis das
.,B925 26 63    ROL $63         Bit 7
.,B927 26 62    ROL $62         gesetzt ist
.,B929 10 F2    BPL $B91D       nicht gesetzt ? dann nochmal
.,B92B 38       SEC             wenn Binärexponent kleiner
.,B92C E5 61    SBC $61         als die Anzahl der
.,B92E B0 C7    BCS $B8F7       Verschiebungen, dann wird die
                                Zahl als Null behandelt
.,B930 49 FF    EOR #$FF        Exponent um
.,B932 69 01    ADC #$01        Verschiebungsanzahl
.,B934 85 61    STA $61         vermindern
.,B936 90 0E    BCC $B946       Carry gesetzt, nein dann RTS
.,B938 E6 61    INC $61         Exponent erhöhen
.,B93A F0 42    BEQ $B97E       wenn Überlauf in Exponent,
                                dann 'OVERFLOW ERROR'
.,B93C 66 62    ROR $62         Überlaufbit in Carry schieben
.,B93E 66 63    ROR $63         Das Carry-Flag
.,B940 66 64    ROR $64         erhält die
.,B942 66 65    ROR $65         Position des
.,B944 66 70    ROR $70         höchstwertigen Bits
.,B946 60       RTS             Rücksprung

                                *** Mantisse von FAC invertieren
.,B947 A5 66    LDA $66         FAC Vorzeichen
.,B949 49 FF    EOR #$FF        invertieren
.,B94B 85 66    STA $66         und speichern
.,B94D A5 62    LDA $62         FAC
.,B94F 49 FF    EOR #$FF        invertieren
.,B951 85 62    STA $62         und speichern
.,B953 A5 63    LDA $63         FAC
.,B955 49 FF    EOR #$FF        invertieren
.,B957 85 63    STA $63         und speichern
.,B959 A5 64    LDA $64         FAC
.,B95B 49 FF    EOR #$FF        invertieren
.,B95D 85 64    STA $64         und speichern
.,B95F A5 65    LDA $65         FAC
.,B961 49 FF    EOR #$FF        invertieren
.,B963 85 65    STA $65         und speichern
.,B965 A5 70    LDA $70         FAC-Rundungsbyte
.,B967 49 FF    EOR #$FF        invertieren
.,B969 85 70    STA $70         und speichern
.,B96B E6 70    INC $70         Mantisse erhöhen
.,B96D D0 0E    BNE $B97D       nicht Null? dann RTS
.,B96F E6 65    INC $65         FAC erhöhen
.,B971 D0 0A    BNE $B97D       nicht Null? dann RTS
.,B973 E6 64    INC $64         FAC erhöhen
.,B975 D0 06    BNE $B97D       nicht Null? dann RTS
.,B977 E6 63    INC $63         FAC erhöhen
.,B979 D0 02    BNE $B97D       nicht Null? dann RTS
.,B97B E6 62    INC $62         FAC erhöhen
.,B97D 60       RTS             Rücksprung
.,B97E A2 0F    LDX #$0F        Nummer für 'OVERFLOW'
.,B980 4C 37 A4 JMP $A437       Fehlermeldung ausgeben

                                *** Rechtsverschieben eines
                                *** Registers
.,B983 A2 25    LDX #$25        Offset-Zeiger auf Register
.,B985 B4 04    LDY $04,X       FAC-
.,B987 84 70    STY $70         Rundungsbyte
.,B989 B4 03    LDY $03,X       1 mal
.,B98B 94 04    STY $04,X       verschieben
.,B98D B4 02    LDY $02,X       2 mal
.,B98F 94 03    STY $03,X       verschieben
.,B991 B4 01    LDY $01,X       3 mal
.,B993 94 02    STY $02,X       verschieben
.,B995 A4 68    LDY $68         FAC-
.,B997 94 01    STY $01,X       Rundungsbyte
.,B999 69 08    ADC #$08        Zähler um 8 erhöhen
.,B99B 30 E8    BMI $B985       größer als 0?
.,B99D F0 E6    BEQ $B985       wenn nicht, dann weiter
                                verschieben
.,B99F E9 08    SBC #$08        Zähler um 8 vermindern
.,B9A1 A8       TAY             Zähler sichern
.,B9A2 A5 70    LDA $70         FAC-Rundungsbyte laden
.,B9A4 B0 14    BCS $B9BA       wenn Null, dann CLC, RTS
.,B9A6 16 01    ASL $01,X       höchstwertiges Bit =1?,
.,B9A8 90 02    BCC $B9AC       wenn nicht, dann zu $B9AC
.,B9AA F6 01    INC $01,X       höchste Mantissenstelle
                                erhöhen
.,B9AC 76 01    ROR $01,X       sämtliche
.,B9AE 76 01    ROR $01,X       Stellen
.,B9B0 76 02    ROR $02,X       um ein
.,B9B2 76 03    ROR $03,X       Bit nach
.,B9B4 76 04    ROR $04,X       rechts
.,B9B6 6A       ROR             verschieben
.,B9B7 C8       INY             Zähler um eins erhöhen
.,B9B8 D0 EC    BNE $B9A6       verschieben bis Zähler =0
.,B9BA 18       CLC             Carry löschen
.,B9BB 60       RTS             Rücksprung

                                *** Konstanten für LOG
.:B9BC 81 00 00 00 00           1
.:B9C1 03                       3 = Polynomgrad, dann 4
                                Koeffizienten
.:B9C2 7F 5E 56 CB 79            .434255942
.:B9C7 80 13 9B 0B 64            .576584541
.:B9CC 80 76 38 93 16            .961800759
.:B9D1 82 38 AA 3B 20           2.88539007
.:B9D6 80 35 04 F3 34            .707106781 = 1/SQR(2)
.:B9DB 81 35 04 F3 34           1.41421356 = SQR(2)
.:B9E0 80 80 00 00 00           -.5
.:B9E5 80 31 72 17 F8            .693147181  =  LOG(2)

                                *** BASIC-Funktion LOG
.,B9EA 20 2B BC JSR $BC2B       Vorzeichen holen
.,B9ED F0 02    BEQ $B9F1       null ?, dann fertig
.,B9EF 10 03    BPL $B9F4       positiv ?, dann ok
.,B9F1 4C 48 B2 JMP $B248       'ILLEGAL QUANTITY'
.,B9F4 A5 61    LDA $61         Exponent
.,B9F6 E9 7F    SBC #$7F        normalisieren
.,B9F8 48       PHA             und merken
.,B9F9 A9 80    LDA #$80        Zahl in Bereich 0.5 bis 1
.,B9FB 85 61    STA $61         bringen
.,B9FD A9 D6    LDA #$D6        Zeiger auf
.,B9FF A0 B9    LDY #$B9        Konstante 1/SQR(2)
.,BA01 20 67 B8 JSR $B867       zu FAC addieren
.,BA04 A9 DB    LDA #$DB        Zeiger auf
.,BA06 A0 B9    LDY #$B9        Konstante SQR(2)
.,BA08 20 0F BB JSR $BB0F       SQR(2) durch FAC dividieren
.,BA0B A9 BC    LDA #$BC        Zeiger
.,BA0D A0 B9    LDY #$B9        auf Konstante 1
.,BA0F 20 50 B8 JSR $B850       1 minus FAC
.,BA12 A9 C1    LDA #$C1        Zeiger auf
.,BA14 A0 B9    LDY #$B9        Polynomkoeffizienten
.,BA16 20 43 E0 JSR $E043       Polynomberechnung
.,BA19 A9 E0    LDA #$E0        Zeiger auf
.,BA1B A0 B9    LDY #$B9        Konstante -0.5
.,BA1D 20 67 B8 JSR $B867       zu FAC addieren
.,BA20 68       PLA             Exponent zurückholen
.,BA21 20 7E BD JSR $BD7E       FAC = FAC + FAC
.,BA24 A9 E5    LDA #$E5        Zeiger auf
.,BA26 A0 B9    LDY #$B9        Konstante LOG(2)

                                *** Multiplikation FAC =
                                *** Konstante (A/Y) * FAC
.,BA28 20 8C BA JSR $BA8C       Konstante nach ARG

                                *** Multiplikation FAC = ARG *
                                *** FAC
.,BA2B D0 03    BNE $BA30       nicht null ?
.,BA2D 4C 8B BA JMP $BA8B       RTS
.,BA30 20 B7 BA JSR $BAB7       Exponent berechnen
.,BA33 A9 00    LDA #$00        Alle
.,BA35 85 26    STA $26         Funktions-
.,BA37 85 27    STA $27         register
.,BA39 85 28    STA $28         lö-
.,BA3B 85 29    STA $29         schen
.,BA3D A5 70    LDA $70         bitweise
.,BA3F 20 59 BA JSR $BA59       Multiplikation
.,BA42 A5 65    LDA $65         bitweise
.,BA44 20 59 BA JSR $BA59       Multiplikation
.,BA47 A5 64    LDA $64         bitweise
.,BA49 20 59 BA JSR $BA59       Multiplikation
.,BA4C A5 63    LDA $63         bitweise
.,BA4E 20 59 BA JSR $BA59       Multiplikation
.,BA51 A5 62    LDA $62         bitweise
.,BA53 20 5E BA JSR $BA5E       Multiplikation
                                Register nach FAC,
                                linksbündig machen

.,BA56 4C 8F BB JMP $BB8F       bitweise Multiplikation
.,BA59 D0 03    BNE $BA5E       Rechtsverschieben
.,BA5B 4C 83 B9 JMP $B983       des Registers
.,BA5E 4A       LSR             binäre Multiplikation
.,BA5F 09 80    ORA #$80        des Akkus
.,BA61 A8       TAY             mit ARG.
.,BA62 90 19    BCC $BA7D       Das Ergebnis kommt
.,BA64 18       CLC             in das
.,BA65 A5 29    LDA $29         Register für
.,BA67 65 6D    ADC $6D         Funktionen.
.,BA69 85 29    STA $29         Bei gesetztem Bit
.,BA6B A5 28    LDA $28         im Akku
.,BA6D 65 6C    ADC $6C         wird ARG
.,BA6F 85 28    STA $28         zum
.,BA71 A5 27    LDA $27         Funktionsregister
.,BA73 65 6B    ADC $6B         addiert.
.,BA75 85 27    STA $27         Zusätzlich
.,BA77 A5 26    LDA $26         werden
.,BA79 65 6A    ADC $6A         die
.,BA7B 85 26    STA $26         Funktionsregister
.,BA7D 66 26    ROR $26         noch
.,BA7F 66 27    ROR $27         verdoppelt.
.,BA81 66 28    ROR $28         Die Routine
.,BA83 66 29    ROR $29         arbeitet
.,BA85 66 70    ROR $70         im selben
.,BA87 98       TYA             Prinzip
.,BA88 4A       LSR             wie
.,BA89 D0 D6    BNE $BA61       bei $B34C.
.,BA8B 60       RTS             Rücksprung

                                *** ARG = Konstante (A/Y)
.,BA8C 85 22    STA $22         Die
.,BA8E 84 23    STY $23         Konstante,
.,BA90 A0 04    LDY #$04        auf
.,BA92 B1 22    LDA ($22),Y     die
.,BA94 85 6D    STA $6D         das
.,BA96 88       DEY             Akku
.,BA97 B1 22    LDA ($22),Y     und
.,BA99 85 6C    STA $6C         das
.,BA9B 88       DEY             Y-Reg
.,BA9C B1 22    LDA ($22),Y     zeigt, nach ARG.
.,BA9E 85 6B    STA $6B         Die
.,BAA0 88       DEY             gesamten
.,BAA1 B1 22    LDA ($22),Y     Vor-
.,BAA3 85 6E    STA $6E         zei -
.,BAA5 45 66    EOR $66         chen
.,BAA7 85 6F    STA $6F         von
.,BAA9 A5 6E    LDA $6E         FAC
.,BAAB 09 80    ORA #$80        und
.,BAAD 85 6A    STA $6A         ARG
.,BAAF 88       DEY             ver-
.,BAB0 B1 22    LDA ($22),Y     knüp-
.,BAB2 85 69    STA $69         fen
.,BAB4 A5 61    LDA $61         FAC-Exponent
.,BAB6 60       RTS             Rücksprung
.,BAB7 A5 69    LDA $69         wenn Exponent von ARG=0,
.,BAB9 F0 1F    BEQ $BADA       dann zu $BADA
.,BABB 18       CLC             FAC- und ARG-
.,BABC 65 61    ADC $61         Exponent
.,BABE 90 04    BCC $BAC4       addieren
.,BAC0 30 1D    BMI $BADF       wenn Überlauf, dann
                                'OVERFLOW ERROR'
.,BAC2 18       CLC             Carry
.:BAC3 2C       .BYTE $2C       löschen
.,BAC4 10 14    BPL $BADA       Wenn Unterlauf, dann zu $BADA
.,BAC6 69 80    ADC #$80        ergibt
.,BAC8 85 61    STA $61         FAC-
.,BACA D0 03    BNE $BACF       Exponent
.,BACC 4C FB B8 JMP $B8FB       FAC = 0
.,BACF A5 6F    LDA $6F         FAC- und ARG-Vorzeichen
                                verknüpfen
.,BAD1 85 66    STA $66         und speichern
.,BAD3 60       RTS             Rücksprung
.,BAD4 A5 66    LDA $66         wenn positives
.,BAD6 49 FF    EOR #$FF        Vorzeichen, dann
.,BAD8 30 05    BMI $BADF       'OVERFLOW ERROR'
.,BADA 68       PLA             Einsprungadresse
.,BADB 68       PLA             vom Stack holen
.,BADC 4C F7 B8 JMP $B8F7       FAC = 0
.,BADF 4C 7E B9 JMP $B97E       'OVERFLOW ERROR'

                                *** FAC = FAC * 10
.,BAE2 20 0C BC JSR $BC0C       FAC runden und nach ARG
.,BAE5 AA       TAX             FAC-Exponent
.,BAE6 F0 10    BEQ $BAF8       FAC gleich null, dann fertig
.,BAE8 18       CLC             Exponent + 2
.,BAE9 69 02    ADC #$02        entspricht mal 4
.,BAEB B0 F2    BCS $BADF       Übertrag ?
.,BAED A2 00    LDX #$00        Vergleichsbyte
.,BAEF 86 6F    STX $6F         löschen
.,BAF1 20 77 B8 JSR $B877       FAC = FAC + ARG entspricht
                                mal 5
.,BAF4 E6 61    INC $61         Exponent erhöhen entspricht
                                mal 2
.,BAF6 F0 E7    BEQ $BADF       Übertrag, dann 'OVERFLOW'
.,BAF8 60       RTS             Rücksprung

.:BAF9 84 20 00 00 00           Fließkommakonstante 10

                                *** FAC = FAC / 10
.,BAFE 20 0C BC JSR $BC0C       FAC runden und nach ARG
.,BB01 A9 F9    LDA #$F9        Zeiger
.,BB03 A0 BA    LDY #$BA        auf
.,BB05 A2 00    LDX #$00        Konstante 10
.,BB07 86 6F    STX $6F         Vergleichsbyte löschen
.,BB09 20 A2 BB JSR $BBA2       Konstante 10 nach FAC
.,BB0C 4C 12 BB JMP $BB12       FAC = ARG / FAC

                                *** FAC = Konstante (A/Y) / FAC
.,BB0F 20 8C BA JSR $BA8C       Konstante (A/Y) nach ARG

                                *** FAC = ARG / FAC
.,BB12 F0 76    BEQ $BB8A       FAC gleich null,
                                'DIVISION BY ZERO'
.,BB14 20 1B BC JSR $BC1B       FAC runden
.,BB17 A9 00    LDA #$00        Vorzeichen
.,BB19 38       SEC             von FAC-
.,BB1A E5 61    SBC $61         Exponent
.,BB1C 85 61    STA $61         wechseln
.,BB1E 20 B7 BA JSR $BAB7       Exponent des Ergebnisses
                                bestimmen
.,BB21 E6 61    INC $61         wenn Exponentenüberlauf,
.,BB23 F0 BA    BEQ $BADF       dann ’OVERFLOW ERROR’
.,BB25 A2 FC    LDX #$FC        Zeiger
.,BB27 A9 01    LDA #$01        auf
.,BB29 A4 6A    LDY $6A         Funktionsregister
.,BB2B C4 62    CPY $62         diese
.,BB2D D0 10    BNE $BB3F       Routine
.,BB2F A4 6B    LDY $6B         vergleicht
.,BB31 C4 63    CPY $63         das
.,BB33 D0 0A    BNE $BB3F       FAC
.,BB35 A4 6C    LDY $6C         und
.,BB37 C4 64    CPY $64         das
.,BB39 D0 04    BNE $BB3F       ARG
.,BB3B A4 6D    LDY $6D         byte-
.,BB3D C4 65    CPY $65         weise
.,BB3F 08       PHP             Statusregister retten
.,BB40 2A       ROL             Carry gelöscht,
.,BB41 90 09    BCC $BB4C       dann zu $BB4C
.,BB43 E8       INX             Ergebnis
.,BB44 95 29    STA $29,X       aufbauen
.,BB46 F0 32    BEQ $BB7A       wenn X-Reg =0, dann zu $BB7A
.,BB48 10 34    BPL $BB7E       wenn X-Reg =1, dann zu $BB7E
.,BB4A A9 01    LDA #$01        wenn
.,BB4C 28       PLP             FAC kleiner oder gleich
.,BB4D B0 0E    BCS $BB5D       ARG, dann zu $BB5D
.,BB4F 06 6D    ASL $6D         Das
.,BB51 26 6C    ROL $6C         ARG
.,BB53 26 6B    ROL $6B         ver-
.,BB55 26 6A    ROL $6A         doppeln
.,BB57 B0 E6    BCS $BB3F       wenn Überlauf, dann zu $BB3F
.,BB59 30 CE    BMI $BB29       wenn Bit 7 gesetzt, dann
                                zu $BB29
.,BB5B 10 E2    BPL $BB3F       ansonsten zu $BB3F
.,BB5D A8       TAY             Die
.,BB5E A5 6D    LDA $6D         Mantisse
.,BB60 E5 65    SBC $65         von
.,BB62 85 6D    STA $6D         ARG
.,BB64 A5 6C    LDA $6C         minus
.,BB66 E5 64    SBC $64         der
.,BB68 85 6C    STA $6C         Mantisse
.,BB6A A5 6B    LDA $6B         von
.,BB6C E5 63    SBC $63         FAC
.,BB6E 85 6B    STA $6B         sub-
.,BB70 A5 6A    LDA $6A         tra-
.,BB72 E5 62    SBC $62         hie-
.,BB74 85 6A    STA $6A         ren
.,BB76 98       TYA             und wieder
.,BB77 4C 4F BB JMP $BB4F       zu $BB4C
.,BB7A A9 40    LDA #$40        unbedingter
.,BB7C D0 CE    BNE $BB4C       Sprung
.,BB7E 0A       ASL             den
.,BB7F 0A       ASL             Akku
.,BB80 0A       ASL             mit
.,BB81 0A       ASL             64
.,BB82 0A       ASL             multi -
.,BB83 0A       ASL             plizieren
.,BB84 85 70    STA $70         Ergeben = RundungssteLle
.,BB86 28       PLP             Statusregister aus Stack
.,BB87 4C 8F BB JMP $BB8F       Hilfsregister nach FAC
.,BB8A A2 14    LDX #$14        Nummer für 'DIVISION BY ZERO'
.,BB8C 4C 37 A4 JMP $A437       Fehlermeldung ausgeben
.,BB8F A5 26    LDA $26         Hilfs-
.,BB91 85 62    STA $62         register
.,BB93 A5 27    LDA $27         ($26 - $29)
.,BB95 85 63    STA $63         nach
.,BB97 A5 28    LDA $28         FAC
.,BB99 85 64    STA $64         über-
.,BB9B A5 29    LDA $29         tra-
.,BB9D 85 65    STA $65         gen
.,BB9F 4C D7 B8 JMP $B8D7       FAC linksbündig machen

                                *** Konstante (A/Y) nach FAC
                                *** übertragen
.,BBA2 85 22    STA $22         Zeiger
.,BBA4 84 23    STY $23         setzen
.,BBA6 A0 04    LDY #$04        Zähler setzen
.,BBA8 B1 22    LDA ($22),Y     LOW-Byte
.,BBAA 85 65    STA $65         der
.,BBAC 88       DEY             Mantisse
.,BBAD B1 22    LDA ($22),Y     und
.,BBAF 85 64    STA $64         HIGH-
.,BBB1 88       DEY             Byte
.,BBB2 B1 22    LDA ($22),Y     der
.,BBB4 85 63    STA $63         Mantisse
.,BBB6 88       DEY             in
.,BBB7 B1 22    LDA ($22),Y     FAC
.,BBB9 85 66    STA $66         holen
.,BBBB 09 80    ORA #$80        Vorzeichen
.,BBBD 85 62    STA $62         der
.,BBBF 88       DEY             Man-
.,BBC0 B1 22    LDA ($22),Y     tisse
.,BBC2 85 61    STA $61         Exponent
.,BBC4 84 70    STY $70         Rundungsstelle
.,BBC6 60       RTS             Rücksprung
.,BBC7 A2 5C    LDX #$5C        Adresse LOW
.:BBC9 2C       .BYTE $2C       Akku #4

                                *** FAC nach Akku #3 übertragen
.,BBCA A2 57    LDX #$57        Adresse LOW Akku #3
.,BBCC A0 00    LDY #$00        Adresse HIGH
.,BBCE F0 04    BEQ $BBD4       unbedingter Sprung

                                *** FAC nach Variable übertragen
.,BBD0 A6 49    LDX $49         Variablenadresse
.,BBD2 A4 4A    LDY $4A         holen
.,BBD4 20 1B BC JSR $BC1B       FAC runden
.,BBD7 86 22    STX $22         Zeiger auf
.,BBD9 84 23    STY $23         Zieladresse
.,BBDB A0 04    LDY #$04        Zähler setzen
.,BBDD A5 65    LDA $65         LOW-Byte der Mantisse
.,BBDF 91 22    STA ($22),Y     Den
.,BBE1 88       DEY             FAC
.,BBE2 A5 64    LDA $64         in
.,BBE4 91 22    STA ($22),Y     den
.,BBE6 88       DEY             Ziel-
.,BBE7 A5 63    LDA $63         bereich
.,BBE9 91 22    STA ($22),Y     über-
.,BBEB 88       DEY             tragen
.,BBEC A5 66    LDA $66         FAC-Vorzeichen
.,BBEE 09 7F    ORA #$7F        Die Bits 0 bis 6 setzen
.,BBF0 25 62    AND $62         Vorzeichen auf
.,BBF2 91 22    STA ($22),Y     Speicherformat
.,BBF4 88       DEY             bringen
.,BBF5 A5 61    LDA $61         FAC-Exponent
.,BBF7 91 22    STA ($22),Y     übertragen
.,BBF9 84 70    STY $70         FAC-Rundungsstelle löschen
.,BBFB 60       RTS             Rücksprung

                                *** ARG nach FAC übertragen
.,BBFC A5 6E    LDA $6E         ARG-Vorzeichen
.,BBFE 85 66    STA $66         in FAC-Reg übertragen
.,BC00 A2 05    LDX #$05        5 Bytes
.,BC02 B5 68    LDA $68,X       ARG in
.,BC04 95 60    STA $60,X       FAC
.,BC06 CA       DEX             übertragen
.,BC07 D0 F9    BNE $BC02       schon alle Zeichen ?
.,BC09 86 70    STX $70         FAC-Rundungsstelle löschen
.,BC0B 60       RTS             Rücksprung

                                *** FAC nach ARG übertragen
.,BC0C 20 1B BC JSR $BC1B       FAC runden
.,BC0F A2 06    LDX #$06        6 Zeichen
.,BC11 B5 60    LDA $60,X       FAC in
.,BC13 95 68    STA $68,X       ARG
.,BC15 CA       DEX             übertragen
.,BC16 D0 F9    BNE $BC11       schon alle Zeichen ?
.,BC18 86 70    STX $70         FAC-Rundungsstelle löschen
.,BC1A 60       RTS             Rücksprung

                                *** FAC runden
.,BC1B A5 61    LDA $61         Exponent null ?,
.,BC1D F0 FB    BEQ $BC1A       dann fertig
.,BC1F 06 70    ASL $70         Rundungsstelle größer $7F ?
.,BC21 90 F7    BCC $BC1A       nein, dann fertig
.,BC23 20 6F B9 JSR $B96F       Mantisse um eins erhöhen
.,BC26 D0 F2    BNE $BC1A       jetzt null ?
.,BC28 4C 38 B9 JMP $B938       nach rechts verschieben,
                                Exponent erhöhen

                                *** Vorzeichen von FAC holen
.,BC2B A5 61    LDA $61         wenn null,
.,BC2D F0 09    BEQ $BC38       dann RTS
.,BC2F A5 66    LDA $66         FAC-Vorzeichen
.,BC31 2A       ROL             holen
.,BC32 A9 FF    LDA #$FF        negativ?
.,BC34 B0 02    BCS $BC38       dann RTS
.,BC36 A9 01    LDA #$01        sonst positiv
.,BC38 60       RTS             Rücksprung

                                *** BASIC-Funktion SGN
.,BC39 20 2B BC JSR $BC2B       Vorzeichen holen
.,BC3C 85 62    STA $62         und in FAC speichern
.,BC3E A9 00    LDA #$00        $63
.,BC40 85 63    STA $63         löschen
.,BC42 A2 88    LDX #$88        Exponent
.,BC44 A5 62    LDA $62         Vorzeichen
.,BC46 49 FF    EOR #$FF        invertieren
.,BC48 2A       ROL             und nach links rollen
.,BC49 A9 00    LDA #$00        Die Adressen
.,BC4B 85 65    STA $65         $65
.,BC4D 85 64    STA $64         und $64 löschen
.,BC4F 86 61    STX $61         Exponent
.,BC51 85 70    STA $70         Rundungsstelle
.,BC53 85 66    STA $66         löschen
.,BC55 4C D2 B8 JMP $B8D2       linksbündig machen

                                *** BASIC-Funktion ABS
.,BC58 46 66    LSR $66         Vorzeichenbit löschen
.,BC5A 60       RTS             Rücksprung

                                *** Vergleich Konstante (A/Y) mit
                                *** FAC
.,BC5B 85 24    STA $24         Zeiger auf
.,BC5D 84 25    STY $25         Konstante
.,BC5F A0 00    LDY #$00        Zähler setzen
.,BC61 B1 24    LDA ($24),Y     Exponent
.,BC63 C8       INY             Zähler erhöhen
.,BC64 AA       TAX             ins X-Reg
.,BC65 F0 C4    BEQ $BC2B       null?, dann Vorzeichen von
                                FAC holen
.,BC67 B1 24    LDA ($24),Y     Konstante
.,BC69 45 66    EOR $66         FAC-Vorzeichen
.,BC6B 30 C2    BMI $BC2F       verschiedene Vorzeichen?,
                                dann zu $BC2F
.,BC6D E4 61    CPX $61         Exponenten vergleichen
.,BC6F D0 21    BNE $BC92       falls verschieden, dann zu
                                $BC92
.,BC71 B1 24    LDA ($24),Y     das
.,BC73 09 80    ORA #$80        erste
.,BC75 C5 62    CMP $62         Byte
.,BC77 D0 19    BNE $BC92       vergleichen
.,BC79 C8       INY             Zähler erhöhen
.,BC7A B1 24    LDA ($24),Y     das zweite
.,BC7C C5 63    CMP $63         Byte
.,BC7E D0 12    BNE $BC92       vergleichen
.,BC80 C8       INY             Zähler erhöhen
.,BC81 B1 24    LDA ($24),Y     das dritte
.,BC83 C5 64    CMP $64         Byte
.,BC85 D0 0B    BNE $BC92       vergleichen
.,BC87 C8       INY             Zähler erhöhen
.,BC88 A9 7F    LDA #$7F        FAC-Rundungsstelle mit
.,BC8A C5 70    CMP $70         $7F vergleichen
.,BC8C B1 24    LDA ($24),Y     letzte Stellen, gemäß Ver-
.,BC8E E5 65    SBC $65         gleich der Rundungsstelle,
                                subtrahieren
.,BC90 F0 28    BEQ $BCBA       wenn alle Stellen gleich
                                sind, dann RTS
.,BC92 A5 66    LDA $66         FAC-Vorzeichen
.,BC94 90 02    BCC $BC98       ist die Konstante kleiner
                                FAC, dann zu $BC98
.,BC96 49 FF    EOR #$FF        Ergebnis kleiner, dann
                                invertieren
.,BC98 4C 31 BC JMP $BC31       Flag für Ergebnis setzen

                                *** Umwandlung Fließkomma nach
                                *** Integer
.,BC9B A5 61    LDA $61         Exponent
.,BC9D F0 4A    BEQ $BCE9       null ?
.,BC9F 38       SEC             Integer-
.,BCA0 E9 A0    SBC #$A0        Exponent
.,BCA2 24 66    BIT $66         wenn FAC positiv,
.,BCA4 10 09    BPL $BCAF       dann zu $BCAF
.,BCA6 AA       TAX             FAC
.,BCA7 A9 FF    LDA #$FF        Rundungsbyte
.,BCA9 85 68    STA $68         setzen
.,BCAB 20 4D B9 JSR $B94D       Mantisse von FAC invertieren
.,BCAE 8A       TXA             Exponent in Akku
.,BCAF A2 61    LDX #$61        FAC-Offset-Zeiger
.,BCB1 C9 F9    CMP #$F9        wenn Exponent größer als
.,BCB3 10 06    BPL $BCBB       -8, dann zu BCBB
.,BCB5 20 99 B9 JSR $B999       FAC rechtsverschieben
.,BCB8 84 68    STY $68         FAC-Rundungsbyte löschen
.,BCBA 60       RTS             Rücksprung
.,BCBB A8       TAY             Akku löschen
.,BCBC A5 66    LDA $66         FAC-Vorzeichen laden
.,BCBE 29 80    AND #$80        das
.,BCC0 46 62    LSR $62         FAC-
.,BCC2 05 62    ORA $62         Vorzeichen
.,BCC4 85 62    STA $62         isolieren
.,BCC6 20 B0 B9 JSR $B9B0       FAC bitweise nach rechts
                                verschieben
.,BCC9 84 68    STY $68         FAC-Rundungsbyte löschen
.,BCCB 60       RTS             Rücksprung

                                *** BASIC-Funktion INT
.,BCCC A5 61    LDA $61         Exponent
.,BCCE C9 A0    CMP #$A0        ganze Zahl ?
.,BCD0 B0 20    BCS $BCF2       ja, dann fertig
.,BCD2 20 9B BC JSR $BC9B       FAC nach Integer wandeln
.,BCD5 84 70    STY $70         Rundungsstelle löschen
.,BCD7 A5 66    LDA $66         Vorzeichen in Akku
.,BCD9 84 66    STY $66         und positiv machen
.,BCDB 49 80    EOR #$80        Bei
.,BCDD 2A       ROL             negativen Vorzeichen
.,BCDE A9 A0    LDA #$A0        das
.,BCE0 85 61    STA $61         Carry-
.,BCE2 A5 65    LDA $65         flag
.,BCE4 85 07    STA $07         löschen
.,BCE6 4C D2 B8 JMP $B8D2       FAC linksbündig machen
.,BCE9 85 62    STA $62         Mantisse
.,BCEB 85 63    STA $63         mit
.,BCED 85 64    STA $64         Nullen
.,BCEF 85 65    STA $65         füllen
.,BCF1 A8       TAY             Y-Reg löschen
.,BCF2 60       RTS             Rücksprung

                                *** Umwandlung ASCII nach
                                *** Fließkommaformat
.,BCF3 A0 00    LDY #$00        Wert festlegen
.,BCF5 A2 0A    LDX #$0A        Zähler stellen
.,BCF7 94 5D    STY $5D,X       den Bereich
.,BCF9 CA       DEX             von $5D bis $66 mit
.,BCFA 10 FB    BPL $BCF7       Nullen füllen
.,BCFC 90 0F    BCC $BD0D       wenn erstes Zeichen eine
                                Ziffer, dann zu $BD0D
.,BCFE C9 2D    CMP #$2D        Nummer für '-'?
.,BD00 D0 04    BNE $BD06       wenn nicht, dann zu $BD06
.,BD02 86 67    STX $67         Flag für negativ
.,BD04 F0 04    BEQ $BD0A       unbedingter Sprung
.,BD06 C9 2B    CMP #$2B        Nummer für ' + '
.,BD08 D0 05    BNE $BD0F       wenn nicht, dann zu $BD0F
.,BD0A 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,BD0D 90 5B    BCC $BD6A       wenn Ziffer, dann zu $BD6A
.,BD0F C9 2E    CMP #$2E        Nummer für '.'
.,BD11 F0 2E    BEQ $BD41       wenn ja, dann zu $BD41
.,BD13 C9 45    CMP #$45        Nummer für 'E'
.,BD15 D0 30    BNE $BD47       wenn nicht, dann zu $BD47
.,BD17 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,BD1A 90 17    BCC $BD33       wenn Ziffer, dann zu $BD33
.,BD1C C9 AB    CMP #$AB        '-' BASIC-Kode
.,BD1E F0 0E    BEQ $BD2E       wenn ja, dann zu $BD2E
.,BD20 C9 2D    CMP #$2D        Nummer für '-'
.,BD22 F0 0A    BEQ $BD2E       wenn ja, dann zu $BD2E
.,BD24 C9 AA    CMP #$AA        '+' BASIC-Kode
.,BD26 F0 08    BEQ $BD30       wenn ja, dann zu $BD30
.,BD28 C9 2B    CMP #$2B        Nummer für '+'
.,BD2A F0 04    BEQ $BD30       wenn ja, dann zu $BD30
.,BD2C D0 07    BNE $BD35       unbedingter Sprung
.,BD2E 66 60    ROR $60         Bit 7 setzen
.,BD30 20 73 00 JSR $0073       CHRGET nächstes Zeichen holen
.,BD33 90 5C    BCC $BD91       wenn Ziffer, dann zu $BD91
.,BD35 24 60    BIT $60         Bit 7 gesetzt ?
.,BD37 10 0E    BPL $BD47       wenn nicht, dann zu $BD47
.,BD39 A9 00    LDA #$00        Vorzeichen des
.,BD3B 38       SEC             Exponenten
.,BD3C E5 5E    SBC $5E         wechseln
.,BD3E 4C 49 BD JMP $BD49       weiter bei $BD49
.,BD41 66 5F    ROR $5F         Aufruf durch Dezimalpunkt
.,BD43 24 5F    BIT $5F         schon zweiter Dezimalpunkt
.,BD45 50 C3    BVC $BD0A       wenn nicht, dann weiter
.,BD47 A5 5E    LDA $5E         Zahl gemäß
.,BD49 38       SEC             Position
.,BD4A E5 5D    SBC $5D         des Dezimalpunkts
.,BD4C 85 5E    STA $5E         und Exponenten anpassen
.,BD4E F0 12    BEQ $BD62       Zahl= Null, dann zu $BD62
.,BD50 10 09    BPL $BD5B       Zahl kleiner als $7F
.,BD52 20 FE BA JSR $BAFE       FAC = FAC / 10
.,BD55 E6 5E    INC $5E         Zahl erhöhen
.,BD57 D0 F9    BNE $BD52       unbedingter
.,BD59 F0 07    BEQ $BD62       Sprung
.,BD5B 20 E2 BA JSR $BAE2       FAC = FAC * 10
.,BD5E C6 5E    DEC $5E         Zahl gemäß
.,BD60 D0 F9    BNE $BD5B       Exponenten anpassen
.,BD62 A5 67    LDA $67         wenn negativ,
.,BD64 30 01    BMI $BD67       dann Vorzeichen invertieren
.,BD66 60       RTS             Rücksprung
.,BD67 4C B4 BF JMP $BFB4       Vorzeichenwechsel FAC = -FAC
.,BD6A 48       PHA             Aufruf durch Mantisse
.,BD6B 24 5F    BIT $5F         wenn Vorkommastelle,
.,BD6D 10 02    BPL $BD71       dann zu $BD71
.,BD6F E6 5D    INC $5D         Zähler erhöhen
.,BD71 20 E2 BA JSR $BAE2       FAC = FAC * 10
.,BD74 68       PLA             ASCII in
.,BD75 38       SEC             Ziffer umwandeln
.,BD76 E9 30    SBC #$30        '0' abziehen gibt hex
.,BD78 20 7E BD JSR $BD7E       addiert nächste Stelle zu FAC
.,BD7B 4C 0A BD JMP $BD0A       nächstes Zeichen
.,BD7E 48       PHA             Wert aus Stack
.,BD7F 20 0C BC JSR $BC0C       FAC nach ARG
.,BD82 68       PLA             Wert in Stack
.,BD83 20 3C BC JSR $BC3C       Accu in höchste Stelle von FAC
.,BD86 A5 6E    LDA $6E         FAC-Vorzeichen und
.,BD88 45 66    EOR $66         ARG-Vorzeichen
.,BD8A 85 6F    STA $6F         verknüpfen
.,BD8C A6 61    LDX $61         erste Stelle von FAC holen
.,BD8E 4C 6A B8 JMP $B86A       FAC = FAC + ARG
.,BD91 A5 5E    LDA $5E         Aufruf durch 'E'
.,BD93 C9 0A    CMP #$0A        wenn dritte Exponentenziffer,
.,BD95 90 09    BCC $BDA0       dann zu $BDA0
.,BD97 A9 64    LDA #$64        wenn Vorzeichen
.,BD99 24 60    BIT $60         negativ,
.,BD9B 30 11    BMI $BDAE       dann Unterlauf
.,BD9D 4C 7E B9 JMP $B97E       zu 'OVERFLOW ERROR'
.,BDA0 0A       ASL             Den
.,BDA1 0A       ASL             Exponenten
.,BDA2 18       CLC             mit
.,BDA3 65 5E    ADC $5E         10
.,BDA5 0A       ASL             multi-
.,BDA6 18       CLC             plizieren
.,BDA7 A0 00    LDY #$00        Zähler setzen
.,BDA9 71 7A    ADC ($7A),Y     Exponenten-
.,BDAB 38       SEC             ziffer
.,BDAC E9 30    SBC #$30        addie-
.,BDAE 85 5E    STA $5E         ren
.,BDB0 4C 30 BD JMP $BD30       nächstes Zeichen holen

                                *** Konstanten für Fließkomma
                                *** nach ASCII
.:BDB3 9B 3E BC 1F FD           99999999.9
.:BDB8 9E 6E 6B 27 FD           999999999
.:BDBD 9E 6E 6B 28 00           1E9

                                *** Ausgabe der Zeilennummer
                                *** bei Fehlermeldung
.,BDC2 A9 71    LDA #$71        Zeiger
.,BDC4 A0 A3    LDY #$A3        auf 'in'
.,BDC6 20 DA BD JSR $BDDA       String ausgeben
.,BDC9 A5 3A    LDA $3A         laufende
.,BDCB A6 39    LDX $39         Zeilennummer holen

                                *** positive Integerzahl
                                *** in A/X ausgeben
.,BDCD 85 62    STA $62         für Umwandlung
.,BDCF 86 63    STX $63         in FAC schreiben
.,BDD1 A2 90    LDX #$90        Exponent
.,BDD3 38       SEC             = 16
.,BDD4 20 49 BC JSR $BC49       Integer nach Fließkomma
                                wandeln
.,BDD7 20 DF BD JSR $BDDF       FAC nach ASCII wandeln
.,BDDA 4C 1E AB JMP $AB1E       String ausgeben

                                *** FAC nach ASCII-Format
                                *** wandeln und nach $100
.,BDDD A0 01    LDY #$01        Stringzeiger
.,BDDF A9 20    LDA #$20        ' ' Leerzeichen für positive
                                Zahl
.,BDE1 24 66    BIT $66         wenn Vorzeichen
.,BDE3 10 02    BPL $BDE7       positiv ?, dann zu $BDE7
.,BDE5 A9 2D    LDA #$2D        '-' Minuszeichen für
.,BDE7 99 FF 00 STA $00FF,Y     negative Zahl
                                in
.,BDEA 85 66    STA $66         Pufferbereich
.,BDEC 84 71    STY $71         schreiben
.,BDEE C8       INY             Zähler erhöhen
.,BDEF A9 30    LDA #$30        '0’
.,BDF1 A6 61    LDX $61         Exponent
.,BDF3 D0 03    BNE $BDF8       wenn Zahl nicht null ?
.,BDF5 4C 04 BF JMP $BF04       dann fertig
.,BDF8 A9 00    LDA #$00        FAC
.,BDFA E0 80    CPX #$80        mit 1 vergleichen
.,BDFC F0 02    BEQ $BE00       wenn ja ,dann zu $BE00
.,BDFE B0 09    BCS $BE09       FAC größer 1
.,BE00 A9 BD    LDA #$BD        Zeiger auf
.,BE02 A0 BD    LDY #$BD        Konstante 1E9
.,BE04 20 28 BA JSR $BA28       Konstante (Zeiger A/Y) * FAC
.,BE07 A9 F7    LDA #$F7        = -9
.,BE09 85 5D    STA $5D         $ 5D = -9
.,BE0B A9 B8    LDA #$B8        Zeiger auf
.,BE0D A0 BD    LDY #$BD        Konstante 999999999
.,BE0F 20 5B BC JSR $BC5B       Vergleich Konstante
                                (Zeiger A/Y) mit FAC
.,BE12 F0 1E    BEQ $BE32       gleich
.,BE14 10 12    BPL $BE28       kleiner
.,BE16 A9 B3    LDA #$B3        Zeiger auf
.,BE18 A0 BD    LDY #$BD        Konstante 99999999.9
.,BE1A 20 5B BC JSR $BC5B       Vergleich Konstante
                                (Zeiger A/Y) mit FAC
.,BE1D F0 02    BEQ $BE21       gleich
.,BE1F 10 0E    BPL $BE2F       kleiner
.,BE21 20 E2 BA JSR $BAE2       FAC = FAC * 10
.,BE24 C6 5D    DEC $5D         Dezimalexponent erniedrigen
.,BE26 D0 EE    BNE $BE16       schon 0?
.,BE28 20 FE BA JSR $BAFE       FAC = FAC / 10
.,BE2B E6 5D    INC $5D         Dezimalexponent erhöhen
.,BE2D D0 DC    BNE $BE0B       Überlauf ?
.,BE2F 20 49 B8 JSR $B849       FAC = FAC + .5 , runden
.,BE32 20 9B BC JSR $BC9B       FAC nach Integer
.,BE35 A2 01    LDX #$01        FAC ist nun im Bereich von
.,BE37 A5 5D    LDA $5D         1E8 bis 1E9, $5D hat Wert
.,BE39 18       CLC             von Zehnerpotenz
.,BE3A 69 0A    ADC #$0A        Zahl =0.01
.,BE3C 30 09    BMI $BE47       Betrag kleiner 0.1 ?
.,BE3E C9 0B    CMP #$0B        wenn ja, dann
.,BE40 B0 06    BCS $BE48       Betrag größer 1E9 ?
.,BE42 69 FF    ADC #$FF        die
.,BE44 AA       TAX             Be-
.,BE45 A9 02    LDA #$02        rechnung
.,BE47 38       SEC             des
.,BE48 E9 02    SBC #$02        Exponenten-
.,BE4A 85 5E    STA $5E         flags
.,BE4C 86 5D    STX $5D         Negative Darstellung des
.,BE4E 8A       TXA             Exponenten
.,BE4F F0 02    BEQ $BE53       wenn 0.1, dann zu $BE53
.,BE51 10 13    BPL $BE66       wenn nicht 0.01, dann
                                zu $BE66
.,BE53 A4 71    LDY $71         Zeiger für Polynomauswertung
.,BE55 A9 2E    LDA #$2E        Nummer für '.'
.,BE57 C8       INY             Zeiger erhöhen
.,BE58 99 FF 00 STA $00FF,Y     in Stringbereich
.,BE5B 8A       TXA             schreiben
.,BE5C F0 06    BEQ $BE64       wenn 0.1, dann zu $BE64
.,BE5E A9 30    LDA #$30        Nummer für '0'
.,BE60 C8       INY             Zeiger erhöhen
.,BE61 99 FF 00 STA $00FF,Y     in Stringbereich
.,BE64 84 71    STY $71         schreiben
.,BE66 A0 00    LDY #$00        Zeiger
.,BE68 A2 80    LDX #$80        stellen
.,BE6A A5 65    LDA $65         Durch
.,BE6C 18       CLC             Addition
.,BE6D 79 19 BF ADC $BF19,Y     und
.,BE70 85 65    STA $65         Subtraktion
.,BE72 A5 64    LDA $64         der
.,BE74 79 18 BF ADC $BF18,Y     Werte
.,BE77 85 64    STA $64         aus
.,BE79 A5 63    LDA $63         der
.,BE7B 79 17 BF ADC $BF17,Y     Tabelle
.,BE7E 85 63    STA $63         werden
.,BE80 A5 62    LDA $62         die
.,BE82 79 16 BF ADC $BF16,Y     einzelnen
.,BE85 85 62    STA $62         Ziffern
.,BE87 E8       INX             des
.,BE88 B0 04    BCS $BE8E       Zahlen-
.,BE8A 10 DE    BPL $BE6A       Strings
.,BE8C 30 02    BMI $BE90       be-
.,BE8E 30 DA    BMI $BE6A       rech-
.,BE90 8A       TXA             net
.,BE91 90 04    BCC $BE97       alles addiert?, wenn nicht,
                                dann zu $BE97
.,BE93 49 FF    EOR #$FF        Ergebnis mit 10
.,BE95 69 0A    ADC #$0A        komplementieren
.,BE97 69 2F    ADC #$2F        '0' - 1
.,BE99 C8       INY             Zähler
.,BE9A C8       INY             ent-
.,BE9B C8       INY             sprechend
.,BE9C C8       INY             erhöhen
.,BE9D 84 47    STY $47         Zähler sichern
.,BE9F A4 71    LDY $71         Zeiger auf Stringbereich laden
.,BEA1 C8       INY             und erhöhen
.,BEA2 AA       TAX             Ziffer
.,BEA3 29 7F    AND #$7F        in
.,BEA5 99 FF 00 STA $00FF,Y     Stringbereich
.,BEA8 C6 5D    DEC $5D         bringen
.,BEAA D0 06    BNE $BEB2       wenn Einerstelle nicht
                                erreicht, dann zu $BEB2
.,BEAC A9 2E    LDA #$2E        Nummer für '.'
.,BEAE C8       INY             Zähler erhöhen
.,BEAF 99 FF 00 STA $00FF,Y     in Stringbereich schreiben
.,BEB2 84 71    STY $71         Zähler speichern
.,BEB4 A4 47    LDY $47         Neuen Zähler holen
.,BEB6 8A       TXA             FAC-
.,BEB7 49 FF    EOR #$FF        Um-
.,BEB9 29 80    AND #$80        wand-
.,BEBB AA       TAX             lung
.,BEBC C0 24    CPY #$24        Tabellenende ereicht,
.,BEBE F0 04    BEQ $BEC4       dann zu $BEC4
.,BEC0 C0 3C    CPY #$3C        Tabellenende bei
                                TI$-Berechnung
.,BEC2 D0 A6    BNE $BE6A       nicht erreicht, dann zu $BE6A
.,BEC4 A4 71    LDY $71         Zähler wieder holen
.,BEC6 B9 FF 00 LDA $00FF,Y     letzte Stelle suchen
.,BEC9 88       DEY             Zähler erniedrigen
.,BECA C9 30    CMP #$30        Nummer für '0'
.,BECC F0 F8    BEQ $BEC6       wenn ja, dann zu $BEC6
.,BECE C9 2E    CMP #$2E        Nummer für '.'
.,BED0 F0 01    BEQ $BED3       wenn ja, dann zu $BED3
.,BED2 C8       INY             Zähler erhöhen
.,BED3 A9 2B    LDA #$2B        Nummer für '+'
.,BED5 A6 5E    LDX $5E         wenn Flag nicht gesetzt,
.,BED7 F0 2E    BEQ $BF07       dann zu $BF07
.,BED9 10 08    BPL $BEE3       wenn Exponent positiv, dann
                                zu $BEE3
.,BEDB A9 00    LDA #$00        Den
.,BEDD 38       SEC             Exponenten
.,BEDE E5 5E    SBC $5E         be-
.,BEE0 AA       TAX             rechnen
.,BEE1 A9 2D    LDA #$2D        Nummer für '-'
.,BEE3 99 01 01 STA $0101,Y     in Stringbereich schreiben
.,BEE6 A9 45    LDA #$45        Nummer für 'E'
.,BEE8 99 00 01 STA $0100,Y     in Stringbereich schreiben
.,BEEB 8A       TXA             Zehner-
.,BEEC A2 2F    LDX #$2F        stelle
.,BEEE 38       SEC             für
.,BEEF E8       INX             den
.,BEF0 E9 0A    SBC #$0A        Exponenten
.,BEF2 B0 FB    BCS $BEEF       berechnen
.,BEF4 69 3A    ADC #$3A        '9' + 1
.,BEF6 99 03 01 STA $0103,Y     in Stringbereich schreiben
.,BEF9 8A       TXA             Zehnerstelle
.,BEFA 99 02 01 STA $0102,Y     in Stringbereich schreiben
.,BEFD A9 00    LDA #$00        Puffer mit $0
.,BEFF 99 04 01 STA $0104,Y     abschließen
.,BF02 F0 08    BEQ $BF0C       unbedingter Sprung
.,BF04 99 FF 00 STA $00FF,Y     Puffer
.,BF07 A9 00    LDA #$00        mit $0
.,BF09 99 00 01 STA $0100,Y     abschließen
.,BF0C A9 00    LDA #$00        Zeiger auf
.,BF0E A0 01    LDY #$01        Puffer $100
.,BF10 60       RTS             Rücksprung

.:BF11 80 00 00 00 00           Konstante 0.5 für
                                SQR-Funktion

                                *** Konstanten für Gleitkomma
                                *** nach ASCII
                                (32-Bit Binärzahlen mit Vorzeichen)
.:BF16 FA 0A 1F 00              -100 000 000
.:BF1A 00 98 96 80                10 000 000
.:BF1E FF F0 BD C0                -1 000 000
.:BF22 00 01 86 A0                   100 000
.:BF26 FF FF D8 F0                   -10 000
.:BF2A 00 00 03 E8                     1 000
.:BF2E FF FF FF 9C                     - 100
.:BF32 00 00 00 0A                        10
.:BF36 FF FF FF FF                        -1

                                *** Konstanten für Umwandlung
                                *** TI nach TI$
.:BF3A FF DF 0A 80              -2 160 000
.:BF3E 00 03 4B C0                  216 000
.:BF42 FF FF 73 60                  -36 000
.:BF46 00 00 0E 10                    3 600
.:BF4A FF FF FD A8                    - 600
.:BF4E 00 00 00 3C                      60

.:BF52 EC

.:BF53 AA AA AA AA AA
.:BF58 AA AA AA AA AA AA AA AA
.:BF60 AA AA AA AA AA AA AA AA
.:BF68 AA AA AA AA AA AA AA AA
.:BF70 AA

                                *** BASIC-Funktion SQR
.,BF71 20 0C BC JSR $BC0C       FAC runden und nach ARG
.,BF74 A9 11    LDA #$11        Zeiger auf
.,BF76 A0 BF    LDY #$BF        Konstante 0.5

                                *** Potenzierung FAC = ARG
                                *** hoch Konstante (A/Y)
.,BF78 20 A2 BB JSR $BBA2       Konstante nach FAC

                                *** Potenzierung FAC = ARG
                                *** hoch FAC
.,BF7B F0 70    BEQ $BFED       wenn FAC=0, dann zu $BFED
.,BF7D A5 69    LDA $69         Exponent ARG = Basis
.,BF7F D0 03    BNE $BF84       nicht null ?,
.,BF81 4C F9 B8 JMP $B8F9       dann fertig
.,BF84 A2 4E    LDX #$4E        Zeiger auf
.,BF86 A0 00    LDY #$00        Hilfsakku
.,BF88 20 D4 BB JSR $BBD4       FAC nach Hilfsakku
.,BF8B A5 6E    LDA $6E         Exponent FAC = Potenzexponent
.,BF8D 10 0F    BPL $BF9E       kleiner eins ?,
.,BF8F 20 CC BC JSR $BCCC       dann INT-Funktion
.,BF92 A9 4E    LDA #$4E        Zeiger auf
.,BF94 A0 00    LDY #$00        Hilfsakku
.,BF96 20 5B BC JSR $BC5B       mit FAC vergleichen
.,BF99 D0 03    BNE $BF9E       Exponent nicht ganzzahlig,
                                dann zu $BF9E
.,BF9B 98       TYA             Akku= 4
.,BF9C A4 07    LDY $07         Exponentenstelle
.,BF9E 20 FE BB JSR $BBFE       ARG nach FAC
.,BFA1 98       TYA             Exponentenstelle
.,BFA2 48       PHA             in Stack
.,BFA3 20 EA B9 JSR $B9EA       LOG-Funktion
.,BFA6 A9 4E    LDA #$4E        Zeiger auf
.,BFA8 A0 00    LDY #$00        Hilfsakku
.,BFAA 20 28 BA JSR $BA28       mit FAC multiplizieren
.,BFAD 20 ED BF JSR $BFED       EXP-Funktion
.,BFB0 68       PLA             Exponent aus Stack
.,BFB1 4A       LSR             wenn Exponent gradzahlig,
.,BFB2 90 0A    BCC $BFBE       dann fertig

                                *** Vorzeichenwechsel
.,BFB4 A5 61    LDA $61         Exponent
.,BFB6 F0 06    BEQ $BFBE       Zahl gleich null, dann fertig
.,BFB8 A5 66    LDA $66         Vorzeichen
.,BFBA 49 FF    EOR #$FF        invertieren und
.,BFBC 85 66    STA $66         speichern
.,BFBE 60       RTS             Rücksprung

                                *** Konstanten für EXP
.:BFBF 81 38 AA 3B 29           1.44269504 = 1/LOG(2)
.:BFC4 07                       7 = Polynomgrad, 8
                                Koeffizienten
.:BFC5 71 34 58 3E 56           2.14987637E-5
.:BFCA 74 16 7E B3 1B           1.4352314E-4
.:BFCF 77 2F EE E3 85           1.34226348E-3
.:BFD4 7A 1D 84 1C 2A           9.614011701E-3
.:BFD9 7C 63 59 58 0A           .0555051269
.:BFDE 7E 75 FD E7 C6           .240226385
.:BFE3 80 31 72 18 10           .693147186
.:BFE8 81 00 00 00 00           1

                                *** BASIC-Funktion EXP
.,BFED A9 BF    LDA #$BF        Zeiger auf
.,BFEF A0 BF    LDY #$BF        Konstante 1/LOG(2)
.,BFF1 20 28 BA JSR $BA28       mit FAC multiplizieren
.,BFF4 A5 70    LDA $70         80 zu Rundungsstelle
.,BFF6 69 50    ADC #$50        addieren
.,BFF8 90 03    BCC $BFFD       wenn kleiner als $FF, dann
                                zu $BFFD
.,BFFA 20 23 BC JSR $BC23       Mantisse von FAC um
                                eins erhöhen
.,BFFD 4C 00 E0 JMP $E000       weiter bei $E000
.,E000 85 56    STA $56         Rundungsstelle
.,E002 20 0F BC JSR $BC0F       FAC nach ARG bringen
.,E005 A5 61    LDA $61         Exponent
.,E007 C9 88    CMP #$88        Zahl größer 128 ?,
.,E009 90 03    BCC $E00E       dann zu $E00E
.,E00B 20 D4 BA JSR $BAD4       falls positiv 'OVERFLOW'
.,E00E 20 CC BC JSR $BCCC       INTEGER-Funktion
.,E011 A5 07    LDA $07         ganze Zahl
.,E013 18       CLC             Zahl
.,E014 69 81    ADC #$81        gleich
.,E016 F0 F3    BEQ $E00B       127 ?, dann zu $E00B
.,E018 38       SEC             ansonsten
.,E019 E9 01    SBC #$01        subtrahieren
.,E01B 48       PHA             und in Stack
.,E01C A2 05    LDX #$05        FAC
.,E01E B5 69    LDA $69,X       und
.,E020 B4 61    LDY $61,X       ARG
.,E022 95 61    STA $61,X       ver-
.,E024 94 69    STY $69,X       tauschen
.,E026 CA       DEX             Zähler erniedrigen
.,E027 10 F5    BPL $E01E       schon alle Zeichen?
.,E029 A5 56    LDA $56         Rundungs-
.,E02B 85 70    STA $70         stelle
.,E02D 20 53 B8 JSR $B853       ARG - FAC
.,E030 20 B4 BF JSR $BFB4       Vorzeichenwechsel
.,E033 A9 C4    LDA #$C4        Zeiger auf
.,E035 A0 BF    LDY #$BF        Polynomkoeffizienten
.,E037 20 59 E0 JSR $E059       Polynom berechnen
.,E03A A9 00    LDA #$00        Vergleichsbyte
.,E03C 85 6F    STA $6F         löschen
.,E03E 68       PLA             Zahl aus Stack
.,E03F 20 B9 BA JSR $BAB9       Exponenten von
                                FAC und ARG addieren
.,E042 60       RTS             Rücksprung

                                *** Polynomberechnung
                                *** y=a1*x+a2*x^3+a3*x^5+...
.,E043 85 71    STA $71         Zeiger auf
.,E045 84 72    STY $72         Polynomkoeffizienten
.,E047 20 CA BB JSR $BBCA       FAC nach Akku #3 bringen
.,E04A A9 57    LDA #$57        Zeiger auf Akku #3
.,E04C 20 28 BA JSR $BA28       FAC * Akku #3 (quadrieren)
.,E04F 20 5D E0 JSR $E05D       Polynomberechnung
.,E052 A9 57    LDA #$57        Zeiger auf
.,E054 A0 00    LDY #$00        Akku #3
.,E056 4C 28 BA JMP $BA28       FAC = FAC * Akku #3

                                *** Polynomberechnung
                                *** y=a0+a1*x+a2*x^2+a3*x^3+...
.,E059 85 71    STA $71         Zeiger auf
.,E05B 84 72    STY $72         Polynomgrad
.,E05D 20 C7 BB JSR $BBC7       FAC nach Akku #4 bringen
.,E060 B1 71    LDA ($71),Y     Polynomgrad
.,E062 85 67    STA $67         als Zähler
.,E064 A4 71    LDY $71         Zeiger für Polynomauswertung
.,E066 C8       INY             Zeiger erhöhen,
.,E067 98       TYA             zeigt dann
.,E068 D0 02    BNE $E06C       auf ersten Koeffizienten
.,E06A E6 72    INC $72         Zeiger
.,E06C 85 71    STA $71         für
.,E06E A4 72    LDY $72         Polynomauswertung
.,E070 20 28 BA JSR $BA28       FAC = FAC * Konstante
.,E073 A5 71    LDA $71         Zeiger in
.,E075 A4 72    LDY $72         (A/Y)
.,E077 18       CLC             Zeiger
.,E078 69 05    ADC #$05        um 5 erhöhen - nächste Zahl
.,E07A 90 01    BCC $E07D       wenn kleiner, dann zu $E07D
.,E07C C8       INY             ansonsten erhöhen
.,E07D 85 71    STA $71         Zeiger für
.,E07F 84 72    STY $72         Polynomauswertung speichern
.,E081 20 67 B8 JSR $B867       FAC = FAC + Konstante
.,E084 A9 5C    LDA #$5C        Zeiger auf
.,E086 A0 00    LDY #$00        Akku #4
.,E088 C6 67    DEC $67         Zähler erniedrigen
.,E08A D0 E4    BNE $E070       schon alle, nein, dann
                                zu $E070
.,E08C 60       RTS             Rücksprung

                                *** Konstanten für RND
.:E08D 98 35 44 7A 00           11879546
.:E092 68 28 B1 46 00           3.92767774E-4

                                *** BASIC-Funktion RND
.,E097 20 2B BC JSR $BC2B       Vorzeichen holen
.,E09A 30 37    BMI $E0D3       negativ ?, dann zu $E0D3
.,E09C D0 20    BNE $E0BE       nicht Null?, dann zu $E0BE
.,E09E 20 F3 FF JSR $FFF3       Basis-Adresse CIA holen
.,E0A1 86 22    STX $22         als Zeiger
.,E0A3 84 23    STY $23         speichern
.,E0A5 A0 04    LDY #$04        Zähler setzen
.,E0A7 B1 22    LDA ($22),Y     LOW-Byte Timer A laden
.,E0A9 85 62    STA $62         und speichern
.,E0AB C8       INY             Zähler erhöhen
.,E0AC B1 22    LDA ($22),Y     HIGH-Byte Timer A laden
.,E0AE 85 64    STA $64         und speichern
.,E0B0 A0 08    LDY #$08        Zähler neu setzen
.,E0B2 B1 22    LDA ($22),Y     TOD 1/10 sec laden
.,E0B4 85 63    STA $63         und speichern
.,E0B6 C8       INY             Zähler erhöhen
.,E0B7 B1 22    LDA ($22),Y     TOD sec laden
.,E0B9 85 65    STA $65         und speichern
.,E0BB 4C E3 E0 JMP $E0E3       weiter bei $E0E3
.,E0BE A9 8B    LDA #$8B        Zeiger auf
.,E0C0 A0 00    LDY #$00        letzten RND-Wert
.,E0C2 20 A2 BB JSR $BBA2       nach FAC holen
.,E0C5 A9 8D    LDA #$8D        Zeiger auf
.,E0C7 A0 E0    LDY #$E0        Konstante
.,E0C9 20 28 BA JSR $BA28       FAC = FAC * Konstante
.,E0CC A9 92    LDA #$92        Zeiger auf
.,E0CE A0 E0    LDY #$E0        Konstante
.,E0D0 20 67 B8 JSR $B867       FAC = FAC + Konstante
.,E0D3 A6 65    LDX $65         alle
.,E0D5 A5 62    LDA $62         Stel-
.,E0D7 85 65    STA $65         len
.,E0D9 86 62    STX $62         im
.,E0DB A6 63    LDX $63         FAC
.,E0DD A5 64    LDA $64         ver-
.,E0DF 85 63    STA $63         tau-
.,E0E1 86 64    STX $64         schen
.,E0E3 A9 00    LDA #$00        Vorzeichen
.,E0E5 85 66    STA $66         positiv
.,E0E7 A5 61    LDA $61         Exponent in
.,E0E9 85 70    STA $70         Rundungsstelle
.,E0EB A9 80    LDA #$80        Zufallszahl
.,E0ED 85 61    STA $61         speichern
.,E0EF 20 D7 B8 JSR $B8D7       FAC linksbündig machen
.,E0F2 A2 8B    LDX #$8B        Zeiger auf
.,E0F4 A0 00    LDY #$00        letzten RND-Wert
.,E0F6 4C D4 BB JMP $BBD4       FAC runden und speichern

                                *** Fehlerauswertung nach
                                *** I/O-Routinen
.,E0F9 C9 F0    CMP #$F0        RS 232 OPEN oder CLOSE ?
.,E0FB D0 07    BNE $E104       nein
.,E0FD 84 38    STY $38         BASIC-RAM Ende
.,E0FF 86 37    STX $37         neu setzen
.,E101 4C 63 A6 JMP $A663       und zum CLR-Befehl
.,E104 AA       TAX             Fehlernummer nach X
.,E105 D0 02    BNE $E109       nicht Null ?
.,E107 A2 1E    LDX #$1E        sonst Nummer für 'BREAK'
.,E109 4C 37 A4 JMP $A437       Fehlermeldung ausgeben

                                *** BASIC BSOUT
.,E10C 20 D2 FF JSR $FFD2       ein Zeichen ausgeben
.,E10F B0 E8    BCS $E0F9       Fehler ?
.,E111 60       RTS             Rücksprung

                                *** BASIC BASIN
.,E112 20 CF FF JSR $FFCF       ein Zeichen holen
.,E115 B0 E2    BCS $E0F9       Fehler ?
.,E117 60       RTS             Rücksprung

                                *** BASIC CKOUT
.,E118 20 AD E4 JSR $E4AD       Ausgabegerät setzen
.,E11B B0 DC    BCS $E0F9       Fehler ?
.,E11D 60       RTS             Rücksprung

                                *** BASIC CHKIN
.,E11E 20 C6 FF JSR $FFC6       Eingabegerät setzen
.,E121 B0 D6    BCS $E0F9       Fehler ?
.,E123 60       RTS             Rücksprung

                                *** BASIC GETIN
.,E124 20 E4 FF JSR $FFE4       ein Zeichen holen
.,E127 B0 D0    BCS $E0F9       Fehler ?
.,E129 60       RTS             Rücksprung

                                *** SYS-Befehl
.,E12A 20 8A AD JSR $AD8A       FRMNUM, numerischen
                                Ausdruck holen
.,E12D 20 F7 B7 JSR $B7F7       in Adressformat wandeln,
                                nach $14/$15
.,E130 A9 E1    LDA #$E1        Rück-
.,E132 48       PHA             sprungadresse
.,E133 A9 46    LDA #$46        auf
.,E135 48       PHA             Stack
.,E136 AD 0F 03 LDA $030F       Status,
.,E139 48       PHA             in Stack
.,E13A AD 0C 03 LDA $030C       Akku,
.,E13D AE 0D 03 LDX $030D       X-Register und
.,E140 AC 0E 03 LDY $030E       Y-Register übergeben
.,E143 28       PLP             Status setzen
.,E144 6C 14 00 JMP ($0014)     Routine aufrufen
.,E147 08       PHP             Status speichern
.,E148 8D 0C 03 STA $030C       Akku,
.,E14B 8E 0D 03 STX $030D       X-Register,
.,E14E 8C 0E 03 STY $030E       Y-Register und
.,E151 68       PLA             Status
.,E152 8D 0F 03 STA $030F       wieder speichern
.,E155 60       RTS             Rücksprung

                                *** SAVE-Befehl
.,E156 20 D4 E1 JSR $E1D4       Parameter (Filenamen, Prim,
                                und Sek. Adresse)
.,E159 A6 2D    LDX $2D         Endadresse gleich
.,E15B A4 2E    LDY $2E         BASIC-Rücksprung
.,E15D A9 2B    LDA #$2B        Startadresse gleich Zeiger
                                auf BASIC Anfang
.,E15F 20 D8 FF JSR $FFD8       Save-Routine
.,E162 B0 95    BCS $E0F9       Fehler ?
.,E164 60       RTS             Rücksprung

                                *** VERIFY-Befehl
.,E165 A9 01    LDA #$01        Verify-
.:E167 2C       .BYTE $2C       Flag

                                *** LOAD-Befehl
.,E168 A9 00    LDA #$00        Load-Flag
.,E16A 85 0A    STA $0A         speichern
.,E16C 20 D4 E1 JSR $E1D4       Parameter holen
.,E16F A5 0A    LDA $0A         Flag
.,E171 A6 2B    LDX $2B         Startadresse gleich
.,E173 A4 2C    LDY $2C         BASIC-Start
.,E175 20 D5 FF JSR $FFD5       Load-Routine
.,E178 B0 57    BCS $E1D1       Fehler ?
.,E17A A5 0A    LDA $0A         Load/Verify - Flag
.,E17C F0 17    BEQ $E195       Load ?
.,E17E A2 1C    LDX #$1C        Offset für 'VERIFY ERROR'
.,E180 20 B7 FF JSR $FFB7       Status holen
.,E183 29 10    AND #$10        Fehler-Bit isolieren
.,E185 D0 17    BNE $E19E       Statusbit gesetzt, dann
                                Fehler
.,E187 A5 7A    LDA $7A         muß HIGH-Byte $7B sein
.,E189 C9 02    CMP #$02        Test auf Direkt-Modus
.,E18B F0 07    BEQ $E194       ja, dann fertig
.,E18D A9 64    LDA #$64        Zeiger auf
.,E18F A0 A3    LDY #$A3        'OK'
.,E191 4C 1E AB JMP $AB1E       ausgeben
.,E194 60       RTS             Rücksprung
.,E195 20 B7 FF JSR $FFB7       Status holen
.,E198 29 BF    AND #$BF        EOF-Bit löschen
.,E19A F0 05    BEQ $E1A1       kein Fehler
.,E19C A2 1D    LDX #$1D        Offset für 'LOAD ERROR'
.,E19E 4C 37 A4 JMP $A437       Fehlermeldung ausgeben
.,E1A1 A5 7B    LDA $7B         Direkt-
.,E1A3 C9 02    CMP #$02        modus testen
.,E1A5 D0 0E    BNE $E1B5       nein, dann weiter
.,E1A7 86 2D    STX $2D         Endadresse gleich
.,E1A9 84 2E    STY $2E         Rücksprung
.,E1AB A9 76    LDA #$76        Zeiger auf
.,E1AD A0 A3    LDY #$A3        'READY'
.,E1AF 20 1E AB JSR $AB1E       String ausgeben
.,E1B2 4C 2A A5 JMP $A52A       Programmzeilen neu binden,
                                CLR
.,E1B5 20 8E A6 JSR $A68E       CHRGET-Zeiger auf
                                Programmstart
.,E1B8 20 33 A5 JSR $A533       Programmzeilen neu binden
.,E1BB 4C 77 A6 JMP $A677       RESTORE, BASIC initialisieren

                                *** BASIC-Befehl OPEN
.,E1BE 20 19 E2 JSR $E219       Parameter holen
.,E1C1 20 C0 FF JSR $FFC0       OPEN-Routine
.,E1C4 B0 0B    BCS $E1D1       Fehler ?
.,E1C6 60       RTS             Rücksprung

                                *** BASIC-Befehl CLOSE
.,E1C7 20 19 E2 JSR $E219       Parameter holen
.,E1CA A5 49    LDA $49         Filenummer
.,E1CC 20 C3 FF JSR $FFC3       CLOSE-Routine
.,E1CF 90 C3    BCC $E194       kein Fehler, RTS
.,E1D1 4C F9 E0 JMP $E0F9       zur Fehlerauswertung

                                *** Parameter für LOAD und SAVE
                                *** holen
.,E1D4 A9 00    LDA #$00        Default für Länge des
                                Filenamen
.,E1D6 20 BD FF JSR $FFBD       Filenamenparameter setzen
.,E1D9 A2 01    LDX #$01        Default für Gerätenummer
.,E1DB A0 00    LDY #$00        Sekundäradresse
.,E1DD 20 BA FF JSR $FFBA       Fileparameter setzen
.,E1E0 20 06 E2 JSR $E206       weitere Zeichen ?
.,E1E3 20 57 E2 JSR $E257       Filenamen holen
.,E1E6 20 06 E2 JSR $E206       weitere Zeichen ?
.,E1E9 20 00 E2 JSR $E200       Geräteadresse holen
.,E1EC A0 00    LDY #$00        Sekundäradresse
.,E1EE 86 49    STX $49         Geräteadresse
.,E1F0 20 BA FF JSR $FFBA       Fileparameter setzen
.,E1F3 20 06 E2 JSR $E206       weitere Zeichen ?
.,E1F6 20 00 E2 JSR $E200       Sekundäradresse holen
.,E1F9 8A       TXA             in Akku schieben
.,E1FA A8       TAY             Sekundäradresse
.,E1FB A6 49    LDX $49         Gerätenummer
.,E1FD 4C BA FF JMP $FFBA       Fileparameter setzen
.,E200 20 0E E2 JSR $E20E       prüft auf Komma und weitere
                                Zeichen
.,E203 4C 9E B7 JMP $B79E       holt Byte-Wert nach X

                                *** prüft auf weitere Zeichen
.,E206 20 79 00 JSR $0079       CHRGOT letztes Zeichen
.,E209 D0 02    BNE $E20D       weiteres Zeichen, dann
                                Rückkehr
.,E20B 68       PLA             sonst Rückkehr zur
.,E20C 68       PLA             übergeordneten Routine
.,E20D 60       RTS             Rücksprung
.,E20E 20 FD AE JSR $AEFD       prüft auf Komma
.,E211 20 79 00 JSR $0079       CHRGOT letztes Zeichen holen
.,E214 D0 F7    BNE $E20D       weitere Zeichen, dann
                                Rückkehr
.,E216 4C 08 AF JMP $AF08       'SYNTAX ERROR'

                                *** Parameter für OPEN holen
.,E219 A9 00    LDA #$00        Default für Länge des
                                Filenamens
.,E21B 20 BD FF JSR $FFBD       Filenamenparameter setzen
.,E21E 20 11 E2 JSR $E211       weitere Zeichen ?
.,E221 20 9E B7 JSR $B79E       holt logische Filenummer
                                nach X-Reg
.,E224 86 49    STX $49         und speichern
.,E226 8A       TXA             logische Filenummer
.,E227 A2 01    LDX #$01        Default für Geräteadresse
.,E229 A0 00    LDY #$00        Sekundäradresse
.,E22B 20 BA FF JSR $FFBA       Fileparameter setzen
.,E22E 20 06 E2 JSR $E206       weitere Zeichen ?
.,E231 20 00 E2 JSR $E200       holt Geräteadresse
.,E234 86 4A    STX $4A         und speichern
.,E236 A0 00    LDY #$00        Sekundäradresse
.,E238 A5 49    LDA $49         logische Filenummer
.,E23A E0 03    CPX #$03        Gerätenummer kleiner 3 ?
.,E23C 90 01    BCC $E23F       ja
.,E23E 88       DEY             sonst Sekundäradresse auf
                                255 (keine Sek-Adr)
.,E23F 20 BA FF JSR $FFBA       Fileparameter setzen
.,E242 20 06 E2 JSR $E206       weitere Zeichen ?
.,E245 20 00 E2 JSR $E200       holt Sekundäradresse
.,E248 8A       TXA             in Akku schieben
.,E249 A8       TAY             Sekundäradresse
.,E24A A6 4A    LDX $4A         Gerätenummer
.,E24C A5 49    LDA $49         logische Filenummer
.,E24E 20 BA FF JSR $FFBA       Fileparameter setzen
.,E251 20 06 E2 JSR $E206       weitere Zeichen ?
.,E254 20 0E E2 JSR $E20E       prüft auf Komma
.,E257 20 9E AD JSR $AD9E       FRMEVL Ausdruck holen
.,E25A 20 A3 B6 JSR $B6A3       holt Stringparameter, FRESTR
.,E25D A6 22    LDX $22         Adresse des
.,E25F A4 23    LDY $23         Filenamens
.,E261 4C BD FF JMP $FFBD       Filenamenparameter setzen

                                *** BASIC-Funktion COS
.,E264 A9 E0    LDA #$E0        Zeiger auf
.,E266 A0 E2    LDY #$E2        Konstante Pi/2
.,E268 20 67 B8 JSR $B867       zu FAC addieren

                                *** BASIC-Funktion SIN
.,E26B 20 0C BC JSR $BC0C       FAC runden und nach ARG
.,E26E A9 E5    LDA #$E5        Zeiger auf
.,E270 A0 E2    LDY #$E2        Konstante Pi*2
.,E272 A6 6E    LDX $6E         Vorzeichen von ARG
.,E274 20 07 BB JSR $BB07       FAC durch 2*Pi dividieren
.,E277 20 0C BC JSR $BC0C       FAC runden und nach ARG
.,E27A 20 CC BC JSR $BCCC       INT - Funktion
.,E27D A9 00    LDA #$00        Vergleichsbyte
.,E27F 85 6F    STA $6F         löschen
.,E281 20 53 B8 JSR $B853       ARG minus FAC
.,E284 A9 EA    LDA #$EA        Zeiger auf
.,E286 A0 E2    LDY #$E2        Konstante 0.25
.,E288 20 50 B8 JSR $B850       0.25 - FAC
.,E28B A5 66    LDA $66         Vorzeichen laden
.,E28D 48       PHA             Vorzeichen in Stack
.,E28E 10 0D    BPL $E29D       positiv ?
.,E290 20 49 B8 JSR $B849       FAC + 0.5
.,E293 A5 66    LDA $66         Vorzeichen
.,E295 30 09    BMI $E2A0       negativ ?
.,E297 A5 12    LDA $12         Vorzeichen laden
.,E299 49 FF    EOR #$FF        und umdrehen
.,E29B 85 12    STA $12         Vorzeichen speichern
.,E29D 20 B4 BF JSR $BFB4       Vorzeichen wechseln
.,E2A0 A9 EA    LDA #$EA        Zeiger auf
.,E2A2 A0 E2    LDY #$E2        Konstante 0.25
.,E2A4 20 67 B8 JSR $B867       FAC + 0.25
.,E2A7 68       PLA             Vorzeichen holen
.,E2A8 10 03    BPL $E2AD       positiv ?
.,E2AA 20 B4 BF JSR $BFB4       Vorzeichen wechseln
.,E2AD A9 EF    LDA #$EF        Zeiger auf
.,E2AF A0 E2    LDY #$E2        Polynomkoeffizienten
.,E2B1 4C 43 E0 JMP $E043       Polynom berechnen

                                *** BASIC-Funktion TAN
.,E2B4 20 CA BB JSR $BBCA       FAC nach Akku#3
.,E2B7 A9 00    LDA #$00        Flag
.,E2B9 85 12    STA $12         setzen
.,E2BB 20 6B E2 JSR $E26B       SIN berechnen
.,E2BE A2 4E    LDX #$4E        Zeiger auf
.,E2C0 A0 00    LDY #$00        Hilfsakku
.,E2C2 20 F6 E0 JSR $E0F6       FAC nach Hilfsakku
.,E2C5 A9 57    LDA #$57        Zeiger auf
.,E2C7 A0 00    LDY #$00        Akku#3
.,E2C9 20 A2 BB JSR $BBA2       Akku#3 nach FAC
.,E2CC A9 00    LDA #$00        Vorzeichen
.,E2CE 85 66    STA $66         löschen
.,E2D0 A5 12    LDA $12         Flag
.,E2D2 20 DC E2 JSR $E2DC       COS berechnen
.,E2D5 A9 4E    LDA #$4E        Zeiger auf
.,E2D7 A0 00    LDY #$00        Hilfsakku (SIN)
.,E2D9 4C 0F BB JMP $BB0F       durch FAC dividieren
.,E2DC 48       PHA             COS
.,E2DD 4C 9D E2 JMP $E29D       berechnen

                                *** Konstanten für SIN und COS
.:E2E0 81 49 0F DA A2           1.57079633   Pi/2
.:E2E5 83 49 0F DA A2           6.28318531   2*Pi
.:E2EA 7F 00 00 00 00            .25
.:E2EF 05                       5 = Polynomgrad, 6
                                Koeffizienten
.:E2F0 84 E6 1A 2D 1B           -14.3813907
.:E2F5 86 28 07 FB F8            42.0077971
.:E2FA 87 99 68 89 01           -76.7041703
.:E2FF 87 23 35 DF E1            81.6052237
.:E304 86 A5 5D E7 28           -41.3147021
.:E309 83 49 0F DA A2             6.28318531   2*Pi

                                *** BASIC-Funktion ATN
.,E30E A5 66    LDA $66         Vorzeichen
.,E310 48       PHA             retten
.,E311 10 03    BPL $E316       positiv ?
.,E313 20 B4 BF JSR $BFB4       Vorzeichen vertauschen
.,E316 A5 61    LDA $61         Exponent
.,E318 48       PHA             retten
.,E319 C9 81    CMP #$81        Zahl mit 1 vergleichen
.,E31B 90 07    BCC $E324       kleiner ?
.,E31D A9 BC    LDA #$BC        Zeiger auf
.,E31F A0 B9    LDY #$B9        Konstante 1
.,E321 20 0F BB JSR $BB0F       1 durch FAC dividieren
                                (Kehrwert)
.,E324 A9 3E    LDA #$3E        Zeiger auf
.,E326 A0 E3    LDY #$E3        Polynomkoeffizienten
.,E328 20 43 E0 JSR $E043       Polynom berechnen
.,E32B 68       PLA             Exponent zurückholen
.,E32C C9 81    CMP #$81        war Zahl
.,E32E 90 07    BCC $E337       kleiner 1, dann zu $E337
.,E330 A9 E0    LDA #$E0        Zeiger auf
.,E332 A0 E2    LDY #$E2        Konstante Pi/2
.,E334 20 50 B8 JSR $B850       Pi/2 minus FAC
.,E337 68       PLA             Vorzeichen holen
.,E338 10 03    BPL $E33D       positiv ?
.,E33A 4C B4 BF JMP $BFB4       Vorzeichen wechseln
.,E33D 60       RTS             Rücksprung

                                *** Fließkommakonstanten für
                                *** ATN-Funktion
.:E33E 0B                       11 = Polynomgrad, dann 12
                                Koeffizienten
.:E33F 76 B3 83 BD D3           -6.84793912E-04
.:E344 79 1E F4 A6 F5            4.85094216E-03
.:E349 7B 83 FC B0 10            -.0161117015
.:E34E 7C 0C 1F 67 CA             .034209638
.:E353 7C DE 53 CB C1            -.054279133
.:E358 7D 14 64 70 4C             .0724571965
.:E35D 7D B7 EA 51 7A            -.0898019185
.:E362 7D 63 30 88 7E             .110932413
.:E367 7E 92 44 99 3A            -.142839808
.:E36C 7E 4C CC 91 C7             .19999912
.:E371 7F AA AA AA 13            -.333333316
.:E376 81 00 00 00 00            1

                                *** BASIC NMI-Einsprung
.,E37B 20 CC FF JSR $FFCC       CLRCH
.,E37E A9 00    LDA #$00        Eingabegerät gleich
.,E380 85 13    STA $13         Tastatur
.,E382 20 7A A6 JSR $A67A       BASIC initialisieren
.,E385 58       CLI             Interrupt freigeben
.,E386 A2 80    LDX #$80        Flag für kein Fehler
.,E388 6C 00 03 JMP ($0300)     BASIC Warmstart Vektor
                                JMP $E38B
.,E38B 8A       TXA             Fehlernummer in Akku
.,E38C 30 03    BMI $E391       kein Fehler, dann 'ready.'
.,E38E 4C 3A A4 JMP $A43A       Fehlermeldung ausgeben
.,E391 4C 74 A4 JMP $A474       Ready - Modus

                                *** BASIC Kaltstart
.,E394 20 53 E4 JSR $E453       BASIC-Vektoren setzen
.,E397 20 BF E3 JSR $E3BF       RAM initialisieren
.,E39A 20 22 E4 JSR $E422       Einschaltmeldung ausgeben
.,E39D A2 FB    LDX #$FB        Stackzeiger
.,E39F 9A       TXS             setzen
.,E3A0 D0 E4    BNE $E386       zum Warmstart

                                *** Kopie der CHRGET-Routine
.,E3A2 E6 7A    INC $7A         LOW-Byte Zeiger erhöhen
.,E3A4 D0 02    BNE $E3A8       Zeiger in BASIC-Text erhöhen
.,E3A6 E6 7B    INC $7B         HIGH-Byte Zeiger erhöhen
.,E3A8 AD 60 EA LDA $EA60       BASIC-Adresse laden
.,E3AB C9 3A    CMP #$3A        keine Zahl,
.,E3AD B0 0A    BCS $E3B9       dann fertig
.,E3AF C9 20    CMP #$20        ' ' Leerzeichen überlesen
.,E3B1 F0 EF    BEQ $E3A2       ja, nächstes Zeichen
.,E3B3 38       SEC             Test auf
.,E3B4 E9 30    SBC #$30        Ziffer,
.,E3B6 38       SEC             dann
.,E3B7 E9 D0    SBC #$D0        C=1
.,E3B9 60       RTS             Rücksprung

                                *** Anfangswert für RND-Funktion
.:E3BA 80 4F C7 52 58           .811635157

                                *** RAM für BASIC initialisieren
.,E3BF A9 4C    LDA #$4C        JMP
.,E3C1 85 54    STA $54         für Funktionen
.,E3C3 8D 10 03 STA $0310       für USR-Funktion
.,E3C6 A9 48    LDA #$48        Zeiger auf
.,E3C8 A0 B2    LDY #$B2        'ILLEGAL QUANTITY'
.,E3CA 8D 11 03 STA $0311       als USR-Vektor
.,E3CD 8C 12 03 STY $0312       speichern
.,E3D0 A9 91    LDA #$91        Adresse
.,E3D2 A0 B3    LDY #$B3        $B391
.,E3D4 85 05    STA $05         als Vektor für
.,E3D6 84 06    STY $06         Fest-/Fließkomma-Wandlung
.,E3D8 A9 AA    LDA #$AA        Adresse
.,E3DA A0 B1    LDY #$B1        $B1AA
.,E3DC 85 03    STA $03         als Vektor für
.,E3DE 84 04    STY $04         Fließ-/Festkomma-Wandlung
.,E3E0 A2 1C    LDX #$1C        Zähler setzen
.,E3E2 BD A2 E3 LDA $E3A2,X     CHRGET-Routine
.,E3E5 95 73    STA $73,X       ins
.,E3E7 CA       DEX             RAM kopieren
.,E3E8 10 F8    BPL $E3E2       schon alles?
.,E3EA A9 03    LDA #$03        Schrittweise
.,E3EC 85 53    STA $53         für Garbage Collection
.,E3EE A9 00    LDA #$00        FAC-Rundungsbyte
.,E3F0 85 68    STA $68         löschen
.,E3F2 85 13    STA $13         Eingabegerät gleich
.,E3F4 85 18    STA $18         Tastatur
.,E3F6 A2 01    LDX #$01        Dummys
.,E3F8 8E FD 01 STX $01FD       für Linkadresse beim
.,E3FB 8E FC 01 STX $01FC       Zeileneinbau
.,E3FE A2 19    LDX #$19        Zeiger für
.,E400 86 16    STX $16         Stringverwaltung
.,E402 38       SEC             RAM-
.,E403 20 9C FF JSR $FF9C       Start holen
.,E406 86 2B    STX $2B         als BASIC-Start
.,E408 84 2C    STY $2C         speichern
.,E40A 38       SEC             RAM-
.,E40B 20 99 FF JSR $FF99       Ende holen
.,E40E 86 37    STX $37         als
.,E410 84 38    STY $38         BASIC-
.,E412 86 33    STX $33         Ende
.,E414 84 34    STY $34         speichern
.,E416 A0 00    LDY #$00        $00
.,E418 98       TYA             an
.,E419 91 2B    STA ($2B),Y     BASIC-Start
.,E41B E6 2B    INC $2B         den
.,E41D D0 02    BNE $E421       BASIC-
.,E41F E6 2C    INC $2C         Start + 1
.,E421 60       RTS             Programmnde
.,E422 A5 2B    LDA $2B         Zeiger auf
.,E424 A4 2C    LDY $2C         BASIC-RAM Start
.,E426 20 08 A4 JSR $A408       prüft auf Platz im Speicher
.,E429 A9 73    LDA #$73        Zeiger auf
.,E42B A0 E4    LDY #$E4        Einschaltmeldung
.,E42D 20 1E AB JSR $AB1E       String ausgeben
.,E430 A5 37    LDA $37         BASIC-
.,E432 38       SEC             Ende
.,E433 E5 2B    SBC $2B         minus
.,E435 AA       TAX             BASIC-Start
.,E436 A5 38    LDA $38         gleich
.,E438 E5 2C    SBC $2C         Bytes free
.,E43A 20 CD BD JSR $BDCD       Anzahl ausgeben
.,E43D A9 60    LDA #$60        Zeiger auf
.,E43F A0 E4    LDY #$E4        'BASIC BYTES FREE'
.,E441 20 1E AB JSR $AB1E       String ausgeben
.,E444 4C 44 A6 JMP $A644       zum NEW-Befehl

                                *** Tabelle der BASIC-Vektoren
.:E447 8B E3 83 A4 7C A5 1A A7
.:E44F E4 A7 86 AE

.,E453 A2 0B    LDX #$0B        Die
.,E455 BD 47 E4 LDA $E447,X     BASIC-
.,E458 9D 00 03 STA $0300,X     Vektoren
.,E45B CA       DEX             laden
.,E45C 10 F7    BPL $E455       schon alle?
.,E45E 60       RTS             Rücksprung

                                *** Betriebssystem

                                *** System-Meldungen
.:E45F 00 20 42 41 53 49 43 20  basic bytes free
.:E467 42 59 54 45 53 20 46 52
.:E46F 45 45 0D 00 93 0D 20 20
.:E473 93 0D 20 20 20 20 2A 2A  (clr) **** commodore 64 basic v2 ****
.:E47B 2A 2A 20 43 4F 4D 4D 4F  (cr) (cr) 64k ram system
.:E483 44 4F 52 45 20 36 34 20
.:E48B 42 41 53 49 43 20 56 32
.:E493 20 2A 2A 2A 2A 0D 0D 20
.:E49B 36 34 4B 20 52 41 4D 20
.:E4A3 53 59 53 54 45 4D 20 20
.:E4AB 00
.:E4AC 5C

                                *** BASIC-CKOUT Routine
.,E4AD 48       PHA             Akkuinhalt in Stack
.,E4AE 20 C9 FF JSR $FFC9       CKOUT Ausgabegerät setzen
.,E4B1 AA       TAX             Fehlernummer nach X
.,E4B2 68       PLA             Akkuinhalt zurückholen
.,E4B3 90 01    BCC $E4B6       kein Fehler ?
.,E4B5 8A       TXA             Fehlernummer wieder in Akku
.,E4B6 60       RTS             Rücksprung

.:E4B7 AA AA AA AA AA AA AA AA
.:E4BF AA AA AA AA AA AA AA AA
.:E4C7 AA AA AA AA AA AA AA AA
.:E4CF AA AA AA AA AA AA AA AA
.:E4D7 AA AA AA

                                *** Hintergrundfarbe setzen
.,E4DA AD 21 D0 LDA $D021       Farbe holen
.,E4DD 91 F3    STA ($F3),Y     ins Farbram schreiben
.,E4DF 60       RTS             Rücksprung

                                *** wartet auf Commodore-Taste
.,E4E0 69 02    ADC #$02        2*256/60 = 8.5 Sekunden
                                warten
.,E4E2 A4 91    LDY $91         Flag testen
.,E4E4 C8       INY             und erhöhen
.,E4E5 D0 04    BNE $E4EB       Taste gedrückt ?
.,E4E7 C5 A1    CMP $A1         Zeit noch nicht um ?,
.,E4E9 D0 F7    BNE $E4E2       dann warten
.,E4EB 60       RTS             Rücksprung

                                *** Timerkonstanten für RS 232
                                *** Baud Rate, PAL-Version
.:E4EC 19 26                    $2619 = 9753     50 Baud
.:E4EE 44 19                    $1944 = 6468     75 Baud
.:E4F0 1A 11                    $111A = 4378    110 Baud
.:E4F2 E8 0D                    $0DE8 = 3560    134.5 Baud
.:E4F4 70 0C                    $0C70 = 3184    150 Baud
.:E4F6 06 06                    $0606 = 1542    300 Baud
.:E4F8 D1 02                    $02D1 =  736    600 Baud
.:E4FA 37 01                    $0137 =  311   1200 Baud
.:E4FC AE 00                    $00AE =  174   1800 Baud
.:E4FE 69 00                    $0069 =  105   2400 Baud

                                *** Basis-Adresse des CIAs holen
.,E500 A2 00    LDX #$00        Adresse
.,E502 A0 DC    LDY #$DC        $DC00
.,E504 60       RTS             Rücksprung

                                *** holt Anzahl der Zeilen und
                                *** Spalten
.,E505 A2 28    LDX #$28        40 Spalten
.,E507 A0 19    LDY #$19        25 Zeilen
.,E509 60       RTS             Rücksprung

                                *** Cursor setzen (C=0) / holen
                                *** (C=1)
.,E50A B0 07    BCS $E513       Carry gesetzt, dann zu $E513
.,E50C 86 D6    STX $D6         Zeile
.,E50E 84 D3    STY $D3         Spalte
.,E510 20 6C E5 JSR $E56C       Cursor setzen
.,E513 A6 D6    LDX $D6         Zeile
.,E515 A4 D3    LDY $D3         Spalte
.,E517 60       RTS             Rücksprung

                                *** Bildschirm Reset
.,E518 20 A0 E5 JSR $E5A0       Videocontroller
                                initialisieren
.,E51B A9 00    LDA #$00        Shift-
.,E51D 8D 91 02 STA $0291       Commodore ermöglichen
.,E520 85 CF    STA $CF         Cursor nicht in Blinkphase
.,E522 A9 48    LDA #$48        Adresse
.,E524 8D 8F 02 STA $028F       ($028F) = $EB48
.,E527 A9 EB    LDA #$EB        setzen
.,E529 8D 90 02 STA $0290       = Zeiger auf Adressen für
                                Tastaturdekodierung
.,E52C A9 0A    LDA #$0A        10
.,E52E 8D 89 02 STA $0289       max. Länge des
                                Tastaturpuffers
.,E531 8D 8C 02 STA $028C       Zähler für
                                Repeat-Geschwindigkeit
.,E534 A9 0E    LDA #$0E        hellblau
.,E536 8D 86 02 STA $0286       Augenblickliche Farbe
.,E539 A9 04    LDA #$04        Repeat-
.,E53B 8D 8B 02 STA $028B       Geschwindigkeit
.,E53E A9 0C    LDA #$0C        Cursor
.,E540 85 CD    STA $CD         Blinkzeit
.,E542 85 CC    STA $CC         Cursor Blinkflag

                                *** Bildschirm löschen
.,E544 AD 88 02 LDA $0288       Speicherseite für
                                Bildschirm-RAM
.,E547 09 80    ORA #$80        Adressen
.,E549 A8       TAY             der
.,E54A A9 00    LDA #$00        Bild-
.,E54C AA       TAX             schirm-
.,E54D 94 D9    STY $D9,X       zeilen
.,E54F 18       CLC             40 addieren
.,E550 69 28    ADC #$28        (eine Zeile)
.,E552 90 01    BCC $E555       kein Übertrag, dann
                                HIGH-Byte nicht erhöhen
.,E554 C8       INY             HIGH-Byte erhöhen
.,E555 E8       INX             LOW-Byte erhöhen
.,E556 E0 1A    CPX #$1A        26, alle Zeilen ?
.,E558 D0 F3    BNE $E54D       nein, dann weiter
.,E55A A9 FF    LDA #$FF        Kennzeichnung der
.,E55C 95 D9    STA $D9,X       26, Zeile
.,E55E A2 18    LDX #$18        24, Anzahl der Zeilen minus 1
.,E560 20 FF E9 JSR $E9FF       Bildschirmzeile löschen
.,E563 CA       DEX             Zähler erniedrigen
.,E564 10 FA    BPL $E560       schon alle?

                                *** Cursor Home
.,E566 A0 00    LDY #$00        Löschen der
.,E568 84 D3    STY $D3         Cursorspalte und
.,E56A 84 D6    STY $D6         Cursorzeile

                                *** Cursorpos. berechnen,
                                *** Bildschirmzeiger setzen
.,E56C A6 D6    LDX $D6         Cursorzeile
.,E56E A5 D3    LDA $D3         Cursorspalte
.,E570 B4 D9    LDY $D9,X       HIGH-Bytes für Doppelzeilen
.,E572 30 08    BMI $E57C       einfache Zeile, dann zu $E57C
.,E574 18       CLC             Spalte
.,E575 69 28    ADC #$28        +40
.,E577 85 D3    STA $D3         und speichern
.,E579 CA       DEX             nächste Zeile
.,E57A 10 F4    BPL $E570       schon alle?
.,E57C 20 F0 E9 JSR $E9F0       Zeiger auf Video-RAM setzen
.,E57F A9 27    LDA #$27        39 Spalten
.,E581 E8       INX             Zeiger auf Bildschirmtabelle
                                erhöhen
.,E582 B4 D9    LDY $D9,X       HIGH-Byte Startadresse der
                                Zeile in Y-REG schreiben
.,E584 30 06    BMI $E58C       Verzweige falls größer,
                                gleich 128
.,E586 18       CLC             Cursor eine Zeile
.,E587 69 28    ADC #$28        tiefer setzen (+40 Spalten)
.,E589 E8       INX             Zeiger auf Bildschirmtabelle
                                erhöhen
.,E58A 10 F6    BPL $E582       unbedingter Sprung
.,E58C 85 D5    STA $D5         Zeilenlänge speichern
.,E58E 4C 24 EA JMP $EA24       Zeiger auf Farb-RAM berechnen
                                Rücksprung
.,E591 E4 C9    CPX $C9         wenn Cursorzeile
.,E593 F0 03    BEQ $E598       gleich null, dann Rücksprung
.,E595 4C ED E6 JMP $E6ED       Adresse für zugehörige
                                Zeilennummer nach $D1/$D2
.,E598 60       RTS             Rücksprung
.,E599 EA       NOP             no operation
.,E59A 20 A0 E5 JSR $E5A0       Videocontroller
                                initialisieren
.,E59D 4C 66 E5 JMP $E566       Cursor Home

                                *** Videocontroller
                                *** initialisieren
.,E5A0 A9 03    LDA #$03        Ausgabe auf
.,E5A2 85 9A    STA $9A         Bildschirm
.,E5A4 A9 00    LDA #$00        Eingabe von
.,E5A6 85 99    STA $99         Tastatur
.,E5A8 A2 2F    LDX #$2F        47
.,E5AA BD B8 EC LDA $ECB8,X     Konstanten
.,E5AD 9D FF CF STA $CFFF,X     in Videokontroller schreiben
.,E5B0 CA       DEX             Zähler erniedrigen
.,E5B1 D0 F7    BNE $E5AA       schon alle?
.,E5B3 60       RTS             Rücksprung

                                *** Zeichen aus Tastaturpuffer
                                *** holen
.,E5B4 AC 77 02 LDY $0277       erstes Zeichen holen
.,E5B7 A2 00    LDX #$00        Zähler auf Null
.,E5B9 BD 78 02 LDA $0278,X     Puffer nach
.,E5BC 9D 77 02 STA $0277,X     vorne aufrücken
.,E5BF E8       INX             Zähler erhöhen
.,E5C0 E4 C6    CPX $C6         mit Anzahl der
.,E5C2 D0 F5    BNE $E5B9       Zeichen vergleichen
.,E5C4 C6 C6    DEC $C6         Zeichenzahl erniedrigen
.,E5C6 98       TYA             Zeichen in Akku holen
.,E5C7 58       CLI             Interrupt freigeben
.,E5C8 18       CLC             Carry löschen
.,E5C9 60       RTS             Rücksprung

                                *** Warteschleife für
                                *** Tastatureingabe
.,E5CA 20 16 E7 JSR $E716       Zeichen auf Bildschirm
                                ausgeben
.,E5CD A5 C6    LDA $C6         Anzahl der
.,E5CF 85 CC    STA $CC         gedrückten
.,E5D1 8D 92 02 STA $0292       Tasten
.,E5D4 F0 F7    BEQ $E5CD       keine Taste gedrückt ?,
                                dann warten
.,E5D6 78       SEI             Interrupt verhindern
.,E5D7 A5 CF    LDA $CF         Cursor in Blink-Phase ?
.,E5D9 F0 0C    BEQ $E5E7       nein
.,E5DB A5 CE    LDA $CE         Zeichen unter dem Cursor
.,E5DD AE 87 02 LDX $0287       Farbe unter dem Cursor
.,E5E0 A0 00    LDY #$00        Cursor nicht
.,E5E2 84 CF    STY $CF         in Blinkphase
.,E5E4 20 13 EA JSR $EA13       Zeichen und Farbe setzen
.,E5E7 20 B4 E5 JSR $E5B4       Zeichen aus Tastaturpuffer
                                holen
.,E5EA C9 83    CMP #$83        Kode für
.,E5EC D0 10    BNE $E5FE       'SHIFT RUN' ?
.,E5EE A2 09    LDX #$09        9 Zeichen
.,E5F0 78       SEI             Interrupt verhindern
.,E5F1 86 C6    STX $C6         Zeichenzahl merken
.,E5F3 BD E6 EC LDA $ECE6,X     'LOAD (cr) RUN (cr)'
.,E5F6 9D 76 02 STA $0276,X     in Tastaturpuffer holen
.,E5F9 CA       DEX             nächstes Zeichen
.,E5FA D0 F7    BNE $E5F3       schon alle ?
.,E5FC F0 CF    BEQ $E5CD       und auswerten
.,E5FE C9 0D    CMP #$0D        'CR'
.,E600 D0 C8    BNE $E5CA       nein ?, dann zurück zur
                                Warteschleife
.,E602 A4 D5    LDY $D5         Länge der Bildschirmzeile
.,E604 84 D0    STY $D0         CR-Flag setzen
.,E606 B1 D1    LDA ($D1),Y     Zeichen vom Bildschirm holen
.,E608 C9 20    CMP #$20        Leerzeichen
.,E60A D0 03    BNE $E60F       am Ende
.,E60C 88       DEY             der
.,E60D D0 F7    BNE $E606       Zeile
.,E60F C8       INY             eliminieren
.,E610 84 C8    STY $C8         Position als Index merken
.,E612 A0 00    LDY #$00        Cursorspalte
.,E614 8C 92 02 STY $0292       gleich Null
.,E617 84 D3    STY $D3         Cursorposition auf Null
.,E619 84 D4    STY $D4         Hochkommaflag löschen
.,E61B A5 C9    LDA $C9         wenn Cursorzeile schon durch
.,E61D 30 1B    BMI $E63A       scrollen verschwunden, dann
                                zu $E63A
.,E61F A6 D6    LDX $D6         Cursorzeile
.,E621 20 ED E6 JSR $E6ED       Adresse für Startzeile setzen
.,E624 E4 C9    CPX $C9         Fehler bei Eingabe ?,
.,E626 D0 12    BNE $E63A       dann nochmal lesen
.,E628 A5 CA    LDA $CA         letzte Spalte
.,E62A 85 D3    STA $D3         in Spaltenzeiger bringen
.,E62C C5 C8    CMP $C8         mit Index vergleichen
.,E62E 90 0A    BCC $E63A       wenn kleiner, dann Zeile
                                auswerten
.,E630 B0 2B    BCS $E65D       wenn größer oder gleich, dann
                                keine Eingabe

                                *** Ein Zeichen vom Bildschirm
                                *** holen
.,E632 98       TYA             die
.,E633 48       PHA             Re-
.,E634 8A       TXA             gister
.,E635 48       PHA             retten
.,E636 A5 D0    LDA $D0         CR-Flag
.,E638 F0 93    BEQ $E5CD       nein, dann zur Warteschleife
.,E63A A4 D3    LDY $D3         Spalte
.,E63C B1 D1    LDA ($D1),Y     Zeichen vom Bildschirm holen
.,E63E 85 D7    STA $D7         und
.,E640 29 3F    AND #$3F        nach
.,E642 06 D7    ASL $D7         ASCII
.,E644 24 D7    BIT $D7         wandeln
.,E646 10 02    BPL $E64A       wenn Bit 6 nicht gesetzt,
                                dann zu $E64A
.,E648 09 80    ORA #$80        Bit 7 setzen
.,E64A 90 04    BCC $E650       Zeichen nicht revers ?, dann
                                zu $E650
.,E64C A6 D4    LDX $D4         Hochkommaflag nicht
.,E64E D0 04    BNE $E654       gesetzt ?, dann zu $E654
.,E650 70 02    BVS $E654       wenn ja, dann zu $E654
.,E652 09 40    ORA #$40        Bit 6 im Zeichen setzen
.,E654 E6 D3    INC $D3         Cursor eins weiter setzen
.,E656 20 84 E6 JSR $E684       auf Hochkomma testen
.,E659 C4 C8    CPY $C8         Cursor in letzter Spalte ?
.,E65B D0 17    BNE $E674       wenn nicht, dann zu $E674
.,E65D A9 00    LDA #$00        Zeile
.,E65F 85 D0    STA $D0         vollständig gelesen
.,E661 A9 0D    LDA #$0D        'CR'
.,E663 A6 99    LDX $99         ans Ende der Zeile setzen
.,E665 E0 03    CPX #$03        Eingabe vom Bildschirm ?
.,E667 F0 06    BEQ $E66F       ja, dann zu $E66F
.,E669 A6 9A    LDX $9A         Ausgabe auf Bildschirm
.,E66B E0 03    CPX #$03        ja, dann
.,E66D F0 03    BEQ $E672       zu $E672
.,E66F 20 16 E7 JSR $E716       Zeichen auf Bildschirm
                                schreiben
.,E672 A9 0D    LDA #$0D        Wert für
.,E674 85 D7    STA $D7         'CR'
.,E676 68       PLA             die
.,E677 AA       TAX             Register
.,E678 68       PLA             zürück-
.,E679 A8       TAY             holen
.,E67A A5 D7    LDA $D7         Bildschirm-Kode
.,E67C C9 DE    CMP #$DE        mit Kode für Pi vergleichen
.,E67E D0 02    BNE $E682       nein ?, dann fertig
.,E680 A9 FF    LDA #$FF        ja ?, durch BASIC-Kode
                                für Pi ersetzen
.,E682 18       CLC             Carry löschen
.,E683 60       RTS             Rücksprung

                                *** auf Hochkomma testen
.,E684 C9 22    CMP #$22        '"' ?
.,E686 D0 08    BNE $E690       nein ?, dann fertig
.,E688 A5 D4    LDA $D4         Hochkomma-
.,E68A 49 01    EOR #$01        Flag
.,E68C 85 D4    STA $D4         umdrehen
.,E68E A9 22    LDA #$22        Hochkomma-Code wieder-
                                herstellen
.,E690 60       RTS             Rücksprung

                                *** Zeichen auf Bildschirm
                                *** ausgeben
.,E691 09 40    ORA #$40        Bit 6 im Zeichen setzen
.,E693 A6 C7    LDX $C7         RVS ?
.,E695 F0 02    BEQ $E699       Umwandlung in Bildschirmcode
.,E697 09 80    ORA #$80        ja, dann Bit 7 setzen
.,E699 A6 D8    LDX $D8         wenn Einfügzähler Null,
.,E69B F0 02    BEQ $E69F       dann zu $E69F
.,E69D C6 D8    DEC $D8         Zähler erniedrigen
.,E69F AE 86 02 LDX $0286       Farbkode
.,E6A2 20 13 EA JSR $EA13       Zeichen in Bildschirm-RAM
                                schreiben
.,E6A5 20 B6 E6 JSR $E6B6       Tabelle der Zeilenanfänge
                                aktualisieren
.,E6A8 68       PLA             Y-Reg
.,E6A9 A8       TAY             aus Stack
.,E6AA A5 D8    LDA $D8         wenn Einfügzähler Null,
.,E6AC F0 02    BEQ $E6B0       dann zu $E6B0
.,E6AE 46 D4    LSR $D4         Hochkommamodus löschen
.,E6B0 68       PLA             X-Reg
.,E6B1 AA       TAX             aus Stack
.,E6B2 68       PLA             Akku aus Stack
.,E6B3 18       CLC             Carry löschen
.,E6B4 58       CLI             Interrupt freigeben
.,E6B5 60       RTS             Rücksprung

                                *** HIGH-Byte für Zeilenanfänge
                                *** neu berechnen
.,E6B6 20 B3 E8 JSR $E8B3       Zeilenzeiger erhöhen
.,E6B9 E6 D3    INC $D3         Cursorspalte erhöhen
.,E6BB A5 D5    LDA $D5         Zeilenlänge holen
.,E6BD C5 D3    CMP $D3         Vergleich mit Cursorspalte
.,E6BF B0 3F    BCS $E700       nicht überschritten, dann RTS
.,E6C1 C9 4F    CMP #$4F        79 Zeichen (Doppelzeile) ?
.,E6C3 F0 32    BEQ $E6F7       wenn ja, dann zu $E6F7
.,E6C5 AD 92 02 LDA $0292       Zeilenübergang nicht
.,E6C8 F0 03    BEQ $E6CD       im Editmodus, dann zu $E6CD
.,E6CA 4C 67 E9 JMP $E967       neue Zeile einfügen
.,E6CD A6 D6    LDX $D6         Zeile
.,E6CF E0 19    CPX #$19        25 ?
.,E6D1 90 07    BCC $E6DA       wenn ja, dann zu $E6DA
.,E6D3 20 EA E8 JSR $E8EA       SCROLL
.,E6D6 C6 D6    DEC $D6         Cursorzeilenzeiger
                                erniedrigen
.,E6D8 A6 D6    LDX $D6         Zähler holen
.,E6DA 16 D9    ASL $D9,X       Zeile
.,E6DC 56 D9    LSR $D9,X       markieren
.,E6DE E8       INX             Zähler erhöhen
.,E6DF B5 D9    LDA $D9,X       Startzeile
.,E6E1 09 80    ORA #$80        markieren
.,E6E3 95 D9    STA $D9,X       und speichern
.,E6E5 CA       DEX             Zähler erniedrigen
.,E6E6 A5 D5    LDA $D5         Zeilenlänge
.,E6E8 18       CLC             mit
.,E6E9 69 28    ADC #$28        40 addieren
.,E6EB 85 D5    STA $D5         und speichern
.,E6ED B5 D9    LDA $D9,X       keine Doppelzeile,
.,E6EF 30 03    BMI $E6F4       dann zu $E6F4
.,E6F1 CA       DEX             Zähler erniedrigen
.,E6F2 D0 F9    BNE $E6ED       noch nicht alle?, dann weiter
.,E6F4 4C F0 E9 JMP $E9F0       Zeiger auf Farb-RAM
                                für Zeile X
.,E6F7 C6 D6    DEC $D6         Cursorzeile erniedrigen
.,E6F9 20 7C E8 JSR $E87C       und initialisieren
.,E6FC A9 00    LDA #$00        Spalte
.,E6FE 85 D3    STA $D3         auf Null
.,E700 60       RTS             Rücksprung

                                *** Rückschritt in vorhergehende
                                *** Zeile
.,E701 A6 D6    LDX $D6         Cursorzeile
.,E703 D0 06    BNE $E70B       wenn null, dann zu $E70B
.,E705 86 D3    STX $D3         Cursorspalte
.,E707 68       PLA             Sprungadresse
.,E708 68       PLA             aus Stack holen
.,E709 D0 9D    BNE $E6A8       unbedingter Sprung
.,E70B CA       DEX             Zeilennummer
.,E70C 86 D6    STX $D6         erniedrigen
.,E70E 20 6C E5 JSR $E56C       Cursorposition berechnen
.,E711 A4 D5    LDY $D5         Zeilenlänge
.,E713 84 D3    STY $D3         speichern
.,E715 60       RTS             Rücksprung

                                *** Ausgabe auf Bildschirm
.,E716 48       PHA             Zeichen
.,E717 85 D7    STA $D7         merken
.,E719 8A       TXA             die
.,E71A 48       PHA             Re-
.,E71B 98       TYA             gister
.,E71C 48       PHA             retten
.,E71D A9 00    LDA #$00        Eingabeflag
.,E71F 85 D0    STA $D0         löschen
.,E721 A4 D3    LDY $D3         Cursorspalte
.,E723 A5 D7    LDA $D7         Zeichen
.,E725 10 03    BPL $E72A       wenn kleiner 128, dann
                                zu $E72A
.,E727 4C D4 E7 JMP $E7D4       Zeichen größer $7F behandeln
.,E72A C9 0D    CMP #$0D        'CARRIAGE RETURN' ?
.,E72C D0 03    BNE $E731       wenn nicht, dann zu $E731
.,E72E 4C 91 E8 JMP $E891       Return ausgeben
.,E731 C9 20    CMP #$20        ' '
.,E733 90 10    BCC $E745       druckendes Zeichen ?
.,E735 C9 60    CMP #$60        Zahl kleiner $60,
.,E737 90 04    BCC $E73D       dann keine Graphikzeichen
.,E739 29 DF    AND #$DF        Umwandlung in BS-Kode
.,E73B D0 02    BNE $E73F       unbedingter Sprung
.,E73D 29 3F    AND #$3F        Umwandlung in BS-Kode
.,E73F 20 84 E6 JSR $E684       Test auf Hochkomma
.,E742 4C 93 E6 JMP $E693       zur Ausgabe, ASCII-Kode
                                in BS-Code
.,E745 A6 D8    LDX $D8         wenn Einfügzähler =0,
.,E747 F0 03    BEQ $E74C       dann zu $E74C
.,E749 4C 97 E6 JMP $E697       ASCII-Kode in BS-Code
.,E74C C9 14    CMP #$14        nicht 'DEL' ?,
.,E74E D0 2E    BNE $E77E       dann zu $E77E
.,E750 98       TYA             erste Spalte =0
.,E751 D0 06    BNE $E759       dann zu $E759
.,E753 20 01 E7 JSR $E701       zurück in vorherige Zeile
.,E756 4C 73 E7 JMP $E773       Zeichen in Cursorposition
                                eliminieren
.,E759 20 A1 E8 JSR $E8A1       Rückschritt prüfen
.,E75C 88       DEY             Zeiger erniedrigen
.,E75D 84 D3    STY $D3         und speichern
.,E75F 20 24 EA JSR $EA24       Zeiger auf Farb-RAM berechnen
.,E762 C8       INY             Zeiger erhöhen
.,E763 B1 D1    LDA ($D1),Y     Zeichen vom Bildschirm
.,E765 88       DEY             Zeiger erniedrigen
.,E766 91 D1    STA ($D1),Y     eins nach links schieben
.,E768 C8       INY             Zeiger erhöhen
.,E769 B1 F3    LDA ($F3),Y     Farbe
.,E76B 88       DEY             Zeiger erniedrigen
.,E76C 91 F3    STA ($F3),Y     eins nach links schieben
.,E76E C8       INY             Zeiger erhöhen
.,E76F C4 D5    CPY $D5         Endspalte nicht
.,E771 D0 EF    BNE $E762       erreicht, dann weiter
.,E773 A9 20    LDA #$20        Blank
.,E775 91 D1    STA ($D1),Y     einfügen
.,E777 AD 86 02 LDA $0286       Farbcode
.,E77A 91 F3    STA ($F3),Y     setzen
.,E77C 10 4D    BPL $E7CB       fertig
.,E77E A6 D4    LDX $D4         Hochkomma-Modus ?
.,E780 F0 03    BEQ $E785       nein
.,E782 4C 97 E6 JMP $E697       Zeichen revers ausgeben
.,E785 C9 12    CMP #$12        'RVS ON' ?
.,E787 D0 02    BNE $E78B       nein, dann
.,E789 85 C7    STA $C7         Flag für RVS setzen
.,E78B C9 13    CMP #$13        'HOME' ?
.,E78D D0 03    BNE $E792       nein
.,E78F 20 66 E5 JSR $E566       ja, Cursor Home
.,E792 C9 1D    CMP #$1D        'Cursor right' ?
.,E794 D0 17    BNE $E7AD       nein
.,E796 C8       INY             Zeiger erhöhen
.,E797 20 B3 E8 JSR $E8B3       Cursorposition prüfen
.,E79A 84 D3    STY $D3         neuer Zeiger
.,E79C 88       DEY             Zeiger erniedrigen
.,E79D C4 D5    CPY $D5         keine neue Zeile ?,
.,E79F 90 09    BCC $E7AA       dann fertig
.,E7A1 C6 D6    DEC $D6         Zeiger erniedrigen
.,E7A3 20 7C E8 JSR $E87C       Zeile initialisieren
.,E7A6 A0 00    LDY #$00        Spalte
.,E7A8 84 D3    STY $D3         gleich null
.,E7AA 4C A8 E6 JMP $E6A8       fertig
.,E7AD C9 11    CMP #$11        'Cursor down' ?
.,E7AF D0 1D    BNE $E7CE       nein
.,E7B1 18       CLC             plus
.,E7B2 98       TYA             40,
.,E7B3 69 28    ADC #$28        eine Zeile
.,E7B5 A8       TAY             tiefer
.,E7B6 E6 D6    INC $D6         Zeiger erhöhen
.,E7B8 C5 D5    CMP $D5         neue Zeile erreicht?
.,E7BA 90 EC    BCC $E7A8       nein, dann zu $E7A8
.,E7BC F0 EA    BEQ $E7A8       Ja, dann zu $E7A8
.,E7BE C6 D6    DEC $D6         Zeiger erniedrigen
.,E7C0 E9 28    SBC #$28        40 abziehen
.,E7C2 90 04    BCC $E7C8       genügend abgezogen, dann
                                zu $E7C8
.,E7C4 85 D3    STA $D3         Spalte setzen
.,E7C6 D0 F8    BNE $E7C0       noch mal
.,E7C8 20 7C E8 JSR $E87C       Zeile initialisieren
.,E7CB 4C A8 E6 JMP $E6A8       fertig
.,E7CE 20 CB E8 JSR $E8CB       prüft auf Farbcodes
.,E7D1 4C 44 EC JMP $EC44       Test auf weitere
                                Sonderzeichen

                                *** Zeichen größer $127
.,E7D4 29 7F    AND #$7F        Kode größer 127,
                                Bit 7 löschen
.,E7D6 C9 7F    CMP #$7F        nicht 'Pi' ?
.,E7D8 D0 02    BNE $E7DC       dann zu $E7DC
.,E7DA A9 5E    LDA #$5E        Bildschirmkode für Pi
.,E7DC C9 20    CMP #$20        Steuerzeichen ?
.,E7DE 90 03    BCC $E7E3       ja
.,E7E0 4C 91 E6 JMP $E691       druckendes Zeichen ausgeben
.,E7E3 C9 0D    CMP #$0D        nicht 'Shift return' ?
.,E7E5 D0 03    BNE $E7EA       dann zu $E7EA
.,E7E7 4C 91 E8 JMP $E891       neue Zeile
.,E7EA A6 D4    LDX $D4         Hochkomma-Hodus ?
.,E7EC D0 3F    BNE $E82D       ja, Steuerzeichen revers
                                ausgeben
.,E7EE C9 14    CMP #$14        nicht 'INS' ?,
.,E7F0 D0 37    BNE $E829       dann zu $E829
.,E7F2 A4 D5    LDY $D5         Zeilenlänge
.,E7F4 B1 D1    LDA ($D1),Y     letztes Zeichen in Zeile
.,E7F6 C9 20    CMP #$20        gleich Leerzeichen ?
.,E7F8 D0 04    BNE $E7FE       nein, dann zu $E7FE
.,E7FA C4 D3    CPY $D3         Cursor in letzter Spalte ?
.,E7FC D0 07    BNE $E805       nein, dann zu $E805
.,E7FE C0 4F    CPY #$4F        79 ? maximale Zeilenlänge
.,E800 F0 24    BEQ $E826       letzte Spalte, dann keine
                                Aktion
.,E802 20 65 E9 JSR $E965       Leerzeile einfügen
.,E805 A4 D5    LDY $D5         Zeilenlänge
.,E807 20 24 EA JSR $EA24       Zeiger auf Farbram berechnen
.,E80A 88       DEY             Zeiger erniedrigen
.,E80B B1 D1    LDA ($D1),Y     Zeichen vom Bildschirm
.,E80D C8       INY             Zeiger erhöhen
.,E80E 91 D1    STA ($D1),Y     eins nach rechts schieben
.,E810 88       DEY             Zeiger erniedrigen
.,E811 B1 F3    LDA ($F3),Y     und Farbe
.,E813 C8       INY             Zeiger erhöhen
.,E814 91 F3    STA ($F3),Y     verschieben
.,E816 88       DEY             Zeiger erniedrigen
.,E817 C4 D3    CPY $D3         bis zur aktuellen Position
                                aufrücken
.,E819 D0 EF    BNE $E80A       nicht ?, dann weiter
.,E81B A9 20    LDA #$20        Leerzeichen
.,E81D 91 D1    STA ($D1),Y     an augenblickliche Position
                                schreiben
.,E81F AD 86 02 LDA $0286       Farbe
.,E822 91 F3    STA ($F3),Y     setzen
.,E824 E6 D8    INC $D8         Anzahl der Inserts erhöhen
.,E826 4C A8 E6 JMP $E6A8       Ende der Zeichenausgabe
.,E829 A6 D8    LDX $D8         Zähler Null?
.,E82B F0 05    BEQ $E832       dann zu $E832
.,E82D 09 40    ORA #$40        Bit 6 setzen
.,E82F 4C 97 E6 JMP $E697       und Zeichen ausgeben
.,E832 C9 11    CMP #$11        nicht Cursor up ?,
.,E834 D0 16    BNE $E84C       dann zu $E84C
.,E836 A6 D6    LDX $D6         Zeile
.,E838 F0 37    BEQ $E871       null, dann fertig
.,E83A C6 D6    DEC $D6         Zeilennummer um eins erniedrigen
.,E83C A5 D3    LDA $D3         Spalte
.,E83E 38       SEC             40
.,E83F E9 28    SBC #$28        abziehen
                                nicht in Doppelzeile ?,
.,E841 90 04    BCC $E847       dann zu $E847
.,E843 85 D3    STA $D3         Cursorspalte
.,E845 10 2A    BPL $E871       positiv, ok
.,E847 20 6C E5 JSR $E56C       Bildschirmzeiger neu setzen
.,E84A D0 25    BNE $E871       unbedingter Sprung
.,E84C C9 12    CMP #$12        nicht 'RVS OFF' ?,
.,E84E D0 04    BNE $E854       dann zu $E854
.,E850 A9 00    LDA #$00        RVS-Flag
.,E852 85 C7    STA $C7         löschen
.,E854 C9 1D    CMP #$1D        nicht ’Cursor left' ?,
.,E856 D0 12    BNE $E86A       dann zu $E86A
.,E858 98       TYA             wenn erste Spalte,
.,E859 F0 09    BEQ $E864       dann zu $E864
.,E85B 20 A1 E8 JSR $E8A1       Cursorzeile erniedrigen
.,E85E 88       DEY             Zähler erniedrigen
.,E85F 84 D3    STY $D3         Cursorspalte
.,E861 4C A8 E6 JMP $E6A8       fertig
.,E864 20 01 E7 JSR $E701       Rückschritt in vorherige
                                Zeile
.,E867 4C A8 E6 JMP $E6A8       fertig
.,E86A C9 13    CMP #$13        nicht 'CLR SCREEN' ?,
.,E86C D0 06    BNE $E874       dann zu $E874
.,E86E 20 44 E5 JSR $E544       Bildschirm löschen
.,E871 4C A8 E6 JMP $E6A8       fertig
.,E874 09 80    ORA #$80        Bit 7 wiederherstellen
.,E876 20 CB E8 JSR $E8CB       auf Farbcode prüfen
.,E879 4C 4F EC JMP $EC4F       prüft auf Umschaltung
                                Text/Grafik
.,E87C 46 C9    LSR $C9         Flag für Zeilenwechsel
.,E87E A6 D6    LDX $D6         Cursorzeilenzeiger
.,E880 E8       INX             Zeiger erhöhen
.,E881 E0 19    CPX #$19        noch nicht letzte Zeile ?,
.,E883 D0 03    BNE $E888       dann zu $E888
.,E885 20 EA E8 JSR $E8EA       Bildschirm scrollen
.,E888 B5 D9    LDA $D9,X       nächste Zeile, dann
.,E88A 10 F4    BPL $E880       wieder scrollen
.,E88C 86 D6    STX $D6         neue Zeile
.,E88E 4C 6C E5 JMP $E56C       Cursorposition berechnen
.,E891 A2 00    LDX #$00        Einfüg-
.,E893 86 D8    STX $D8         zähler löschen
.,E895 86 C7    STX $C7         Flag für RVS löschen
.,E897 86 D4    STX $D4         Quote-Modus löschen
.,E899 86 D3    STX $D3         Cursor in erste Spalte
.,E89B 20 7C E8 JSR $E87C       Zeile initialisieren
.,E89E 4C A8 E6 JMP $E6A8       fertig
.,E8A1 A2 02    LDX #$02        maximale Zeilenanzahl
.,E8A3 A9 00    LDA #$00        wenn Cursorspalte
.,E8A5 C5 D3    CMP $D3         gleich Akku,
.,E8A7 F0 07    BEQ $E8B0       dann zu $E8B0
.,E8A9 18       CLC             40 addieren,
.,E8AA 69 28    ADC #$28        eine Zeile
.,E8AC CA       DEX             schon zweimal addiert ?,
.,E8AD D0 F6    BNE $E8A5       ja, dann weiter
.,E8AF 60       RTS             Rücksprung
.,E8B0 C6 D6    DEC $D6         Zeiger auf Cursorzeile
                                erniedrigen
.,E8B2 60       RTS             Rücksprung
.,E8B3 A2 02    LDX #$02        maximale Zeilenanzahl
.,E8B5 A9 27    LDA #$27        39, letzte Spalte
.,E8B7 C5 D3    CMP $D3         wenn Cursorspalte gleich
.,E8B9 F0 07    BEQ $E8C2       akku ?, dann zu $E8C2
.,E8BB 18       CLC             40
.,E8BC 69 28    ADC #$28        addieren
.,E8BE CA       DEX             schon zweimal ?,
.,E8BF D0 F6    BNE $E8B7       ja, dann weiter
.,E8C1 60       RTS             Rücksprung
.,E8C2 A6 D6    LDX $D6         wenn Cursorzeile
.,E8C4 E0 19    CPX #$19        gleich 25,
.,E8C6 F0 02    BEQ $E8CA       dann fertig
.,E8C8 E6 D6    INC $D6         Zeiger auf Cursorzeile
                                erhöhen
.,E8CA 60       RTS             Rücksprung

                                *** prüft auf Farbcodes
.,E8CB A2 0F    LDX #$0F        Anzahl der Kodes
.,E8CD DD DA E8 CMP $E8DA,X     mit Farbcodetabelle
                                vergleichen
.,E8D0 F0 04    BEQ $E8D6       wenn gefunden, dann farbe
                                setzen
.,E8D2 CA       DEX             nächster Farbcode
.,E8D3 10 F8    BPL $E8CD       schon alle ?
.,E8D5 60       RTS             Rücksprung
.,E8D6 8E 86 02 STX $0286       Farbcode setzen
.,E8D9 60       RTS             Rücksprung

                                *** Tabelle der Farb-Kodes
.:E8DA 90 05 1C 9F 9C 1E 1F 9E
.:E8E2 81 95 96 97 98 99 9A 9B

                                *** Bildschirm scrollen
.,E8EA A5 AC    LDA $AC         Alle
.,E8EC 48       PHA             wichtigen
.,E8ED A5 AD    LDA $AD         Zeiger
.,E8EF 48       PHA             in
.,E8F0 A5 AE    LDA $AE         den
.,E8F2 48       PHA             Stack
.,E8F3 A5 AF    LDA $AF         schie-
.,E8F5 48       PHA             ben
.,E8F6 A2 FF    LDX #$FF        ab Zeile Null beginnen
.,E8F8 C6 D6    DEC $D6         Cursorzeiger
.,E8FA C6 C9    DEC $C9         erniedrigen
.,E8FC CE A5 02 DEC $02A5       Fortsetzungszeile erniedrigen
.,E8FF E8       INX             Zeilennummer erhöhen
.,E900 20 F0 E9 JSR $E9F0       Zeiger auf Video-RAM für
                                Zeile X
.,E903 E0 18    CPX #$18        24
.,E905 B0 0C    BCS $E913       schon alle Zeilen ?
.,E907 BD F1 EC LDA $ECF1,X     LOW-Byte holen
.,E90A 85 AC    STA $AC         und speichern
.,E90C B5 DA    LDA $DA,X       HIGH-Byte
.,E90E 20 C8 E9 JSR $E9C8       Bildschirmzeile nach oben
                                schieben
.,E911 30 EC    BMI $E8FF       nächste Zeile
.,E913 20 FF E9 JSR $E9FF       unterste Bildschirmzeile
                                löschen
.,E916 A2 00    LDX #$00        HIGH-
.,E918 B5 D9    LDA $D9,X       Bytes
.,E91A 29 7F    AND #$7F        und
.,E91C B4 DA    LDY $DA,X       die
.,E91E 10 02    BPL $E922       Doppel-
.,E920 09 80    ORA #$80        zeilen
.,E922 95 D9    STA $D9,X       ver-
.,E924 E8       INX             schieben
.,E925 E0 18    CPX #$18        nicht 24 ?,
.,E927 D0 EF    BNE $E918       dann nochmal
.,E929 A5 F1    LDA $F1         Zeile
.,E92B 09 80    ORA #$80        als einfache Zeile
.,E92D 85 F1    STA $F1         auszeichnen
.,E92F A5 D9    LDA $D9         wenn Fortsetzungszeile,
.,E931 10 C3    BPL $E8F6       dann nochmal
.,E933 E6 D6    INC $D6         Zeiger auf Cursor erhöhen
.,E935 EE A5 02 INC $02A5       Fortsetzungszeile erhöhen
.,E938 A9 7F    LDA #$7F        Kode
.,E93A 8D 00 DC STA $DC00       für
.,E93D AD 01 DC LDA $DC01       Tastaturabfrage
.,E940 C9 FB    CMP #$FB        CTRL-Taste gedrückt ?
.,E942 08       PHP             Statusregister retten
.,E943 A9 7F    LDA #$7F        code für
.,E945 8D 00 DC STA $DC00       Tastaturabfrage
.,E948 28       PLP             Statusregister holen
.,E949 D0 0B    BNE $E956       nicht gedrückt ?
.,E94B A0 00    LDY #$00        Ver-
.,E94D EA       NOP             zö-
.,E94E CA       DEX             geru-
.,E94F D0 FC    BNE $E94D       ngs-
.,E951 88       DEY             sch-
.,E952 D0 F9    BNE $E94D       leife
.,E954 84 C6    STY $C6         Anzahl der gedrückten
                                Tasten gleich null
.,E956 A6 D6    LDX $D6         alle
.,E958 68       PLA             benö-
.,E959 85 AF    STA $AF         tigten
.,E95B 68       PLA             Zei-
.,E95C 85 AE    STA $AE         ger
.,E95E 68       PLA             zu-
.,E95F 85 AD    STA $AD         rück-
.,E961 68       PLA             ho-
.,E962 85 AC    STA $AC         len
.,E964 60       RTS             Rücksprung

                                *** Einfügen einer
                                *** Fortsetzungszeile
.,E965 A6 D6    LDX $D6         Zeiger auf Cursorzeile
.,E967 E8       INX             Zeiger erhöhen
.,E968 B5 D9    LDA $D9,X       untere Zeile gleich
.,E96A 10 FB    BPL $E967       Cursorzeile, dann zu $E967
.,E96C 8E A5 02 STX $02A5       Zeilennummer
.,E96F E0 18    CPX #$18        gleich
.,E971 F0 0E    BEQ $E981       24
.,E973 90 0C    BCC $E981       dann zu $E981
.,E975 20 EA E8 JSR $E8EA       Bildschirm scrollen
.,E978 AE A5 02 LDX $02A5       Zeilennummer
.,E97B CA       DEX             erniedrigen
.,E97C C6 D6    DEC $D6         Zeiger auf Cursorzeile
                                erniedrigen
.,E97E 4C DA E6 JMP $E6DA       Zeile initialisieren
.,E981 A5 AC    LDA $AC         Alle
.,E983 48       PHA             benötigten
.,E984 A5 AD    LDA $AD         Zeiger
.,E986 48       PHA             in
.,E987 A5 AE    LDA $AE         den
.,E989 48       PHA             Stack
.,E98A A5 AF    LDA $AF         schie-
.,E98C 48       PHA             ben
.,E98D A2 19    LDX #$19        25
.,E98F CA       DEX             Zeilennummer
.,E990 20 F0 E9 JSR $E9F0       Zeilen-Zeiger berechnen
.,E993 EC A5 02 CPX $02A5       alle Zeilen verschoben ?,
.,E996 90 0E    BCC $E9A6       wenn ja,
.,E998 F0 0C    BEQ $E9A6       dann zu $E9A6
.,E99A BD EF EC LDA $ECEF,X     LOW-Byte des Zeilenanfangs
.,E99D 85 AC    STA $AC         setzen
.,E99F B5 D8    LDA $D8,X       HIGH-Byte setzen
.,E9A1 20 C8 E9 JSR $E9C8       Zeile nach oben schieben
.,E9A4 30 E9    BMI $E98F       Unbedingter Sprung
.,E9A6 20 FF E9 JSR $E9FF       Bildschirmzeile löschen
.,E9A9 A2 17    LDX #$17        HIGH-Byte-Tabelle
.,E9AB EC A5 02 CPX $02A5       verschieben
.,E9AE 90 0F    BCC $E9BF       alles verschoben ?
.,E9B0 B5 DA    LDA $DA,X       HIGH-
.,E9B2 29 7F    AND #$7F        Byte-
.,E9B4 B4 D9    LDY $D9,X       und
.,E9B6 10 02    BPL $E9BA       Doppelzeilen-
.,E9B8 09 80    ORA #$80        Tabelle
.,E9BA 95 DA    STA $DA,X       nach
.,E9BC CA       DEX             unten schieben
.,E9BD D0 EC    BNE $E9AB       schon alles ?
.,E9BF AE A5 02 LDX $02A5       Zeilennummer
.,E9C2 20 DA E6 JSR $E6DA       MSB neu berechnen
.,E9C5 4C 58 E9 JMP $E958       Register zurückholen, RTS

                                *** Zeile nach oben schieben
.,E9C8 29 03    AND #$03        Bildschirmzeiger
.,E9CA 0D 88 02 ORA $0288       für neue Zeile
.,E9CD 85 AD    STA $AD         berechnen
.,E9CF 20 E0 E9 JSR $E9E0       Zeiger für neue Zeile
                                berechnen
.,E9D2 A0 27    LDY #$27        39 Zeichen
.,E9D4 B1 AC    LDA ($AC),Y     alle
.,E9D6 91 D1    STA ($D1),Y     Zeichen
.,E9D8 B1 AE    LDA ($AE),Y     und
.,E9DA 91 F3    STA ($F3),Y     Farbe übertragen
.,E9DC 88       DEY             nächstes Zeichen
.,E9DD 10 F5    BPL $E9D4       schon alle ?
.,E9DF 60       RTS             Rücksprung

                                *** Bildschirmzeile für
                                *** Scrollzeile berechnen
.,E9E0 20 24 EA JSR $EA24       Zeiger auf Farb-RAM berechnen
.,E9E3 A5 AC    LDA $AC         Zeiger
.,E9E5 85 AE    STA $AE         für Zeile
.,E9E7 A5 AD    LDA $AD         speichern
.,E9E9 29 03    AND #$03        Startadresse
.,E9EB 09 D8    ORA #$D8        des Video-RAM
.,E9ED 85 AF    STA $AF         berechnen
.,E9EF 60       RTS             Rücksprung

                                *** Zeiger auf Video-RAM für
                                *** Zeile X
.,E9F0 BD F0 EC LDA $ECF0,X     LOW-Byte
.,E9F3 85 D1    STA $D1         holen
.,E9F5 B5 D9    LDA $D9,X       HIGH-Byte
.,E9F7 29 03    AND #$03        des
.,E9F9 0D 88 02 ORA $0288       Video-
.,E9FC 85 D2    STA $D2         RAM
.,E9FE 60       RTS             Rücksprung

                                *** Bildschirmzeile X löschen
.,E9FF A0 27    LDY #$27        40-1 Spalten
.,EA01 20 F0 E9 JSR $E9F0       Zeilenpointer (D1/D2) setzen
.,EA04 20 24 EA JSR $EA24       Pointer (F3/F4) für Farb-RAM
                                berechnen
.,EA07 A9 20    LDA #$20        Leerzeichen
.,EA09 91 D1    STA ($D1),Y     ins Video-RAM schreiben
.,EA0B 20 DA E4 JSR $E4DA       Hintergrundfarbe setzen
.,EA0E EA       NOP
.,EA0F 88       DEY             schon 40 Zeichen gelöscht?
.,EA10 10 F5    BPL $EA07       wenn nicht, fortfahren
.,EA12 60       RTS             Rücksprung zum Hauptprogramm
.,EA13 A8       TAY             Akku retten
.,EA14 A9 02    LDA #$02
.,EA16 85 CD    STA $CD         Blinkzähler bei
                                Repeatfunktion setzen
.,EA18 20 24 EA JSR $EA24       Pointer für Farb-RAM
                                berechnen
.,EA1B 98       TYA             Akku wieder holen

                                *** Zeichen und Farbe auf
                                *** Bildschirm setzen
.,EA1C A4 D3    LDY $D3         Spaltenposition
.,EA1E 91 D1    STA ($D1),Y     Zeichen in Akku auf
                                Bildschirm
.,EA20 8A       TXA             Farb-Code von x in Akku
.,EA21 91 F3    STA ($F3),Y     in Farb-RAM schreiben
.,EA23 60       RTS             Rücksprung zum Hauptprogramm

                                *** Zeiger auf Farb-RAM berechnen
.,EA24 A5 D1    LDA $D1         $D1/$D2 = Zeiger auf
                                Video-RAM-Position
.,EA26 85 F3    STA $F3         LOW-Byte auf Zeichenposition
                                = LOW-Byte auf Farbposition
.,EA28 A5 D2    LDA $D2         HIGH-Byte der Zeichenposition
.,EA2A 29 03    AND #$03        mit HIGH-Byte der Farb-RAM-
.,EA2C 09 D8    ORA #$D8        Position = $D8 verknüpfen und
.,EA2E 85 F4    STA $F4         in $F4 = speichern
.,EA30 60       RTS             Rücksprung zum Hauptprogramm

                                *** Interrupt-Routine
.,EA31 20 EA FF JSR $FFEA       Stop-Taste, Zeit erhöhen
.,EA34 A5 CC    LDA $CC         Blink-Flag für Cursor
.,EA36 D0 29    BNE $EA61       nicht blinkend, dann weiter
.,EA38 C6 CD    DEC $CD         Blinkzähler erniedrigen
.,EA3A D0 25    BNE $EA61       nicht Null, dann weiter
.,EA3C A9 14    LDA #$14        Blinkzähler wieder auf 20
                                setzen
.,EA3E 85 CD    STA $CD         und speichern
.,EA40 A4 D3    LDY $D3         Cursorspalte
.,EA42 46 CF    LSR $CF         Blinkschalter eins dann C=1
.,EA44 AE 87 02 LDX $0287       Farbe unter Cursor
.,EA47 B1 D1    LDA ($D1),Y     Zeichen-Kode holen
.,EA49 B0 11    BCS $EA5C       Blinkschalter war ein, dann
                                weiter
.,EA4B E6 CF    INC $CF         Blinkschalter ein
.,EA4D 85 CE    STA $CE         Zeichen unter Cursor merken
.,EA4F 20 24 EA JSR $EA24       Zeiger in Farb-RAM berechnen
.,EA52 B1 F3    LDA ($F3),Y     Farb-Code holen
.,EA54 8D 87 02 STA $0287       und merken
.,EA57 AE 86 02 LDX $0286       Farb-Code unter Cursor
.,EA5A A5 CE    LDA $CE         Zeichen unter Cursor holen
.,EA5C 49 80    EOR #$80        RVS-Bit umdrehen
.,EA5E 20 1C EA JSR $EA1C       Zeichen und Farbe setzen
.,EA61 A5 01    LDA $01         Prozessorport laden
.,EA63 29 10    AND #$10        prüft Rekorder-Taste
.,EA65 F0 0A    BEQ $EA71       gedrückt, dann verzweige
.,EA67 A0 00    LDY #$00        Wert für keine Taste gedrückt
.,EA69 84 C0    STY $C0         Rekorder-Flag setzen
.,EA6B A5 01    LDA $01         Prozessorport laden
.,EA6D 09 20    ORA #$20        Rekoder-Motor ausschalten
.,EA6F D0 08    BNE $EA79       unbedingter Sprung
.,EA71 A5 C0    LDA $C0         lade Rekorder-Flag
.,EA73 D0 06    BNE $EA7B       verzweige, wenn Motor läuft
.,EA75 A5 01    LDA $01         Prozessorport laden
.,EA77 29 1F    AND #$1F        Rekorder-Motor einschalten
.,EA79 85 01    STA $01         und wieder speichern
.,EA7B 20 87 EA JSR $EA87       Tastaturabfrage
.,EA7E AD 0D DC LDA $DC0D       IRQ-Flag löschen
.,EA81 68       PLA             Accu aus dem Stapel holen
.,EA82 A8       TAY             und in Y-Register schieben
.,EA83 68       PLA             Accu aus dem Stapel holen
.,EA84 AA       TAX             und in X-Register schieben
.,EA85 68       PLA             und Rückkehr vom Interrupt
.,EA86 40       RTI

                                *** Tastaturabfrage
.,EA87 A9 00    LDA #$00
.,EA89 8D 8D 02 STA $028D       Shift/CTRL Flag rücksetzen
.,EA8C A0 40    LDY #$40        $40 = keine Taste gedrückt
.,EA8E 84 CB    STY $CB         Kode für gedrückte Taste
.,EA90 8D 00 DC STA $DC00       alle Bits des Port A löschen
.,EA93 AE 01 DC LDX $DC01       Port B laden
.,EA96 E0 FF    CPX #$FF        keine Taste gedrückt ?
.,EA98 F0 61    BEQ $EAFB       dann beenden
.,EA9A A8       TAY             Y-Register löschen
.,EA9B A9 81    LDA #$81
.,EA9D 85 F5    STA $F5         $F5/$F6 = Zeiger auf
.,EA9F A9 EB    LDA #$EB        Tastaturtabelle setzen
.,EAA1 85 F6    STA $F6
.,EAA3 A9 FE    LDA #$FE        erstes Bit für erste
                                Matrixzeile löschen
.,EAA5 8D 00 DC STA $DC00       und in Port A schreiben
.,EAA8 A2 08    LDX #$08        8 Matrixzeilen
.,EAAA 48       PHA             Bitstellung für Matrix retten
.,EAAB AD 01 DC LDA $DC01       Port B laden und
.,EAAE CD 01 DC CMP $DC01       Tastatur entprellen
.,EAB1 D0 F8    BNE $EAAB       noch nicht entprellt ?
.,EAB3 4A       LSR             Bits nacheinander ins Carry
                                schieben
.,EAB4 B0 16    BCS $EACC       '1' gleich nicht gedrückt
.,EAB6 48       PHA             Bitstelung retten
.,EAB7 B1 F5    LDA ($F5),Y     ASCII-Kode aus Tabelle holen
.,EAB9 C9 05    CMP #$05        größer als 4, dann keine
                                Control-Taste
.,EABB B0 0C    BCS $EAC9       verzweige bei größer/gleich 5
.,EABD C9 03    CMP #$03        Kode für STOP-Taste ?
.,EABF F0 08    BEQ $EAC9       falls ja, dann verzweige
.,EAC1 0D 8D 02 ORA $028D       entsprechendes Flag für SHIFT
.,EAC4 8D 8D 02 STA $028D       COMMOD.-Taste oder CTRL
                                setzen
.,EAC7 10 02    BPL $EACB       unbedingter Sprung
.,EAC9 84 CB    STY $CB         Nummer der Taste merken
.,EACB 68       PLA             Akku holen
.,EACC C8       INY             Zähler für Taste erhöhen
.,EACD C0 41    CPY #$41        schon alle Tasten?
.,EACF B0 0B    BCS $EADC       wenn ja, verzweige
.,EAD1 CA       DEX             nächste Matrix-Spalte
.,EAD2 D0 DF    BNE $EAB3       unbedingter Sprung
.,EAD4 38       SEC             Carry setzen
.,EAD5 68       PLA             gespeicherte Bitfolge holen
.,EAD6 2A       ROL             verschieben und
.,EAD7 8D 00 DC STA $DC00       in Port A schreiben
.,EADA D0 CC    BNE $EAA8       unbedingter Sprung
.,EADC 68       PLA             Stapel normalisieren
.,EADD 6C 8F 02 JMP ($028F)     JMP $EB48 setzt Zeiger auf
                                Tabelle
.,EAE0 A4 CB    LDY $CB         Nummer der Taste
.,EAE2 B1 F5    LDA ($F5),Y     ASCII-Wert aus Tabelle
                                holen
.,EAE4 AA       TAX             Tastenwert retten
.,EAE5 C4 C5    CPY $C5         mit letzter Taste
                                vergleichen
.,EAE7 F0 07    BEQ $EAF0       verzweige wenn gleiche Taste
.,EAE9 A0 10    LDY #$10        Wert für Repeatverzögerung
.,EAEB 8C 8C 02 STY $028C       in Repeat-Verzögerungszähler
.,EAEE D0 36    BNE $EB26       unbedingter Sprung
.,EAF0 29 7F    AND #$7F        Bit 7 löschen
.,EAF2 2C 8A 02 BIT $028A       Repeat-Funktion für alle
                                Tasten ?
.,EAF5 30 16    BMI $EB0D       Bit 7 gesetzt, dann alle
                                Tasten wiederholen
.,EAF7 70 49    BVS $EB42       Bit 6 gesetzt, dann
                                keine Wiederholung
.,EAF9 C9 7F    CMP #$7F        keine Taste?
.,EAFB F0 29    BEQ $EB26       ja, dann verzweige
.,EAFD C9 14    CMP #$14        'DEL', 'INST' Kode
.,EAFF F0 0C    BEQ $EB0D       wenn ja, verzweige
.,EB01 C9 20    CMP #$20        Leerzeichen
.,EB03 F0 08    BEQ $EB0D       wenn ja, verzweige
.,EB05 C9 1D    CMP #$1D        Cursor right, left
.,EB07 F0 04    BEQ $EB0D       wenn ja, verzweige
.,EB09 C9 11    CMP #$11        Cursor down, up
.,EB0B D0 35    BNE $EB42       verzweige wenn keine Taste
                                zu wiederholen ist
.,EB0D AC 8C 02 LDY $028C       Repeatverzögerungszähler
.,EB10 F0 05    BEQ $EB17       wenn abgelaufen, so verzweige
.,EB12 CE 8C 02 DEC $028C       herunterzählen
.,EB15 D0 2B    BNE $EB42       0? nein dann verzweige
.,EB17 CE 8B 02 DEC $028B       Repeatgeschwindigkeitszähler
.,EB1A D0 26    BNE $EB42       0? nein dann verzweige
.,EB1C A0 04    LDY #$04        Repeatgeschwindigkeits-
.,EB1E 8C 8B 02 STY $028B       zähler neu setzen
.,EB21 A4 C6    LDY $C6         Anzahl der Zeichen im
                                Tastaturpuffer
.,EB23 88       DEY             herunterzählen
.,EB24 10 1C    BPL $EB42       mehr als ein Zeichen im
                                Puffer, dann ignorieren
.,EB26 A4 CB    LDY $CB         Tastennummermatrixcode
.,EB28 84 C5    STY $C5         umspeichern
.,EB2A AC 8D 02 LDY $028D       sowie die Flags für SHIFT
.,EB2D 8C 8E 02 STY $028E       COMMOD.-Taste und CTRL
.,EB30 E0 FF    CPX #$FF        Tastatur-Kode ungültig ?
.,EB32 F0 0E    BEQ $EB42       ja, dann ignorieren
.,EB34 8A       TXA             gerettete Taste wieder holen
.,EB35 A6 C6    LDX $C6         Anzahl der Zeichen im
                                Tastaturpuffer
.,EB37 EC 89 02 CPX $0289       mit Haximalzahl vergleichen
.,EB3A B0 06    BCS $EB42       Puffer voll, dann Zeichen
                                ignorieren
.,EB3C 9D 77 02 STA $0277,X     Zeichen in Tastaturpuffer
                                schreiben
.,EB3F E8       INX             Zeichenanzahl erhöhen und
.,EB40 86 C6    STX $C6         abspeichern
.,EB42 A9 7F    LDA #$7F        Tastatur-Matrix Abfrage
.,EB44 8D 00 DC STA $DC00       auf Normalwert
.,EB47 60       RTS             Rücksprung

                                *** Prüft auf Shift, CTRL,
                                *** Commodore
.,EB48 AD 8D 02 LDA $028D       Flag für Shift/CTRL
.,EB4B C9 03    CMP #$03        SHIFT und COMMOD.-Taste
                                gedrückt?
.,EB4D D0 15    BNE $EB64       nein dann zum Dekodieren
.,EB4F CD 8E 02 CMP $028E       waren beide Tasten vorher
                                schon vorher gedrückt
.,EB52 F0 EE    BEQ $EB42       ja, dann zum Ende
.,EB54 AD 91 02 LDA $0291       Shift-Commodore erlaubt ?
.,EB57 30 1D    BMI $EB76       nein, zurück zur
                                Dekodierung
.,EB59 AD 18 D0 LDA $D018       Zeichensatzzeiger laden
.,EB5C 49 02    EOR #$02        Umschaltung Klein
                                -Großschreibung und
.,EB5E 8D 18 D0 STA $D018       wieder speichern
.,EB61 4C 76 EB JMP $EB76       fertig
.,EB64 0A       ASL             Wert mit 2 multiplizieren,
                                da jede Adresse 2 Bytes hat
.,EB65 C9 08    CMP #$08        vergleiche mit CTRL
.,EB67 90 02    BCC $EB6B       nein dann verzweige
.,EB69 A9 06    LDA #$06        Tabellenpointer für CTRL
.,EB6B AA       TAX             in X Register übertragen
.,EB6C BD 79 EB LDA $EB79,X     LOW-Byte der Tabellenadresse
                                laden
.,EB6F 85 F5    STA $F5         und in die Zeigeradresse
                                LOW schreiben
.,EB71 BD 7A EB LDA $EB7A,X     HIGH-Byte der Tabellenadresse
                                laden
.,EB74 85 F6    STA $F6         und in die Zeigeradresse
                                HIGH schreiben
.,EB76 4C E0 EA JMP $EAE0       zurück zur Dekodierung

                                *** Zeiger auf Tastatur-
                                *** Dekodiertabellen
.:EB79 81 EB C2 EB 03 EC 78 EC

                                *** Tastatur-Dekodiertabelle 1
                                *** ungeshifted
.:EB81 14 0D 1D 88 85 86 87 11
.:EB89 33 57 41 34 5A 53 45 01
.:EB91 35 52 44 36 43 46 54 58
.:EB99 37 59 47 38 42 48 55 56
.:EBA1 39 49 4A 30 4D 4B 4F 4E
.:EBA9 2B 50 4C 2D 2E 3A 40 2C
.:EBB1 5C 2A 3B 13 01 3D 5E 2F
.:EBB9 31 5F 04 32 20 02 51 03
.:EBC1 FF

                                *** Tastatur-Dekodierung,
                                *** Tabelle 2 geshifted
.:EBC2 94 8D 9D 8C 89 8A 8B 91
.:EBCA 23 D7 C1 24 DA D3 C5 01
.:EBD2 25 D2 C4 26 C3 C6 D4 D8
.:EBDA 27 D9 C7 28 C2 C8 D5 D6
.:EBE2 29 C9 CA 30 CD CB CF CE
.:EBEA DB D0 CC DD 3E 5B BA 3C
.:EBF2 A9 C0 5D 93 01 3D DE 3F
.:EBFA 21 5F 04 22 A0 02 D1 83
.:EC02 FF

                                *** Tastatur-Dekodierung,
                                *** Tabelle 3, mit 'C='-Taste
.:EC03 94 8D 9D 8C 89 8A 8B 91
.:EC0B 96 B3 B0 97 AD AE B1 01
.:EC13 98 B2 AC 99 BC BB A3 BD
.:EC1B 9A B7 A5 9B BF B4 B8 BE
.:EC23 29 A2 B5 30 A7 A1 B9 AA
.:EC2B A6 AF B6 DC 3E 5B A4 3C
.:EC33 A8 DF 5D 93 01 3D DE 3F
.:EC3B 81 5F 04 95 A0 02 AB 83
.:EC43 FF

                                *** prüft auf Steuerzeichen
.,EC44 C9 0E    CMP #$0E        chr$(14) Großschrift
.,EC46 D0 07    BNE $EC4F       verzweige wenn nein
.,EC48 AD 18 D0 LDA $D018       Character-Generator
.,EC4B 09 02    ORA #$02        auf Großschrift-Modus
.,EC4D D0 09    BNE $EC58       unbedingter Sprung
.,EC4F C9 8E    CMP #$8E        chr$(142) Kleinschrift
.,EC51 D0 0B    BNE $EC5E       verzweige wenn nein
.,EC53 AD 18 D0 LDA $D018       Character-Generator
.,EC56 29 FD    AND #$FD        Kleinschrift-Modus
.,EC58 8D 18 D0 STA $D018       setzen
.,EC5B 4C A8 E6 JMP $E6A8       Ausgabe abschließen
.,EC5E C9 08    CMP #$08        chr$(8) Code zur Blockierung
                                SHIFT und COMMOD.-Taste
.,EC60 D0 07    BNE $EC69       verzweige wenn nein
.,EC62 A9 80    LDA #$80        oberstes Bit des
.,EC64 0D 91 02 ORA $0291       Shift-Commodore Flags setzen
.,EC67 30 09    BMI $EC72       unbedingter Sprung
.,EC69 C9 09    CMP #$09        chr$(9) Code zur Freigabe von
                                SHIFT und COMMOD.-Taste
.,EC6B D0 EE    BNE $EC5B       verzweige wenn nein
.,EC6D A9 7F    LDA #$7F        oberstes Bit des
.,EC6F 2D 91 02 AND $0291       Shift-Commodore Flags löschen
.,EC72 8D 91 02 STA $0291       Wert speichern
.,EC75 4C A8 E6 JMP $E6A8       Ausgabe abschließen

                                *** Tastaturdekodierung,
                                *** Tabelle 4, mit CTRL-Taste
.:EC78 FF FF FF FF FF FF FF FF
.:EC80 1C 17 01 9F 1A 13 05 FF
.:EC88 9C 12 04 1E 03 06 14 18
.:EC90 1F 19 07 9E 02 08 15 16
.:EC98 12 09 0A 92 0D 0B 0F 0E
.:ECA0 FF 10 0C FF FF 1B 00 FF
.:ECA8 1C FF 1D FF FF 1F 1E FF
.:ECB0 90 06 FF 05 FF FF 11 FF
.:ECB8 FF

                                *** Konstanten für
                                *** Videocontroller
.:ECB9 00 00 00 00 00 00 00 00
.:ECC1 00 00 00 00 00 00 00 00
.:ECC9 00 9B 37 00 00 00 08 00
.:ECD1 14 0F 00 00 00 00 00 00
.:ECD9 0E 06 01 02 03 04 00 01
.:ECE1 02 03 04 05 06 07

                                *** Text nach Drücken von SHIFT
                                *** RUN/STOP
.:ECE7 4C 4F 41 44 0D 52 55 4E  'load (cr) run (cr)'
.:ECEA 44 0D 52 55 4E 0D

                                *** Tabelle der LSB der
                                *** Bildschirmzeilen-Anfänge
.:ECF0 00 28 50 78 A0 C8 F0 18
.:ECF8 40 68 90 B8 E0 08 30 58
.:ED00 80 A8 D0 F8 20 48 70 98
.:ED08 C0

                                *** IEC-Bus Routinen

                                *** TALK senden
.,ED09 09 40    ORA #$40        Bit für Talk setzen
.:ED0B 2C       .BYTE $2C       Skip nach $ED0E

                                *** LISTEN senden
.,ED0C 09 20    ORA #$20        Bit für Listen setzen
.,ED0E 20 A4 F0 JSR $F0A4       Ende der RS 232 Übertragung
                                abwarten
.,ED11 48       PHA             Akku merken
.,ED12 24 94    BIT $94         Noch Zeichen im Puffer ?
.,ED14 10 0A    BPL $ED20       verzweige wenn nein
.,ED16 38       SEC             Carry setzen
.,ED17 66 A3    ROR $A3         Bit für EOI setzen
.,ED19 20 40 ED JSR $ED40       Byte auf IEC-Bus ausgeben
.,ED1C 46 94    LSR $94         Flag für Zeichen im Puffer
                                löschen
.,ED1E 46 A3    LSR $A3         Flag für EOI löschen
.,ED20 68       PLA             Akku wiederholen und
.,ED21 85 95    STA $95         im Puffer speichern
.,ED23 78       SEI             Interruptflag setzen
.,ED24 20 97 EE JSR $EE97       DATA auf LOW setzen
.,ED27 C9 3F    CMP #$3F        Akku kann nicht $3F sein
.,ED29 D0 03    BNE $ED2E       unbedingter Sprung
.,ED2B 20 85 EE JSR $EE85       CLOCK auf LOW setzen
.,ED2E AD 00 DD LDA $DD00       Port A laden
.,ED31 09 08    ORA #$08        ATN HIGH setzen und
.,ED33 8D 00 DD STA $DD00       ausgeben
.,ED36 78       SEI             InterruptfLag setzen
.,ED37 20 8E EE JSR $EE8E       CLOCK auf HIGH setzen
.,ED3A 20 97 EE JSR $EE97       DATA auf LOW setzen
.,ED3D 20 B3 EE JSR $EEB3       eine Millisekunde warten

                                *** ein Byte auf IEC-Bus
                                *** ausgeben
.,ED40 78       SEI             Interruptflag setzen
.,ED41 20 97 EE JSR $EE97       DATA auf LOW setzen
.,ED44 20 A9 EE JSR $EEA9       Hardware-Rückmeldung aus
                                DATA holen
.,ED47 B0 64    BCS $EDAD       DATA LOW, dann 'DEVICE NOT
                                PRESENT'
.,ED49 20 85 EE JSR $EE85       CLOCK auf LOW setzen
.,ED4C 24 A3    BIT $A3         Bit für EOI gesetzt?
.,ED4E 10 0A    BPL $ED5A       nein, dann verzweige
.,ED50 20 A9 EE JSR $EEA9       DATA ins Carry
.,ED53 90 FB    BCC $ED50       warten bis Listener bereit
.,ED55 20 A9 EE JSR $EEA9       DATA ins Carry
.,ED58 B0 FB    BCS $ED55       warten auf DATA HIGH
.,ED5A 20 A9 EE JSR $EEA9       DATA ins Carry
.,ED5D 90 FB    BCC $ED5A       warten bis bereit für Daten
.,ED5F 20 8E EE JSR $EE8E       CLOCK auf HIGH setzen
.,ED62 A9 08    LDA #$08        Bitzähler für serielle
.,ED64 85 A5    STA $A5         Ausgabe setzen ($08 Bits)
.,ED66 AD 00 DD LDA $DD00       Port A lesen
.,ED69 CD 00 DD CMP $DD00       und entprellen
.,ED6C D0 F8    BNE $ED66       verzweige wenn Änderung
.,ED6E 0A       ASL             Datenbit ins Carry
.,ED6F 90 3F    BCC $EDB0       DATA HIGH, dann 'TIME OUT'
.,ED71 66 95    ROR $95         nächstes Bit zur Ausgabe
                                bereitstellen
.,ED73 B0 05    BCS $ED7A       verzweige wenn Bit gesetzt
.,ED75 20 A0 EE JSR $EEA0       DATA auf HIGH setzen
.,ED78 D0 03    BNE $ED7D       unbedingter Sprung
.,ED7A 20 97 EE JSR $EE97       DATA auf LOW setzen
.,ED7D 20 85 EE JSR $EE85       CLOCK auf LOW setzen
.,ED80 EA       NOP             Listener
.,ED81 EA       NOP             8 Microsekunden Zeit zur
.,ED82 EA       NOP             Verarbeitung der
.,ED83 EA       NOP             Daten geben
.,ED84 AD 00 DD LDA $DD00       Port A laden
.,ED87 29 DF    AND #$DF        DATA auf LOW
.,ED89 09 10    ORA #$10        und CLOCK auf HIGH
.,ED8B 8D 00 DD STA $DD00       setzen
.,ED8E C6 A5    DEC $A5         nächstes Bit
.,ED90 D0 D4    BNE $ED66       mache weiter wenn noch nicht
                                alle Bits gesendet
.,ED92 A9 04    LDA #$04        $04 als Timerwert setzen
.,ED94 8D 07 DC STA $DC07       Timer B HIGH, ca. eine ms
.,ED97 A9 19    LDA #$19        und Timer B
.,ED99 8D 0F DC STA $DC0F       starten
.,ED9C AD 0D DC LDA $DC0D       Interrupt control register
.,ED9F AD 0D DC LDA $DC0D       laden
.,EDA2 29 02    AND #$02        Timer B abgelaufen ?
.,EDA4 D0 0A    BNE $EDB0       ja, dann 'TIME OUT'
.,EDA6 20 A9 EE JSR $EEA9       DATA ins Carry
.,EDA9 B0 F4    BCS $ED9F       warten auf DATA HIGH
.,EDAB 58       CLI             Interruptflag löschen
.,EDAC 60       RTS             Rücksprung
.,EDAD A9 80    LDA #$80        'DEVICE NOT PRESENT'
.:EDAF 2C       .BYTE $2C       Skip nach $EDB2
.,EDB0 A9 03    LDA #$03        'TIME OUT'
.,EDB2 20 1C FE JSR $FE1C       Status setzen
.,EDB5 58       CLI             Interruptflag löschen
.,EDB6 18       CLC             Carry setzen
.,EDB7 90 4A    BCC $EE03       unbedingter Sprung

                                *** Sekundäradresse nach LISTEN
                                *** senden
.,EDB9 85 95    STA $95         Sekundäradresse speichern
.,EDBB 20 36 ED JSR $ED36       mit ATN HIGH ausgeben
.,EDBE AD 00 DD LDA $DD00       Port A laden
.,EDC1 29 F7    AND #$F7        ATN rücksetzen, LOW
.,EDC3 8D 00 DD STA $DD00       und ausgeben
.,EDC6 60       RTS             Rücksprung

                                *** Sekundäradresse nach TALK
                                *** ausgeben
.,EDC7 85 95    STA $95         Sekundäradresse speichern
.,EDC9 20 36 ED JSR $ED36       mit ATN ausgeben
.,EDCC 78       SEI             Interruptflag setzen
.,EDCD 20 A0 EE JSR $EEA0       DATA auf HIGH setzen
.,EDD0 20 BE ED JSR $EDBE       ATN rücksetzen, LOW
.,EDD3 20 85 EE JSR $EE85       CLOCK auf LOW setzen
.,EDD6 20 A9 EE JSR $EEA9       CLOCK-IN holen
.,EDD9 30 FB    BMI $EDD6       auf CLOCK HIGH warten
.,EDDB 58       CLI             Interruptflag löschen
.,EDDC 60       RTS             Rücksprung

                                *** IECOUT ein Byte auf IEC-Bus
                                *** ausgeben
.,EDDD 24 94    BIT $94         noch ein Byte auszugeben ?
.,EDDF 30 05    BMI $EDE6       verzweige wenn ja
.,EDE1 38       SEC             Carry setzen
.,EDE2 66 94    ROR $94         Flag für gepuffertes Byte
                                setzen
.,EDE4 D0 05    BNE $EDEB       unbedingter Sprung
.,EDE6 48       PHA             Byte merken
.,EDE7 20 40 ED JSR $ED40       gepuffertes Byte auf Bus
                                ausgeben
.,EDEA 68       PLA             Byte zurückholen und
.,EDEB 85 95    STA $95         in Ausgaberegister holen
.,EDED 18       CLC             Carry löschen
.,EDEE 60       RTS             Rücksprung

                                *** UNTALK senden
.,EDEF 78       SEI             Interruptflag setzen
.,EDF0 20 8E EE JSR $EE8E       CLOCK auf HIGH setzen
.,EDF3 AD 00 DD LDA $DD00       Poar A laden
.,EDF6 09 08    ORA #$08        ATN HIGH setzen und
.,EDF8 8D 00 DD STA $DD00       ausgeben
.,EDFB A9 5F    LDA #$5F        Kennzeichnung für UNTALK
.:EDFD 2C       .BYTE $2C       Skip nach $EE00

                                *** UNLISTEN senden
.,EDFE A9 3F    LDA #$3F        Kennzeichnung für UNLISTEN
.,EE00 20 11 ED JSR $ED11       ausgeben
.,EE03 20 BE ED JSR $EDBE       ATN rücksetzen, LOW
.,EE06 8A       TXA             X-Register merken
.,EE07 A2 0A    LDX #$0A        Warteschleife von
.,EE09 CA       DEX             ca. 40 Mikrosekunden
.,EE0A D0 FD    BNE $EE09       abwarten
.,EE0C AA       TAX             X-Register wiederholen
.,EE0D 20 85 EE JSR $EE85       CLOCK auf LOW setzen
.,EE10 4C 97 EE JMP $EE97       DATA auf LOW setzen

                                *** IECIN ein Zeichen vom
                                *** IEC-Bus holen
.,EE13 78       SEI             Interruptflag setzen
.,EE14 A9 00    LDA #$00        $00 laden
.,EE16 85 A5    STA $A5         und Zähler löschen
.,EE18 20 85 EE JSR $EE85       CLOCK auf LOW setzen
.,EE1B 20 A9 EE JSR $EEA9       CLOCK-IN LOW ?
.,EE1E 10 FB    BPL $EE1B       nein, dann warten
.,EE20 A9 01    LDA #$01        $01
.,EE22 8D 07 DC STA $DC07       in Timer B HIGH schreiben
.,EE25 A9 19    LDA #$19        Timer
.,EE27 8D 0F DC STA $DC0F       starten
.,EE2A 20 97 EE JSR $EE97       DATA auf LOW setzen
.,EE2D AD 0D DC LDA $DC0D       Interrupt Control Register
.,EE30 AD 0D DC LDA $DC0D       laden
.,EE33 29 02    AND #$02        Timer B abgelaufen ?
.,EE35 D0 07    BNE $EE3E       ja, 'TIME OUT'
.,EE37 20 A9 EE JSR $EEA9       CLOCK-IN HIGH ?
.,EE3A 30 F4    BMI $EE30       nein, dann warten
.,EE3C 10 18    BPL $EE56       unbedingter Sprung
.,EE3E A5 A5    LDA $A5         lade Zähler
.,EE40 F0 05    BEQ $EE47       verzweige wenn $00
.,EE42 A9 02    LDA #$02        'TIME OUT'
.,EE44 4C B2 ED JMP $EDB2       Status setzen
.,EE47 20 A0 EE JSR $EEA0       DATA auf HIGH setzen
.,EE4A 20 85 EE JSR $EE85       CLOCK auf LOW setzen
.,EE4D A9 40    LDA #$40        Bit 6 für 'END OR IDENTIFY'
.,EE4F 20 1C FE JSR $FE1C       Status setzen
.,EE52 E6 A5    INC $A5         Zähler erhöhen
.,EE54 D0 CA    BNE $EE20       unbedingter Sprung
.,EE56 A9 08    LDA #$08        $08 als
.,EE58 85 A5    STA $A5         Bitzähler setzen
.,EE5A AD 00 DD LDA $DD00       Port A laden
.,EE5D CD 00 DD CMP $DD00       Änderung ?
.,EE60 D0 F8    BNE $EE5A       verzweige wenn ja
.,EE62 0A       ASL             Datenbit ins Carry schieben
.,EE63 10 F5    BPL $EE5A       erneut holen wenn CLOCK = 1
.,EE65 66 A4    ROR $A4         Datenbit in $A4 schieben
.,EE67 AD 00 DD LDA $DD00       Port A laden
.,EE6A CD 00 DD CMP $DD00       Änderung ?
.,EE6D D0 F8    BNE $EE67       verzweige wenn ja
.,EE6F 0A       ASL             Datenbit ins Carry schieben
.,EE70 30 F5    BMI $EE67       erneut wenn CLOCK = 0
.,EE72 C6 A5    DEC $A5         Bitzähler veringerrn
.,EE74 D0 E4    BNE $EE5A       verzweige wenn noch nicht
                                alle 8 Bits gesendet
.,EE76 20 A0 EE JSR $EEA0       DATA auf HIGH setzen
.,EE79 24 90    BIT $90         Status
.,EE7B 50 03    BVC $EE80       verzweige wenn kein 'EOI' ?
.,EE7D 20 06 EE JSR $EE06       warten und Bits 101 senden
.,EE80 A5 A4    LDA $A4         Datenbyte in Akku holen
.,EE82 58       CLI             Interruptflag löschen
.,EE83 18       CLC             Carry löschen
.,EE84 60       RTS             Rücksprung

                                *** CLOCK auf LOW setzen
.,EE85 AD 00 DD LDA $DD00       Port A laden
.,EE88 29 EF    AND #$EF        Bit 4 löschen
.,EE8A 8D 00 DD STA $DD00       und wieder speichern
.,EE8D 60       RTS             Rücksprung

                                *** CLOCK auf HIGH setzen
.,EE8E AD 00 DD LDA $DD00       Port A laden
.,EE91 09 10    ORA #$10        Bit 4 setzen
.,EE93 8D 00 DD STA $DD00       und wieder speichern
.,EE96 60       RTS             Rücksprung

                                *** DATA auf LOW setzen
.,EE97 AD 00 DD LDA $DD00       Port A laden
.,EE9A 29 DF    AND #$DF        Bit 5 löschen
.,EE9C 8D 00 DD STA $DD00       und wieder speichern
.,EE9F 60       RTS             Rücksprung

                                *** DATA auf HIGH setzen
.,EEA0 AD 00 DD LDA $DD00       Port A laden
.,EEA3 09 20    ORA #$20        Bit 5 setzen
.,EEA5 8D 00 DD STA $DD00       und wieder speichern
.,EEA8 60       RTS             Rücksprung

                                *** Bit vom IEC-Bus ins
                                *** Carry-Flag holen
.,EEA9 AD 00 DD LDA $DD00       Port A laden
.,EEAC CD 00 DD CMP $DD00       Änderung ?
.,EEAF D0 F8    BNE $EEA9       verzweige wenn ja
.,EEB1 0A       ASL             Datenbit ins Carry schieben
.,EEB2 60       RTS             Rücksprung

                                *** Verzögerung 1 Millisekunde
.,EEB3 8A       TXA             X-Register retten
.,EEB4 A2 B8    LDX #$B8        X-Register mit $B8 laden
.,EEB6 CA       DEX             herunterzählen
.,EEB7 D0 FD    BNE $EEB6       verzweige wenn nicht fertig
.,EEB9 AA       TAX             X-Register wiederherstellen
.,EEBA 60       RTS             Rücksprung

                                *** RS 232 Ausgabe
.,EEBB A5 B4    LDA $B4         Anzahl Bits zu senden
.,EEBD F0 47    BEQ $EF06       verzweige wenn Byte schon
                                komplett übertragen
.,EEBF 30 3F    BMI $EF00       verzweige falls Stopbit
                                erforderlich
.,EEC1 46 B6    LSR $B6         nächstes Bit ins Carry
                                schieben
.,EEC3 A2 00    LDX #$00        '0' falls Datenbit = 0
.,EEC5 90 01    BCC $EEC8       verzweige wenn Datenbit
                                gelöscht
.,EEC7 CA       DEX             nein, dann X-Register =$FF
.,EEC8 8A       TXA             X-Register in Akku
.,EEC9 45 BD    EOR $BD         mit Register für Paritybit
                                verknüpfen
.,EECB 85 BD    STA $BD         und abspeichern
.,EECD C6 B4    DEC $B4         Bitzähler erniedrigen
.,EECF F0 06    BEQ $EED7       verzweige wenn alle Bits
                                übertragen
.,EED1 8A       TXA             alten Akku wiederherstellen
.,EED2 29 04    AND #$04        Bit 2 isolieren
.,EED4 85 B5    STA $B5         und ins Ausgaberegister
                                bringen
.,EED6 60       RTS             Rücksprung
.,EED7 A9 20    LDA #$20        Bit 5 (Parity)
.,EED9 2C 94 02 BIT $0294       RS 232 Befehlsregister
                                abfragen
.,EEDC F0 14    BEQ $EEF2       verzweige wenn ohne Parity
.,EEDE 30 1C    BMI $EEFC       verzweige wenn feste Parität
.,EEE0 70 14    BVS $EEF6       verzweige wenn ungerade
                                Parität
.,EEE2 A5 BD    LDA $BD         verzweige wenn Parity
                                gleich eins
.,EEE4 D0 01    BNE $EEE7       verzweige wenn ja
.,EEE6 CA       DEX             Parity $FF
.,EEE7 C6 B4    DEC $B4         Bitzähler auf $FF
.,EEE9 AD 93 02 LDA $0293       RS 232 Kontrollregister laden
.,EEEC 10 E3    BPL $EED1       verzweige wenn zwei Stopbits
.,EEEE C6 B4    DEC $B4         Bitzähler auf $FE
.,EEF0 D0 DF    BNE $EED1       unbedingter Sprung zur
                                Berechnung der Stopbits
.,EEF2 E6 B4    INC $B4         Bitzähler erhöhen, keine
                                Parity
.,EEF4 D0 F0    BNE $EEE6       unbedingter Sprung zur
                                Berechnung der Stopbits
.,EEF6 A5 BD    LDA $BD         Parity
.,EEF8 F0 ED    BEQ $EEE7       verzweige wenn gleich 0,
                                dann Null-Bit ausgeben
.,EEFA D0 EA    BNE $EEE6       unbedingter Sprung 1-Bit
                                ausgeben
.,EEFC 70 E9    BVS $EEE7       Null-Bit ausgeben
.,EEFE 50 E6    BVC $EEE6       sonst 1-Bit ausgeben (feste
                                Parität)
.,EF00 E6 B4    INC $B4         Bitzähler erhöhen
.,EF02 A2 FF    LDX #$FF        Wert für Stopbit
.,EF04 D0 CB    BNE $EED1       unbedingter Sprung
.,EF06 AD 94 02 LDA $0294       RS 232 Befehlsregister laden
.,EF09 4A       LSR             Bit 0 ins Carry
.,EF0A 90 07    BCC $EF13       verzweige wenn 3-Line
                                Handshake, Abfrage übergehen
.,EF0C 2C 01 DD BIT $DD01       Port B abfragen
.,EF0F 10 1D    BPL $EF2E       verzweige wenn DSR fehlt
.,EF11 50 1E    BVC $EF31       verzweige wenn CTS fehlt
.,EF13 A9 00    LDA #$00        0 laden und
.,EF15 85 BD    STA $BD         Parity-Register löschen
.,EF17 85 B5    STA $B5         Register für zu sendendes
                                Bit (Startbit)
.,EF19 AE 98 02 LDX $0298       Anzahl der zu übertragenden
                                Bits
.,EF1C 86 B4    STX $B4         als Bitzähler merken
.,EF1E AC 9D 02 LDY $029D       lade Zeiger für übertragenes
                                Byte
.,EF21 CC 9E 02 CPY $029E       alle Bytes übertragen ?
.,EF24 F0 13    BEQ $EF39       ja, dann abschließen
.,EF26 B1 F9    LDA ($F9),Y     Datenbyte aus RS 232 Puffer
                                holen
.,EF28 85 B6    STA $B6         zum Senden übergeben
.,EF2A EE 9D 02 INC $029D       Pufferzeiger erhöhen
.,EF2D 60       RTS             Rücksprung
.,EF2E A9 40    LDA #$40        DSR (Data Set Ready) fehlt
.:EF30 2C       .BYTE $2C       Skip nach $EF33
.,EF31 A9 10    LDA #$10        CTS (Clear To Send) fehlt
.,EF33 0D 97 02 ORA $0297       mit Status verknüpfen
.,EF36 8D 97 02 STA $0297       und setzen
.,EF39 A9 01    LDA #$01        NMI für
.,EF3B 8D 0D DD STA $DD0D       Timer A löschen
.,EF3E 4D A1 02 EOR $02A1       Flag für
.,EF41 09 80    ORA #$80        RS 232 umdrehen
.,EF43 8D A1 02 STA $02A1       und speichern
.,EF46 8D 0D DD STA $DD0D       IRR setzen, alle übrigen
                                zulassen NMIs
.,EF49 60       RTS             Rücksprung

                                *** Anzahl der RS 232 Datenbits
                                *** berechnen
.,EF4A A2 09    LDX #$09        Zähler für Wortlänge
.,EF4C A9 20    LDA #$20        Maskenwert für Bit 5
.,EF4E 2C 93 02 BIT $0293       Testen vom RS-232
                                Kontrollregister
.,EF51 F0 01    BEQ $EF54       verzweige wenn Bit 5 gelöscht
.,EF53 CA       DEX             Zähler für Wortlänge
                                vermindern
.,EF54 50 02    BVC $EF58       verzweige wenn Bit 6 gelöscht
.,EF56 CA       DEX             Wortlänge um zwei
.,EF57 CA       DEX             vermindern
.,EF58 60       RTS             Rücksprung

                                *** empfangenes Bit verarbeiten
.,EF59 A6 A9    LDX $A9         Startbit ?
.,EF5B D0 33    BNE $EF90       verzweige wenn ja
.,EF5D C6 A8    DEC $A8         Bitzähler erniedrigen
.,EF5F F0 36    BEQ $EF97       verzweige wenn alle Bits
                                empfangen
.,EF61 30 0D    BMI $EF70       verzweige wenn noch Stopbits
                                zu erwarten
.,EF63 A5 A7    LDA $A7         empfangenes Bit
.,EF65 45 AB    EOR $AB         mit Register für Parity
                                verknüpfen
.,EF67 85 AB    STA $AB         und abspeichern
.,EF69 46 A7    LSR $A7         empfangenes Bit ins Carry
.,EF6B 66 AA    ROR $AA         und in Empfangsregister
                                schieben
.,EF6D 60       RTS             Rücksprung
.,EF6E C6 A8    DEC $A8         Bitzähler erniedrigen
.,EF70 A5 A7    LDA $A7         Stopbit
.,EF72 F0 67    BEQ $EFDB       verzweige wenn gleich Null
.,EF74 AD 93 02 LDA $0293       Kontrollregister laden
.,EF77 0A       ASL             Bit 7 (Anzahl Stopbits) ins
                                Carry
.,EF78 A9 01    LDA #$01        1 laden und mit der Anzahl
.,EF7A 65 A8    ADC $A8         von Bits und Stopbits
                                addieren
.,EF7C D0 EF    BNE $EF6D       verzweige wenn noch nicht
                                alle Stopbits empfangen
.,EF7E A9 90    LDA #$90        Wert für Freigabe von NMI
                                über die Flagleitung
.,EF80 8D 0D DD STA $DD0D       Wert NMI freigeben
.,EF83 0D A1 02 ORA $02A1       auch im NMI Register
.,EF86 8D A1 02 STA $02A1       für RS 232 NMIs vermerken
.,EF89 85 A9    STA $A9         und Flag für Startbit setzen
.,EF8B A9 02    LDA #$02        Bitwert für
.,EF8D 4C 3B EF JMP $EF3B       NMI für Timer B löschen
.,EF90 A5 A7    LDA $A7         Startbit laden
.,EF92 D0 EA    BNE $EF7E       verzweige wenn ungleich Null
.,EF94 85 A9    STA $A9         Flag für Startbit
                                rücksetzen
.,EF96 60       RTS             Rücksprung

                                *** Empfangenes Byte
                                *** weiterverarbeiten
.,EF97 AC 9B 02 LDY $029B       Pufferzeiger laden
.,EF9A C8       INY             und erhöhen
.,EF9B CC 9C 02 CPY $029C       mit Empfangspuffer
                                vergleichen
.,EF9E F0 2A    BEQ $EFCA       verzweige wenn voll, dann
                                Status setzen
.,EFA0 8C 9B 02 STY $029B       Pufferzeiger abspeichern
.,EFA3 88       DEY             und normalisieren
.,EFA4 A5 AA    LDA $AA         empfangenes Byte laden
.,EFA6 AE 98 02 LDX $0298       Anzahl Datenbits laden
.,EFA9 E0 09    CPX #$09        8 Bits plus ein Stopbit?
.,EFAB F0 04    BEQ $EFB1       verzweige wenn ja, ok
.,EFAD 4A       LSR             sonst Bits in richtige
                                Position schieben
.,EFAE E8       INX             Datenbitzähler um 1 erhöhen
.,EFAF D0 F8    BNE $EFA9       unbedingter Sprung
.,EFB1 91 F7    STA ($F7),Y     Byte in RS 232 Puffer
                                schreiben
.,EFB3 A9 20    LDA #$20        Maskenwert für
                                Paritätsprüfung
.,EFB5 2C 94 02 BIT $0294       Bit 5 im Kommandregister
                                prüfen
.,EFB8 F0 B4    BEQ $EF6E       verzweige wenn Übertragung
                                ohne Parity
.,EFBA 30 B1    BMI $EF6D       verzweige wenn festes Bit
                                anstelle Parity
.,EFBC A5 A7    LDA $A7         empfangenes Paritybit laden
.,EFBE 45 AB    EOR $AB         mit berechneter Parity
                                vergleichen
.,EFC0 F0 03    BEQ $EFC5       verzweige wenn gleich, ok
.,EFC2 70 A9    BVS $EF6D       gerade Parity, dann ok
.:EFC4 2C       .BYTE $2C       Skip nach $EFC7
.,EFC5 50 A6    BVC $EF6D       verzweige wenn ungerade
                                Parity, dann ok
.,EFC7 A9 01    LDA #$01        sonst Parity-Fehler
.:EFC9 2C       .BYTE $2C       Skip nach EFCC
.,EFCA A9 04    LDA #$04        Empfängerpuffer voll
.:EFCC 2C       .BYTE $2C       Skip nach $EFCF
.,EFCD A9 80    LDA #$80        Break-Befehl empfangen
.:EFCF 2C       .BYTE $2C       Skip nach $EFD2
.,EFD0 A9 02    LDA #$02        Rahmen-Fehler
.,EFD2 0D 97 02 ORA $0297       mit Code für RS-232 Status
                                verknüpfen
.,EFD5 8D 97 02 STA $0297       und speichern
.,EFD8 4C 7E EF JMP $EF7E       zum Empfang des nächsten
                                Bytes springen
.,EFDB A5 AA    LDA $AA         empfangenes Byte
.,EFDD D0 F1    BNE $EFD0       ungleich 0, dann zu Rahmen-
                                Fehler
.,EFDF F0 EC    BEQ $EFCD       sonst zu Break-Befehl
                                empfangen

                                *** RS-232 CKOUT, Ausgabe auf
                                *** RS-232
.,EFE1 85 9A    STA $9A         Gerätenummer abspeichern
.,EFE3 AD 94 02 LDA $0294       RS 232 Kommandregister laden
.,EFE6 4A       LSR             Bit 0 (Handshake) ins Carry
.,EFE7 90 29    BCC $F012       verzweige wenn 3-Line-
                                Handshake
.,EFE9 A9 02    LDA #$02        Haske für DATA SET READY
.,EFEB 2C 01 DD BIT $DD01       Port B auslesen
.,EFEE 10 1D    BPL $F00D       kein DSR, dann Fehler
.,EFF0 D0 20    BNE $F012       verzweige wenn kein Request
                                To Send
.,EFF2 AD A1 02 LDA $02A1       RS-232 NMI Status Laden
.,EFF5 29 02    AND #$02        verknüpfe mit Bit für
                                Datenempfang aktiv
.,EFF7 D0 F9    BNE $EFF2       warten bis Empfang beendet
.,EFF9 2C 01 DD BIT $DD01       Port B der NMI-CIA auslesen
.,EFFC 70 FB    BVS $EFF9       und auf Clear To Send warten
.,EFFE AD 01 DD LDA $DD01       Port B lesen
.,F001 09 02    ORA #$02        Bit für Request To Send setzen
.,F003 8D 01 DD STA $DD01       und wieder zurückschreiben
.,F006 2C 01 DD BIT $DD01       Port B holen und
.,F009 70 07    BVS $F012       auf Clear To Send warten
.,F00B 30 F9    BMI $F006       verzweige wenn nicht Data Set
                                Ready
.,F00D A9 40    LDA #$40        Bit für fehlendes DSR
.,F00F 8D 97 02 STA $0297       Status setzen
.,F012 18       CLC             Carry für ok Kennzeichen
                                setzen
.,F013 60       RTS             Rücksprung

                                *** Ausgabe in RS 232 Puffer
.,F014 20 28 F0 JSR $F028       falls erforderlich Übertragung starten
.,F017 AC 9E 02 LDY $029E       Zeiger auf Ausgabepuffer
                                laden
.,F01A C8       INY             und erhöhen
.,F01B CC 9D 02 CPY $029D       und mit Lesezeiger
                                vergleichen
.,F01E F0 F4    BEQ $F014       Puffer voll, dann warten
.,F020 8C 9E 02 STY $029E       neuen Wert für
                                Schreibzeiger merken
.,F023 88       DEY             und wieder normalisieren
.,F024 A5 9E    LDA $9E         auszugebendes Byte holen und
.,F026 91 F9    STA ($F9),Y     in Puffer schreiben
.,F028 AD A1 02 LDA $02A1       RS 232 NMI Status laden
.,F02B 4A       LSR             Bit 0 testen (läuft
                                Sendebetrieb)
.,F02C B0 1E    BCS $F04C       verzweige wenn ja
.,F02E A9 10    LDA #$10        Bitwert für Timer starten
.,F030 8D 0E DD STA $DD0E       Timer A starten
.,F033 AD 99 02 LDA $0299       Timer für
.,F036 8D 04 DD STA $DD04       Sende-Baud-Rate
.,F039 AD 9A 02 LDA $029A       neu
.,F03C 8D 05 DD STA $DD05       setzen
.,F03F A9 81    LDA #$81        Code für Timer-Unterlauf NMI
                                Timer A
.,F041 20 3B EF JSR $EF3B       in IC-Register schreiben
.,F044 20 06 EF JSR $EF06       CTS und DSR prüfen und
                                Übertragung freigeben
.,F047 A9 11    LDA #$11        Bitwert Timer A starten
.,F049 8D 0E DD STA $DD0E       Timer A starten
.,F04C 60       RTS             Rücksprung

                                *** RS-232 CHKIN, Eingabe auf
                                *** RS-232 setzen
.,F04D 85 99    STA $99         Gerätenummer speichern
.,F04F AD 94 02 LDA $0294       RS 232 Befehlsregister laden
.,F052 4A       LSR             Bit 0 ins Carry schieben
.,F053 90 28    BCC $F07D       verzweige wenn 3-Line-
                                Handshake
.,F055 29 08    AND #$08        Bit für Dupex Mode isolieren
.,F057 F0 24    BEQ $F07D       verzweige wenn voll Dupex
.,F059 A9 02    LDA #$02        Maske für 'RTS OUT'
.,F05B 2C 01 DD BIT $DD01       Data Set Ready abfragen
.,F05E 10 AD    BPL $F00D       verzweige wenn nein
.,F060 F0 22    BEQ $F084       Ready To Send abfragen
.,F062 AD A1 02 LDA $02A1       RS 232 NMI Status laden
.,F065 4A       LSR             Bit 0 ins Carry
                                (Sendebetrieb aktiv)
.,F066 B0 FA    BCS $F062       ja, warten bis beendet
.,F068 AD 01 DD LDA $DD01       Port B laden
.,F06B 29 FD    AND #$FD        Request To Send
.,F06D 8D 01 DD STA $DD01       und wieder speichern
.,F070 AD 01 DD LDA $DD01       Port B holen
.,F073 29 04    AND #$04        Bit für Data Terminal Ready
.,F075 F0 F9    BEQ $F070       verzweige wenn nein, warten
.,F077 A9 90    LDA #$90        NMI-Maske für 'Flag' laden
.,F079 18       CLC             Carry löschen (ok Kennzeichen)
.,F07A 4C 3B EF JMP $EF3B       NMI freigeben

                                *** RS-232 CHKIN bei 3-Line
                                *** Handshake
.,F07D AD A1 02 LDA $02A1       RS-232 NMI Status laden
.,F080 29 12    AND #$12        wenn RS-232 nicht aktiv
.,F082 F0 F3    BEQ $F077       dann starten
.,F084 18       CLC             Carry löschen (ok
                                Kenneichen)
.,F085 60       RTS             Rücksprung

                                *** GET von RS-232
.,F086 AD 97 02 LDA $0297       RS-232 Status holen
.,F089 AC 9C 02 LDY $029C       Zeiger auf Ende des
                                Eingabepuffers
.,F08C CC 9B 02 CPY $029B       mit Zeiger auf Anfang
                                vergleichen
.,F08F F0 0B    BEQ $F09C       verzweige wenn gleich (Puffer
                                leer)
.,F091 29 F7    AND #$F7        Bit 3 (Puffer leer)
.,F093 8D 97 02 STA $0297       im Status löschen (Zeichen
                                im Puffer)
.,F096 B1 F7    LDA ($F7),Y     Byte aus Puffer holen
.,F098 EE 9C 02 INC $029C       Pufferzeiger erhöhen
.,F09B 60       RTS             Rücksprung
.,F09C 09 08    ORA #$08        Bitwert für Puffer leer
.,F09E 8D 97 02 STA $0297       Status setzen
.,F0A1 A9 00    LDA #$00        Null übergeben
.,F0A3 60       RTS             Rücksprung

                                *** Ende der RS-232 Übertragung
                                *** abwarten
.,F0A4 48       PHA             Akku auf Stack retten
.,F0A5 AD A1 02 LDA $02A1       RS-232 NMI Status laden
.,F0A8 F0 11    BEQ $F0BB       nicht gesetzt, dann ok
.,F0AA AD A1 02 LDA $02A1       RS-232 NMI Status laden
.,F0AD 29 03    AND #$03        Bit 0 = senden und Bit 1 =
                                empfangen
.,F0AF D0 F9    BNE $F0AA       warten bis beide Bits
                                gelöscht
.,F0B1 A9 10    LDA #$10        Bitwert für Interrupt durch
.,F0B3 8D 0D DD STA $DD0D       'Flag'-Leitung setzen
.,F0B6 A9 00    LDA #$00        RS-232 NMI Status
.,F0B8 8D A1 02 STA $02A1       zurücksetzen
.,F0BB 68       PLA             Akku wieder holen
.,F0BC 60       RTS             Rücksprung

                                *** Systemmeldungen
.:F0BD 0D 49 2F 4F 20 45 52 52  I/O ERROR #
.:F0C6 52 20 A3 0D 53 45 41 52
.:F0C9 0D 53 45 41 52 43 48 49  SEARCHING
.:F0D1 4E 47 A0 46 4F 52 A0 0D
.:F0D4 46 4F 52 A0 0D 50 52 45  FOR
.:F0D8 0D 50 52 45 53 53 20 50  PRESS PLAY ON TAPE
.:F0E0 4C 41 59 20 4F 4E 20 54
.:F0E8 41 50 C5 50 52 45 53 53
.:F0EB 50 52 45 53 53 20 52 45  PRESS RECORD & PLAY ON TAPE
.:F0F3 43 4F 52 44 20 26 20 50
.:F0FB 4C 41 59 20 4F 4E 20 54
.:F103 41 50 C5 0D 4C 4F 41 44
.:F106 0D 4C 4F 41 44 49 4E C7  LOADING
.:F10E 0D 53 41 56 49 4E 47 A0  SAVING
.:F116 0D 56 45 52 49 46 59 49  VERIFYING
.:F11E 4E C7 0D 46 4F 55 4E 44
.:F120 0D 46 4F 55 4E 44 A0 0D  FOUND
.:F127 0D 4F 4B 8D              OK


                                *** Systemmeldungen ausgeben
.,F12B 24 9D    BIT $9D         Direkt-Modus Flag
.,F12D 10 0D    BPL $F13C       Programm, dann überspringen
.,F12F B9 BD F0 LDA $F0BD,Y     Zeichen holen mit Offset der
                                Meldung in Y-Register
.,F132 08       PHP             Status-Register retten
.,F133 29 7F    AND #$7F        Bit 7 löschen
.,F135 20 D2 FF JSR $FFD2       und Zeichen ausgeben
.,F138 C8       INY             Zeiger erhöhen
.,F139 28       PLP             Status wiederholen
.,F13A 10 F3    BPL $F12F       verzweige wenn noch weitere
                                Buchstaben
.,F13C 18       CLC             Carry löschen, ok
.,F13D 60       RTS             Rücksprung

                                *** GETIN
.,F13E A5 99    LDA $99         Eingabegerät laden
.,F140 D0 08    BNE $F14A       verzweige wenn nicht Tastatur
.,F142 A5 C6    LDA $C6         Anzahl der Zeichen im
                                Tastaturpuffer laden
.,F144 F0 0F    BEQ $F155       verzweige wenn kein Zeichen
.,F146 78       SEI             Interruptflag setzen
.,F147 4C B4 E5 JMP $E5B4       Zeichen aus Tastaturpuffer
                                holen
.,F14A C9 02    CMP #$02        Geräteadresse für RS-232
.,F14C D0 18    BNE $F166       nein dann zur BASIN-Routine
.,F14E 84 97    STY $97         Y-Register merken
.,F150 20 86 F0 JSR $F086       Get von RS 232
.,F153 A4 97    LDY $97         Y-Register wiederholen
.,F155 18       CLC             Carry löschen, ok
.,F156 60       RTS             Rücksprung

                                *** BASIN Eingabe eines
                                *** Zeichens
.,F157 A5 99    LDA $99         Gerätenummer laden
.,F159 D0 0B    BNE $F166       verzweige wenn nicht Tastatur
.,F15B A5 D3    LDA $D3         Cursorposition holen
.,F15D 85 CA    STA $CA         und für
.,F15F A5 D6    LDA $D6         Tastatureingabe
.,F161 85 C9    STA $C9         setzen
.,F163 4C 32 E6 JMP $E632       Eingabe vom Bildschirm
.,F166 C9 03    CMP #$03        Eingabekanal 3 = Bildschirm
.,F168 D0 09    BNE $F173       wenn nicht verzweige

                                *** vom Bildschirm
.,F16A 85 D0    STA $D0         Flag auf Eingabe von Bild-
                                schimrstelle
.,F16C A5 D5    LDA $D5         Cursorzeile laden
.,F16E 85 C8    STA $C8         als Pointer für Ende der
                                Zeile speichern
.,F170 4C 32 E6 JMP $E632       zu Eingabe vom Bildschirm
.,F173 B0 38    BCS $F1AD       verzweige zu Eingabe vom
                                IEC-Bus
.,F175 C9 02    CMP #$02        Eingabe von RS-232 ?
.,F177 F0 3F    BEQ $F1B8       ja, so verzweige

                                *** Eingabe vom Band
.,F179 86 97    STX $97         X-Register merken
.,F17B 20 99 F1 JSR $F199       ein Zeichen vom Band holen
.,F17E B0 16    BCS $F196       verzweige bei Fehler
.,F180 48       PHA             Akku retten
.,F181 20 99 F1 JSR $F199       ein Zeichen vom Band holen
.,F184 B0 0D    BCS $F193       verzweige bei Fehler
.,F186 D0 05    BNE $F18D       letzes Zeichen ?
.,F188 A9 40    LDA #$40        Code für 'End of Identify'
.,F18A 20 1C FE JSR $FE1C       Status setzen
.,F18D C6 A6    DEC $A6         Bandpuffer Zeiger erniedrigen
.,F18F A6 97    LDX $97         X-Register zurückholen
.,F191 68       PLA             geholtes Zeichen in Akku
.,F192 60       RTS             Rücksprung
.,F193 AA       TAX             Fehlernummer ins X-Register
.,F194 68       PLA             Stack normalisieren
.,F195 8A       TXA             Fehlernummer in Akku
.,F196 A6 97    LDX $97         X-Register zurückholen
.,F198 60       RTS             Rücksprung

                                *** ein Zeichen vom Band holen
.,F199 20 0D F8 JSR $F80D       Bandpuffer Zeiger erhöhen
.,F19C D0 0B    BNE $F1A9       verzweige wenn noch Zeichen
                                im Puffer
.,F19E 20 41 F8 JSR $F841       sonst nächsten Block vom
                                Band holen
.,F1A1 B0 11    BCS $F1B4       STOP-Taste, dann Abbruch
.,F1A3 A9 00    LDA #$00        Pufferzeiger
.,F1A5 85 A6    STA $A6         auf Null
.,F1A7 F0 F0    BEQ $F199       unbedingter Sprung
.,F1A9 B1 B2    LDA ($B2),Y     Zeichen aus Puffer lesen
.,F1AB 18       CLC             Carry =0 (ok Kennzeichen)
.,F1AC 60       RTS             Rücksprung

                                *** Eingabe vom IEC-Bus
.,F1AD A5 90    LDA $90         Status testen
.,F1AF F0 04    BEQ $F1B5       verzweige wenn ok
.,F1B1 A9 0D    LDA #$0D        'CR' Kode ausgeben
.,F1B3 18       CLC             Carry =0 (ok Kennzeichen)
.,F1B4 60       RTS             Rücksprung
.,F1B5 4C 13 EE JMP $EE13       ein Byte vom IEC-Bus holen

                                *** RS 232 Eingabe
.,F1B8 20 4E F1 JSR $F14E       ein Byte von RS 232 holen
.,F1BB B0 F7    BCS $F1B4       verzweige wenn Fehler
.,F1BD C9 00    CMP #$00        vergleiche mit Nullbyte
.,F1BF D0 F2    BNE $F1B3       nein, dann ok
.,F1C1 AD 97 02 LDA $0297       Status laden
.,F1C4 29 60    AND #$60        fehlt DSR ?
.,F1C6 D0 E9    BNE $F1B1       ja, 'CR' zurückgeben
.,F1C8 F0 EE    BEQ $F1B8       nein, neuer Versuch

                                *** BSOUT Ausgabe eines
                                *** Zeichens
.,F1CA 48       PHA             Datenbyte retten
.,F1CB A5 9A    LDA $9A         Gerätenummer für Ausgabe
.,F1CD C9 03    CMP #$03        vergleiche mit Bildschirm
.,F1CF D0 04    BNE $F1D5       verzweige wenn nein
.,F1D1 68       PLA             Datenbyte wiederholen
.,F1D2 4C 16 E7 JMP $E716       ein Zeichen auf Bildschirm
                                ausgeben
.,F1D5 90 04    BCC $F1DB       verzweige wenn keine Ausgabe
                                IEC-Bus

                                *** Ausgabe auf IEC-Bus
.,F1D7 68       PLA             Datenbyte retten
.,F1D8 4C DD ED JMP $EDDD       ein Byte auf IEC-Bus ausgeben
.,F1DB 4A       LSR             Bit 0 der Ausgabekanal-
                                Nummer ins Carry
.,F1DC 68       PLA             Datenbyte wiederholen
.,F1DD 85 9E    STA $9E         auszugebendes Zeichen merken
.,F1DF 8A       TXA             X-Register
.,F1E0 48       PHA             und Y-Register
.,F1E1 98       TYA             auf Stack
.,F1E2 48       PHA             retten
.,F1E3 90 23    BCC $F208       RS-232 Ausgabe

                                *** Ausgabe auf Band
.,F1E5 20 0D F8 JSR $F80D       Bandpuffer Zeiger erhöhen
.,F1E8 D0 0E    BNE $F1F8       verzweige wenn Puffer
                                nicht voll
.,F1EA 20 64 F8 JSR $F864       Puffer auf Band schreiben
.,F1ED B0 0E    BCS $F1FD       STOP-Taste, dann Abbruch
.,F1EF A9 02    LDA #$02        Kontrollbyte für Datenblock
.,F1F1 A0 00    LDY #$00        Pufferzeiger auf 0
.,F1F3 91 B2    STA ($B2),Y     Akku in Puffer schreiben
.,F1F5 C8       INY             Zeiger erhöhen
.,F1F6 84 A6    STY $A6         und merken
.,F1F8 A5 9E    LDA $9E         Datenbyte holen
.,F1FA 91 B2    STA ($B2),Y     Zeichen in Puffer schreiben
.,F1FC 18       CLC             Carry =0 (ok Kennzeichen)
.,F1FD 68       PLA             X-Register
.,F1FE A8       TAY             und Y-Register
.,F1FF 68       PLA             aus Stack
.,F200 AA       TAX             holen
.,F201 A5 9E    LDA $9E         Datenbyte zurückholen
.,F203 90 02    BCC $F207       verzweige wenn ok
.,F205 A9 00    LDA #$00        Flag für 'STOP-Taste
                                gedrückt'
.,F207 60       RTS             Rücksprung

                                *** RS-232 Ausgabe
.,F208 20 17 F0 JSR $F017       ein Zeichen in RS-232
                                Puffer schreiben
.,F20B 4C FC F1 JMP $F1FC       CHROUT

                                *** CHKIN Eingabegerät setzen
.,F20E 20 0F F3 JSR $F30F       sucht logische Filenummer
.,F211 F0 03    BEQ $F216       verzweige wenn gefunden
.,F213 4C 01 F7 JMP $F701       sonst 'file not open'
.,F216 20 1F F3 JSR $F31F       setzt Fileparameter
.,F219 A5 BA    LDA $BA         Gerätenummer laden
.,F21B F0 16    BEQ $F233       0, Tastatur
.,F21D C9 03    CMP #$03        vergleiche mit Bildschirm
.,F21F F0 12    BEQ $F233       verzweige zu Bildschirm
.,F221 B0 14    BCS $F237       verzweige zu IEC-Bus
.,F223 C9 02    CMP #$02        vergleiche mit RS-232
.,F225 D0 03    BNE $F22A       nein, dann Band
.,F227 4C 4D F0 JMP $F04D       ja, dann RS-232

                                *** Band als Eingabegerät setzen
.,F22A A6 B9    LDX $B9         Sekundäradresse laden
.,F22C E0 60    CPX #$60        vergleichemit 'Null'
.,F22E F0 03    BEQ $F233       verzweige wenn 'Null'
.,F230 4C 0A F7 JMP $F70A       sonst 'not input file'
.,F233 85 99    STA $99         Gerätenummer für Ausgabe
                                speichern
.,F235 18       CLC             Carry =0 (ok Kennzeichen)
.,F236 60       RTS             Rücksprung

                                *** IEC-Bus als Eingabegerät
.,F237 AA       TAX             Geräteadresse retten
.,F238 20 09 ED JSR $ED09       TALK senden
.,F23B A5 B9    LDA $B9         Sekundäradresse laden
.,F23D 10 06    BPL $F245       verzweige wenn kleiner 128
.,F23F 20 CC ED JSR $EDCC       wartet auf Takt-Signal
.,F242 4C 48 F2 JMP $F248       nächsten Befehl überspringen
.,F245 20 C7 ED JSR $EDC7       Sekundäradresse für TALK
                                senden
.,F248 8A       TXA             Geräteadresse wiederholen
.,F249 24 90    BIT $90         Status abfragen
.,F24B 10 E6    BPL $F233       verzweige wenn ok
.,F24D 4C 07 F7 JMP $F707       sonst 'DEVICE NOT PRESENT'

                                *** CKOUT Ausgabegerät setzen
.,F250 20 0F F3 JSR $F30F       sucht logische Filenummer
.,F253 F0 03    BEQ $F258       verzweige wenn gefunden
.,F255 4C 01 F7 JMP $F701       sonst 'FILE NOT OPEN'
.,F258 20 1F F3 JSR $F31F       setzt Fileparameter
.,F25B A5 BA    LDA $BA         Gerätenummer holen
.,F25D D0 03    BNE $F262       verzweige wenn ungleich Null
.,F25F 4C 0D F7 JMP $F70D       sonst 'NOT INPUT FILE'
.,F262 C9 03    CMP #$03        vergleiche mit Bildschirm ?
.,F264 F0 0F    BEQ $F275       verzweige wenn Bildschirm
.,F266 B0 11    BCS $F279       verzweige wenn IEC-Bus
.,F268 C9 02    CMP #$02        vergleiche mit RS-232
.,F26A D0 03    BNE $F26F       verzweige wenn nein
.,F26C 4C E1 EF JMP $EFE1       Ausgabe auf RS-232
                                vorbereiten

                                *** Band als Ausgabegerät setzen
.,F26F A6 B9    LDX $B9         Sekundäradresse laden
.,F271 E0 60    CPX #$60        mit 'Null' vergleichen
.,F273 F0 EA    BEQ $F25F       Bandfile zum Lesen, 'NOT
                                OUTPUT FILE'
.,F275 85 9A    STA $9A         Nummer des Ausgabegeräts
                                setzen
.,F277 18       CLC             Carry =0 (ok Kennzeichen)
.,F278 60       RTS             Rücksprung

                                *** Ausgabe auf IEC-Bus legen
.,F279 AA       TAX             Geräteadresse retten
.,F27A 20 0C ED JSR $ED0C       LISTEN senden
.,F27D A5 B9    LDA $B9         Sekundäradresse laden
.,F27F 10 05    BPL $F286       verzweige wenn kleiner 128
.,F281 20 BE ED JSR $EDBE       ATN zurücksetzen
.,F284 D0 03    BNE $F289       unbedingter Sprung
.,F286 20 B9 ED JSR $EDB9       Sekundäradresse für LISTEN
                                senden
.,F289 8A       TXA             Geräteadresse wiederholen
.,F28A 24 90    BIT $90         Status abfragen
.,F28C 10 E7    BPL $F275       verzweige wenn ok
.,F28E 4C 07 F7 JMP $F707       'device not present'

                                *** CLOSE logische Filenummer
                                *** im Akku
.,F291 20 14 F3 JSR $F314       sucht logische Filenummer
.,F294 F0 02    BEQ $F298       verzweige wenn gefunden
.,F296 18       CLC             File nicht vorhanden, dann
                                fertig
.,F297 60       RTS             Rücksprung
.,F298 20 1F F3 JSR $F31F       Fileparameter setzen
.,F29B 8A       TXA             Zeiger auf Parametereintrag
                                in Filetabelle
.,F29C 48       PHA             retten
.,F29D A5 BA    LDA $BA         Geräteadresse laden
.,F29F F0 50    BEQ $F2F1       verzweige wenn Tastatur
.,F2A1 C9 03    CMP #$03        vergleiche mit Bildschirm
.,F2A3 F0 4C    BEQ $F2F1       verzweige wenn Bildschirm
.,F2A5 B0 47    BCS $F2EE       verzweige wenn IEC-Bus
.,F2A7 C9 02    CMP #$02        vergleiche mit RS-232
.,F2A9 D0 1D    BNE $F2C8       nein, dann Band

                                *** RS-232 File schließen
.,F2AB 68       PLA             Zeiger auf Parametereintrag
.,F2AC 20 F2 F2 JSR $F2F2       Fileeintrag in Tabelle
                                löschen
.,F2AF 20 83 F4 JSR $F483       CIAs für I/O rücksetzen
.,F2B2 20 27 FE JSR $FE27       Memory-Top holen
.,F2B5 A5 F8    LDA $F8         RS-232 Eingabepuffer
                                HIGH-Byte laden
.,F2B7 F0 01    BEQ $F2BA       verzweige wenn 0
.,F2B9 C8       INY             HIGH-Byte von Memory-Top
                                erhöhen
.,F2BA A5 FA    LDA $FA         RS-232 Ausgabepuffer
                                HIGH-Byte laden
.,F2BC F0 01    BEQ $F2BF       verzweige wenn 0
.,F2BE C8       INY             sonst HIGH-Byte von Memory-
                                Top erhöhen
.,F2BF A9 00    LDA #$00        0 laden
.,F2C1 85 F8    STA $F8         und Puffer
.,F2C3 85 FA    STA $FA         freigeben
.,F2C5 4C 7D F4 JMP $F47D       Memory Top neu setzen

                                *** Band File schließen
.,F2C8 A5 B9    LDA $B9         Sekundäradresse laden
.,F2CA 29 0F    AND #$0F        Bits 0 bis 3 isolieren
.,F2CC F0 23    BEQ $F2F1       verzweige wenn File zum Lesen
.,F2CE 20 D0 F7 JSR $F7D0       Band-Puffer Startadresse
                                holen
.,F2D1 A9 00    LDA #$00        Markierung für letztes
                                Zeichen im Datenpuffer
.,F2D3 38       SEC             Flag für Ausgabe auf Recorder
.,F2D4 20 DD F1 JSR $F1DD       Zeichen in Kassettenpuffer
.,F2D7 20 64 F8 JSR $F864       Puffer auf Band schreiben
.,F2DA 90 04    BCC $F2E0       verzweige wenn alles ok
.,F2DC 68       PLA             Zeiger auf Fileeintrag holen
.,F2DD A9 00    LDA #$00        0 für Break
.,F2DF 60       RTS             Rücksprung
.,F2E0 A5 B9    LDA $B9         Sekundäradresse laden
.,F2E2 C9 62    CMP #$62        vergleiche auf Open mit EOT
.,F2E4 D0 0B    BNE $F2F1       verzweige wenn kein EOT
.,F2E6 A9 05    LDA #$05        Kontrollbyte für EOT-Header
.,F2E8 20 6A F7 JSR $F76A       Block auf Band schreiben
.,F2EB 4C F1 F2 JMP $F2F1       Überspringe nächsten Befehl
.,F2EE 20 42 F6 JSR $F642       IEC-File schließen
.,F2F1 68       PLA             Zeiger auf Fileeintrag holen
.,F2F2 AA       TAX             ins X-Register schieben
.,F2F3 C6 98    DEC $98         Anzahl der offenen Files
                                erniedrigen
.,F2F5 E4 98    CPX $98         und mit Zeiger auf
                                Fileeintrag vergleichen
.,F2F7 F0 14    BEQ $F30D       gleich, dann fertig
.,F2F9 A4 98    LDY $98         Anzahl der offenen Files
.,F2FB B9 59 02 LDA $0259,Y     Letzten Fileeintrag
.,F2FE 9D 59 02 STA $0259,X     an die
.,F301 B9 63 02 LDA $0263,Y     freigewordene
.,F304 9D 63 02 STA $0263,X     Stelle in der
.,F307 B9 6D 02 LDA $026D,Y     Filetabelle
.,F30A 9D 6D 02 STA $026D,X     schreiben
.,F30D 18       CLC             Carry =0 (ok Kennzeichnung)
.,F30E 60       RTS             Rücksprung

                                *** sucht logische Filenummer
                                *** (in X)
.,F30F A9 00    LDA #$00        Status
.,F311 85 90    STA $90         löschen
.,F313 8A       TXA             Filenummer in Akku schieben
.,F314 A6 98    LDX $98         Anzahl der offenen Files
.,F316 CA       DEX             Anzahl um eins verringern
.,F317 30 15    BMI $F32E       verzweige wenn kein File
                                offen oder Filenummer nicht
                                gefunden
.,F319 DD 59 02 CMP $0259,X     sucht Eintrag in Tabelle
.,F31C D0 F8    BNE $F316       verzweige wenn noch nicht
                                gefunden
.,F31E 60       RTS             Rücksprung

                                *** setzt Fileparameter
.,F31F BD 59 02 LDA $0259,X     logische Filenummer aus
.,F322 85 B8    STA $B8         Tabelle holen und speichern
.,F324 BD 63 02 LDA $0263,X     Geräteadresse aus Tabelle
.,F327 85 BA    STA $BA         holen und speichern
.,F329 BD 6D 02 LDA $026D,X     Sekundäradresse aus Tabelle
.,F32C 85 B9    STA $B9         holen und speichern
.,F32E 60       RTS             Rücksprung

                                *** CLALL schließt alle
                                Ein-/Ausgabe Kanäle
.,F32F A9 00    LDA #$00        Anzahl der offenen Files
.,F331 85 98    STA $98         auf Null stellen

                                *** CLRCH schließt aktiven
                                *** I/O-Kanal
.,F333 A2 03    LDX #$03        Vergleichswert in X
.,F335 E4 9A    CPX $9A         vergleiche mit Nummer des
                                Ausgabegeräts
.,F337 B0 03    BCS $F33C       verzweige wenn kleiner als 3
.,F339 20 FE ED JSR $EDFE       IEC, UNLISTEN senden
.,F33C E4 99    CPX $99         vergleiche mit Nummer des
                                Eingabegeräts
.,F33E B0 03    BCS $F343       verzweige wenn kleiner als 3
.,F340 20 EF ED JSR $EDEF       IEC, UNTALK senden
.,F343 86 9A    STX $9A         Ausgabe wieder auf Bildschirm
.,F345 A9 00    LDA #$00        Eingabe wieder
.,F347 85 99    STA $99         von Tastatur
.,F349 60       RTS             Rücksprung

                                *** OPEN
.,F34A A6 B8    LDX $B8         Filenummer in X
.,F34C D0 03    BNE $F351       verzweige wenn ungleich Null
.,F34E 4C 0A F7 JMP $F70A       'not input file' (??)
.,F351 20 0F F3 JSR $F30F       sucht logische Filenummer
.,F354 D0 03    BNE $F359       nicht gefunden, kann neu
                                angelegt werden
.,F356 4C FE F6 JMP $F6FE       sonst 'file open'
.,F359 A6 98    LDX $98         Anzahl der offenen Files
.,F35B E0 0A    CPX #$0A        mit 10 vergleichen
.,F35D 90 03    BCC $F362       kleiner 10 dann ok
.,F35F 4C FB F6 JMP $F6FB       'too many files'
.,F362 E6 98    INC $98         Anzahl erhöhen
.,F364 A5 B8    LDA $B8         logische Filenummer laden
.,F366 9D 59 02 STA $0259,X     und in die Tabelle schreiben
.,F369 A5 B9    LDA $B9         Sekundäradresse laden
.,F36B 09 60    ORA #$60        Bit 5 und 6 setzen
.,F36D 85 B9    STA $B9         wieder speichern
.,F36F 9D 6D 02 STA $026D,X     und in die Tabelle schreiben
.,F372 A5 BA    LDA $BA         Gerätenummer laden
.,F374 9D 63 02 STA $0263,X     und in die Tabelle schreiben
.,F377 F0 5A    BEQ $F3D3       verzweige wenn Gerätenummer
                                für Tastatur
.,F379 C9 03    CMP #$03        Code für Bildschirm
.,F37B F0 56    BEQ $F3D3       ja, so verzweige
.,F37D 90 05    BCC $F384       verzweige wenn nicht IEC-Bus
.,F37F 20 D5 F3 JSR $F3D5       File auf IEC-Bus eröffnen
.,F382 90 4F    BCC $F3D3       unbedingter Sprung
.,F384 C9 02    CMP #$02        Code für Band
.,F386 D0 03    BNE $F38B       verzweige wenn nein
.,F388 4C 09 F4 JMP $F409       RS-232 open
.,F38B 20 D0 F7 JSR $F7D0       Bandpuffer Startadresse in X
                                und Y holen
.,F38E B0 03    BCS $F393       verzweige wenn HIGH-Byte
                                größer als 2
.,F390 4C 13 F7 JMP $F713       'illegal device number'
.,F393 A5 B9    LDA $B9         Sekundäradresse laden
.,F395 29 0F    AND #$0F        Bits 0 bis 3 isolieren
.,F397 D0 1F    BNE $F3B8       ungleich Null dann schreiben
.,F399 20 17 F8 JSR $F817       wartet auf Play-Taste
.,F39C B0 36    BCS $F3D4       verzweige wenn Play Taste
                                gedrückt
.,F39E 20 AF F5 JSR $F5AF       'SEARCHING' ('for name')
                                ausgeben
.,F3A1 A5 B7    LDA $B7         Länge des Filenamens
.,F3A3 F0 0A    BEQ $F3AF       kein Filename, dann weiter
.,F3A5 20 EA F7 JSR $F7EA       sucht gewünschen Bandheader
.,F3A8 90 18    BCC $F3C2       verzweige wenn gefunden
.,F3AA F0 28    BEQ $F3D4       verzweige wenn STOP-Taste
.,F3AC 4C 04 F7 JMP $F704       EOT, 'FILE NOT FOUND'
                                ausgeben
.,F3AF 20 2C F7 JSR $F72C       nächsten Bandheader suchen
.,F3B2 F0 20    BEQ $F3D4       EOT, Fehler
.,F3B4 90 0C    BCC $F3C2       verzweige wenn gefunden
.,F3B6 B0 F4    BCS $F3AC       sonst PRG-File, weiter suchen
.,F3B8 20 38 F8 JSR $F838       wartet auf Record & Play
                                Taste
.,F3BB B0 17    BCS $F3D4       STOP-Taste, dann Abbruch
.,F3BD A9 04    LDA #$04        Kontrollbyte für Datenheader
.,F3BF 20 6A F7 JSR $F76A       Header auf Band schreiben
.,F3C2 A9 BF    LDA #$BF        Zeiger auf Ende des
                                Bandpuffers
.,F3C4 A4 B9    LDY $B9         Sekundäradresse laden
.,F3C6 C0 60    CPY #$60        vergleiche mit $60 für Band
                                lesen
.,F3C8 F0 07    BEQ $F3D1       lesen, dann verzweige
.,F3CA A0 00    LDY #$00        Zeiger auf 0 setzen
.,F3CC A9 02    LDA #$02        Kontrollbyte für Datenblock
.,F3CE 91 B2    STA ($B2),Y     in Bandpuffer schreiben
.,F3D0 98       TYA             Zeiger in Akku
.,F3D1 85 A6    STA $A6         Zeiger in Bandpuffer setzen
.,F3D3 18       CLC             Carry =0 (ok Kennzeichen)
.,F3D4 60       RTS             Rücksprung

                                *** File auf IEC-Bus eröffnen
.,F3D5 A5 B9    LDA $B9         Sekundäradresse laden
.,F3D7 30 FA    BMI $F3D3       Rücksprung wenn größer,
                                gleich 128
.,F3D9 A4 B7    LDY $B7         Länge des Filenamens laden
.,F3DB F0 F6    BEQ $F3D3       gleich Null, dann fertig
.,F3DD A9 00    LDA #$00        Status
.,F3DF 85 90    STA $90         löschen
.,F3E1 A5 BA    LDA $BA         Geräteadressse laden
.,F3E3 20 0C ED JSR $ED0C       LISTEN
.,F3E6 A5 B9    LDA $B9         Sekundäradresse laden
.,F3E8 09 F0    ORA #$F0        Bits 4 bis 7 setzen (Open
                                Kennzeichnung)
.,F3EA 20 B9 ED JSR $EDB9       Sekundäradresse senden
.,F3ED A5 90    LDA $90         Status testen
.,F3EF 10 05    BPL $F3F6       verzweige wenn ok
.,F3F1 68       PLA             Stack
.,F3F2 68       PLA             rücksetzen
.,F3F3 4C 07 F7 JMP $F707       'device not present'
.,F3F6 A5 B7    LDA $B7         Länge des Filenamens
.,F3F8 F0 0C    BEQ $F406       kein Filename, dann fertig
.,F3FA A0 00    LDY #$00        Zeiger auf Null setzen
.,F3FC B1 BB    LDA ($BB),Y     Filenamen holen
.,F3FE 20 DD ED JSR $EDDD       auf IEC-Bus ausgeben
.,F401 C8       INY             Zeiger erhöhen
.,F402 C4 B7    CPY $B7         mit Länge des Filenamens
                                vergleichen
.,F404 D0 F6    BNE $F3FC       verzweige wenn noch nicht
                                alle Zeichen
.,F406 4C 54 F6 JMP $F654       UNLISTEN, return

                                *** RS-232 Open
.,F409 20 83 F4 JSR $F483       CIAs setzen
.,F40C 8C 97 02 STY $0297       RS-232 Status löschen
.,F40F C4 B7    CPY $B7         Länge des "Filenamens"
.,F411 F0 0A    BEQ $F41D       verzweige wenn kein Filename
.,F413 B1 BB    LDA ($BB),Y     die ersten
.,F415 99 93 02 STA $0293,Y     vier
.,F418 C8       INY             Zeichen
.,F419 C0 04    CPY #$04        speichern
.,F41B D0 F2    BNE $F40F       verzweige wenn noch nicht
                                alle vier Zeichen
.,F41D 20 4A EF JSR $EF4A       Anzahl der Datenbits
                                berechnen
.,F420 8E 98 02 STX $0298       und speichern
.,F423 AD 93 02 LDA $0293       Kontrollregister holen
.,F426 29 0F    AND #$0F        Bits für Baud-Rate isolieren
.,F428 F0 1C    BEQ $F446       verzweige wenn User-Baud-Rate
.,F42A 0A       ASL             mal 2 für Tabelle
.,F42B AA       TAX             als Zeiger merken
.,F42C AD A6 02 LDA $02A6       NTSC-Version
.,F42F D0 09    BNE $F43A       verzweige wenn nein
.,F431 BC C1 FE LDY $FEC1,X     Baud-Rate, HIGH für
                                NTSC-Timing
.,F434 BD C0 FE LDA $FEC0,X     Baud-Rate, LOW
.,F437 4C 40 F4 JMP $F440       überspringe zwei Befehle
.,F43A BC EB E4 LDY $E4EB,X     Baud-Rate, HIGH für
                                PAL-Timing
.,F43D BD EA E4 LDA $E4EA,X     Baud-Rate, LOW
.,F440 8C 96 02 STY $0296       HIGH-Byte speichern
.,F443 8D 95 02 STA $0295       LOW-Byte speichern
.,F446 AD 95 02 LDA $0295       Timerwert = Baud-Rate *
                                zwei + $C8 (200)
.,F449 0A       ASL             Timer LOW * zwei
.,F44A 20 2E FF JSR $FF2E       Timerwert für Baud-Rate
                                ermitteln
.,F44D AD 94 02 LDA $0294       Kommandoregister laden
.,F450 4A       LSR             Prüfe ob 3-Line-Handshake
.,F451 90 09    BCC $F45C       verzweige wenn ja
.,F453 AD 01 DD LDA $DD01       Prüfe ob Data Set Ready
.,F456 0A       ASL             Bit 7 ins Carry
.,F457 B0 03    BCS $F45C       verzweige wenn DSR vorhanden
.,F459 20 0D F0 JSR $F00D       Status für DSR setzen
.,F45C AD 9B 02 LDA $029B       Anfang RS-232 Eingabepuffer
.,F45F 8D 9C 02 STA $029C       mit Ende des Eingabepuffers
                                gleichsetzen
.,F462 AD 9E 02 LDA $029E       Anfang des RS-232
                                Ausgabepuffers
.,F465 8D 9D 02 STA $029D       mit Ende des Ausgabepuffers
                                gleichsetzen
.,F468 20 27 FE JSR $FE27       Memory Top holen
.,F46B A5 F8    LDA $F8         HIGH-Byte des Zeigers auf
                                RS-232 Eingabepuffer
.,F46D D0 05    BNE $F474       ungleich Null, so Eingabe-
                                puffer bereits angelegt
.,F46F 88       DEY             HIGH-Byte Memory Top -1
.,F470 84 F8    STY $F8         als Zeiger für RS-232
                                Eingabepuffer speichern
.,F472 86 F7    STX $F7         LOW-Byte Memory Top als LOW-
                                Byte Eingabepuffer setzen
.,F474 A5 FA    LDA $FA         HIGH-Byte des Zeigers auf
                                RS-232 Ausgabepuffer
.,F476 D0 05    BNE $F47D       verzweige wenn Ausgabepuffer
                                bereits angelegt
.,F478 88       DEY             HIGH-Byte des Memory Top -1
.,F479 84 FA    STY $FA         und als Zeiger für RS-232
                                Ausgabepuffer setzen
.,F47B 86 F9    STX $F9         LOW-Byte Memory Top als LOW-
                                Byte Ausgabepuffer setzen
.,F47D 38       SEC             Carry =1 (Fehlerkennzeichen)
.,F47E A9 F0    LDA #$F0        Ftag für Puffer schützen/
                                freigeben setzen
.,F480 4C 2D FE JMP $FE2D       Memory-Top neu setzen

                                *** CIAs nach RS 232 rücksetzen
.,F483 A9 7F    LDA #$7F        Bitwert für alle
.,F485 8D 0D DD STA $DD0D       NMIs blockieren setzen
.,F488 A9 06    LDA #$06        Bit 1 und 2 Ausgang
.,F48A 8D 03 DD STA $DD03       PORT B Richtung
.,F48D 8D 01 DD STA $DD01       PORT A Richtung
.,F490 A9 04    LDA #$04        Bit 2 setzen
.,F492 0D 00 DD ORA $DD00       Bit 2 = TXD
.,F495 8D 00 DD STA $DD00       Ausgeben
.,F498 A0 00    LDY #$00        RS-232
.,F49A 8C A1 02 STY $02A1       NMI-Flag löschen
.,F49D 60       RTS             Rücksprung

                                *** LOAD - Routine
.,F49E 86 C3    STX $C3         Startadresse
.,F4A0 84 C4    STY $C4         speichern
.,F4A2 6C 30 03 JMP ($0330)     JMP $F4A5 LOAD-Vektor
.,F4A5 85 93    STA $93         Load/Verify Flag
.,F4A7 A9 00    LDA #$00        Status
.,F4A9 85 90    STA $90         löschen
.,F4AB A5 BA    LDA $BA         Geräteadresse laden
.,F4AD D0 03    BNE $F4B2       ungleich Null, dann weiter
.,F4AF 4C 13 F7 JMP $F713       'ILLEGAL DEVICE NUMBER'
.,F4B2 C9 03    CMP #$03        vergleiche mit Code für
                                Bildschirm
.,F4B4 F0 F9    BEQ $F4AF       verzweige wenn ja, Fehler
.,F4B6 90 7B    BCC $F533       kleiner 3, dann vom Band

                                *** IEC-Load
.,F4B8 A4 B7    LDY $B7         Länge des Filenamens laden
.,F4BA D0 03    BNE $F4BF       ungleich Null, dann ok
.,F4BC 4C 10 F7 JMP $F710       'MISSING FILENAME'
.,F4BF A6 B9    LDX $B9         Sekundäradresse laden
.,F4C1 20 AF F5 JSR $F5AF       'SEARCHING FOR' (filename)
.,F4C4 A9 60    LDA #$60        Sekundäradresse Null laden
                                (für OPEN)
.,F4C6 85 B9    STA $B9         und speichern
.,F4C8 20 D5 F3 JSR $F3D5       File auf IEC-Bus eröffnen
.,F4CB A5 BA    LDA $BA         Gerätenummer laden
.,F4CD 20 09 ED JSR $ED09       und TALK senden
.,F4D0 A5 B9    LDA $B9         Sekundäradresse laden
.,F4D2 20 C7 ED JSR $EDC7       und senden
.,F4D5 20 13 EE JSR $EE13       Byte vom IEC-Bus holen
.,F4D8 85 AE    STA $AE         als Startadresse LOW spei
                                chern
.,F4DA A5 90    LDA $90         Status laden
.,F4DC 4A       LSR             Bit 1
.,F4DD 4A       LSR             ins Carry schieben
.,F4DE B0 50    BCS $F530       falls gesetzt, dann Time out
                                (Fehler)
.,F4E0 20 13 EE JSR $EE13       Startadresse HIGH holen
.,F4E3 85 AF    STA $AF         und speichern
.,F4E5 8A       TXA             Sekundäradresse laden
.,F4E6 D0 08    BNE $F4F0       verzweige falls ungleich Null
.,F4E8 A5 C3    LDA $C3         Startadresse LOW laden
.,F4EA 85 AE    STA $AE         und speichern
.,F4EC A5 C4    LDA $C4         Startadresse HIGH laden
.,F4EE 85 AF    STA $AF         und speichern
.,F4F0 20 D2 F5 JSR $F5D2       'LOADING'/'VERIFYING'
                                ausgeben
.,F4F3 A9 FD    LDA #$FD        Time-out
.,F4F5 25 90    AND $90         Bit
.,F4F7 85 90    STA $90         löschen
.,F4F9 20 E1 FF JSR $FFE1       Stop-Taste abfragen
.,F4FC D0 03    BNE $F501       nicht gedrückt, dann weiter
.,F4FE 4C 33 F6 JMP $F633       File schließen
.,F501 20 13 EE JSR $EE13       Programmbyte vom Bus holen
.,F504 AA       TAX             Akku in X-REG retten
.,F505 A5 90    LDA $90         Status testen
.,F507 4A       LSR             Time-out
.,F508 4A       LSR             Bit ins Carry schieben
.,F509 B0 E8    BCS $F4F3       falls Fehler, dann abbrechen
.,F50B 8A       TXA             ansonsten Akku wiederholen
.,F50C A4 93    LDY $93         Load/Verify Flag testen
.,F50E F0 0C    BEQ $F51C       gleich Null, dann LOAD
.,F510 A0 00    LDY #$00        Zähler auf Null setzen
.,F512 D1 AE    CMP ($AE),Y     Verify, Vergleich
.,F514 F0 08    BEQ $F51E       verzweige falls gleich
.,F516 A9 10    LDA #$10        Bit 4 für Status setzen
.,F518 20 1C FE JSR $FE1C       Status setzen
.:F51B 2C       .BYTE $2C       Skip nach $F51E
.,F51C 91 AE    STA ($AE),Y     Byte abspeichern
.,F51E E6 AE    INC $AE         LOW-Byte der Adresse erhöhen
.,F520 D0 02    BNE $F524       verzweige falls kein Übertrag
.,F522 E6 AF    INC $AF         ansonsten HIGH-Byte erhöhen
.,F524 24 90    BIT $90         Status prüfen
.,F526 50 CB    BVC $F4F3       verzweige wenn noch kein EOI
.,F528 20 EF ED JSR $EDEF       UNTALK senden
.,F52B 20 42 F6 JSR $F642       File schließen
.,F52E 90 79    BCC $F5A9       vezweige wenn kein Fehler
.,F530 4C 04 F7 JMP $F704       'FILE NOT FOUND'
.,F533 4A       LSR             Gerätenummer feststellen
.,F534 B0 03    BCS $F539       eins (Band) , dann weiter
.,F536 4C 13 F7 JMP $F713       RS 232, 'ILLEGAL DEVICE
                                NUMBER'
.,F539 20 D0 F7 JSR $F7D0       Bandpuffer Startadresse holen
.,F53C B0 03    BCS $F541       verzweige wenn HIGH-Byte der
                                Bandpufferstartadresse größer/
                                gleich 2
.,F53E 4C 13 F7 JMP $F713       sonst 'ILLEGAL DEVICE NUMBER'
.,F541 20 17 F8 JSR $F817       wartet auf Play-Taste
.,F544 B0 68    BCS $F5AE       STOP-Taste, dann Abbruch
.,F546 20 AF F5 JSR $F5AF       'SEARCHING' ('for name')
                                ausgeben
.,F549 A5 B7    LDA $B7         Länge des Filenamens laden
.,F54B F0 09    BEQ $F556       verzweige wenn Null
.,F54D 20 EA F7 JSR $F7EA       gewünschten Bandheader suchen
.,F550 90 0B    BCC $F55D       verzweige wenn gefunden
.,F552 F0 5A    BEQ $F5AE       STOP-Taste, dann Abbruch
.,F554 B0 DA    BCS $F530       EOT, dann 'FILE NOT FOUND'
.,F556 20 2C F7 JSR $F72C       nächsten Bandheader suchen
.,F559 F0 53    BEQ $F5AE       STOP-Taste, dann Abbruch
.,F55B B0 D3    BCS $F530       'EOT', dann 'FILE NOT FOUND'
.,F55D A5 90    LDA $90         Status holen
.,F55F 29 10    AND #$10        EOF-Bit ausblenden
.,F561 38       SEC             Carry =1 (Fehlerkennzeichen)
.,F562 D0 4A    BNE $F5AE       verzweige falls Fehler
.,F564 E0 01    CPX #$01        Header-Typ 1 = BASIC-
                                Programm (verschiebbar)
.,F566 F0 11    BEQ $F579       verzweige wenn Header-Typ =1
.,F568 E0 03    CPX #$03        3 = Maschinen-Programm
                                (absolut)
.,F56A D0 DD    BNE $F549       verzweige wenn nicht 3
                                (falscher Header)
.,F56C A0 01    LDY #$01        Zeiger setzen
.,F56E B1 B2    LDA ($B2),Y     LOW-Byte Startadresse holen
.,F570 85 C3    STA $C3         und speichern
.,F572 C8       INY             Zeiger erhöhen
.,F573 B1 B2    LDA ($B2),Y     HIGH-Byte Startadresse holen
.,F575 85 C4    STA $C4         und speichern
.,F577 B0 04    BCS $F57D       unbedingter Sprung
.,F579 A5 B9    LDA $B9         Sekundär-Adresse
.,F57B D0 EF    BNE $F56C       ungleich Null, dann nicht
                                verschiebbar laden
.,F57D A0 03    LDY #$03        Zeiger setzen
.,F57F B1 B2    LDA ($B2),Y     LOW-Byte der Endadresse+1 des
                                Programms holen
.,F581 A0 01    LDY #$01        Zeiger auf LOW-Byte Anfangs
                                adresse setzen
.,F583 F1 B2    SBC ($B2),Y     von Endadresse subtrahieren
.,F585 AA       TAX             Ergebnis ins X-REG schieben
.,F586 A0 04    LDY #$04        Zeiger auf HIGH-Byte der
                                Endadresse setzen
.,F588 B1 B2    LDA ($B2),Y     Endadresse holen
.,F58A A0 02    LDY #$02        Zeiger auf Startadresse
                                setzen
.,F58C F1 B2    SBC ($B2),Y     und von Endadresse subtrahie
                                ren
.,F58E A8       TAY             Ergebnis ins Y-REG schieben
.,F58F 18       CLC             Carry für Addition löschen
.,F590 8A       TXA             LOW-Byte der Programmlänge
                                in Akku schieben
.,F591 65 C3    ADC $C3         mit LOW-Byte der Anfangs
                                adresse addieren
.,F593 85 AE    STA $AE         als LOW-Byte der Endadresse
                                speichern
.,F595 98       TYA             HIGH-Byte der Programmlänge
                                in Akku schieben
.,F596 65 C4    ADC $C4         mit HIGH-Byte Anfangsadresse
                                addieren
.,F598 85 AF    STA $AF         als HIGH-Byte Endadresse
                                speichern
.,F59A A5 C3    LDA $C3         Startadresse
.,F59C 85 C1    STA $C1         nach $C1
.,F59E A5 C4    LDA $C4         und $C2
.,F5A0 85 C2    STA $C2         bringen
.,F5A2 20 D2 F5 JSR $F5D2       'LOADING' / 'VERIFYING'
                                ausgeben
.,F5A5 20 4A F8 JSR $F84A       Programm vom Band laden
.:F5A8 24       .BYTE $24       Skip nach $F5AA
.,F5A9 18       CLC             Carry =0 (ok Kennzeichen)
.,F5AA A6 AE    LDX $AE         Endadresse
.,F5AC A4 AF    LDY $AF         nach X/Y
.,F5AE 60       RTS             Rücksprung

                                *** 'SEARCHING FOR' (Filename)
                                *** ausgeben
.,F5AF A5 9D    LDA $9D         Direkt-Modus-Flag laden
.,F5B1 10 1E    BPL $F5D1       verzweige wenn Bit 7 =0
                                (Programm-Mode)
.,F5B3 A0 0C    LDY #$0C        Offset für 'SEARCHING'
.,F5B5 20 2F F1 JSR $F12F       Meldung ausgeben
.,F5B8 A5 B7    LDA $B7         Länge des Filenamens
.,F5BA F0 15    BEQ $F5D1       gleich Null, dann fertig
.,F5BC A0 17    LDY #$17        Offset für 'FOR'
.,F5BE 20 2F F1 JSR $F12F       Meldung ausgeben
.,F5C1 A4 B7    LDY $B7         Länge des Filenamens
.,F5C3 F0 0C    BEQ $F5D1       gleich Null, dann fertig
.,F5C5 A0 00    LDY #$00        Zähler setzen
.,F5C7 B1 BB    LDA ($BB),Y     Filenamen holen
.,F5C9 20 D2 FF JSR $FFD2       und ausgeben
.,F5CC C8       INY             Zähler erhöhen
.,F5CD C4 B7    CPY $B7         mit Länge des Filenamens ver-
                                gleichen
.,F5CF D0 F6    BNE $F5C7       verzweige wenn noch nicht
                                alle Buchstaben
.,F5D1 60       RTS             Rücksprung

                                *** 'LOADING/VERIFYING' ausgeben
.,F5D2 A0 49    LDY #$49        Offset für 'LOADING'
.,F5D4 A5 93    LDA $93         Load/Verify-Flag laden
.,F5D6 F0 02    BEQ $F5DA       Load wenn 0, dann ausgeben
.,F5D8 A0 59    LDY #$59        sonst Offset für 'VERIFYING'
.,F5DA 4C 2B F1 JMP $F12B       Meldung ausgeben, Rücksprung

                                *** SAVE - Routine
.,F5DD 86 AE    STX $AE         LOW-Byte der Endadresse
                                speichern
.,F5DF 84 AF    STY $AF         High-Byte der Endadresse
                                speichern
.,F5E1 AA       TAX             Zeiger auf Anfangsadress-
                                tabelle ins X-REG schieben
.,F5E2 B5 00    LDA $00,X       LOW-Byte der Startadresse
.,F5E4 85 C1    STA $C1         holen und speichern
.,F5E6 B5 01    LDA $01,X       HIGH-Byte der Startadresse
.,F5E8 85 C2    STA $C2         holen und speichern
.,F5EA 6C 32 03 JMP ($0332)     SAVE-Vektor, JMP $F5ED
.,F5ED A5 BA    LDA $BA         Geräteadresse laden
.,F5EF D0 03    BNE $F5F4       verzweige wenn nicht gleich 0
.,F5F1 4C 13 F7 JMP $F713       sonst 'ILLEGAL DEVICE NUMBER'
.,F5F4 C9 03    CMP #$03        mit Code für Bildschirm
                                vergleichen
.,F5F6 F0 F9    BEQ $F5F1       wenn Bildschirm, dann Fehler
.,F5F8 90 5F    BCC $F659       kleiner 3, dann verzweige

                                *** Speichern auf IEC-Bus
.,F5FA A9 61    LDA #$61        Sekundäradresse 1
.,F5FC 85 B9    STA $B9         setzen
.,F5FE A4 B7    LDY $B7         Länge des Filenamens laden
.,F600 D0 03    BNE $F605       ungleich Null, dann ok
.,F602 4C 10 F7 JMP $F710       sonst 'MISSING FILENAME'
.,F605 20 D5 F3 JSR $F3D5       Filenamen auf IEC-Bus
.,F608 20 8F F6 JSR $F68F       'SAVING' ausgeben
.,F60B A5 BA    LDA $BA         Geräteadresse laden
.,F60D 20 0C ED JSR $ED0C       und LISTEN senden
.,F610 A5 B9    LDA $B9         Sekundäradresse laden
.,F612 20 B9 ED JSR $EDB9       und für LISTEN senden
.,F615 A0 00    LDY #$00        Zähler auf Null setzen
.,F617 20 8E FB JSR $FB8E       Startadresse nach $AC/$AD
.,F61A A5 AC    LDA $AC         Startadresse LOW-
.,F61C 20 DD ED JSR $EDDD       Byte senden
.,F61F A5 AD    LDA $AD         und HIGH-
.,F621 20 DD ED JSR $EDDD       senden
.,F624 20 D1 FC JSR $FCD1       Endadresse schon erreicht ?
.,F627 B0 16    BCS $F63F       ja, dann fertig
.,F629 B1 AC    LDA ($AC),Y     Programmbyte laden
.,F62B 20 DD ED JSR $EDDD       auf IEC-Bus ausgeben
.,F62E 20 E1 FF JSR $FFE1       STOP-Taste abfragen
.,F631 D0 07    BNE $F63A       nicht gedrückt, dann
                                weitermachen
.,F633 20 42 F6 JSR $F642       IEC-Bus Kanal schließen
.,F636 A9 00    LDA #$00        Kennzeichnung für 'BREAK'
.,F638 38       SEC             Carry =1 (Fehlerkennzeichen)
.,F639 60       RTS             Rücksprung
.,F63A 20 DB FC JSR $FCDB       laufende Adresse erhöhen
.,F63D D0 E5    BNE $F624       unbedingter Sprung
.,F63F 20 FE ED JSR $EDFE       UNLISTEN senden

                                *** File auf IEC-Bus schließen
.,F642 24 B9    BIT $B9         Sekundäradresse testen
.,F644 30 11    BMI $F657       verzweige falls keine
                                Sekundäradresse
.,F646 A5 BA    LDA $BA         Geräteadresse laden
.,F648 20 0C ED JSR $ED0C       und LISTEN senden
.,F64B A5 B9    LDA $B9         Sekundäradresse laden
.,F64D 29 EF    AND #$EF        Sekundäradresse
.,F64F 09 E0    ORA #$E0        für CLOSE berechnen
.,F651 20 B9 ED JSR $EDB9       und ausgeben
.,F654 20 FE ED JSR $EDFE       UNLISTEN senden
.,F657 18       CLC             Carry =0 (ok Kennzeichen)
.,F658 60       RTS             Rücksprung
.,F659 4A       LSR             Bit 0 ins Carry schieben
.,F65A B0 03    BCS $F65F       falls gesetzt, dann zu Band
.,F65C 4C 13 F7 JMP $F713       sonst RS-232, 'ILLEGAL DIVICE
                                NUMBER'
.,F65F 20 D0 F7 JSR $F7D0       Bandpuffer Startadresse holen
.,F662 90 8D    BCC $F5F1       falls HIGH-Byte der Band
                                Pufferstartadresse kleiner 2
                                dann 'ILLEGAL DEVICE NUMBER'
.,F664 20 38 F8 JSR $F838       wartet auf Record & Play-
                                Taste
.,F667 B0 25    BCS $F68E       STOP, dann Abbruch
.,F669 20 8F F6 JSR $F68F       'SAVING' (Name) ausgeben
.,F66C A2 03    LDX #$03        Header-Typ 3 = Maschinen
                                programm (absolut)
.,F66E A5 B9    LDA $B9         Sekundäradresse laden
.,F670 29 01    AND #$01        Bit 0 gesetzt (1 oder 3)
.,F672 D0 02    BNE $F676       falls ja, dann Maschinen
                                programm
.,F674 A2 01    LDX #$01        Header-Typ 1 = BASIC-
                                Programm (verschiebbar)
.,F676 8A       TXA             Header in Akku schieben
.,F677 20 6A F7 JSR $F76A       Header auf Band schreiben
.,F67A B0 12    BCS $F68E       Aussprung bei Stop-Taste
.,F67C 20 67 F8 JSR $F867       Programm auf Band schreiben
.,F67F B0 0D    BCS $F68E       Aussprung bei Stop-Taste
.,F681 A5 B9    LDA $B9         Sekundäradresse laden
.,F683 29 02    AND #$02        Bit 1 gesetzt (2 oder 3)
.,F685 F0 06    BEQ $F68D       falls nicht, dann fertig
.,F687 A9 05    LDA #$05        EOT Kontrollbyte
.,F689 20 6A F7 JSR $F76A       Block auf Band schreiben
.:F68C 24       .BYTE $24       Skip zu $F68E
.,F68D 18       CLC             Carry =0 (ok Kennzeichen)
.,F68E 60       RTS             Rücksprung

                                *** 'SAVING' ausgeben
.,F68F A5 9D    LDA $9D         Flag für Direktmodus laden
.,F691 10 FB    BPL $F68E       Bit 7 gelöscht, dann
                                Programm-Mode
.,F693 A0 51    LDY #$51        Offset für 'SAVING'
.,F695 20 2F F1 JSR $F12F       Meldung ausgeben
.,F698 4C C1 F5 JMP $F5C1       Filenamen ausgeben,
                                Rücksprung

                                *** UDTIM Time erhöhen und
                                *** STOP-Taste abfragen
.,F69B A2 00    LDX #$00        X-REG auf Null setzen
.,F69D E6 A2    INC $A2         Sekundenzeiger erhöhen
.,F69F D0 06    BNE $F6A7       verzweige falls kein Überlauf
.,F6A1 E6 A1    INC $A1         Minutenzeiger erhöhen
.,F6A3 D0 02    BNE $F6A7       verzweige falls kein Überlauf
.,F6A5 E6 A0    INC $A0         Stundenzeiger erhöhen
.,F6A7 38       SEC             Carry für Subtraktion löschen
.,F6A8 A5 A2    LDA $A2         Stundenzeiger laden
.,F6AA E9 01    SBC #$01        feststellen
.,F6AC A5 A1    LDA $A1         ob
.,F6AE E9 1A    SBC #$1A        24
.,F6B0 A5 A0    LDA $A0         Stunden
.,F6B2 E9 4F    SBC #$4F        erreicht
.,F6B4 90 06    BCC $F6BC       falls kleiner, dann verzweige
.,F6B6 86 A0    STX $A0         alle
.,F6B8 86 A1    STX $A1         Zeiger
.,F6BA 86 A2    STX $A2         auf Null setzen

                                *** Abfrage auf STOP-Taste direkt
                                *** vom Port
.,F6BC AD 01 DC LDA $DC01       Port B laden
.,F6BF CD 01 DC CMP $DC01       und
.,F6C2 D0 F8    BNE $F6BC       entprellen
.,F6C4 AA       TAX             Wert ins X-REG schieben
.,F6C5 30 13    BMI $F6DA       verzweige falls STOP-Taste
                                nicht gedrückt
.,F6C7 A2 BD    LDX #$BD        Bitmuster zur Abrage der
                                Reihe mit SHIFT-Tasten
.,F6C9 8E 00 DC STX $DC00       in Port A schreiben
.,F6CC AE 01 DC LDX $DC01       Port B laden
.,F6CF EC 01 DC CPX $DC01       und
.,F6D2 D0 F8    BNE $F6CC       entprellen
.,F6D4 8D 00 DC STA $DC00       Akku in Port A schreiben
.,F6D7 E8       INX             inhalt von Port B erhöhen
.,F6D8 D0 02    BNE $F6DC       verzweige falls ungleich Null
                                (SHIFT-Taste gedrückt)
.,F6DA 85 91    STA $91         Flag für Stop-Taste setzen
.,F6DC 60       RTS             Rücksprung

                                *** TIME holen
.,F6DD 78       SEI             Interrupt verhindern um Uhr
                                anzuhalten
.,F6DE A5 A2    LDA $A2         Stunden
.,F6E0 A6 A1    LDX $A1         Minuten
.,F6E2 A4 A0    LDY $A0         Sekunden holen

                                *** TIME setzen
.,F6E4 78       SEI             Interrupt verhindern um Uhr
                                anzuhalten
.,F6E5 85 A2    STA $A2         Stunden
.,F6E7 86 A1    STX $A1         Minuten
.,F6E9 84 A0    STY $A0         Sekunden schreiben
.,F6EB 58       CLI             Interrupt wieder ermöglichen
.,F6EC 60       RTS             Rücksprung

                                *** STOP-Taste abfragen
.,F6ED A5 91    LDA $91         STOP-Flag laden
.,F6EF C9 7F    CMP #$7F        auf Code für STOP testen
.,F6F1 D0 07    BNE $F6FA       verzweige falls nicht
.,F6F3 08       PHP             Statusregister retten
.,F6F4 20 CC FF JSR $FFCC       Ein-Ausgabe zurücksetzen
                                CLRCH
.,F6F7 85 C6    STA $C6         Anzahl der gedrückten Tasten
.,F6F9 28       PLP             Statusregister holen
.,F6FA 60       RTS             Rücksprung

                                *** Meldungen des Betriebs
                                *** systems ausgeben
.,F6FB A9 01    LDA #$01        'TOO MANY FILES'
.:F6FD 2C       .BYTE $2C       Skip zu $F700
.,F6FE A9 02    LDA #$02        'FILE OPEN'
.:F700 2C       .BYTE $2C       Skip zu $F703
.,F701 A9 03    LDA #$03        'FILE NOT OPEN'
.:F703 2C       .BYTE $2C       Skip zu $F706
.,F704 A9 04    LDA #$04        'FILE NOT FOUND'
.:F706 2C       .BYTE $2C       Skip zu $F709
.,F707 A9 05    LDA #$05        'DIVICE NOT PRESENT'
.:F709 2C       .BYTE $2C       Skip zu $F70C
.,F70A A9 06    LDA #$06        'NOT INPUT FILE'
.:F70C 2C       .BYTE $2C       Skip zu $F70F
.,F70D A9 07    LDA #$07        'NOT OUTPUT FILE'
.:F70F 2C       .BYTE $2C       Skip zu $F712
.,F710 A9 08    LDA #$08        'MISSING FILENAME'
.:F712 2C       .BYTE $2C       Skip zu $F715
.,F713 A9 09    LDA #$09        'ILLEGAL DEVICE NUMBER'
.,F715 48       PHA             Fehlernummer merken
.,F716 20 CC FF JSR $FFCC       Ein-Ausgabe zurücksetzen
                                CLRCH
.,F719 A0 00    LDY #$00
.,F71B 24 9D    BIT $9D         Flag auf Direkt-Mode testen
.,F71D 50 0A    BVC $F729       nicht gesetzt, dann übergehen
.,F71F 20 2F F1 JSR $F12F       'I/O ERROR #' ausgeben
.,F722 68       PLA             Fehlernummer holen
.,F723 48       PHA             und wieder merken
.,F724 09 30    ORA #$30        nach ASCII wandeln
.,F726 20 D2 FF JSR $FFD2       und ausgeben
.,F729 68       PLA             Fehlernummer holen
.,F72A 38       SEC             Carry =1 (Fehlerkennzeichen)
.,F72B 60       RTS             Rücksprung

                                *** Programm Header vom Band
                                *** lesen
.,F72C A5 93    LDA $93         Load/Verify Flag laden
.,F72E 48       PHA             und retten
.,F72F 20 41 F8 JSR $F841       Block vom Band lesen
.,F732 68       PLA             L/V Flag wiederholen
.,F733 85 93    STA $93         und speichern
.,F735 B0 32    BCS $F769       Fehler, dann beenden
.,F737 A0 00    LDY #$00        Zähler auf Null stellen
.,F739 B1 B2    LDA ($B2),Y     Header-Typ testen
.,F73B C9 05    CMP #$05        EOT ?
.,F73D F0 2A    BEQ $F769       verzweige falls ja
.,F73F C9 01    CMP #$01        BASIC-Programm ?
.,F741 F0 08    BEQ $F74B       verzweige falls ja
.,F743 C9 03    CMP #$03        Maschinenprogramm ?
.,F745 F0 04    BEQ $F74B       verzweige falls ja
.,F747 C9 04    CMP #$04        Daten-Header ?
.,F749 D0 E1    BNE $F72C       kein Header gefunden, dann
                                erneut suchen
.,F74B AA       TAX             Kennzeichen merken
.,F74C 24 9D    BIT $9D         Direktmodus ?
.,F74E 10 17    BPL $F767       nein, dann weiter
.,F750 A0 63    LDY #$63        Offset für 'FOUND'
.,F752 20 2F F1 JSR $F12F       Meldung ausgeben
.,F755 A0 05    LDY #$05        Zeiger auf Filenamen
.,F757 B1 B2    LDA ($B2),Y     Filenamen holen
.,F759 20 D2 FF JSR $FFD2       und ausgeben
.,F75C C8       INY             Zeiger erhöhen
.,F75D C0 15    CPY #$15        schon alle Buchstaben
.,F75F D0 F6    BNE $F757       verzweige wenn nein
.,F761 A5 A1    LDA $A1         Akku mit mittelwertigem
                                Time-Byte laden
.,F763 20 E0 E4 JSR $E4E0       wartet auf Commodore-Taste
                                oder Zeitschleife
.,F766 EA       NOP             no operation
.,F767 18       CLC             Carry =0 (ok Kennzeichen)
.,F768 88       DEY             Y-REG auf $FF zur Kennzeich
                                nung, daß kein EOT
.,F769 60       RTS             Rücksprung

                                *** Header generieren und auf
                                *** Band schreiben
.,F76A 85 9E    STA $9E         Header-Typ speichern
.,F76C 20 D0 F7 JSR $F7D0       Bandpufferadresse holen
.,F76F 90 5E    BCC $F7CF       verzweige falls Adresse
                                ungültig
.,F771 A5 C2    LDA $C2         Startadresse
.,F773 48       PHA             laden
.,F774 A5 C1    LDA $C1         und in
.,F776 48       PHA             Stack schreiben
.,F777 A5 AF    LDA $AF         Endadresse
.,F779 48       PHA             laden
.,F77A A5 AE    LDA $AE         und in
.,F77C 48       PHA             Stack schreiben
.,F77D A0 BF    LDY #$BF        Pufferlänge für Schleife
                                holen
.,F77F A9 20    LDA #$20        Code für ' ' laden
.,F781 91 B2    STA ($B2),Y     und speichern
.,F783 88       DEY             Zähler verringern
.,F784 D0 FB    BNE $F781       verzweige falls Puffer noch
                                nicht alles gelöscht
.,F786 A5 9E    LDA $9E         gespeicherten Header-Typ
                                holen
.,F788 91 B2    STA ($B2),Y     und in Puffer schreiben
.,F78A C8       INY             Zähler erhöhen
.,F78B A5 C1    LDA $C1         Startadresse LOW holen
.,F78D 91 B2    STA ($B2),Y     und in Puffer schreiben
.,F78F C8       INY             Zähler erhöhen
.,F790 A5 C2    LDA $C2         Startadesse HIGH holen
.,F792 91 B2    STA ($B2),Y     und in Puffer schreiben
.,F794 C8       INY             Zähler erhöhen
.,F795 A5 AE    LDA $AE         Endadresse LOW holen
.,F797 91 B2    STA ($B2),Y     und in Puffer schreiben
.,F799 C8       INY             Zähler erhöhen
.,F79A A5 AF    LDA $AF         Endadresse HIGH holen
.,F79C 91 B2    STA ($B2),Y     und in Puffer schreiben
.,F79E C8       INY             Zähler erhöhen
.,F79F 84 9F    STY $9F         Zähler speichern
.,F7A1 A0 00    LDY #$00        Zähler für Filenamen auf Null
                                setzen
.,F7A3 84 9E    STY $9E         und speichern
.,F7A5 A4 9E    LDY $9E         Zähler holen
.,F7A7 C4 B7    CPY $B7         und mit Länge des Filenamens
                                vergleichen
.,F7A9 F0 0C    BEQ $F7B7       verzweige falls alle Buchsta-
                                ben geholt
.,F7AB B1 BB    LDA ($BB),Y     Filenamen holen
.,F7AD A4 9F    LDY $9F         Pufferzeiger laden
.,F7AF 91 B2    STA ($B2),Y     und Zeichen in Puffer schrei-
                                ben
.,F7B1 E6 9E    INC $9E         Zähler für Filenamen erhöhen
.,F7B3 E6 9F    INC $9F         Zeiger auf Bandpuffer erhöhen
.,F7B5 D0 EE    BNE $F7A5       unbedingter Sprung
.,F7B7 20 D7 F7 JSR $F7D7       Start- und Endadresse auf
                                Bandpuffer holen
.,F7BA A9 69    LDA #$69
.,F7BC 85 AB    STA $AB         Checksumme für Header bzw.
                                Datenblock = $69
.,F7BE 20 6B F8 JSR $F86B       Block auf Band schreiben
.,F7C1 A8       TAY             Akku retten
.,F7C2 68       PLA             Endadresse
.,F7C3 85 AE    STA $AE         vom Stack
.,F7C5 68       PLA             holen und
.,F7C6 85 AF    STA $AF         in $AE/SAF speichern
.,F7C8 68       PLA             Startadresse
.,F7C9 85 C1    STA $C1         vom Stack
.,F7CB 68       PLA             holen und
.,F7CC 85 C2    STA $C2         in $C1/C2 speichern
.,F7CE 98       TYA             Akku wiederholen
.,F7CF 60       RTS             Rücksprung

                                *** Bandpuffer Startadresse holen
                                *** und prüfen ob gültig
.,F7D0 A6 B2    LDX $B2         Anfang Bandpuffer LOW in X
.,F7D2 A4 B3    LDY $B3         Anfang Bandpuffer HIGH in Y
.,F7D4 C0 02    CPY #$02        Adresse kleiner $200 ?
.,F7D6 60       RTS             Rücksprung

                                *** Bandpufferendadresse = Puf-
                                *** ferstartadresse + $C0 (192)
.,F7D7 20 D0 F7 JSR $F7D0       BandpufferaAdresse holen
.,F7DA 8A       TXA             Pufferanfang LOW in Akku
.,F7DB 85 C1    STA $C1         und speichern
.,F7DD 18       CLC             Carry für Addition löschen
.,F7DE 69 C0    ADC #$C0        Endadresse = Startadresse +
                                Länge $C0 (192)
.,F7E0 85 AE    STA $AE         und Endadresse speichern
.,F7E2 98       TYA             Pufferanfang HIGH in Akku
.,F7E3 85 C2    STA $C2         und speichern
.,F7E5 69 00    ADC #$00        mit Übertrag addieren
.,F7E7 85 AF    STA $AF         und speichern
.,F7E9 60       RTS             Rücksprung

                                *** Bandheader nach Namen suchen
.,F7EA 20 2C F7 JSR $F72C       nächsten Bandheader suchen
.,F7ED B0 1D    BCS $F80C       verzweige falls EOT (fertig)
.,F7EF A0 05    LDY #$05        Offset für Filenamen im
                                Header
.,F7F1 84 9F    STY $9F         und speichern
.,F7F3 A0 00    LDY #$00        Zähler für Länge des Filena-
                                mens auf Null setzen
.,F7F5 84 9E    STY $9E         und Zähler speichern
.,F7F7 C4 B7    CPY $B7         mit Länge des gesuchten
                                Namens vergleichen
.,F7F9 F0 10    BEQ $F80B       gleich, dann gefunden
.,F7FB B1 BB    LDA ($BB),Y     Buchstaben des Filenamens
.,F7FD A4 9F    LDY $9F         Position im Header laden
.,F7FF D1 B2    CMP ($B2),Y     mit Filenamen im Header
                                vergleichen
.,F801 D0 E7    BNE $F7EA       verzweige falls ungleich,
                                dann nächsten Header testen
.,F803 E6 9E    INC $9E         Zähler für Filenamen erhöhen
.,F805 E6 9F    INC $9F         Zeiger auf Position im Header
                                erhöhen
.,F807 A4 9E    LDY $9E         Zähler für Filenamen laden
.,F809 D0 EC    BNE $F7F7       unbedingter Sprung
.,F80B 18       CLC             Carry =0 (ok Kennzeichen)
.,F80C 60       RTS             Rücksprung

                                *** Bandpufferzeiger erhöhen
.,F80D 20 D0 F7 JSR $F7D0       Bandpufferadresse holen
.,F810 E6 A6    INC $A6         Zeiger erhöhen
.,F812 A4 A6    LDY $A6         und laden um
.,F814 C0 C0    CPY #$C0        mit Maximalwert (192) zu
                                vergleichen
.,F816 60       RTS             Rücksprung

                                *** Wartet auf Bandtaste
.,F817 20 2E F8 JSR $F82E       fragt BandtTaste ab
.,F81A F0 1A    BEQ $F836       gedrückt, dann fertig
.,F81C A0 1B    LDY #$1B        Offset für 'PRESS PLAY ON
                                TAPE'
.,F81E 20 2F F1 JSR $F12F       und ausgeben
.,F821 20 D0 F8 JSR $F8D0       testet auf STOP-Taste
.,F824 20 2E F8 JSR $F82E       fragt BandtTaste ab
.,F827 D0 F8    BNE $F821       nicht gedrückt so erneut
                                abfragen
.,F829 A0 6A    LDY #$6A        Offset für 'OK'
.,F82B 4C 2F F1 JMP $F12F       und ausgeben, Rücksprung

                                *** Abfrage ob Band-Taste
                                *** gedrückt
.,F82E A9 10    LDA #$10        Bit 4 testen
.,F830 24 01    BIT $01         mit Port vergleichen
.,F832 D0 02    BNE $F836       verzweige wenn Bandtaste
                                nicht gedrückt
.,F834 24 01    BIT $01         nochmal abfragen (Entprellen)
.,F836 18       CLC             Carry =0 (ok Kennzeichen)
.,F837 60       RTS             Rücksprung

                                *** Wartet auf Bandtaste für
                                *** Schreiben
.,F838 20 2E F8 JSR $F82E       fragt Bandtaste ab
.,F83B F0 F9    BEQ $F836       gedrückt, dann fertig
.,F83D A0 2E    LDY #$2E        Offset für 'PRESS RECORD &
                                PLAY ON TAPE'
.,F83F D0 DD    BNE $F81E       unbedingter Sprung

                                *** Block vom Band lesen
.,F841 A9 00    LDA #$00        Status
.,F843 85 90    STA $90         und Verify-Flag
.,F845 85 93    STA $93         löschen
.,F847 20 D7 F7 JSR $F7D7       Bandpufferadresse holen

                                *** Programm vom Band laden
.,F84A 20 17 F8 JSR $F817       wartet auf Play-Taste
.,F84D B0 1F    BCS $F86E       STOP-Taste gedrückt ?
.,F84F 78       SEI             Interrupt verhindern
.,F850 A9 00    LDA #$00        Arbeitsspeicher für IRQ-
                                Routine löschen
.,F852 85 AA    STA $AA         Eingabebytespeicher (read)
.,F854 85 B4    STA $B4         Band Hilfszeiger
.,F856 85 B0    STA $B0         Kassetten Zeitkonstante
.,F858 85 9E    STA $9E         Korrekturzähler Pass 1
.,F85A 85 9F    STA $9F         Korrekturzähler Pass 2
.,F85C 85 9C    STA $9C         Flag für Byte emfngen
.,F85E A9 90    LDA #$90        Bitwert IRQ an Pin 'Flag'
.,F860 A2 0E    LDX #$0E        Nummer des IRQ-Vektors, $F92C
.,F862 D0 11    BNE $F875       unbedingter Sprung

                                *** Bandpuffer auf Band schreiben
.,F864 20 D7 F7 JSR $F7D7       Bandpufferadresse holen
.,F867 A9 14    LDA #$14        Länge des Vorspanns vor WRITE
.,F869 85 AB    STA $AB         speichern

                                *** Block bzw. Programm auf Band
                                *** schreiben
.,F86B 20 38 F8 JSR $F838       wartet auf Record & Play
                                Taste
.,F86E B0 6C    BCS $F8DC       verzweige falls STOP-Taste
                                gedrückt
.,F870 78       SEI             Interrupt verhindern
.,F871 A9 82    LDA #$82        Bitwert für IRQ bei Unterlauf
                                von Timer B
.,F873 A2 08    LDX #$08        Nummer des IRQ-Vektors, $FC6A
.,F875 A0 7F    LDY #$7F        Bitwert für alle IRQs sperren
.,F877 8C 0D DC STY $DC0D       Wert schreiben
.,F87A 8D 0D DC STA $DC0D       und neu setzen
.,F87D AD 0E DC LDA $DC0E       Control Register A laden
.,F880 09 19    ORA #$19        Bitwert für one shot, starten
.,F882 8D 0F DC STA $DC0F       und ins Steuerregister für
                                Timer B
.,F885 29 91    AND #$91        Vergleichszeiger für Bandope-
.,F887 8D A2 02 STA $02A2       rationen entsprechend setzen
.,F88A 20 A4 F0 JSR $F0A4       auf Ende RS-232 Übertragung
                                warten
.,F88D AD 11 D0 LDA $D011       Bildschirm
.,F890 29 EF    AND #$EF        dunkel
.,F892 8D 11 D0 STA $D011       Tasten
.,F895 AD 14 03 LDA $0314       IRQ-Vector
.,F898 8D 9F 02 STA $029F       nach $029F
.,F89B AD 15 03 LDA $0315       und $02A0
.,F89E 8D A0 02 STA $02A0       speichern
.,F8A1 20 BD FC JSR $FCBD       IRQ-Vektor für Band I/O
                                setzen (X-indiziert)
.,F8A4 A9 02    LDA #$02        Anzahl der
.,F8A6 85 BE    STA $BE         zu lesenden Blöcke
.,F8A8 20 97 FB JSR $FB97       serielle Ausgabe vorbereiten
                                Bit-Zähler setzen
.,F8AB A5 01    LDA $01         Prozessorport laden
.,F8AD 29 1F    AND #$1F        Bandmotor einschalten
.,F8AF 85 01    STA $01         und wieder speichern
.,F8B1 85 C0    STA $C0         Flag für Bandmotor setzen
.,F8B3 A2 FF    LDX #$FF        HIGH-Byte für Zähler
.,F8B5 A0 FF    LDY #$FF        LOW-Byte für Zähler
.,F8B7 88       DEY             Verzögerungsschleife
.,F8B8 D0 FD    BNE $F8B7       für Bandhochlaufzeit
.,F8BA CA       DEX             HIGH-Byte veringern
.,F8BB D0 F8    BNE $F8B5       verzweige falls nicht Null
.,F8BD 58       CLI             Interrupt für Band I/O
                                freigeben

                                *** I/O Abschluß abwarten
.,F8BE AD A0 02 LDA $02A0       Band IRQ Vector mit normalem
.,F8C1 CD 15 03 CMP $0315       IRQ Vector vergleichen
.,F8C4 18       CLC             Carry =0 (ok Kennzeichen)
.,F8C5 F0 15    BEQ $F8DC       verzweige falls ja (fertig)
.,F8C7 20 D0 F8 JSR $F8D0       Testen auf Stop-Taste
.,F8CA 20 BC F6 JSR $F6BC       bei gedrückter Stop-Taste
                                Flag setzen
.,F8CD 4C BE F8 JMP $F8BE       weiter warten

                                *** testet auf Stop-Taste
.,F8D0 20 E1 FF JSR $FFE1       Stop-Taste abfragen
.,F8D3 18       CLC             Carry =0 (ok Kennzeichen)
.,F8D4 D0 0B    BNE $F8E1       verzweige wenn Taste nein
                                gedrückt
.,F8D6 20 93 FC JSR $FC93       Band-Motor aus, normalen
                                IRQ wiederherstellen
.,F8D9 38       SEC             Kennzeichen für Abbruch
.,F8DA 68       PLA             Rücksprung
.,F8DB 68       PLA             Adresse löschen
.,F8DC A9 00    LDA #$00        Kennzeichen für normalen
.,F8DE 8D A0 02 STA $02A0       IRQ setzen
.,F8E1 60       RTS             Rücksprung

                                *** Band für Lesen vorbereiten
.,F8E2 86 B1    STX $B1         X-Register speichern
.,F8E4 A5 B0    LDA $B0         Timing-Konstante laden
.,F8E6 0A       ASL             mit vier
.,F8E7 0A       ASL             multiplizieren
.,F8E8 18       CLC             zur Addition Carry löschen
.,F8E9 65 B0    ADC $B0         mit altem Wert addieren (*5)
.,F8EB 18       CLC             zur Addition Carry löschen
.,F8EC 65 B1    ADC $B1         alten X Wert dazuaddieren
.,F8EE 85 B1    STA $B1         und im Hilfszeiger speichern
.,F8F0 A9 00    LDA #$00        Akku löschen
.,F8F2 24 B0    BIT $B0         prüfe Timing-Konstante
.,F8F4 30 01    BMI $F8F7       verzweige, falls größer 128
.,F8F6 2A       ROL             Carry in die unterste
                                Position des Akkus schieben
.,F8F7 06 B1    ASL $B1         und Timer A
.,F8F9 2A       ROL             Initialisierung
.,F8FA 06 B1    ASL $B1         mit vier
.,F8FC 2A       ROL             multiplizieren
.,F8FD AA       TAX             Akku ins X-Register
.,F8FE AD 06 DC LDA $DC06       LOW-Byte Timer B laden
.,F901 C9 16    CMP #$16        mit $16 vergleichen
.,F903 90 F9    BCC $F8FE       verzweige, wenn kleiner
.,F905 65 B1    ADC $B1         LOW-Byte für Initialisierung
                                addieren
.,F907 8D 04 DC STA $DC04       Timer A LOW speichern
.,F90A 8A       TXA             HIGH-Byte für Initialisierung
.,F90B 6D 07 DC ADC $DC07       zu Timer B HIGH addieren
.,F90E 8D 05 DC STA $DC05       und in Timer A HIGH schreiben
.,F911 AD A2 02 LDA $02A2       Init. Wert für Band Zeitkon.
.,F914 8D 0E DC STA $DC0E       zum Starten von Timer A
.,F917 8D A4 02 STA $02A4       Timer A Flag zurücksetzten
.,F91A AD 0D DC LDA $DC0D       ICR laden
.,F91D 29 10    AND #$10        Bit isolieren
.,F91F F0 09    BEQ $F92A       verzweige wenn IRQ nicht vom
                                Pin Flag
.,F921 A9 F9    LDA #$F9        Rücksprungadresse
.,F923 48       PHA             auf
.,F924 A9 2A    LDA #$2A        Stack
.,F926 48       PHA             schieben
.,F927 4C 43 FF JMP $FF43       zum Interrupt
.,F92A 58       CLI             alle Interrupts freigeben
.,F92B 60       RTS             Rücksprung

                                *** Interrupt-Routine für Band
                                *** lesen
.,F92C AE 07 DC LDX $DC07       Timer B HIGH laden
.,F92F A0 FF    LDY #$FF        Y-Register mit $FF laden (für
                                Timer)
.,F931 98       TYA             in Akku schieben
.,F932 ED 06 DC SBC $DC06       Timer B von $FF abziehen
.,F935 EC 07 DC CPX $DC07       Timer B mit altem Wert
                                vergleichen
.,F938 D0 F2    BNE $F92C       verzweige, falls vermindert
.,F93A 86 B1    STX $B1         Timer B HIGH ablegen
.,F93C AA       TAX             und in Akku schieben
.,F93D 8C 06 DC STY $DC06       Timer B LOW und
.,F940 8C 07 DC STY $DC07       Timer B HIGH auf $FF setzen
.,F943 A9 19    LDA #$19        Arbeitsmodus für Timer B
.,F945 8D 0F DC STA $DC0F       festlegen und starten
.,F948 AD 0D DC LDA $DC0D       Interrupt Control Register
.,F94B 8D A3 02 STA $02A3       laden und nach $02A3
.,F94E 98       TYA             Y-REG in Akku ($FF)
.,F94F E5 B1    SBC $B1         Errechnung von vergangener
                                Zeit seit letzter Flanke
.,F951 86 B1    STX $B1         vergangene Zeit LOW nach $B1
.,F953 4A       LSR             vergangene Zeit
.,F954 66 B1    ROR $B1         HIGH
.,F956 4A       LSR             geteilt
.,F957 66 B1    ROR $B1         durch vier
.,F959 A5 B0    LDA $B0         Timingkonstante laden
.,F95B 18       CLC             und mit
.,F95C 69 3C    ADC #$3C        $3C addiert
.,F95E C5 B1    CMP $B1         errechnete Zeit größer als
                                die Zeit bei letzten Flanken
.,F960 B0 4A    BCS $F9AC       verzweige, wenn größer
.,F962 A6 9C    LDX $9C         Flag für empfangenes Byte
                                laden
.,F964 F0 03    BEQ $F969       verzweige, falls Null (Byte
                                nicht geladen)
.,F966 4C 60 FA JMP $FA60       ansonsten nach $FA60
.,F969 A6 A3    LDX $A3         Byte vollständig gelesen
.,F96B 30 1B    BMI $F988       verzweige, falls ja
.,F96D A2 00    LDX #$00        Code für kurzer Impuls (X=0)
.,F96F 69 30    ADC #$30        zu errechneter Zeit mit $30
.,F971 65 B0    ADC $B0         und mit Zeitkonstante
                                addieren
.,F973 C5 B1    CMP $B1         größer als Zeit beim letztem
                                Flanken ?
.,F975 B0 1C    BCS $F993       verzweige wenn größer
.,F977 E8       INX             sonst langer Impuls (X=1)
.,F978 69 26    ADC #$26        und wieder $26 und
.,F97A 65 B0    ADC $B0         Zeitkonstanten addieren
.,F97C C5 B1    CMP $B1         jetzt größer ?
.,F97E B0 17    BCS $F997       verzweige, falls ja
.,F980 69 2C    ADC #$2C        sonst wieder $2C und
.,F982 65 B0    ADC $B0         Zeitkonstante addieren
.,F984 C5 B1    CMP $B1         vergangene Zeit noch länger ?
.,F986 90 03    BCC $F98B       verzweige, wenn jetzt kürzer
.,F988 4C 10 FA JMP $FA10       zu empfangenes Byte verarbeiten
.,F98B A5 B4    LDA $B4         Flag für Timer A laden
.,F98D F0 1D    BEQ $F9AC       verzweige, wenn Timer A nicht
                                freigegeben
.,F98F 85 A8    STA $A8         Zeiger auf 'READ ERROR'
                                setzen
.,F991 D0 19    BNE $F9AC       unbedingter Sprung
.,F993 E6 A9    INC $A9         Zeiger auf Impulswechsel +1
.,F995 B0 02    BCS $F999       unbedingter Sprung
.,F997 C6 A9    DEC $A9         Zeiger auf Impulswechsel -1
.,F999 38       SEC             Carry für Subtraktion setzen
.,F99A E9 13    SBC #$13        Anfangswert ($13) und
.,F99C E5 B1    SBC $B1         vergangene Zeit subtrahieren
.,F99E 65 92    ADC $92         und mit Flag für Timing
                                Korrektur addieren
.,F9A0 85 92    STA $92         Ergebnis dort speichern
.,F9A2 A5 A4    LDA $A4         Flag für Empfang beider
.,F9A4 49 01    EOR #$01        Impulse invertieren
.,F9A6 85 A4    STA $A4         und abspeichern
.,F9A8 F0 2B    BEQ $F9D5       verzweige wenn beide Impulse
                                empfangen
.,F9AA 86 D7    STX $D7         empfangenes Signal speichern
.,F9AC A5 B4    LDA $B4         Flag für Timer A laden
.,F9AE F0 22    BEQ $F9D2       verzweige wenn Timer gesperrt
.,F9B0 AD A3 02 LDA $02A3       ICR in Akku
.,F9B3 29 01    AND #$01        Bit 0 isolieren
.,F9B5 D0 05    BNE $F9BC       verzweige wenn Interrupt von
                                Timer A
.,F9B7 AD A4 02 LDA $02A4       Timer A abgelaufen
.,F9BA D0 16    BNE $F9D2       nein, dann zum Interruptende
.,F9BC A9 00    LDA #$00        Impulszähler
.,F9BE 85 A4    STA $A4         löschen und
.,F9C0 8D A4 02 STA $02A4       Zeiger auf Timeout setzen
.,F9C3 A5 A3    LDA $A3         prüfe ob Byte vollständig
                                gelesen
.,F9C5 10 30    BPL $F9F7       verzweige falls nein
.,F9C7 30 BF    BMI $F988       unbedingter Sprung
.,F9C9 A2 A6    LDX #$A6        Initialisierungswert für
                                Timer A
.,F9CB 20 E2 F8 JSR $F8E2       Band zum Lesen vorbereiten
.,F9CE A5 9B    LDA $9B         Paritätsbyte in Akku
.,F9D0 D0 B9    BNE $F98B       verzweige falls parit. Fehler
.,F9D2 4C BC FE JMP $FEBC       Rückkehr vom Interrupt
.,F9D5 A5 92    LDA $92         Timing Korrekturzeiger laden
.,F9D7 F0 07    BEQ $F9E0       verzweige wenn Flag gelöscht
.,F9D9 30 03    BMI $F9DE       verzweige wenn kleiner Null
.,F9DB C6 B0    DEC $B0         Timing Konstante -1
.:F9DD 2C       .BYTE $2C       Skip zu $F9E0
.,F9DE E6 B0    INC $B0         Timing Konstante +1
.,F9E0 A9 00    LDA #$00        Timing
.,F9E2 85 92    STA $92         Korrekturzeiger löschen
.,F9E4 E4 D7    CPX $D7         Vergleiche empfangenen Impuls
                                mit vorherigem
.,F9E6 D0 0F    BNE $F9F7       verzweige falls ungleich
.,F9E8 8A       TXA             Prüfe ob kurzer Impuls
                                empfangen
.,F9E9 D0 A0    BNE $F98B       falls nein, verzweige
.,F9EB A5 A9    LDA $A9         Impulswechselzeiger laden
.,F9ED 30 BD    BMI $F9AC       verzweige wenn negativ
.,F9EF C9 10    CMP #$10        vergleiche mit $10
.,F9F1 90 B9    BCC $F9AC       verzweige wenn kleiner $10
.,F9F3 85 96    STA $96         sonst EOB Flag empfangen
.,F9F5 B0 B5    BCS $F9AC       unbedingter Sprung
.,F9F7 8A       TXA             Empfangenes Bit in Akku
.,F9F8 45 9B    EOR $9B         mit Band-Parität verknüpfen
.,F9FA 85 9B    STA $9B         in Band-Parität speichern
.,F9FC A5 B4    LDA $B4         Flag für Timer A laden
.,F9FE F0 D2    BEQ $F9D2       verzweige wenn nicht frei ge-
                                geben
.,FA00 C6 A3    DEC $A3         Speicher für Bitzähler -1
.,FA02 30 C5    BMI $F9C9       verzweige wenn Paritätsbit
                                empfangen
.,FA04 46 D7    LSR $D7         gelesenes Bit ins Carry und
.,FA06 66 BF    ROR $BF         dann in $BF rollen
.,FA08 A2 DA    LDX #$DA        Initialisierungswert für
                                Timer A ins X-Register
.,FA0A 20 E2 F8 JSR $F8E2       zur Kassettensynchronisation
.,FA0D 4C BC FE JMP $FEBC       Rückkehr vom Interrupt
.,FA10 A5 96    LDA $96         Prüfe ob EOB empfangen
.,FA12 F0 04    BEQ $FA18       falls nein, verzweige
.,FA14 A5 B4    LDA $B4         Prüfe ob Timer A freige.
.,FA16 F0 07    BEQ $FA1F       wenn nein, überspringe Bit
                                Zähler Test
.,FA18 A5 A3    LDA $A3         Bitzähler laden
.,FA1A 30 03    BMI $FA1F       verzweige falls negatv
.,FA1C 4C 97 F9 JMP $F997       langen Impuls verarbeiten
.,FA1F 46 B1    LSR $B1         vergangene Zeit seit letztem
                                Flangen halbieren
.,FA21 A9 93    LDA #$93        und diesen Wert
.,FA23 38       SEC             von $93
.,FA24 E5 B1    SBC $B1         abziehen
.,FA26 65 B0    ADC $B0         dazu dann Timing-Konstante
                                addieren
.,FA28 0A       ASL             und Ergebnis verdoppeln
.,FA29 AA       TAX             Ergebnis ins X-Register
.,FA2A 20 E2 F8 JSR $F8E2       Timing initialisieren
.,FA2D E6 9C    INC $9C         Flag für Byte empfangen
                                setzen
.,FA2F A5 B4    LDA $B4         Flag für Timer A laden
.,FA31 D0 11    BNE $FA44       verzweige falls freigegeben
.,FA33 A5 96    LDA $96         wurde EOB emfangen ?
.,FA35 F0 26    BEQ $FA5D       verzweige wenn nicht
                                empfangen
.,FA37 85 A8    STA $A8         Flag für Lesefehler setzen
.,FA39 A9 00    LDA #$00        Flag für
.,FA3B 85 96    STA $96         EOB rücksetzen
.,FA3D A9 81    LDA #$81        Interrupt für
.,FA3F 8D 0D DC STA $DC0D       Timer A freigeben
.,FA42 85 B4    STA $B4         und Flag für Timer A setzen
.,FA44 A5 96    LDA $96         Flag für EOB laden
.,FA46 85 B5    STA $B5         und nach $B5 kopieren
.,FA48 F0 09    BEQ $FA53       verzweige wenn kein EOB
.,FA4A A9 00    LDA #$00        Flag für Timer A
.,FA4C 85 B4    STA $B4         löschen und auch
.,FA4E A9 01    LDA #$01        Interruptflag
.,FA50 8D 0D DC STA $DC0D       wieder löschen
.,FA53 A5 BF    LDA $BF         Shift Register für Read laden
.,FA55 85 BD    STA $BD         und nach $BD bringen
.,FA57 A5 A8    LDA $A8         Flag für Lesefehler laden
.,FA59 05 A9    ORA $A9         mit Impulswechselzeiger
.,FA5B 85 B6    STA $B6         verknüpfen und in Fehlercode
                                des Bytes ablegen
.,FA5D 4C BC FE JMP $FEBC       Rückkehr vom Interrupt
.,FA60 20 97 FB JSR $FB97       Bitzähler für serielle
                                Ausgabe setzen
.,FA63 85 9C    STA $9C         Zeiger auf Byte empfangen
                                rücksetzen
.,FA65 A2 DA    LDX #$DA        Initialisierungswert Timer A
.,FA67 20 E2 F8 JSR $F8E2       Kassettensynchronisation
.,FA6A A5 BE    LDA $BE         Anzahl der verbliebenen
                                Blöcke laden
.,FA6C F0 02    BEQ $FA70       verzweige wenn Null
.,FA6E 85 A7    STA $A7         Blockanzahl neu setzen
.,FA70 A9 0F    LDA #$0F        Maskenwert für Zählung vor
                                dem Lesen
.,FA72 24 AA    BIT $AA         Prüfe Zeiger für Lesen von
                                Band
.,FA74 10 17    BPL $FA8D       verzweige wenn alle Zeichen
                                empfangen (Ende)
.,FA76 A5 B5    LDA $B5         Flag für EOB laden
.,FA78 D0 0C    BNE $FA86       verzweige wenn gültiges EOB
                                empfangen
.,FA7A A6 BE    LDX $BE         Anzahl der verbliebenen
                                Blöcke laden
.,FA7C CA       DEX             Anzahl -1
.,FA7D D0 0B    BNE $FA8A       verzweige wenn nicht Null
.,FA7F A9 08    LDA #$08        'LONG BLOCK' error
.,FA81 20 1C FE JSR $FE1C       Status setzen
.,FA84 D0 04    BNE $FA8A       unbedingter Sprung zum
                                normalen IRQ
.,FA86 A9 00    LDA #$00        Flag für Lesen vom Band auf
.,FA88 85 AA    STA $AA         Abtastung setzen
.,FA8A 4C BC FE JMP $FEBC       Rückkehr vom Interrupt
.,FA8D 70 31    BVS $FAC0       verzweige wenn Bandzeiger auf
                                lesen
.,FA8F D0 18    BNE $FAA9       verzweige wenn Bandzeiger
                                auf Zählen
.,FA91 A5 B5    LDA $B5         Flag für EOB laden
.,FA93 D0 F5    BNE $FA8A       verzweige wenn EOB empfangen
.,FA95 A5 B6    LDA $B6         Flag für Lesefehler laden
.,FA97 D0 F1    BNE $FA8A       verzweige falls Fehler
                                aufgetreten
.,FA99 A5 A7    LDA $A7         Anzahl der noch zu lesenden
                                Blöcke holen
.,FA9B 4A       LSR             Bit 0 ins Carry schieben
.,FA9C A5 BD    LDA $BD         hole gelesenes Byte
.,FA9E 30 03    BMI $FAA3       verzweige wenn es Zählbyte
                                ist
.,FAA0 90 18    BCC $FABA       verzweige wenn mehr als ein
                                Block zu lesen
.,FAA2 18       CLC             lösche Carry um nicht zu
                                verzweigen
.,FAA3 B0 15    BCS $FABA       verzweige falls nur ein Block
                                zu lesen
.,FAA5 29 0F    AND #$0F        Bits 0 bis 3 isolieren
.,FAA7 85 AA    STA $AA         und für Zählung speichern
.,FAA9 C6 AA    DEC $AA         alle Synchrrnisationsbytes
                                empfangen
.,FAAB D0 DD    BNE $FA8A       wenn nein verzweige
.,FAAD A9 40    LDA #$40        Bandzeiger auf
.,FAAF 85 AA    STA $AA         lesen stellen
.,FAB1 20 8E FB JSR $FB8E       Ein/Ausgabe Adresse kopieren
.,FAB4 A9 00    LDA #$00        Flag für
.,FAB6 85 AB    STA $AB         Leseprüfsumme löschen
.,FAB8 F0 D0    BEQ $FA8A       unbedingter Sprung
.,FABA A9 80    LDA #$80        Bandzeiger
.,FABC 85 AA    STA $AA         auf Ende stellen
.,FABE D0 CA    BNE $FA8A       unbedingter Sprung
.,FAC0 A5 B5    LDA $B5         Flag für EOB laden
.,FAC2 F0 0A    BEQ $FACE       verzweige wenn nicht gesetzt
.,FAC4 A9 04    LDA #$04        'SHORT BLOCK’ error
.,FAC6 20 1C FE JSR $FE1C       Status setzen
.,FAC9 A9 00    LDA #$00        Code für Lesezeiger auf
                                "Abtasten"
.,FACB 4C 4A FB JMP $FB4A       setzen, unbedingter Sprung
.,FACE 20 D1 FC JSR $FCD1       Endadresse schon erreicht ?
.,FAD1 90 03    BCC $FAD6       nein dann verzweige
.,FAD3 4C 48 FB JMP $FB48       zu Read Ende für Block
.,FAD6 A6 A7    LDX $A7         nur noch
.,FAD8 CA       DEX             ein Block zu lesen
.,FAD9 F0 2D    BEQ $FB08       verzweige wenn ja (Pass 2)
.,FADB A5 93    LDA $93         Load/Verify-Flag
.,FADD F0 0C    BEQ $FAEB       verzweige wenn Load
.,FADF A0 00    LDY #$00        Zähler auf Null setzen
.,FAE1 A5 BD    LDA $BD         gelesenes Byte
.,FAE3 D1 AC    CMP ($AC),Y     vergleichen
.,FAE5 F0 04    BEQ $FAEB       verzweige wenn Übereinstim-
                                mung
.,FAE7 A9 01    LDA #$01        Fehlerflag
.,FAE9 85 B6    STA $B6         setzen
.,FAEB A5 B6    LDA $B6         Fehlerflag laden
.,FAED F0 4B    BEQ $FB3A       verzweige wenn kein Fehler
                                aufgetreten
.,FAEF A2 3D    LDX #$3D        bereits 31 Fehler
.,FAF1 E4 9E    CPX $9E         aufgetreten
.,FAF3 90 3E    BCC $FB33       verzweige wenn weniger Fehler
.,FAF5 A6 9E    LDX $9E         Index für Lesefehler
.,FAF7 A5 AD    LDA $AD         laufender Adressbyte HIGH
.,FAF9 9D 01 01 STA $0101,X     im Stack speichern
.,FAFC A5 AC    LDA $AC         Adressbyte LOW
.,FAFE 9D 00 01 STA $0100,X     für spätere Korrektur
                                ebenfalls im Stack speichern
.,FB01 E8       INX             Zeiger auf nachfolgende
.,FB02 E8       INX             freie Stelle setzen
.,FB03 86 9E    STX $9E         und abspeichern
.,FB05 4C 3A FB JMP $FB3A       weitermachen
.,FB08 A6 9F    LDX $9F         bereits alle Lesefehler
.,FB0A E4 9E    CPX $9E         korrigiert ?
.,FB0C F0 35    BEQ $FB43       verzweige falls ja
.,FB0E A5 AC    LDA $AC         Adressbyte LOW laden
.,FB10 DD 00 01 CMP $0100,X     mit fehlerhaftem Adressbyte
                                LOW vergleichen
.,FB13 D0 2E    BNE $FB43       verzweige falls nicht
                                gefunden
.,FB15 A5 AD    LDA $AD         Adressbyte HIGH laden
.,FB17 DD 01 01 CMP $0101,X     mit fehlerhaftem Adressbyte
                                HIGH vergleichen
.,FB1A D0 27    BNE $FB43       verzweige wenn nicht gefunden
.,FB1C E6 9F    INC $9F         Korrekturzähler
.,FB1E E6 9F    INC $9F         Pass 2 um zwei erhöhen
.,FB20 A5 93    LDA $93         Verify-Flag gesetzt
.,FB22 F0 0B    BEQ $FB2F       verzweige wenn nicht gesetzt
.,FB24 A5 BD    LDA $BD         gelesenes Byte laden
.,FB26 A0 00    LDY #$00        Zähler auf Null setzen
.,FB28 D1 AC    CMP ($AC),Y     mit Speicherinhalt verglei-
                                chen
.,FB2A F0 17    BEQ $FB43       verzweige wenn gleich, dann
                                nächstes Byte
.,FB2C C8       INY             Flag für
.,FB2D 84 B6    STY $B6         Fehler setzen
.,FB2F A5 B6    LDA $B6         Fehlerflag testen
.,FB31 F0 07    BEQ $FB3A       verzweige wenn kein Fehler
.,FB33 A9 10    LDA #$10        'SECOND PASS' error
.,FB35 20 1C FE JSR $FE1C       Status setzen
.,FB38 D0 09    BNE $FB43       und nächstes Byte verarbeiten
.,FB3A A5 93    LDA $93         Verify-Flag laden
.,FB3C D0 05    BNE $FB43       verzweige wenn gesetzt
.,FB3E A8       TAY             Zeiger löschen
.,FB3F A5 BD    LDA $BD         gelesenes Byte
.,FB41 91 AC    STA ($AC),Y     speichern
.,FB43 20 DB FC JSR $FCDB       Adresszeiger erhöhen
.,FB46 D0 43    BNE $FB8B       Rückkehr vom Interrupt
.,FB48 A9 80    LDA #$80        Flag für Lesen
.,FB4A 85 AA    STA $AA         auf Ende
.,FB4C 78       SEI             Interrupt verhindern
.,FB4D A2 01    LDX #$01        IRQ vom
.,FB4F 8E 0D DC STX $DC0D       Timer A verhindern
.,FB52 AE 0D DC LDX $DC0D       IRQ-Flag löschen
.,FB55 A6 BE    LDX $BE         Pass-Zähler
.,FB57 CA       DEX             erniedrigen
.,FB58 30 02    BMI $FB5C       verzweige wenn Null gewesen
.,FB5A 86 BE    STX $BE         Passzähler merken
.,FB5C C6 A7    DEC $A7         Blockzähler vermindern
.,FB5E F0 08    BEQ $FB68       verzweige wenn Null
.,FB60 A5 9E    LDA $9E         Fehler in Pass 1 aufgetre-
                                ten ?
.,FB62 D0 27    BNE $FB8B       ja, Rückkehr vom Interrupt
.,FB64 85 BE    STA $BE         kein Block mehr zu verarbei-
                                ten
.,FB66 F0 23    BEQ $FB8B       Rückkehr vom Interrupt
.,FB68 20 93 FC JSR $FC93       ein Pass beendet
.,FB6B 20 8E FB JSR $FB8E       Adresse wieder auf Programm-
                                anfang
.,FB6E A0 00    LDY #$00        Zähler auf Null setzen
.,FB70 84 AB    STY $AB         Checksumme löschen
.,FB72 B1 AC    LDA ($AC),Y     Programm
.,FB74 45 AB    EOR $AB         Checksumme berechnen
.,FB76 85 AB    STA $AB         und speichern
.,FB78 20 DB FC JSR $FCDB       Adresszeiger erhöhen
.,FB7B 20 D1 FC JSR $FCD1       Endadresse schon erreicht ?
.,FB7E 90 F2    BCC $FB72       nein, weiter vergleichen
.,FB80 A5 AB    LDA $AB         berechnete Checksumme
.,FB82 45 BD    EOR $BD         mit Checksumme vom Band
                                vergleichen
.,FB84 F0 05    BEQ $FB8B       Checksumme gleich , dann ok
.,FB86 A9 20    LDA #$20        'CHECKSUM' error
.,FB88 20 1C FE JSR $FE1C       Status setzen
.,FB8B 4C BC FE JMP $FEBC       Rückkehr vom Interrupt

                                *** laufenden Zeiger auf
                                *** Programmstart
.,FB8E A5 C2    LDA $C2         Startadresse
.,FB90 85 AD    STA $AD         $C1/$C2
.,FB92 A5 C1    LDA $C1         nach $AC/$AD
.,FB94 85 AC    STA $AC         speichern
.,FB96 60       RTS             Rücksprung

                                *** Bitzähler für serielle
                                *** Ausgabe setzen
.,FB97 A9 08    LDA #$08        Zähler für 8 Bits
.,FB99 85 A3    STA $A3         Nach $A3
.,FB9B A9 00    LDA #$00        Akku mit $00 laden
.,FB9D 85 A4    STA $A4         Bit-Impuls-Flag löschen
.,FB9F 85 A8    STA $A8         Lesefehler Byte löschen
.,FBA1 85 9B    STA $9B         Parity-Bit löschen
.,FBA3 85 A9    STA $A9         Impulswechsel-Flag löschen
.,FBA5 60       RTS             Rücksprung

                                *** Ein Bit auf Band schreiben
.,FBA6 A5 BD    LDA $BD         Bit in $BD
.,FBA8 4A       LSR             Bit 0 in Carry
.,FBA9 A9 60    LDA #$60        Zeit für '0' Bit
.,FBAB 90 02    BCC $FBAF       verzweige falls Carry=0
.,FBAD A9 B0    LDA #$B0        Zeit für '1' Bit
.,FBAF A2 00    LDX #$00        HIGH-Byte Timerwert laden
.,FBB1 8D 06 DC STA $DC06       Timer B LOW
.,FBB4 8E 07 DC STX $DC07       Timer B HIGH
.,FBB7 AD 0D DC LDA $DC0D       Interrupt-Flag löschen
.,FBBA A9 19    LDA #$19        Timer
.,FBBC 8D 0F DC STA $DC0F       B starten
.,FBBF A5 01    LDA $01         Tape-Write-Bit laden
.,FBC1 49 08    EOR #$08        Ausgabe-Bit für Band
                                invertieren
.,FBC3 85 01    STA $01         und speichern
.,FBC5 29 08    AND #$08        augenblicklichen Pegel merken
.,FBC7 60       RTS
.,FBC8 38       SEC             Block-Write-Flag
.,FBC9 66 B6    ROR $B6         Negativ
.,FBCB 30 3C    BMI $FC09       Rückkehr vom Interrupt

                                *** Interrupt-Routine für Band
                                *** schreiben
.,FBCD A5 A8    LDA $A8         falls 'Byte'-Impuls ge-
.,FBCF D0 12    BNE $FBE3       schrieben, dann verzweige
.,FBD1 A9 10    LDA #$10        Timer auf
.,FBD3 A2 01    LDX #$01        $110 (272)
.,FBD5 20 B1 FB JSR $FBB1       Takt auf Band schreiben
.,FBD8 D0 2F    BNE $FC09       Rückkehr vom Interrupt
.,FBDA E6 A8    INC $A8         '1' Byte-Write-Flag setzen
.,FBDC A5 B6    LDA $B6         falls Block-Write-Flag
                                positiv, dann
.,FBDE 10 29    BPL $FC09       Rückkehr vom Interrupt
.,FBE0 4C 57 FC JMP $FC57       zweiten Block schreiben
.,FBE3 A5 A9    LDA $A9         falls '1' Bit gesezt
.,FBE5 D0 09    BNE $FBF0       dann verzweige
.,FBE7 20 AD FB JSR $FBAD       '1' Bit schreiben
.,FBEA D0 1D    BNE $FC09       Rückkehr vom Interrupt
.,FBEC E6 A9    INC $A9         '1' Bit-Flag setzen
.,FBEE D0 19    BNE $FC09       Rückkehr vom Interrupt
.,FBF0 20 A6 FB JSR $FBA6       Bit auf Band schreiben
.,FBF3 D0 14    BNE $FC09       Rückkehr vom Interrupt
.,FBF5 A5 A4    LDA $A4         Bit-Impulsflag laden
.,FBF7 49 01    EOR #$01        Bit 0 invertieren
.,FBF9 85 A4    STA $A4         und speichern
.,FBFB F0 0F    BEQ $FC0C       falls null, dann verzweige
.,FBFD A5 BD    LDA $BD         Bit-SHIFT-Register laden
.,FBFF 49 01    EOR #$01        Bit für Ausgabe invertieren
.,FC01 85 BD    STA $BD         und speichern
.,FC03 29 01    AND #$01        Bit holen und mit
.,FC05 45 9B    EOR $9B         Parity-Bit verknüpfen
.,FC07 85 9B    STA $9B         und speichern
.,FC09 4C BC FE JMP $FEBC       Rückkehr vom Interrupt
.,FC0C 46 BD    LSR $BD         nächstes Bit in Position 0
.,FC0E C6 A3    DEC $A3         Bitzähler erniedrigen
.,FC10 A5 A3    LDA $A3         und laden
.,FC12 F0 3A    BEQ $FC4E       nächstes Bit ausgeben
.,FC14 10 F3    BPL $FC09       Rückkehr vom Interrupt
.,FC16 20 97 FB JSR $FB97       Bitzähler wieder auf 8 setzen
.,FC19 58       CLI             Interrupt freigeben
.,FC1A A5 A5    LDA $A5         Falls Synchronbytes geschrie-
                                ben
.,FC1C F0 12    BEQ $FC30       dann verzweige
.,FC1E A2 00    LDX #$00        Prüfsumme
.,FC20 86 D7    STX $D7         löschen
.,FC22 C6 A5    DEC $A5         Zähler vermindern
.,FC24 A6 BE    LDX $BE         noch zu schreibende
                                Blockanzahl laden
.,FC26 E0 02    CPX #$02        falls erster Block nicht
.,FC28 D0 02    BNE $FC2C       geschrieben, dann verzweige
.,FC2A 09 80    ORA #$80        Bit 7 setzen
.,FC2C 85 BD    STA $BD         und speichern
.,FC2E D0 D9    BNE $FC09       Rückkehr vom Interrupt
.,FC30 20 D1 FC JSR $FCD1       Endadresse schon erreicht ?
.,FC33 90 0A    BCC $FC3F       falls kleiner, dann
                                weiterschreiben
.,FC35 D0 91    BNE $FBC8       falls ungleich, dann
                                Block-Write-Flag setzen
.,FC37 E6 AD    INC $AD         HIGH-Byte ungleich machen
.,FC39 A5 D7    LDA $D7         Prüfsumme laden
.,FC3B 85 BD    STA $BD         und in SHIFT-Flag speichern
.,FC3D B0 CA    BCS $FC09       Rückkehr vom Interrupt
.,FC3F A0 00    LDY #$00        Zähler auf Null
.,FC41 B1 AC    LDA ($AC),Y     zu schreibendes Byte laden
.,FC43 85 BD    STA $BD         in SHIFT-Flag bringen
.,FC45 45 D7    EOR $D7         Prüfsumme
.,FC47 85 D7    STA $D7         bilden
.,FC49 20 DB FC JSR $FCDB       Adresszeiger erhöhen
.,FC4C D0 BB    BNE $FC09       Rückkehr vom Interrupt
.,FC4E A5 9B    LDA $9B         Parity-Bit
.,FC50 49 01    EOR #$01        invertieren
.,FC52 85 BD    STA $BD         und ins SHIFT-Flag speichern
.,FC54 4C BC FE JMP $FEBC       Rückkehr vom Interrupt
.,FC57 C6 BE    DEC $BE         Zähler für Blocks erniedrigen
.,FC59 D0 03    BNE $FC5E       falls noch ein Block,
.,FC5B 20 CA FC JSR $FCCA       dann Bandmotor aus
.,FC5E A9 50    LDA #$50        80
.,FC60 85 A7    STA $A7         Zähler für Impulse
.,FC62 A2 08    LDX #$08        Offset für IRQ
.,FC64 78       SEI             Interrupt verhindern
.,FC65 20 BD FC JSR $FCBD       IRQ auf $FC6A
.,FC68 D0 EA    BNE $FC54       Rückkehr vom Interrupt

                                *** Interrupt-Routine für Band
                                *** schreiben
.,FC6A A9 78    LDA #$78        120
.,FC6C 20 AF FB JSR $FBAF       Bit auf Band schreiben
.,FC6F D0 E3    BNE $FC54       Rückkehr vom Interrupt
.,FC71 C6 A7    DEC $A7         Zähler erniedrigen
.,FC73 D0 DF    BNE $FC54       nicht null, dann Rückkehr
                                vom Interrupt
.,FC75 20 97 FB JSR $FB97       Bitzähler für serielle
                                Ausgabe setzen
.,FC78 C6 AB    DEC $AB         falls Datenende nicht er-
                                reicht, dann
.,FC7A 10 D8    BPL $FC54       Rückkehr vom Interrupt
.,FC7C A2 0A    LDX #$0A        IRQ
.,FC7E 20 BD FC JSR $FCBD       IRQ auf $FBCD
.,FC81 58       CLI             Interrupt ermöglichen
.,FC82 E6 AB    INC $AB         Shortdauer
.,FC84 A5 BE    LDA $BE         Zähler für Anzahl der Blocks
.,FC86 F0 30    BEQ $FCB8       alle Blocks geschrieben ?
.,FC88 20 8E FB JSR $FB8E       Adresse wieder auf Anfang
                                setzen
.,FC8B A2 09    LDX #$09        Zähler für
.,FC8D 86 A5    STX $A5         Synchronisation
.,FC8F 86 B6    STX $B6         Flag für Block geschrieben
.,FC91 D0 83    BNE $FC16       unbedingter Sprung

                                *** Rekorderbetrieb beenden
.,FC93 08       PHP             Status merken
.,FC94 78       SEI             Interrupt verhindern
.,FC95 AD 11 D0 LDA $D011       Bildschirm
.,FC98 09 10    ORA #$10        wieder
.,FC9A 8D 11 D0 STA $D011       einschalten
.,FC9D 20 CA FC JSR $FCCA       Rekordermotor ausschalten
.,FCA0 A9 7F    LDA #$7F        Interruptmöglichkeiten
.,FCA2 8D 0D DC STA $DC0D       löschen
.,FCA5 20 DD FD JSR $FDDD       CIA wieder auf Standardwerte,
                                1/60 s Timing
.,FCA8 AD A0 02 LDA $02A0       Interruptvektor schon auf
                                Standardwert ?
.,FCAB F0 09    BEQ $FCB6       falls ja, dann fertig
.,FCAD 8D 15 03 STA $0315       ansonsten zurücksetzen
.,FCB0 AD 9F 02 LDA $029F       geretteten lRQ zurückholen
.,FCB3 8D 14 03 STA $0314       und speichern
.,FCB6 28       PLP             Status zurückholen
.,FCB7 60       RTS             Rücksprung

                                *** IRQ-Vektor setzen,
                                *** X-indiziert
.,FCB8 20 93 FC JSR $FC93       IRQ auf Standard
.,FCBB F0 97    BEQ $FC54       Abschluß IRQ
.,FCBD BD 93 FD LDA $FD93,X     IRQ-Vektor
.,FCC0 8D 14 03 STA $0314       aus Tabelle setzen
.,FCC3 BD 94 FD LDA $FD94,X     lRQ-Vektor
.,FCC6 8D 15 03 STA $0315       aus Tabelle setzen
.,FCC9 60       RTS             Rücksprung
.,FCCA A5 01    LDA $01         Rekorder-
.,FCCC 09 20    ORA #$20        motor
.,FCCE 85 01    STA $01         ausschalten
.,FCD0 60       RTS             Rücksprung

                                *** prüft auf Erreichen der
                                *** Endadresse
.,FCD1 38       SEC             Carry für Subtraktion
                                vorbereiten
.,FCD2 A5 AC    LDA $AC         laufende Adresse
.,FCD4 E5 AE    SBC $AE         $AC/$AD
.,FCD6 A5 AD    LDA $AD         Endadresse
.,FCD8 E5 AF    SBC $AF         $AE/$AF
.,FCDA 60       RTS             Rücksprung
.,FCDB E6 AC    INC $AC         Adreßzeiger
.,FCDD D0 02    BNE $FCE1       er-
.,FCDF E6 AD    INC $AD         höhen
.,FCE1 60       RTS             Rücksprung

                                *** RESET
.,FCE2 A2 FF    LDX #$FF        Wert für Stapelzeiger
.,FCE4 78       SEI             Interrupt setzen
.,FCE5 9A       TXS             Stapelzeiger initialisieren
.,FCE6 D8       CLD             Dezimalflag zurücksetzen
.,FCE7 20 02 FD JSR $FD02       prüft auf ROM in $8000
.,FCEA D0 03    BNE $FCEF       kein Autostart-Modul ?
.,FCEC 6C 00 80 JMP ($8000)     Sprung auf Modul-Start
.,FCEF 8E 16 D0 STX $D016       Videocontroller Steuerreg. 2
.,FCF2 20 A3 FD JSR $FDA3       Interrupt vorbereiten
.,FCF5 20 50 FD JSR $FD50       Arbeitsspeicher initialisieren
.,FCF8 20 15 FD JSR $FD15       Hardware und I/O Vekt. setzen
.,FCFB 20 5B FF JSR $FF5B       Video-Reset
.,FCFE 58       CLI
.,FCFF 6C 00 A0 JMP ($A000)     zum BASIC Kaltstart

                                *** prüft auf ROM in $8000
.,FD02 A2 05    LDX #$05        Zeiger setzen
.,FD04 BD 0F FD LDA $FD0F,X     Wert aus Tabelle holen und
.,FD07 DD 03 80 CMP $8003,X     ab $8000 vergleichen (CBM80)
.,FD0A D0 03    BNE $FD0F       verzweige wenn ungleich
.,FD0C CA       DEX             Zeiger vermindern
.,FD0D D0 F5    BNE $FD04       weiter wenn nicht 5 Bytes
.,FD0F 60       RTS             Rücksprung

                                *** ROM-Modul Identifizierung
.:FD10 C3 C2 CD 38 30           'CBM80’

                                *** Hardware und I/O Vektoren
                                *** setzen/holen
.,FD15 A2 30    LDX #$30        LOW- und HIGH-Byte des
.,FD17 A0 FD    LDY #$FD        Zeigers auf Tabelle $FD30
.,FD19 18       CLC             Flag für 'Vektoren setzen'
.,FD1A 86 C3    STX $C3         LOW- und HIGH-Byte
.,FD1C 84 C4    STY $C4         des Zeigers setzen
.,FD1E A0 1F    LDY #$1F        Zeiger setzen (16 Vektoren)
.,FD20 B9 14 03 LDA $0314,Y     Wert aus Tabelle holen
.,FD23 B0 02    BCS $FD27       C=1 holen,C=0 setzen
.,FD25 B1 C3    LDA ($C3),Y     Tabellenwert holen
.,FD27 91 C3    STA ($C3),Y     Tabellenwert setzen
.,FD29 99 14 03 STA $0314,Y     Wert in Tabelle ablegen
.,FD2C 88       DEY             Zähler vermindern
.,FD2D 10 F1    BPL $FD20       Fertig? nein: nächster Wert
.,FD2F 60       RTS             Rücksprung

                                *** Tabelle der Hardware
                                *** und I/O-Vektoren
.:FD30 31 EA 66 FE 47 FE 4A F3
.:FD38 91 F2 0E F2 50 F2 33 F3
.:FD40 57 F1 CA F1 ED F6 3E F1
.:FD48 2F F3 66 FE A5 F4 ED F5

                                *** Arbeitsspei. initialisieren
.,FD50 A9 00    LDA #$00        Wert zum Löschen laden
.,FD52 A8       TAY             als Zähler nach Y
.,FD53 99 02 00 STA $0002,Y     Zeropage,
.,FD56 99 00 02 STA $0200,Y     Page 2 und
.,FD59 99 00 03 STA $0300,Y     Page 3 löschen
.,FD5C C8       INY             Zähler vermindern
.,FD5D D0 F4    BNE $FD53       weiter wenn nicht fertig
.,FD5F A2 3C    LDX #$3C        Werte für Startadresse
.,FD61 A0 03    LDY #$03        des Bandpuffers laden
.,FD63 86 B2    STX $B2         Bandpuffer Zeiger
.,FD65 84 B3    STY $B3         auf $033C setzen
.,FD67 A8       TAY             Zeiger in Y auf 0 setzen
.,FD68 A9 03    LDA #$03        Wert für RAM testen ($04-1)
.,FD6A 85 C2    STA $C2         Startadresse (HIGH) des RAM
.,FD6C E6 C2    INC $C2         setzen und auf $0400 erhöhen
.,FD6E B1 C1    LDA ($C1),Y     Wert holen
.,FD70 AA       TAX             Wert merken
.,FD71 A9 55    LDA #$55        %01010101 ($55)
.,FD73 91 C1    STA ($C1),Y     abspeichern und über-
.,FD75 D1 C1    CMP ($C1),Y     prüfen, ob Wert drin ist
.,FD77 D0 0F    BNE $FD88       ungleich dann kein RAM
.,FD79 2A       ROL             %10101010
.,FD7A 91 C1    STA ($C1),Y     Wert abspeichern und
.,FD7C D1 C1    CMP ($C1),Y     überprüfen, ob Wert drin ist
.,FD7E D0 08    BNE $FD88       ungleich dann kein RAM
.,FD80 8A       TXA             Wert wieder zurückholen
.,FD81 91 C1    STA ($C1),Y     und wieder zurückschreiben
.,FD83 C8       INY             Zeiger erhöhen
.,FD84 D0 E8    BNE $FD6E       Pageende? nein: weiter
.,FD86 F0 E4    BEQ $FD6C       sonst Zeiger-HIGH erhöhen
.,FD88 98       TYA             Zeiger-LOW ins
.,FD89 AA       TAX             X-Register bringen
.,FD8A A4 C2    LDY $C2         Zeiger-HIGH holen
.,FD8C 18       CLC             C=0 (Flag für setzen)
.,FD8D 20 2D FE JSR $FE2D       Memory (RAM) Top setzen
.,FD90 A9 08    LDA #$08        HIGH-Byte der Startadresse
.,FD92 8D 82 02 STA $0282       Memory (RAM) Start auf $800
.,FD95 A9 04    LDA #$04        HIGH-Byte der Startadresse
.,FD97 8D 88 02 STA $0288       Video-RAM auf $400
.,FD9A 60       RTS             Rücksprung

                                *** IRQ Vektoren
.:FD9B 6A FC CD FB 31 EA 2C F9  $FC6A, $FBCD, $EA31, $F92C

                                *** Interrupt Initialisierung
.,FDA3 A9 7F    LDA #$7F        Interrupt löschen
.,FDA5 8D 0D DC STA $DC0D       ICR CIA 1
.,FDA8 8D 0D DD STA $DD0D       ICR CIA 2
                                Port A CIA 1
.,FDAB 8D 00 DC STA $DC00       Tastatur Matrixzeile 0
.,FDAE A9 08    LDA #$08        Wert laden
.,FDB0 8D 0E DC STA $DC0E       CRA CIA 1 Timer A 'one shot'
.,FDB3 8D 0E DD STA $DD0E       CRA CIA 2 Timer A 'one shot'
.,FDB6 8D 0F DC STA $DC0F       CRB CIA 1 Timer B 'one shot'
.,FDB9 8D 0F DD STA $DD0F       CRB CIA 2 Timer B 'one shot'
.,FDBC A2 00    LDX #$00        Eingangs-Modus
.,FDBE 8E 03 DC STX $DC03       Datenrichtungsreg. B CIA 1
.,FDC1 8E 03 DD STX $DD03       Datenrichtungsreg. B CIA 2
.,FDC4 8E 18 D4 STX $D418       Lautstärke für SID auf Null
.,FDC7 CA       DEX             Ausgabe-Modus
.,FDC8 8E 02 DC STX $DC02       Datenrichtungsreg. A CIA 1
.,FDCB A9 07    LDA #$07        Videocontroller auf
                                unterste 16 K
.,FDCD 8D 00 DD STA $DD00       Port A CIA 2, ATN löschen
.,FDD0 A9 3F    LDA #$3F        Bit 0 bis 5 auf Ausgabe
.,FDD2 8D 02 DD STA $DD02       Datenrichtungsreg. A CIA 2
.,FDD5 A9 E7    LDA #$E7        Normalwert laden und
.,FDD7 85 01    STA $01         Speicheraufteilung neu setzen
.,FDD9 A9 2F    LDA #$2F        Bit 0-3 und 5 Ausgang,
                                Bit 4 Eingang
.,FDDB 85 00    STA $00         Datenrichtung Prozessorport
.,FDDD AD A6 02 LDA $02A6       NTSC-Version ?
.,FDE0 F0 0A    BEQ $FDEC       ja
.,FDE2 A9 25    LDA #$25        Wert für PAL-Version
.,FDE4 8D 04 DC STA $DC04       Timer für PAL-Version setzen
.,FDE7 A9 40    LDA #$40        $4025 = 16421 Zyklen
.,FDE9 4C F3 FD JMP $FDF3       NTSC-Version übergehen
.,FDEC A9 95    LDA #$95        Wert für NTSC-Version
.,FDEE 8D 04 DC STA $DC04       Timer für NTSC-Version setzen
.,FDF1 A9 42    LDA #$42        $4295 = 17045 Zyklen
.,FDF3 8D 05 DC STA $DC05       Timer-HIGH setzen
.,FDF6 4C 6E FF JMP $FF6E       Interrupt durch Timer setzen

                                *** Parameter f. Filenamen setzen
.,FDF9 85 B7    STA $B7         Länge speichern
.,FDFB 86 BB    STX $BB         Adresse-LOW speichern
.,FDFD 84 BC    STY $BC         Adresse-HIGH speichern
.,FDFF 60       RTS             Rücksprung

                                *** Parameter für aktives
                                *** File setzen
.,FE00 85 B8    STA $B8         logische Filenummer
.,FE02 86 BA    STX $BA         Geräteadresse
.,FE04 84 B9    STY $B9         Sekundäradresse
.,FE06 60       RTS             Rücksprung

                                *** Status holen
.,FE07 A5 BA    LDA $BA         Gerätenummer holen
.,FE09 C9 02    CMP #$02        gleich 2 ? (RS 232)
.,FE0B D0 0D    BNE $FE1A       nein
.,FE0D AD 97 02 LDA $0297       RS 232-Status holen
.,FE10 48       PHA             und auf Stapel retten
.,FE11 A9 00    LDA #$00        Status
.,FE13 8D 97 02 STA $0297       löschen
.,FE16 68       PLA             und Statuswert zurückholen
.,FE17 60       RTS             Rücksprung

                                *** Flag für Betriebssystem-
                                *** meldungen setzen
.,FE18 85 9D    STA $9D         Ausgabeflag (Direktmodus)
.,FE1A A5 90    LDA $90         Statusflag holen

                                *** Status setzen
.,FE1C 05 90    ORA $90         Statusflag testen und
.,FE1E 85 90    STA $90         wieder abspeichern
.,FE20 60       RTS             Rücksprung

                                *** Timeout-Flag für IEC setzen
.,FE21 8D 85 02 STA $0285       Timeout-disable
.,FE24 60       RTS             Rücksprung

                                *** MEMTOP, Obergrenze des
                                *** BASIC-RAM holen/setzen
.,FE25 90 06    BCC $FE2D       C=0: Adresse setzen
.,FE27 AE 83 02 LDX $0283       Carry gesetzt
.,FE2A AC 84 02 LDY $0284       Adresse nach X/Y holen
.,FE2D 8E 83 02 STX $0283       Carry gelöscht
.,FE30 8C 84 02 STY $0284       X/Y nach Adresse setzen
.,FE33 60       RTS             Rücksprung

                                *** MEMBOT, Untergrenze des
                                *** BASIC-RAM holen/setzen
.,FE34 90 06    BCC $FE3C       C=0: Adresse setzen
.,FE36 AE 81 02 LDX $0281       Carry gesetzt
.,FE39 AC 82 02 LDY $0282       Adresse nach X/Y holen
.,FE3C 8E 81 02 STX $0281       Carry gelöscht
.,FE3F 8C 82 02 STY $0282       Adresse aus X/Y setzen
.,FE42 60       RTS             Rücksprung

                                *** NMI Einsprung
.,FE43 78       SEI             Interrupt setzen
.,FE44 6C 18 03 JMP ($0318)     JMP $FE47, NMI-Vektor
.,FE47 48       PHA             Akku auf Stapel retten
.,FE48 8A       TXA             X nach Akku
.,FE49 48       PHA             X retten
.,FE4A 98       TYA             Y nach Akku
.,FE4B 48       PHA             Y retten
.,FE4C A9 7F    LDA #$7F        Wert laden
.,FE4E 8D 0D DD STA $DD0D       NMI-Möglichkeiten löschen
.,FE51 AC 0D DD LDY $DD0D       Flags lesen und löschen
.,FE54 30 1C    BMI $FE72       RS 232 aktiv ?
.,FE56 20 02 FD JSR $FD02       Prüft auf ROM-Modul in $8000
.,FE59 D0 03    BNE $FE5E       nein: weiter
.,FE5B 6C 02 80 JMP ($8002)     ja: Sprung auf Modul-NMI
.,FE5E 20 BC F6 JSR $F6BC       Flag für Stop-Taste setzen
.,FE61 20 E1 FF JSR $FFE1       Stop-Taste abfragen
.,FE64 D0 0C    BNE $FE72       nicht gedrückt ?
.,FE66 20 15 FD JSR $FD15       Standard-Vektoren für
                                Interrupt und I/O setzen
.,FE69 20 A3 FD JSR $FDA3       I/O initialisieren
.,FE6C 20 18 E5 JSR $E518       Bildschirmreset
.,FE6F 6C 02 A0 JMP ($A002)     zum BASIC-Warmstart

                                *** NMI-Routine für RS 232
.,FE72 98       TYA             ICR-Register
.,FE73 2D A1 02 AND $02A1       mit RS 232 NMI-Flag verknüp.
.,FE76 AA       TAX             nach X retten
.,FE77 29 01    AND #$01        Sendebetrieb aktiv ?
.,FE79 F0 28    BEQ $FEA3       nein
.,FE7B AD 00 DD LDA $DD00       Datenport lesen
.,FE7E 29 FB    AND #$FB        Bit 2 TXD löschen
.,FE80 05 B5    ORA $B5         zu sendendes Bit übergeben
.,FE82 8D 00 DD STA $DD00       und wieder in Datenport spei.
.,FE85 AD A1 02 LDA $02A1       RS-232 NMI-Flag
.,FE88 8D 0D DD STA $DD0D       wieder in ICR schreiben
.,FE8B 8A       TXA             Wert aus X zurückholen
.,FE8C 29 12    AND #$12        Bit 1 und 4 isolieren
.,FE8E F0 0D    BEQ $FE9D       Bit 1 und 4=0: Bit empfangen
.,FE90 29 02    AND #$02        Bit 1, Aufruf von Timer B
.,FE92 F0 06    BEQ $FE9A       nein: verzweige zu Startbit
.,FE94 20 D6 FE JSR $FED6       empfangenes Bit verarbeiten
.,FE97 4C 9D FE JMP $FE9D       Vorbereitung für Byte umgehen
.,FE9A 20 07 FF JSR $FF07       Vorbereitung für Empfang
                                des nächsten Bytes
.,FE9D 20 BB EE JSR $EEBB       Empfang des nächsten Bits v.
.,FEA0 4C B6 FE JMP $FEB6       Rückkehr vom Interrupt
.,FEA3 8A       TXA             X nach Akku
.,FEA4 29 02    AND #$02        Datenempfang ?
.,FEA6 F0 06    BEQ $FEAE       verzweige wenn kein Empfang
.,FEA8 20 D6 FE JSR $FED6       empfangenes Bit verarbeiten
.,FEAB 4C B6 FE JMP $FEB6       Rückkehr vom Interrupt
.,FEAE 8A       TXA             X nach Akku
.,FEAF 29 10    AND #$10        warten auf Startbit ?
.,FEB1 F0 03    BEQ $FEB6       verzweige wenn kein Startbit
.,FEB3 20 07 FF JSR $FF07       Vorbereitung für Empfang
                                des nächsten Bytes
.,FEB6 AD A1 02 LDA $02A1       RS-232 NMI-Flag
.,FEB9 8D 0D DD STA $DD0D       wieder in ICR
.,FEBC 68       PLA             Y-Register vom Stapel
.,FEBD A8       TAY             zurückholen
.,FEBE 68       PLA             X-Register
.,FEBF AA       TAX             zurückholen
.,FEC0 68       PLA             Akku zurückholen
.,FEC1 40       RTI             Rücksprung

                                *** Timerkonstanten für RS 232 Baud-Rate,
                                *** NTSC-Version
.:FEC2 C1 27                    $27C1 = 10177       50 Baud
.:FEC4 3E 1A                    $1A3E =  6718       75 Baud
.:FEC6 C5 11                    $11C5 =  4549      110 Baud
.:FEC8 74 0E                    $0E74 =  3700      134.5 Baud
.:FECA ED 0C                    $0CED =  3309      150 Baud
.:FECC 45 06                    $0645 =  1605      300 Baud
.:FECE F0 02                    $02F0 =   752      600 Baud
.:FED0 46 01                    $0146 =   326     1200 Baud
.:FED2 B8 00                    $00B8 =   184     1800 Baud
.:FED4 71 00                    $0071 =   113     2400 Baud

                                *** NMI-Routine für RS-232
                                *** Eingabe
.,FED6 AD 01 DD LDA $DD01       Port Register B
.,FED9 29 01    AND #$01        Bit für Receive Data isolie-
                                ren
.,FEDB 85 A7    STA $A7         und speichern
.,FEDD AD 06 DD LDA $DD06       Timer B LOW
.,FEE0 E9 1C    SBC #$1C        minus 28
.,FEE2 6D 99 02 ADC $0299       + LOW-Byte der Baudrate
.,FEE5 8D 06 DD STA $DD06       wieder abspeichern
.,FEE8 AD 07 DD LDA $DD07       RS 232 Timerkon. für Baudrate
.,FEEB 6D 9A 02 ADC $029A       HIGH-Byte addieren
.,FEEE 8D 07 DD STA $DD07       in Timer schreiben
.,FEF1 A9 11    LDA #$11        Timer B starten
.,FEF3 8D 0F DD STA $DD0F       Control Register B
.,FEF6 AD A1 02 LDA $02A1       CIA 2 NMI-Flag holen
.,FEF9 8D 0D DD STA $DD0D       Interrupt Control Register
.,FEFC A9 FF    LDA #$FF        Wert laden
.,FEFE 8D 06 DD STA $DD06       und damit
.,FF01 8D 07 DD STA $DD07       Timer setzen
.,FF04 4C 59 EF JMP $EF59       Bit holen

                                *** NMI-Routine RS 232 Ausgabe
.,FF07 AD 95 02 LDA $0295       LOW- und HIGH-Byte
.,FF0A 8D 06 DD STA $DD06       holen und in
.,FF0D AD 96 02 LDA $0296       RS 232 Timerkonstanten für
.,FF10 8D 07 DD STA $DD07       Baudrate
.,FF13 A9 11    LDA #$11        Timer B starten
.,FF15 8D 0F DD STA $DD0F       Control Register B
.,FF18 A9 12    LDA #$12        Bit 1 und 4 für Verknüpfung
.,FF1A 4D A1 02 EOR $02A1       mit NMI-Flag für CIA 2
.,FF1D 8D A1 02 STA $02A1       Wert wieder speichern
.,FF20 A9 FF    LDA #$FF        höchsten Wert laden
.,FF22 8D 06 DD STA $DD06       und in Latch von
.,FF25 8D 07 DD STA $DD07       Timer B laden
.,FF28 AE 98 02 LDX $0298       Anzahl der zu sendenden Bits
.,FF2B 86 A8    STX $A8         in Zähler für Wortlänge
.,FF2D 60       RTS             Rücksprung

                                *** Timerwert für Sendebaudrate
                                *** ermitteln
.,FF2E AA       TAX             Baudrate aus Tabelle nach X
.,FF2F AD 96 02 LDA $0296       HIGH-Byte holen
.,FF32 2A       ROL             mal 2
.,FF33 A8       TAY             nach Y retten
.,FF34 8A       TXA             LOW-Byte holen
.,FF35 69 C8    ADC #$C8        plus 200
.,FF37 8D 99 02 STA $0299       nach Timerwert LOW
.,FF3A 98       TYA             HIGH-Byte zurückholen
.,FF3B 69 00    ADC #$00        Übertrag addieren
.,FF3D 8D 9A 02 STA $029A       nach Timerwert HIGH
.,FF40 60       RTS             Rücksprung
.,FF41 EA       NOP             No OPeration
.,FF42 EA       NOP             No OPeration

                                *** Einsprung aus Bandroutine
.,FF43 08       PHP             Statusregister auf Stapel
.,FF44 68       PLA             Statusregister in Akku
.,FF45 29 EF    AND #$EF        Break-Flag löschen
.,FF47 48       PHA             und wieder auf Stapel legen

                                *** IRQ-Einsprung
.,FF48 48       PHA             Akku auf Stapel retten
.,FF49 8A       TXA             X nach Akku
.,FF4A 48       PHA             X-Register retten
.,FF4B 98       TYA             Y nach Akku
.,FF4C 48       PHA             Y-Register retten
.,FF4D BA       TSX             Stapelzeiger als Zähler in X
.,FF4E BD 04 01 LDA $0104,X     Break-Flag vom Stapel holen
.,FF51 29 10    AND #$10        und testen
.,FF53 F0 03    BEQ $FF58       nicht gesetzt
.,FF55 6C 16 03 JMP ($0316)     BREAK - Routine
.,FF58 6C 14 03 JMP ($0314)     Interrupt - Routine

                                *** Video-Reset
.,FF5B 20 18 E5 JSR $E518       Videocontroller initialisie-
                                ren
.,FF5E AD 12 D0 LDA $D012       Rasterzeile
.,FF61 D0 FB    BNE $FF5E       wartet auf Ende Videozeile
.,FF63 AD 19 D0 LDA $D019       Interrupt durch Rasterzeile?
.,FF66 29 01    AND #$01        Bit 0 isolieren und als Flag
.,FF68 8D A6 02 STA $02A6       PAL/NTSC-Version merken
.,FF6B 4C DD FD JMP $FDDD       Interrupttimer setzen

                                *** Timer für Interrupt setzen
.,FF6E A9 81    LDA #$81        Timer A Unterlauf
.,FF70 8D 0D DC STA $DC0D       Interrupt Control Register
.,FF73 AD 0E DC LDA $DC0E       Control Register A
.,FF76 29 80    AND #$80        Bit 7 retten
                                Uhrzeittrigger (50/60 Hz)
.,FF78 09 11    ORA #$11        Timer A starten
.,FF7A 8D 0E DC STA $DC0E       Control Register A
.,FF7D 4C 8E EE JMP $EE8E       seriellen Takt aus
.,FF80 00       BRK             BReaK

                                *** Sprungtabelle für
                                *** Betriebssystem-Routinen
.,FF81 4C 5B FF JMP $FF5B       Video-Reset
.,FF84 4C A3 FD JMP $FDA3       CIAs initialisieren
.,FF87 4C 50 FD JMP $FD50       RAM löschen bzw. testen
.,FF8A 4C 15 FD JMP $FD15       I/O initialisieren
.,FF8D 4C 1A FD JMP $FD1A       I/O Vektoren initialisieren
.,FF90 4C 18 FE JMP $FE18       Status setzen
.,FF93 4C B9 ED JMP $EDB9       Sekundäradresse nach LISTEN senden
.,FF96 4C C7 ED JMP $EDC7       Sekundäradresse nach TALK senden
.,FF99 4C 25 FE JMP $FE25       RAM-Ende setzen/holen
.,FF9C 4C 34 FE JMP $FE34       RAM-Anfang setzen/holen
.,FF9F 4C 87 EA JMP $EA87       Tastatur abfragen
.,FFA2 4C 21 FE JMP $FE21       Time-out-Flag für IEC-Bus setzen
.,FFA5 4C 13 EE JMP $EE13       Eingabe vom IEC-Bus
.,FFA8 4C DD ED JMP $EDDD       Ausgabe vom IEC-Bus
.,FFAB 4C EF ED JMP $EDEF       UNTALK senden
.,FFAE 4C FE ED JMP $EDFE       UNLISTEN senden
.,FFB1 4C 0C ED JMP $ED0C       LISTEN senden
.,FFB4 4C 09 ED JMP $ED09       TALK senden
.,FFB7 4C 07 FE JMP $FE07       Status holen
.,FFBA 4C 00 FE JMP $FE00       Fileparameter setzen
.,FFBD 4C F9 FD JMP $FDF9       Filenamenparameter setzen
.,FFC0 6C 1A 03 JMP ($031A)     $F34A OPEN
.,FFC3 6C 1C 03 JMP ($031C)     $F291 CLOSE
.,FFC6 6C 1E 03 JMP ($031E)     $F20E CHKIN Eingabeg. setzen
.,FFC9 6C 20 03 JMP ($0320)     $F250 CKOUT Ausgabegerät set.
.,FFCC 6C 22 03 JMP ($0322)     $F333 CLRCH Ein-Ausgabe zurücksetzen
.,FFCF 6C 24 03 JMP ($0324)     $F157 BASIN Eingabe eines Zeichens
.,FFD2 6C 26 03 JMP ($0326)     $F1CA BSOUT Ausgabe eines Zeichens
.,FFD5 4C 9E F4 JMP $F49E       LOAD
.,FFD8 4C DD F5 JMP $F5DD       SAVE
.,FFDB 4C E4 F6 JMP $F6E4       Time setzen
.,FFDE 4C DD F6 JMP $F6DD       Time holen
.,FFE1 6C 28 03 JMP ($0328)     $F6ED STOP-Taste abfragen
.,FFE4 6C 2A 03 JMP ($032A)     $F13E GET
.,FFE7 6C 2C 03 JMP ($032C)     $F32F CLALL
.,FFEA 4C 9B F6 JMP $F69B       Time erhöhen
.,FFED 4C 05 E5 JMP $E505       SCREEN Anzahl Zeilen und Spalten holen
.,FFF0 4C 0A E5 JMP $E50A       Cursor setzen / Cursorposition holen
.,FFF3 4C 00 E5 JMP $E500       Startadresse des I/O-Bausteins holen


.:FFF6 52 52 42 59

                                *** Hardware Vektoren
.:FFFA 43 FE                    NMI Vektor
.:FFFC E2 FC                    RESET Vektor
.:FFFE 48 FF                    IRQ Vektor
