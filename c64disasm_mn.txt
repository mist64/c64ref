- Commented Commodore 64 KERNAL Disassembly (Magnus Nyman)
-
- The comments have been taken from
-    JIFFYDOS version 6.01/version 6.02 by Magnus Nyman (Harlekin/FairLight)
-
- The original comments were meant for the JiffyDOS KERNAL, so it had to be
- adapted for the regular KERNAL (901227-03, $FF80 = 3). Therefore, some serial
- code and all tape code is missing comments.
-
- Converted, formatted and adapted by Michael Steil <mist64@mac.com>
-
- Corrections (typos, formatting, content) welcome at:
- https://github.com/mist64/c64disasm
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

                                *** BIOERR: HANDLE I/O ERROR IN BASIC
                                This routine is called whenever BASIC wishes to call one
                                of the KERNAL I/O routines. It is also used to handle I/O
                                errors in BASIC.
.,E0F9 C9 F0    CMP #$F0        test error
.,E0FB D0 07    BNE $E104
.,E0FD 84 38    STY $38         MEMSIZ, highest address in BASIC
.,E0FF 86 37    STX $37
.,E101 4C 63 A6 JMP $A663       do CLR without aborting I/O
.,E104 AA       TAX             put error flag i (X)
.,E105 D0 02    BNE $E109       if error code $00, then set error code $1e
.,E107 A2 1E    LDX #$1E
.,E109 4C 37 A4 JMP $A437       do error

                                *** BCHOUT: OUTPUT CHARACTER
                                This routine uses the KERNAL routine CHROUT to output the
                                character in (A) to an available output channel. A test is
                                made for a possible I/O error.
.,E10C 20 D2 FF JSR $FFD2       output character in (A)
.,E10F B0 E8    BCS $E0F9       if carry set, handle I/O error
.,E111 60       RTS             else return

                                *** BCHIN: INPUT CHARACTER
                                This routine uses the KERNAL routine CHRIN to input a
                                character to (A) from an available input channel. A test
                                is made for a possible I/O error.
.,E112 20 CF FF JSR $FFCF       input character from CHRIN
.,E115 B0 E2    BCS $E0F9       if carry set, handle I/O error
.,E117 60       RTS             else return

                                *** BCKOUT:SET UP FOR OUTPUT
                                This routine uses the KERNAL routine CHKOUT to open an
                                output channel, and tests for possible I/O error. On entry
                                (X) must hold the the logical file number as used in OPEN.
.,E118 20 AD E4 JSR $E4AD       open output channel via CHKOUT
.,E11B B0 DC    BCS $E0F9       if carry set, handle I/O error
.,E11D 60       RTS             else return

                                *** BCKIN: SET UP FOR INPUT
                                This routine uses the KERNAL routine CHKIN to open an
                                input channel. A test as made for possible I/O error.
.,E11E 20 C6 FF JSR $FFC6       open input channel via CHKIN
.,E121 B0 D6    BCS $E0F9       if carry set, handle I/O error
.,E123 60       RTS             else return

                                *** BGETIN: GET ONT CHARACTER
                                This routine uses the KERNAL routine GETIN to get a
                                character from the keyboard buffer into (A). A test is
                                made for possible I/O error.
.,E124 20 E4 FF JSR $FFE4       GETIN, get character from keyboard buffer
.,E127 B0 D0    BCS $E0F9       if carry set, handle I/O error
.,E129 60       RTS             else return

                                *** SYS: PERFORM SYS
                                This routine enables machine language routines to be
                                executed from BASIC. The routine evaluates the address and
                                confirms that it is a numeric number. The return address
                                is set up, and the user routine is executed.
.,E12A 20 8A AD JSR $AD8A       evaluate text & confirm numeric
.,E12D 20 F7 B7 JSR $B7F7       convert fac#1 to integer in LINNUM
.,E130 A9 E1    LDA #$E1        set return address on stack to $ea46
.,E132 48       PHA
.,E133 A9 46    LDA #$46
.,E135 48       PHA
.,E136 AD 0F 03 LDA $030F       SPREG, user flag register
.,E139 48       PHA
.,E13A AD 0C 03 LDA $030C       SAREG, user (A) register
.,E13D AE 0D 03 LDX $030D       SXREG, user (X) register
.,E140 AC 0E 03 LDY $030E       SYREG, user (Y) register
.,E143 28       PLP
.,E144 6C 14 00 JMP ($0014)     execute user routine, exit with rts
.,E147 08       PHP
.,E148 8D 0C 03 STA $030C       store in SAREG, user (A) register
.,E14B 8E 0D 03 STX $030D       store in SXREG, user (X) register
.,E14E 8C 0E 03 STY $030E       store in SYREG, user (Y) register
.,E151 68       PLA
.,E152 8D 0F 03 STA $030F       store in SPREG, user flag register
.,E155 60       RTS             back

                                *** SAVET: PERFORM SAVE
                                This routine is sets parameters for save, and calls the
                                save routine. The start and end addresses are obtained
                                from TXTTAB and VARTAB. Finally, a test is made if any
                                errors ocured.
.,E156 20 D4 E1 JSR $E1D4       get SAVE paramerters from text
.,E159 A6 2D    LDX $2D         VARTAB, start of variables
.,E15B A4 2E    LDY $2E
.,E15D A9 2B    LDA #$2B        <TXTTAB, start of BASIC text
.,E15F 20 D8 FF JSR $FFD8       execute SAVE
.,E162 B0 95    BCS $E0F9       if carry is set, handle I/O errors
.,E164 60       RTS

                                *** VERFYT: PERFORM LOAD/SAVE
                                This routine is essentially the same for both LOAD and
                                VERIFY. The entry point determins which is performed, by
                                setting VERCK accordingly. The LOAD/VERIFY parameters,
                                filename, device etc. are obtained from text before the
                                KERNAL routine LOAD is called. A test is made for I/O
                                errors. At this point, the two functios are distiguished.
                                VERIFY reads the the status word and prints the message OK
                                or ?VERIFY error depending on the result of the test. LOAD
                                reads the I/O status word for a possible ?LOAD error, then
                                updates the pointers to text and variables, exiting via
                                CLR.
.,E165 A9 01    LDA #$01        flag verify
.:E167 2C       .BYTE $2C       mask
.,E168 A9 00    LDA #$00
.,E16A 85 0A    STA $0A         store in VRECK, LOAD/VERIFY flag
.,E16C 20 D4 E1 JSR $E1D4       get LOAD/VERIFY parameters from text
.,E16F A5 0A    LDA $0A         get VRECK
.,E171 A6 2B    LDX $2B         TXTTAB, start of BASIC
.,E173 A4 2C    LDY $2C
.,E175 20 D5 FF JSR $FFD5       execute LOAD, KERNAL routine
.,E178 B0 57    BCS $E1D1       if carry set, handle error
.,E17A A5 0A    LDA $0A         test VRECK for LOAD or VERIFY
.,E17C F0 17    BEQ $E195       do LOAD
.,E17E A2 1C    LDX #$1C        set error $1c, VERIFY error
.,E180 20 B7 FF JSR $FFB7       do READST, get status I/O word
.,E183 29 10    AND #$10        %00010000, test for mismatch
.,E185 D0 17    BNE $E19E       data mismatch, do error
.,E187 A5 7A    LDA $7A         <TXTPTR
.,E189 C9 02    CMP #$02
.,E18B F0 07    BEQ $E194
.,E18D A9 64    LDA #$64        set address to text OK
.,E18F A0 A3    LDY #$A3        at $a364
.,E191 4C 1E AB JMP $AB1E       output string in (A/Y)
.,E194 60       RTS
.,E195 20 B7 FF JSR $FFB7       do READST, get status I/O for LOAD
.,E198 29 BF    AND #$BF        %10111111, test all but EOI
.,E19A F0 05    BEQ $E1A1       nope, no errors
.,E19C A2 1D    LDX #$1D        set error $1d, LOAD error
.,E19E 4C 37 A4 JMP $A437       do error
.,E1A1 A5 7B    LDA $7B         >TXTPTR
.,E1A3 C9 02    CMP #$02
.,E1A5 D0 0E    BNE $E1B5
.,E1A7 86 2D    STX $2D         set VARTAB, start of variables
.,E1A9 84 2E    STY $2E
.,E1AB A9 76    LDA #$76        set address to text READY
.,E1AD A0 A3    LDY #$A3        at $a376
.,E1AF 20 1E AB JSR $AB1E       output string in (A/Y)
.,E1B2 4C 2A A5 JMP $A52A       do CLR and restart BASIC
.,E1B5 20 8E A6 JSR $A68E       reset TXTPTR
.,E1B8 20 33 A5 JSR $A533       rechain BASIC lines
.,E1BB 4C 77 A6 JMP $A677       do RESTORE and reset OLDTXT

                                *** OPENT: PERFORM OPEN
                                This routine extracts paramerters from text and performs
                                the OPEN routine in KERNAL. A test is made for I/O errors.
.,E1BE 20 19 E2 JSR $E219       get parameters from text
.,E1C1 20 C0 FF JSR $FFC0       execute OPEN
.,E1C4 B0 0B    BCS $E1D1       if carry set, handle error
.,E1C6 60       RTS

                                *** CLOSET: PERFORM CLOSE
                                The parameters for CLOSE are obtained from text, and the
                                logical filenumber placed in (A), The KERNAL routine CLOSE
                                is performed, and a test is made for I/O errors.
.,E1C7 20 19 E2 JSR $E219       get parameters from text
.,E1CA A5 49    LDA $49         logical file number
.,E1CC 20 C3 FF JSR $FFC3       perform CLOSE
.,E1CF 90 C3    BCC $E194       if carry set, handle error, else return
.,E1D1 4C F9 E0 JMP $E0F9       jump to error routine

                                *** SLPARA: GET PARAMETERS FOR LOAD/SAVE
                                This routine gets the filename, devicenumber and secondary
                                address for LOAD/VERIFY and SAVE operations. The KERNAL
                                routines SETNAM and SETLFS are used to do this. Default
                                parameters are set up, then tests are made if any of the
                                parameters were given. If so, these are set up as wanted.
.,E1D4 A9 00    LDA #$00        clear length of filename
.,E1D6 20 BD FF JSR $FFBD       SETNAM
.,E1D9 A2 01    LDX #$01        default FA, device number is #01
.,E1DB A0 00    LDY #$00        default SA, secondary address is #00
.,E1DD 20 BA FF JSR $FFBA       SETLFS, and device number
.,E1E0 20 06 E2 JSR $E206       test if "end of line", if so end here
.,E1E3 20 57 E2 JSR $E257       set up given filename and perform SETNAM
.,E1E6 20 06 E2 JSR $E206       test if "end of line", if so end here
.,E1E9 20 00 E2 JSR $E200       check for comma, and input one byte, FA, to (X)
.,E1EC A0 00    LDY #$00
.,E1EE 86 49    STX $49
.,E1F0 20 BA FF JSR $FFBA       perform new SETLFS with device number
.,E1F3 20 06 E2 JSR $E206       test if "end of line", if so end here
.,E1F6 20 00 E2 JSR $E200       check for comma, and input one byte, SA, to (X)
.,E1F9 8A       TXA             transfer (X) to (Y)
.,E1FA A8       TAY
.,E1FB A6 49    LDX $49         get FA
.,E1FD 4C BA FF JMP $FFBA       perform SETLFS with both device number and secondary
                                address. Then exit

                                *** COMBYT: GET NEXT ONE-BYTE PARAMETER
                                This routine checks if the next character of text is a
                                comma, and then inputs the parameter following into (X).
.,E200 20 0E E2 JSR $E20E       check for comma
.,E203 4C 9E B7 JMP $B79E       input one byte parameter to (X)

                                *** DEFLT: CHECK DEFAULT PARAMETERS
                                This routine tests CHRGOT to see if a optional parameter
                                was included in the text. If it was, a normal exit is
                                performed via RTS. If not, the return address on the stack
                                is discarded, and the routine exits both this and the
                                calling routine.
.,E206 20 79 00 JSR $0079       get CHRGOT
.,E209 D0 02    BNE $E20D       if last character is a character, do normal exit
.,E20B 68       PLA             else, remove return address
.,E20C 68       PLA             to exit this AND the calling routine.
.,E20D 60       RTS             exit

                                *** CMMERR: CHECK FOR COMMA
                                This routine confirms that the next character in the text
                                is a comma. It also test that the comma is not immediately
                                ollowed by a terminator. If so, exit and do SYNTAX error.
.,E20E 20 FD AE JSR $AEFD       confirm comma
.,E211 20 79 00 JSR $0079       get CHRGOT
.,E214 D0 F7    BNE $E20D       else than null
.,E216 4C 08 AF JMP $AF08       execute SYNTAX error

                                *** OCPARA: GET PARAMETERS FOR OPEN/CLOSE
                                This routine gets the logical file number, device number,
                                secondary address and filename for OPEN/CLOSE. Initially
                                the default filename is set to null, and the device number
                                to #1. The logical filenumber is compulsory, and is
                                obtained from text and placed in <FORPNT. The other
                                parameters are optinal and are obtained if present. The
                                device number is stored in >FORPNT. The parameters are set
                                via the KERNAL routines SETNAM and SETLFS.
.,E219 A9 00    LDA #$00        default filename is null
.,E21B 20 BD FF JSR $FFBD       SETNAM
.,E21E 20 11 E2 JSR $E211       confirm TXTPNT is no terminator, if so - error
.,E221 20 9E B7 JSR $B79E       input one byte character to (X)
.,E224 86 49    STX $49         store logical filenumber in <FORPNT
.,E226 8A       TXA             set default parameters to
.,E227 A2 01    LDX #$01        device = #1
.,E229 A0 00    LDY #$00        secondary address = #0
.,E22B 20 BA FF JSR $FFBA       SETLFS
.,E22E 20 06 E2 JSR $E206       test if "end of line", if so end here
.,E231 20 00 E2 JSR $E200       check for comma, and input FA, device number
.,E234 86 4A    STX $4A         store in >FORPNT
.,E236 A0 00    LDY #$00        secondary address = #0
.,E238 A5 49    LDA $49         logical file number from temp store
.,E23A E0 03    CPX #$03        test if serial devce
.,E23C 90 01    BCC $E23F       nope
.,E23E 88       DEY             if serial, set secondary address to $ff
.,E23F 20 BA FF JSR $FFBA       SETLFS
.,E242 20 06 E2 JSR $E206       test if "end of line", if so end here
.,E245 20 00 E2 JSR $E200       check for comma, and input SA, secondary address
.,E248 8A       TXA
.,E249 A8       TAY             SA to (Y)
.,E24A A6 4A    LDX $4A         FA
.,E24C A5 49    LDA $49         LA
.,E24E 20 BA FF JSR $FFBA       SETLFS
.,E251 20 06 E2 JSR $E206       test if "end of line", if so end here
.,E254 20 0E E2 JSR $E20E       check for comma only
.,E257 20 9E AD JSR $AD9E       evaluate expression in text
.,E25A 20 A3 B6 JSR $B6A3       do string housekeeping
.,E25D A6 22    LDX $22         pointers to given filename
.,E25F A4 23    LDY $23
.,E261 4C BD FF JMP $FFBD       SETNAM and exit

                                *** COS: PERFORM COS
                                This routine manipulates the input COS to be calcuated
                                with SIN. COS(X) = SIN(X+pi/2), where  X is in radians. We
                                use it as Fac#1=SIN(fac#1+pi/2), ie pi/2 is added to fac#1
                                and the following SIN is performed.
.,E264 A9 E0    LDA #$E0        set address to pi/2
.,E266 A0 E2    LDY #$E2        at $e2e0
.,E268 20 67 B8 JSR $B867       add fltp at (A/Y) to fac#1

                                *** SIN: PERFORM SIN
.,E26B 20 0C BC JSR $BC0C
.,E26E A9 E5    LDA #$E5
.,E270 A0 E2    LDY #$E2
.,E272 A6 6E    LDX $6E
.,E274 20 07 BB JSR $BB07
.,E277 20 0C BC JSR $BC0C
.,E27A 20 CC BC JSR $BCCC
.,E27D A9 00    LDA #$00
.,E27F 85 6F    STA $6F
.,E281 20 53 B8 JSR $B853
.,E284 A9 EA    LDA #$EA
.,E286 A0 E2    LDY #$E2
.,E288 20 50 B8 JSR $B850
.,E28B A5 66    LDA $66
.,E28D 48       PHA
.,E28E 10 0D    BPL $E29D
.,E290 20 49 B8 JSR $B849
.,E293 A5 66    LDA $66
.,E295 30 09    BMI $E2A0
.,E297 A5 12    LDA $12
.,E299 49 FF    EOR #$FF
.,E29B 85 12    STA $12
.,E29D 20 B4 BF JSR $BFB4
.,E2A0 A9 EA    LDA #$EA
.,E2A2 A0 E2    LDY #$E2
.,E2A4 20 67 B8 JSR $B867
.,E2A7 68       PLA
.,E2A8 10 03    BPL $E2AD
.,E2AA 20 B4 BF JSR $BFB4
.,E2AD A9 EF    LDA #$EF
.,E2AF A0 E2    LDY #$E2
.,E2B1 4C 43 E0 JMP $E043

                                *** TAN: PERFORM TAN
.,E2B4 20 CA BB JSR $BBCA
.,E2B7 A9 00    LDA #$00
.,E2B9 85 12    STA $12
.,E2BB 20 6B E2 JSR $E26B
.,E2BE A2 4E    LDX #$4E
.,E2C0 A0 00    LDY #$00
.,E2C2 20 F6 E0 JSR $E0F6
.,E2C5 A9 57    LDA #$57
.,E2C7 A0 00    LDY #$00
.,E2C9 20 A2 BB JSR $BBA2
.,E2CC A9 00    LDA #$00
.,E2CE 85 66    STA $66
.,E2D0 A5 12    LDA $12
.,E2D2 20 DC E2 JSR $E2DC
.,E2D5 A9 4E    LDA #$4E
.,E2D7 A0 00    LDY #$00
.,E2D9 4C 0F BB JMP $BB0F
.,E2DC 48       PHA
.,E2DD 4C 9D E2 JMP $E29D

                                *** PI2: TABLE OF TRIGONOMETRY CONSTANTS
                                The following constants are held in 5 byte flpt for
                                trigonometry evaluation.
.:E2E0 81 49 0F DA A2           ; 1.570796327 (pi/2)
.:E2E5 83 49 0F DA A2           ; 6.28318531  (pi*2)
.:E2EA 7F 00 00 00 00           ; 0.25
.:E2EF 05                       ; 5 (one byte counter for SIN series)
.:E2F0 84 E6 1A 2D 1B           ; -14.3813907 (SIN constant 1)
.:E2F5 86 28 07 FB F8           ; 42.0077971  (SIN constant 2)
.:E2FA 87 99 68 89 01           ; -76.7041703 (SIN constant 3)
.:E2FF 87 23 35 DF E1           ; 81.6052237  (SIN constant 4)
.:E304 86 A5 5D E7 28           ; -41.3417021 (SIN constant 5)
.:E309 83 49 0F DA A2           ; 6.28318531  (SIN constant 6, pi*2)

                                *** ATN: PERFORM ATN
.,E30E A5 66    LDA $66
.,E310 48       PHA
.,E311 10 03    BPL $E316
.,E313 20 B4 BF JSR $BFB4
.,E316 A5 61    LDA $61
.,E318 48       PHA
.,E319 C9 81    CMP #$81
.,E31B 90 07    BCC $E324
.,E31D A9 BC    LDA #$BC
.,E31F A0 B9    LDY #$B9
.,E321 20 0F BB JSR $BB0F
.,E324 A9 3E    LDA #$3E
.,E326 A0 E3    LDY #$E3
.,E328 20 43 E0 JSR $E043
.,E32B 68       PLA
.,E32C C9 81    CMP #$81
.,E32E 90 07    BCC $E337
.,E330 A9 E0    LDA #$E0
.,E332 A0 E2    LDY #$E2
.,E334 20 50 B8 JSR $B850
.,E337 68       PLA
.,E338 10 03    BPL $E33D
.,E33A 4C B4 BF JMP $BFB4
.,E33D 60       RTS


                                *** ATNCON: TABLE OF ATN CONSTANTS
                                The table holds a 1 byte counter and the folloeing 5 byte
                                flpt constants.
.:E33E 0B                       ; 13 (one byte counter for ATN series)
.:E33F 76 B3 83 BD D3           ; -0.000684793912 (ATN constant 1)
.:E344 79 1E F4 A6 F5           ; 0.00485094216   (ATN constant 2)
.:E349 7B 83 FC B0 10           ; -0.161117018    (ATN constant 3)
.:E34E 7C 0C 1F 67 CA           ; 0.034209638     (ATN constant 5)
.:E353 7C DE 53 CB C1           ; -0.0542791328   (ATN constant 6)
.:E358 7D 14 64 70 4C           ; 0.0724571965    (ATN constant 7)
.:E35D 7D B7 EA 51 7A           ; -0.0898023954   (ATN constant 8)
.:E362 7D 63 30 88 7E           ; 0.110932413     (ATN constant 9)
.:E367 7E 92 44 99 3A           ; -0.14283908     (ATN constant 10)
.:E36C 7E 4C CC 91 C7           ; 0.19999912      (ATN constant 11)
.:E371 7F AA AA AA 13           ; -0.333333316    (ATN constant 12)
.:E376 81 00 00 00 00           ; 1               (ATN constant 13)

                                *** BASSFT: BASIC WARM START
                                This is the BASIC warm start routine that is vectored at
                                the very start of the BASIC ROM. The routine is called by
                                the 6510 BRK instruction, or STOP/RESTORE being pressed.
                                It outputs the READY prompt via the IERROR vector at
                                $0300. If the error code, in (X) is larger than $80, then
                                only the READY text will be displayed.
.,E37B 20 CC FF JSR $FFCC       CLRCHN, close all I/O channels
.,E37E A9 00    LDA #$00
.,E380 85 13    STA $13         input prompt flag
.,E382 20 7A A6 JSR $A67A       do CLR
.,E385 58       CLI             enable IRQ
.,E386 A2 80    LDX #$80        error code #$80
.,E388 6C 00 03 JMP ($0300)     perform error
.,E38B 8A       TXA             error number
.,E38C 30 03    BMI $E391       larger than $80
.,E38E 4C 3A A4 JMP $A43A       nope, print error
.,E391 4C 74 A4 JMP $A474       print READY

                                *** INIT: BASIC COLD START
                                This is the BASIC cold start routine that is vectored at
                                the very start of the BASIC ROM. BASIC vectors and
                                variables are set up, and power-up message is output, and
                                BASIC is restarted.
.,E394 20 53 E4 JSR $E453
.,E397 20 BF E3 JSR $E3BF       Initialize BASIC
.,E39A 20 22 E4 JSR $E422       output power-up message
.,E39D A2 FB    LDX #$FB        reset stack
.,E39F 9A       TXS
.,E3A0 D0 E4    BNE $E386       output READY, and restart BASIC

                                *** INITAT: CHRGET FOR ZEROPAGE
                                This is the CHRGET routine which is transferred to RAM
                                starting at $0073 on power-up or reset.
.,E3A2 E6 7A    INC $7A         increment <TXTPTR
.,E3A4 D0 02    BNE $E3A8       skip high byte
.,E3A6 E6 7B    INC $7B         increment >TXTPTR
.,E3A8 AD 60 EA LDA $EA60       CHRGOT entry, read TXTPTR
.,E3AB C9 3A    CMP #$3A        colon (terminator), sets (Z)
.,E3AD B0 0A    BCS $E3B9
.,E3AF C9 20    CMP #$20        space, get next character
.,E3B1 F0 EF    BEQ $E3A2
.,E3B3 38       SEC
.,E3B4 E9 30    SBC #$30        zero
.,E3B6 38       SEC
.,E3B7 E9 D0    SBC #$D0
.,E3B9 60       RTS

                                *** RNDSED: RANDOM SEED FOR ZEROPAGE
                                This is the initial value of the seed for the random
                                number function. It is copied into RAM from $008b-$008f.
                                Its fltp value is 0.811635157.
.:E3BA 80 4F C7 52 58

                                *** INITCZ: INITIALISE BASIC RAM
                                This routine sets the USR jump instruction to point to
                                ?ILLEGAL QUANTITY error, sets ADRAY1 and ADRAY2, copies
                                CHRGET and RNDSED to zeropage, sets up the start and end
                                locations for BASIC text and sets the first text byte to
                                zero.
.,E3BF A9 4C    LDA #$4C        ; opcode for JMP
.,E3C1 85 54    STA $54         ; store in JMPER
.,E3C3 8D 10 03 STA $0310       ; USRPOK, set USR JMP instruction
.,E3C6 A9 48    LDA #$48
.,E3C8 A0 B2    LDY #$B2        ; vector to $b248, ?ILLEGAL QUANTITY
.,E3CA 8D 11 03 STA $0311
.,E3CD 8C 12 03 STY $0312       ; store in USRADD
.,E3D0 A9 91    LDA #$91
.,E3D2 A0 B3    LDY #$B3        ; vector to $b391
.,E3D4 85 05    STA $05
.,E3D6 84 06    STY $06         ; store in ADRAY2
.,E3D8 A9 AA    LDA #$AA
.,E3DA A0 B1    LDY #$B1        ; vector to $b1aa
.,E3DC 85 03    STA $03
.,E3DE 84 04    STY $04         ; store in ADRAY1
.,E3E0 A2 1C    LDX #$1C        ; copy the CHRGET routine and RNDSED to RAM
.,E3E2 BD A2 E3 LDA $E3A2,X     ; source address
.,E3E5 95 73    STA $73,X       ; destination address
.,E3E7 CA       DEX             ; next byte
.,E3E8 10 F8    BPL $E3E2       ; till ready
.,E3EA A9 03    LDA #$03
.,E3EC 85 53    STA $53         ; store #3 in FOUR6, garbage collection
.,E3EE A9 00    LDA #$00
.,E3F0 85 68    STA $68         ; init BITS, fac#1 overflow
.,E3F2 85 13    STA $13         ; init input prompt flag
.,E3F4 85 18    STA $18         ; init LASTPT
.,E3F6 A2 01    LDX #$01
.,E3F8 8E FD 01 STX $01FD
.,E3FB 8E FC 01 STX $01FC
.,E3FE A2 19    LDX #$19
.,E400 86 16    STX $16         ; TEMPPT, pointer to descriptor stack
.,E402 38       SEC             ; set carry to indicate read mode
.,E403 20 9C FF JSR $FF9C       ; read MEMBOT
.,E406 86 2B    STX $2B         ; set TXTTAB, bottom of RAM
.,E408 84 2C    STY $2C
.,E40A 38       SEC             ; set carry to indicate read mode
.,E40B 20 99 FF JSR $FF99       ; read MEMTOP
.,E40E 86 37    STX $37         ; set MEMSIZ, top of RAM
.,E410 84 38    STY $38
.,E412 86 33    STX $33         ; set FRETOP = MEMTOP
.,E414 84 34    STY $34
.,E416 A0 00    LDY #$00
.,E418 98       TYA
.,E419 91 2B    STA ($2B),Y     ; store zero at start of BASIC
.,E41B E6 2B    INC $2B         ; increment TXTTAB to next memory position
.,E41D D0 02    BNE $E421       ; skip msb
.,E41F E6 2C    INC $2C
.,E421 60       RTS             ; return

                                *** INITMS: OUTPUT POWER-UP MESSAGE
                                This routine outputs the startup message. It then
                                calcuates the number of BASIC bytes free by subatracting
                                the TXTTAB from MEMSIZ, and outputs this number. The
                                routine exits via NEW.
.,E422 A5 2B    LDA $2B         read TXTTAB, start of BASIC
.,E424 A4 2C    LDY $2C
.,E426 20 08 A4 JSR $A408       check for memory overlap
.,E429 A9 73    LDA #$73        $e473, startup message
.,E42B A0 E4    LDY #$E4
.,E42D 20 1E AB JSR $AB1E       output (A/Y)
.,E430 A5 37    LDA $37         MEMSIZ, highest address in BASIC
.,E432 38       SEC             prepare for substract
.,E433 E5 2B    SBC $2B         substract TXTTAB
.,E435 AA       TAX             move to (X)
.,E436 A5 38    LDA $38         and highbyte
.,E438 E5 2C    SBC $2C
.,E43A 20 CD BD JSR $BDCD       output number in (A/X)
.,E43D A9 60    LDA #$60        $e460
.,E43F A0 E4    LDY #$E4        pointer to 'BASIC BYTES FREE'
.,E441 20 1E AB JSR $AB1E       output (A/Y)
.,E444 4C 44 A6 JMP $A644       perform NEW

                                *** VECTORS
                                This table contains jump vectors that are transfered to
                                $0300-$030b.
.:E447 8B E3                    IERROR VEC, print basic error message ($e38b)
.:E449 83 A4                    IMAIN VECTOR, basic warm start ($a483)
.:E44B 7C A5                    ICRNCH VECTOR, tokenise basic text ($a57c)
.:E44D 1A A7                    IQPLOP VECTOR, list basic text ($a7a1)
.:E44F E4 A7                    IGONE VEXTOR, basic character dispatch ($a7e4)
.:E451 86 AE                    IEVAL VECTOR, evaluate basic token ($ae86)

                                *** INIT VECTORS
                                This routine transfers the vectors $0300-$030b.
.,E453 A2 0B    LDX #$0B        6 vectors to be copied
.,E455 BD 47 E4 LDA $E447,X
.,E458 9D 00 03 STA $0300,X
.,E45B CA       DEX             next byte
.,E45C 10 F7    BPL $E455       ready
.,E45E 60       RTS             return

                                *** WORDS: POWER UP MESSAGE
                                This is the power up message displayed on the screen when
                                the 'Commie' is switched on or reset. The strings are
                                seperated by a zero byte.
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

                                *** PATCH FOR BASIC CHKOUT CALL
                                This is a short patch added for the KERNAL ROM to preserv
                                (A) when there was no error returned from BASIC calling
                                the CHKOUT routine. This corrects a bug in the early
                                versions of PRINT# and CMD.
.,E4AD 48       PHA             temp store (A)
.,E4AE 20 C9 FF JSR $FFC9       CHKOUT
.,E4B1 AA       TAX
.,E4B2 68       PLA             retrieve (A)
.,E4B3 90 01    BCC $E4B6
.,E4B5 8A       TXA
.,E4B6 60       RTS

.:E4B7 AA AA AA AA AA AA AA AA
.:E4BF AA AA AA AA AA AA AA AA
.:E4C7 AA AA AA AA AA AA AA AA
.:E4CF AA AA AA AA AA

                                *** RS232 PATCH
                                This patch has been added to the RS232 input routine in
                                KERNAL v.3. It initialises the RS232 parity byte, RIPRTY,
                                on reception of a start bit.
.,E4D3 85 A9    STA $A9         RINONE, check for start bit
.,E4D5 A9 01    LDA #$01
.,E4D7 85 AB    STA $AB         RIPRTY, RS232 input parity
.,E4D9 60       RTS

                                *** RESET CHARACTER COLOUR
                                This routine is a patch in KERNAL version 3 to fix a bug
                                with the colour code. The routine is called by 'clear a
                                screen line', and sets the character colour to COLOR.
.,E4DA AD 86 02 LDA $0286       get COLOR
.,E4DD 91 F3    STA ($F3),Y     and store in current screen position
.,E4DF 60       RTS

                                *** PAUSE AFTER FINDING TAPE FILE
                                This routine continues tape loading without pressing C=
                                when a file was found.
.,E4E0 69 02    ADC #$02
.,E4E2 A4 91    LDY $91
.,E4E4 C8       INY
.,E4E5 D0 04    BNE $E4EB
.,E4E7 C5 A1    CMP $A1
.,E4E9 D0 F7    BNE $E4E2
.,E4EB 60       RTS

                                *** RS232 TIMING TABLE - PAL
                                Timingtable for RS232 NMI for use with PAL machines. This
                                table contains the prescaler values for setting up the
                                RS232 baudrates. The table containe 10 entries which
                                corresponds to one of the fixed RS232 rates, starting with
                                lowest (50 baud) and finishing with the highest (2400
                                baud). Since the clock frequency is different between NTSC
                                and PAL systems, there is another table for NTSC machines
                                at $fec2.
.:E4EC 19 26                    50 baud
.:E4EE 44 19                    75 baud
.:E4F0 1A 11                    110 baud
.:E4F2 E8 0D                    134.5 baud
.:E4F4 70 0C                    150 baud
.:E4F6 06 06                    300 baud
.:E4F8 D1 02                    600 baud
.:E4FA 37 01                    1200 baud
.:E4FC AE 00                    (1800) 2400 baud
.:E4FE 69 00                    2400 baud

                                *** IOBASE: GET I/O ADDRESS
                                The KERNAL routine IOBASE ($fff3) jumps to this routine.
                                It returns the base address $dc00 in (X/Y)
.,E500 A2 00    LDX #$00        set (X/Y) to $dc00
.,E502 A0 DC    LDY #$DC
.,E504 60       RTS

                                *** SCREEN: GET SCREEN SIZE
                                The KERNAL routine SCREEN ($ffed) jumps to this routine.
                                It returns the screen size; columns in (X) and rows in
                                (Y).
.,E505 A2 28    LDX #$28        40 columns
.,E507 A0 19    LDY #$19        25 rows
.,E509 60       RTS

                                *** PLOT: PUT/GET ROW AND COLUMN
                                The KERNAL routine PLOT ($fff0) jumps to this routine. The
                                option taken depends on the state of carry on entry. If it
                                is set, the column is placed in (Y) and the row placed in
                                (X). If carry is clear, the cursor position is read from
                                (X/Y) and the screen pointers are set.
.,E50A B0 07    BCS $E513       if carry set, jump
.,E50C 86 D6    STX $D6         store TBLX, current row
.,E50E 84 D3    STY $D3         store PNTR, current column
.,E510 20 6C E5 JSR $E56C       set screen pointers
.,E513 A6 D6    LDX $D6         read TBLX
.,E515 A4 D3    LDY $D3         read PNTR
.,E517 60       RTS

                                *** CINT1: INITIALISE I/O
                                This routine is part of the KERNAL CINT init routine. I/O
                                default values are set, <shift+cbm> keys are disabled, and
                                cursor is switched off. The vector to the keyboard table
                                is set up, and the length of the keyboardbuffer is set to
                                10 characters. The cursor color is set to lightblue, and
                                the key-repeat parameters are set up.
.,E518 20 A0 E5 JSR $E5A0       set I/O defaults
.,E51B A9 00    LDA #$00
.,E51D 8D 91 02 STA $0291       disable <SHIFT + CBM> by writing zero into MODE
.,E520 85 CF    STA $CF         the cursor blink flag, set BLNON on
.,E522 A9 48    LDA #$48
.,E524 8D 8F 02 STA $028F
.,E527 A9 EB    LDA #$EB        set the KEYLOG vector to point at $eb48
.,E529 8D 90 02 STA $0290
.,E52C A9 0A    LDA #$0A        set max number of character is keyboard buffer to 10
.,E52E 8D 89 02 STA $0289       XMAX
.,E531 8D 8C 02 STA $028C       How many 1/60 of a second to wait before key is repeated.
                                Used togeather with $028b
.,E534 A9 0E    LDA #$0E        set character colour to light blue
.,E536 8D 86 02 STA $0286       COLOR
.,E539 A9 04    LDA #$04        How many $028c before a new entry is
.,E53B 8D 8B 02 STA $028B       put in the keyboard buffer, KOUNT
.,E53E A9 0C    LDA #$0C
.,E540 85 CD    STA $CD         store in BLCNT, cursor toggle timer
.,E542 85 CC    STA $CC         store in BLNSW, cursor enable

                                *** CLEAR SCREEN
                                This routine sets up the screen line link table ($d9 -
                                $f2), LDTB1, which is used to point out the address to the
                                screen. The later part of the routine performs the screen
                                clear, line by line, starting at the bottom line. It
                                continues to the next routine which is used to home the
                                cursor.
.,E544 AD 88 02 LDA $0288       get HIBASE, top of screen memory
.,E547 09 80    ORA #$80        fool around
.,E549 A8       TAY
.,E54A A9 00    LDA #$00
.,E54C AA       TAX
.,E54D 94 D9    STY $D9,X       store in screen line link table, LDTB1
.,E54F 18       CLC
.,E550 69 28    ADC #$28        add #40 to next line
.,E552 90 01    BCC $E555
.,E554 C8       INY             inc page number
.,E555 E8       INX             next
.,E556 E0 1A    CPX #$1A        till all 26?? is done
.,E558 D0 F3    BNE $E54D
.,E55A A9 FF    LDA #$FF
.,E55C 95 D9    STA $D9,X       last pointer is $ff
.,E55E A2 18    LDX #$18        start clear screen with line $18 (bottom line)
.,E560 20 FF E9 JSR $E9FF       erase line (X)
.,E563 CA       DEX             next
.,E564 10 FA    BPL $E560       till screen is empty

                                *** HOME CURSOR
                                This routine puts the cursor in the top left corner by
                                writing its column and line to zero.
.,E566 A0 00    LDY #$00
.,E568 84 D3    STY $D3         write to PNTR, cursor column
.,E56A 84 D6    STY $D6         write to TBLX, line number

                                *** SET SCREEN POINTERS
                                This routine positions the cursor on the screen and sets
                                up the screen pointers. On entry, TBLX must hold the line
                                number, and PNTR the column number of the cursor position.
.,E56C A6 D6    LDX $D6         read TBLX
.,E56E A5 D3    LDA $D3         read PNTR
.,E570 B4 D9    LDY $D9,X       read value from screen line link table, LDTB1
.,E572 30 08    BMI $E57C       heavy calcuations??? jump when ready
.,E574 18       CLC
.,E575 69 28    ADC #$28
.,E577 85 D3    STA $D3         PNTR
.,E579 CA       DEX
.,E57A 10 F4    BPL $E570
.,E57C 20 F0 E9 JSR $E9F0       set start of line (X)
.,E57F A9 27    LDA #$27
.,E581 E8       INX
.,E582 B4 D9    LDY $D9,X       LDTB1
.,E584 30 06    BMI $E58C
.,E586 18       CLC
.,E587 69 28    ADC #$28
.,E589 E8       INX
.,E58A 10 F6    BPL $E582
.,E58C 85 D5    STA $D5         store in LMNX, physical screen line length
.,E58E 4C 24 EA JMP $EA24       sync color pointer
.,E591 E4 C9    CPX $C9         read LXSP, chech cursor at start of input
.,E593 F0 03    BEQ $E598
.,E595 4C ED E6 JMP $E6ED       retreat cursor
.,E598 60       RTS

.,E599 EA       NOP             A free byte!!!

                                *** SET I/O DEFAULTS
                                The default output device is set to 3 (screen), and the
                                default input device is set to 0 (keyboard). The VIC chip
                                registers are set from the video chip setup table. The
                                cursor is then set to the home position.
.,E59A 20 A0 E5 JSR $E5A0       set I/O defaults
.,E59D 4C 66 E5 JMP $E566       home cursor and exit routine
.,E5A0 A9 03    LDA #$03
.,E5A2 85 9A    STA $9A         DFLTO, default output device - screen
.,E5A4 A9 00    LDA #$00
.,E5A6 85 99    STA $99         DFLTN, default input device - keyboard
.,E5A8 A2 2F    LDX #$2F
.,E5AA BD B8 EC LDA $ECB8,X     VIC chip setup table
.,E5AD 9D FF CF STA $CFFF,X     VIC chip I/O registers
.,E5B0 CA       DEX             next
.,E5B1 D0 F7    BNE $E5AA       till ready
.,E5B3 60       RTS

                                *** LP2: GET CHARACTER FROM KEYBOARD BUFFER
                                It is assumed that there is at leaset one character in the
                                keyboard buffer. This character is obtained and the rest
                                of the queue is moved up one by one to overwrite it. On
                                exit, the character is in (A).
.,E5B4 AC 77 02 LDY $0277       read KEYD, first character in keyboard buffer queue
.,E5B7 A2 00    LDX #$00
.,E5B9 BD 78 02 LDA $0278,X     overwrite with next in queue
.,E5BC 9D 77 02 STA $0277,X
.,E5BF E8       INX
.,E5C0 E4 C6    CPX $C6         compare with NDX, number of characters in queue
.,E5C2 D0 F5    BNE $E5B9       till all characters are moved
.,E5C4 C6 C6    DEC $C6         decrement NDX
.,E5C6 98       TYA             transfer read character to (A)
.,E5C7 58       CLI             enable interrupt
.,E5C8 18       CLC
.,E5C9 60       RTS

                                *** INPUT FROM KEYBOARD
                                This routine uses the previous routine to get characters
                                from the keyboard buffer. Each character is output to the
                                screen, unless it is <shift/RUN>. If so, the contents of
                                the keyboard buffer is replaced with LOAD <CR> RUN <CR>.
                                The routine ends when a carriage routine is encountered.
.,E5CA 20 16 E7 JSR $E716       output to screen
.,E5CD A5 C6    LDA $C6         read NDX, number of characters in keyboard queue
.,E5CF 85 CC    STA $CC         BLNSW, cursor blink enable
.,E5D1 8D 92 02 STA $0292       AUTODN, auto scroll down flag
.,E5D4 F0 F7    BEQ $E5CD       loop till key is pressed
.,E5D6 78       SEI             disable interrupt
.,E5D7 A5 CF    LDA $CF         BLNON, last cursor blink (on/off)
.,E5D9 F0 0C    BEQ $E5E7
.,E5DB A5 CE    LDA $CE         GDBLN, character under cursor
.,E5DD AE 87 02 LDX $0287       GDCOL, background color under cursor
.,E5E0 A0 00    LDY #$00
.,E5E2 84 CF    STY $CF         clear BLNON
.,E5E4 20 13 EA JSR $EA13       print to screen
.,E5E7 20 B4 E5 JSR $E5B4       Get character from keyboard buffer
.,E5EA C9 83    CMP #$83        test if <shift/RUN> is pressed
.,E5EC D0 10    BNE $E5FE       nope
.,E5EE A2 09    LDX #$09        transfer 'LOAD <CR> RUN <CR>' to keyboard buffer
.,E5F0 78       SEI
.,E5F1 86 C6    STX $C6         store #9 in NDX, characters in buffer
.,E5F3 BD E6 EC LDA $ECE6,X     'LOAD <CR> RUN <CR>' message in ROM
.,E5F6 9D 76 02 STA $0276,X     store in keyboard buffer
.,E5F9 CA       DEX
.,E5FA D0 F7    BNE $E5F3       all nine characters
.,E5FC F0 CF    BEQ $E5CD       allways jump
.,E5FE C9 0D    CMP #$0D        carriage return pressed?
.,E600 D0 C8    BNE $E5CA       nope, go to start
.,E602 A4 D5    LDY $D5         get LNMX, screen line length
.,E604 84 D0    STY $D0         CRSV, flag input/get from keyboard
.,E606 B1 D1    LDA ($D1),Y     PNT, screen address
.,E608 C9 20    CMP #$20        space?
.,E60A D0 03    BNE $E60F       nope
.,E60C 88       DEY
.,E60D D0 F7    BNE $E606       next
.,E60F C8       INY
.,E610 84 C8    STY $C8         store in INDX, end of logical line for input
.,E612 A0 00    LDY #$00
.,E614 8C 92 02 STY $0292       AUTODN
.,E617 84 D3    STY $D3         PNTR, cursor column
.,E619 84 D4    STY $D4         QTSW, reset quoute mode
.,E61B A5 C9    LDA $C9         LXSP, corsor X/Y position
.,E61D 30 1B    BMI $E63A
.,E61F A6 D6    LDX $D6         TBLX, cursor line number
.,E621 20 ED E6 JSR $E6ED       retreat cursor
.,E624 E4 C9    CPX $C9         LXSP
.,E626 D0 12    BNE $E63A
.,E628 A5 CA    LDA $CA
.,E62A 85 D3    STA $D3         PNTR
.,E62C C5 C8    CMP $C8         INDX
.,E62E 90 0A    BCC $E63A
.,E630 B0 2B    BCS $E65D

                                *** INPUT FROM SCREEN OR KEYBOARD
                                This routine is used by INPUT to input data from devices
                                not on the serial bus, ie. from screen or keyboard. On
                                entry (X) and (Y) registers are preserved. A test is made
                                to determine which device the input is to be from. If it
                                is the screen, then quotes and <RVS> are tested for and
                                the character is echoed on the screen. Keyboard inputs
                                make use of the previous routine.
.,E632 98       TYA             preserve (X) and (Y) registers
.,E633 48       PHA
.,E634 8A       TXA
.,E635 48       PHA
.,E636 A5 D0    LDA $D0         CRSW, INPUT/GET from keyboard or screen
.,E638 F0 93    BEQ $E5CD       input from keyboard
.,E63A A4 D3    LDY $D3         PNTR, cursor column
.,E63C B1 D1    LDA ($D1),Y     read from current screen address
.,E63E 85 D7    STA $D7         temp store
.,E640 29 3F    AND #$3F
.,E642 06 D7    ASL $D7
.,E644 24 D7    BIT $D7
.,E646 10 02    BPL $E64A
.,E648 09 80    ORA #$80
.,E64A 90 04    BCC $E650
.,E64C A6 D4    LDX $D4         QTSW, editor in quotes mode
.,E64E D0 04    BNE $E654       yepp
.,E650 70 02    BVS $E654
.,E652 09 40    ORA #$40
.,E654 E6 D3    INC $D3         PNTR
.,E656 20 84 E6 JSR $E684       do quotes test
.,E659 C4 C8    CPY $C8         INDX, end of logical line for input
.,E65B D0 17    BNE $E674
.,E65D A9 00    LDA #$00
.,E65F 85 D0    STA $D0         CRSW
.,E661 A9 0D    LDA #$0D
.,E663 A6 99    LDX $99         DFLTN, default input device
.,E665 E0 03    CPX #$03        screen
.,E667 F0 06    BEQ $E66F       yes
.,E669 A6 9A    LDX $9A         DFLTO, default output device
.,E66B E0 03    CPX #$03        screen
.,E66D F0 03    BEQ $E672       yes
.,E66F 20 16 E7 JSR $E716       output to screen
.,E672 A9 0D    LDA #$0D
.,E674 85 D7    STA $D7
.,E676 68       PLA
.,E677 AA       TAX             restore (X) and (Y) registers
.,E678 68       PLA
.,E679 A8       TAY
.,E67A A5 D7    LDA $D7
.,E67C C9 DE    CMP #$DE
.,E67E D0 02    BNE $E682
.,E680 A9 FF    LDA #$FF
.,E682 18       CLC
.,E683 60       RTS

                                *** QUOTES TSET
                                On entry, (A) holds the character to be tested. If (A)
                                holds ASCII quotes, then the quotes flag is toggled.
.,E684 C9 22    CMP #$22        ASCII quotes (")
.,E686 D0 08    BNE $E690       nope, return
.,E688 A5 D4    LDA $D4         QTSW, quotes mode flag
.,E68A 49 01    EOR #$01        toggle on/off
.,E68C 85 D4    STA $D4         store
.,E68E A9 22    LDA #$22        restore (A) to #$22
.,E690 60       RTS

                                *** SET UP SCREEN PRINT
                                The RVS flag is tested to see if reversed characters are
                                to be printed. If insert mode is on, the insert counter is
                                decremented by one. When in insert mode, all characters
                                will be displayd, ie. DEL RVS etc. The character colour is
                                placed in (X) and the character is printed to the scrren
                                and the cursor advanced.
.,E691 09 40    ORA #$40
.,E693 A6 C7    LDX $C7         test RVS, flag for reversed characters
.,E695 F0 02    BEQ $E699       nope
.,E697 09 80    ORA #$80        set bit 7 to reverse character
.,E699 A6 D8    LDX $D8         test INSRT, flag for insert mode
.,E69B F0 02    BEQ $E69F       nope
.,E69D C6 D8    DEC $D8         decrement number of characters left to insert
.,E69F AE 86 02 LDX $0286       get COLOR, current character colour code
.,E6A2 20 13 EA JSR $EA13       print to screen
.,E6A5 20 B6 E6 JSR $E6B6       advance cursor
.,E6A8 68       PLA
.,E6A9 A8       TAY
.,E6AA A5 D8    LDA $D8         INSRT
.,E6AC F0 02    BEQ $E6B0
.,E6AE 46 D4    LSR $D4
.,E6B0 68       PLA
.,E6B1 AA       TAX
.,E6B2 68       PLA
.,E6B3 18       CLC
.,E6B4 58       CLI
.,E6B5 60       RTS

                                *** ADVANCE CURSOR
                                The cursor is advanced one position on the screen. If this
                                puts it beyond the 40th column, then it is placed at the
                                beginning of the next line. If the length of that line is
                                less than 80, then this new line is linked to the previous
                                one. A space is opened if data already exists on the new
                                line. If the cursor has reached the bottom of the screen,
                                then the screen is scrolled down.
.,E6B6 20 B3 E8 JSR $E8B3       check line increment
.,E6B9 E6 D3    INC $D3         increment PNTR, cursor column on current line
.,E6BB A5 D5    LDA $D5         LNMX, physical screen line length
.,E6BD C5 D3    CMP $D3         compare to PNTR
.,E6BF B0 3F    BCS $E700       not beyond end of line, exit
.,E6C1 C9 4F    CMP #$4F        $4f = 79
.,E6C3 F0 32    BEQ $E6F7       put cursor on new logical line
.,E6C5 AD 92 02 LDA $0292       AUTODN, auto scroll down flag
.,E6C8 F0 03    BEQ $E6CD       auto scroll is on
.,E6CA 4C 67 E9 JMP $E967       open a space on the screen
.,E6CD A6 D6    LDX $D6         read TBLX, current line number
.,E6CF E0 19    CPX #$19        $19 = 25
.,E6D1 90 07    BCC $E6DA       less than 25
.,E6D3 20 EA E8 JSR $E8EA       scroll down
.,E6D6 C6 D6    DEC $D6         place cursor on line 24
.,E6D8 A6 D6    LDX $D6
.,E6DA 16 D9    ASL $D9,X       clear bit7 in LDTB1 to indicate that it is line 2
.,E6DC 56 D9    LSR $D9,X       in the logical line
.,E6DE E8       INX             next line
.,E6DF B5 D9    LDA $D9,X       set bit7 in LDTB1 to indicate that it is line 1
.,E6E1 09 80    ORA #$80        in the logical line
.,E6E3 95 D9    STA $D9,X
.,E6E5 CA       DEX
.,E6E6 A5 D5    LDA $D5         add $28 (40) to LNMX to allow 80 characters
.,E6E8 18       CLC             on the logical line
.,E6E9 69 28    ADC #$28
.,E6EB 85 D5    STA $D5

                                *** RETREAT CURSOR
                                The screen line link table is searched, and then the start
                                of line is set. The rest of the routine sets the cursor
                                onto the next line for the previous routine.
.,E6ED B5 D9    LDA $D9,X       LDTB1, screen line link table
.,E6EF 30 03    BMI $E6F4       test bit7
.,E6F1 CA       DEX             next line
.,E6F2 D0 F9    BNE $E6ED       till all are done
.,E6F4 4C F0 E9 JMP $E9F0       set start of line
.,E6F7 C6 D6    DEC $D6         decrement TBLX, cursor line
.,E6F9 20 7C E8 JSR $E87C       goto next line
.,E6FC A9 00    LDA #$00
.,E6FE 85 D3    STA $D3         set PNTR, the cursor column, to zero
.,E700 60       RTS

                                *** BACK ON TO PREVIOUS LINE
                                This routine is called when using <DEL> and <cursor LEFT>.
                                The line number is tested, and if the cursor is already on
                                the top line, then no further action is taken. The screen
                                pointers are set up and the cursor placed at the end of
                                the previous line.
.,E701 A6 D6    LDX $D6         test TBLX, physical line number
.,E703 D0 06    BNE $E70B       if not on top line, branch
.,E705 86 D3    STX $D3         set PNTR to zero as well
.,E707 68       PLA
.,E708 68       PLA
.,E709 D0 9D    BNE $E6A8       allways jump
.,E70B CA       DEX             decrement TBLX
.,E70C 86 D6    STX $D6         and store
.,E70E 20 6C E5 JSR $E56C       set screen pointers
.,E711 A4 D5    LDY $D5         get LNMX
.,E713 84 D3    STY $D3         and store in PNTR
.,E715 60       RTS

                                *** OUTPUT TO SCREEN
                                This routine is part of the main KERNAL CHROUT routine. It
                                prints CBM ASCII characters to the screen and takes care
                                of all the screen editing characters. The cursor is
                                automatically updated and scrolling occurs if necessary.
                                On entry, (A) must hold the character to be output. On
                                entry all registers are stored on the stack. For
                                convinience, the routine is slpit into sections showing
                                the processing of both shifted and unshifted character.
.,E716 48       PHA             store (A), (X) and (Y) on stack
.,E717 85 D7    STA $D7         temp store
.,E719 8A       TXA
.,E71A 48       PHA
.,E71B 98       TYA
.,E71C 48       PHA
.,E71D A9 00    LDA #$00
.,E71F 85 D0    STA $D0         store in CRSW
.,E721 A4 D3    LDY $D3         PNTR, cursor positions on line
.,E723 A5 D7    LDA $D7         retrieve from temp store
.,E725 10 03    BPL $E72A       do unshifted characters
.,E727 4C D4 E7 JMP $E7D4       do shifted characters

                                UNSHIFTED CHARACTERS. Ordinary unshifted ASCII characters
                                and PET graphics are output directly to the screen. The
                                following control codes are trapped and precessed:
                                <RETURN>, <DEL>, <CRSR RIGHT>, <CRSR DOWN>. If either
                                insert mode is on or quotes are open (except for <DEL>)
                                then the control characters are not processed, but output
                                as reversed ASCII literals.
.,E72A C9 0D    CMP #$0D        <RETURN>?
.,E72C D0 03    BNE $E731       nope
.,E72E 4C 91 E8 JMP $E891       execute return
.,E731 C9 20    CMP #$20        <SPACE>?
.,E733 90 10    BCC $E745
.,E735 C9 60    CMP #$60        #$60, first PET graphic character?
.,E737 90 04    BCC $E73D
.,E739 29 DF    AND #$DF        %11011111
.,E73B D0 02    BNE $E73F
.,E73D 29 3F    AND #$3F        %00111111
.,E73F 20 84 E6 JSR $E684       do quotes test
.,E742 4C 93 E6 JMP $E693       setup screen print
.,E745 A6 D8    LDX $D8         INSRT, insert mode flag
.,E747 F0 03    BEQ $E74C       mode not set
.,E749 4C 97 E6 JMP $E697       output reversed charcter
.,E74C C9 14    CMP #$14        <DEL>?
.,E74E D0 2E    BNE $E77E       nope
.,E750 98       TYA             (Y) holds cursor column
.,E751 D0 06    BNE $E759       not start of line
.,E753 20 01 E7 JSR $E701       back on previous line
.,E756 4C 73 E7 JMP $E773
.,E759 20 A1 E8 JSR $E8A1       check line decrement
.,E75C 88       DEY             decrement cursor column
.,E75D 84 D3    STY $D3         and store in PNTR
.,E75F 20 24 EA JSR $EA24       syncronise colour pointer
.,E762 C8       INY             copy character at cursor position (Y+1) to (Y)
.,E763 B1 D1    LDA ($D1),Y     read character
.,E765 88       DEY
.,E766 91 D1    STA ($D1),Y     and store it one position back
.,E768 C8       INY
.,E769 B1 F3    LDA ($F3),Y     read character  colour
.,E76B 88       DEY
.,E76C 91 F3    STA ($F3),Y     and store it one position back
.,E76E C8       INY             more characters to move
.,E76F C4 D5    CPY $D5         compare with LNMX, length of physical screen line
.,E771 D0 EF    BNE $E762       if not equal, move more characters
.,E773 A9 20    LDA #$20
.,E775 91 D1    STA ($D1),Y     store <SPACE> at end of line
.,E777 AD 86 02 LDA $0286       COLOR, current character colour
.,E77A 91 F3    STA ($F3),Y     store colour at end of line
.,E77C 10 4D    BPL $E7CB       allways jump
.,E77E A6 D4    LDX $D4         QTSW, editor in quotes mode
.,E780 F0 03    BEQ $E785       no
.,E782 4C 97 E6 JMP $E697       output reversed character
.,E785 C9 12    CMP #$12        <RVS>?
.,E787 D0 02    BNE $E78B       no
.,E789 85 C7    STA $C7         RVS, reversed character output flag
.,E78B C9 13    CMP #$13        <HOME>?
.,E78D D0 03    BNE $E792       no
.,E78F 20 66 E5 JSR $E566       home cursor
.,E792 C9 1D    CMP #$1D        <CRSR RIGHT>?
.,E794 D0 17    BNE $E7AD       nope
.,E796 C8       INY             increment (Y), internal counter for column
.,E797 20 B3 E8 JSR $E8B3       check line increment
.,E79A 84 D3    STY $D3         store (Y) in PNTR
.,E79C 88       DEY             decrement (Y)
.,E79D C4 D5    CPY $D5         and compare to LNMX
.,E79F 90 09    BCC $E7AA       not exceeded line length
.,E7A1 C6 D6    DEC $D6         TBLX, current physical line number
.,E7A3 20 7C E8 JSR $E87C       goto next line
.,E7A6 A0 00    LDY #$00
.,E7A8 84 D3    STY $D3         set PNTR to zero, cursor to the left
.,E7AA 4C A8 E6 JMP $E6A8       finish screen print
.,E7AD C9 11    CMP #$11        <CRSR DOWN>?
.,E7AF D0 1D    BNE $E7CE       no
.,E7B1 18       CLC             prepare for add
.,E7B2 98       TYA             (Y) holds cursor column
.,E7B3 69 28    ADC #$28        add 40 to next line
.,E7B5 A8       TAY             to (Y)
.,E7B6 E6 D6    INC $D6         increment TBLX, physical line number
.,E7B8 C5 D5    CMP $D5         compare to LNMX
.,E7BA 90 EC    BCC $E7A8       finish screen print
.,E7BC F0 EA    BEQ $E7A8       finish screen print
.,E7BE C6 D6    DEC $D6         restore TBLX
.,E7C0 E9 28    SBC #$28
.,E7C2 90 04    BCC $E7C8
.,E7C4 85 D3    STA $D3         store PNTR
.,E7C6 D0 F8    BNE $E7C0
.,E7C8 20 7C E8 JSR $E87C       go to next line
.,E7CB 4C A8 E6 JMP $E6A8       finish screen print
.,E7CE 20 CB E8 JSR $E8CB       set colour code
.,E7D1 4C 44 EC JMP $EC44       do graphics/text control

                                SHIFTED CHARACTERS. These are dealt with in the following
                                order: Shifted ordinart ASCII and PET graphics characters,
                                <shift RETURN>, <INST>, <CRSR UP>, <RVS OFF>, <CRSR LEFT>,
                                <CLR>. If either insert mode is on, or quotes are open,
                                then the control character is not processed but reversed
                                ASCII literal is printed.
.,E7D4 29 7F    AND #$7F        clear bit7
.,E7D6 C9 7F    CMP #$7F        compare to #$7f
.,E7D8 D0 02    BNE $E7DC       not equal
.,E7DA A9 5E    LDA #$5E        if #$7f, load #$5e
.,E7DC C9 20    CMP #$20        ASCII <SPACE>?
.,E7DE 90 03    BCC $E7E3
.,E7E0 4C 91 E6 JMP $E691       set up screen print
.,E7E3 C9 0D    CMP #$0D        <RETURN>?
.,E7E5 D0 03    BNE $E7EA       nope
.,E7E7 4C 91 E8 JMP $E891       do return
.,E7EA A6 D4    LDX $D4         read QTSW
.,E7EC D0 3F    BNE $E82D       if quotes mode, jump
.,E7EE C9 14    CMP #$14        <INST>?
.,E7F0 D0 37    BNE $E829       nope
.,E7F2 A4 D5    LDY $D5         LNMX
.,E7F4 B1 D1    LDA ($D1),Y     get screen character
.,E7F6 C9 20    CMP #$20        space?
.,E7F8 D0 04    BNE $E7FE       nope
.,E7FA C4 D3    CPY $D3         PNTR equal to LNMX
.,E7FC D0 07    BNE $E805       nope
.,E7FE C0 4F    CPY #$4F        #$4f=79, last character
.,E800 F0 24    BEQ $E826       end of logical line, can not insert
.,E802 20 65 E9 JSR $E965       open space on line
.,E805 A4 D5    LDY $D5         LNMX
.,E807 20 24 EA JSR $EA24       syncronise colour pointer
.,E80A 88       DEY             prepare for move
.,E80B B1 D1    LDA ($D1),Y     read character at pos (Y)
.,E80D C8       INY
.,E80E 91 D1    STA ($D1),Y     and move one step to the right
.,E810 88       DEY
.,E811 B1 F3    LDA ($F3),Y     read character colour
.,E813 C8       INY
.,E814 91 F3    STA ($F3),Y     move one step to the right
.,E816 88       DEY             decrement counter
.,E817 C4 D3    CPY $D3         compare with PNTR
.,E819 D0 EF    BNE $E80A       till all characters right of cursor are moved
.,E81B A9 20    LDA #$20        <SPACE>, ASCII #$20
.,E81D 91 D1    STA ($D1),Y     store at new character position
.,E81F AD 86 02 LDA $0286       COLOR, current character colour
.,E822 91 F3    STA ($F3),Y     store at new colour position
.,E824 E6 D8    INC $D8         INSRT FLAG
.,E826 4C A8 E6 JMP $E6A8       finish screen print
.,E829 A6 D8    LDX $D8         INSRT FLAG
.,E82B F0 05    BEQ $E832       insert mode is off
.,E82D 09 40    ORA #$40
.,E82F 4C 97 E6 JMP $E697       set up screen print
.,E832 C9 11    CMP #$11        <CRSR UP>?
.,E834 D0 16    BNE $E84C       nope
.,E836 A6 D6    LDX $D6         read TBLX
.,E838 F0 37    BEQ $E871       at topline, do nothing
.,E83A C6 D6    DEC $D6         else decrement TBLX
.,E83C A5 D3    LDA $D3         PNTR
.,E83E 38       SEC             prepare for substract
.,E83F E9 28    SBC #$28        back 40 columns for double line
.,E841 90 04    BCC $E847       skip
.,E843 85 D3    STA $D3         store PNTR
.,E845 10 2A    BPL $E871       finish screen print
.,E847 20 6C E5 JSR $E56C       set screen pointer
.,E84A D0 25    BNE $E871       finish screen print
.,E84C C9 12    CMP #$12        <RVS OFF>?
.,E84E D0 04    BNE $E854       nope
.,E850 A9 00    LDA #$00
.,E852 85 C7    STA $C7         RVS, disable reverse print
.,E854 C9 1D    CMP #$1D        <CRSR LEFT>?
.,E856 D0 12    BNE $E86A       nope
.,E858 98       TYA             (Y) holds cursor column
.,E859 F0 09    BEQ $E864       at first position
.,E85B 20 A1 E8 JSR $E8A1       check line decrement
.,E85E 88       DEY             one position left
.,E85F 84 D3    STY $D3         store in PNTR
.,E861 4C A8 E6 JMP $E6A8       finish screen print
.,E864 20 01 E7 JSR $E701       back to previous line
.,E867 4C A8 E6 JMP $E6A8       finish screen print
.,E86A C9 13    CMP #$13        <CLR>?
.,E86C D0 06    BNE $E874       nope
.,E86E 20 44 E5 JSR $E544       clear screen
.,E871 4C A8 E6 JMP $E6A8       finish screen print
.,E874 09 80    ORA #$80
.,E876 20 CB E8 JSR $E8CB       set colour code
.,E879 4C 4F EC JMP $EC4F       set graphics/text mode

                                *** GO TO NEXT LINE
                                The cursor is placed at the start of the next logical
                                screen line. This involves moving down two lines for a
                                linked line. If this places the cursor below the bottom of
                                the screen, then the screen is scrolled.
.,E87C 46 C9    LSR $C9         LXSP, cursor X-Y position
.,E87E A6 D6    LDX $D6         TBLX, current line number
.,E880 E8       INX             next line
.,E881 E0 19    CPX #$19        26th line
.,E883 D0 03    BNE $E888       nope, scroll is not needed
.,E885 20 EA E8 JSR $E8EA       scroll down
.,E888 B5 D9    LDA $D9,X       test LTDB1, screen line link table if first of two
.,E88A 10 F4    BPL $E880       yes, jump down another line
.,E88C 86 D6    STX $D6         store in TBLX
.,E88E 4C 6C E5 JMP $E56C       set screen pointers

                                *** OUTPUT <CARRIAGE RETURN>
                                All editor modes are swithed off and the cursor placed at
                                the start of the next line.
.,E891 A2 00    LDX #$00
.,E893 86 D8    STX $D8         INSRT, disable insert mode
.,E895 86 C7    STX $C7         RVS, disable reversed mode
.,E897 86 D4    STX $D4         QTSW, disable quotes mode
.,E899 86 D3    STX $D3         PNTR, put cursor at first column
.,E89B 20 7C E8 JSR $E87C       go to next line
.,E89E 4C A8 E6 JMP $E6A8       finish screen print

                                *** CHECK LINE DECREMENT
                                When the cursor is at the beginning of a screen line, if
                                it is moved backwards, this routine places the cursor at
                                the end of the line above. It tests both column 0 and
                                column 40.
.,E8A1 A2 02    LDX #$02        test if PNTR is at the first column
.,E8A3 A9 00    LDA #$00        yepp
.,E8A5 C5 D3    CMP $D3         add $28 (40)
.,E8A7 F0 07    BEQ $E8B0       to test if cursor is at line two in the logical line
.,E8A9 18       CLC
.,E8AA 69 28    ADC #$28        test two lines
.,E8AC CA       DEX
.,E8AD D0 F6    BNE $E8A5       decrement line number
.,E8AF 60       RTS
.,E8B0 C6 D6    DEC $D6
.,E8B2 60       RTS

                                *** CHECK LINE INCREMENT
                                When the cursor is at the end of the screen, if it is
                                moved forward, this routine places the cursor at the start
                                of the line below.
.,E8B3 A2 02    LDX #$02        start by testing position $27 (39)
.,E8B5 A9 27    LDA #$27        compare with PNTR
.,E8B7 C5 D3    CMP $D3         brach if equal, and move cursor down
.,E8B9 F0 07    BEQ $E8C2       else, add $28 to test next physical line
.,E8BB 18       CLC
.,E8BC 69 28    ADC #$28        two lines to test
.,E8BE CA       DEX
.,E8BF D0 F6    BNE $E8B7       return here without moving cursor down
.,E8C1 60       RTS             get TBLX
.,E8C2 A6 D6    LDX $D6         and test if at the 25th line
.,E8C4 E0 19    CPX #$19        yepp, return without moving down
.,E8C6 F0 02    BEQ $E8CA       increment TBLX
.,E8C8 E6 D6    INC $D6
.,E8CA 60       RTS

                                *** SET COLOUR CODE
                                This routine is called by the output to screen routine.
                                The Commodore ASCII code in (A) is compared with the ASCII
                                colout code table. If a match is found, then the table
                                offset (and hence the colour value) is stored in COLOR.
.,E8CB A2 0F    LDX #$0F        16 values to be tested
.,E8CD DD DA E8 CMP $E8DA,X     compare with colour code table
.,E8D0 F0 04    BEQ $E8D6       found, jump
.,E8D2 CA       DEX             next colour in table
.,E8D3 10 F8    BPL $E8CD       till all 16 are tested
.,E8D5 60       RTS             if not found, return
.,E8D6 8E 86 02 STX $0286       if found, store code in COLOR
.,E8D9 60       RTS

                                *** COLOUR CODE TABLE
                                This is a table containing 16 Commodore ASCII codes
                                representing the 16 available colours. Thus red is
                                represented as $1c in the table, and would be obtained by
                                PRINT CHR$(28), or poke 646,2.
.:E8DA 90                       color0, black
.:E8DB 05                       color1, white
.:E8DC 1C                       color2, red
.:E8DD 9F                       color3, cyan
.:E8DE 9C                       color4, purple
.:E8DF 1E                       color5, green
.:E8E0 1F                       color6, blue
.:E8E1 9E                       color7, yellow
.:E8E2 81                       color8, orange
.:E8E3 95                       color9, brown
.:E8E4 96                       colorA, pink
.:E8E5 97                       colorB, grey1
.:E8E6 98                       colorC, grey2
.:E8E7 99                       colorD, light green
.:E8E8 9A                       colorE, light blue
.:E8E9 9B                       colorF, grey3

                                *** SCROLL SCREEN
                                This routine scrolls the screen down by one line. If the
                                top two lines are linked togeather, then the scroll down
                                is repeated. The screen line link pointers are updated,
                                each screen line is cleared and the line below is moved
                                up. The keyboard is directly read from CIA#1, and the
                                routine tests if <CTRL> is pressed.
.,E8EA A5 AC    LDA $AC         temp store SAL on stack
.,E8EC 48       PHA
.,E8ED A5 AD    LDA $AD
.,E8EF 48       PHA
.,E8F0 A5 AE    LDA $AE         temp store EAL on stack
.,E8F2 48       PHA
.,E8F3 A5 AF    LDA $AF
.,E8F5 48       PHA
.,E8F6 A2 FF    LDX #$FF
.,E8F8 C6 D6    DEC $D6         decrement TBLX
.,E8FA C6 C9    DEC $C9         decrement LXSP
.,E8FC CE A5 02 DEC $02A5       temp store for line index
.,E8FF E8       INX
.,E900 20 F0 E9 JSR $E9F0       set start of line (X)
.,E903 E0 18    CPX #$18
.,E905 B0 0C    BCS $E913
.,E907 BD F1 EC LDA $ECF1,X     read low-byte screen addresses
.,E90A 85 AC    STA $AC
.,E90C B5 DA    LDA $DA,X
.,E90E 20 C8 E9 JSR $E9C8       move a screen line
.,E911 30 EC    BMI $E8FF
.,E913 20 FF E9 JSR $E9FF       clear a screen line
.,E916 A2 00    LDX #$00
.,E918 B5 D9    LDA $D9,X       calcuate new screen line link table
.,E91A 29 7F    AND #$7F        clear bit7
.,E91C B4 DA    LDY $DA,X
.,E91E 10 02    BPL $E922
.,E920 09 80    ORA #$80        set bit7
.,E922 95 D9    STA $D9,X       store new value in table
.,E924 E8       INX             next line
.,E925 E0 18    CPX #$18        till all 25 are done
.,E927 D0 EF    BNE $E918
.,E929 A5 F1    LDA $F1         bottom line link
.,E92B 09 80    ORA #$80        unlink it
.,E92D 85 F1    STA $F1         and store back
.,E92F A5 D9    LDA $D9         test top line link
.,E931 10 C3    BPL $E8F6       line is linked, scroll again
.,E933 E6 D6    INC $D6         increment TBLX
.,E935 EE A5 02 INC $02A5

.,E938 A9 7F    LDA #$7F
.,E93A 8D 00 DC STA $DC00
.,E93D AD 01 DC LDA $DC01       read keyboard decode column
.,E940 C9 FB    CMP #$FB        <CTRL> pressed
.,E942 08       PHP
.,E943 A9 7F    LDA #$7F
.,E945 8D 00 DC STA $DC00
.,E948 28       PLP
.,E949 D0 0B    BNE $E956       nope, exit
.,E94B A0 00    LDY #$00
.,E94D EA       NOP
.,E94E CA       DEX
.,E94F D0 FC    BNE $E94D
.,E951 88       DEY
.,E952 D0 F9    BNE $E94D
.,E954 84 C6    STY $C6         clear NDX
.,E956 A6 D6    LDX $D6         read TBLX
.,E958 68       PLA             retrieve EAL
.,E959 85 AF    STA $AF
.,E95B 68       PLA
.,E95C 85 AE    STA $AE
.,E95E 68       PLA             retrieve SAL
.,E95F 85 AD    STA $AD
.,E961 68       PLA
.,E962 85 AC    STA $AC
.,E964 60       RTS             exit

                                *** OPEN A SPACE ON THE SCREEN
                                This routine opens a space on the screen for use with
                                <INST>. If needed, the screen is then scrolled down,
                                otherwise the screen line is moved and cleared. Finally
                                the screen line link table is adjusted and updated.
.,E965 A6 D6    LDX $D6         TBLX, current cursor line number
.,E967 E8       INX             test next
.,E968 B5 D9    LDA $D9,X       LDTB1, screen line link table
.,E96A 10 FB    BPL $E967
.,E96C 8E A5 02 STX $02A5       temp line for index
.,E96F E0 18    CPX #$18        bottom of screen
.,E971 F0 0E    BEQ $E981       yes
.,E973 90 0C    BCC $E981       above bottom line
.,E975 20 EA E8 JSR $E8EA       scroll screen down
.,E978 AE A5 02 LDX $02A5       temp line for index
.,E97B CA       DEX
.,E97C C6 D6    DEC $D6         TBLX
.,E97E 4C DA E6 JMP $E6DA       adjust link table and end
.,E981 A5 AC    LDA $AC         push SAL, scrolling pointer
.,E983 48       PHA
.,E984 A5 AD    LDA $AD
.,E986 48       PHA
.,E987 A5 AE    LDA $AE         push EAL, end of program
.,E989 48       PHA
.,E98A A5 AF    LDA $AF
.,E98C 48       PHA
.,E98D A2 19    LDX #$19
.,E98F CA       DEX
.,E990 20 F0 E9 JSR $E9F0       set start of line
.,E993 EC A5 02 CPX $02A5       temp line for index
.,E996 90 0E    BCC $E9A6
.,E998 F0 0C    BEQ $E9A6
.,E99A BD EF EC LDA $ECEF,X     screen line address table
.,E99D 85 AC    STA $AC         SAL
.,E99F B5 D8    LDA $D8,X       LDTB1
.,E9A1 20 C8 E9 JSR $E9C8       move screen line
.,E9A4 30 E9    BMI $E98F
.,E9A6 20 FF E9 JSR $E9FF       clear screen line
.,E9A9 A2 17    LDX #$17        fix screen line link table
.,E9AB EC A5 02 CPX $02A5       temp line for index
.,E9AE 90 0F    BCC $E9BF
.,E9B0 B5 DA    LDA $DA,X       LDTB1+1
.,E9B2 29 7F    AND #$7F
.,E9B4 B4 D9    LDY $D9,X       LDTB1
.,E9B6 10 02    BPL $E9BA
.,E9B8 09 80    ORA #$80
.,E9BA 95 DA    STA $DA,X
.,E9BC CA       DEX             next line
.,E9BD D0 EC    BNE $E9AB       till line zero
.,E9BF AE A5 02 LDX $02A5       temp line for index
.,E9C2 20 DA E6 JSR $E6DA       adjust link table
.,E9C5 4C 58 E9 JMP $E958       pull SAL and EAL

                                *** MOVE A SCREEN LINE
                                This routine synchronises colour transfer, and then moves
                                the screen line pointed to down, character by character.
                                The colour codes for each character are also moved in the
                                same way.
.,E9C8 29 03    AND #$03
.,E9CA 0D 88 02 ORA $0288       HIBASE, top of screen page
.,E9CD 85 AD    STA $AD         store >SAL, screen scroll pointer
.,E9CF 20 E0 E9 JSR $E9E0       synchronise colour transfer
.,E9D2 A0 27    LDY #$27        offset for character on screen line
.,E9D4 B1 AC    LDA ($AC),Y     move screen character
.,E9D6 91 D1    STA ($D1),Y
.,E9D8 B1 AE    LDA ($AE),Y     move character colour
.,E9DA 91 F3    STA ($F3),Y
.,E9DC 88       DEY             next character
.,E9DD 10 F5    BPL $E9D4       till all 40 are done
.,E9DF 60       RTS

                                *** SYNCHRONISE COLOUR TRANSFER
                                This routine setd up a temporary pointer in EAL to the
                                colour RAM address that corresponts to the temporary
                                screen address held in EAL.
.,E9E0 20 24 EA JSR $EA24       synchronise colour pointer
.,E9E3 A5 AC    LDA $AC         SAL, pointer for screen scroll
.,E9E5 85 AE    STA $AE         EAL
.,E9E7 A5 AD    LDA $AD
.,E9E9 29 03    AND #$03
.,E9EB 09 D8    ORA #$D8        setup colour ram to $d800
.,E9ED 85 AF    STA $AF
.,E9EF 60       RTS

                                *** SET START OF LINE
                                On entry, (X) holds the line number. The low byte of the
                                address is set from the ROM table, and the highbyte
                                derived from the screen link and HIBASE.
.,E9F0 BD F0 EC LDA $ECF0,X     table of screen line to bytes
.,E9F3 85 D1    STA $D1         <PNT, current screen line address
.,E9F5 B5 D9    LDA $D9,X       LDTB1, screen line link table
.,E9F7 29 03    AND #$03
.,E9F9 0D 88 02 ORA $0288       HIBASE, page of top screen
.,E9FC 85 D2    STA $D2         >PNT
.,E9FE 60       RTS

                                *** CLEAR SCREEN LINE
                                The start of line is set and the screen line is cleared by
                                filloing it with ASCII spaces. The corresponding line of
                                colour RAM is also cleared to the value held in COLOR.
.,E9FF A0 27    LDY #$27
.,EA01 20 F0 E9 JSR $E9F0       set start of line
.,EA04 20 24 EA JSR $EA24       synchronise colour pointer
.,EA07 20 DA E4 JSR $E4DA       reset character colour, to COLOR
.,EA0A A9 20    LDA #$20        ASCII space
.,EA0C 91 D1    STA ($D1),Y     store character on screen
.,EA0E 88       DEY             next
.,EA0F 10 F6    BPL $EA07       till hole line is done
.,EA11 60       RTS

.,EA12 EA       NOP             free byte

                                *** PRINT TO SCREEN
                                The colour pointer is synchronised, and the character in
                                (A) directly stored in the screen RAM. The character
                                colour in (X) is stored at the equivalent point in the
                                colour RAM.
.,EA13 A8       TAY             put print character in (Y)
.,EA14 A9 02    LDA #$02set the
.,EA16 85 CD    STA $CD         store in BLNCT, timer to toggle cursor
.,EA18 20 24 EA JSR $EA24       synchronise colour pointer
.,EA1B 98       TYA             print character back to (A)
.,EA1C A4 D3    LDY $D3         PNTR, cursor column on line
.,EA1E 91 D1    STA ($D1),Y     store character on screen
.,EA20 8A       TXA
.,EA21 91 F3    STA ($F3),Y     stor character colour
.,EA23 60       RTS

                                *** SYNCHRONISE COLOUR POINTER
                                The pointer to the colour RAM is set up according to the
                                current screen line address. This is done by reading the
                                current screen line address and modefying it to colour RAM
                                pointers and write it to USER at $f3/$f4
.,EA24 A5 D1    LDA $D1         copy screen line low byte
.,EA26 85 F3    STA $F3         to colour RAM low byte
.,EA28 A5 D2    LDA $D2         read'n modify the hi byte
.,EA2A 29 03    AND #$03
.,EA2C 09 D8    ORA #$D8
.,EA2E 85 F4    STA $F4         to suite the colour RAM
.,EA30 60       RTS

                                *** MAIN IRQ ENTRY POINT
                                This routine services the normal IRQ that jumps through
                                the hardware vector to $ff48, and then continues to the
                                CINV vector at $0314. First it checks if the <STOP> key
                                was pressed and updates the realtime clock. Next, the
                                cursor is updated (if it is enabled, BLNSW). The blink
                                counter, BLNCT, is decremented. When this reaches zero,
                                the cursor is toggled (blink on/off). Finally it scans
                                the keyboard. The processor registers are then restored
                                on exit.
.,EA31 20 EA FF JSR $FFEA       update realtime clock, routine UDTIM
.,EA34 A5 CC    LDA $CC         read BLNSW to see if cursor is enabled
.,EA36 D0 29    BNE $EA61       nope
.,EA38 C6 CD    DEC $CD         read BLNCT
.,EA3A D0 25    BNE $EA61       if zero, toggle cursor - else jump
.,EA3C A9 14    LDA #$14        blink speed
.,EA3E 85 CD    STA $CD         restore BLCNT
.,EA40 A4 D3    LDY $D3         get PNTR, cursor column
.,EA42 46 CF    LSR $CF         BLNON, flag last cursor blink on/off
.,EA44 AE 87 02 LDX $0287       get background colour under cursor, GDCOL
.,EA47 B1 D1    LDA ($D1),Y     get screen character
.,EA49 B0 11    BCS $EA5C       ?
.,EA4B E6 CF    INC $CF         increment BLNON
.,EA4D 85 CE    STA $CE         temporary store character under cursor
.,EA4F 20 24 EA JSR $EA24       synchronise colour pointer
.,EA52 B1 F3    LDA ($F3),Y     get colour under character
.,EA54 8D 87 02 STA $0287       store in GDCOL
.,EA57 AE 86 02 LDX $0286       get current COLOR
.,EA5A A5 CE    LDA $CE         retrieve character under cursor
.,EA5C 49 80    EOR #$80        toggle cursor by inverting character
.,EA5E 20 1C EA JSR $EA1C       print to screen by using part of 'print to screen'
.,EA61 A5 01    LDA $01
.,EA63 29 10    AND #$10
.,EA65 F0 0A    BEQ $EA71
.,EA67 A0 00    LDY #$00
.,EA69 84 C0    STY $C0
.,EA6B A5 01    LDA $01
.,EA6D 09 20    ORA #$20
.,EA6F D0 08    BNE $EA79
.,EA71 A5 C0    LDA $C0
.,EA73 D0 06    BNE $EA7B
.,EA75 A5 01    LDA $01
.,EA77 29 1F    AND #$1F
.,EA79 85 01    STA $01
.,EA7B 20 87 EA JSR $EA87       scan keyboard
.,EA7E AD 0D DC LDA $DC0D       clear CIA#1 I.C.R to enable next IRQ
.,EA81 68       PLA             restore (Y), (X), (A)
.,EA82 A8       TAY
.,EA83 68       PLA
.,EA84 AA       TAX
.,EA85 68       PLA
.,EA86 40       RTI             back to normal

                                *** SCNKEY: SCAN KEYBOARD
                                The KERNAL routine SCNKEY ($ff9f) jumps to this routine.
                                First, the shift-flag, SHFLAG, is cleared, and the
                                keyboard tested for nokey. The keyboard is set up as a
                                8 * 8 matrix, and is read one row at a time. $ff indicates
                                that no key has been pressed, and a zerobit, that one key
                                has been pressed.
.,EA87 A9 00    LDA #$00
.,EA89 8D 8D 02 STA $028D       clear SHFLAG
.,EA8C A0 40    LDY #$40
.,EA8E 84 CB    STY $CB
.,EA90 8D 00 DC STA $DC00       store in keyboard write register
.,EA93 AE 01 DC LDX $DC01       keyboard read register
.,EA96 E0 FF    CPX #$FF        no key pressed
.,EA98 F0 61    BEQ $EAFB       skip
.,EA9A A8       TAY
.,EA9B A9 81    LDA #$81        point KEYTAB vector to $eb81
.,EA9D 85 F5    STA $F5
.,EA9F A9 EB    LDA #$EB
.,EAA1 85 F6    STA $F6
.,EAA3 A9 FE    LDA #$FE        bit0 = 0
.,EAA5 8D 00 DC STA $DC00       will test first row in matrix
.,EAA8 A2 08    LDX #$08        scan 8 rows in matrix
.,EAAA 48       PHA             temp store
.,EAAB AD 01 DC LDA $DC01       read
.,EAAE CD 01 DC CMP $DC01       wait for value to settle (key bouncing)
.,EAB1 D0 F8    BNE $EAAB
.,EAB3 4A       LSR             test bit0
.,EAB4 B0 16    BCS $EACC       no key pressed
.,EAB6 48       PHA
.,EAB7 B1 F5    LDA ($F5),Y     get key from KEYTAB
.,EAB9 C9 05    CMP #$05        value less than 5
.,EABB B0 0C    BCS $EAC9       nope
.,EABD C9 03    CMP #$03        value = 3
.,EABF F0 08    BEQ $EAC9       nope
.,EAC1 0D 8D 02 ORA $028D
.,EAC4 8D 8D 02 STA $028D       store in SHFLAG
.,EAC7 10 02    BPL $EACB
.,EAC9 84 CB    STY $CB         store keynumber we pressed in SFDX
.,EACB 68       PLA
.,EACC C8       INY             key counter
.,EACD C0 41    CPY #$41        all 64 keys (8*8)
.,EACF B0 0B    BCS $EADC       jump if ready
.,EAD1 CA       DEX             next key in row
.,EAD2 D0 DF    BNE $EAB3       row ready
.,EAD4 38       SEC             prepare for rol
.,EAD5 68       PLA
.,EAD6 2A       ROL             next row
.,EAD7 8D 00 DC STA $DC00       store bit
.,EADA D0 CC    BNE $EAA8       always jump
.,EADC 68       PLA             clean up

                                *** PROCESS KEY IMAGE
                                This routine decodes the pressed key, and calcuates its
                                ASCII value, by use of the four tables. If the pressed key
                                is the same key as in the former interrupt, then the key-
                                repeat-section is entered. The routine tests the RPTFLG if
                                he key shall repeat. The new key is stored in the keyboard
                                buffer, and all pointers are uppdated.
.,EADD 6C 8F 02 JMP ($028F)     jump through KEYLOG vector, points to $eae0
.,EAE0 A4 CB    LDY $CB         SFDX, number of the key we pressed
.,EAE2 B1 F5    LDA ($F5),Y     get ASCII value from decode table
.,EAE4 AA       TAX             temp store
.,EAE5 C4 C5    CPY $C5         same key as former interrupt
.,EAE7 F0 07    BEQ $EAF0       yepp
.,EAE9 A0 10    LDY #$10        restore the repeat delay counter
.,EAEB 8C 8C 02 STY $028C       DELAY
.,EAEE D0 36    BNE $EB26       always jump
.,EAF0 29 7F    AND #$7F
.,EAF2 2C 8A 02 BIT $028A       RPTFLG, test repeat mode
.,EAF5 30 16    BMI $EB0D       repeat all keys
.,EAF7 70 49    BVS $EB42       repeat none - exit routine
.,EAF9 C9 7F    CMP #$7F
.,EAFB F0 29    BEQ $EB26
.,EAFD C9 14    CMP #$14        <DEL> key pressed
.,EAFF F0 0C    BEQ $EB0D       yepp...
.,EB01 C9 20    CMP #$20        <space> key pressed
.,EB03 F0 08    BEQ $EB0D       yepp...
.,EB05 C9 1D    CMP #$1D        <CRSR LEFT/RIGHT>
.,EB07 F0 04    BEQ $EB0D       yepp..
.,EB09 C9 11    CMP #$11        <CRSRS DOWN/UP>
.,EB0B D0 35    BNE $EB42       yepp..
.,EB0D AC 8C 02 LDY $028C       DELAY
.,EB10 F0 05    BEQ $EB17       skip
.,EB12 CE 8C 02 DEC $028C       decrement DELAY
.,EB15 D0 2B    BNE $EB42       end
.,EB17 CE 8B 02 DEC $028B       decremant KOUNT, repeat speed counter
.,EB1A D0 26    BNE $EB42       end
.,EB1C A0 04    LDY #$04
.,EB1E 8C 8B 02 STY $028B       init KOUNT
.,EB21 A4 C6    LDY $C6         read NDX, number of keys in keyboard queue
.,EB23 88       DEY
.,EB24 10 1C    BPL $EB42       end
.,EB26 A4 CB    LDY $CB         read SFDX
.,EB28 84 C5    STY $C5         store in LSTX
.,EB2A AC 8D 02 LDY $028D       read SHFLAG
.,EB2D 8C 8E 02 STY $028E       store in LSTSHF, last keyboard shift pattern
.,EB30 E0 FF    CPX #$FF        no valid key pressed
.,EB32 F0 0E    BEQ $EB42       end
.,EB34 8A       TXA
.,EB35 A6 C6    LDX $C6         NDX, number of keys in buffer
.,EB37 EC 89 02 CPX $0289       compare to XMAX, max numbers oc characters in buffer
.,EB3A B0 06    BCS $EB42       buffer is full, end
.,EB3C 9D 77 02 STA $0277,X     store new character in keyboard buffer
.,EB3F E8       INX             increment counter
.,EB40 86 C6    STX $C6         and store in NDX
.,EB42 A9 7F    LDA #$7F
.,EB44 8D 00 DC STA $DC00       keyboard write register
.,EB47 60       RTS             exit
.,EB48 AD 8D 02 LDA $028D       SHFLAG
.,EB4B C9 03    CMP #$03        <SHIFT> and <CBM> at the same time
.,EB4D D0 15    BNE $EB64       nope
.,EB4F CD 8E 02 CMP $028E       same as LSTSHF
.,EB52 F0 EE    BEQ $EB42       if so, end
.,EB54 AD 91 02 LDA $0291       read MODE, shift key enable flag
.,EB57 30 1D    BMI $EB76       end
.,EB59 AD 18 D0 LDA $D018       VIC memory control register
.,EB5C 49 02    EOR #$02        toggle character set, upper/lower case
.,EB5E 8D 18 D0 STA $D018       and store
.,EB61 4C 76 EB JMP $EB76       process key image
.,EB64 0A       ASL
.,EB65 C9 08    CMP #$08        test <CTRL>
.,EB67 90 02    BCC $EB6B       nope
.,EB69 A9 06    LDA #$06        set offset for ctrl
.,EB6B AA       TAX             to (X)
.,EB6C BD 79 EB LDA $EB79,X     read keyboard select vectors, low byte
.,EB6F 85 F5    STA $F5         store in KEYTAB, decode table vector
.,EB71 BD 7A EB LDA $EB7A,X     read keyboard select vectors, high byte
.,EB74 85 F6    STA $F6         KEYTAB+1
.,EB76 4C E0 EA JMP $EAE0       process key image

                                *** KEYBOARD SELECT VECTORS
                                This is a table of vectors pointing to the start of the
                                four keyboard decode tables.
.:EB79 81 EB                    vector to unshifted keyboard, $eb81
.:EB7B C2 EB                    vector to shifted keyboard, $ebc2
.:EB7D 03 EC                    vector to cbm keyboard, $ec03
.:EB7F 78 EC                    vector to ctrl keyboard, $ec78

                                *** KEYBOARD 1 - UNSHIFTED
                                This is the first of four keybboard decode tables. The
                                ASCII code for the key pressed is at the intersection of
                                the row (written to $dc00) and the column (read from
                                $dc01). The matrix values are shown below. Note that left
                                and right shift keys are seperated.
.:EB81 14 0D 1D 88 85 86 87 11
.:EB89 33 57 41 34 5A 53 45 01
.:EB91 35 52 44 36 43 46 54 58
.:EB99 37 59 47 38 42 48 55 56
.:EBA1 39 49 4A 30 4D 4B 4F 4E
.:EBA9 2B 50 4C 2D 2E 3A 40 2C
.:EBB1 5C 2A 3B 13 01 3D 5E 2F
.:EBB9 31 5F 04 32 20 02 51 03
.:EBC1 FF                       free byte

                                *** KEYBOARD 2 - SHIFTED
                                This is the second of four keyboard decode tables. The
                                ASCII code for the key pressed is at the intersection of
                                the row (written to $dc00) and the column (read from
                                $dc01). The matrix values are shown below.
.:EBC2 94 8D 9D 8C 89 8A 8B 91
.:EBCA 23 D7 C1 24 DA D3 C5 01
.:EBD2 25 D2 C4 26 C3 C6 D4 D8
.:EBDA 27 D9 C7 28 C2 C8 D5 D6
.:EBE2 29 C9 CA 30 CD CB CF CE
.:EBEA DB D0 CC DD 3E 5B BA 3C
.:EBF2 A9 C0 5D 93 01 3D DE 3F
.:EBFA 21 5F 04 22 A0 02 D1 83
.:EC02 FF                       free byte

                                *** KEYBOARD 3 - COMMODORE
                                This is the third of four keyboard decode tables. The
                                ASCII code for the key pressed is at the intersection of
                                the ro (written to $dc00) and hte column (read from
                                $dc01). The matrix values are shown below.
.:EC03 94 8D 9D 8C 89 8A 8B 91
.:EC0B 96 B3 B0 97 AD AE B1 01
.:EC13 98 B2 AC 99 BC BB A3 BD
.:EC1B 9A B7 A5 9B BF B4 B8 BE
.:EC23 29 A2 B5 30 A7 A1 B9 AA
.:EC2B A6 AF B6 DC 3E 5B A4 3C
.:EC33 A8 DF 5D 93 01 3D DE 3F
.:EC3B 81 5F 04 95 A0 02 AB 83
.:EC43 FF                       free byte

                                *** GRAPHICS / TEXT CONTROL
                                This routine is used to toggle between text and graphics
                                character set, and to enable/disable the <shift-CBM> keys.
                                The routine is called by the main 'output to screen'
                                routine, and (A) holds a CBM ASCII code on entry.
.,EC44 C9 0E    CMP #$0E        <switch to lower case>
.,EC46 D0 07    BNE $EC4F       nope
.,EC48 AD 18 D0 LDA $D018       VIC memory control register
.,EC4B 09 02    ORA #$02        set bit1
.,EC4D D0 09    BNE $EC58       allways branch
.,EC4F C9 8E    CMP #$8E        <switch to upper case>
.,EC51 D0 0B    BNE $EC5E       nope
.,EC53 AD 18 D0 LDA $D018       VIC memory control register
.,EC56 29 FD    AND #$FD        clear bit1
.,EC58 8D 18 D0 STA $D018       and store
.,EC5B 4C A8 E6 JMP $E6A8       finish screen print
.,EC5E C9 08    CMP #$08        <disable <shift-CBM>>
.,EC60 D0 07    BNE $EC69       nope
.,EC62 A9 80    LDA #$80
.,EC64 0D 91 02 ORA $0291       disable MODE
.,EC67 30 09    BMI $EC72       allways jump
.,EC69 C9 09    CMP #$09        <enable <shift-CBM>>
.,EC6B D0 EE    BNE $EC5B       nope, exit
.,EC6D A9 7F    LDA #$7F
.,EC6F 2D 91 02 AND $0291       enable MODE
.,EC72 8D 91 02 STA $0291       store MODE, enable/disable shift keys
.,EC75 4C A8 E6 JMP $E6A8       finish screen print

                                *** KEYBOARD 4 - CONTROL
                                This is the last keyboard decode table. The ASCII code for
                                the key pressed is at the intersection of the row (written
                                to $dc00) and the column (read from $dc01). The matrix
                                values are shown below.
                                A few special function are found in this table ie.
                                <ctrl H> - disables the upper/lower case switch
                                <ctrl I> - enables the upper/lower case switch
                                <ctrl S> - homes the cursor
                                <ctrl T> - delets character
                                Note that the italic keys only represent a ASCII code, and
                                not a CBM character.
.:EC78 FF FF FF FF FF FF FF FF
.:EC80 1C 17 01 9F 1A 13 05 FF
.:EC88 9C 12 04 1E 03 06 14 18
.:EC90 1F 19 07 9E 02 08 15 16
.:EC98 12 09 0A 92 0D 0B 0F 0E
.:ECA0 FF 10 0C FF FF 1B 00 FF
.:ECA8 1C FF 1D FF FF 1F 1E FF
.:ECB0 90 06 FF 05 FF FF 11 FF
.:ECB8 FF                       free byte

                                *** VIDEO CHIP SET UP TABLE
                                This is a table of the initial values for the VIC chip
                                registers at start up.
.:ECB9 00 00                    $d000/1, sprite0 - x,y cordinate
.:ECBB 00 00                    $d002/3, sprite1 - x,y cordinate
.:ECBD 00 00                    $d004/5, sprite2 - x,y cordinate
.:ECBF 00 00                    $d006/7, sprite3 - x,y cordinate
.:ECC1 00 00                    $d008/9, sprite4 - x,y cordinate
.:ECC3 00 00                    $d00a/b, sprite5 - x,y cordinate
.:ECC5 00 00                    $d00c/d, sprite6 - x,y cordinate
.:ECC7 00 00                    $d00e/f, sprite7 - x,y cordinate
.:ECC9 00                       $d010, sprite MSB
.:ECCA 9B                       $d011, VIC control register
.:ECCB 37                       $d012,
.:ECCC 00 00                    $d013/4, light pen x/y position
.:ECCE 00                       $d015, sprite enable
.:ECCF 08                       $d016, VIC control register 2
.:ECD0 00                       $d017, sprite y-expansion
.:ECD1 14                       $d018, VIC memory control register
.:ECD2 0F                       $d019, VIC irq flag register
.:ECD3 00                       $d01a, VIC irq mask register
.:ECD4 00                       $d01b, sprite/background priority
.:ECD5 00                       $d01c, sprite multicolour mode
.:ECD6 00                       $d01d, sprite x-expansion
.:ECD7 00                       $d01e, sprite/sprite collision
.:ECD8 00                       $d01f, sprite/background collision
.:ECD9 0E                       $d020, border colour (light blue)
.:ECDA 06                       $d021, background colour 0 (blue)
.:ECDB 01                       $d022, background colour 1
.:ECDC 02                       $d023, background colour 2
.:ECDD 03                       $d024, background colour 3
.:ECDE 04                       $d025, sprite multicolour register 0
.:ECDF 00                       $d026, sprite multicolour register 1
.:ECE0 01                       $d027, sprite0 colour
.:ECE1 02                       $d028, sprite1 colour
.:ECE2 03                       $d029, sprite2 colour
.:ECE3 04                       $d02a, sprite3 colour
.:ECE4 05                       $d02b, sprite4 colour
.:ECE5 06                       $d02c, sprite5 colour
.:ECE6 07                       $d02d, sprite6 colour

                                *** SHIFT-RUN EQUIVALENT
                                This is the message LOAD <CR> RUN <CR>, which is placed in
                                the keyboard buffer when <shift-RUN> is pressed.
.:ECE7 4C 4F 41 44 0D 52 55 4E  LOAD <CR> RUN <CR>
.:ECEF 0D

                                *** LOW BYTE SCREEN LINE ADDRESSES
                                This is a table of the low bytes of screen line addresses.
                                The high byte of the addresses is obtained by derivation
                                from the page on which the screen starts. There was an
                                additional table of high byte addresses on the fixed
                                screen PETs.
.:ECF0 00 28 50 78 A0 C8 F0 18
.:ECF8 40 68 90 B8 E0 08 30 58
.:ED00 80 A8 D0 F8 20 48 70 98
.:ED08 C0

                                *** TALK: SEND 'TALK' / 'LISTEN'
                                The KERNAL routine TALK ($ffb4) and LISTEN ($ffb1) are
                                vectored here. The routine sends the command 'TALK' or
                                'LISTEN' on the serial bus. On entry (A) must hold the
                                device number to which the command will be sent. The two
                                entry points differ only in that to TALK, (A) is ORed with
                                #$40, and to LISTEN, (A) is ORed with #$20. The UNTALK
                                (#$3f) and UNLISTEN (#$5f) are also sent via this routine,
                                but their values are set on entry. If there is a character
                                waiting to go out on the bus, then this is output.
                                Handshaking is performed, and ATN (attension) is set low
                                so that the byte is interpreted as a command. The routine
                                drops through to the next one to output the byte on the
                                serial bus. Note that on conclusion, ATN must be set high.
.,ED09 09 40    ORA #$40        set TALK flag
.:ED0B 2C       .BYTE $2C       bit $2009, mask ORA command
.,ED0C 09 20    ORA #$20        set LISTEN flag
.,ED0E 20 A4 F0 JSR $F0A4       check serial bus idle
.,ED11 48       PHA
.,ED12 24 94    BIT $94         C3PO, character in serial buffer
.,ED14 10 0A    BPL $ED20       nope
.,ED16 38       SEC             prepare for ROR
.,ED17 66 A3    ROR $A3         temp data area
.,ED19 20 40 ED JSR $ED40       send data to serial bus
.,ED1C 46 94    LSR $94         3CPO
.,ED1E 46 A3    LSR $A3
.,ED20 68       PLA
.,ED21 85 95    STA $95         BSOUR, buffered character for bus
.,ED23 78       SEI
.,ED24 20 97 EE JSR $EE97       set data 1, and clear serial bit count
.,ED27 C9 3F    CMP #$3F        UNTALK?
.,ED29 D0 03    BNE $ED2E       nope
.,ED2B 20 85 EE JSR $EE85       set CLK 1
.,ED2E AD 00 DD LDA $DD00       serial bus I/O port
.,ED31 09 08    ORA #$08        clear ATN, prepare for command
.,ED33 8D 00 DD STA $DD00       store
.,ED36 78       SEI             disable interrupts
.,ED37 20 8E EE JSR $EE8E       set CLK 1
.,ED3A 20 97 EE JSR $EE97       set data 1
.,ED3D 20 B3 EE JSR $EEB3       delay 1 ms

                                *** SEND DATA ON SERIAL BUS
                                The byte of data to be output on the serial bus must have
                                been previously stored in the serial buffer, BSOUR. An
                                initial test is made for bus activity, and if none is
                                detected then ST is set to #$80, ie. ?DEVICE NOT PRESENT.
                                The byte is output by rotating it right and sending the
                                state of the carry flag. This is done eight times until
                                the whole byte was sent. The CIA timer is set to 65 ms and
                                the bus is checked for 'data accepted'. If timeout occurs
                                before this happens then ST is set to #$03, ie. write
                                timeout.
.,ED40 78       SEI             disable interrupts
.,ED41 20 97 EE JSR $EE97       set data 1
.,ED44 20 A9 EE JSR $EEA9       get serial in and clock
.,ED47 B0 64    BCS $EDAD       no activity, device not present.
.,ED49 20 85 EE JSR $EE85       set CLK 1
.,ED4C 24 A3    BIT $A3         temp data area
.,ED4E 10 0A    BPL $ED5A
.,ED50 20 A9 EE JSR $EEA9       get serial in and clock
.,ED53 90 FB    BCC $ED50       wait for indata = 0
.,ED55 20 A9 EE JSR $EEA9       get serial in and clock
.,ED58 B0 FB    BCS $ED55       wait for indata = 1
.,ED5A 20 A9 EE JSR $EEA9       get serial in and clock
.,ED5D 90 FB    BCC $ED5A       wait for indata = 0
.,ED5F 20 8E EE JSR $EE8E       set CLK 0

.,ED62 A9 08    LDA #$08        output 8 bits
.,ED64 85 A5    STA $A5
.,ED66 AD 00 DD LDA $DD00
.,ED69 CD 00 DD CMP $DD00
.,ED6C D0 F8    BNE $ED66
.,ED6E 0A       ASL
.,ED6F 90 3F    BCC $EDB0
.,ED71 66 95    ROR $95         BSOUR, buffered character for bus
.,ED73 B0 05    BCS $ED7A       prepare to output 1
.,ED75 20 A0 EE JSR $EEA0       else, serial output 0
.,ED78 D0 03    BNE $ED7D
.,ED7A 20 97 EE JSR $EE97
.,ED7D 20 85 EE JSR $EE85
.,ED80 EA       NOP
.,ED81 EA       NOP
.,ED82 EA       NOP
.,ED83 EA       NOP
.,ED84 AD 00 DD LDA $DD00
.,ED87 29 DF    AND #$DF
.,ED89 09 10    ORA #$10
.,ED8B 8D 00 DD STA $DD00
.,ED8E C6 A5    DEC $A5         decrement bit counter
.,ED90 D0 D4    BNE $ED66       next bit till all 8 are done
.,ED92 A9 04    LDA #$04
.,ED94 8D 07 DC STA $DC07       CIA timer B, high byte
.,ED97 A9 19    LDA #$19
.,ED99 8D 0F DC STA $DC0F       set 1 shot, load and start CIA timer B
.,ED9C AD 0D DC LDA $DC0D       CIA ICR
.,ED9F AD 0D DC LDA $DC0D
.,EDA2 29 02    AND #$02        timeout
.,EDA4 D0 0A    BNE $EDB0       yep, flag write timeout
.,EDA6 20 A9 EE JSR $EEA9       get serial in and clock
.,EDA9 B0 F4    BCS $ED9F
.,EDAB 58       CLI             enable interrupts
.,EDAC 60       RTS

                                *** FLAG ERRORS
                                (A) is loaded with one of the two error flags, depending
                                on the entry point. #$80 signifies the device was not
                                present, and #$03 signifies a write timeout. The value is
                                then set into the I/O status word, ST. The routine exits
                                by clearing ATN and giving the final handshake.
.,EDAD A9 80    LDA #$80        flag ?DEVICE NOT PRESENT
.:EDAF 2C       .BYTE $2C       mask LDA #$03
.,EDB0 A9 03    LDA #$03        flag write timeout
.,EDB2 20 1C FE JSR $FE1C       set I/O status word
.,EDB5 58       CLI
.,EDB6 18       CLC
.,EDB7 90 4A    BCC $EE03       allways jump, do final handshake

                                *** SECOND: SEND LISTEN SA
                                The KERNAL routine SECOND ($ff93) is vectored here. On
                                entry, (A) holds the secondary address. This is placed in
                                the serial buffer and sent to the serial bus "under
                                attension". Finally the routine drops through to the next
                                routine to set ATN false.
.,EDB9 85 95    STA $95         store (A) in BSOUT, buffer for the serial bus
.,EDBB 20 36 ED JSR $ED36       handshake and send byte.

                                *** CLEAR ATN
                                The ATN, attension, line on the serial bus is set to 1,
                                ie. ATN is now false and data sent on the serial bus will
                                not be interpreted as a command.
.,EDBE AD 00 DD LDA $DD00       serial bus I/O port
.,EDC1 29 F7    AND #$F7        clear bit4, ie. ATN 1
.,EDC3 8D 00 DD STA $DD00       store to port
.,EDC6 60       RTS

                                *** TKSA: SEND TALK SA
                                The KERNAL routine TKSA ($ff96) is vectored here. On
                                entry, (A) holds the secondary address. This is placed in
                                the serial buffer and sent out to the serial bus "under
                                attension". The routine drops through to the next routine
                                to wait for CLK and clear ATN.
.,EDC7 85 95    STA $95         BSOUR, the serial bus buffer
.,EDC9 20 36 ED JSR $ED36       handshake and send byte to the bus

                                *** WAIT FOR CLOCK
                                This routine sets data = 0, ATN = 1 and CLK = 1. It then
                                waits to recieve CLK = 0 from the serial bus.
.,EDCC 78       SEI             disable interrupts
.,EDCD 20 A0 EE JSR $EEA0       set data 0
.,EDD0 20 BE ED JSR $EDBE       set ATN 1
.,EDD3 20 85 EE JSR $EE85       set CLK 1
.,EDD6 20 A9 EE JSR $EEA9       read serial bus I/O port
.,EDD9 30 FB    BMI $EDD6       test bit6, and wait for CLK = 0
.,EDDB 58       CLI             enable interrupt
.,EDDC 60       RTS

                                *** CIOUT: SEND SERIAL DEFERRED
                                The KERNAL routine CIOUT ($ffa8) jumps to this routine.
                                The output flag, C3PO is set (ie. bit 7 = 1) and the
                                contents of (A) is placed in the serial buffer.
.,EDDD 24 94    BIT $94         C3PO flag, character in serial buffer
.,EDDF 30 05    BMI $EDE6       yes
.,EDE1 38       SEC             prepare for ROR
.,EDE2 66 94    ROR $94         set C3PO
.,EDE4 D0 05    BNE $EDEB       always jump
.,EDE6 48       PHA             temp store
.,EDE7 20 40 ED JSR $ED40       send data to serial bus
.,EDEA 68       PLA
.,EDEB 85 95    STA $95         store character in BSOUR
.,EDED 18       CLC             clear carry to indicate no errors
.,EDEE 60       RTS

                                *** UNTLK: SEND 'UNTALK'/'UNLISTEN'
                                The KERNAL routine UNTALK ($ffab)and UNLISTEN ($ffae) are
                                vectored here. ATN is set to 0, and CLK is set to 0. (A)
                                is loaded with #$5f for 'UNTALK' and #$3f for 'UNLISTEN'.
                                The command is sent to the serial bus via the 'send TALK/
                                LISTEN' routine. Finally ATN is set to 1, and after s
                                short delay, CLK and data are both set to 1.
.,EDEF 78       SEI             disable interrupts
.,EDF0 20 8E EE JSR $EE8E       serial bus I/O
.,EDF3 AD 00 DD LDA $DD00       set bit4
.,EDF6 09 08    ORA #$08        and store, set ATN 0
.,EDF8 8D 00 DD STA $DD00       set CLK 0
.,EDFB A9 5F    LDA #$5F        flag UNTALK
.:EDFD 2C       .BYTE $2C       mask LDA #$3f with BIT $3fa9
.,EDFE A9 3F    LDA #$3F        flag UNLISTEN
.,EE00 20 11 ED JSR $ED11       send command to serial bus
.,EE03 20 BE ED JSR $EDBE       clear ATN
.,EE06 8A       TXA
.,EE07 A2 0A    LDX #$0A        init delay
.,EE09 CA       DEX             decrement counter
.,EE0A D0 FD    BNE $EE09       till ready
.,EE0C AA       TAX
.,EE0D 20 85 EE JSR $EE85       set CLK 1
.,EE10 4C 97 EE JMP $EE97       set data 1

                                *** ACPTR: RECIEVE FROM SERIAL BUS
                                The KERNAL routine ACPTR ($ffa5) points to this routine. A
                                timing loop is enteredusing the CIA timer, and if a byte
                                is not received in 65 ms, ST is set to #$02, ie. a read
                                timeout. A test is made for EOI and if this occurs, ST is
                                set to #$40, indicating end of file. The byte is then
                                received from the serial bus and built up bit by bit in
                                the temporary stora at #$a4. This is transfered to (A) on
                                exit, unless EOI has occured.
.,EE13 78       SEI
.,EE14 A9 00    LDA #$00
.,EE16 85 A5    STA $A5         CNTDN, counter
.,EE18 20 85 EE JSR $EE85       set CLK 1
.,EE1B 20 A9 EE JSR $EEA9       get serial in and clock
.,EE1E 10 FB    BPL $EE1B       wait for CLK = 1
.,EE20 A9 01    LDA #$01
.,EE22 8D 07 DC STA $DC07       setup CIA#1 timer B, high byte
.,EE25 A9 19    LDA #$19
.,EE27 8D 0F DC STA $DC0F       set 1 shot, load and start CIA timer B
.,EE2A 20 97 EE JSR $EE97       set data 1
.,EE2D AD 0D DC LDA $DC0D
.,EE30 AD 0D DC LDA $DC0D       read CIA#1 ICR
.,EE33 29 02    AND #$02        test if timer B reaches zero
.,EE35 D0 07    BNE $EE3E       timeout
.,EE37 20 A9 EE JSR $EEA9       get serial in and clock
.,EE3A 30 F4    BMI $EE30       CLK 1
.,EE3C 10 18    BPL $EE56       CLK 0
.,EE3E A5 A5    LDA $A5         CNTDN
.,EE40 F0 05    BEQ $EE47
.,EE42 A9 02    LDA #$02        flag read timeout
.,EE44 4C B2 ED JMP $EDB2       set I/O status word
.,EE47 20 A0 EE JSR $EEA0       set data 1
.,EE4A 20 85 EE JSR $EE85       set CLK 1
.,EE4D A9 40    LDA #$40        flag EOI
.,EE4F 20 1C FE JSR $FE1C       set I/O status word
.,EE52 E6 A5    INC $A5         increment CNTDN, counter
.,EE54 D0 CA    BNE $EE20       again
.,EE56 A9 08    LDA #$08        set up CNTDN to receive 8 bits
.,EE58 85 A5    STA $A5
.,EE5A AD 00 DD LDA $DD00       serial bus I/O port
.,EE5D CD 00 DD CMP $DD00       compare
.,EE60 D0 F8    BNE $EE5A       wait for serial bus to settle
.,EE62 0A       ASL
.,EE63 10 F5    BPL $EE5A       wait for data in =1
.,EE65 66 A4    ROR $A4         roll in received bit in temp data area
.,EE67 AD 00 DD LDA $DD00       serial bus I/O port
.,EE6A CD 00 DD CMP $DD00       compare
.,EE6D D0 F8    BNE $EE67       wait for bus to settle
.,EE6F 0A       ASL
.,EE70 30 F5    BMI $EE67       wait for data in =0
.,EE72 C6 A5    DEC $A5         one bit received
.,EE74 D0 E4    BNE $EE5A       repeat for all 8 bits
.,EE76 20 A0 EE JSR $EEA0       set data 1
.,EE79 24 90    BIT $90         STATUS, I/O status word
.,EE7B 50 03    BVC $EE80       not EOI
.,EE7D 20 06 EE JSR $EE06       handshake and exit without byte
.,EE80 A5 A4    LDA $A4         read received byte
.,EE82 58       CLI             enable interrupts
.,EE83 18       CLC             clear carry, no errors
.,EE84 60       RTS

                                *** SERIAL CLOCK ON
                                This routine sets the clock outline on the serial bus to
                                1. This means writing a 0 to the port. This value is
                                reversed by hardware on the bus.
.,EE85 AD 00 DD LDA $DD00       serial port I/O register
.,EE88 29 EF    AND #$EF        clear bit4, ie. CLK out =1
.,EE8A 8D 00 DD STA $DD00       store
.,EE8D 60       RTS

                                *** SERIAL CLOCK OFF
                                This routine sets the clock outline on the serial bus to
                                0. This means writing a 1 to the port. This value is
                                reversed by hardware on the bus.
.,EE8E AD 00 DD LDA $DD00       serial port I/O register
.,EE91 09 10    ORA #$10        set bit4, ie. CLK out =0
.,EE93 8D 00 DD STA $DD00       store
.,EE96 60       RTS

                                *** SERIAL OUTPUT 1
                                This routine sets the data out line on the serial bus to
                                1. This means writing a 0 to the port. This value is
                                reversed by hardware on the bus.
.,EE97 AD 00 DD LDA $DD00       serial bus I/O register
.,EE9A 29 DF    AND #$DF        clear bit5
.,EE9C 8D 00 DD STA $DD00       store
.,EE9F 60       RTS

                                *** SERIAL OUTPUT 0
                                This routine sets the data out line on the serial bus to
                                0. This means writing a 1 to the port. This value is
                                reversed by hardware on the bus.
.,EEA0 AD 00 DD LDA $DD00       serial bus I/O resister
.,EEA3 09 20    ORA #$20        set bit 5
.,EEA5 8D 00 DD STA $DD00       store
.,EEA8 60       RTS

                                *** GET SERIAL DATA AND CLOCK IN
                                The serial port I/O register is stabilised and read. The
                                data is shifteed into carry and CLK into bit 7. This way,
                                both the data and clock can bee determined by flags in the
                                processor status register. Note that the values read are
                                true, and do not nead to be reversed in the same way as
                                the outuput line do.
.,EEA9 AD 00 DD LDA $DD00       serial port I/O register
.,EEAC CD 00 DD CMP $DD00       compare
.,EEAF D0 F8    BNE $EEA9       wait for bus to settle
.,EEB1 0A       ASL             shift data into carry, and CLK into bit 7
.,EEB2 60       RTS

                                *** DELAY 1 MS
                                This routine is a software delay loop where (X) is used as
                                counter, and are decremented for a period of 1
                                millisecond. The original (X) is stored on entry and (A)
                                is messed up.
.,EEB3 8A       TXA             move (X) to (A)
.,EEB4 A2 B8    LDX #$B8        start value
.,EEB6 CA       DEX             decrement
.,EEB7 D0 FD    BNE $EEB6       untill zero
.,EEB9 AA       TAX             (A) to (X)
.,EEBA 60       RTS

                                *** RS232 SEND
                                This routine is concerned with sending a byte on the RS232
                                port. The data is actually written to the port under NMI
                                interrupt control. The CTS line generates an NMI when the
                                port is ready for data. If all the bits in the byte have
                                been sent, then a new RS232 byte is set up. Otherwise,
                                this routine calculates parity and number of stop bits set
                                up in the OPEN command. These bits are added to the end of
                                the byte being sent.
.,EEBB A5 B4    LDA $B4         BITTS, RS232 out bit count
.,EEBD F0 47    BEQ $EF06       send new RS232 byte
.,EEBF 30 3F    BMI $EF00
.,EEC1 46 B6    LSR $B6         RODATA, RS232 out byte buffer
.,EEC3 A2 00    LDX #$00
.,EEC5 90 01    BCC $EEC8
.,EEC7 CA       DEX
.,EEC8 8A       TXA
.,EEC9 45 BD    EOR $BD         ROPRTY, RS232 out parity
.,EECB 85 BD    STA $BD
.,EECD C6 B4    DEC $B4         BITTS
.,EECF F0 06    BEQ $EED7
.,EED1 8A       TXA
.,EED2 29 04    AND #$04
.,EED4 85 B5    STA $B5         NXTBIT, next RS232 bit to send
.,EED6 60       RTS
.,EED7 A9 20    LDA #$20
.,EED9 2C 94 02 BIT $0294       M51CDR, 6551 command register immage
.,EEDC F0 14    BEQ $EEF2       no patity
.,EEDE 30 1C    BMI $EEFC       mark/space transmit
.,EEE0 70 14    BVS $EEF6       even parity
.,EEE2 A5 BD    LDA $BD         ROPRTY, out parity
.,EEE4 D0 01    BNE $EEE7
.,EEE6 CA       DEX
.,EEE7 C6 B4    DEC $B4         BITTS, out bit count
.,EEE9 AD 93 02 LDA $0293       M51CTR, 6551 control register image
.,EEEC 10 E3    BPL $EED1       one stop bit only
.,EEEE C6 B4    DEC $B4         BITTS
.,EEF0 D0 DF    BNE $EED1
.,EEF2 E6 B4    INC $B4         BITTS
.,EEF4 D0 F0    BNE $EEE6
.,EEF6 A5 BD    LDA $BD         ROPRTY
.,EEF8 F0 ED    BEQ $EEE7
.,EEFA D0 EA    BNE $EEE6
.,EEFC 70 E9    BVS $EEE7
.,EEFE 50 E6    BVC $EEE6
.,EF00 E6 B4    INC $B4         BITTS
.,EF02 A2 FF    LDX #$FF
.,EF04 D0 CB    BNE $EED1

                                *** SEND NEW RS232 BYTE
                                This routine sets up the system variables ready to send a
                                new byte to the RS232 port. A test is made for 3-line or
                                X-line modus. In X-line mode, DSR and  CTS are checked.
.,EF06 AD 94 02 LDA $0294       M51CDR, 6551 command register
.,EF09 4A       LSR             test handshake mode
.,EF0A 90 07    BCC $EF13       3-line mode (no handshake)
.,EF0C 2C 01 DD BIT $DD01       RS232 port
.,EF0F 10 1D    BPL $EF2E       no DSR, error
.,EF11 50 1E    BVC $EF31       no CTS, error
.,EF13 A9 00    LDA #$00
.,EF15 85 BD    STA $BD         ROPRTY, RS232 out parity
.,EF17 85 B5    STA $B5         NXTBIT, next bit to send
.,EF19 AE 98 02 LDX $0298       BITNUM, number of bits left to send
.,EF1C 86 B4    STX $B4         BITTS, RS232 out bit count
.,EF1E AC 9D 02 LDY $029D       RODBS, start page of out buffer
.,EF21 CC 9E 02 CPY $029E       RODBE, index to end if out buffer
.,EF24 F0 13    BEQ $EF39       disable timer
.,EF26 B1 F9    LDA ($F9),Y     RS232 out buffer
.,EF28 85 B6    STA $B6         RODATA, RS232 out byte buffer
.,EF2A EE 9D 02 INC $029D       RODBS
.,EF2D 60       RTS

                                *** NO DSR / CTS ERROR
                                (A) is loaded with the error flag - $40 for no DSR, and
                                $10 for no CTS. This is then ORed with 6551 status image
                                and stored in RSSTAT.
.,EF2E A9 40    LDA #$40        entrypoint for 'NO DSR'
.:EF30 2C       .BYTE $2C       mask next LDA-command
.,EF31 A9 10    LDA #$10        entrypoint for 'NO CTS'
.,EF33 0D 97 02 ORA $0297       RSSTAT, 6551 status register image
.,EF36 8D 97 02 STA $0297

                                *** DISABLE TIMER
                                This routine set the interrupt mask on CIA#2 timer B. It
                                also clears the NMI flag.
.,EF39 A9 01    LDA #$01        ; CIA#2 interrupt control register
.,EF3B 8D 0D DD STA $DD0D       ; ENABL, RS232 enables
.,EF3E 4D A1 02 EOR $02A1
.,EF41 09 80    ORA #$80        ; ENABL
.,EF43 8D A1 02 STA $02A1       ; CIA#2 interrupt control register
.,EF46 8D 0D DD STA $DD0D
.,EF49 60       RTS

                                *** COMPUTE BIT COUNT
                                This routine computes the number of bits in the word to be
                                sent. The word length information is held in bits 5 & 6 of
                                M51CTR. Bit 7 of this register indicates the number of
                                stop bits. On exit, the number of bits is held in (X).
.,EF4A A2 09    LDX #$09
.,EF4C A9 20    LDA #$20
.,EF4E 2C 93 02 BIT $0293       M51CTR, 6551 control register image
.,EF51 F0 01    BEQ $EF54
.,EF53 CA       DEX
.,EF54 50 02    BVC $EF58
.,EF56 CA       DEX
.,EF57 CA       DEX
.,EF58 60       RTS

                                *** RS232 RECEIVE
                                This routine builds up the input byte from the RS232 port
                                in RIDATA. Each bit is input from the port under NMI
                                interrupt control. The bit is placed in INBIT before being
                                passed to this routine, where it is shifted into the carry
                                flag and then rotated into RIDATA. The bit count is
                                decremented and parity updated.
.,EF59 A6 A9    LDX $A9         RINONE, check for start bit?
.,EF5B D0 33    BNE $EF90
.,EF5D C6 A8    DEC $A8         BITC1, RS232 in bit count
.,EF5F F0 36    BEQ $EF97       process received byte
.,EF61 30 0D    BMI $EF70
.,EF63 A5 A7    LDA $A7         INBIT, RS232 in bits
.,EF65 45 AB    EOR $AB         RIPRTY, RS232 in parity
.,EF67 85 AB    STA $AB
.,EF69 46 A7    LSR $A7         INBIT, put input bit into carry
.,EF6B 66 AA    ROR $AA         RIDATA,
.,EF6D 60       RTS
.,EF6E C6 A8    DEC $A8         BITC1
.,EF70 A5 A7    LDA $A7         INBIT
.,EF72 F0 67    BEQ $EFDB
.,EF74 AD 93 02 LDA $0293       M51CTR, 6551 control register image
.,EF77 0A       ASL
.,EF78 A9 01    LDA #$01
.,EF7A 65 A8    ADC $A8         BITC1
.,EF7C D0 EF    BNE $EF6D       end

                                *** SET UP TO RECEIVE
                                This routine sets up the I.C.R. to wait for the receiver
                                edge, and flags this into ENABL. It then flags the check
                                for a start bit.
.,EF7E A9 90    LDA #$90
.,EF80 8D 0D DD STA $DD0D       CIA#2 I.C.R.
.,EF83 0D A1 02 ORA $02A1       ENABL, RS232 enables
.,EF86 8D A1 02 STA $02A1
.,EF89 85 A9    STA $A9         RINONE, check for start bit
.,EF8B A9 02    LDA #$02
.,EF8D 4C 3B EF JMP $EF3B       disable timer and exit

                                *** PROCESS RS232 BYTE
                                The byte recieved from the RS232 port is checked against
                                parity. This involvs checking the input parity options
                                selected, and then verifying the parity bit calculated
                                against that input. If the test is passed, then the byte
                                is stored in the in-buffer. Otherwise an error is flagged
                                into RSSTAT.
                                A patch in KERNAL version 3, has been added to the input
                                routine at $ef94 to initialise the RS232 parity byte,
                                RIPRTY, on reception of a start bit.
.,EF90 A5 A7    LDA $A7         INBIT, RS232 in bits
.,EF92 D0 EA    BNE $EF7E       set up to receive
.,EF94 4C D3 E4 JMP $E4D3       patch, init parity byte
.,EF97 AC 9B 02 LDY $029B       RIDBE, index to the end of in buffer
.,EF9A C8       INY
.,EF9B CC 9C 02 CPY $029C       RIDBS, start page of in buffer
.,EF9E F0 2A    BEQ $EFCA       receive overflow error
.,EFA0 8C 9B 02 STY $029B       RIDBE
.,EFA3 88       DEY
.,EFA4 A5 AA    LDA $AA         RIDATA, RS232 in byte buffer
.,EFA6 AE 98 02 LDX $0298       BITNUM, number of bits left to send
.,EFA9 E0 09    CPX #$09        full word to come?
.,EFAB F0 04    BEQ $EFB1       yes
.,EFAD 4A       LSR
.,EFAE E8       INX
.,EFAF D0 F8    BNE $EFA9
.,EFB1 91 F7    STA ($F7),Y     RIBUF, RS232 in buffer
.,EFB3 A9 20    LDA #$20
.,EFB5 2C 94 02 BIT $0294       M51CDR, 6551 command register image
.,EFB8 F0 B4    BEQ $EF6E       parity disabled
.,EFBA 30 B1    BMI $EF6D       parity check disabled, TRS
.,EFBC A5 A7    LDA $A7         INBIT, parity check
.,EFBE 45 AB    EOR $AB         RIPRTY, RS232 in parity
.,EFC0 F0 03    BEQ $EFC5       receive parity error
.,EFC2 70 A9    BVS $EF6D
.:EFC4 2C       .BYTE $2C       mask
.,EFC5 50 A6    BVC $EF6D
.,EFC7 A9 01    LDA #$01        receive parity error
.:EFC9 2C       .BYTE $2C       mask
.,EFCA A9 04    LDA #$04        receive overflow
.:EFCC 2C       .BYTE $2C       mask
.,EFCD A9 80    LDA #$80        framing break
.:EFCF 2C       .BYTE $2C       mask
.,EFD0 A9 02    LDA #$02        framing error
.,EFD2 0D 97 02 ORA $0297       RSSTAT, 6551 status register image
.,EFD5 8D 97 02 STA $0297
.,EFD8 4C 7E EF JMP $EF7E       set up to receive
.,EFDB A5 AA    LDA $AA         RIDATA
.,EFDD D0 F1    BNE $EFD0       framing error
.,EFDF F0 EC    BEQ $EFCD       receive break

                                *** SUBMIT TO RS232
                                This routine is called when data is required from the
                                RS232 port. Its function is to perform the handshaking on
                                the poort needed to receive the data. If 3 line mode is
                                used, then no handshaking is implemented and the routine
                                exits.
.,EFE1 85 9A    STA $9A         DFLTO, default output device
.,EFE3 AD 94 02 LDA $0294       M51CDR, 6551 command register image
.,EFE6 4A       LSR
.,EFE7 90 29    BCC $F012       3 line mode, no handshaking, exit
.,EFE9 A9 02    LDA #$02
.,EFEB 2C 01 DD BIT $DD01       RS232 I/O port
.,EFEE 10 1D    BPL $F00D       no DRS, error
.,EFF0 D0 20    BNE $F012
.,EFF2 AD A1 02 LDA $02A1       ENABL, RS232 enables
.,EFF5 29 02    AND #$02
.,EFF7 D0 F9    BNE $EFF2
.,EFF9 2C 01 DD BIT $DD01       RS232 I/O port
.,EFFC 70 FB    BVS $EFF9       wait for no CTS
.,EFFE AD 01 DD LDA $DD01
.,F001 09 02    ORA #$02
.,F003 8D 01 DD STA $DD01       set RTS
.,F006 2C 01 DD BIT $DD01
.,F009 70 07    BVS $F012       CTS set
.,F00B 30 F9    BMI $F006       wait for no DSR

                                *** NO DSR ERROR
                                This routine sets the 6551 status register image to #40
                                when a no DSR error has occurred.
.,F00D A9 40    LDA #$40
.,F00F 8D 97 02 STA $0297       RSSTAT, 6551 status register image
.,F012 18       CLC
.,F013 60       RTS

                                *** SEND TO RS232 BUFFER
                                Note: The entry point to the routine is at
.,F014 20 28 F0 JSR $F028
.,F017 AC 9E 02 LDY $029E
.,F01A C8       INY
.,F01B CC 9D 02 CPY $029D
.,F01E F0 F4    BEQ $F014
.,F020 8C 9E 02 STY $029E
.,F023 88       DEY
.,F024 A5 9E    LDA $9E
.,F026 91 F9    STA ($F9),Y
.,F028 AD A1 02 LDA $02A1
.,F02B 4A       LSR
.,F02C B0 1E    BCS $F04C
.,F02E A9 10    LDA #$10
.,F030 8D 0E DD STA $DD0E
.,F033 AD 99 02 LDA $0299
.,F036 8D 04 DD STA $DD04
.,F039 AD 9A 02 LDA $029A
.,F03C 8D 05 DD STA $DD05
.,F03F A9 81    LDA #$81
.,F041 20 3B EF JSR $EF3B
.,F044 20 06 EF JSR $EF06
.,F047 A9 11    LDA #$11
.,F049 8D 0E DD STA $DD0E
.,F04C 60       RTS

                                *** INPUT FROM RS232
.,F04D 85 99    STA $99
.,F04F AD 94 02 LDA $0294
.,F052 4A       LSR
.,F053 90 28    BCC $F07D
.,F055 29 08    AND #$08
.,F057 F0 24    BEQ $F07D
.,F059 A9 02    LDA #$02
.,F05B 2C 01 DD BIT $DD01
.,F05E 10 AD    BPL $F00D
.,F060 F0 22    BEQ $F084
.,F062 AD A1 02 LDA $02A1
.,F065 4A       LSR
.,F066 B0 FA    BCS $F062
.,F068 AD 01 DD LDA $DD01
.,F06B 29 FD    AND #$FD
.,F06D 8D 01 DD STA $DD01
.,F070 AD 01 DD LDA $DD01
.,F073 29 04    AND #$04
.,F075 F0 F9    BEQ $F070
.,F077 A9 90    LDA #$90
.,F079 18       CLC
.,F07A 4C 3B EF JMP $EF3B
.,F07D AD A1 02 LDA $02A1
.,F080 29 12    AND #$12
.,F082 F0 F3    BEQ $F077
.,F084 18       CLC
.,F085 60       RTS

                                F086 GET FROM RS232
.,F086 AD 97 02 LDA $0297
.,F089 AC 9C 02 LDY $029C
.,F08C CC 9B 02 CPY $029B
.,F08F F0 0B    BEQ $F09C
.,F091 29 F7    AND #$F7
.,F093 8D 97 02 STA $0297
.,F096 B1 F7    LDA ($F7),Y
.,F098 EE 9C 02 INC $029C
.,F09B 60       RTS
.,F09C 09 08    ORA #$08
.,F09E 8D 97 02 STA $0297
.,F0A1 A9 00    LDA #$00
.,F0A3 60       RTS

                                *** SERIAL BUS IDLE
                                This routine checks the RS232 bus for data transmission/
                                reception. The routine waits for any activity on the bus
                                to end before setting I.C.R. The routine is called by
                                serial bus routines, since these devices use IRQ generated
                                timing, and conflicts may occur if they are all used at
                                once.
.,F0A4 48       PHA             store (A)
.,F0A5 AD A1 02 LDA $02A1       ENABL, RS232 enables
.,F0A8 F0 11    BEQ $F0BB       bus not in use
.,F0AA AD A1 02 LDA $02A1       ENABL
.,F0AD 29 03    AND #$03        test RS232
.,F0AF D0 F9    BNE $F0AA       yes, wait for port to clear
.,F0B1 A9 10    LDA #$10
.,F0B3 8D 0D DD STA $DD0D       set up CIA#2 I.C.R
.,F0B6 A9 00    LDA #$00        clear
.,F0B8 8D A1 02 STA $02A1       ENABL
.,F0BB 68       PLA             retrieve (A)
.,F0BC 60       RTS

                                *** TABLE OF KERNAL I/O MESSAGES 1
                                This is a table of messages used by the KERNAL in
                                conjunction with its I/O routines. Bit 7 is set in the
                                last character in each message as a terminator.
.:F0BD 0D 49 2F 4F 20 45 52 52  I/O error
.:F0C5 4F 52 20 A3
.:F0C9 0D 53 45 41 52 43 48 49  searching for
.:F0D1 4E 47 A0 46 4F 52 A0
.:F0D8 0D 50 52 45 53 53 20 50  press play on tape
.:F0E0 4C 41 59 20 4F 4E 20 54
.:F0E8 41 50 C5
.:F0EB 50 52 45 53 53 20 52 45  press record and play on tape
.:F0F3 43 4F 52 44 20 26 20 50
.:F0FB 4C 41 59 20 4F 4E 20 54
.:F103 41 50 C5
.:F106 0D 4C 4F 41 44 49 4E C7  loading
.:F10E 0D 53 41 56 49 4E 47 A0  saving
.:F116 0D 56 45 52 49 46 59 49  verifying
.:F11E 4E C7
.:F120 0D 46 4F 55 4E 44 A0     found
.:F127 0D 4F 4B 8D              ok

                                *** PRINT MESSAGE IF DIRECT
                                This is a routine to output a message from the I/O
                                messages table at $f0bd. On entry, (Y) holds the offset to
                                control which message is printed. The routine tests if we
                                are in program mode or direct mode. If in program mode,
                                the routine exits. Else, the routine prints character
                                after caracter untill it reaches a character with bit7
                                set.
.,F12B 24 9D    BIT $9D         MSGFLG, test if direct or program mode
.,F12D 10 0D    BPL $F13C       program mode, don't print message
.,F12F B9 BD F0 LDA $F0BD,Y     get output character from table
.,F132 08       PHP             store processor registers
.,F133 29 7F    AND #$7F        clear bit7
.,F135 20 D2 FF JSR $FFD2       output character using CHROUT
.,F138 C8       INY             increment pointer to next character
.,F139 28       PLP             retrieve message
.,F13A 10 F3    BPL $F12F       untill bit7 was set
.,F13C 18       CLC             clear carry to indicate no error
.,F13D 60       RTS

                                *** GETIN: GET a BYTE
                                The KERNAL routine GETIN ($ffe4) is vectored to this
                                routine. It load a character into fac#1 from the external
                                device indicated by DFLTN. Thus, if device = 0, GET is
                                from the keyboard buffer. If device = 2, GET is from the
                                RS232 port. If neither of these devices then GET is
                                further handled by the next routine, INPUT.
.,F13E A5 99    LDA $99         DFLTN, default input device.
.,F140 D0 08    BNE $F14A       not keyboard
.,F142 A5 C6    LDA $C6         NDX, number of keys in keyboard queue
.,F144 F0 0F    BEQ $F155       buffer empty, exit
.,F146 78       SEI             disable interrupts
.,F147 4C B4 E5 JMP $E5B4       get character from keyboard buffer, and exit
.,F14A C9 02    CMP #$02        RS232
.,F14C D0 18    BNE $F166       nope, try next device
.,F14E 84 97    STY $97         temp store
.,F150 20 86 F0 JSR $F086       get character from RS232
.,F153 A4 97    LDY $97         retrieve (Y)
.,F155 18       CLC
.,F156 60       RTS

                                *** CHRIN: INPUT A BYTE
                                The KERNAL routine CHRIN ($ffcf) is vectored to this
                                routine. It is similar in function to the GET routine
                                above, and also provides a continuation to that routine.
                                If the input device is 0 or 3, ie. keyboard or screen,
                                then input takes place from the screen. INPUT/GET from
                                other devices are performed by calls to the next routine.
                                Two bytes are input from the device so that end of file
                                can be set if necessary (ie. ST = #40)
.,F157 A5 99    LDA $99         DFLTN, default input
.,F159 D0 0B    BNE $F166       not keyboard, next device
.,F15B A5 D3    LDA $D3         PNTR, cursor column on  screen
.,F15D 85 CA    STA $CA         >LXSP, cursor position at start
.,F15F A5 D6    LDA $D6         TBLX, cursor line number
.,F161 85 C9    STA $C9         <LXSP
.,F163 4C 32 E6 JMP $E632       input from screen or keyboard
.,F166 C9 03    CMP #$03        screen
.,F168 D0 09    BNE $F173       nope, next device
.,F16A 85 D0    STA $D0         CRSW, flag INPUT/GET from keyboard
.,F16C A5 D5    LDA $D5         LNMX, physical screen line length
.,F16E 85 C8    STA $C8         INDX, end of logical line for input
.,F170 4C 32 E6 JMP $E632       input from screen of keyboard
.,F173 B0 38    BCS $F1AD
.,F175 C9 02    CMP #$02        RS232
.,F177 F0 3F    BEQ $F1B8       yes, get data from RS232 port
.,F179 86 97    STX $97
.,F17B 20 99 F1 JSR $F199
.,F17E B0 16    BCS $F196
.,F180 48       PHA
.,F181 20 99 F1 JSR $F199
.,F184 B0 0D    BCS $F193
.,F186 D0 05    BNE $F18D
.,F188 A9 40    LDA #$40
.,F18A 20 1C FE JSR $FE1C
.,F18D C6 A6    DEC $A6
.,F18F A6 97    LDX $97
.,F191 68       PLA
.,F192 60       RTS
.,F193 AA       TAX
.,F194 68       PLA
.,F195 8A       TXA
.,F196 A6 97    LDX $97
.,F198 60       RTS
.,F199 20 0D F8 JSR $F80D
.,F19C D0 0B    BNE $F1A9
.,F19E 20 41 F8 JSR $F841
.,F1A1 B0 11    BCS $F1B4
.,F1A3 A9 00    LDA #$00
.,F1A5 85 A6    STA $A6
.,F1A7 F0 F0    BEQ $F199
.,F1A9 B1 B2    LDA ($B2),Y
.,F1AB 18       CLC
.,F1AC 60       RTS

                                *** GET FROM SERIAL/RS232
                                These routines, actually two different, is entered from
                                the previous routine. The serial sectionchecks the state
                                of ST. If zero, then the data is recieved from the bus,
                                otherwise carriage return (#0d) is returned in (A). In the
                                second section, the recieved byte is read from the RS232
                                port.
.,F1AD A5 90    LDA $90         STATUS, I/O status word
.,F1AF F0 04    BEQ $F1B5       status OK
.,F1B1 A9 0D    LDA #$0D        else return <CR> and exit
.,F1B3 18       CLC
.,F1B4 60       RTS
.,F1B5 4C 13 EE JMP $EE13       ACPTR, get byte from serial bus

.,F1B8 20 4E F1 JSR $F14E       receive from RS232
.,F1BB B0 F7    BCS $F1B4       end with carry set
.,F1BD C9 00    CMP #$00
.,F1BF D0 F2    BNE $F1B3       end with  carry clear
.,F1C1 AD 97 02 LDA $0297       RSSTAT, 6551 status register
.,F1C4 29 60    AND #$60        mask
.,F1C6 D0 E9    BNE $F1B1       return with <CR>
.,F1C8 F0 EE    BEQ $F1B8       get from RS232

                                *** CHROUT: OUTPUT ONE CHARACTER
                                The KERNAL routine CHROUT ($ffd2) is vectored to this
                                routine. On entry, (A) must hold the character to be
                                output. The default output device number is examined, and
                                output directed to relevant device. The screen, serial bus
                                and RS232 all use previously described routines for their
                                output.
.,F1CA 48       PHA             temp store on stack
.,F1CB A5 9A    LDA $9A         DFLTO, default output device
.,F1CD C9 03    CMP #$03        screen?
.,F1CF D0 04    BNE $F1D5       nope, test next device
.,F1D1 68       PLA             retrieve (A)
.,F1D2 4C 16 E7 JMP $E716       output to screen
.,F1D5 90 04    BCC $F1DB       device <3
.,F1D7 68       PLA             retrieve (A)
.,F1D8 4C DD ED JMP $EDDD       send serial deferred
.,F1DB 4A       LSR
.,F1DC 68       PLA
.,F1DD 85 9E    STA $9E         PTR1
.,F1DF 8A       TXA
.,F1E0 48       PHA
.,F1E1 98       TYA
.,F1E2 48       PHA
.,F1E3 90 23    BCC $F208       RS232
.,F1E5 20 0D F8 JSR $F80D
.,F1E8 D0 0E    BNE $F1F8
.,F1EA 20 64 F8 JSR $F864
.,F1ED B0 0E    BCS $F1FD
.,F1EF A9 02    LDA #$02
.,F1F1 A0 00    LDY #$00
.,F1F3 91 B2    STA ($B2),Y
.,F1F5 C8       INY
.,F1F6 84 A6    STY $A6
.,F1F8 A5 9E    LDA $9E
.,F1FA 91 B2    STA ($B2),Y
.,F1FC 18       CLC
.,F1FD 68       PLA
.,F1FE A8       TAY
.,F1FF 68       PLA
.,F200 AA       TAX
.,F201 A5 9E    LDA $9E
.,F203 90 02    BCC $F207
.,F205 A9 00    LDA #$00
.,F207 60       RTS
.,F208 20 17 F0 JSR $F017       send to RS232
.,F20B 4C FC F1 JMP $F1FC       end output

                                *** CHKIN: SET INPUT DEVICE
                                The KERNAL routine CHKIN ($ffc6) is vectored to this
                                routine. On entry, (X) must hold the logical file number.
                                A test is made to see if the file is open, or ?FILE NOT
                                OPEN. If the file is not an input file then ?NOT INPUT
                                FILE. If the device is on the serial bus then it is
                                commanded to TALK  and secondary address is sent. ST is
                                then checked, and if non-zero, ?DEVICE NOT PRESENT.
                                Finally, the device number is stored in DLFTN.
.,F20E 20 0F F3 JSR $F30F       find file number
.,F211 F0 03    BEQ $F216       ok, skip next command
.,F213 4C 01 F7 JMP $F701       I/O error #3, file not open
.,F216 20 1F F3 JSR $F31F       set file variables
.,F219 A5 BA    LDA $BA         FA, current device number
.,F21B F0 16    BEQ $F233       keyboard
.,F21D C9 03    CMP #$03        screen
.,F21F F0 12    BEQ $F233       yes
.,F221 B0 14    BCS $F237       larger than 3, serial bus device
.,F223 C9 02    CMP #$02        RS232
.,F225 D0 03    BNE $F22A       nope
.,F227 4C 4D F0 JMP $F04D       input from RS232
.,F22A A6 B9    LDX $B9         SA, current secondart address
.,F22C E0 60    CPX #$60
.,F22E F0 03    BEQ $F233
.,F230 4C 0A F7 JMP $F70A       I/O error #6, not output file
.,F233 85 99    STA $99         DFLTN, default input device
.,F235 18       CLC
.,F236 60       RTS
.,F237 AA       TAX
.,F238 20 09 ED JSR $ED09       send TALK to serial device
.,F23B A5 B9    LDA $B9         SA
.,F23D 10 06    BPL $F245       send SA
.,F23F 20 CC ED JSR $EDCC       wait for clock
.,F242 4C 48 F2 JMP $F248
.,F245 20 C7 ED JSR $EDC7       send talk secondary address
.,F248 8A       TXA
.,F249 24 90    BIT $90         STATUS, I/O status word
.,F24B 10 E6    BPL $F233       store DFLTN, and exit
.,F24D 4C 07 F7 JMP $F707       I/O error #5, device not present

                                *** CHKOUT: SET OUTPUT DEVICE
                                The KERNAL routine CHKOUT ($ffc9) is vectored to this
                                routinr. On entry (X) must hold the logical filenumber. A
                                test is made to see if the file is open, or ?FILE NOT OPEN
                                error. If the device is 0, ie. the keyboard, or the file
                                is not an output file, then ?FILE OUTPUT FILE error is
                                generated. If the device is on the serial bus, then it
                                commanded to LISTEN and the secondary address is sent. ST
                                is then checked and if non-zero, then ?DEVICE NOT PRESENT
                                error. Finally, the device number is stored in DFLTO.
.,F250 20 0F F3 JSR $F30F       fine file number (X)
.,F253 F0 03    BEQ $F258       OK
.,F255 4C 01 F7 JMP $F701       I/O error #3, file not open
.,F258 20 1F F3 JSR $F31F       set file values
.,F25B A5 BA    LDA $BA         FA, current device number
.,F25D D0 03    BNE $F262       not keyboard
.,F25F 4C 0D F7 JMP $F70D       I/O error #7, not output file
.,F262 C9 03    CMP #$03        screen?
.,F264 F0 0F    BEQ $F275       yes
.,F266 B0 11    BCS $F279       serial bus device
.,F268 C9 02    CMP #$02        RS232
.,F26A D0 03    BNE $F26F       nope
.,F26C 4C E1 EF JMP $EFE1       submit to RS232
.,F26F A6 B9    LDX $B9         SA, current secondary address
.,F271 E0 60    CPX #$60
.,F273 F0 EA    BEQ $F25F       not output file error
.,F275 85 9A    STA $9A         DFLTO, default output device
.,F277 18       CLC             clear carry to incicate no errors
.,F278 60       RTS
.,F279 AA       TAX             file (X) to (A)
.,F27A 20 0C ED JSR $ED0C       send LISTEN to serial device
.,F27D A5 B9    LDA $B9         SA
.,F27F 10 05    BPL $F286       send SA
.,F281 20 BE ED JSR $EDBE       clear ATN
.,F284 D0 03    BNE $F289
.,F286 20 B9 ED JSR $EDB9       send listen secondary address
.,F289 8A       TXA
.,F28A 24 90    BIT $90         STATUS, I/O status word
.,F28C 10 E7    BPL $F275       OK, set output device
.,F28E 4C 07 F7 JMP $F707       I/O error #5, device not present

                                *** CLOSE: CLOSE FILE, PART 1
                                The KERNAL routine CLOSE ($ffc3) is vectored here. The
                                file parameters are fetched, and if not found, the routine
                                exits without any action. It checks the device number
                                associated with the file. If it is RS232, then the RS232
                                port is reset. If it is a serial device, the device is
                                UNTALKed, or UNLISTENed. Finally the number of open
                                logical files are decremented, and the table of active
                                file numbers are updated. On entry (A) holds the file
                                number to close.
.,F291 20 14 F3 JSR $F314       find logical file, (X) holds location i table
.,F294 F0 02    BEQ $F298       OK
.,F296 18       CLC             file not found
.,F297 60       RTS             and exit
.,F298 20 1F F3 JSR $F31F       get file values from table, position (X)
.,F29B 8A       TXA
.,F29C 48       PHA             temp store
.,F29D A5 BA    LDA $BA         FA, current device number
.,F29F F0 50    BEQ $F2F1       keyboard?, update file table
.,F2A1 C9 03    CMP #$03        screen
.,F2A3 F0 4C    BEQ $F2F1       yepp, update file table
.,F2A5 B0 47    BCS $F2EE       Serial bus
.,F2A7 C9 02    CMP #$02        RS232
.,F2A9 D0 1D    BNE $F2C8       nope, serial
.,F2AB 68       PLA             retrieve (A)
.,F2AC 20 F2 F2 JSR $F2F2       remove entry (A) from file table
.,F2AF 20 83 F4 JSR $F483       init RS232 port by using part of RS232OPEN
.,F2B2 20 27 FE JSR $FE27       MEMTOP, read top of memory (X/Y)
.,F2B5 A5 F8    LDA $F8         >RIBUF, RS232 input buffer
.,F2B7 F0 01    BEQ $F2BA
.,F2B9 C8       INY
.,F2BA A5 FA    LDA $FA         >ROBUF, RS232 output buffer
.,F2BC F0 01    BEQ $F2BF
.,F2BE C8       INY
.,F2BF A9 00    LDA #$00        Clear RS232 input/output buffers
.,F2C1 85 F8    STA $F8
.,F2C3 85 FA    STA $FA
.,F2C5 4C 7D F4 JMP $F47D       Set new ROBOF values and set new MEMTOP
.,F2C8 A5 B9    LDA $B9
.,F2CA 29 0F    AND #$0F
.,F2CC F0 23    BEQ $F2F1
.,F2CE 20 D0 F7 JSR $F7D0
.,F2D1 A9 00    LDA #$00
.,F2D3 38       SEC
.,F2D4 20 DD F1 JSR $F1DD
.,F2D7 20 64 F8 JSR $F864
.,F2DA 90 04    BCC $F2E0
.,F2DC 68       PLA
.,F2DD A9 00    LDA #$00
.,F2DF 60       RTS
.,F2E0 A5 B9    LDA $B9
.,F2E2 C9 62    CMP #$62
.,F2E4 D0 0B    BNE $F2F1
.,F2E6 A9 05    LDA #$05
.,F2E8 20 6A F7 JSR $F76A
.,F2EB 4C F1 F2 JMP $F2F1

                                *** CLOSE: CLOSE FILE, PART 2
.,F2EE 20 42 F6 JSR $F642       UNTALK/UNLISTEN serial device
.,F2F1 68       PLA
.,F2F2 AA       TAX
.,F2F3 C6 98    DEC $98         decrement LDTND, number of open files
.,F2F5 E4 98    CPX $98         compare LDTND to (X)
.,F2F7 F0 14    BEQ $F30D       equal, closed file = last file in table
.,F2F9 A4 98    LDY $98         else, move last entry to position of closed entry
.,F2FB B9 59 02 LDA $0259,Y     LAT, active filenumbers
.,F2FE 9D 59 02 STA $0259,X
.,F301 B9 63 02 LDA $0263,Y     FAT, active device numbers
.,F304 9D 63 02 STA $0263,X
.,F307 B9 6D 02 LDA $026D,Y     SAT, active secondary addresses
.,F30A 9D 6D 02 STA $026D,X
.,F30D 18       CLC
.,F30E 60       RTS             return

                                *** FIND FILE
                                This routine finds a logical file from it's file number.
                                On entry, (X) must hold the logical file number to be
                                found. LAT, the table of file numbers is searched, and if
                                found (X) contains the offset to the position of the file
                                in the table, and the Z flag is set. If not found, Z=0.
.,F30F A9 00    LDA #$00
.,F311 85 90    STA $90         clear STATUS
.,F313 8A       TXA             file number to search for
.,F314 A6 98    LDX $98         LDTND, number of open files
.,F316 CA       DEX
.,F317 30 15    BMI $F32E       end of table, return
.,F319 DD 59 02 CMP $0259,X     compare file number with LAT, table of open files
.,F31C D0 F8    BNE $F316       not equal, try next
.,F31E 60       RTS             back with Z flag set

                                *** SEET FILE VALUES
                                This routine sets the current logical file number, device
                                number and secondary address from the file parameter
                                tables. On entry (X) must hold the offset to the position
                                of the file in the table.
.,F31F BD 59 02 LDA $0259,X     LAT, table of active logical files
.,F322 85 B8    STA $B8         store in LA
.,F324 BD 63 02 LDA $0263,X     FAT, table of active device numbers
.,F327 85 BA    STA $BA         store in FA
.,F329 BD 6D 02 LDA $026D,X     SAT, table of active secondary addresses
.,F32C 85 B9    STA $B9         store in SAT
.,F32E 60       RTS             return

                                *** CLALL: ABORT ALL FILES
                                The KERNAL routine CLALL ($ffe7) is vectored here. The
                                number of open files are set to zero, and the next routine
                                is performed.
.,F32F A9 00    LDA #$00
.,F331 85 98    STA $98         clear LDTND, no open files

                                *** CLRCHN: RESTORE TO DEFAULT I/O
                                The KERNAL routine CLRCHN ($ffcc) is vectored here. The
                                default output device is UNLISTENed, if it is on the
                                serial bus, and the default output is set to the screen.
                                The default input device is UNTALKed, if it is on the
                                serial bus, and the default input device is set to
                                keyboard.
.,F333 A2 03    LDX #$03        check if device > 3 (serial bus is 4,5...)
.,F335 E4 9A    CPX $9A         test DFLTO, default output device
.,F337 B0 03    BCS $F33C       nope, no serial device
.,F339 20 FE ED JSR $EDFE       send UNLISTEN to serial bus
.,F33C E4 99    CPX $99         test DFLTI, default input device
.,F33E B0 03    BCS $F343       nope, no serial device
.,F340 20 EF ED JSR $EDEF       send UNTALK to serial bus
.,F343 86 9A    STX $9A         store screen as DFLTO
.,F345 A9 00    LDA #$00
.,F347 85 99    STA $99         store keyboard as DFLTI
.,F349 60       RTS

                                *** OPEN: OPEN FILE
                                The KERNAL routine OPEN ($ffc0) is vectored here. The file
                                paramerters must be set before entry. The routine reads
                                the LAT, to see if file already exists, which will result
                                in I/O error #2, ?FILE OPEN. A test is made to see if more
                                than 10 files are open. If so, I/O error #1, ?TOO MANY
                                FiLES, will occur. The file parameters are set, and put in
                                their respective tables. The device number is checked, and
                                each kind of device jumps to their own routine. Keyboard
                                and screen will exit here with no further actions. RS232
                                is opened via a seperate routine. SA, secondary address,
                                and filename will be sent on the serial bus.
.,F34A A6 B8    LDX $B8         LA, current logical number
.,F34C D0 03    BNE $F351
.,F34E 4C 0A F7 JMP $F70A       I/O error #6, not input file
.,F351 20 0F F3 JSR $F30F       find file (X)
.,F354 D0 03    BNE $F359
.,F356 4C FE F6 JMP $F6FE       I/O error #2, file exists
.,F359 A6 98    LDX $98         LDTND, number of open files
.,F35B E0 0A    CPX #$0A        more than ten
.,F35D 90 03    BCC $F362       nope
.,F35F 4C FB F6 JMP $F6FB       I/O error #1, too many files
.,F362 E6 98    INC $98         increment LDTND
.,F364 A5 B8    LDA $B8         LA
.,F366 9D 59 02 STA $0259,X     store in LAT, table of active file numbers
.,F369 A5 B9    LDA $B9         SA
.,F36B 09 60    ORA #$60        fixx
.,F36D 85 B9    STA $B9         store in SA
.,F36F 9D 6D 02 STA $026D,X     store in SAT, table of active secondary addresses
.,F372 A5 BA    LDA $BA         FA
.,F374 9D 63 02 STA $0263,X     store in FAT, table of active device numbers
.,F377 F0 5A    BEQ $F3D3       keyboard, end
.,F379 C9 03    CMP #$03        screen
.,F37B F0 56    BEQ $F3D3       yep, end
.,F37D 90 05    BCC $F384       less than 3, not serial bus
.,F37F 20 D5 F3 JSR $F3D5       send SA
.,F382 90 4F    BCC $F3D3       end
.,F384 C9 02    CMP #$02        TAPE
.,F386 D0 03    BNE $F38B       I/O error #5, device not present
.,F388 4C 09 F4 JMP $F409       open RS232 file

.,F38B 20 D0 F7 JSR $F7D0
.,F38E B0 03    BCS $F393
.,F390 4C 13 F7 JMP $F713
.,F393 A5 B9    LDA $B9
.,F395 29 0F    AND #$0F
.,F397 D0 1F    BNE $F3B8
.,F399 20 17 F8 JSR $F817
.,F39C B0 36    BCS $F3D4
.,F39E 20 AF F5 JSR $F5AF
.,F3A1 A5 B7    LDA $B7
.,F3A3 F0 0A    BEQ $F3AF
.,F3A5 20 EA F7 JSR $F7EA
.,F3A8 90 18    BCC $F3C2
.,F3AA F0 28    BEQ $F3D4
.,F3AC 4C 04 F7 JMP $F704
.,F3AF 20 2C F7 JSR $F72C
.,F3B2 F0 20    BEQ $F3D4
.,F3B4 90 0C    BCC $F3C2
.,F3B6 B0 F4    BCS $F3AC
.,F3B8 20 38 F8 JSR $F838
.,F3BB B0 17    BCS $F3D4
.,F3BD A9 04    LDA #$04
.,F3BF 20 6A F7 JSR $F76A
.,F3C2 A9 BF    LDA #$BF
.,F3C4 A4 B9    LDY $B9
.,F3C6 C0 60    CPY #$60
.,F3C8 F0 07    BEQ $F3D1
.,F3CA A0 00    LDY #$00
.,F3CC A9 02    LDA #$02
.,F3CE 91 B2    STA ($B2),Y
.,F3D0 98       TYA
.,F3D1 85 A6    STA $A6
.,F3D3 18       CLC
.,F3D4 60       RTS

                                *** SEND SA
                                This routine exits if there is no secondary address or
                                filename specifyed. The I/O status word, ST, is reset, and
                                the serial device is commanded to LISTEN. A check is made
                                for a possible ?DEVICE NOT PRESENT error. Finally, the
                                filename is sent to the device.
.,F3D5 A5 B9    LDA $B9         SA, current secondary address
.,F3D7 30 FA    BMI $F3D3       exit
.,F3D9 A4 B7    LDY $B7         FNLEN, length of filename
.,F3DB F0 F6    BEQ $F3D3       exit
.,F3DD A9 00    LDA #$00
.,F3DF 85 90    STA $90         clear STATUS, I/O status word
.,F3E1 A5 BA    LDA $BA         FA, current device number
.,F3E3 20 0C ED JSR $ED0C       send LISTEN to serial bus
.,F3E6 A5 B9    LDA $B9         SA
.,F3E8 09 F0    ORA #$F0
.,F3EA 20 B9 ED JSR $EDB9       send LISTEN SA
.,F3ED A5 90    LDA $90         STATUS
.,F3EF 10 05    BPL $F3F6       ok
.,F3F1 68       PLA             remove two stack entries for RTS command
.,F3F2 68       PLA
.,F3F3 4C 07 F7 JMP $F707       I/O error #5, device not present
.,F3F6 A5 B7    LDA $B7         FNLEN
.,F3F8 F0 0C    BEQ $F406       unlisten and exit
.,F3FA A0 00    LDY #$00        clear offset
.,F3FC B1 BB    LDA ($BB),Y     FNADR, pointer to filename
.,F3FE 20 DD ED JSR $EDDD       send byte on serial bus
.,F401 C8       INY             next character
.,F402 C4 B7    CPY $B7         until entire filename is sent
.,F404 D0 F6    BNE $F3FC       again
.,F406 4C 54 F6 JMP $F654       unlisten and exit

                                *** OPEN RS232
.,F409 20 83 F4 JSR $F483
.,F40C 8C 97 02 STY $0297
.,F40F C4 B7    CPY $B7
.,F411 F0 0A    BEQ $F41D
.,F413 B1 BB    LDA ($BB),Y
.,F415 99 93 02 STA $0293,Y
.,F418 C8       INY
.,F419 C0 04    CPY #$04
.,F41B D0 F2    BNE $F40F
.,F41D 20 4A EF JSR $EF4A
.,F420 8E 98 02 STX $0298
.,F423 AD 93 02 LDA $0293
.,F426 29 0F    AND #$0F
.,F428 F0 1C    BEQ $F446
.,F42A 0A       ASL
.,F42B AA       TAX
.,F42C AD A6 02 LDA $02A6
.,F42F D0 09    BNE $F43A
.,F431 BC C1 FE LDY $FEC1,X
.,F434 BD C0 FE LDA $FEC0,X
.,F437 4C 40 F4 JMP $F440
.,F43A BC EB E4 LDY $E4EB,X
.,F43D BD EA E4 LDA $E4EA,X
.,F440 8C 96 02 STY $0296
.,F443 8D 95 02 STA $0295
.,F446 AD 95 02 LDA $0295
.,F449 0A       ASL
.,F44A 20 2E FF JSR $FF2E
.,F44D AD 94 02 LDA $0294
.,F450 4A       LSR
.,F451 90 09    BCC $F45C
.,F453 AD 01 DD LDA $DD01
.,F456 0A       ASL
.,F457 B0 03    BCS $F45C
.,F459 20 0D F0 JSR $F00D
.,F45C AD 9B 02 LDA $029B
.,F45F 8D 9C 02 STA $029C
.,F462 AD 9E 02 LDA $029E
.,F465 8D 9D 02 STA $029D
.,F468 20 27 FE JSR $FE27
.,F46B A5 F8    LDA $F8
.,F46D D0 05    BNE $F474
.,F46F 88       DEY
.,F470 84 F8    STY $F8
.,F472 86 F7    STX $F7
.,F474 A5 FA    LDA $FA
.,F476 D0 05    BNE $F47D
.,F478 88       DEY
.,F479 84 FA    STY $FA
.,F47B 86 F9    STX $F9
.,F47D 38       SEC
.,F47E A9 F0    LDA #$F0
.,F480 4C 2D FE JMP $FE2D
.,F483 A9 7F    LDA #$7F
.,F485 8D 0D DD STA $DD0D
.,F488 A9 06    LDA #$06
.,F48A 8D 03 DD STA $DD03
.,F48D 8D 01 DD STA $DD01
.,F490 A9 04    LDA #$04
.,F492 0D 00 DD ORA $DD00
.,F495 8D 00 DD STA $DD00
.,F498 A0 00    LDY #$00
.,F49A 8C A1 02 STY $02A1
.,F49D 60       RTS

                                *** LOAD: LOAD RAM
                                The kernal routine LOAD ($ffd5) is vectoed here. If a
                                relocated load is desired, then the start address is set
                                in MEMUSS. The load/verify flag is set, and the I/O status
                                word is reset. A test is done on the device number, less
                                than 3 results in illegal device number.
.,F49E 86 C3    STX $C3         MEMUSS, relocated load address
.,F4A0 84 C4    STY $C4
.,F4A2 6C 30 03 JMP ($0330)     ILOAD vector. Points to $f4a5
.,F4A5 85 93    STA $93         VRECK, load/verify flag
.,F4A7 A9 00    LDA #$00
.,F4A9 85 90    STA $90         clear STATUS, I/O status
.,F4AB A5 BA    LDA $BA         get FA, current device
.,F4AD D0 03    BNE $F4B2       keyboard
.,F4AF 4C 13 F7 JMP $F713       I/O error #9, illegal device
.,F4B2 C9 03    CMP #$03        screen?
.,F4B4 F0 F9    BEQ $F4AF       yes, illegal device

                                *** LOAD FROM SERIAL BUS
                                The message 'SEARCHING' is printed and the filename is
                                sent with the TALK command and secondary address to the
                                serial bus. If EOI occurs at this point, then ?FILE NOT
                                FOUND is displayed. The message 'LOADING' or 'VERIFYING'
                                is output and a loop is entered, which recieves a byte
                                from the serial bus, checks the <STOP> key and either
                                stores the received byte, or compares it to the memory,
                                depending on the state of VERCK. Finally the bus is
                                UNTALKed.
.,F4B6 90 7B    BCC $F533       device < 3, eg tape or RS232, illegal device
.,F4B8 A4 B7    LDY $B7         FNLEN, length of filename
.,F4BA D0 03    BNE $F4BF       if length not is zero
.,F4BC 4C 10 F7 JMP $F710       'MISSING FILENAME'
.,F4BF A6 B9    LDX $B9         SA, current secondary address
.,F4C1 20 AF F5 JSR $F5AF       print "SEARCHING"
.,F4C4 A9 60    LDA #$60
.,F4C6 85 B9    STA $B9         set SA to $60
.,F4C8 20 D5 F3 JSR $F3D5       send SA and filename
.,F4CB A5 BA    LDA $BA         FA, current devicenumber
.,F4CD 20 09 ED JSR $ED09       send TALK to serial bus
.,F4D0 A5 B9    LDA $B9         SA
.,F4D2 20 C7 ED JSR $EDC7       send TALK SA
.,F4D5 20 13 EE JSR $EE13       receive from serial bus
.,F4D8 85 AE    STA $AE         load address, <EAL
.,F4DA A5 90    LDA $90         check STATUS
.,F4DC 4A       LSR
.,F4DD 4A       LSR
.,F4DE B0 50    BCS $F530       EOI set, file not found
.,F4E0 20 13 EE JSR $EE13       recieve from serial bus
.,F4E3 85 AF    STA $AF         load address, >EAL
.,F4E5 8A       TXA             retrieve SA and test relocated load
.,F4E6 D0 08    BNE $F4F0
.,F4E8 A5 C3    LDA $C3         use MEMUSS as load address
.,F4EA 85 AE    STA $AE         store in <EAL
.,F4EC A5 C4    LDA $C4
.,F4EE 85 AF    STA $AF         store in >EAL
.,F4F0 20 D2 F5 JSR $F5D2
.,F4F3 A9 FD    LDA #$FD        mask %11111101
.,F4F5 25 90    AND $90         read ST
.,F4F7 85 90    STA $90
.,F4F9 20 E1 FF JSR $FFE1       scan <STOP>
.,F4FC D0 03    BNE $F501       not stopped
.,F4FE 4C 33 F6 JMP $F633
.,F501 20 13 EE JSR $EE13      ACPTR, recrive from serial bus
.,F504 AA       TAX
.,F505 A5 90    LDA $90
.,F507 4A       LSR
.,F508 4A       LSR
.,F509 B0 E8    BCS $F4F3
.,F50B 8A       TXA
.,F50C A4 93    LDY $93
.,F50E F0 0C    BEQ $F51C       jump to LOAD
.,F510 A0 00    LDY #$00
.,F512 D1 AE    CMP ($AE),Y     compare with memory
.,F514 F0 08    BEQ $F51E       veryfied byte OK
.,F516 A9 10    LDA #$10
.,F518 20 1C FE JSR $FE1C
.:F51B 2C       .BYTE $2C       mask next write command
.,F51C 91 AE    STA ($AE),Y     store in memory
.,F51E E6 AE    INC $AE         increment <EAL, next address
.,F520 D0 02    BNE $F524       skip MSB
.,F522 E6 AF    INC $AF         increment >EAL
.,F524 24 90    BIT $90         test STATUS
.,F526 50 CB    BVC $F4F3       get next byte
.,F528 20 EF ED JSR $EDEF       send UNTALK to serial bus
.,F52B 20 42 F6 JSR $F642
.,F52E 90 79    BCC $F5A9       end routine
.,F530 4C 04 F7 JMP $F704       I/O error #4, file not found

.,F533 4A       LSR
.,F534 B0 03    BCS $F539
.,F536 4C 13 F7 JMP $F713
.,F539 20 D0 F7 JSR $F7D0
.,F53C B0 03    BCS $F541
.,F53E 4C 13 F7 JMP $F713
.,F541 20 17 F8 JSR $F817
.,F544 B0 68    BCS $F5AE
.,F546 20 AF F5 JSR $F5AF
.,F549 A5 B7    LDA $B7
.,F54B F0 09    BEQ $F556
.,F54D 20 EA F7 JSR $F7EA
.,F550 90 0B    BCC $F55D
.,F552 F0 5A    BEQ $F5AE
.,F554 B0 DA    BCS $F530
.,F556 20 2C F7 JSR $F72C
.,F559 F0 53    BEQ $F5AE
.,F55B B0 D3    BCS $F530
.,F55D A5 90    LDA $90
.,F55F 29 10    AND #$10
.,F561 38       SEC
.,F562 D0 4A    BNE $F5AE
.,F564 E0 01    CPX #$01
.,F566 F0 11    BEQ $F579
.,F568 E0 03    CPX #$03
.,F56A D0 DD    BNE $F549
.,F56C A0 01    LDY #$01
.,F56E B1 B2    LDA ($B2),Y
.,F570 85 C3    STA $C3
.,F572 C8       INY
.,F573 B1 B2    LDA ($B2),Y
.,F575 85 C4    STA $C4
.,F577 B0 04    BCS $F57D
.,F579 A5 B9    LDA $B9
.,F57B D0 EF    BNE $F56C
.,F57D A0 03    LDY #$03
.,F57F B1 B2    LDA ($B2),Y
.,F581 A0 01    LDY #$01
.,F583 F1 B2    SBC ($B2),Y
.,F585 AA       TAX
.,F586 A0 04    LDY #$04
.,F588 B1 B2    LDA ($B2),Y
.,F58A A0 02    LDY #$02
.,F58C F1 B2    SBC ($B2),Y
.,F58E A8       TAY
.,F58F 18       CLC
.,F590 8A       TXA
.,F591 65 C3    ADC $C3
.,F593 85 AE    STA $AE
.,F595 98       TYA
.,F596 65 C4    ADC $C4
.,F598 85 AF    STA $AF
.,F59A A5 C3    LDA $C3
.,F59C 85 C1    STA $C1
.,F59E A5 C4    LDA $C4
.,F5A0 85 C2    STA $C2
.,F5A2 20 D2 F5 JSR $F5D2
.,F5A5 20 4A F8 JSR $F84A
.:F5A8 24       .BYTE $24

                                *** LOAD END
                                This is the last part of the loader routine which sets the
                                (X/Y) register with the endaddress of the loaded program,
                                clears carry and exit.
.,F5A9 18       CLC
.,F5AA A6 AE    LDX $AE
.,F5AC A4 AF    LDY $AF
.,F5AE 60       RTS

                                *** PRINT "SEARCHING"
                                If MSGFLG indicates program mode then the message is not
                                printed, otherwise the message "SEARCHING" is printed from
                                the KERNAL I/O message table. If the length of
                                filename >0 then the message "FOR" is printed, and the
                                routine drops through to print the filename.
.,F5AF A5 9D    LDA $9D         MSGFLG, direct or program mode?
.,F5B1 10 1E    BPL $F5D1       program mode, don´t print, exit
.,F5B3 A0 0C    LDY #$0C
.,F5B5 20 2F F1 JSR $F12F       print "SEARCHING"
.,F5B8 A5 B7    LDA $B7         FNLEN, length of current filename
.,F5BA F0 15    BEQ $F5D1       no name, exit
.,F5BC A0 17    LDY #$17
.,F5BE 20 2F F1 JSR $F12F       print "FOR"

                                *** PRINT FILENAME
                                Filename is pointed to by FNADR, and length in FNLEN. The
                                KERNAL routine CHROUT is used to print filename.
.,F5C1 A4 B7    LDY $B7         FNLEN, length of current filename
.,F5C3 F0 0C    BEQ $F5D1       exit
.,F5C5 A0 00    LDY #$00
.,F5C7 B1 BB    LDA ($BB),Y     get character in filename
.,F5C9 20 D2 FF JSR $FFD2       output
.,F5CC C8       INY             next character
.,F5CD C4 B7    CPY $B7         ready?
.,F5CF D0 F6    BNE $F5C7
.,F5D1 60       RTS             back

                                *** PRINT "LOADING/VERIFYING"
                                The load/verify flag is checked, and if the message to be
                                output is flagged according to the result. This message is
                                printed from the KERNAL I/O messages table.
.,F5D2 A0 49    LDY #$49        offset to verify message
.,F5D4 A5 93    LDA $93         VERCK, load/verify flag
.,F5D6 F0 02    BEQ $F5DA       verify
.,F5D8 A0 59    LDY #$59        offset to load message
.,F5DA 4C 2B F1 JMP $F12B       output message flagged by (Y)

                                *** SAVE: SAVE RAM
                                The KERNAL routine SAVE ($ffd8) jumps to this routine. On
                                entry, (X/Y) must hold the end address+1 of the area of
                                memory to be saved. (A) holds the pointer to the start
                                address of the block, held in zeropage. The current device
                                number is checked to ensure that it is niether keyboard
                                (0) or screen (3). Both of these result in ?ILLEGAL DEVICE
                                NUMBER.
.,F5DD 86 AE    STX $AE         EAL , end address of block +1
.,F5DF 84 AF    STY $AF
.,F5E1 AA       TAX             move start pointer to (X)
.,F5E2 B5 00    LDA $00,X
.,F5E4 85 C1    STA $C1         STAL, start address of block
.,F5E6 B5 01    LDA $01,X
.,F5E8 85 C2    STA $C2
.,F5EA 6C 32 03 JMP ($0332)     vector ISAVE, points to $f5ed
.,F5ED A5 BA    LDA $BA         FA, current device number
.,F5EF D0 03    BNE $F5F4       ok
.,F5F1 4C 13 F7 JMP $F713       I/O error #9, illegal device number
.,F5F4 C9 03    CMP #$03        screen?
.,F5F6 F0 F9    BEQ $F5F1       yep, output error
.,F5F8 90 5F    BCC $F659       less than 3, ie. tape, output error

                                *** SAVE TO SERIAL BUS
                                A filename is assumed by the routine, or ?MISSING FILENAME
                                error is called. The serial device is commanded to LISTEN,
                                and the filename is sent along with the secondary address.
                                The message 'SAVING' is printed, and a loop sends a byte
                                to the serial bus and checks <STOP> key until the whole
                                specifyed block of memory has been saved. Note that the
                                first two bytes sent are the start address of the block.
                                Finally the serial bus is UNLISTENed.
.,F5FA A9 61    LDA #$61
.,F5FC 85 B9    STA $B9         set SA, secondary address, to #1
.,F5FE A4 B7    LDY $B7         FNLEN, length of current filename
.,F600 D0 03    BNE $F605       ok
.,F602 4C 10 F7 JMP $F710       I/O error #8, missing filename
.,F605 20 D5 F3 JSR $F3D5       send SA & filename
.,F608 20 8F F6 JSR $F68F       print 'SAVING' and filename
.,F60B A5 BA    LDA $BA         FA, current device number
.,F60D 20 0C ED JSR $ED0C       send LISTEN
.,F610 A5 B9    LDA $B9         SA
.,F612 20 B9 ED JSR $EDB9       send LISTEN SA
.,F615 A0 00    LDY #$00
.,F617 20 8E FB JSR $FB8E       reset pointer
.,F61A A5 AC    LDA $AC         SAL, holds start address
.,F61C 20 DD ED JSR $EDDD       send low byte of start address
.,F61F A5 AD    LDA $AD
.,F621 20 DD ED JSR $EDDD       send high byte of start address
.,F624 20 D1 FC JSR $FCD1       check read/write pointer
.,F627 B0 16    BCS $F63F
.,F629 B1 AC    LDA ($AC),Y     get character from memory
.,F62B 20 DD ED JSR $EDDD       send byte to serial device
.,F62E 20 E1 FF JSR $FFE1       test <STOP> key
.,F631 D0 07    BNE $F63A       not pressed
.,F633 20 42 F6 JSR $F642       exit and unlisten
.,F636 A9 00    LDA #$00        flag break
.,F638 38       SEC
.,F639 60       RTS
.,F63A 20 DB FC JSR $FCDB       bump r/w pointer
.,F63D D0 E5    BNE $F624       save next byte
.,F63F 20 FE ED JSR $EDFE       send UNLISTEN
.,F642 24 B9    BIT $B9         SA
.,F644 30 11    BMI $F657
.,F646 A5 BA    LDA $BA         FA
.,F648 20 0C ED JSR $ED0C       send LISTEN
.,F64B A5 B9    LDA $B9
.,F64D 29 EF    AND #$EF
.,F64F 09 E0    ORA #$E0
.,F651 20 B9 ED JSR $EDB9       send UNLISTEN SA
.,F654 20 FE ED JSR $EDFE       send UNLISTEN
.,F657 18       CLC
.,F658 60       RTS

.,F659 4A       LSR
.,F65A B0 03    BCS $F65F
.,F65C 4C 13 F7 JMP $F713
.,F65F 20 D0 F7 JSR $F7D0
.,F662 90 8D    BCC $F5F1
.,F664 20 38 F8 JSR $F838
.,F667 B0 25    BCS $F68E
.,F669 20 8F F6 JSR $F68F
.,F66C A2 03    LDX #$03
.,F66E A5 B9    LDA $B9
.,F670 29 01    AND #$01
.,F672 D0 02    BNE $F676
.,F674 A2 01    LDX #$01
.,F676 8A       TXA
.,F677 20 6A F7 JSR $F76A
.,F67A B0 12    BCS $F68E
.,F67C 20 67 F8 JSR $F867
.,F67F B0 0D    BCS $F68E
.,F681 A5 B9    LDA $B9
.,F683 29 02    AND #$02
.,F685 F0 06    BEQ $F68D
.,F687 A9 05    LDA #$05
.,F689 20 6A F7 JSR $F76A
.:F68C 24       .BYTE $24
.,F68D 18       CLC
.,F68E 60       RTS

                                *** PRINT 'SAVING'
                                MSGFLG is checked, and if direct mode is on, then the
                                message 'SAVING' is flagged and printed from the KERNAL
                                I/O message table.
.,F68F A5 9D    LDA $9D         MSGFLG
.,F691 10 FB    BPL $F68E       not in direct mode, exit
.,F693 A0 51    LDY #$51        offset to message in table
.,F695 20 2F F1 JSR $F12F       output 'SAVING'
.,F698 4C C1 F5 JMP $F5C1       output filename

                                *** UDTIM: BUMP CLOCK
                                The KERNAL routine UDTIM ($ffea) jumps to this routine.
                                The three byte jiffy clock in RAM is incremented. If it
                                has reached $4f1a01, then it is reset to zero. this number
                                represents 5184001 jiffies (each jiffy is 1/60 sec) or 24
                                hours. finally, the next routine is used to log the CIA
                                key reading.
.,F69B A2 00    LDX #$00
.,F69D E6 A2    INC $A2         low byte of jiffy clock
.,F69F D0 06    BNE $F6A7
.,F6A1 E6 A1    INC $A1         mid byte of jiffy clock
.,F6A3 D0 02    BNE $F6A7
.,F6A5 E6 A0    INC $A0         high byte of jiffy clock
.,F6A7 38       SEC
.,F6A8 A5 A2    LDA $A2         substract $4f1a01
.,F6AA E9 01    SBC #$01
.,F6AC A5 A1    LDA $A1
.,F6AE E9 1A    SBC #$1A
.,F6B0 A5 A0    LDA $A0
.,F6B2 E9 4F    SBC #$4F
.,F6B4 90 06    BCC $F6BC       and test carry if 24 hours
.,F6B6 86 A0    STX $A0         yepp, reset jiffy clock
.,F6B8 86 A1    STX $A1
.,F6BA 86 A2    STX $A2

                                *** LOG CIA KEY READING
                                This routine tests the keyboard for either <STOP> or <RVS>
                                pressed. If so, the keypress is stored in STKEY.
.,F6BC AD 01 DC LDA $DC01       keyboard read register
.,F6BF CD 01 DC CMP $DC01
.,F6C2 D0 F8    BNE $F6BC       wait for value to settle
.,F6C4 AA       TAX
.,F6C5 30 13    BMI $F6DA
.,F6C7 A2 BD    LDX #$BD
.,F6C9 8E 00 DC STX $DC00       keyboard write register
.,F6CC AE 01 DC LDX $DC01       keyboard read register
.,F6CF EC 01 DC CPX $DC01
.,F6D2 D0 F8    BNE $F6CC       wiat for value to settle
.,F6D4 8D 00 DC STA $DC00
.,F6D7 E8       INX
.,F6D8 D0 02    BNE $F6DC
.,F6DA 85 91    STA $91         STKEY, flag STOP/RVS
.,F6DC 60       RTS

                                *** RDTIM: GET TIME
                                The KERNAL routine RDTIM ($ffde) jumps to this routine.
                                The three byte jiffy clock is read into (A/X/Y) in the
                                format high/mid/low. The routine exits, setting the time
                                to its existing value in the next routine. The clock
                                resolution is 1/60 second. SEI is included since part of
                                the IRQ routine is to update the clock.
.,F6DD 78       SEI             disable interrupt
.,F6DE A5 A2    LDA $A2         read TIME
.,F6E0 A6 A1    LDX $A1
.,F6E2 A4 A0    LDY $A0

                                *** SETTIM: SET TIME
                                The KERNAL routine SETTIM ($ffdb) jumps to this routine.
                                On entry, (A/X/Y) must hold the value to be stored in the
                                clock. The forman is high/mid/low, and clock resolution is
                                1/60 second. SEI is included since part of the IRQ routine
                                is to update the clock.
.,F6E4 78       SEI             disable interrupt
.,F6E5 85 A2    STA $A2         wrine TIME
.,F6E7 86 A1    STX $A1
.,F6E9 84 A0    STY $A0
.,F6EB 58       CLI             enable interrupts
.,F6EC 60       RTS

                                *** STOP: CHECK <STOP> KEY
                                The KERNAL routine STOP ($ffe1) is vectored here. If STKEY
                                =#7f, then <STOP> was pressed and logged whilest the jiffy
                                clock was being updated, so all I/O channels are closed
                                and the keyboard buffer reset.
.,F6ED A5 91    LDA $91         STKEY
.,F6EF C9 7F    CMP #$7F        <STOP> ?
.,F6F1 D0 07    BNE $F6FA       nope
.,F6F3 08       PHP
.,F6F4 20 CC FF JSR $FFCC       CLRCHN, close all I/O channels
.,F6F7 85 C6    STA $C6         NDX, number of characters in keyboard buffer
.,F6F9 28       PLP
.,F6FA 60       RTS

                                *** OUTPUT KERNAL ERROR MESSAGES
                                The error message to be output is flagged into (A)
                                depending on the entry point. I/O channels are closed, and
                                then if KERNAL messages are enabled, "I/O ERROR #" is
                                printed along with the error number.
.,F6FB A9 01    LDA #$01        error #1, too many files
.:F6FD 2C       .BYTE $2C
.,F6FE A9 02    LDA #$02        error #2, file open
.:F700 2C       .BYTE $2C
.,F701 A9 03    LDA #$03        error #3, file not open
.:F703 2C       .BYTE $2C
.,F704 A9 04    LDA #$04        error #4, file not found
.:F706 2C       .BYTE $2C
.,F707 A9 05    LDA #$05        error #5, device not found
.:F709 2C       .BYTE $2C
.,F70A A9 06    LDA #$06        error #6, not input file
.:F70C 2C       .BYTE $2C
.,F70D A9 07    LDA #$07        error #7, not output file
.:F70F 2C       .BYTE $2C
.,F710 A9 08    LDA #$08        error #8, missing filename
.:F712 2C       .BYTE $2C
.,F713 A9 09    LDA #$09        error #9, illegal device number
.,F715 48       PHA
.,F716 20 CC FF JSR $FFCC       CLRCHN, close all I/O channels
.,F719 A0 00    LDY #$00
.,F71B 24 9D    BIT $9D         test MSGFLAG, KERNAL messages enabled
.,F71D 50 0A    BVC $F729       no
.,F71F 20 2F F1 JSR $F12F       print "I/O ERROR #"
.,F722 68       PLA
.,F723 48       PHA
.,F724 09 30    ORA #$30        convert (A) to ASCII number
.,F726 20 D2 FF JSR $FFD2       use CHROUT to print number in (A)
.,F729 68       PLA
.,F72A 38       SEC
.,F72B 60       RTS

.,F72C A5 93    LDA $93
.,F72E 48       PHA
.,F72F 20 41 F8 JSR $F841
.,F732 68       PLA
.,F733 85 93    STA $93
.,F735 B0 32    BCS $F769
.,F737 A0 00    LDY #$00
.,F739 B1 B2    LDA ($B2),Y
.,F73B C9 05    CMP #$05
.,F73D F0 2A    BEQ $F769
.,F73F C9 01    CMP #$01
.,F741 F0 08    BEQ $F74B
.,F743 C9 03    CMP #$03
.,F745 F0 04    BEQ $F74B
.,F747 C9 04    CMP #$04
.,F749 D0 E1    BNE $F72C
.,F74B AA       TAX
.,F74C 24 9D    BIT $9D
.,F74E 10 17    BPL $F767
.,F750 A0 63    LDY #$63
.,F752 20 2F F1 JSR $F12F
.,F755 A0 05    LDY #$05
.,F757 B1 B2    LDA ($B2),Y
.,F759 20 D2 FF JSR $FFD2
.,F75C C8       INY
.,F75D C0 15    CPY #$15
.,F75F D0 F6    BNE $F757
.,F761 A5 A1    LDA $A1
.,F763 20 E0 E4 JSR $E4E0
.,F766 EA       NOP
.,F767 18       CLC
.,F768 88       DEY
.,F769 60       RTS
.,F76A 85 9E    STA $9E
.,F76C 20 D0 F7 JSR $F7D0
.,F76F 90 5E    BCC $F7CF
.,F771 A5 C2    LDA $C2
.,F773 48       PHA
.,F774 A5 C1    LDA $C1
.,F776 48       PHA
.,F777 A5 AF    LDA $AF
.,F779 48       PHA
.,F77A A5 AE    LDA $AE
.,F77C 48       PHA
.,F77D A0 BF    LDY #$BF
.,F77F A9 20    LDA #$20
.,F781 91 B2    STA ($B2),Y
.,F783 88       DEY
.,F784 D0 FB    BNE $F781
.,F786 A5 9E    LDA $9E
.,F788 91 B2    STA ($B2),Y
.,F78A C8       INY
.,F78B A5 C1    LDA $C1
.,F78D 91 B2    STA ($B2),Y
.,F78F C8       INY
.,F790 A5 C2    LDA $C2
.,F792 91 B2    STA ($B2),Y
.,F794 C8       INY
.,F795 A5 AE    LDA $AE
.,F797 91 B2    STA ($B2),Y
.,F799 C8       INY
.,F79A A5 AF    LDA $AF
.,F79C 91 B2    STA ($B2),Y
.,F79E C8       INY
.,F79F 84 9F    STY $9F
.,F7A1 A0 00    LDY #$00
.,F7A3 84 9E    STY $9E
.,F7A5 A4 9E    LDY $9E
.,F7A7 C4 B7    CPY $B7
.,F7A9 F0 0C    BEQ $F7B7
.,F7AB B1 BB    LDA ($BB),Y
.,F7AD A4 9F    LDY $9F
.,F7AF 91 B2    STA ($B2),Y
.,F7B1 E6 9E    INC $9E
.,F7B3 E6 9F    INC $9F
.,F7B5 D0 EE    BNE $F7A5
.,F7B7 20 D7 F7 JSR $F7D7
.,F7BA A9 69    LDA #$69
.,F7BC 85 AB    STA $AB
.,F7BE 20 6B F8 JSR $F86B
.,F7C1 A8       TAY
.,F7C2 68       PLA
.,F7C3 85 AE    STA $AE
.,F7C5 68       PLA
.,F7C6 85 AF    STA $AF
.,F7C8 68       PLA
.,F7C9 85 C1    STA $C1
.,F7CB 68       PLA
.,F7CC 85 C2    STA $C2
.,F7CE 98       TYA
.,F7CF 60       RTS
.,F7D0 A6 B2    LDX $B2
.,F7D2 A4 B3    LDY $B3
.,F7D4 C0 02    CPY #$02
.,F7D6 60       RTS
.,F7D7 20 D0 F7 JSR $F7D0
.,F7DA 8A       TXA
.,F7DB 85 C1    STA $C1
.,F7DD 18       CLC
.,F7DE 69 C0    ADC #$C0
.,F7E0 85 AE    STA $AE
.,F7E2 98       TYA
.,F7E3 85 C2    STA $C2
.,F7E5 69 00    ADC #$00
.,F7E7 85 AF    STA $AF
.,F7E9 60       RTS
.,F7EA 20 2C F7 JSR $F72C
.,F7ED B0 1D    BCS $F80C
.,F7EF A0 05    LDY #$05
.,F7F1 84 9F    STY $9F
.,F7F3 A0 00    LDY #$00
.,F7F5 84 9E    STY $9E
.,F7F7 C4 B7    CPY $B7
.,F7F9 F0 10    BEQ $F80B
.,F7FB B1 BB    LDA ($BB),Y
.,F7FD A4 9F    LDY $9F
.,F7FF D1 B2    CMP ($B2),Y
.,F801 D0 E7    BNE $F7EA
.,F803 E6 9E    INC $9E
.,F805 E6 9F    INC $9F
.,F807 A4 9E    LDY $9E
.,F809 D0 EC    BNE $F7F7
.,F80B 18       CLC
.,F80C 60       RTS
.,F80D 20 D0 F7 JSR $F7D0
.,F810 E6 A6    INC $A6
.,F812 A4 A6    LDY $A6
.,F814 C0 C0    CPY #$C0
.,F816 60       RTS
.,F817 20 2E F8 JSR $F82E
.,F81A F0 1A    BEQ $F836
.,F81C A0 1B    LDY #$1B
.,F81E 20 2F F1 JSR $F12F
.,F821 20 D0 F8 JSR $F8D0
.,F824 20 2E F8 JSR $F82E
.,F827 D0 F8    BNE $F821
.,F829 A0 6A    LDY #$6A
.,F82B 4C 2F F1 JMP $F12F
.,F82E A9 10    LDA #$10
.,F830 24 01    BIT $01
.,F832 D0 02    BNE $F836
.,F834 24 01    BIT $01
.,F836 18       CLC
.,F837 60       RTS
.,F838 20 2E F8 JSR $F82E
.,F83B F0 F9    BEQ $F836
.,F83D A0 2E    LDY #$2E
.,F83F D0 DD    BNE $F81E
.,F841 A9 00    LDA #$00
.,F843 85 90    STA $90
.,F845 85 93    STA $93
.,F847 20 D7 F7 JSR $F7D7
.,F84A 20 17 F8 JSR $F817
.,F84D B0 1F    BCS $F86E
.,F84F 78       SEI
.,F850 A9 00    LDA #$00
.,F852 85 AA    STA $AA
.,F854 85 B4    STA $B4
.,F856 85 B0    STA $B0
.,F858 85 9E    STA $9E
.,F85A 85 9F    STA $9F
.,F85C 85 9C    STA $9C
.,F85E A9 90    LDA #$90
.,F860 A2 0E    LDX #$0E
.,F862 D0 11    BNE $F875
.,F864 20 D7 F7 JSR $F7D7
.,F867 A9 14    LDA #$14
.,F869 85 AB    STA $AB
.,F86B 20 38 F8 JSR $F838
.,F86E B0 6C    BCS $F8DC
.,F870 78       SEI
.,F871 A9 82    LDA #$82
.,F873 A2 08    LDX #$08
.,F875 A0 7F    LDY #$7F
.,F877 8C 0D DC STY $DC0D
.,F87A 8D 0D DC STA $DC0D
.,F87D AD 0E DC LDA $DC0E
.,F880 09 19    ORA #$19
.,F882 8D 0F DC STA $DC0F
.,F885 29 91    AND #$91
.,F887 8D A2 02 STA $02A2
.,F88A 20 A4 F0 JSR $F0A4
.,F88D AD 11 D0 LDA $D011
.,F890 29 EF    AND #$EF
.,F892 8D 11 D0 STA $D011
.,F895 AD 14 03 LDA $0314
.,F898 8D 9F 02 STA $029F
.,F89B AD 15 03 LDA $0315
.,F89E 8D A0 02 STA $02A0
.,F8A1 20 BD FC JSR $FCBD
.,F8A4 A9 02    LDA #$02
.,F8A6 85 BE    STA $BE
.,F8A8 20 97 FB JSR $FB97
.,F8AB A5 01    LDA $01
.,F8AD 29 1F    AND #$1F
.,F8AF 85 01    STA $01
.,F8B1 85 C0    STA $C0
.,F8B3 A2 FF    LDX #$FF
.,F8B5 A0 FF    LDY #$FF
.,F8B7 88       DEY
.,F8B8 D0 FD    BNE $F8B7
.,F8BA CA       DEX
.,F8BB D0 F8    BNE $F8B5
.,F8BD 58       CLI
.,F8BE AD A0 02 LDA $02A0
.,F8C1 CD 15 03 CMP $0315
.,F8C4 18       CLC
.,F8C5 F0 15    BEQ $F8DC
.,F8C7 20 D0 F8 JSR $F8D0
.,F8CA 20 BC F6 JSR $F6BC
.,F8CD 4C BE F8 JMP $F8BE
.,F8D0 20 E1 FF JSR $FFE1
.,F8D3 18       CLC
.,F8D4 D0 0B    BNE $F8E1
.,F8D6 20 93 FC JSR $FC93
.,F8D9 38       SEC
.,F8DA 68       PLA
.,F8DB 68       PLA
.,F8DC A9 00    LDA #$00
.,F8DE 8D A0 02 STA $02A0
.,F8E1 60       RTS
.,F8E2 86 B1    STX $B1
.,F8E4 A5 B0    LDA $B0
.,F8E6 0A       ASL
.,F8E7 0A       ASL
.,F8E8 18       CLC
.,F8E9 65 B0    ADC $B0
.,F8EB 18       CLC
.,F8EC 65 B1    ADC $B1
.,F8EE 85 B1    STA $B1
.,F8F0 A9 00    LDA #$00
.,F8F2 24 B0    BIT $B0
.,F8F4 30 01    BMI $F8F7
.,F8F6 2A       ROL
.,F8F7 06 B1    ASL $B1
.,F8F9 2A       ROL
.,F8FA 06 B1    ASL $B1
.,F8FC 2A       ROL
.,F8FD AA       TAX
.,F8FE AD 06 DC LDA $DC06
.,F901 C9 16    CMP #$16
.,F903 90 F9    BCC $F8FE
.,F905 65 B1    ADC $B1
.,F907 8D 04 DC STA $DC04
.,F90A 8A       TXA
.,F90B 6D 07 DC ADC $DC07
.,F90E 8D 05 DC STA $DC05
.,F911 AD A2 02 LDA $02A2
.,F914 8D 0E DC STA $DC0E
.,F917 8D A4 02 STA $02A4
.,F91A AD 0D DC LDA $DC0D
.,F91D 29 10    AND #$10
.,F91F F0 09    BEQ $F92A
.,F921 A9 F9    LDA #$F9
.,F923 48       PHA
.,F924 A9 2A    LDA #$2A
.,F926 48       PHA
.,F927 4C 43 FF JMP $FF43
.,F92A 58       CLI
.,F92B 60       RTS
.,F92C AE 07 DC LDX $DC07
.,F92F A0 FF    LDY #$FF
.,F931 98       TYA
.,F932 ED 06 DC SBC $DC06
.,F935 EC 07 DC CPX $DC07
.,F938 D0 F2    BNE $F92C
.,F93A 86 B1    STX $B1
.,F93C AA       TAX
.,F93D 8C 06 DC STY $DC06
.,F940 8C 07 DC STY $DC07
.,F943 A9 19    LDA #$19
.,F945 8D 0F DC STA $DC0F
.,F948 AD 0D DC LDA $DC0D
.,F94B 8D A3 02 STA $02A3
.,F94E 98       TYA
.,F94F E5 B1    SBC $B1
.,F951 86 B1    STX $B1
.,F953 4A       LSR
.,F954 66 B1    ROR $B1
.,F956 4A       LSR
.,F957 66 B1    ROR $B1
.,F959 A5 B0    LDA $B0
.,F95B 18       CLC
.,F95C 69 3C    ADC #$3C
.,F95E C5 B1    CMP $B1
.,F960 B0 4A    BCS $F9AC
.,F962 A6 9C    LDX $9C
.,F964 F0 03    BEQ $F969
.,F966 4C 60 FA JMP $FA60
.,F969 A6 A3    LDX $A3
.,F96B 30 1B    BMI $F988
.,F96D A2 00    LDX #$00
.,F96F 69 30    ADC #$30
.,F971 65 B0    ADC $B0
.,F973 C5 B1    CMP $B1
.,F975 B0 1C    BCS $F993
.,F977 E8       INX
.,F978 69 26    ADC #$26
.,F97A 65 B0    ADC $B0
.,F97C C5 B1    CMP $B1
.,F97E B0 17    BCS $F997
.,F980 69 2C    ADC #$2C
.,F982 65 B0    ADC $B0
.,F984 C5 B1    CMP $B1
.,F986 90 03    BCC $F98B
.,F988 4C 10 FA JMP $FA10
.,F98B A5 B4    LDA $B4
.,F98D F0 1D    BEQ $F9AC
.,F98F 85 A8    STA $A8
.,F991 D0 19    BNE $F9AC
.,F993 E6 A9    INC $A9
.,F995 B0 02    BCS $F999
.,F997 C6 A9    DEC $A9
.,F999 38       SEC
.,F99A E9 13    SBC #$13
.,F99C E5 B1    SBC $B1
.,F99E 65 92    ADC $92
.,F9A0 85 92    STA $92
.,F9A2 A5 A4    LDA $A4
.,F9A4 49 01    EOR #$01
.,F9A6 85 A4    STA $A4
.,F9A8 F0 2B    BEQ $F9D5
.,F9AA 86 D7    STX $D7
.,F9AC A5 B4    LDA $B4
.,F9AE F0 22    BEQ $F9D2
.,F9B0 AD A3 02 LDA $02A3
.,F9B3 29 01    AND #$01
.,F9B5 D0 05    BNE $F9BC
.,F9B7 AD A4 02 LDA $02A4
.,F9BA D0 16    BNE $F9D2
.,F9BC A9 00    LDA #$00
.,F9BE 85 A4    STA $A4
.,F9C0 8D A4 02 STA $02A4
.,F9C3 A5 A3    LDA $A3
.,F9C5 10 30    BPL $F9F7
.,F9C7 30 BF    BMI $F988
.,F9C9 A2 A6    LDX #$A6
.,F9CB 20 E2 F8 JSR $F8E2
.,F9CE A5 9B    LDA $9B
.,F9D0 D0 B9    BNE $F98B
.,F9D2 4C BC FE JMP $FEBC
.,F9D5 A5 92    LDA $92
.,F9D7 F0 07    BEQ $F9E0
.,F9D9 30 03    BMI $F9DE
.,F9DB C6 B0    DEC $B0
.:F9DD 2C       .BYTE $2C
.,F9DE E6 B0    INC $B0
.,F9E0 A9 00    LDA #$00
.,F9E2 85 92    STA $92
.,F9E4 E4 D7    CPX $D7
.,F9E6 D0 0F    BNE $F9F7
.,F9E8 8A       TXA
.,F9E9 D0 A0    BNE $F98B
.,F9EB A5 A9    LDA $A9
.,F9ED 30 BD    BMI $F9AC
.,F9EF C9 10    CMP #$10
.,F9F1 90 B9    BCC $F9AC
.,F9F3 85 96    STA $96
.,F9F5 B0 B5    BCS $F9AC
.,F9F7 8A       TXA
.,F9F8 45 9B    EOR $9B
.,F9FA 85 9B    STA $9B
.,F9FC A5 B4    LDA $B4
.,F9FE F0 D2    BEQ $F9D2
.,FA00 C6 A3    DEC $A3
.,FA02 30 C5    BMI $F9C9
.,FA04 46 D7    LSR $D7
.,FA06 66 BF    ROR $BF
.,FA08 A2 DA    LDX #$DA
.,FA0A 20 E2 F8 JSR $F8E2
.,FA0D 4C BC FE JMP $FEBC
.,FA10 A5 96    LDA $96
.,FA12 F0 04    BEQ $FA18
.,FA14 A5 B4    LDA $B4
.,FA16 F0 07    BEQ $FA1F
.,FA18 A5 A3    LDA $A3
.,FA1A 30 03    BMI $FA1F
.,FA1C 4C 97 F9 JMP $F997
.,FA1F 46 B1    LSR $B1
.,FA21 A9 93    LDA #$93
.,FA23 38       SEC
.,FA24 E5 B1    SBC $B1
.,FA26 65 B0    ADC $B0
.,FA28 0A       ASL
.,FA29 AA       TAX
.,FA2A 20 E2 F8 JSR $F8E2
.,FA2D E6 9C    INC $9C
.,FA2F A5 B4    LDA $B4
.,FA31 D0 11    BNE $FA44
.,FA33 A5 96    LDA $96
.,FA35 F0 26    BEQ $FA5D
.,FA37 85 A8    STA $A8
.,FA39 A9 00    LDA #$00
.,FA3B 85 96    STA $96
.,FA3D A9 81    LDA #$81
.,FA3F 8D 0D DC STA $DC0D
.,FA42 85 B4    STA $B4
.,FA44 A5 96    LDA $96
.,FA46 85 B5    STA $B5
.,FA48 F0 09    BEQ $FA53
.,FA4A A9 00    LDA #$00
.,FA4C 85 B4    STA $B4
.,FA4E A9 01    LDA #$01
.,FA50 8D 0D DC STA $DC0D
.,FA53 A5 BF    LDA $BF
.,FA55 85 BD    STA $BD
.,FA57 A5 A8    LDA $A8
.,FA59 05 A9    ORA $A9
.,FA5B 85 B6    STA $B6
.,FA5D 4C BC FE JMP $FEBC
.,FA60 20 97 FB JSR $FB97
.,FA63 85 9C    STA $9C
.,FA65 A2 DA    LDX #$DA
.,FA67 20 E2 F8 JSR $F8E2
.,FA6A A5 BE    LDA $BE
.,FA6C F0 02    BEQ $FA70
.,FA6E 85 A7    STA $A7
.,FA70 A9 0F    LDA #$0F
.,FA72 24 AA    BIT $AA
.,FA74 10 17    BPL $FA8D
.,FA76 A5 B5    LDA $B5
.,FA78 D0 0C    BNE $FA86
.,FA7A A6 BE    LDX $BE
.,FA7C CA       DEX
.,FA7D D0 0B    BNE $FA8A
.,FA7F A9 08    LDA #$08
.,FA81 20 1C FE JSR $FE1C
.,FA84 D0 04    BNE $FA8A
.,FA86 A9 00    LDA #$00
.,FA88 85 AA    STA $AA
.,FA8A 4C BC FE JMP $FEBC
.,FA8D 70 31    BVS $FAC0
.,FA8F D0 18    BNE $FAA9
.,FA91 A5 B5    LDA $B5
.,FA93 D0 F5    BNE $FA8A
.,FA95 A5 B6    LDA $B6
.,FA97 D0 F1    BNE $FA8A
.,FA99 A5 A7    LDA $A7
.,FA9B 4A       LSR
.,FA9C A5 BD    LDA $BD
.,FA9E 30 03    BMI $FAA3
.,FAA0 90 18    BCC $FABA
.,FAA2 18       CLC
.,FAA3 B0 15    BCS $FABA
.,FAA5 29 0F    AND #$0F
.,FAA7 85 AA    STA $AA
.,FAA9 C6 AA    DEC $AA
.,FAAB D0 DD    BNE $FA8A
.,FAAD A9 40    LDA #$40
.,FAAF 85 AA    STA $AA
.,FAB1 20 8E FB JSR $FB8E
.,FAB4 A9 00    LDA #$00
.,FAB6 85 AB    STA $AB
.,FAB8 F0 D0    BEQ $FA8A
.,FABA A9 80    LDA #$80
.,FABC 85 AA    STA $AA
.,FABE D0 CA    BNE $FA8A
.,FAC0 A5 B5    LDA $B5
.,FAC2 F0 0A    BEQ $FACE
.,FAC4 A9 04    LDA #$04
.,FAC6 20 1C FE JSR $FE1C
.,FAC9 A9 00    LDA #$00
.,FACB 4C 4A FB JMP $FB4A
.,FACE 20 D1 FC JSR $FCD1
.,FAD1 90 03    BCC $FAD6
.,FAD3 4C 48 FB JMP $FB48
.,FAD6 A6 A7    LDX $A7
.,FAD8 CA       DEX
.,FAD9 F0 2D    BEQ $FB08
.,FADB A5 93    LDA $93
.,FADD F0 0C    BEQ $FAEB
.,FADF A0 00    LDY #$00
.,FAE1 A5 BD    LDA $BD
.,FAE3 D1 AC    CMP ($AC),Y
.,FAE5 F0 04    BEQ $FAEB
.,FAE7 A9 01    LDA #$01
.,FAE9 85 B6    STA $B6
.,FAEB A5 B6    LDA $B6
.,FAED F0 4B    BEQ $FB3A
.,FAEF A2 3D    LDX #$3D
.,FAF1 E4 9E    CPX $9E
.,FAF3 90 3E    BCC $FB33
.,FAF5 A6 9E    LDX $9E
.,FAF7 A5 AD    LDA $AD
.,FAF9 9D 01 01 STA $0101,X
.,FAFC A5 AC    LDA $AC
.,FAFE 9D 00 01 STA $0100,X
.,FB01 E8       INX
.,FB02 E8       INX
.,FB03 86 9E    STX $9E
.,FB05 4C 3A FB JMP $FB3A
.,FB08 A6 9F    LDX $9F
.,FB0A E4 9E    CPX $9E
.,FB0C F0 35    BEQ $FB43
.,FB0E A5 AC    LDA $AC
.,FB10 DD 00 01 CMP $0100,X
.,FB13 D0 2E    BNE $FB43
.,FB15 A5 AD    LDA $AD
.,FB17 DD 01 01 CMP $0101,X
.,FB1A D0 27    BNE $FB43
.,FB1C E6 9F    INC $9F
.,FB1E E6 9F    INC $9F
.,FB20 A5 93    LDA $93
.,FB22 F0 0B    BEQ $FB2F
.,FB24 A5 BD    LDA $BD
.,FB26 A0 00    LDY #$00
.,FB28 D1 AC    CMP ($AC),Y
.,FB2A F0 17    BEQ $FB43
.,FB2C C8       INY
.,FB2D 84 B6    STY $B6
.,FB2F A5 B6    LDA $B6
.,FB31 F0 07    BEQ $FB3A
.,FB33 A9 10    LDA #$10
.,FB35 20 1C FE JSR $FE1C
.,FB38 D0 09    BNE $FB43
.,FB3A A5 93    LDA $93
.,FB3C D0 05    BNE $FB43
.,FB3E A8       TAY
.,FB3F A5 BD    LDA $BD
.,FB41 91 AC    STA ($AC),Y
.,FB43 20 DB FC JSR $FCDB
.,FB46 D0 43    BNE $FB8B
.,FB48 A9 80    LDA #$80
.,FB4A 85 AA    STA $AA
.,FB4C 78       SEI
.,FB4D A2 01    LDX #$01
.,FB4F 8E 0D DC STX $DC0D
.,FB52 AE 0D DC LDX $DC0D
.,FB55 A6 BE    LDX $BE
.,FB57 CA       DEX
.,FB58 30 02    BMI $FB5C
.,FB5A 86 BE    STX $BE
.,FB5C C6 A7    DEC $A7
.,FB5E F0 08    BEQ $FB68
.,FB60 A5 9E    LDA $9E
.,FB62 D0 27    BNE $FB8B
.,FB64 85 BE    STA $BE
.,FB66 F0 23    BEQ $FB8B
.,FB68 20 93 FC JSR $FC93
.,FB6B 20 8E FB JSR $FB8E
.,FB6E A0 00    LDY #$00
.,FB70 84 AB    STY $AB
.,FB72 B1 AC    LDA ($AC),Y
.,FB74 45 AB    EOR $AB
.,FB76 85 AB    STA $AB
.,FB78 20 DB FC JSR $FCDB
.,FB7B 20 D1 FC JSR $FCD1
.,FB7E 90 F2    BCC $FB72
.,FB80 A5 AB    LDA $AB
.,FB82 45 BD    EOR $BD
.,FB84 F0 05    BEQ $FB8B
.,FB86 A9 20    LDA #$20
.,FB88 20 1C FE JSR $FE1C
.,FB8B 4C BC FE JMP $FEBC

.,FB8E A5 C2    LDA $C2
.,FB90 85 AD    STA $AD
.,FB92 A5 C1    LDA $C1
.,FB94 85 AC    STA $AC
.,FB96 60       RTS

.,FB97 A9 08    LDA #$08
.,FB99 85 A3    STA $A3
.,FB9B A9 00    LDA #$00
.,FB9D 85 A4    STA $A4
.,FB9F 85 A8    STA $A8
.,FBA1 85 9B    STA $9B
.,FBA3 85 A9    STA $A9
.,FBA5 60       RTS
.,FBA6 A5 BD    LDA $BD
.,FBA8 4A       LSR
.,FBA9 A9 60    LDA #$60
.,FBAB 90 02    BCC $FBAF
.,FBAD A9 B0    LDA #$B0
.,FBAF A2 00    LDX #$00
.,FBB1 8D 06 DC STA $DC06
.,FBB4 8E 07 DC STX $DC07
.,FBB7 AD 0D DC LDA $DC0D
.,FBBA A9 19    LDA #$19
.,FBBC 8D 0F DC STA $DC0F
.,FBBF A5 01    LDA $01
.,FBC1 49 08    EOR #$08
.,FBC3 85 01    STA $01
.,FBC5 29 08    AND #$08
.,FBC7 60       RTS
.,FBC8 38       SEC
.,FBC9 66 B6    ROR $B6
.,FBCB 30 3C    BMI $FC09
.,FBCD A5 A8    LDA $A8
.,FBCF D0 12    BNE $FBE3
.,FBD1 A9 10    LDA #$10
.,FBD3 A2 01    LDX #$01
.,FBD5 20 B1 FB JSR $FBB1
.,FBD8 D0 2F    BNE $FC09
.,FBDA E6 A8    INC $A8
.,FBDC A5 B6    LDA $B6
.,FBDE 10 29    BPL $FC09
.,FBE0 4C 57 FC JMP $FC57
.,FBE3 A5 A9    LDA $A9
.,FBE5 D0 09    BNE $FBF0
.,FBE7 20 AD FB JSR $FBAD
.,FBEA D0 1D    BNE $FC09
.,FBEC E6 A9    INC $A9
.,FBEE D0 19    BNE $FC09
.,FBF0 20 A6 FB JSR $FBA6
.,FBF3 D0 14    BNE $FC09
.,FBF5 A5 A4    LDA $A4
.,FBF7 49 01    EOR #$01
.,FBF9 85 A4    STA $A4
.,FBFB F0 0F    BEQ $FC0C
.,FBFD A5 BD    LDA $BD
.,FBFF 49 01    EOR #$01
.,FC01 85 BD    STA $BD
.,FC03 29 01    AND #$01
.,FC05 45 9B    EOR $9B
.,FC07 85 9B    STA $9B
.,FC09 4C BC FE JMP $FEBC
.,FC0C 46 BD    LSR $BD
.,FC0E C6 A3    DEC $A3
.,FC10 A5 A3    LDA $A3
.,FC12 F0 3A    BEQ $FC4E
.,FC14 10 F3    BPL $FC09
.,FC16 20 97 FB JSR $FB97
.,FC19 58       CLI
.,FC1A A5 A5    LDA $A5
.,FC1C F0 12    BEQ $FC30
.,FC1E A2 00    LDX #$00
.,FC20 86 D7    STX $D7
.,FC22 C6 A5    DEC $A5
.,FC24 A6 BE    LDX $BE
.,FC26 E0 02    CPX #$02
.,FC28 D0 02    BNE $FC2C
.,FC2A 09 80    ORA #$80
.,FC2C 85 BD    STA $BD
.,FC2E D0 D9    BNE $FC09
.,FC30 20 D1 FC JSR $FCD1
.,FC33 90 0A    BCC $FC3F
.,FC35 D0 91    BNE $FBC8
.,FC37 E6 AD    INC $AD
.,FC39 A5 D7    LDA $D7
.,FC3B 85 BD    STA $BD
.,FC3D B0 CA    BCS $FC09
.,FC3F A0 00    LDY #$00
.,FC41 B1 AC    LDA ($AC),Y
.,FC43 85 BD    STA $BD
.,FC45 45 D7    EOR $D7
.,FC47 85 D7    STA $D7
.,FC49 20 DB FC JSR $FCDB
.,FC4C D0 BB    BNE $FC09
.,FC4E A5 9B    LDA $9B
.,FC50 49 01    EOR #$01
.,FC52 85 BD    STA $BD
.,FC54 4C BC FE JMP $FEBC
.,FC57 C6 BE    DEC $BE
.,FC59 D0 03    BNE $FC5E
.,FC5B 20 CA FC JSR $FCCA
.,FC5E A9 50    LDA #$50
.,FC60 85 A7    STA $A7
.,FC62 A2 08    LDX #$08
.,FC64 78       SEI
.,FC65 20 BD FC JSR $FCBD
.,FC68 D0 EA    BNE $FC54
.,FC6A A9 78    LDA #$78
.,FC6C 20 AF FB JSR $FBAF
.,FC6F D0 E3    BNE $FC54
.,FC71 C6 A7    DEC $A7
.,FC73 D0 DF    BNE $FC54
.,FC75 20 97 FB JSR $FB97
.,FC78 C6 AB    DEC $AB
.,FC7A 10 D8    BPL $FC54
.,FC7C A2 0A    LDX #$0A
.,FC7E 20 BD FC JSR $FCBD
.,FC81 58       CLI
.,FC82 E6 AB    INC $AB
.,FC84 A5 BE    LDA $BE
.,FC86 F0 30    BEQ $FCB8
.,FC88 20 8E FB JSR $FB8E
.,FC8B A2 09    LDX #$09
.,FC8D 86 A5    STX $A5
.,FC8F 86 B6    STX $B6
.,FC91 D0 83    BNE $FC16
.,FC93 08       PHP
.,FC94 78       SEI
.,FC95 AD 11 D0 LDA $D011
.,FC98 09 10    ORA #$10
.,FC9A 8D 11 D0 STA $D011
.,FC9D 20 CA FC JSR $FCCA
.,FCA0 A9 7F    LDA #$7F
.,FCA2 8D 0D DC STA $DC0D
.,FCA5 20 DD FD JSR $FDDD
.,FCA8 AD A0 02 LDA $02A0
.,FCAB F0 09    BEQ $FCB6
.,FCAD 8D 15 03 STA $0315
.,FCB0 AD 9F 02 LDA $029F
.,FCB3 8D 14 03 STA $0314
.,FCB6 28       PLP
.,FCB7 60       RTS
.,FCB8 20 93 FC JSR $FC93
.,FCBB F0 97    BEQ $FC54
.,FCBD BD 93 FD LDA $FD93,X
.,FCC0 8D 14 03 STA $0314
.,FCC3 BD 94 FD LDA $FD94,X
.,FCC6 8D 15 03 STA $0315
.,FCC9 60       RTS
.,FCCA A5 01    LDA $01
.,FCCC 09 20    ORA #$20
.,FCCE 85 01    STA $01
.,FCD0 60       RTS
.,FCD1 38       SEC
.,FCD2 A5 AC    LDA $AC
.,FCD4 E5 AE    SBC $AE
.,FCD6 A5 AD    LDA $AD
.,FCD8 E5 AF    SBC $AF
.,FCDA 60       RTS
.,FCDB E6 AC    INC $AC
.,FCDD D0 02    BNE $FCE1
.,FCDF E6 AD    INC $AD
.,FCE1 60       RTS

                                *** POWER RESET ENTRY POINT
                                The system hardware reset vector ($FFFC) points here. This
                                is the first routine executed when the computer is
                                switched on. The routine firstly sets the stackpointer to
                                #ff, disables interrupts and clears the decimal flag. It
                                jumps to a routine at $fd02 which checks for autostart-
                                cartridges. If so, an indirectjump is performed to the
                                cartridge coldstart vector at $8000. I/O chips are
                                initiated, and system constants are set up. Finaly the IRQ
                                is enabled, and an indirect jump is performed to $a000,
                                the basic cold start vector.
.,FCE2 A2 FF    LDX #$FF
.,FCE4 78       SEI
.,FCE5 9A       TXS             Set stackpointer to #ff
.,FCE6 D8       CLD
.,FCE7 20 02 FD JSR $FD02       Check ROM at $8000
.,FCEA D0 03    BNE $FCEF
.,FCEC 6C 00 80 JMP ($8000)     Jump to autostartvector
.,FCEF 8E 16 D0 STX $D016
.,FCF2 20 A3 FD JSR $FDA3       Init I/O
.,FCF5 20 50 FD JSR $FD50       Init system constants
.,FCF8 20 15 FD JSR $FD15       KERNAL reset
.,FCFB 20 5B FF JSR $FF5B       Setup PAL/NTSC
.,FCFE 58       CLI
.,FCFF 6C 00 A0 JMP ($A000)     Basic coldstart

                                *** CHECK FOR 8-ROM
                                Checks for the ROM autostartparametrar at $8004-$8008. It
                                compares data with $fd10, and if equal, set Z=1.
.,FD02 A2 05    LDX #$05        5 bytes to check
.,FD04 BD 0F FD LDA $FD0F,X     Identifyer at $fd10
.,FD07 DD 03 80 CMP $8003,X     Compare with $8004
.,FD0A D0 03    BNE $FD0F       NOT equal!
.,FD0C CA       DEX
.,FD0D D0 F5    BNE $FD04       until Z=1
.,FD0F 60       RTS

                                *** 8-ROM IDENTIFYER
                                The following 5 bytes contains the 8-ROM identifyer,
                                reading "CBM80" with CBM ASCII. It is used with
                                autostartcartridges. See $fd02.
.:FD10 C3 C2 CD 38 30           CBM80


                                *** RESTOR: KERNAL RESET
                                The KERNAL routine RESTOR ($ff8a) jumps to this routine.
                                It restores (copys) the KERNAL vectors at $fd30 to $0314-
                                $0333. Continues through VECTOR.
.,FD15 A2 30    LDX #$30        $fd30 - table of KERNAL vectors
.,FD17 A0 FD    LDY #$FD        Clear carry to SET values.
.,FD19 18       CLC

                                *** VECTOR: KERNAL MOVE
                                The KERNAL routine VECTOR ($ff8d) jumps to this routine.
                                It reads or sets the vactors at $0314-$0333 depending on
                                state of carry. X/Y contains the adress to read/write
                                area, normally $fd30. See $fd15.
                                A problem is that the RAM under the ROM at $fd30 always
                                gets a copy of the contents in the ROM then you perform
                                the copy.
.,FD1A 86 C3    STX $C3         MEMUSS - c3/c4 temporary used for adress
.,FD1C 84 C4    STY $C4
.,FD1E A0 1F    LDY #$1F        Number of bytes to transfer
.,FD20 B9 14 03 LDA $0314,Y
.,FD23 B0 02    BCS $FD27       Read or Write the vectors
.,FD25 B1 C3    LDA ($C3),Y
.,FD27 91 C3    STA ($C3),Y
.,FD29 99 14 03 STA $0314,Y
.,FD2C 88       DEY
.,FD2D 10 F1    BPL $FD20       Again...
.,FD2F 60       RTS

                                *** KERNAL RESET VECTORS
                                These are the vectors that is copyed to $0314-$0333 when
                                RESTOR is called.
.:FD30 31 EA                    CINV VECTOR: hardware interrupt ($ea31)
.:FD32 66 FE                    CBINV VECTOR: software interrupt ($fe66)
.:FD34 47 FE                    NMINV VECTOR: hardware nmi interrupt ($fe47)
.:FD36 4A F3                    IOPEN VECTOR: KERNAL open routine ($f3a4)
.:FD38 91 F2                    ICLOSE VECTOR: KERNAL close routine ($f291)
.:FD3A 0E F2                    ICHKIN VECTOR: KERNAL chkin routine ($f20e)
.:FD3C 50 F2                    ICKOUT VECTOR: KERNAL chkout routine ($f250)
.:FD3E 33 F3                    ICLRCH VECTOR: KERNAL clrchn routine ($f333)
.:FD40 57 F1                    IBASIN VECTOR: KERNAL chrin routine ($f157)
.:FD42 CA F1                    IBSOUT VECTOR: KERNAL chrout routine ($f1ca)
.:FD44 ED F6                    ISTOP VECTOR: KERNAL stop routine ($f6ed)
.:FD46 3E F1                    IGETIN VECTOR: KERNAL getin routine ($f13e)
.:FD48 2F F3                    ICLALL VECTOR: KERNAL clall routine ($f32f)
.:FD4A 66 FE                    USRCMD VECTOR: user defined ($fe66)
.:FD4C A5 F4                    ILOAD VECTOR: KERNAL load routine ($f4a5)
.:FD4E ED F5                    ISAVE VECTOR: KERNAL save routine ($f5ed)

                                *** RAMTAS: INIT SYSTEM CONSTANTS
                                The KERNAL routine RAMTAS($ff87) jumps to this routine. It
                                clears the pages 0,2 and 3 by writing 00 into them. It
                                also sets the start of the cassette buffer - $033c, and
                                determins how much free RAM-memory there is. The
                                memorycheck is performed by writing two different bytes
                                into all memory positions, starting at $0400, till it
                                reaches the ROM (the byte read is not the same as the one
                                you wrote.) Note that the contents of the memory is
                                restored afterwards. Finally, bottom of the memory, and
                                top of screen-pointers are set.
.,FD50 A9 00    LDA #$00
.,FD52 A8       TAY
.,FD53 99 02 00 STA $0002,Y     Fill pages 0,2,3 with zeros
.,FD56 99 00 02 STA $0200,Y
.,FD59 99 00 03 STA $0300,Y
.,FD5C C8       INY
.,FD5D D0 F4    BNE $FD53       all 256 bytes
.,FD5F A2 3C    LDX #$3C
.,FD61 A0 03    LDY #$03        Set tapebuffer to $033c
.,FD63 86 B2    STX $B2         Variables TAPE1 is used.
.,FD65 84 B3    STY $B3
.,FD67 A8       TAY
.,FD68 A9 03    LDA #$03
.,FD6A 85 C2    STA $C2
.,FD6C E6 C2    INC $C2
.,FD6E B1 C1    LDA ($C1),Y     Perform memorytest. Starting at $0400 and upwards.
.,FD70 AA       TAX             Store temporary in X-reg
.,FD71 A9 55    LDA #$55
.,FD73 91 C1    STA ($C1),Y     Write #$55 into memory
.,FD75 D1 C1    CMP ($C1),Y     and compare.
.,FD77 D0 0F    BNE $FD88       if not equal... ROM
.,FD79 2A       ROL
.,FD7A 91 C1    STA ($C1),Y     Write #$AA into same memory
.,FD7C D1 C1    CMP ($C1),Y     and compare again.
.,FD7E D0 08    BNE $FD88       if not equal... ROM
.,FD80 8A       TXA
.,FD81 91 C1    STA ($C1),Y     Restore stored value
.,FD83 C8       INY
.,FD84 D0 E8    BNE $FD6E       Next memorypos
.,FD86 F0 E4    BEQ $FD6C       New page in memory
.,FD88 98       TYA             The memorytest always exits when reaching a ROM
.,FD89 AA       TAX
.,FD8A A4 C2    LDY $C2
.,FD8C 18       CLC
.,FD8D 20 2D FE JSR $FE2D       Set top of memory. X and Y holds address.
.,FD90 A9 08    LDA #$08
.,FD92 8D 82 02 STA $0282       Set pointer to bottom of memory ($0800)
.,FD95 A9 04    LDA #$04
.,FD97 8D 88 02 STA $0288       Set pointer to bottom of screen ($0400)
.,FD9A 60       RTS

                                *** TAPE IRQ VECTORS
                                This table contains the vectors to the four tape-IRQ
                                routines.
.:FD9B 6A FC                    $fc6a - tape write
.:FD9D CD FB                    $fbcd - tape write II
.:FD9F 31 EA                    $ea31 - normal IRQ
.:FDA1 2C F9                    $f92c - tape read

                                *** IOINIT: INIT I/O
                                The KERNAL routine IOINIT ($ff84) jumps to this routine.
                                It sets the init-values for the CIAs (IRQ, DDRA, DRA
                                etc.), the SID-volume, and the processor onboard I/O port.
.,FDA3 A9 7F    LDA #$7F
.,FDA5 8D 0D DC STA $DC0D       CIA#1 IRQ control register
.,FDA8 8D 0D DD STA $DD0D       CIA#2 IRQ control register
.,FDAB 8D 00 DC STA $DC00       CIA#1 data port $ (keyboard)
.,FDAE A9 08    LDA #$08
.,FDB0 8D 0E DC STA $DC0E       CIA#1 control register timer A
.,FDB3 8D 0E DD STA $DD0E       CIA#2 control register timer A
.,FDB6 8D 0F DC STA $DC0F       CIA#1 control register timer B
.,FDB9 8D 0F DD STA $DD0F       CIA#2 control register timer B
.,FDBC A2 00    LDX #$00
.,FDBE 8E 03 DC STX $DC03       CIA#1 DDRB. Port B is input
.,FDC1 8E 03 DD STX $DD03       CIA#2 DDRB. Port B is input
.,FDC4 8E 18 D4 STX $D418       No sound from SID
.,FDC7 CA       DEX
.,FDC8 8E 02 DC STX $DC02       CIA#1 DDRA. Port A is output
.,FDCB A9 07    LDA #$07        %00000111
.,FDCD 8D 00 DD STA $DD00       CIA#2 dataport A. Set Videobank to $0000-$3fff
.,FDD0 A9 3F    LDA #$3F        %00111111
.,FDD2 8D 02 DD STA $DD02       CIA#2 DDRA. Serial bus and videobank
.,FDD5 A9 E7    LDA #$E7        6510 I/O port - %XX100111
.,FDD7 85 01    STA $01
.,FDD9 A9 2F    LDA #$2F        6510 I/O DDR - %00101111
.,FDDB 85 00    STA $00

                                *** ENABLE TIMER
                                This routine inits and starts the CIA#1 timer A according
                                to the PAL/NTSC flag. Different system clocks rates are
                                used in PAL/NTSC systems.
.,FDDD AD A6 02 LDA $02A6       PAL/NTSC flag
.,FDE0 F0 0A    BEQ $FDEC       NTSC setup
.,FDE2 A9 25    LDA #$25
.,FDE4 8D 04 DC STA $DC04       CIA#1 timer A - lowbyte
.,FDE7 A9 40    LDA #$40        PAL-setup #4025
.,FDE9 4C F3 FD JMP $FDF3
.,FDEC A9 95    LDA #$95
.,FDEE 8D 04 DC STA $DC04       CIA#1 timer A - lowbyte
.,FDF1 A9 42    LDA #$42        NTSC-setup #4295
.,FDF3 8D 05 DC STA $DC05       CIA#1 timer A - highbyte
.,FDF6 4C 6E FF JMP $FF6E       start timer

                                *** SETNAM: SAVE FILENAME DATA
                                The KERNAL routine SETNAM ($ffbd) jumps to this routine.
                                On entry, A-reg holds the length of the filename, and X/Y
                                the address in mem to the filename.
.,FDF9 85 B7    STA $B7         store length of filename in FNLEN
.,FDFB 86 BB    STX $BB         store pointer to filename in FNADDR
.,FDFD 84 BC    STY $BC
.,FDFF 60       RTS

                                *** SETLFS: SAVE FILE DETAILS
                                The KERNAL routine SETLFS ($ffba) jumps to this routine.
                                On entry A-reg holds the logical filenumber, X the device
                                number, and Y the secondary address.
.,FE00 85 B8    STA $B8         store logical filenumber in LA
.,FE02 86 BA    STX $BA         store devicenumber in FA
.,FE04 84 B9    STY $B9         store secondary address in SA
.,FE06 60       RTS

                                *** READST: READ STATUS
                                The KERNAL routine READST ($ffb7) jumps to this routine.
                                The routine checks if the current devicenumber is 2, (ie
                                RS232) then the value of RSSTAT (the ACIA 6551 status)is
                                returned in (A), and RSSTAT is cleared. Else it reads and
                                returnes the value of STATUS.
.,FE07 A5 BA    LDA $BA         read current device number from FA
.,FE09 C9 02    CMP #$02        device = RS232?
.,FE0B D0 0D    BNE $FE1A       nope, read STATUS
.,FE0D AD 97 02 LDA $0297       RSSTAT
.,FE10 48       PHA             temp store
.,FE11 A9 00    LDA #$00
.,FE13 8D 97 02 STA $0297       clear RSSTAT
.,FE16 68       PLA
.,FE17 60       RTS

                                *** SETMSG: FLAG STATUS
                                The KERNAL routine SETMSG ($ff90) jumps to this routine.
                                On entry, the value in (A) is stored in MSGFLG, then the
                                I/O status is placed in (A). If routine is entered at
                                $fe1c the contents in (A) will be stored in STATUS.
.,FE18 85 9D    STA $9D         store MSGFLG
.,FE1A A5 90    LDA $90         read STATUS
.,FE1C 05 90    ORA $90
.,FE1E 85 90    STA $90
.,FE20 60       RTS

                                *** SETTMO: SET TIMEOUT
                                The KERNAL routine SETTMO ($ffa2) jumps to this routine.
                                On entry the value in (A) is stored in the IEEE timeout
                                flag. (Who uses IEEE nowadays?)
.,FE21 8D 85 02 STA $0285       store in TIMOUT
.,FE24 60       RTS

                                *** MEMTOP: READ/SET TOP OF MEMORY
                                The KERNAL routine MEMTOP ($ffa9) jumps to this routine.
                                If carry is set on entry, the top of memory address will
                                be loaded into (X/Y). If carry is clear on entry, the top
                                of memory will be set according to the contents in (X/Y)
.,FE25 90 06    BCC $FE2D       carry clear?
.,FE27 AE 83 02 LDX $0283       read memtop from MEMSIZ
.,FE2A AC 84 02 LDY $0284
.,FE2D 8E 83 02 STX $0283       store memtop in MEMSIZ
.,FE30 8C 84 02 STY $0284
.,FE33 60       RTS

                                *** MEMBOT: READ/SET BOTTOM OF MEMORY
                                The KERNAL routine MEMBOT ($ff9c) jumps to this routine.
                                If carry is set on entry, the bottom of memory address
                                will be loaded into (X/Y). If carry is clear on entry, the
                                bottom of memory will set according to the contents in
                                (X/Y)
.,FE34 90 06    BCC $FE3C       carry clear?
.,FE36 AE 81 02 LDX $0281       read membot from MEMSTR
.,FE39 AC 82 02 LDY $0282
.,FE3C 8E 81 02 STX $0281       store membot in MEMSTR
.,FE3F 8C 82 02 STY $0282
.,FE42 60       RTS

                                *** NMI ENTRY POINT
                                The processor jumps to this routine every time a NMI
                                occurs (see jump vector at $fffa). On entry all processor
                                registers will be put on the stack. The routine will check
                                the presents of a ROM cartridge at $8000 with autostart,
                                and warm start it. Otherwise, the following warm start
                                routine is called.
.,FE43 78       SEI             disable interrupts
.,FE44 6C 18 03 JMP ($0318)     jump to NMINV, points normally to $fe47
.,FE47 48       PHA             store (A), (X), (Y) on the stack
.,FE48 8A       TXA
.,FE49 48       PHA
.,FE4A 98       TYA
.,FE4B 48       PHA
.,FE4C A9 7F    LDA #$7F        CIA#2 interrupt control register
.,FE4E 8D 0D DD STA $DD0D
.,FE51 AC 0D DD LDY $DD0D
.,FE54 30 1C    BMI $FE72       NMI caused by RS232? If so - jump
.,FE56 20 02 FD JSR $FD02       check for autostart at $8000
.,FE59 D0 03    BNE $FE5E
.,FE5B 6C 02 80 JMP ($8002)     Jump to warm start vector
.,FE5E 20 BC F6 JSR $F6BC       Scan 1 row in keymatrix and store value in $91
.,FE61 20 E1 FF JSR $FFE1       Check $91 to see if <STOP> was pressed
.,FE64 D0 0C    BNE $FE72       <STOP> not pressed, skip part of following routine

                                *** WARM START BASIC
                                This routine is called from the NMI routine above. If
                                <STOP> was pressed, then KERNAL vectors are restored to
                                default values, I/O vectors initialised and a jump to
                                ($a002), the Basic warm start vector.
                                The NMI routine continues at $fe72 by checking the RS232,
                                if there is anyting to send.
.,FE66 20 15 FD JSR $FD15       KERNAL reset
.,FE69 20 A3 FD JSR $FDA3       init I/O
.,FE6C 20 18 E5 JSR $E518       init I/O
.,FE6F 6C 02 A0 JMP ($A002)     jump to Basic warm start vector

                                *** NMI RS232 HANDLING
.,FE72 98       TYA             Read CIA#2 interrupt control register
.,FE73 2D A1 02 AND $02A1       mask with ENABL, RS232 enable
.,FE76 AA       TAX             temp store in (X)
.,FE77 29 01    AND #$01        test if sending (%00000001)
.,FE79 F0 28    BEQ $FEA3       nope, jump to recieve test
.,FE7B AD 00 DD LDA $DD00       load CIA#1 DRA
.,FE7E 29 FB    AND #$FB        mask bit2 (RS232 send)
.,FE80 05 B5    ORA $B5         NXTBIT, next bit to send
.,FE82 8D 00 DD STA $DD00       and write to port
.,FE85 AD A1 02 LDA $02A1
.,FE88 8D 0D DD STA $DD0D       write ENABL to CIA#2 I.C.R
.,FE8B 8A       TXA             get temp
.,FE8C 29 12    AND #$12        test if recieving (bit1), or waiting for reciever
                                edge (bit4) ($12 = %00010010)
.,FE8E F0 0D    BEQ $FE9D       nope, skip reciever routine
.,FE90 29 02    AND #$02        test if recieving
.,FE92 F0 06    BEQ $FE9A       nope
.,FE94 20 D6 FE JSR $FED6       jump to NMI RS232 in
.,FE97 4C 9D FE JMP $FE9D
.,FE9A 20 07 FF JSR $FF07       jump to NMI RS232 out
.,FE9D 20 BB EE JSR $EEBB       RS232 send byte
.,FEA0 4C B6 FE JMP $FEB6       goto exit
.,FEA3 8A       TXA             get temp
.,FEA4 29 02    AND #$02        test bit1
.,FEA6 F0 06    BEQ $FEAE       nope
.,FEA8 20 D6 FE JSR $FED6       NMI RS232 in???
.,FEAB 4C B6 FE JMP $FEB6       goto exit
.,FEAE 8A       TXA             set temp
.,FEAF 29 10    AND #$10        test bit4
.,FEB1 F0 03    BEQ $FEB6       nope, exit
.,FEB3 20 07 FF JSR $FF07       NMI RS232 out
.,FEB6 AD A1 02 LDA $02A1       ENABL
.,FEB9 8D 0D DD STA $DD0D       CIA#2 interrupt control register
.,FEBC 68       PLA             restore registers (Y),(X),(A)
.,FEBD A8       TAY
.,FEBE 68       PLA
.,FEBF AA       TAX
.,FEC0 68       PLA
.,FEC1 40       RTI             back from NMI

                                *** RS232 TIMING TABLE - NTSC
                                Timingtable for RS232 NMI for use with NTSC machines. The
                                table containe 10 entries which corresponds to one of the
                                fixed RS232 rates, starting with lowest (50 baud) and
                                finishing with the highest (2400 baud). Since the clock
                                frequency is different between NTSC and PAL systems, there
                                is another table for PAL machines at $e4ec.
.:FEC2 C1 27                    50 baud
.:FEC4 3E 1A                    75 baud
.:FEC6 C5 11                    110 baud
.:FEC8 74 0E                    134.5 baud
.:FECA ED 0C                    150 baud
.:FECC 45 06                    300 baud
.:FECE F0 02                    600 baud
.:FED0 46 01                    1200 baud
.:FED2 B8 00                    (1800) 2400 baud
.:FED4 71 00                    2400 baud

                                *** NMI RS232 IN
                                This routine inputs a bit from the RS232 port and sets the
                                baudrate timing for the next bit. Continues to the RS232
                                recieve routine.
.,FED6 AD 01 DD LDA $DD01       RS232 I/O port
.,FED9 29 01    AND #$01        test bit0, received data
.,FEDB 85 A7    STA $A7         store in INBIT
.,FEDD AD 06 DD LDA $DD06       lowbyte of timer B
.,FEE0 E9 1C    SBC #$1C
.,FEE2 6D 99 02 ADC $0299       <BAUDOF
.,FEE5 8D 06 DD STA $DD06       store timer B
.,FEE8 AD 07 DD LDA $DD07       highbyte of timer B
.,FEEB 6D 9A 02 ADC $029A       >BAUDOF
.,FEEE 8D 07 DD STA $DD07       store timer B
.,FEF1 A9 11    LDA #$11
.,FEF3 8D 0F DD STA $DD0F       CIA#2 control register B
.,FEF6 AD A1 02 LDA $02A1       ENABL
.,FEF9 8D 0D DD STA $DD0D       CIA#2 interrupt control register
.,FEFC A9 FF    LDA #$FF
.,FEFE 8D 06 DD STA $DD06
.,FF01 8D 07 DD STA $DD07
.,FF04 4C 59 EF JMP $EF59       jump to RS232 receive routine

                                *** NMI RS232 OUT
                                This routine sets up the baudrate for sending the bits
                                out, and adjusts the number of bits remaining to send.
.,FF07 AD 95 02 LDA $0295       M51AJB - non standard BPS time
.,FF0A 8D 06 DD STA $DD06       timer B low
.,FF0D AD 96 02 LDA $0296
.,FF10 8D 07 DD STA $DD07       timer B high
.,FF13 A9 11    LDA #$11
.,FF15 8D 0F DD STA $DD0F       CIA#2 control register B
.,FF18 A9 12    LDA #$12
.,FF1A 4D A1 02 EOR $02A1
.,FF1D 8D A1 02 STA $02A1       ENABL, RS232 enables
.,FF20 A9 FF    LDA #$FF
.,FF22 8D 06 DD STA $DD06
.,FF25 8D 07 DD STA $DD07       timer B
.,FF28 AE 98 02 LDX $0298       BITNUM, number of bits still to send in this byte
.,FF2B 86 A8    STX $A8         BITC1, RS232 bitcount
.,FF2D 60       RTS
.,FF2E AA       TAX
.,FF2F AD 96 02 LDA $0296
.,FF32 2A       ROL
.,FF33 A8       TAY
.,FF34 8A       TXA
.,FF35 69 C8    ADC #$C8
.,FF37 8D 99 02 STA $0299
.,FF3A 98       TYA
.,FF3B 69 00    ADC #$00
.,FF3D 8D 9A 02 STA $029A
.,FF40 60       RTS
.,FF41 EA       NOP
.,FF42 EA       NOP

                                *** FAKE IRQ TAPE
.,FF43 08       PHP             store processor reg.
.,FF44 68       PLA             get reg
.,FF45 29 EF    AND #$EF        clear bit4
.,FF47 48       PHA             store reg

                                *** IRQ ENTRY
                                This routine is pointed to by the hardware IRQ vector at
                                $fffe. This routine is able to distinguish between a
                                hardware IRQ, and a software BRK. The two types of
                                interrupts are processed by its own routine.
.,FF48 48       PHA             Store Acc
.,FF49 8A       TXA
.,FF4A 48       PHA             Store X-reg
.,FF4B 98       TYA
.,FF4C 48       PHA             Store Y-reg
.,FF4D BA       TSX
.,FF4E BD 04 01 LDA $0104,X     Read byte on stack written by processor?
.,FF51 29 10    AND #$10        check bit 4 to determine HW or SW interrupt
.,FF53 F0 03    BEQ $FF58
.,FF55 6C 16 03 JMP ($0316)     jump to CBINV. Points to FE66, basic warm start
.,FF58 6C 14 03 JMP ($0314)     jump to CINV. Points to EA31, main IRQ entry point

                                *** CINT: INIT SCREEN EDITOR
                                The KERNAL routine CINT ($FF81) jumps to this routine. It
                                sets up VIC for operation. The original CINT is at $e518,
                                and this patch checks out if this is a PAL or NTSC
                                machine. This is done by setting the raster compare
                                register to 311, which is the number of scanlines in a PAL
                                machine. If no interrupt occurs, then it's a NTSC machine.
.,FF5B 20 18 E5 JSR $E518       original I/O init
.,FF5E AD 12 D0 LDA $D012       wait for top of screen
.,FF61 D0 FB    BNE $FF5E       at line zero
.,FF63 AD 19 D0 LDA $D019       Check IRQ flag register if interrupt occured
.,FF66 29 01    AND #$01        only first bit
.,FF68 8D A6 02 STA $02A6       store in PAL/NTSC flag
.,FF6B 4C DD FD JMP $FDDD       jump to ENABLE TIMER

                                *** START TIMER
                                This routine starts the CIA#1 timer and jumps into a
                                routine that handles the serial clock.
.,FF6E A9 81    LDA #$81        Enable IRQ when timer B reaches zero
.,FF70 8D 0D DC STA $DC0D       CIA#1 interrupt controll register
.,FF73 AD 0E DC LDA $DC0E       CIA#1 control register A
.,FF76 29 80    AND #$80
.,FF78 09 11    ORA #$11        Force load of timer A values -bit4, and start -bit0
.,FF7A 8D 0E DC STA $DC0E       Action!
.,FF7D 4C 8E EE JMP $EE8E       Continue to 'serial clock off'

                                *** KERNAL VERSION ID
                                This byte contains the version number of the KERNAL.
.:FF80 03

                                *** KERNAL JUMP TABLE
                                This table contains jump vectors to the I/O routines. This
                                is a Commodore standard, so no matter what system you are
                                using (VIC20, C64, C128, Plus4 etc) the jump vectors are
                                always located at this position.
.,FF81 4C 5B FF JMP $FF5B       CINT, init screen editor
.,FF84 4C A3 FD JMP $FDA3       IOINT, init input/output
.,FF87 4C 50 FD JMP $FD50       RAMTAS, init RAM, tape screen
.,FF8A 4C 15 FD JMP $FD15       RESTOR, restore default I/O vector
.,FF8D 4C 1A FD JMP $FD1A       VECTOR, read/set I/O vector
.,FF90 4C 18 FE JMP $FE18       SETMSG, control KERNAL messages
.,FF93 4C B9 ED JMP $EDB9       SECOND, send SA after LISTEN
.,FF96 4C C7 ED JMP $EDC7       TKSA, send SA after TALK
.,FF99 4C 25 FE JMP $FE25       MEMTOP, read/set top of memory
.,FF9C 4C 34 FE JMP $FE34       MEMBOT, read/set bottom of memory
.,FF9F 4C 87 EA JMP $EA87       SCNKEY, scan keyboard
.,FFA2 4C 21 FE JMP $FE21       SETTMO, set IEEE timeout
.,FFA5 4C 13 EE JMP $EE13       ACPTR, input byte from serial bus
.,FFA8 4C DD ED JMP $EDDD       CIOUT, output byte to serial bus
.,FFAB 4C EF ED JMP $EDEF       UNTALK, command serial bus UNTALK
.,FFAE 4C FE ED JMP $EDFE       UNLSN, command serial bus UNLSN
.,FFB1 4C 0C ED JMP $ED0C       LISTEN, command serial bus LISTEN
.,FFB4 4C 09 ED JMP $ED09       TALK, command serial bus TALK
.,FFB7 4C 07 FE JMP $FE07       READST, read I/O status word
.,FFBA 4C 00 FE JMP $FE00       SETLFS, set logical file parameters
.,FFBD 4C F9 FD JMP $FDF9       SETNAM, set filename
.,FFC0 6C 1A 03 JMP ($031A)     OPEN, open file
.,FFC3 6C 1C 03 JMP ($031C)     CLOSE, close file
.,FFC6 6C 1E 03 JMP ($031E)     CHKIN, prepare channel for input
.,FFC9 6C 20 03 JMP ($0320)     CHKOUT, prepare channel for output
.,FFCC 6C 22 03 JMP ($0322)     CLRCHN, close all I/O
.,FFCF 6C 24 03 JMP ($0324)     CHRIN, inpup byte from channel
.,FFD2 6C 26 03 JMP ($0326)     CHROUT, output byte to channel
.,FFD5 4C 9E F4 JMP $F49E       LOAD, load from serial device
.,FFD8 4C DD F5 JMP $F5DD       SAVE, save to serial device
.,FFDB 4C E4 F6 JMP $F6E4       SETTIM, set realtime clock
.,FFDE 4C DD F6 JMP $F6DD       RDTIM, read realtime clock
.,FFE1 6C 28 03 JMP ($0328)     STOP, check <STOP> key
.,FFE4 6C 2A 03 JMP ($032A)     GETIN, get input from keyboard
.,FFE7 6C 2C 03 JMP ($032C)     CLALL, close all files and channels
.,FFEA 4C 9B F6 JMP $F69B       UDTIM, increment realtime clock
.,FFED 4C 05 E5 JMP $E505       SCREEN, return screen organisation
.,FFF0 4C 0A E5 JMP $E50A       PLOT, read/set cursor X/Y position
.,FFF3 4C 00 E5 JMP $E500       IOBASE, return IOBASE address

.:FFF6 52 52 42 59

                                *** SYSTEM HARDWARE VECTORS
                                This table contains jumpvectors for system reset, IRQ, and
                                NMI. The IRQ and NMI vectors points to addresses which
                                contains an indirect jump to RAM, to provide user defined
                                routines.
.:FFFA 43 FE
.:FFFC E2 FC
.:FFFE 48 FF
