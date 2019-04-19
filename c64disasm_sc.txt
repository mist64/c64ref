- Fully Commented Commodore 64 BASIC ROM Disassembly (English, "S-C")
-
- The comments have been taken from
-    Bob Sander-Cederlof: S-C DocuMentor for Applesoft
-    http://www.txbobsc.com/scsc/scdocumentor/
-
- The original comments are based on a disassembly of Applesoft BASIC
- as found in the ROMs of the Apple II. C64 BASIC V2 and Applesoft BASIC
- are both based on Microsoft BASIC for 6502, albeit on different versions,
- and they both add incompatible extensions. Nevertheless, they are still
- extremely similar, so that Bob Sander-Cederlof's Applestoft comments could
- be semi-automatically ported over to the version of BASIC in the ROM of
- the Commodore 64.
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

.:A000 94 E3
.:A002 7B E3

.:A004 43 42 4D 42 41 53 49 43  'cbmbasic'

                                *** BRANCH TABLE FOR TOKENS
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

                                *** MATH OPERATOR BRANCH TABLE
                                ONE-BYTE PRECEDENCE CODE
                                TWO-BYTE ADDRESS
.:A080 79 69 B8                 $79, $B86A +
.:A083 79 52 B8                 $79, $B853 -
.:A086 7B 2A BA                 $7B, $BA2B *
.:A089 7B 11 BB                 $7B, $BB12 /
.:A08C 7F 7A BF                 $7F, $BF7B ^
.:A08F 50 E8 AF                 $50, $AFE9 AND
.:A092 46 E5 AF                 $46, $AFE6 OR (LOWEST PRECEDENCE)
.:A095 7D B3 BF                 $7D, $BFB4 >
.:A098 5A D3 AE                 $5A, $AED4 =
.:A09B 64 15 B0                 $64, $B016 <
                                *** TOKEN NAME TABLE
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
.:A148 4F D2 BE BD BC           or <=>
.:A14D                53 47 CE  sgn
.:A150 49 4E D4 41 42 D3 55 53  int abs usr
.:A158 D2 46 52 C5 50 4F D3 53  fre pos sqr
.:A160 51 D2 52 4E C4 4C 4F C7  rnd log
.:A168 45 58 D0 43 4F D3 53 49  exp cos sin
.:A170 CE 54 41 CE 41 54 CE 50  tan atn peek
.:A178 45 45 CB 4C 45 CE 53 54  len str$
.:A180 52 A4 56 41 CC 41 53 C3  val asc
.:A188 43 48 52 A4 4C 45 46 54  chr$ left$
.:A190 A4 52 49 47 48 54 A4 4D  right$ mid$
.:A198 49 44 A4 47 CF           go
.:A19D 00                       END OF TOKEN NAME TABLE

                                *** ERROR MESSAGES
.:A19E 54 4F                    1 too many files
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

.:A328 9E A1 AC A1 B5 A1 C2 A1
.:A330 D0 A1 E2 A1 F0 A1 FF A1
.:A338 10 A2 25 A2 35 A2 3B A2
.:A340 4F A2 5A A2 6A A2 72 A2
.:A348 7F A2 90 A2 9D A2 AA A2
.:A350 BA A2 C8 A2 D5 A2 E4 A2
.:A358 ED A2 00 A3 0E A3 1E A3
.:A360 24 A3 83 A3

.:A364 0D 4F 4B 0D              OK
.:A368 00 20 20 45 52 52 4F 52  ERROR
.:A370 00 20 49 4E 20 00 0D 0A  IN
.:A378 52 45 41 44 59 2E 0D 0A  READY.
.:A380 00 0D 0A 42 52 45 41 4B  BREAK
.:A388 00

.:A389 A0
                                *** CALLED BY "NEXT" AND "FOR" TO SCAN THROUGH
                                *** THE STACK FOR A FRAME WITH THE SAME VARIABLE.
                                (FORPNT) = ADDRESS OF VARIABLE IF "FOR" OR "NEXT"
                                         = $XXFF IF CALLED FROM "RETURN"
                                           <<< BUG: SHOULD BE $FFXX >>>

                                RETURNS .NE. IF VARIABLE NOT FOUND,
                                        (X) = STACK PNTR AFTER SKIPPING ALL FRAMES

                                        .EQ. IF FOUND
                                        (X) = STACK PNTR OF FRAME FOUND
.,A38A BA       TSX             
.,A38B E8       INX             
.,A38C E8       INX             
.,A38D E8       INX             
.,A38E E8       INX             
.,A38F BD 01 01 LDA $0101,X     "FOR" FRAME HERE?
.,A392 C9 81    CMP #$81        
.,A394 D0 21    BNE $A3B7       NO
.,A396 A5 4A    LDA $4A         YES -- "NEXT" WITH NO VARIABLE?
.,A398 D0 0A    BNE $A3A4       NO, VARIABLE SPECIFIED
.,A39A BD 02 01 LDA $0102,X     YES, SO USE THIS FRAME
.,A39D 85 49    STA $49         
.,A39F BD 03 01 LDA $0103,X     
.,A3A2 85 4A    STA $4A         
.,A3A4 DD 03 01 CMP $0103,X     IS VARIABLE IN THIS FRAME?
.,A3A7 D0 07    BNE $A3B0       NO
.,A3A9 A5 49    LDA $49         LOOK AT 2ND BYTE TOO
.,A3AB DD 02 01 CMP $0102,X     SAME VARIABLE?
.,A3AE F0 07    BEQ $A3B7       YES
.,A3B0 8A       TXA             NO, SO TRY NEXT FRAME (IF ANY)
.,A3B1 18       CLC             18 BYTES PER FRAME
.,A3B2 69 12    ADC #$12        
.,A3B4 AA       TAX             
.,A3B5 D0 D8    BNE $A38F       ...ALWAYS?
.,A3B7 60       RTS             

                                *** MOVE BLOCK OF MEMORY UP
                                ON ENTRY:
                                    (Y,A) = (HIGHDS) = DESTINATION END+1
                                    (LOWTR) = LOWEST ADDRESS OF SOURCE
                                    (HIGHTR) = HIGHEST SOURCE ADDRESS+1
.,A3B8 20 08 A4 JSR $A408       BE SURE (Y,A) < FRETOP
.,A3BB 85 31    STA $31         NEW TOP OF ARRAY STORAGE
.,A3BD 84 32    STY $32         
.,A3BF 38       SEC             
.,A3C0 A5 5A    LDA $5A         COMPUTE # OF BYTES TO BE MOVED
.,A3C2 E5 5F    SBC $5F         (FROM LOWTR THRU HIGHTR-1)
.,A3C4 85 22    STA $22         PARTIAL PAGE AMOUNT
.,A3C6 A8       TAY             
.,A3C7 A5 5B    LDA $5B         
.,A3C9 E5 60    SBC $60         
.,A3CB AA       TAX             # OF WHOLE PAGES IN X-REG
.,A3CC E8       INX             
.,A3CD 98       TYA             # BYTES IN PARTIAL PAGE
.,A3CE F0 23    BEQ $A3F3       NO PARTIAL PAGE
.,A3D0 A5 5A    LDA $5A         BACK UP HIGHTR # BYTES IN PARTIAL PAGE
.,A3D2 38       SEC             
.,A3D3 E5 22    SBC $22         
.,A3D5 85 5A    STA $5A         
.,A3D7 B0 03    BCS $A3DC       
.,A3D9 C6 5B    DEC $5B         
.,A3DB 38       SEC             
.,A3DC A5 58    LDA $58         BACK UP HIGHDS # BYTES IN PARTIAL PAGE
.,A3DE E5 22    SBC $22         
.,A3E0 85 58    STA $58         
.,A3E2 B0 08    BCS $A3EC       
.,A3E4 C6 59    DEC $59         
.,A3E6 90 04    BCC $A3EC       ...ALWAYS
.,A3E8 B1 5A    LDA ($5A),Y     MOVE THE BYTES
.,A3EA 91 58    STA ($58),Y     
.,A3EC 88       DEY             
.,A3ED D0 F9    BNE $A3E8       LOOP TO END OF THIS 256 BYTES
.,A3EF B1 5A    LDA ($5A),Y     MOVE ONE MORE BYTE
.,A3F1 91 58    STA ($58),Y     
.,A3F3 C6 5B    DEC $5B         DOWN TO NEXT BLOCK OF 256
.,A3F5 C6 59    DEC $59         
.,A3F7 CA       DEX             ANOTHER BLOCK OF 256 TO MOVE?
.,A3F8 D0 F2    BNE $A3EC       YES
.,A3FA 60       RTS             NO, FINISHED

                                *** CHECK IF ENOUGH ROOM LEFT ON STACK
                                *** FOR "FOR", "GOSUB", OR EXPRESSION EVALUATION
.,A3FB 0A       ASL             
.,A3FC 69 3E    ADC #$3E        
.,A3FE B0 35    BCS $A435       ...MEM FULL ERR
.,A400 85 22    STA $22         
.,A402 BA       TSX             
.,A403 E4 22    CPX $22         
.,A405 90 2E    BCC $A435       ...MEM FULL ERR
.,A407 60       RTS             

                                *** CHECK IF ENOUGH ROOM BETWEEN ARRAYS AND STRINGS
                                (Y,A) = ADDR ARRAYS NEED TO GROW TO
.,A408 C4 34    CPY $34         HIGH BYTE
.,A40A 90 28    BCC $A434       PLENTY OF ROOM
.,A40C D0 04    BNE $A412       NOT ENOUGH, TRY GARBAGE COLLECTION
.,A40E C5 33    CMP $33         LOW BYTE
.,A410 90 22    BCC $A434       ENOUGH ROOM

.,A412 48       PHA             SAVE (Y,A), TEMP1, AND TEMP2
.,A413 A2 09    LDX #$09        
.,A415 98       TYA             
.,A416 48       PHA             
.,A417 B5 57    LDA $57,X       
.,A419 CA       DEX             
.,A41A 10 FA    BPL $A416       
.,A41C 20 26 B5 JSR $B526       MAKE AS MUCH ROOM AS POSSIBLE
.,A41F A2 F7    LDX #$F7        RESTORE TEMP1 AND TEMP2
.,A421 68       PLA             AND (Y,A)
.,A422 95 61    STA $61,X       
.,A424 E8       INX             
.,A425 30 FA    BMI $A421       
.,A427 68       PLA             
.,A428 A8       TAY             
.,A429 68       PLA             DID WE FIND ENOUGH ROOM?
.,A42A C4 34    CPY $34         HIGH BYTE
.,A42C 90 06    BCC $A434       YES, AT LEAST A PAGE
.,A42E D0 05    BNE $A435       NO, MEM FULL ERR
.,A430 C5 33    CMP $33         LOW BYTE
.,A432 B0 01    BCS $A435       NO, MEM FULL ERR
.,A434 60       RTS             YES, RETURN

.,A435 A2 10    LDX #$10        

                                *** HANDLE AN ERROR
                                (X)=OFFSET IN ERROR MESSAGE TABLE
                                (ERRFLG) > 128 IF "ON ERR" TURNED ON
                                (CURLIN+1) = $FF IF IN DIRECT MODE

                                *** WARM RESTART ENTRY
                                COME HERE FROM MONITOR BY CTL-C, 0G, 3D0G, OR E003G
.,A437 6C 00 03 JMP ($0300)     
.,A43A 8A       TXA             
.,A43B 0A       ASL             
.,A43C AA       TAX             
.,A43D BD 26 A3 LDA $A326,X     
.,A440 85 22    STA $22         
.,A442 BD 27 A3 LDA $A327,X     
.,A445 85 23    STA $23         
.,A447 20 CC FF JSR $FFCC       
.,A44A A9 00    LDA #$00        
.,A44C 85 13    STA $13         
.,A44E 20 D7 AA JSR $AAD7       
.,A451 20 45 AB JSR $AB45       
.,A454 A0 00    LDY #$00        
.,A456 B1 22    LDA ($22),Y     
.,A458 48       PHA             
.,A459 29 7F    AND #$7F        
.,A45B 20 47 AB JSR $AB47       
.,A45E C8       INY             
.,A45F 68       PLA             
.,A460 10 F4    BPL $A456       
.,A462 20 7A A6 JSR $A67A       
.,A465 A9 69    LDA #$69        
.,A467 A0 A3    LDY #$A3        
.,A469 20 1E AB JSR $AB1E       
.,A46C A4 3A    LDY $3A         
.,A46E C8       INY             
.,A46F F0 03    BEQ $A474       
.,A471 20 C2 BD JSR $BDC2       
.,A474 A9 76    LDA #$76        
.,A476 A0 A3    LDY #$A3        
.,A478 20 1E AB JSR $AB1E       
.,A47B A9 80    LDA #$80        
.,A47D 20 90 FF JSR $FF90       
.,A480 6C 02 03 JMP ($0302)     
.,A483 20 60 A5 JSR $A560       READ A LINE
.,A486 86 7A    STX $7A         SET UP CHRGET TO SCAN THE LINE
.,A488 84 7B    STY $7B         
.,A48A 20 73 00 JSR $0073       
.,A48D AA       TAX             
.,A48E F0 F0    BEQ $A480       EMPTY LINE
.,A490 A2 FF    LDX #$FF        $FF IN HI-BYTE OF CURLIN MEANS
.,A492 86 3A    STX $3A         WE ARE IN DIRECT MODE
.,A494 90 06    BCC $A49C       CHRGET SAW DIGIT, NUMBERED LINE
.,A496 20 79 A5 JSR $A579       NO NUMBER, SO PARSE IT
.,A499 4C E1 A7 JMP $A7E1       AND TRY EXECUTING IT

                                *** HANDLE NUMBERED LINE
.,A49C 20 6B A9 JSR $A96B       
.,A49F 20 79 A5 JSR $A579       
.,A4A2 84 0B    STY $0B         SAVE INDEX TO INPUT BUFFER
.,A4A4 20 13 A6 JSR $A613       IS THIS LINE # ALREADY IN PROGRAM?
.,A4A7 90 44    BCC $A4ED       NO
.,A4A9 A0 01    LDY #$01        YES, SO DELETE IT
.,A4AB B1 5F    LDA ($5F),Y     LOWTR POINTS AT LINE
.,A4AD 85 23    STA $23         GET HIGH BYTE OF FORWARD PNTR
.,A4AF A5 2D    LDA $2D         
.,A4B1 85 22    STA $22         
.,A4B3 A5 60    LDA $60         
.,A4B5 85 25    STA $25         
.,A4B7 A5 5F    LDA $5F         
.,A4B9 88       DEY             
.,A4BA F1 5F    SBC ($5F),Y     
.,A4BC 18       CLC             
.,A4BD 65 2D    ADC $2D         
.,A4BF 85 2D    STA $2D         
.,A4C1 85 24    STA $24         
.,A4C3 A5 2E    LDA $2E         
.,A4C5 69 FF    ADC #$FF        
.,A4C7 85 2E    STA $2E         
.,A4C9 E5 60    SBC $60         
.,A4CB AA       TAX             
.,A4CC 38       SEC             
.,A4CD A5 5F    LDA $5F         
.,A4CF E5 2D    SBC $2D         
.,A4D1 A8       TAY             
.,A4D2 B0 03    BCS $A4D7       
.,A4D4 E8       INX             
.,A4D5 C6 25    DEC $25         
.,A4D7 18       CLC             
.,A4D8 65 22    ADC $22         
.,A4DA 90 03    BCC $A4DF       
.,A4DC C6 23    DEC $23         
.,A4DE 18       CLC             

.,A4DF B1 22    LDA ($22),Y     MOVE HIGHER LINES OF PROGRAM
.,A4E1 91 24    STA ($24),Y     DOWN OVER THE DELETED LINE.
.,A4E3 C8       INY             
.,A4E4 D0 F9    BNE $A4DF       
.,A4E6 E6 23    INC $23         
.,A4E8 E6 25    INC $25         
.,A4EA CA       DEX             
.,A4EB D0 F2    BNE $A4DF       

.,A4ED 20 59 A6 JSR $A659       
.,A4F0 20 33 A5 JSR $A533       
.,A4F3 AD 00 02 LDA $0200       ANY CHARACTERS AFTER LINE #?
.,A4F6 F0 88    BEQ $A480       NO, SO NOTHING TO INSERT.
.,A4F8 18       CLC             
.,A4F9 A5 2D    LDA $2D         SET UP BLTU SUBROUTINE
.,A4FB 85 5A    STA $5A         INSERT NEW LINE.
.,A4FD 65 0B    ADC $0B         
.,A4FF 85 58    STA $58         
.,A501 A4 2E    LDY $2E         
.,A503 84 5B    STY $5B         
.,A505 90 01    BCC $A508       
.,A507 C8       INY             
.,A508 84 59    STY $59         
.,A50A 20 B8 A3 JSR $A3B8       MAKE ROOM FOR THE LINE
.,A50D A5 14    LDA $14         PUT LINE NUMBER IN LINE IMAGE
.,A50F A4 15    LDY $15         
.,A511 8D FE 01 STA $01FE       
.,A514 8C FF 01 STY $01FF       
.,A517 A5 31    LDA $31         
.,A519 A4 32    LDY $32         
.,A51B 85 2D    STA $2D         
.,A51D 84 2E    STY $2E         
.,A51F A4 0B    LDY $0B         
.,A521 88       DEY
                                
                                COPY LINE INTO PROGRAM
.,A522 B9 FC 01 LDA $01FC,Y     
.,A525 91 5F    STA ($5F),Y     
.,A527 88       DEY
.,A528 10 F8    BPL $A522

                                *** CLEAR ALL VARIABLES
                                RE-ESTABLISH ALL FORWARD LINKS
.,A52A 20 59 A6 JSR $A659       CLEAR ALL VARIABLES
.,A52D 20 33 A5 JSR $A533
.,A530 4C 80 A4 JMP $A480
.,A533 A5 2B    LDA $2B         POINT INDEX AT START OF PROGRAM
.,A535 A4 2C    LDY $2C         
.,A537 85 22    STA $22         
.,A539 84 23    STY $23         
.,A53B 18       CLC             
.,A53C A0 01    LDY #$01        HI-BYTE OF NEXT FORWARD PNTR
.,A53E B1 22    LDA ($22),Y     END OF PROGRAM YET?
.,A540 F0 1D    BEQ $A55F
.,A542 A0 04    LDY #$04        FIND END OF THIS LINE
.,A544 C8       INY             (NOTE MAXIMUM LENGTH < 256)
.,A545 B1 22    LDA ($22),Y     
.,A547 D0 FB    BNE $A544       
.,A549 C8       INY             COMPUTE ADDRESS OF NEXT LINE
.,A54A 98       TYA             
.,A54B 65 22    ADC $22         
.,A54D AA       TAX             
.,A54E A0 00    LDY #$00        STORE FORWARD PNTR IN THIS LINE
.,A550 91 22    STA ($22),Y     
.,A552 A5 23    LDA $23         
.,A554 69 00    ADC #$00        (NOTE: THIS CLEARS CARRY)
.,A556 C8       INY             
.,A557 91 22    STA ($22),Y     
.,A559 86 22    STX $22         
.,A55B 85 23    STA $23         
.,A55D 90 DD    BCC $A53C       ...ALWAYS
.,A55F 60       RTS

.,A560 A2 00    LDX #$00
.,A562 20 12 E1 JSR $E112
.,A565 C9 0D    CMP #$0D
.,A567 F0 0D    BEQ $A576
.,A569 9D 00 02 STA $0200,X
.,A56C E8       INX
.,A56D E0 59    CPX #$59
.,A56F 90 F1    BCC $A562
.,A571 A2 17    LDX #$17
.,A573 4C 37 A4 JMP $A437
.,A576 4C CA AA JMP $AACA
.,A579 6C 04 03 JMP ($0304)

                                *** TOKENIZE THE INPUT LINE
.,A57C A6 7A    LDX $7A         INDEX INTO UNPARSED LINE
.,A57E A0 04    LDY #$04        INDEX TO PARSED OUTPUT LINE
.,A580 84 0F    STY $0F         CLEAR SIGN-BIT OF DATAFLG
.,A582 BD 00 02 LDA $0200,X     
.,A585 10 07    BPL $A58E
.,A587 C9 FF    CMP #$FF
.,A589 F0 3E    BEQ $A5C9
.,A58B E8       INX
.,A58C D0 F4    BNE $A582
.,A58E C9 20    CMP #$20        IGNORE BLANKS
.,A590 F0 37    BEQ $A5C9       
.,A592 85 08    STA $08         
.,A594 C9 22    CMP #$22        START OF QUOTATION?
.,A596 F0 56    BEQ $A5EE       
.,A598 24 0F    BIT $0F
.,A59A 70 2D    BVS $A5C9       BRANCH IF IN "DATA" STATEMENT
.,A59C C9 3F    CMP #$3F        SHORTHAND FOR "PRINT"?
.,A59E D0 04    BNE $A5A4       NO
.,A5A0 A9 99    LDA #$99        YES, REPLACE WITH "PRINT" TOKEN
.,A5A2 D0 25    BNE $A5C9       ...ALWAYS
.,A5A4 C9 30    CMP #$30        IS IT A DIGIT, COLON, OR SEMI-COLON?
.,A5A6 90 04    BCC $A5AC       NO, PUNCTUATION !"#$%&amp;'()*+,-./
.,A5A8 C9 3C    CMP #$3C        
.,A5AA 90 1D    BCC $A5C9       YES, NOT A TOKEN

                                *** SEARCH TOKEN NAME TABLE FOR MATCH STARTING
                                *** WITH CURRENT CHAR FROM INPUT LINE
.,A5AC 84 71    STY $71         SAVE INDEX TO OUTPUT LINE
.,A5AE A0 00    LDY #$00        USE Y-REG WITH (FAC) TO ADDRESS TABLE
.,A5B0 84 0B    STY $0B         HOLDS CURRENT TOKEN-$80
.,A5B2 88       DEY             PREPARE FOR "INY" A FEW LINES DOWN
.,A5B3 86 7A    STX $7A         SAVE POSITION IN INPUT LINE
.,A5B5 CA       DEX             PREPARE FOR "INX" A FEW LINES DOWN
.,A5B6 C8       INY             ADVANCE POINTER TO TOKEN TABLE
.,A5B7 E8       INX
.,A5B8 BD 00 02 LDA $0200,X     NEXT CHAR FROM INPUT LINE
.,A5BB 38       SEC             NO, COMPARE TO CHAR IN TABLE
.,A5BC F9 9E A0 SBC $A09E,Y     SAME AS NEXT CHAR OF TOKEN NAME?
.,A5BF F0 F5    BEQ $A5B6       YES, CONTINUE MATCHING
.,A5C1 C9 80    CMP #$80        MAYBE; WAS IT SAME EXCEPT FOR BIT 7?
.,A5C3 D0 30    BNE $A5F5       NO, SKIP TO NEXT TOKEN
.,A5C5 05 0B    ORA $0B         YES, END OF TOKEN; GET TOKEN #
.,A5C7 A4 71    LDY $71         GET INDEX TO OUTPUT LINE IN Y-REG
.,A5C9 E8       INX             ADVANCE INPUT INDEX
.,A5CA C8       INY             ADVANCE OUTPUT INDEX
.,A5CB 99 FB 01 STA $01FB,Y     STORE CHAR OR TOKEN
.,A5CE B9 FB 01 LDA $01FB,Y     TEST FOR EOL OR EOS
.,A5D1 F0 36    BEQ $A609       END OF LINE
.,A5D3 38       SEC             
.,A5D4 E9 3A    SBC #$3A        END OF STATEMENT?
.,A5D6 F0 04    BEQ $A5DC       YES, CLEAR DATAFLG
.,A5D8 C9 49    CMP #$49        "DATA" TOKEN?
.,A5DA D0 02    BNE $A5DE       NO, LEAVE DATAFLG ALONE
.,A5DC 85 0F    STA $0F         DATAFLG = 0 OR $83-$3A = $49
.,A5DE 38       SEC             IS IT A "REM" TOKEN?
.,A5DF E9 55    SBC #$55        
.,A5E1 D0 9F    BNE $A582       NO, CONTINUE PARSING LINE
.,A5E3 85 08    STA $08         YES, CLEAR LITERAL FLAG

                                *** HANDLE LITERAL (BETWEEN QUOTES) OR REMARK,
                                *** BY COPYING CHARS UP TO ENDCHR.
.,A5E5 BD 00 02 LDA $0200,X     
.,A5E8 F0 DF    BEQ $A5C9       END OF LINE
.,A5EA C5 08    CMP $08         
.,A5EC F0 DB    BEQ $A5C9       FOUND ENDCHR
.,A5EE C8       INY             NEXT OUTPUT CHAR
.,A5EF 99 FB 01 STA $01FB,Y     
.,A5F2 E8       INX             NEXT INPUT CHAR
.,A5F3 D0 F0    BNE $A5E5       ...ALWAYS

                                *** ADVANCE POINTER TO NEXT TOKEN NAME
.,A5F5 A6 7A    LDX $7A         GET POINTER TO INPUT LINE IN X-REG
.,A5F7 E6 0B    INC $0B         BUMP (TOKEN # - $80)
.,A5F9 C8       INY             NEXT TOKEN ONE BEYOND THAT
.,A5FA B9 9D A0 LDA $A09D,Y     YES, AT NEXT NAME.  END OF TABLE?
.,A5FD 10 FA    BPL $A5F9
.,A5FF B9 9E A0 LDA $A09E,Y
.,A602 D0 B4    BNE $A5B8       NO, NOT END OF TABLE
.,A604 BD 00 02 LDA $0200,X     YES, SO NOT A KEYWORD
.,A607 10 BE    BPL $A5C7       ...ALWAYS, COPY CHAR AS IS
                                
                                END OF LINE
.,A609 99 FD 01 STA $01FD,Y     STORE ANOTHER 00 ON END
.,A60C C6 7B    DEC $7B         SET TXTPTR = INPUT.BUFFER-1
.,A60E A9 FF    LDA #$FF        
.,A610 85 7A    STA $7A         
.,A612 60       RTS             

                                *** SEARCH FOR LINE
                                (LINNUM) = LINE # TO FIND
                                IF NOT FOUND:  CARRY = 0
                                               LOWTR POINTS AT NEXT LINE
                                IF FOUND:      CARRY = 1
                                               LOWTR POINTS AT LINE
.,A613 A5 2B    LDA $2B         SEARCH FROM BEGINNING OF PROGRAM
.,A615 A6 2C    LDX $2C         
.,A617 A0 01    LDY #$01        SEARCH FROM (X,A)
.,A619 85 5F    STA $5F         
.,A61B 86 60    STX $60         
.,A61D B1 5F    LDA ($5F),Y     
.,A61F F0 1F    BEQ $A640       END OF PROGRAM, AND NOT FOUND
.,A621 C8       INY             
.,A622 C8       INY             
.,A623 A5 15    LDA $15         
.,A625 D1 5F    CMP ($5F),Y     
.,A627 90 18    BCC $A641       IF NOT FOUND
.,A629 F0 03    BEQ $A62E       
.,A62B 88       DEY             
.,A62C D0 09    BNE $A637       
.,A62E A5 14    LDA $14         
.,A630 88       DEY             
.,A631 D1 5F    CMP ($5F),Y     
.,A633 90 0C    BCC $A641       PAST LINE, NOT FOUND
.,A635 F0 0A    BEQ $A641       IF FOUND
.,A637 88       DEY             
.,A638 B1 5F    LDA ($5F),Y     
.,A63A AA       TAX             
.,A63B 88       DEY             
.,A63C B1 5F    LDA ($5F),Y     
.,A63E B0 D7    BCS $A617       ALWAYS
.,A640 18       CLC             RETURN CARRY = 0
.,A641 60       RTS             

                                *** "NEW" STATEMENT
.,A642 D0 FD    BNE $A641       IGNORE IF MORE TO THE STATEMENT
.,A644 A9 00    LDA #$00        
.,A646 A8       TAY             
.,A647 91 2B    STA ($2B),Y     
.,A649 C8       INY             
.,A64A 91 2B    STA ($2B),Y     
.,A64C A5 2B    LDA $2B         
.,A64E 18       CLC
.,A64F 69 02    ADC #$02
.,A651 85 2D    STA $2D
.,A653 A5 2C    LDA $2C         
.,A655 69 00    ADC #$00        
.,A657 85 2E    STA $2E         

.,A659 20 8E A6 JSR $A68E       SET TXTPTR TO TXTTAB - 1
.,A65C A9 00    LDA #$00        (THIS COULD HAVE BEEN ".HS 2C")

                                *** "CLEAR" STATEMENT
.,A65E D0 2D    BNE $A68D       IGNORE IF NOT AT END OF STATEMENT
.,A660 20 E7 FF JSR $FFE7
.,A663 A5 37    LDA $37         CLEAR STRING AREA
.,A665 A4 38    LDY $38         
.,A667 85 33    STA $33         
.,A669 84 34    STY $34         
.,A66B A5 2D    LDA $2D         CLEAR ARRAY AREA
.,A66D A4 2E    LDY $2E         
.,A66F 85 2F    STA $2F         
.,A671 84 30    STY $30         
.,A673 85 31    STA $31         LOW END OF FREE SPACE
.,A675 84 32    STY $32         
.,A677 20 1D A8 JSR $A81D       SET "DATA" POINTER TO BEGINNING

.,A67A A2 19    LDX #$19        
.,A67C 86 16    STX $16         
.,A67E 68       PLA             SAVE RETURN ADDRESS
.,A67F A8       TAY             
.,A680 68       PLA             
.,A681 A2 FA    LDX #$FA        START STACK AT $F8,
.,A683 9A       TXS             LEAVING ROOM FOR PARSING LINES
.,A684 48       PHA             RESTORE RETURN ADDRESS
.,A685 98       TYA             
.,A686 48       PHA             
.,A687 A9 00    LDA #$00        
.,A689 85 3E    STA $3E         
.,A68B 85 10    STA $10         
.,A68D 60       RTS             

                                *** SET TXTPTR TO BEGINNING OF PROGRAM
.,A68E 18       CLC             TXTPTR = TXTTAB - 1
.,A68F A5 2B    LDA $2B         
.,A691 69 FF    ADC #$FF        
.,A693 85 7A    STA $7A         
.,A695 A5 2C    LDA $2C         
.,A697 69 FF    ADC #$FF        
.,A699 85 7B    STA $7B         
.,A69B 60       RTS             

                                *** "LIST" STATEMENT
.,A69C 90 06    BCC $A6A4       NO  LINE # SPECIFIED
.,A69E F0 04    BEQ $A6A4       ---DITTO---
.,A6A0 C9 AB    CMP #$AB        IF DASH OR COMMA, START AT LINE 0
.,A6A2 D0 E9    BNE $A68D       NO, ERROR
.,A6A4 20 6B A9 JSR $A96B       CONVERT LINE NUMBER IF ANY
.,A6A7 20 13 A6 JSR $A613       POINT LOWTR TO 1ST LINE
.,A6AA 20 79 00 JSR $0079       RANGE SPECIFIED?
.,A6AD F0 0C    BEQ $A6BB       NO
.,A6AF C9 AB    CMP #$AB        
.,A6B1 D0 8E    BNE $A641       
.,A6B3 20 73 00 JSR $0073       GET NEXT CHAR
.,A6B6 20 6B A9 JSR $A96B       CONVERT SECOND LINE #
.,A6B9 D0 86    BNE $A641       BRANCH IF SYNTAX ERR
.,A6BB 68       PLA             POP RETURN ADRESS
.,A6BC 68       PLA             (GET BACK BY "JMP NEWSTT")
.,A6BD A5 14    LDA $14         IF NO SECOND NUMBER, USE $FFFF
.,A6BF 05 15    ORA $15         
.,A6C1 D0 06    BNE $A6C9       THERE WAS A SECOND NUMBER
.,A6C3 A9 FF    LDA #$FF        MAX END RANGE
.,A6C5 85 14    STA $14         
.,A6C7 85 15    STA $15         
.,A6C9 A0 01    LDY #$01        
.,A6CB 84 0F    STY $0F
.,A6CD B1 5F    LDA ($5F),Y     HIGH BYTE OF LINK
.,A6CF F0 43    BEQ $A714       END OF PROGRAM
.,A6D1 20 2C A8 JSR $A82C       CHECK IF CONTROL-C HAS BEEN TYPED
.,A6D4 20 D7 AA JSR $AAD7       NO, PRINT <RETURN>
.,A6D7 C8       INY             
.,A6D8 B1 5F    LDA ($5F),Y     GET LINE #, COMPARE WITH END RANGE
.,A6DA AA       TAX             
.,A6DB C8       INY             
.,A6DC B1 5F    LDA ($5F),Y     
.,A6DE C5 15    CMP $15         
.,A6E0 D0 04    BNE $A6E6       
.,A6E2 E4 14    CPX $14         
.,A6E4 F0 02    BEQ $A6E8       ON LAST LINE OF RANGE
.,A6E6 B0 2C    BCS $A714       FINISHED THE RANGE
                                
                                LIST ONE LINE
.,A6E8 84 49    STY $49         
.,A6EA 20 CD BD JSR $BDCD       PRINT LINE # FROM X,A
.,A6ED A9 20    LDA #$20        PRINT SPACE AFTER LINE #
.,A6EF A4 49    LDY $49         
.,A6F1 29 7F    AND #$7F        
.,A6F3 20 47 AB JSR $AB47       
.,A6F6 C9 22    CMP #$22
.,A6F8 D0 06    BNE $A700
.,A6FA A5 0F    LDA $0F
.,A6FC 49 FF    EOR #$FF
.,A6FE 85 0F    STA $0F
.,A700 C8       INY             
.,A701 F0 11    BEQ $A714
.,A703 B1 5F    LDA ($5F),Y     
.,A705 D0 10    BNE $A717       NOT END OF LINE YET
.,A707 A8       TAY             END OF LINE
.,A708 B1 5F    LDA ($5F),Y     GET LINK TO NEXT LINE
.,A70A AA       TAX             
.,A70B C8       INY             
.,A70C B1 5F    LDA ($5F),Y     
.,A70E 86 5F    STX $5F         POINT TO NEXT LINE
.,A710 85 60    STA $60         
.,A712 D0 B5    BNE $A6C9       BRANCH IF NOT END OF PROGRAM
.,A714 4C 86 E3 JMP $E386       TO NEXT STATEMENT

.,A717 6C 06 03 JMP ($0306)
.,A71A 10 D7    BPL $A6F3       BRANCH IF NOT A TOKEN
.,A71C C9 FF    CMP #$FF
.,A71E F0 D3    BEQ $A6F3
.,A720 24 0F    BIT $0F
.,A722 30 CF    BMI $A6F3
.,A724 38       SEC             
.,A725 E9 7F    SBC #$7F        CONVERT TOKEN TO INDEX
.,A727 AA       TAX             
.,A728 84 49    STY $49         SAVE LINE POINTER
.,A72A A0 FF    LDY #$FF        
.,A72C CA       DEX             SKIP KEYWORDS UNTIL REACH THIS ONE
.,A72D F0 08    BEQ $A737       
.,A72F C8       INY
.,A730 B9 9E A0 LDA $A09E,Y
.,A733 10 FA    BPL $A72F       NOT AT END OF KEYWORD YET
.,A735 30 F5    BMI $A72C       END OF KEYWORD, ALWAYS BRANCHES
.,A737 C8       INY
.,A738 B9 9E A0 LDA $A09E,Y
.,A73B 30 B2    BMI $A6EF       LAST CHAR OF KEYWORD
.,A73D 20 47 AB JSR $AB47       
.,A740 D0 F5    BNE $A737       ...ALWAYS

                                *** "FOR" STATEMENT
                                FOR PUSHES 18 BYTES ON THE STACK:
                                2 -- TXTPTR
                                2 -- LINE NUMBER
                                5 -- INITIAL (CURRENT)  FOR VARIABLE VALUE
                                1 -- STEP SIGN
                                5 -- STEP VALUE
                                2 -- ADDRESS OF FOR VARIABLE IN VARTAB
                                1 -- FOR TOKEN ($81)
.,A742 A9 80    LDA #$80        
.,A744 85 10    STA $10         SUBSCRIPTS NOT ALLOWED
.,A746 20 A5 A9 JSR $A9A5       DO <VAR> = <EXP>, STORE ADDR IN FORPNT
.,A749 20 8A A3 JSR $A38A       IS THIS FOR VARIABLE ACTIVE?
.,A74C D0 05    BNE $A753       NO
.,A74E 8A       TXA             YES, CANCEL IT AND ENCLOSED LOOPS
.,A74F 69 0F    ADC #$0F        CARRY=1, THIS ADDS 16
.,A751 AA       TAX             X WAS ALREADY S+2
.,A752 9A       TXS             
.,A753 68       PLA             POP RETURN ADDRESS TOO
.,A754 68       PLA             
.,A755 A9 09    LDA #$09        BE CERTAIN ENOUGH ROOM IN STACK
.,A757 20 FB A3 JSR $A3FB       
.,A75A 20 06 A9 JSR $A906       SCAN AHEAD TO NEXT STATEMENT
.,A75D 18       CLC             PUSH STATEMENT ADDRESS ON STACK
.,A75E 98       TYA             
.,A75F 65 7A    ADC $7A         
.,A761 48       PHA             
.,A762 A5 7B    LDA $7B         
.,A764 69 00    ADC #$00        
.,A766 48       PHA             
.,A767 A5 3A    LDA $3A         PUSH LINE NUMBER ON STACK
.,A769 48       PHA             
.,A76A A5 39    LDA $39         
.,A76C 48       PHA             
.,A76D A9 A4    LDA #$A4        
.,A76F 20 FF AE JSR $AEFF       REQUIRE "TO"
.,A772 20 8D AD JSR $AD8D       <VAR> = <EXP> MUST BE NUMERIC
.,A775 20 8A AD JSR $AD8A       GET FINAL VALUE, MUST BE NUMERIC
.,A778 A5 66    LDA $66         PUT SIGN INTO VALUE IN FAC
.,A77A 09 7F    ORA #$7F        
.,A77C 25 62    AND $62         
.,A77E 85 62    STA $62         
.,A780 A9 8B    LDA #$8B        SET UP FOR RETURN
.,A782 A0 A7    LDY #$A7        TO STEP
.,A784 85 22    STA $22         
.,A786 84 23    STY $23         
.,A788 4C 43 AE JMP $AE43       RETURNS BY "JMP (INDEX)"

                                *** "STEP" PHRASE OF "FOR" STATEMENT
.,A78B A9 BC    LDA #$BC        STEP DEFAULT=1
.,A78D A0 B9    LDY #$B9        
.,A78F 20 A2 BB JSR $BBA2       
.,A792 20 79 00 JSR $0079       
.,A795 C9 A9    CMP #$A9        
.,A797 D0 06    BNE $A79F       USE DEFAULT VALUE OF 1.0
.,A799 20 73 00 JSR $0073       STEP SPECIFIED, GET IT
.,A79C 20 8A AD JSR $AD8A       
.,A79F 20 2B BC JSR $BC2B       
.,A7A2 20 38 AE JSR $AE38       
.,A7A5 A5 4A    LDA $4A         
.,A7A7 48       PHA             
.,A7A8 A5 49    LDA $49         
.,A7AA 48       PHA             
.,A7AB A9 81    LDA #$81        
.,A7AD 48       PHA             

                                *** PERFORM NEXT STATEMENT
.,A7AE 20 2C A8 JSR $A82C       SEE IF CONTROL-C HAS BEEN TYPED
.,A7B1 A5 7A    LDA $7A         NO, KEEP EXECUTING
.,A7B3 A4 7B    LDY $7B         
.,A7B5 C0 02    CPY #$02
.,A7B7 EA       NOP
.,A7B8 F0 04    BEQ $A7BE       IN DIRECT MODE
.,A7BA 85 3D    STA $3D         IN RUNNING MODE
.,A7BC 84 3E    STY $3E         
.,A7BE A0 00    LDY #$00        
.,A7C0 B1 7A    LDA ($7A),Y     END OF LINE YET?
.,A7C2 D0 43    BNE $A807       NO
.,A7C4 A0 02    LDY #$02        YES, SEE IF END OF PROGRAM
.,A7C6 B1 7A    LDA ($7A),Y     
.,A7C8 18       CLC             
.,A7C9 D0 03    BNE $A7CE
.,A7CB 4C 4B A8 JMP $A84B       YES, END OF PROGRAM
.,A7CE C8       INY             
.,A7CF B1 7A    LDA ($7A),Y     GET LINE # OF NEXT LINE
.,A7D1 85 39    STA $39         
.,A7D3 C8       INY             
.,A7D4 B1 7A    LDA ($7A),Y     
.,A7D6 85 3A    STA $3A         
.,A7D8 98       TYA             ADJUST TXTPTR TO START
.,A7D9 65 7A    ADC $7A         OF NEW LINE
.,A7DB 85 7A    STA $7A         
.,A7DD 90 02    BCC $A7E1       
.,A7DF E6 7B    INC $7B         

.,A7E1 6C 08 03 JMP ($0308)
.,A7E4 20 73 00 JSR $0073       GET FIRST CHR OF STATEMENT
.,A7E7 20 ED A7 JSR $A7ED       AND START PROCESSING
.,A7EA 4C AE A7 JMP $A7AE       BACK FOR MORE

                                *** EXECUTE A STATEMENT
                                (A) IS FIRST CHAR OF STATEMENT
                                CARRY IS SET
.,A7ED F0 3C    BEQ $A82B       END OF LINE, NULL STATEMENT
.,A7EF E9 80    SBC #$80        FIRST CHAR A TOKEN?
.,A7F1 90 11    BCC $A804       NOT TOKEN, MUST BE "LET"
.,A7F3 C9 23    CMP #$23        STATEMENT-TYPE TOKEN?
.,A7F5 B0 17    BCS $A80E       NO, SYNTAX ERROR
.,A7F7 0A       ASL             DOUBLE TO GET INDEX
.,A7F8 A8       TAY             INTO ADDRESS TABLE
.,A7F9 B9 0D A0 LDA $A00D,Y     
.,A7FC 48       PHA             PUT ADDRESS ON STACK
.,A7FD B9 0C A0 LDA $A00C,Y     
.,A800 48       PHA             
.,A801 4C 73 00 JMP $0073       GET NEXT CHR &amp; RTS TO ROUTINE

.,A804 4C A5 A9 JMP $A9A5       MUST BE <VAR> = <EXP>

.,A807 C9 3A    CMP #$3A        
.,A809 F0 D6    BEQ $A7E1       
.,A80B 4C 08 AF JMP $AF08       

.,A80E C9 4B    CMP #$4B
.,A810 D0 F9    BNE $A80B
.,A812 20 73 00 JSR $0073
.,A815 A9 A4    LDA #$A4
.,A817 20 FF AE JSR $AEFF
.,A81A 4C A0 A8 JMP $A8A0

                                *** "RESTORE" STATEMENT
.,A81D 38       SEC             SET DATPTR TO BEGINNING OF PROGRAM
.,A81E A5 2B    LDA $2B         
.,A820 E9 01    SBC #$01        
.,A822 A4 2C    LDY $2C         
.,A824 B0 01    BCS $A827
.,A826 88       DEY             
                                
                                SET DATPTR TO Y,A
.,A827 85 41    STA $41         
.,A829 84 42    STY $42         
.,A82B 60       RTS             

                                *** SEE IF CONTROL-C TYPED
.,A82C 20 E1 FF JSR $FFE1

                                *** "STOP" STATEMENT
.,A82F B0 01    BCS $A832       CARRY=1 TO FORCE PRINTING "BREAK AT.."

                                *** "END" STATEMENT
.,A831 18       CLC             CARRY=0 TO AVOID PRINTING MESSAGE
.,A832 D0 3C    BNE $A870       IF NOT END OF STATEMENT, DO NOTHING
.,A834 A5 7A    LDA $7A         
.,A836 A4 7B    LDY $7B         
.,A838 A6 3A    LDX $3A         
.,A83A E8       INX             RUNNING?
.,A83B F0 0C    BEQ $A849       NO, DIRECT MODE
.,A83D 85 3D    STA $3D         
.,A83F 84 3E    STY $3E         
.,A841 A5 39    LDA $39         
.,A843 A4 3A    LDY $3A         
.,A845 85 3B    STA $3B         
.,A847 84 3C    STY $3C         
.,A849 68       PLA             
.,A84A 68       PLA             
.,A84B A9 81    LDA #$81        " BREAK" AND BELL
.,A84D A0 A3    LDY #$A3        
.,A84F 90 03    BCC $A854       
.,A851 4C 69 A4 JMP $A469       
.,A854 4C 86 E3 JMP $E386       

                                *** "CONT" COMMAND
.,A857 D0 17    BNE $A870       IF NOT END OF STATEMENT, DO NOTHING
.,A859 A2 1A    LDX #$1A        
.,A85B A4 3E    LDY $3E         MEANINGFUL RE-ENTRY?
.,A85D D0 03    BNE $A862       YES
.,A85F 4C 37 A4 JMP $A437       NO
.,A862 A5 3D    LDA $3D         RESTORE TXTPTR
.,A864 85 7A    STA $7A         
.,A866 84 7B    STY $7B         
.,A868 A5 3B    LDA $3B         RESTORE LINE NUMBER
.,A86A A4 3C    LDY $3C         
.,A86C 85 39    STA $39         
.,A86E 84 3A    STY $3A         
.,A870 60       RTS             

                                *** "RUN" COMMAND
.,A871 08       PHP             SAVE STATUS WHILE SUBTRACTING
.,A872 A9 00    LDA #$00
.,A874 20 90 FF JSR $FF90
.,A877 28       PLP             GET STATUS AGAIN (FROM CHRGET)
.,A878 D0 03    BNE $A87D       PROBABLY A LINE NUMBER
.,A87A 4C 59 A6 JMP $A659       START AT BEGINNING OF PROGRAM
.,A87D 20 60 A6 JSR $A660       CLEAR VARIABLES
.,A880 4C 97 A8 JMP $A897       JOIN GOSUB STATEMENT

                                *** "GOSUB" STATEMENT
                                LEAVES 7 BYTES ON STACK:
                                2 -- RETURN ADDRESS (NEWSTT)
                                2 -- TXTPTR
                                2 -- LINE #
                                1 -- GOSUB TOKEN ($B0)
.,A883 A9 03    LDA #$03        BE SURE ENOUGH ROOM ON STACK
.,A885 20 FB A3 JSR $A3FB       
.,A888 A5 7B    LDA $7B         
.,A88A 48       PHA             
.,A88B A5 7A    LDA $7A         
.,A88D 48       PHA             
.,A88E A5 3A    LDA $3A         
.,A890 48       PHA             
.,A891 A5 39    LDA $39         
.,A893 48       PHA             
.,A894 A9 8D    LDA #$8D        
.,A896 48       PHA             
.,A897 20 79 00 JSR $0079       
.,A89A 20 A0 A8 JSR $A8A0       
.,A89D 4C AE A7 JMP $A7AE       

                                *** "GOTO" STATEMENT
                                ALSO USED BY "RUN" AND "GOSUB"
.,A8A0 20 6B A9 JSR $A96B       GET GOTO LINE
.,A8A3 20 09 A9 JSR $A909       POINT Y TO EOL
.,A8A6 38       SEC
.,A8A7 A5 39    LDA $39
.,A8A9 E5 14    SBC $14
.,A8AB A5 3A    LDA $3A         IS CURRENT PAGE < GOTO PAGE?
.,A8AD E5 15    SBC $15         
.,A8AF B0 0B    BCS $A8BC       SEARCH FROM PROG START IF NOT
.,A8B1 98       TYA             OTHERWISE SEARCH FROM NEXT LINE
.,A8B2 38       SEC             
.,A8B3 65 7A    ADC $7A         
.,A8B5 A6 7B    LDX $7B         
.,A8B7 90 07    BCC $A8C0       
.,A8B9 E8       INX             
.,A8BA B0 04    BCS $A8C0       
.,A8BC A5 2B    LDA $2B         GET PROGRAM BEGINNING
.,A8BE A6 2C    LDX $2C
.,A8C0 20 17 A6 JSR $A617       SEARCH FOR GOTO LINE
.,A8C3 90 1E    BCC $A8E3       ERROR IF NOT THERE
.,A8C5 A5 5F    LDA $5F         TXTPTR = START OF THE DESTINATION LINE
.,A8C7 E9 01    SBC #$01        
.,A8C9 85 7A    STA $7A         
.,A8CB A5 60    LDA $60         
.,A8CD E9 00    SBC #$00        
.,A8CF 85 7B    STA $7B         
.,A8D1 60       RTS             RETURN TO NEWSTT OR GOSUB

                                *** "POP" AND "RETURN" STATEMENTS
.,A8D2 D0 FD    BNE $A8D1       
.,A8D4 A9 FF    LDA #$FF        
.,A8D6 85 4A    STA $4A
.,A8D8 20 8A A3 JSR $A38A       TO CANCEL FOR/NEXT IN SUB
.,A8DB 9A       TXS
.,A8DC C9 8D    CMP #$8D        LAST GOSUB FOUND?
.,A8DE F0 0B    BEQ $A8EB       
.,A8E0 A2 0C    LDX #$0C        
.:A8E2 2C       .BYTE $2C       FAKE
.,A8E3 A2 11    LDX #$02        
.,A8E5 4C 37 A4 JMP $A437       

.,A8E8 4C 08 AF JMP $AF08       

.,A8EB 68       PLA             DISCARD GOSUB TOKEN
.,A8EC 68       PLA             
.,A8ED 85 39    STA $39         PULL LINE #
.,A8EF 68       PLA             
.,A8F0 85 3A    STA $3A         
.,A8F2 68       PLA             
.,A8F3 85 7A    STA $7A         PULL TXTPTR
.,A8F5 68       PLA             
.,A8F6 85 7B    STA $7B         

                                *** "DATA" STATEMENT
                                EXECUTED BY SKIPPING TO NEXT COLON OR EOL
.,A8F8 20 06 A9 JSR $A906       MOVE TO NEXT STATEMENT

                                *** ADD (Y) TO TXTPTR
.,A8FB 98       TYA             
.,A8FC 18       CLC             
.,A8FD 65 7A    ADC $7A         
.,A8FF 85 7A    STA $7A         
.,A901 90 02    BCC $A905       
.,A903 E6 7B    INC $7B         
.,A905 60       RTS             

                                *** SCAN AHEAD TO NEXT ":" OR EOL
.,A906 A2 3A    LDX #$3A        GET OFFSET IN Y TO EOL OR ":"
.:A908 2C       .BYTE $2C       FAKE

.,A909 A2 00    LDX #$00        TO EOL ONLY
.,A90B 86 07    STX $07         
.,A90D A0 00    LDY #$00        
.,A90F 84 08    STY $08         
.,A911 A5 08    LDA $08         TRICK TO COUNT QUOTE PARITY
.,A913 A6 07    LDX $07         
.,A915 85 07    STA $07         
.,A917 86 08    STX $08         
.,A919 B1 7A    LDA ($7A),Y     
.,A91B F0 E8    BEQ $A905       END OF LINE
.,A91D C5 08    CMP $08         
.,A91F F0 E4    BEQ $A905       COLON IF LOOKING FOR COLONS
.,A921 C8       INY             
.,A922 C9 22    CMP #$22        
.,A924 D0 F3    BNE $A919       
.,A926 F0 E9    BEQ $A911       ...ALWAYS

                                *** "IF" STATEMENT
.,A928 20 9E AD JSR $AD9E       
.,A92B 20 79 00 JSR $0079       
.,A92E C9 89    CMP #$89        
.,A930 F0 05    BEQ $A937       
.,A932 A9 A7    LDA #$A7        
.,A934 20 FF AE JSR $AEFF       
.,A937 A5 61    LDA $61         CONDITION TRUE OR FALSE?
.,A939 D0 05    BNE $A940       BRANCH IF TRUE

                                *** "REM" STATEMENT, OR FALSE "IF" STATEMENT
.,A93B 20 09 A9 JSR $A909       SKIP REST OF LINE
.,A93E F0 BB    BEQ $A8FB       ...ALWAYS

.,A940 20 79 00 JSR $0079       COMMAND OR NUMBER?
.,A943 B0 03    BCS $A948       COMMAND
.,A945 4C A0 A8 JMP $A8A0       NUMBER
.,A948 4C ED A7 JMP $A7ED       

                                *** "ON" STATEMENT
                                ON <EXP> GOTO <LIST>
                                ON <EXP> GOSUB <LIST>
.,A94B 20 9E B7 JSR $B79E       EVALUATE <EXP>, AS BYTE IN FAC+4
.,A94E 48       PHA             SAVE NEXT CHAR ON STACK
.,A94F C9 8D    CMP #$8D        
.,A951 F0 04    BEQ $A957       
.,A953 C9 89    CMP #$89        
.,A955 D0 91    BNE $A8E8       
.,A957 C6 65    DEC $65         COUNTED TO RIGHT ONE YET?
.,A959 D0 04    BNE $A95F       NO, KEEP LOOKING
.,A95B 68       PLA             YES, RETRIEVE CMD
.,A95C 4C EF A7 JMP $A7EF       AND GO.
.,A95F 20 73 00 JSR $0073       PRIME CONVERT SUBROUTINE
.,A962 20 6B A9 JSR $A96B       CONVERT LINE #
.,A965 C9 2C    CMP #$2C        TERMINATE WITH COMMA?
.,A967 F0 EE    BEQ $A957       YES
.,A969 68       PLA             NO, END OF LIST, SO IGNORE
.,A96A 60       RTS             

                                *** CONVERT LINE NUMBER
.,A96B A2 00    LDX #$00        ASC # TO HEX ADDRESS
.,A96D 86 14    STX $14         IN LINNUM.
.,A96F 86 15    STX $15         
.,A971 B0 F7    BCS $A96A       NOT A DIGIT
.,A973 E9 2F    SBC #$2F        CONVERT DIGIT TO BINARY
.,A975 85 07    STA $07         SAVE THE DIGIT
.,A977 A5 15    LDA $15         CHECK RANGE
.,A979 85 22    STA $22         
.,A97B C9 19    CMP #$19        LINE # TOO LARGE?
.,A97D B0 D4    BCS $A953       YES, > 63999, GO INDIRECTLY TO
                                "SYNTAX ERROR".
                                <<<<<DANGEROUS CODE>>>>>
                                NOTE THAT IF (A) = $AB ON THE LINE ABOVE,
                                ON.1 WILL COMPARE = AND CAUSE A CATASTROPHIC
                                JUMP TO $22D9 (FOR GOTO), OR OTHER LOCATIONS
                                FOR OTHER CALLS TO LINGET.

                                YOU CAN SEE THIS IS YOU FIRST PUT "BRK" IN $22D9,
                                THEN TYPE "GO TO 437761".

                                ANY VALUE FROM 437760 THROUGH 440319 WILL CAUSE
                                THE PROBLEM.  ($AB00 - $ABFF)
                                <<<<<DANGEROUS CODE>>>>>
.,A97F A5 14    LDA $14         MULTIPLY BY TEN
.,A981 0A       ASL             
.,A982 26 22    ROL $22         
.,A984 0A       ASL             
.,A985 26 22    ROL $22         
.,A987 65 14    ADC $14         
.,A989 85 14    STA $14         
.,A98B A5 22    LDA $22         
.,A98D 65 15    ADC $15         
.,A98F 85 15    STA $15         
.,A991 06 14    ASL $14         
.,A993 26 15    ROL $15         
.,A995 A5 14    LDA $14         
.,A997 65 07    ADC $07         ADD DIGIT
.,A999 85 14    STA $14         
.,A99B 90 02    BCC $A99F       
.,A99D E6 15    INC $15         
.,A99F 20 73 00 JSR $0073       GET NEXT CHAR
.,A9A2 4C 71 A9 JMP $A971       MORE CONVERTING

                                *** "LET" STATEMENT
                                LET <VAR> = <EXP>
                                <VAR> = <EXP>
.,A9A5 20 8B B0 JSR $B08B       GET <VAR>
.,A9A8 85 49    STA $49         
.,A9AA 84 4A    STY $4A         
.,A9AC A9 B2    LDA #$B2        
.,A9AE 20 FF AE JSR $AEFF       
.,A9B1 A5 0E    LDA $0E         SAVE VARIABLE TYPE
.,A9B3 48       PHA             
.,A9B4 A5 0D    LDA $0D         
.,A9B6 48       PHA             
.,A9B7 20 9E AD JSR $AD9E       EVALUATE <EXP>
.,A9BA 68       PLA             
.,A9BB 2A       ROL             
.,A9BC 20 90 AD JSR $AD90       
.,A9BF D0 18    BNE $A9D9       
.,A9C1 68       PLA             

.,A9C2 10 12    BPL $A9D6       REAL VARIABLE
.,A9C4 20 1B BC JSR $BC1B       INTEGER VAR: ROUND TO 32 BITS
.,A9C7 20 BF B1 JSR $B1BF       TRUNCATE TO 16-BITS
.,A9CA A0 00    LDY #$00        
.,A9CC A5 64    LDA $64         
.,A9CE 91 49    STA ($49),Y     
.,A9D0 C8       INY             
.,A9D1 A5 65    LDA $65         
.,A9D3 91 49    STA ($49),Y     
.,A9D5 60       RTS             

                                *** REAL VARIABLE = EXPRESSION
.,A9D6 4C D0 BB JMP $BBD0       

.,A9D9 68       PLA             

                                *** INSTALL STRING, DESCRIPTOR ADDRESS IS AT FAC+3,4
.,A9DA A4 4A    LDY $4A         STRING DATA ALREADY IN STRING AREA?
.,A9DC C0 BF    CPY #$BF
.,A9DE D0 4C    BNE $AA2C
.,A9E0 20 A6 B6 JSR $B6A6
.,A9E3 C9 06    CMP #$06
.,A9E5 D0 3D    BNE $AA24
.,A9E7 A0 00    LDY #$00
.,A9E9 84 61    STY $61
.,A9EB 84 66    STY $66
.,A9ED 84 71    STY $71
.,A9EF 20 1D AA JSR $AA1D
.,A9F2 20 E2 BA JSR $BAE2
.,A9F5 E6 71    INC $71
.,A9F7 A4 71    LDY $71
.,A9F9 20 1D AA JSR $AA1D
.,A9FC 20 0C BC JSR $BC0C
.,A9FF AA       TAX
.,AA00 F0 05    BEQ $AA07
.,AA02 E8       INX
.,AA03 8A       TXA
.,AA04 20 ED BA JSR $BAED
.,AA07 A4 71    LDY $71
.,AA09 C8       INY
.,AA0A C0 06    CPY #$06
.,AA0C D0 DF    BNE $A9ED
.,AA0E 20 E2 BA JSR $BAE2
.,AA11 20 9B BC JSR $BC9B
.,AA14 A6 64    LDX $64
.,AA16 A4 63    LDY $63
.,AA18 A5 65    LDA $65
.,AA1A 4C DB FF JMP $FFDB
.,AA1D B1 22    LDA ($22),Y
.,AA1F 20 80 00 JSR $0080
.,AA22 90 03    BCC $AA27
.,AA24 4C 48 B2 JMP $B248
.,AA27 E9 2F    SBC #$2F
.,AA29 4C 7E BD JMP $BD7E
.,AA2C A0 02    LDY #$02
.,AA2E B1 64    LDA ($64),Y     (STRING AREA IS BTWN FRETOP
.,AA30 C5 34    CMP $34         HIMEM)
.,AA32 90 17    BCC $AA4B       YES, DATA ALREADY UP THERE
.,AA34 D0 07    BNE $AA3D       NO
.,AA36 88       DEY             MAYBE, TEST LOW BYTE OF POINTER
.,AA37 B1 64    LDA ($64),Y     
.,AA39 C5 33    CMP $33         
.,AA3B 90 0E    BCC $AA4B       YES, ALREADY THERE
.,AA3D A4 65    LDY $65         NO. DESCRIPTOR ALREADY AMONG VARIABLES?
.,AA3F C4 2E    CPY $2E         
.,AA41 90 08    BCC $AA4B       NO
.,AA43 D0 0D    BNE $AA52       YES
.,AA45 A5 64    LDA $64         MAYBE, COMPARE LO-BYTE
.,AA47 C5 2D    CMP $2D         
.,AA49 B0 07    BCS $AA52       YES, DESCRIPTOR IS AMONG VARIABLES
.,AA4B A5 64    LDA $64         EITHER STRING ALREADY ON TOP, OR
.,AA4D A4 65    LDY $65         DESCRIPTOR IS NOT A VARIABLE
.,AA4F 4C 68 AA JMP $AA68       SO JUST STORE THE DESCRIPTOR

                                *** STRING NOT YET IN STRING AREA,
                                *** AND DESCRIPTOR IS A VARIABLE
.,AA52 A0 00    LDY #$00        POINT AT LENGTH IN DESCRIPTOR
.,AA54 B1 64    LDA ($64),Y     GET LENGTH
.,AA56 20 75 B4 JSR $B475       MAKE A STRING THAT LONG UP ABOVE
.,AA59 A5 50    LDA $50         SET UP SOURCE PNTR FOR MONINS
.,AA5B A4 51    LDY $51         
.,AA5D 85 6F    STA $6F         
.,AA5F 84 70    STY $70         
.,AA61 20 7A B6 JSR $B67A       MOVE STRING DATA TO NEW AREA
.,AA64 A9 61    LDA #$61        ADDRESS OF DESCRIPTOR IS IN FAC
.,AA66 A0 00    LDY #$00        
.,AA68 85 50    STA $50         
.,AA6A 84 51    STY $51         
.,AA6C 20 DB B6 JSR $B6DB       DISCARD DESCRIPTOR IF 'TWAS TEMPORARY
.,AA6F A0 00    LDY #$00        COPY STRING DESCRIPTOR
.,AA71 B1 50    LDA ($50),Y     
.,AA73 91 49    STA ($49),Y     
.,AA75 C8       INY             
.,AA76 B1 50    LDA ($50),Y     
.,AA78 91 49    STA ($49),Y     
.,AA7A C8       INY             
.,AA7B B1 50    LDA ($50),Y     
.,AA7D 91 49    STA ($49),Y     
.,AA7F 60       RTS             

.,AA80 20 86 AA JSR $AA86
.,AA83 4C B5 AB JMP $ABB5
.,AA86 20 9E B7 JSR $B79E
.,AA89 F0 05    BEQ $AA90
.,AA8B A9 2C    LDA #$2C
.,AA8D 20 FF AE JSR $AEFF
.,AA90 08       PHP
.,AA91 86 13    STX $13
.,AA93 20 18 E1 JSR $E118
.,AA96 28       PLP
.,AA97 4C A0 AA JMP $AAA0
.,AA9A 20 21 AB JSR $AB21
.,AA9D 20 79 00 JSR $0079

                                *** "PRINT" STATEMENT
.,AAA0 F0 35    BEQ $AAD7       NO MORE LIST, PRINT <RETURN>

.,AAA2 F0 43    BEQ $AAE7       NO MORE LIST, DON'T PRINT <RETURN>
.,AAA4 C9 A3    CMP #$A3        
.,AAA6 F0 50    BEQ $AAF8       C=1 FOR TAB(
.,AAA8 C9 A6    CMP #$A6        
.,AAAA 18       CLC             
.,AAAB F0 4B    BEQ $AAF8       C=0 FOR SPC(
.,AAAD C9 2C    CMP #$2C        
.,AAAF F0 37    BEQ $AAE8       
.,AAB1 C9 3B    CMP #$3B        
.,AAB3 F0 5E    BEQ $AB13       
.,AAB5 20 9E AD JSR $AD9E       EVALUATE EXPRESSION
.,AAB8 24 0D    BIT $0D         STRING OR FP VALUE?
.,AABA 30 DE    BMI $AA9A       STRING
.,AABC 20 DD BD JSR $BDDD       FP: CONVERT INTO BUFFER
.,AABF 20 87 B4 JSR $B487       MAKE BUFFER INTO STRING
.,AAC2 20 21 AB JSR $AB21
.,AAC5 20 3B AB JSR $AB3B
.,AAC8 D0 D3    BNE $AA9D       PRINT THE STRING
.,AACA A9 00    LDA #$00
.,AACC 9D 00 02 STA $0200,X
.,AACF A2 FF    LDX #$FF
.,AAD1 A0 01    LDY #$01
.,AAD3 A5 13    LDA $13
.,AAD5 D0 10    BNE $AAE7

.,AAD7 A9 0D    LDA #$0D        PRINT <RETURN>
.,AAD9 20 47 AB JSR $AB47       
.,AADC 24 13    BIT $13
.,AADE 10 05    BPL $AAE5
.,AAE0 A9 0A    LDA #$0A
.,AAE2 20 47 AB JSR $AB47
.,AAE5 49 FF    EOR #$FF        <<< WHY??? >>>
.,AAE7 60       RTS             

.,AAE8 38       SEC
.,AAE9 20 F0 FF JSR $FFF0
.,AAEC 98       TYA
.,AAED 38       SEC
.,AAEE E9 0A    SBC #$0A
.,AAF0 B0 FC    BCS $AAEE
.,AAF2 49 FF    EOR #$FF
.,AAF4 69 01    ADC #$01
.,AAF6 D0 16    BNE $AB0E
.,AAF8 08       PHP             C=0 FOR SPC(, C=1 FOR TAB(
.,AAF9 38       SEC
.,AAFA 20 F0 FF JSR $FFF0
.,AAFD 84 09    STY $09
.,AAFF 20 9B B7 JSR $B79B       GET VALUE
.,AB02 C9 29    CMP #$29        TRAILING PARENTHESIS
.,AB04 D0 59    BNE $AB5F       NO, SYNTAX ERROR
.,AB06 28       PLP             TAB( OR SPC(
.,AB07 90 06    BCC $AB0F       SPC(
.,AB09 8A       TXA             CALCULATE SPACES NEEDED FOR TAB(
.,AB0A E5 09    SBC $09         
.,AB0C 90 05    BCC $AB13       ALREADY PAST THAT COLUMN
.,AB0E AA       TAX             NOW DO A SPC( TO THE SPECIFIED COLUMN
.,AB0F E8       INX             
.,AB10 CA       DEX             
.,AB11 D0 06    BNE $AB19       MORE SPACES TO PRINT

.,AB13 20 73 00 JSR $0073       
.,AB16 4C A2 AA JMP $AAA2       CONTINUE PARSING PRINT LIST

.,AB19 20 3B AB JSR $AB3B       
.,AB1C D0 F2    BNE $AB10       ...ALWAYS

                                *** PRINT STRING AT (Y,A)
.,AB1E 20 87 B4 JSR $B487       MAKE (Y,A) PRINTABLE

                                *** PRINT STRING AT (FACMO,FACLO)
.,AB21 20 A6 B6 JSR $B6A6       GET ADDRESS INTO INDEX, (A)=LENGTH
.,AB24 AA       TAX             USE X-REG FOR COUNTER
.,AB25 A0 00    LDY #$00        USE Y-REG FOR SCANNER
.,AB27 E8       INX             
.,AB28 CA       DEX             
.,AB29 F0 BC    BEQ $AAE7       FINISHED
.,AB2B B1 22    LDA ($22),Y     NEXT CHAR FROM STRING
.,AB2D 20 47 AB JSR $AB47       PRINT THE CHAR
.,AB30 C8       INY             
                                <<< NEXT THREE LINES ARE USELESS >>>
.,AB31 C9 0D    CMP #$0D        WAS IT <RETURN>?
.,AB33 D0 F3    BNE $AB28       NO
.,AB35 20 E5 AA JSR $AAE5       EOR #$FF WOULD DO IT, BUT WHY?
                                <<< ABOVE THREE LINES ARE USELESS >>>
.,AB38 4C 28 AB JMP $AB28       

.,AB3B A5 13    LDA $13
.,AB3D F0 03    BEQ $AB42
.,AB3F A9 20    LDA #$20        PRINT A SPACE
.:AB41 2C       .BYTE $2C       SKIP OVER NEXT LINE
.,AB42 A9 1D    LDA #$1D
.:AB44 2C       .BYTE $2C       SKIP OVER NEXT LINE
.,AB45 A9 3F    LDA #$3F        PRINT QUESTION MARK
.,AB47 20 0C E1 JSR $E10C
.,AB4A 29 FF    AND #$FF

                                *** PRINT CHAR FROM (A)
                                NOTE: POKE 243,32 ($20 IN $F3) WILL CONVERT
                                OUTPUT TO LOWER CASE.  THIS CAN BE CANCELLED
                                BY NORMAL, INVERSE, OR FLASH OR POKE 243,0.
.,AB4C 60       RTS             

                                *** INPUT CONVERSION ERROR
                                ILLEGAL CHARACTER IN NUMERIC FIELD.
                                MUST DISTINGUISH BETWEEN INPUT, READ, AND GET
.,AB4D A5 11    LDA $11         
.,AB4F F0 11    BEQ $AB62       TAKEN IF INPUT
.,AB51 30 04    BMI $AB57       TAKEN IF READ
.,AB53 A0 FF    LDY #$FF        FROM A GET
.,AB55 D0 04    BNE $AB5B       ...ALWAYS

.,AB57 A5 3F    LDA $3F         TELL WHERE THE "DATA" IS, RATHER
.,AB59 A4 40    LDY $40         THAN THE "READ"
.,AB5B 85 39    STA $39
.,AB5D 84 3A    STY $3A
.,AB5F 4C 08 AF JMP $AF08
.,AB62 A5 13    LDA $13
.,AB64 F0 05    BEQ $AB6B

.,AB66 A2 18    LDX #$18        ERROR CODE = 254
.,AB68 4C 37 A4 JMP $A437       
.,AB6B A9 0C    LDA #$0C        "?REENTER"
.,AB6D A0 AD    LDY #$AD        
.,AB6F 20 1E AB JSR $AB1E       
.,AB72 A5 3D    LDA $3D         RE-EXECUTE THE WHOLE INPUT STATEMENT
.,AB74 A4 3E    LDY $3E         
.,AB76 85 7A    STA $7A         
.,AB78 84 7B    STY $7B         
.,AB7A 60       RTS             

                                *** "GET" STATEMENT
.,AB7B 20 A6 B3 JSR $B3A6       ILLEGAL IF IN DIRECT MODE
.,AB7E C9 23    CMP #$23
.,AB80 D0 10    BNE $AB92
.,AB82 20 73 00 JSR $0073
.,AB85 20 9E B7 JSR $B79E
.,AB88 A9 2C    LDA #$2C
.,AB8A 20 FF AE JSR $AEFF
.,AB8D 86 13    STX $13
.,AB8F 20 1E E1 JSR $E11E
.,AB92 A2 01    LDX #$01        SIMULATE INPUT
.,AB94 A0 02    LDY #$02        
.,AB96 A9 00    LDA #$00        
.,AB98 8D 01 02 STA $0201       
.,AB9B A9 40    LDA #$40        SET UP INPUTFLG
.,AB9D 20 0F AC JSR $AC0F
.,ABA0 A6 13    LDX $13
.,ABA2 D0 13    BNE $ABB7
.,ABA4 60       RTS

.,ABA5 20 9E B7 JSR $B79E
.,ABA8 A9 2C    LDA #$2C
.,ABAA 20 FF AE JSR $AEFF
.,ABAD 86 13    STX $13
.,ABAF 20 1E E1 JSR $E11E
.,ABB2 20 CE AB JSR $ABCE
.,ABB5 A5 13    LDA $13
.,ABB7 20 CC FF JSR $FFCC
.,ABBA A2 00    LDX #$00
.,ABBC 86 13    STX $13
.,ABBE 60       RTS


                                *** "INPUT" STATEMENT
.,ABBF C9 22    CMP #$22        CHECK FOR OPTIONAL PROMPT STRING
.,ABC1 D0 0B    BNE $ABCE       NO, PRINT "?" PROMPT
.,ABC3 20 BD AE JSR $AEBD       MAKE A PRINTABLE STRING OUT OF IT
.,ABC6 A9 3B    LDA #$3B        MUST HAVE ; NOW
.,ABC8 20 FF AE JSR $AEFF       
.,ABCB 20 21 AB JSR $AB21       PRINT THE STRING
.,ABCE 20 A6 B3 JSR $B3A6       ILLEGAL IF IN DIRECT MODE
.,ABD1 A9 2C    LDA #$2C        PRIME THE BUFFER
.,ABD3 8D FF 01 STA $01FF       
.,ABD6 20 F9 AB JSR $ABF9       NO STRING, PRINT "?"
.,ABD9 A5 13    LDA $13
.,ABDB F0 0D    BEQ $ABEA
.,ABDD 20 B7 FF JSR $FFB7
.,ABE0 29 02    AND #$02
.,ABE2 F0 06    BEQ $ABEA
.,ABE4 20 B5 AB JSR $ABB5
.,ABE7 4C F8 A8 JMP $A8F8
.,ABEA AD 00 02 LDA $0200
.,ABED D0 1E    BNE $AC0D
.,ABEF A5 13    LDA $13
.,ABF1 D0 E3    BNE $ABD6
.,ABF3 20 06 A9 JSR $A906
.,ABF6 4C FB A8 JMP $A8FB
.,ABF9 A5 13    LDA $13
.,ABFB D0 06    BNE $AC03
.,ABFD 20 45 AB JSR $AB45
.,AC00 20 3B AB JSR $AB3B
.,AC03 4C 60 A5 JMP $A560

                                *** "READ" STATEMENT
.,AC06 A6 41    LDX $41         Y,X POINTS AT NEXT DATA STATEMENT
.,AC08 A4 42    LDY $42         
.,AC0A A9 98    LDA #$98        SET INPUTFLG = $98
.:AC0C 2C       .BYTE $2C

.,AC0D A9 00    LDA #$00        SET INPUTFLG = $00

                                *** PROCESS INPUT LIST
                                (Y,X) IS ADDRESS OF INPUT DATA STRING
                                (A) = VALUE FOR INPUTFLG:  $00 FOR INPUT
                                                           $40 FOR GET
                                                           $98 FOR READ
.,AC0F 85 11    STA $11         
.,AC11 86 43    STX $43         ADDRESS OF INPUT STRING
.,AC13 84 44    STY $44         

.,AC15 20 8B B0 JSR $B08B       GET ADDRESS OF VARIABLE
.,AC18 85 49    STA $49         
.,AC1A 84 4A    STY $4A         
.,AC1C A5 7A    LDA $7A         SAVE CURRENT TXTPTR,
.,AC1E A4 7B    LDY $7B         WHICH POINTS INTO PROGRAM
.,AC20 85 4B    STA $4B         
.,AC22 84 4C    STY $4C         
.,AC24 A6 43    LDX $43         SET TXTPTR TO POINT AT INPUT BUFFER
.,AC26 A4 44    LDY $44         OR "DATA" LINE
.,AC28 86 7A    STX $7A         
.,AC2A 84 7B    STY $7B         
.,AC2C 20 79 00 JSR $0079       GET CHAR AT PNTR
.,AC2F D0 20    BNE $AC51       NOT END OF LINE OR COLON
.,AC31 24 11    BIT $11         DOING A "GET"?
.,AC33 50 0C    BVC $AC41       NO
.,AC35 20 24 E1 JSR $E124       YES, GET CHAR
.,AC38 8D 00 02 STA $0200       
.,AC3B A2 FF    LDX #$FF        
.,AC3D A0 01    LDY #$01        
.,AC3F D0 0C    BNE $AC4D       ...ALWAYS

.,AC41 30 75    BMI $ACB8       DOING A "READ"
.,AC43 A5 13    LDA $13
.,AC45 D0 03    BNE $AC4A
.,AC47 20 45 AB JSR $AB45       DOING AN "INPUT", PRINT "?"
.,AC4A 20 F9 AB JSR $ABF9       PRINT ANOTHER "?", AND INPUT A LINE
.,AC4D 86 7A    STX $7A         
.,AC4F 84 7B    STY $7B         

.,AC51 20 73 00 JSR $0073       GET NEXT INPUT CHAR
.,AC54 24 0D    BIT $0D         STRING OR NUMERIC?
.,AC56 10 31    BPL $AC89       NUMERIC
.,AC58 24 11    BIT $11         STRING -- NOW WHAT INPUT TYPE?
.,AC5A 50 09    BVC $AC65       NOT A "GET"
.,AC5C E8       INX             "GET"
.,AC5D 86 7A    STX $7A         
.,AC5F A9 00    LDA #$00        
.,AC61 85 07    STA $07         NO OTHER TERMINATORS THAN $00
.,AC63 F0 0C    BEQ $AC71       ...ALWAYS

.,AC65 85 07    STA $07         
.,AC67 C9 22    CMP #$22        TERMINATE ON $00 OR QUOTE
.,AC69 F0 07    BEQ $AC72       
.,AC6B A9 3A    LDA #$3A        TERMINATE ON $00, COLON, OR COMMA
.,AC6D 85 07    STA $07         
.,AC6F A9 2C    LDA #$2C        
.,AC71 18       CLC             
.,AC72 85 08    STA $08         
.,AC74 A5 7A    LDA $7A         
.,AC76 A4 7B    LDY $7B         
.,AC78 69 00    ADC #$00        SKIP OVER QUOTATION MARK, IF
.,AC7A 90 01    BCC $AC7D       THERE WAS ONE
.,AC7C C8       INY             
.,AC7D 20 8D B4 JSR $B48D       BUILD STRING STARTING AT (Y,A)
                                TERMINATED BY $00, (CHARAC), OR (ENDCHR)
.,AC80 20 E2 B7 JSR $B7E2       SET TXTPTR TO POINT AT STRING
.,AC83 20 DA A9 JSR $A9DA       STORE STRING IN VARIABLE
.,AC86 4C 91 AC JMP $AC91       

.,AC89 20 F3 BC JSR $BCF3       GET FP NUMBER AT TXTPTR
.,AC8C A5 0E    LDA $0E         
.,AC8E 20 C2 A9 JSR $A9C2       STORE RESULT IN VARIABLE

.,AC91 20 79 00 JSR $0079       
.,AC94 F0 07    BEQ $AC9D       END OF LINE OR COLON
.,AC96 C9 2C    CMP #$2C        COMMA IN INPUT?
.,AC98 F0 03    BEQ $AC9D       YES
.,AC9A 4C 4D AB JMP $AB4D       NOTHING ELSE WILL DO
.,AC9D A5 7A    LDA $7A         SAVE POSITION IN INPUT BUFFER
.,AC9F A4 7B    LDY $7B         
.,ACA1 85 43    STA $43         
.,ACA3 84 44    STY $44         
.,ACA5 A5 4B    LDA $4B         RESTORE PROGRAM POINTER
.,ACA7 A4 4C    LDY $4C         
.,ACA9 85 7A    STA $7A         
.,ACAB 84 7B    STY $7B         
.,ACAD 20 79 00 JSR $0079       NEXT CHAR FROM PROGRAM
.,ACB0 F0 2D    BEQ $ACDF       END OF STATEMENT
.,ACB2 20 FD AE JSR $AEFD       BETTER BE A COMMA THEN
.,ACB5 4C 15 AC JMP $AC15       

.,ACB8 20 06 A9 JSR $A906       GET OFFSET TO NEXT COLON OR EOL
.,ACBB C8       INY             TO FIRST CHAR OF NEXT LINE
.,ACBC AA       TAX             WHICH:  EOL OR COLON?
.,ACBD D0 12    BNE $ACD1       COLON
.,ACBF A2 0D    LDX #$0D        EOL: MIGHT BE OUT OF DATA
.,ACC1 C8       INY             CHECK HI-BYTE OF FORWARD PNTR
.,ACC2 B1 7A    LDA ($7A),Y     END OF PROGRAM?
.,ACC4 F0 6C    BEQ $AD32       YES, WE ARE OUT OF DATA
.,ACC6 C8       INY             PICK UP THE LINE #
.,ACC7 B1 7A    LDA ($7A),Y     
.,ACC9 85 3F    STA $3F         
.,ACCB C8       INY             
.,ACCC B1 7A    LDA ($7A),Y     
.,ACCE C8       INY             POINT AT FIRST TEXT CHAR IN LINE
.,ACCF 85 40    STA $40         
.,ACD1 20 FB A8 JSR $A8FB       GET 1ST TOKEN OF STATEMENT
.,ACD4 20 79 00 JSR $0079
.,ACD7 AA       TAX             SAVE TOKEN IN X-REG
.,ACD8 E0 83    CPX #$83        DID WE FIND A "DATA" STATEMENT?
.,ACDA D0 DC    BNE $ACB8       NOT YET
.,ACDC 4C 51 AC JMP $AC51       YES, READ IT
                                
                                NO MORE INPUT REQUESTED
.,ACDF A5 43    LDA $43         GET POINTER IN CASE IT WAS "READ"
.,ACE1 A4 44    LDY $44         
.,ACE3 A6 11    LDX $11         "READ" OR "INPUT"?
.,ACE5 10 03    BPL $ACEA       "INPUT"
.,ACE7 4C 27 A8 JMP $A827       "DATA", SO STORE (Y,X) AT DATPTR
.,ACEA A0 00    LDY #$00        "INPUT":  ANY MORE CHARS ON LINE?
.,ACEC B1 43    LDA ($43),Y     
.,ACEE F0 0B    BEQ $ACFB       NO, ALL IS WELL
.,ACF0 A5 13    LDA $13         YES, ERROR
.,ACF2 D0 07    BNE $ACFB
.,ACF4 A9 FC    LDA #$FC
.,ACF6 A0 AC    LDY #$AC        "EXTRA IGNORED"
.,ACF8 4C 1E AB JMP $AB1E       
.,ACFB 60       RTS             

.:ACFC 3F 45 58 54 52 41 20 49  '?extra ignored'
.:AD04 47 4E 4F 52 45 44 0D 00
.:AD0C 3F 52 45 44 4F 20 46 52  '?redo from start'
.:AD14 4F 4D 20 53 54 41 52 54
.:AD1C 0D 00

                                *** "NEXT" STATEMENT
.,AD1E D0 04    BNE $AD24       VARIABLE AFTER "NEXT"
.,AD20 A0 00    LDY #$00        FLAG BY SETTING FORPNT+1 = 0
.,AD22 F0 03    BEQ $AD27       ...ALWAYS

.,AD24 20 8B B0 JSR $B08B       GET PNTR TO VARIABLE IN (Y,A)
.,AD27 85 49    STA $49         
.,AD29 84 4A    STY $4A         
.,AD2B 20 8A A3 JSR $A38A       FIND FOR-FRAME FOR THIS VARIABLE
.,AD2E F0 05    BEQ $AD35       FOUND IT
.,AD30 A2 0A    LDX #$0A        NOT THERE, ABORT
.,AD32 4C 37 A4 JMP $A437       ...ALWAYS
.,AD35 9A       TXS             SET STACK PTR TO POINT TO THIS FRAME,
.,AD36 8A       TXA
.,AD37 18       CLC
.,AD38 69 04    ADC #$04
.,AD3A 48       PHA
.,AD3B 69 06    ADC #$06
.,AD3D 85 24    STA $24
.,AD3F 68       PLA
.,AD40 A0 01    LDY #$01        (Y,A) IS ADDRESS OF STEP VALUE
.,AD42 20 A2 BB JSR $BBA2       STEP TO FAC
.,AD45 BA       TSX             
.,AD46 BD 09 01 LDA $0109,X     
.,AD49 85 66    STA $66         
.,AD4B A5 49    LDA $49         
.,AD4D A4 4A    LDY $4A         
.,AD4F 20 67 B8 JSR $B867       ADD TO FOR VALUE
.,AD52 20 D0 BB JSR $BBD0       PUT NEW VALUE BACK
.,AD55 A0 01    LDY #$01        (Y,A) IS ADDRESS OF END VALUE
.,AD57 20 5D BC JSR $BC5D       COMPARE TO END VALUE
.,AD5A BA       TSX             
.,AD5B 38       SEC             
.,AD5C FD 09 01 SBC $0109,X     SIGN OF STEP
.,AD5F F0 17    BEQ $AD78       BRANCH IF FOR COMPLETE
.,AD61 BD 0F 01 LDA $010F,X     OTHERWISE SET UP
.,AD64 85 39    STA $39         FOR LINE #
.,AD66 BD 10 01 LDA $0110,X     
.,AD69 85 3A    STA $3A         
.,AD6B BD 12 01 LDA $0112,X     AND SET TXTPTR TO JUST
.,AD6E 85 7A    STA $7A         AFTER FOR STATEMENT
.,AD70 BD 11 01 LDA $0111,X     
.,AD73 85 7B    STA $7B         
.,AD75 4C AE A7 JMP $A7AE       
.,AD78 8A       TXA             POP OFF FOR-FRAME, LOOP IS DONE
.,AD79 69 11    ADC #$11        CARRY IS SET, SO ADDS 18
.,AD7B AA       TAX             
.,AD7C 9A       TXS             
.,AD7D 20 79 00 JSR $0079       CHAR AFTER VARIABLE
.,AD80 C9 2C    CMP #$2C        ANOTHER VARIABLE IN NEXT?
.,AD82 D0 F1    BNE $AD75       NO, GO TO NEXT STATEMENT
.,AD84 20 73 00 JSR $0073       YES, PRIME FOR NEXT VARIABLE
.,AD87 20 24 AD JSR $AD24       (DOES NOT RETURN)

                                *** EVALUATE EXPRESSION, MAKE SURE IT IS NUMERIC
.,AD8A 20 9E AD JSR $AD9E       

                                *** MAKE SURE (FAC) IS NUMERIC
.,AD8D 18       CLC             
.:AD8E 24       .BYTE $24       DUMMY FOR SKIP

                                *** MAKE SURE (FAC) IS STRING
.,AD8F 38       SEC             

                                *** MAKE SURE (FAC) IS CORRECT TYPE
                                IF C=0, TYPE MUST BE NUMERIC
                                IF C=1, TYPE MUST BE STRING
.,AD90 24 0D    BIT $0D         $00 IF NUMERIC, $FF IF STRING
.,AD92 30 03    BMI $AD97       TYPE IS STRING
.,AD94 B0 03    BCS $AD99       NOT STRING, BUT WE NEED STRING
.,AD96 60       RTS             TYPE IS CORRECT
.,AD97 B0 FD    BCS $AD96       IS STRING AND WE WANTED STRING
.,AD99 A2 16    LDX #$16        TYPE MISMATCH
.,AD9B 4C 37 A4 JMP $A437       

                                *** EVALUATE THE EXPRESSION AT TXTPTR, LEAVING THE
                                *** RESULT IN FAC.
                                WORKS FOR BOTH STRING AND NUMERIC EXPRESSIONS.
.,AD9E A6 7A    LDX $7A         DECREMENT TXTPTR
.,ADA0 D0 02    BNE $ADA4       
.,ADA2 C6 7B    DEC $7B         
.,ADA4 C6 7A    DEC $7A         
.,ADA6 A2 00    LDX #$00        START WITH PRECEDENCE = 0
.:ADA8 24       .BYTE $24       TRICK TO SKIP FOLLOWING "PHA"

.,ADA9 48       PHA             PUSH RELOPS FLAGS
.,ADAA 8A       TXA             
.,ADAB 48       PHA             SAVE LAST PRECEDENCE
.,ADAC A9 01    LDA #$01        
.,ADAE 20 FB A3 JSR $A3FB       CHECK IF ENOUGH ROOM ON STACK
.,ADB1 20 83 AE JSR $AE83       GET AN ELEMENT
.,ADB4 A9 00    LDA #$00        
.,ADB6 85 4D    STA $4D         CLEAR COMPARISON OPERATOR FLAGS

.,ADB8 20 79 00 JSR $0079       CHECK FOR RELATIONAL OPERATORS
.,ADBB 38       SEC             > IS $CF, = IS $D0, < IS $D1
.,ADBC E9 B1    SBC #$B1        > IS 0, = IS 1, < IS 2
.,ADBE 90 17    BCC $ADD7       NOT RELATIONAL OPERATOR
.,ADC0 C9 03    CMP #$03        
.,ADC2 B0 13    BCS $ADD7       NOT RELATIONAL OPERATOR
.,ADC4 C9 01    CMP #$01        SET CARRY IF "=" OR "<"
.,ADC6 2A       ROL             NOW > IS 0, = IS 3, < IS 5
.,ADC7 49 01    EOR #$01        NOW > IS 1, = IS 2, < IS 4
.,ADC9 45 4D    EOR $4D         SET BITS OF CPRTYP:  00000<=>
.,ADCB C5 4D    CMP $4D         CHECK FOR ILLEGAL COMBINATIONS
.,ADCD 90 61    BCC $AE30       IF LESS THAN, A RELOP WAS REPEATED
.,ADCF 85 4D    STA $4D         
.,ADD1 20 73 00 JSR $0073       ANOTHER OPERATOR?
.,ADD4 4C BB AD JMP $ADBB       CHECK FOR <,=,> AGAIN

.,ADD7 A6 4D    LDX $4D         DID WE FIND A RELATIONAL OPERATOR?
.,ADD9 D0 2C    BNE $AE07       YES
.,ADDB B0 7B    BCS $AE58       NO, AND NEXT TOKEN IS > $D1
.,ADDD 69 07    ADC #$07        NO, AND NEXT TOKEN < $CF
.,ADDF 90 77    BCC $AE58       IF NEXT TOKEN < "+"
.,ADE1 65 0D    ADC $0D         + AND LAST RESULT A STRING?
.,ADE3 D0 03    BNE $ADE8       BRANCH IF NOT
.,ADE5 4C 3D B6 JMP $B63D       CONCATENATE IF SO.

.,ADE8 69 FF    ADC #$FF        +-*/ IS 0123
.,ADEA 85 22    STA $22         
.,ADEC 0A       ASL             MULTIPLY BY 3
.,ADED 65 22    ADC $22         +-*/ IS 0,3,6,9
.,ADEF A8       TAY             

.,ADF0 68       PLA             GET LAST PRECEDENCE
.,ADF1 D9 80 A0 CMP $A080,Y     
.,ADF4 B0 67    BCS $AE5D       DO NOW IF HIGHER PRECEDENCE
.,ADF6 20 8D AD JSR $AD8D       WAS LAST RESULT A #?
.,ADF9 48       PHA             YES, SAVE PRECEDENCE ON STACK
.,ADFA 20 20 AE JSR $AE20       SAVE REST, CALL FRMEVL RECURSIVELY
.,ADFD 68       PLA
.,ADFE A4 4B    LDY $4B         
.,AE00 10 17    BPL $AE19       
.,AE02 AA       TAX             
.,AE03 F0 56    BEQ $AE5B       EXIT IF NO MATH IN EXPRESSION
.,AE05 D0 5F    BNE $AE66       ...ALWAYS

                                FOUND ONE OR MORE RELATIONAL OPERATORS <,=,>
.,AE07 46 0D    LSR $0D         (VALTYP) = 0 (NUMERIC), = $FF (STRING)
.,AE09 8A       TXA             SET CPRTYP TO 0000<=>C
.,AE0A 2A       ROL             WHERE C=0 IF #, C=1 IF STRING
.,AE0B A6 7A    LDX $7A         BACK UP TXTPTR
.,AE0D D0 02    BNE $AE11       
.,AE0F C6 7B    DEC $7B         
.,AE11 C6 7A    DEC $7A         
.,AE13 A0 1B    LDY #$1B        POINT AT RELOPS ENTRY
.,AE15 85 4D    STA $4D         
.,AE17 D0 D7    BNE $ADF0       ...ALWAYS

.,AE19 D9 80 A0 CMP $A080,Y     
.,AE1C B0 48    BCS $AE66       DO NOW IF HIGHER PRECEDENCE
.,AE1E 90 D9    BCC $ADF9       ...ALWAYS

                                STACK THIS OPERATION AND CALL FRMEVL FOR
                                ANOTHER ONE
.,AE20 B9 82 A0 LDA $A082,Y     
.,AE23 48       PHA             PUSH ADDRESS OF OPERATION PERFORMER
.,AE24 B9 81 A0 LDA $A081,Y     
.,AE27 48       PHA             
.,AE28 20 33 AE JSR $AE33       STACK FAC.SIGN AND FAC
.,AE2B A5 4D    LDA $4D         A=RELOP FLAGS, X=PRECEDENCE BYTE
.,AE2D 4C A9 AD JMP $ADA9       RECURSIVELY CALL FRMEVL

.,AE30 4C 08 AF JMP $AF08       

                                *** STACK (FAC)
                                THREE ENTRY POINTS:
                                    .1, FROM FRMEVL
                                    .2, FROM "STEP"
                                    .3, FROM "FOR"
.,AE33 A5 66    LDA $66         GET FAC.SIGN TO PUSH IT
.,AE35 BE 80 A0 LDX $A080,Y     PRECEDENCE BYTE FROM MATHTBL

                                ENTER HERE FROM "STEP", TO PUSH STEP SIGN AND VALUE
.,AE38 A8       TAY             FAC.SIGN OR SGN(STEP VALUE)
.,AE39 68       PLA             PULL RETURN ADDRESS AND ADD 1
.,AE3A 85 22    STA $22         <<< ASSUMES NOT ON PAGE BOUNDARY! >>>
.,AE3C E6 22    INC $22         PLACE BUMPED RETURN ADDRESS IN
.,AE3E 68       PLA             INDEX,INDEX+1
.,AE3F 85 23    STA $23         
.,AE41 98       TYA             FAC.SIGN OR SGN(STEP VALUE)
.,AE42 48       PHA             PUSH FAC.SIGN OR SGN(STEP VALUE)

                                ENTER HERE FROM "FOR", WITH (INDEX) = STEP,
                                TO PUSH INITIAL VALUE OF "FOR" VARIABLE
.,AE43 20 1B BC JSR $BC1B       ROUND TO 32 BITS
.,AE46 A5 65    LDA $65         PUSH (FAC)
.,AE48 48       PHA             
.,AE49 A5 64    LDA $64         
.,AE4B 48       PHA             
.,AE4C A5 63    LDA $63         
.,AE4E 48       PHA             
.,AE4F A5 62    LDA $62         
.,AE51 48       PHA             
.,AE52 A5 61    LDA $61         
.,AE54 48       PHA             
.,AE55 6C 22 00 JMP ($0022)     DO RTS FUNNY WAY

.,AE58 A0 FF    LDY #$FF        SET UP TO EXIT ROUTINE
.,AE5A 68       PLA             
.,AE5B F0 23    BEQ $AE80       EXIT IF NO MATH TO DO

                                *** PERFORM STACKED OPERATION
                                (A) = PRECEDENCE BYTE
                                STACK:  1 -- CPRMASK
                                        5 -- (ARG)
                                        2 -- ADDR OF PERFORMER
.,AE5D C9 64    CMP #$64        WAS IT RELATIONAL OPERATOR?
.,AE5F F0 03    BEQ $AE64       YES, ALLOW STRING COMPARE
.,AE61 20 8D AD JSR $AD8D       MUST BE NUMERIC VALUE
.,AE64 84 4B    STY $4B         

.,AE66 68       PLA             GET 0000<=>C FROM STACK
.,AE67 4A       LSR             SHIFT TO 00000<=> FORM
.,AE68 85 12    STA $12         00000<=>
.,AE6A 68       PLA             
.,AE6B 85 69    STA $69         GET FLOATING POINT VALUE OFF STACK,
.,AE6D 68       PLA             AND PUT IT IN ARG
.,AE6E 85 6A    STA $6A         
.,AE70 68       PLA             
.,AE71 85 6B    STA $6B         
.,AE73 68       PLA             
.,AE74 85 6C    STA $6C         
.,AE76 68       PLA             
.,AE77 85 6D    STA $6D         
.,AE79 68       PLA             
.,AE7A 85 6E    STA $6E         
.,AE7C 45 66    EOR $66         SAVE EOR OF SIGNS OF THE OPERANDS,
.,AE7E 85 6F    STA $6F         IN CASE OF MULTIPLY OR DIVIDE
.,AE80 A5 61    LDA $61         FAC EXPONENT IN A-REG
.,AE82 60       RTS             STATUS .EQ. IF (FAC)=0
                                RTS GOES TO PERFORM OPERATION

                                *** GET ELEMENT IN EXPRESSION
                                GET VALUE OF VARIABLE OR NUMBER AT TXTPNT, OR POINT
                                TO STRING DESCRIPTOR IF A STRING, AND PUT IN FAC.
.,AE83 6C 0A 03 JMP ($030A)
.,AE86 A9 00    LDA #$00        ASSUME NUMERIC
.,AE88 85 0D    STA $0D         
.,AE8A 20 73 00 JSR $0073       
.,AE8D B0 03    BCS $AE92       NOT A DIGIT
.,AE8F 4C F3 BC JMP $BCF3       NUMERIC CONSTANT
.,AE92 20 13 B1 JSR $B113       VARIABLE NAME?
.,AE95 90 03    BCC $AE9A       
.,AE97 4C 28 AF JMP $AF28       YES
.,AE9A C9 FF    CMP #$FF
.,AE9C D0 0F    BNE $AEAD
.,AE9E A9 A8    LDA #$A8
.,AEA0 A0 AE    LDY #$AE
.,AEA2 20 A2 BB JSR $BBA2
.,AEA5 4C 73 00 JMP $0073

.:AEA8 82 49 0F DA A1

.,AEAD C9 2E    CMP #$2E        DECIMAL POINT
.,AEAF F0 DE    BEQ $AE8F       YES, NUMERIC CONSTANT
.,AEB1 C9 AB    CMP #$AB        UNARY MINUS?
.,AEB3 F0 58    BEQ $AF0D       YES
.,AEB5 C9 AA    CMP #$AA        UNARY PLUS
.,AEB7 F0 D1    BEQ $AE8A       YES
.,AEB9 C9 22    CMP #$22        STRING CONSTANT?
.,AEBB D0 0F    BNE $AECC       NO

                                *** STRING CONSTANT ELEMENT
                                SET Y,A = (TXTPTR)+CARRY
.,AEBD A5 7A    LDA $7A         ADD (CARRY) TO GET ADDRESS OF 1ST CHAR
.,AEBF A4 7B    LDY $7B         OF STRING IN Y,A
.,AEC1 69 00    ADC #$00        
.,AEC3 90 01    BCC $AEC6       
.,AEC5 C8       INY             
.,AEC6 20 87 B4 JSR $B487       BUILD DESCRIPTOR TO STRING
                                GET ADDRESS OF DESCRIPTOR IN FAC
.,AEC9 4C E2 B7 JMP $B7E2       POINT TXTPTR AFTER TRAILING QUOTE

.,AECC C9 A8    CMP #$A8        
.,AECE D0 13    BNE $AEE3       NOT "NOT", TRY "FN"
.,AED0 A0 18    LDY #$18        POINT AT = COMPARISON
.,AED2 D0 3B    BNE $AF0F       ...ALWAYS

                                *** "NOT" FUNCTION
                                IF FAC=0, RETURN FAC=1
                                IF FAC<>0, RETURN FAC=0
.,AED4 20 BF B1 JSR $B1BF
.,AED7 A5 65    LDA $65
.,AED9 49 FF    EOR #$FF
.,AEDB A8       TAY
.,AEDC A5 64    LDA $64
.,AEDE 49 FF    EOR #$FF
.,AEE0 4C 91 B3 JMP $B391

                                *** COMPARISON FOR EQUALITY (= OPERATOR)
                                ALSO USED TO EVALUATE "NOT" FUNCTION
.,AEE3 C9 A5    CMP #$A5        
.,AEE5 D0 03    BNE $AEEA       
.,AEE7 4C F4 B3 JMP $B3F4       

.,AEEA C9 B4    CMP #$B4        
.,AEEC 90 03    BCC $AEF1       
.,AEEE 4C A7 AF JMP $AFA7       

                                *** EVALUATE "(EXPRESSION)"
.,AEF1 20 FA AE JSR $AEFA       IS THERE A '(' AT TXTPTR?
.,AEF4 20 9E AD JSR $AD9E       YES, EVALUATE EXPRESSION

.,AEF7 A9 29    LDA #$29        CHECK FOR ')'
.:AEF9 2C       .BYTE $2C       TRICK

.,AEFA A9 28    LDA #$28        
.:AEFC 2C       .BYTE $2C       TRICK

.,AEFD A9 2C    LDA #$2C        COMMA AT TXTPTR?

                                *** UNLESS CHAR AT TXTPTR = (A), SYNTAX ERROR
.,AEFF A0 00    LDY #$00        
.,AF01 D1 7A    CMP ($7A),Y     
.,AF03 D0 03    BNE $AF08       
.,AF05 4C 73 00 JMP $0073       MATCH, GET NEXT CHAR &amp; RETURN

.,AF08 A2 0B    LDX #$0B        
.,AF0A 4C 37 A4 JMP $A437       

.,AF0D A0 15    LDY #$15        POINT AT UNARY MINUS
.,AF0F 68       PLA             
.,AF10 68       PLA             
.,AF11 4C FA AD JMP $ADFA       

.,AF14 38       SEC
.,AF15 A5 64    LDA $64
.,AF17 E9 00    SBC #$00
.,AF19 A5 65    LDA $65
.,AF1B E9 A0    SBC #$A0
.,AF1D 90 08    BCC $AF27
.,AF1F A9 A2    LDA #$A2
.,AF21 E5 64    SBC $64
.,AF23 A9 E3    LDA #$E3
.,AF25 E5 65    SBC $65
.,AF27 60       RTS

.,AF28 20 8B B0 JSR $B08B       
.,AF2B 85 64    STA $64         ADDRESS OF VARIABLE
.,AF2D 84 65    STY $65         
.,AF2F A6 45    LDX $45         NUMERIC OR STRING?
.,AF31 A4 46    LDY $46
.,AF33 A5 0D    LDA $0D
.,AF35 F0 26    BEQ $AF5D       NUMERIC
.,AF37 A9 00    LDA #$00
.,AF39 85 70    STA $70
.,AF3B 20 14 AF JSR $AF14
.,AF3E 90 1C    BCC $AF5C
.,AF40 E0 54    CPX #$54
.,AF42 D0 18    BNE $AF5C
.,AF44 C0 C9    CPY #$C9
.,AF46 D0 14    BNE $AF5C
.,AF48 20 84 AF JSR $AF84
.,AF4B 84 5E    STY $5E
.,AF4D 88       DEY
.,AF4E 84 71    STY $71
.,AF50 A0 06    LDY #$06
.,AF52 84 5D    STY $5D
.,AF54 A0 24    LDY #$24
.,AF56 20 68 BE JSR $BE68
.,AF59 4C 6F B4 JMP $B46F
.,AF5C 60       RTS
.,AF5D 24 0E    BIT $0E
.,AF5F 10 0D    BPL $AF6E       FLOATING POINT
.,AF61 A0 00    LDY #$00        INTEGER
.,AF63 B1 64    LDA ($64),Y     
.,AF65 AA       TAX             GET VALUE IN A,Y
.,AF66 C8       INY             
.,AF67 B1 64    LDA ($64),Y     
.,AF69 A8       TAY             
.,AF6A 8A       TXA             
.,AF6B 4C 91 B3 JMP $B391       CONVERT A,Y TO FLOATING POINT
.,AF6E 20 14 AF JSR $AF14
.,AF71 90 2D    BCC $AFA0
.,AF73 E0 54    CPX #$54
.,AF75 D0 1B    BNE $AF92
.,AF77 C0 49    CPY #$49
.,AF79 D0 25    BNE $AFA0
.,AF7B 20 84 AF JSR $AF84
.,AF7E 98       TYA
.,AF7F A2 A0    LDX #$A0
.,AF81 4C 4F BC JMP $BC4F
.,AF84 20 DE FF JSR $FFDE
.,AF87 86 64    STX $64
.,AF89 84 63    STY $63
.,AF8B 85 65    STA $65
.,AF8D A0 00    LDY #$00
.,AF8F 84 62    STY $62
.,AF91 60       RTS
.,AF92 E0 53    CPX #$53
.,AF94 D0 0A    BNE $AFA0
.,AF96 C0 54    CPY #$54
.,AF98 D0 06    BNE $AFA0
.,AF9A 20 B7 FF JSR $FFB7
.,AF9D 4C 3C BC JMP $BC3C
.,AFA0 A5 64    LDA $64
.,AFA2 A4 65    LDY $65
.,AFA4 4C A2 BB JMP $BBA2       

                                *** PROCESS UNARY OPERATORS (FUNCTIONS)
.,AFA7 0A       ASL             DOUBLE TOKEN TO GET INDEX
.,AFA8 48       PHA             
.,AFA9 AA       TAX             
.,AFAA 20 73 00 JSR $0073       
.,AFAD E0 8F    CPX #$8F        LEFT$, RIGHT$, AND MID$
.,AFAF 90 20    BCC $AFD1       NOT ONE OF THE STRING FUNCTIONS
.,AFB1 20 FA AE JSR $AEFA       STRING FUNCTION, NEED "("
.,AFB4 20 9E AD JSR $AD9E       EVALUATE EXPRESSION FOR STRING
.,AFB7 20 FD AE JSR $AEFD       REQUIRE A COMMA
.,AFBA 20 8F AD JSR $AD8F       MAKE SURE EXPRESSION IS A STRING
.,AFBD 68       PLA             
.,AFBE AA       TAX             RETRIEVE ROUTINE POINTER
.,AFBF A5 65    LDA $65         STACK ADDRESS OF STRING
.,AFC1 48       PHA             
.,AFC2 A5 64    LDA $64         
.,AFC4 48       PHA             
.,AFC5 8A       TXA             
.,AFC6 48       PHA             STACK DOUBLED TOKEN
.,AFC7 20 9E B7 JSR $B79E       CONVERT NEXT EXPRESSION TO BYTE IN X-REG
.,AFCA 68       PLA             GET DOUBLED TOKEN OFF STACK
.,AFCB A8       TAY             USE AS INDEX TO BRANCH
.,AFCC 8A       TXA             VALUE OF SECOND PARAMETER
.,AFCD 48       PHA             PUSH 2ND PARAM
.,AFCE 4C D6 AF JMP $AFD6       JOIN UNARY FUNCTIONS
.,AFD1 20 F1 AE JSR $AEF1       REQUIRE "(EXPRESSION)"
.,AFD4 68       PLA             
.,AFD5 A8       TAY             INDEX INTO FUNCTION ADDRESS TABLE
.,AFD6 B9 EA 9F LDA $9FEA,Y     
.,AFD9 85 55    STA $55         PREPARE TO JSR TO ADDRESS
.,AFDB B9 EB 9F LDA $9FEB,Y     
.,AFDE 85 56    STA $56         
.,AFE0 20 54 00 JSR $0054       DOES NOT RETURN FOR
                                CHR$, LEFT$, RIGHT$, OR MID$
.,AFE3 4C 8D AD JMP $AD8D       REQUIRE NUMERIC RESULT

.,AFE6 A0 FF    LDY #$FF
.:AFE8 2C       .BYTE $2C
.,AFE9 A0 00    LDY #$00
.,AFEB 84 0B    STY $0B
.,AFED 20 BF B1 JSR $B1BF
.,AFF0 A5 64    LDA $64
.,AFF2 45 0B    EOR $0B
.,AFF4 85 07    STA $07
.,AFF6 A5 65    LDA $65
.,AFF8 45 0B    EOR $0B
.,AFFA 85 08    STA $08
.,AFFC 20 FC BB JSR $BBFC
.,AFFF 20 BF B1 JSR $B1BF
.,B002 A5 65    LDA $65
.,B004 45 0B    EOR $0B
.,B006 25 08    AND $08
.,B008 45 0B    EOR $0B
.,B00A A8       TAY
.,B00B A5 64    LDA $64
.,B00D 45 0B    EOR $0B
.,B00F 25 07    AND $07
.,B011 45 0B    EOR $0B
.,B013 4C 91 B3 JMP $B391

                                *** PERFORM RELATIONAL OPERATIONS
.,B016 20 90 AD JSR $AD90       MAKE SURE FAC IS CORRECT TYPE
.,B019 B0 13    BCS $B02E       TYPE MATCHES, BRANCH IF STRINGS
.,B01B A5 6E    LDA $6E         NUMERIC COMPARISON
.,B01D 09 7F    ORA #$7F        RE-PACK VALUE IN ARG FOR FCOMP
.,B01F 25 6A    AND $6A         
.,B021 85 6A    STA $6A         
.,B023 A9 69    LDA #$69        
.,B025 A0 00    LDY #$00        
.,B027 20 5B BC JSR $BC5B       RETURN A-REG = -1,0,1
.,B02A AA       TAX             AS ARG <,=,> FAC
.,B02B 4C 61 B0 JMP $B061       

                                *** STRING COMPARISON
.,B02E A9 00    LDA #$00        SET RESULT TYPE TO NUMERIC
.,B030 85 0D    STA $0D         
.,B032 C6 4D    DEC $4D         MAKE CPRTYP 0000<=>0
.,B034 20 A6 B6 JSR $B6A6       
.,B037 85 61    STA $61         STRING LENGTH
.,B039 86 62    STX $62         
.,B03B 84 63    STY $63         
.,B03D A5 6C    LDA $6C         
.,B03F A4 6D    LDY $6D         
.,B041 20 AA B6 JSR $B6AA       
.,B044 86 6C    STX $6C         
.,B046 84 6D    STY $6D         
.,B048 AA       TAX             LEN (ARG) STRING
.,B049 38       SEC             
.,B04A E5 61    SBC $61         SET X TO SMALLER LEN
.,B04C F0 08    BEQ $B056       
.,B04E A9 01    LDA #$01        
.,B050 90 04    BCC $B056       
.,B052 A6 61    LDX $61         
.,B054 A9 FF    LDA #$FF        
.,B056 85 66    STA $66         FLAG WHICH SHORTER
.,B058 A0 FF    LDY #$FF        
.,B05A E8       INX             
.,B05B C8       INY             
.,B05C CA       DEX             
.,B05D D0 07    BNE $B066       MORE CHARS IN BOTH STRINGS
.,B05F A6 66    LDX $66         IF = SO FAR, DECIDE BY LENGTH

.,B061 30 0F    BMI $B072       
.,B063 18       CLC             
.,B064 90 0C    BCC $B072       ...ALWAYS

.,B066 B1 6C    LDA ($6C),Y     
.,B068 D1 62    CMP ($62),Y     
.,B06A F0 EF    BEQ $B05B       SAME, KEEP COMPARING
.,B06C A2 FF    LDX #$FF        IN CASE ARG GREATER
.,B06E B0 02    BCS $B072       IT IS
.,B070 A2 01    LDX #$01        FAC GREATER

.,B072 E8       INX             CONVERT FF,0,1 TO 0,1,2
.,B073 8A       TXA             
.,B074 2A       ROL             AND TO 0,2,4 IF C=0, ELSE 1,2,5
.,B075 25 12    AND $12         00000<=>
.,B077 F0 02    BEQ $B07B       IF NO MATCH: FALSE
.,B079 A9 FF    LDA #$FF        AT LEAST ONE MATCH: TRUE
.,B07B 4C 3C BC JMP $BC3C       

                                *** "DIM" STATEMENT
.,B07E 20 FD AE JSR $AEFD       SEPARATED BY COMMAS
.,B081 AA       TAX             NON-ZERO, FLAGS PTRGET DIM CALLED
.,B082 20 90 B0 JSR $B090       ALLOCATE THE ARRAY
.,B085 20 79 00 JSR $0079       NEXT CHAR
.,B088 D0 F4    BNE $B07E       NOT END OF STATEMENT
.,B08A 60       RTS             

                                *** PTRGET -- GENERAL VARIABLE SCAN
                                SCANS VARIABLE NAME AT TXTPTR, AND SEARCHES THE
                                VARTAB AND ARYTAB FOR THE NAME.
                                IF NOT FOUND, CREATE VARIABLE OF APPROPRIATE TYPE.
                                RETURN WITH ADDRESS IN VARPNT AND Y,A

                                ACTUAL ACTIVITY CONTROLLED SOMEWHAT BY TWO FLAGS:
                                    DIMFLG -- NONZERO IF CALLED FROM "DIM"
                                              ELSE = 0

                                    SUBFLG -- = $00
                                              = $40 IF CALLED FROM "GETARYPT"
                                              = $80 IF CALLED FROM "DEF FN"
                                              = $C1-DA IF CALLED FROM "FN"
.,B08B A2 00    LDX #$00        
.,B08D 20 79 00 JSR $0079       GET FIRST CHAR OF VARIABLE NAME

.,B090 86 0C    STX $0C         X IS NONZERO IF FROM DIM

.,B092 85 45    STA $45         
.,B094 20 79 00 JSR $0079       
.,B097 20 13 B1 JSR $B113       IS IT A LETTER?
.,B09A B0 03    BCS $B09F       YES, OKAY SO FAR
.,B09C 4C 08 AF JMP $AF08       NO, SYNTAX ERROR
.,B09F A2 00    LDX #$00        
.,B0A1 86 0D    STX $0D         
.,B0A3 86 0E    STX $0E         
.,B0A5 20 73 00 JSR $0073       SECOND CHAR OF VARIABLE NAME
.,B0A8 90 05    BCC $B0AF       NUMERIC
.,B0AA 20 13 B1 JSR $B113       LETTER?
.,B0AD 90 0B    BCC $B0BA       NO, END OF NAME
.,B0AF AA       TAX             SAVE SECOND CHAR OF NAME IN X
.,B0B0 20 73 00 JSR $0073       SCAN TO END OF VARIABLE NAME
.,B0B3 90 FB    BCC $B0B0       NUMERIC
.,B0B5 20 13 B1 JSR $B113       
.,B0B8 B0 F6    BCS $B0B0       ALPHA
.,B0BA C9 24    CMP #$24        STRING?
.,B0BC D0 06    BNE $B0C4       NO
.,B0BE A9 FF    LDA #$FF        
.,B0C0 85 0D    STA $0D         
.,B0C2 D0 10    BNE $B0D4       ...ALWAYS
.,B0C4 C9 25    CMP #$25        INTEGER?
.,B0C6 D0 13    BNE $B0DB       NO
.,B0C8 A5 10    LDA $10         YES; INTEGER VARIABLE ALLOWED?
.,B0CA D0 D0    BNE $B09C       NO, SYNTAX ERROR
.,B0CC A9 80    LDA #$80        YES
.,B0CE 85 0E    STA $0E         FLAG INTEGER MODE
.,B0D0 05 45    ORA $45         
.,B0D2 85 45    STA $45         SET SIGN BIT ON VARNAME
.,B0D4 8A       TXA             SECOND CHAR OF NAME
.,B0D5 09 80    ORA #$80        SET SIGN
.,B0D7 AA       TAX             
.,B0D8 20 73 00 JSR $0073       GET TERMINATING CHAR
.,B0DB 86 46    STX $46         STORE SECOND CHAR OF NAME
.,B0DD 38       SEC             
.,B0DE 05 10    ORA $10         $00 OR $40 IF SUBSCRIPTS OK, ELSE $80
.,B0E0 E9 28    SBC #$28        IF SUBFLG=$00 AND CHAR="("...
.,B0E2 D0 03    BNE $B0E7       NOPE
.,B0E4 4C D1 B1 JMP $B1D1       YES
.,B0E7 A0 00    LDY #$00
.,B0E9 84 10    STY $10
.,B0EB A5 2D    LDA $2D         START LOWTR AT SIMPLE VARIABLE TABLE
.,B0ED A6 2E    LDX $2E         
.,B0EF 86 60    STX $60         
.,B0F1 85 5F    STA $5F         
.,B0F3 E4 30    CPX $30         END OF SIMPLE VARIABLES?
.,B0F5 D0 04    BNE $B0FB       NO, GO ON
.,B0F7 C5 2F    CMP $2F         YES; END OF ARRAYS?
.,B0F9 F0 22    BEQ $B11D       YES, MAKE ONE
.,B0FB A5 45    LDA $45         SAME FIRST LETTER?
.,B0FD D1 5F    CMP ($5F),Y     
.,B0FF D0 08    BNE $B109       NOT SAME FIRST LETTER
.,B101 A5 46    LDA $46         SAME SECOND LETTER?
.,B103 C8       INY             
.,B104 D1 5F    CMP ($5F),Y     
.,B106 F0 7D    BEQ $B185       YES, SAME VARIABLE NAME
.,B108 88       DEY             NO, BUMP TO NEXT NAME
.,B109 18       CLC             
.,B10A A5 5F    LDA $5F         
.,B10C 69 07    ADC #$07        
.,B10E 90 E1    BCC $B0F1       
.,B110 E8       INX             
.,B111 D0 DC    BNE $B0EF       ...ALWAYS

                                *** CHECK IF (A) IS ASCII LETTER A-Z
                                RETURN CARRY = 1 IF A-Z
                                             = 0 IF NOT

                                <<<NOTE FASTER AND SHORTER CODE:    >>>
                                <<<    CMP #'Z'+1  COMPARE HI END
                                <<<    BCS .1      ABOVE A-Z
                                <<<    CMP #'A'    COMPARE LO END
                                <<<    RTS         C=0 IF LO, C=1 IF A-Z
                                <<<.1  CLC         C=0 IF HI
                                <<<    RTS
.,B113 C9 41    CMP #$41        COMPARE LO END
.,B115 90 05    BCC $B11C       C=0 IF LOW
.,B117 E9 5B    SBC #$5B        PREPARE HI END TEST
.,B119 38       SEC             TEST HI END, RESTORING (A)
.,B11A E9 A5    SBC #$A5        C=0 IF LO, C=1 IF A-Z
.,B11C 60       RTS             

                                *** VARIABLE NOT FOUND, SO MAKE ONE
.,B11D 68       PLA             LOOK AT RETURN ADDRESS ON STACK TO
.,B11E 48       PHA             SEE IF CALLED FROM FRM.VARIABLE
.,B11F C9 2A    CMP #$2A        
.,B121 D0 05    BNE $B128       NO
.,B123 A9 13    LDA #$13        YES, CALLED FROM FRM.VARIABLE
.,B125 A0 BF    LDY #$BF        POINT TO A CONSTANT ZERO
.,B127 60       RTS             NEW VARIABLE USED IN EXPRESSION = 0

                                *** MAKE A NEW SIMPLE VARIABLE
                                MOVE ARRAYS UP 7 BYTES TO MAKE ROOM FOR NEW VARIABLE
                                ENTER 7-BYTE VARIABLE DATA IN THE HOLE
.,B128 A5 45    LDA $45
.,B12A A4 46    LDY $46
.,B12C C9 54    CMP #$54
.,B12E D0 0B    BNE $B13B
.,B130 C0 C9    CPY #$C9
.,B132 F0 EF    BEQ $B123
.,B134 C0 49    CPY #$49
.,B136 D0 03    BNE $B13B
.,B138 4C 08 AF JMP $AF08
.,B13B C9 53    CMP #$53
.,B13D D0 04    BNE $B143
.,B13F C0 54    CPY #$54
.,B141 F0 F5    BEQ $B138
.,B143 A5 2F    LDA $2F         SET UP CALL TO BLTU TO
.,B145 A4 30    LDY $30         TO MOVE FROM ARYTAB THRU STREND-1
.,B147 85 5F    STA $5F         7 BYTES HIGHER
.,B149 84 60    STY $60         
.,B14B A5 31    LDA $31         
.,B14D A4 32    LDY $32         
.,B14F 85 5A    STA $5A         
.,B151 84 5B    STY $5B         
.,B153 18       CLC             
.,B154 69 07    ADC #$07        
.,B156 90 01    BCC $B159       
.,B158 C8       INY             
.,B159 85 58    STA $58         
.,B15B 84 59    STY $59         
.,B15D 20 B8 A3 JSR $A3B8       MOVE ARRAY BLOCK UP
.,B160 A5 58    LDA $58         STORE NEW START OF ARRAYS
.,B162 A4 59    LDY $59         
.,B164 C8       INY             
.,B165 85 2F    STA $2F         
.,B167 84 30    STY $30         
.,B169 A0 00    LDY #$00        
.,B16B A5 45    LDA $45         FIRST CHAR OF NAME
.,B16D 91 5F    STA ($5F),Y     
.,B16F C8       INY             
.,B170 A5 46    LDA $46         SECOND CHAR OF NAME
.,B172 91 5F    STA ($5F),Y     
.,B174 A9 00    LDA #$00        SET FIVE-BYTE VALUE TO 0
.,B176 C8       INY             
.,B177 91 5F    STA ($5F),Y     
.,B179 C8       INY             
.,B17A 91 5F    STA ($5F),Y     
.,B17C C8       INY             
.,B17D 91 5F    STA ($5F),Y     
.,B17F C8       INY             
.,B180 91 5F    STA ($5F),Y     
.,B182 C8       INY             
.,B183 91 5F    STA ($5F),Y     

                                *** PUT ADDRESS OF VALUE OF VARIABLE IN VARPNT AND Y,A
.,B185 A5 5F    LDA $5F         LOWTR POINTS AT NAME OF VARIABLE,
.,B187 18       CLC             SO ADD 2 TO GET TO VALUE
.,B188 69 02    ADC #$02        
.,B18A A4 60    LDY $60         
.,B18C 90 01    BCC $B18F       
.,B18E C8       INY
.,B18F 85 47    STA $47         ADDRESS IN VARPNT AND Y,A
.,B191 84 48    STY $48         
.,B193 60       RTS             

                                *** COMPUTE ADDRESS OF FIRST VALUE IN ARRAY
                                ARYPNT = (LOWTR) + #DIMS*2 + 5
.,B194 A5 0B    LDA $0B         GET # OF DIMENSIONS

.,B196 0A       ASL             #DIMS*2 (SIZE OF EACH DIM IN 2 BYTES)
.,B197 69 05    ADC #$05        + 5 (2 FOR NAME, 2 FOR OFFSET TO NEXT
                                ARRAY, AND 1 FOR #DIMS
.,B199 65 5F    ADC $5F         ADDRESS OF TH IS ARRAY IN ARYTAB
.,B19B A4 60    LDY $60         
.,B19D 90 01    BCC $B1A0       
.,B19F C8       INY             
.,B1A0 85 58    STA $58         ADDRESS OF FIRST VALUE IN ARRAY
.,B1A2 84 59    STY $59         
.,B1A4 60       RTS             

.:B1A5 90 80 00 00 00           -32768 IN FLOATING POINT

.,B1AA 20 BF B1 JSR $B1BF
.,B1AD A5 64    LDA $64
.,B1AF A4 65    LDY $65
.,B1B1 60       RTS

                                *** EVALUATE NUMERIC FORMULA AT TXTPTR
                                CONVERTING RESULT TO INTEGER 0 <= X <= 32767
                                IN FAC+3,4
.,B1B2 20 73 00 JSR $0073       
.,B1B5 20 9E AD JSR $AD9E       
.,B1B8 20 8D AD JSR $AD8D

                                *** CONVERT FAC TO INTEGER
                                MUST BE POSITIVE AND LESS THAN 32768
.,B1BB A5 66    LDA $66         ERROR IF -
.,B1BD 30 0D    BMI $B1CC       

                                *** CONVERT FAC TO INTEGER
                                MUST BE -32767 <= FAC <= 32767
.,B1BF A5 61    LDA $61         EXPONENT OF VALUE IN FAC
.,B1C1 C9 90    CMP #$90        ABS(VALUE) < 32768?
.,B1C3 90 09    BCC $B1CE       YES, OK FOR INTEGER
.,B1C5 A9 A5    LDA #$A5        NO; NEXT FEW LINES ARE SUPPOSED TO
.,B1C7 A0 B1    LDY #$B1        ALLOW -32768 ($8000)
.,B1C9 20 5B BC JSR $BC5B
.,B1CC D0 7A    BNE $B248       ILLEGAL QUANTITY
.,B1CE 4C 9B BC JMP $BC9B       CONVERT TO INTEGER

                                *** LOCATE ARRAY ELEMENT OR CREATE AN ARRAY

                                *** PARSE THE SUBSCRIPT LIST
.,B1D1 A5 0C    LDA $0C         YES
.,B1D3 05 0E    ORA $0E         SET HIGH BIT IF %
.,B1D5 48       PHA             SAVE VALTYP AND DIMFLG ON STACK
.,B1D6 A5 0D    LDA $0D         
.,B1D8 48       PHA             
.,B1D9 A0 00    LDY #$00        COUNT # DIMENSIONS IN Y-REG
.,B1DB 98       TYA             SAVE #DIMS ON STACK
.,B1DC 48       PHA             
.,B1DD A5 46    LDA $46         SAVE VARIABLE NAME ON STACK
.,B1DF 48       PHA             
.,B1E0 A5 45    LDA $45         
.,B1E2 48       PHA             
.,B1E3 20 B2 B1 JSR $B1B2       EVALUATE SUBSCRIPT AS INTEGER
.,B1E6 68       PLA             RESTORE VARIABLE NAME
.,B1E7 85 45    STA $45         
.,B1E9 68       PLA             
.,B1EA 85 46    STA $46         
.,B1EC 68       PLA             RESTORE # DIMS TO Y-REG
.,B1ED A8       TAY             
.,B1EE BA       TSX             COPY VALTYP AND DIMFLG ON STACK
.,B1EF BD 02 01 LDA $0102,X     TO LEAVE ROOM FOR THE SUBSCRIPT
.,B1F2 48       PHA             
.,B1F3 BD 01 01 LDA $0101,X     
.,B1F6 48       PHA             
.,B1F7 A5 64    LDA $64         GET SUBSCRIPT VALUE AND PLACE IN THE
.,B1F9 9D 02 01 STA $0102,X     STACK WHERE VALTYP &amp; DIMFLG WERE
.,B1FC A5 65    LDA $65         
.,B1FE 9D 01 01 STA $0101,X     
.,B201 C8       INY             COUNT THE SUBSCRIPT
.,B202 20 79 00 JSR $0079       NEXT CHAR
.,B205 C9 2C    CMP #$2C        
.,B207 F0 D2    BEQ $B1DB       COMMA, PARSE ANOTHER SUBSCRIPT
.,B209 84 0B    STY $0B         NO MORE SUBSCRIPTS, SAVE #
.,B20B 20 F7 AE JSR $AEF7       NOW NEED ")"
.,B20E 68       PLA             RESTORE VALTYPE AND DIMFLG
.,B20F 85 0D    STA $0D         
.,B211 68       PLA             
.,B212 85 0E    STA $0E         
.,B214 29 7F    AND #$7F        ISOLATE DIMFLG
.,B216 85 0C    STA $0C         

                                *** SEARCH ARRAY TABLE FOR THIS ARRAY NAME
.,B218 A6 2F    LDX $2F         (A,X) = START OF ARRAY TABLE
.,B21A A5 30    LDA $30         
.,B21C 86 5F    STX $5F         USE LOWTR FOR RUNNING POINTER
.,B21E 85 60    STA $60         
.,B220 C5 32    CMP $32         DID WE REACH THE END OF ARRAYS YET?
.,B222 D0 04    BNE $B228       NO, KEEP SEARCHING
.,B224 E4 31    CPX $31         
.,B226 F0 39    BEQ $B261       YES, THIS IS A NEW ARRAY NAME
.,B228 A0 00    LDY #$00        POINT AT 1ST CHAR OF ARRAY NAME
.,B22A B1 5F    LDA ($5F),Y     GET 1ST CHAR OF NAME
.,B22C C8       INY             POINT AT 2ND CHAR
.,B22D C5 45    CMP $45         1ST CHAR SAME?
.,B22F D0 06    BNE $B237       NO, MOVE TO NEXT ARRAY
.,B231 A5 46    LDA $46         YES, TRY 2ND CHAR
.,B233 D1 5F    CMP ($5F),Y     SAME?
.,B235 F0 16    BEQ $B24D       YES, ARRAY FOUND
.,B237 C8       INY             POINT AT OFFSET TO NEXT ARRAY
.,B238 B1 5F    LDA ($5F),Y     ADD OFFSET TO RUNNING POINTER
.,B23A 18       CLC             
.,B23B 65 5F    ADC $5F         
.,B23D AA       TAX             
.,B23E C8       INY             
.,B23F B1 5F    LDA ($5F),Y     
.,B241 65 60    ADC $60         
.,B243 90 D7    BCC $B21C       ...ALWAYS

                                *** ERROR:  BAD SUBSCRIPTS
.,B245 A2 12    LDX #$12        
.:B247 2C       .BYTE $2C       TRICK TO SKIP NEXT LINE

                                *** ERROR:  ILLEGAL QUANTITY
.,B248 A2 0E    LDX #$0E        
.,B24A 4C 37 A4 JMP $A437       

                                *** FOUND THE ARRAY
.,B24D A2 13    LDX #$13        SET UP FOR REDIM'D ARRAY ERROR
.,B24F A5 0C    LDA $0C         CALLED FROM "DIM" STATEMENT?
.,B251 D0 F7    BNE $B24A       YES, ERROR
.,B253 20 94 B1 JSR $B194       SET (ARYPNT) = ADDR OF FIRST ELEMENT
.,B256 A5 0B    LDA $0B         COMPARE NUMBER OF DIMENSIONS
.,B258 A0 04    LDY #$04        
.,B25A D1 5F    CMP ($5F),Y     
.,B25C D0 E7    BNE $B245       NOT SAME, SUBSCRIPT ERROR
.,B25E 4C EA B2 JMP $B2EA       

                                *** CREATE A NEW ARRAY, UNLESS CALLED FROM GETARYPT
.,B261 20 94 B1 JSR $B194       PUT ADDR OF 1ST ELEMENT IN ARYPNT
.,B264 20 08 A4 JSR $A408       MAKE SURE ENOUGH MEMORY LEFT
.,B267 A0 00    LDY #$00        POINT Y-REG AT VARIABLE NAME SLOT
.,B269 84 72    STY $72         START SIZE COMPUTATION
.,B26B A2 05    LDX #$05        ASSUME 5-BYTES PER ELEMENT
.,B26D A5 45    LDA $45         STUFF VARIABLE NAME IN ARRAY
.,B26F 91 5F    STA ($5F),Y     
.,B271 10 01    BPL $B274       NOT INTEGER ARRAY
.,B273 CA       DEX             INTEGER ARRAY, DECR. SIZE TO 4-BYTES
.,B274 C8       INY             POINT Y-REG AT NEXT CHAR OF NAME
.,B275 A5 46    LDA $46         REST OF ARRAY NAME
.,B277 91 5F    STA ($5F),Y     
.,B279 10 02    BPL $B27D       REAL ARRAY, STICK WITH SIZE = 5 BYTES
.,B27B CA       DEX             INTEGER OR STRING ARRAY, ADJUST SIZE
.,B27C CA       DEX             TO INTEGER=3, STRING=2 BYTES
.,B27D 86 71    STX $71         STORE LOW-BYTE OF ARRAY ELEMENT SIZE
.,B27F A5 0B    LDA $0B         STORE NUMBER OF DIMENSIONS
.,B281 C8       INY             IN 5TH BYTE OF ARRAY
.,B282 C8       INY             
.,B283 C8       INY             
.,B284 91 5F    STA ($5F),Y     
.,B286 A2 0B    LDX #$0B        DEFAULT DIMENSION = 11 ELEMENTS
.,B288 A9 00    LDA #$00        FOR HI-BYTE OF DIMENSION IF DEFAULT
.,B28A 24 0C    BIT $0C         DIMENSIONED ARRAY?
.,B28C 50 08    BVC $B296       NO, USE DEFAULT VALUE
.,B28E 68       PLA             GET SPECIFIED DIM IN A,X
.,B28F 18       CLC             # ELEMENTS IS 1 LARGER THAN
.,B290 69 01    ADC #$01        DIMENSION VALUE
.,B292 AA       TAX             
.,B293 68       PLA             
.,B294 69 00    ADC #$00        
.,B296 C8       INY             ADD THIS DIMENSION TO ARRAY DESCRIPTOR
.,B297 91 5F    STA ($5F),Y     
.,B299 C8       INY             
.,B29A 8A       TXA             
.,B29B 91 5F    STA ($5F),Y     
.,B29D 20 4C B3 JSR $B34C       MULTIPLY THIS
                                DIMENSION BY RUNNING SIZE
                                ((LOWTR)) * (STRNG2) --> A,X
.,B2A0 86 71    STX $71         STORE RUNNING SIZE IN STRNG2
.,B2A2 85 72    STA $72         
.,B2A4 A4 22    LDY $22         RETRIEVE Y SAVED BY MULTIPLY.SUBSCRIPT
.,B2A6 C6 0B    DEC $0B         COUNT DOWN # DIMS
.,B2A8 D0 DC    BNE $B286       LOOP TILL DONE

                                NOW A,X HAS TOTAL # BYTES OF ARRAY ELEMENTS
.,B2AA 65 59    ADC $59         COMPUTE ADDRESS OF END OF THIS ARRAY
.,B2AC B0 5D    BCS $B30B       ...TOO LARGE, ERROR
.,B2AE 85 59    STA $59         
.,B2B0 A8       TAY             
.,B2B1 8A       TXA             
.,B2B2 65 58    ADC $58         
.,B2B4 90 03    BCC $B2B9       
.,B2B6 C8       INY             
.,B2B7 F0 52    BEQ $B30B       ...TOO LARGE, ERROR
.,B2B9 20 08 A4 JSR $A408       MAKE SURE THERE IS ROOM UP TO Y,A
.,B2BC 85 31    STA $31         THERE IS ROOM SO SAVE NEW END OF TABLE
.,B2BE 84 32    STY $32         AND ZERO THE ARRAY
.,B2C0 A9 00    LDA #$00        
.,B2C2 E6 72    INC $72         PREPARE FOR FAST ZEROING LOOP
.,B2C4 A4 71    LDY $71         # BYTES MOD 256
.,B2C6 F0 05    BEQ $B2CD       FULL PAGE
.,B2C8 88       DEY             CLEAR PAGE FULL
.,B2C9 91 58    STA ($58),Y     
.,B2CB D0 FB    BNE $B2C8       
.,B2CD C6 59    DEC $59         POINT TO NEXT PAGE
.,B2CF C6 72    DEC $72         COUNT THE PAGES
.,B2D1 D0 F5    BNE $B2C8       STILL MORE TO CLEAR
.,B2D3 E6 59    INC $59         RECOVER LAST DEC, POINT AT 1ST ELEMENT
.,B2D5 38       SEC             
.,B2D6 A5 31    LDA $31         COMPUTE OFFSET TO END OF ARRAYS
.,B2D8 E5 5F    SBC $5F         AND STORE IN ARRAY DESCRIPTOR
.,B2DA A0 02    LDY #$02        
.,B2DC 91 5F    STA ($5F),Y     
.,B2DE A5 32    LDA $32         
.,B2E0 C8       INY             
.,B2E1 E5 60    SBC $60         
.,B2E3 91 5F    STA ($5F),Y     
.,B2E5 A5 0C    LDA $0C         WAS THIS CALLED FROM "DIM" STATEMENT?
.,B2E7 D0 62    BNE $B34B       YES, WE ARE FINISHED
.,B2E9 C8       INY             NO, NOW NEED TO FIND THE ELEMENT

                                *** FIND SPECIFIED ARRAY ELEMENT
                                (LOWTR),Y POINTS AT # OF DIMS IN ARRAY DESCRIPTOR
                                THE SUBSCRIPTS ARE ALL ON THE STACK AS INTEGERS
.,B2EA B1 5F    LDA ($5F),Y     GET # OF DIMENSIONS
.,B2EC 85 0B    STA $0B         
.,B2EE A9 00    LDA #$00        ZERO SUBSCRIPT ACCUMULATOR
.,B2F0 85 71    STA $71         
.,B2F2 85 72    STA $72         
.,B2F4 C8       INY             
.,B2F5 68       PLA             PULL NEXT SUBSCRIPT FROM STACK
.,B2F6 AA       TAX             SAVE IN FAC+3,4
.,B2F7 85 64    STA $64         AND COMPARE WITH DIMENSIONED SIZE
.,B2F9 68       PLA             
.,B2FA 85 65    STA $65         
.,B2FC D1 5F    CMP ($5F),Y     
.,B2FE 90 0E    BCC $B30E       SUBSCRIPT NOT TOO LARGE
.,B300 D0 06    BNE $B308       SUBSCRIPT IS TOO LARGE
.,B302 C8       INY             CHECK LOW-BYTE OF SUBSCRIPT
.,B303 8A       TXA             
.,B304 D1 5F    CMP ($5F),Y     
.,B306 90 07    BCC $B30F       NOT TOO LARGE

.,B308 4C 45 B2 JMP $B245       BAD SUBSCRIPTS ERROR
.,B30B 4C 35 A4 JMP $A435       MEM FULL ERROR

.,B30E C8       INY             BUMP POINTER INTO DESCRIPTOR
.,B30F A5 72    LDA $72         BYPASS MULTIPLICATION IF VALUE SO
.,B311 05 71    ORA $71         FAR = 0
.,B313 18       CLC             
.,B314 F0 0A    BEQ $B320       IT IS ZERO SO FAR
.,B316 20 4C B3 JSR $B34C       NOT ZERO, SO MULTIPLY
.,B319 8A       TXA             ADD CURRENT SUBSCRIPT
.,B31A 65 64    ADC $64
.,B31C AA       TAX             
.,B31D 98       TYA
.,B31E A4 22    LDY $22         RETRIEVE Y SAVED BY MULTIPLY.SUBSCRIPT
.,B320 65 65    ADC $65         FINISH ADDING CURRENT SUBSCRIPT
.,B322 86 71    STX $71         STORE ACCUMULATED OFFSET
.,B324 C6 0B    DEC $0B         LAST SUBSCRIPT YET?
.,B326 D0 CA    BNE $B2F2       NO, LOOP TILL DONE
.,B328 85 72    STA $72         YES, NOW MULTIPLY BE ELEMENT SIZE
.,B32A A2 05    LDX #$05        START WITH SIZE = 5
.,B32C A5 45    LDA $45         DETERMINE VARIABLE TYPE
.,B32E 10 01    BPL $B331       NOT INTEGER
.,B330 CA       DEX             INTEGER, BACK DOWN SIZE TO 4 BYTES
.,B331 A5 46    LDA $46         DISCRIMINATE BETWEEN REAL AND STR
.,B333 10 02    BPL $B337       IT IS REAL
.,B335 CA       DEX             SIZE = 3 IF STRING, =2 IF INTEGER
.,B336 CA       DEX             
.,B337 86 28    STX $28         SET UP MULTIPLIER
.,B339 A9 00    LDA #$00        HI-BYTE OF MULTIPLIER
.,B33B 20 55 B3 JSR $B355       (STRNG2) BY ELEMENT SIZE
.,B33E 8A       TXA             ADD ACCUMULATED OFFSET
.,B33F 65 58    ADC $58         TO ADDRESS OF 1ST ELEMENT
.,B341 85 47    STA $47         TO GET ADDRESS OF SPECIFIED ELEMENT
.,B343 98       TYA             
.,B344 65 59    ADC $59         
.,B346 85 48    STA $48         
.,B348 A8       TAY             RETURN WITH ADDR IN VARPNT
.,B349 A5 47    LDA $47         AND IN Y,A
.,B34B 60       RTS             

                                *** MULTIPLY (STRNG2) BY ((LOWTR),Y)
                                *** LEAVING PRODUCT IN A,X.
                                (HI-BYTE ALSO IN Y.)
                                USED ONLY BY ARRAY SUBSCRIPT ROUTINES
.,B34C 84 22    STY $22         SAVE Y-REG
.,B34E B1 5F    LDA ($5F),Y     GET MULTIPLIER
.,B350 85 28    STA $28         SAVE IN RESULT+2,3
.,B352 88       DEY             
.,B353 B1 5F    LDA ($5F),Y     

.,B355 85 29    STA $29         LOW BYTE OF MULTIPLIER
.,B357 A9 10    LDA #$10        MULTIPLY 16 BITS
.,B359 85 5D    STA $5D         
.,B35B A2 00    LDX #$00        PRODUCT = 0 INITIALLY
.,B35D A0 00    LDY #$00        
.,B35F 8A       TXA             DOUBLE PRODUCT
.,B360 0A       ASL             LOW BYTE
.,B361 AA       TAX             
.,B362 98       TYA             HIGH BYTE
.,B363 2A       ROL             IF TOO LARGE, SET CARRY
.,B364 A8       TAY             
.,B365 B0 A4    BCS $B30B       TOO LARGE, "MEM FULL ERROR"
.,B367 06 71    ASL $71         NEXT BIT OF MUTLPLICAND
.,B369 26 72    ROL $72         INTO CARRY
.,B36B 90 0B    BCC $B378       BIT=0, DON'T NEED TO ADD
.,B36D 18       CLC             BIT=1, ADD INTO PARTIAL PRODUCT
.,B36E 8A       TXA             
.,B36F 65 28    ADC $28         
.,B371 AA       TAX             
.,B372 98       TYA             
.,B373 65 29    ADC $29         
.,B375 A8       TAY             
.,B376 B0 93    BCS $B30B       TOO LARGE, "MEM FULL ERROR"
.,B378 C6 5D    DEC $5D         16-BITS YET?
.,B37A D0 E3    BNE $B35F       NO, KEEP SHUFFLING
.,B37C 60       RTS             YES, PRODUCT IN Y,X AND A,X

                                *** "FRE" FUNCTION
                                COLLECTS GARBAGE AND RETURNS # BYTES OF MEMORY LEFT
.,B37D A5 0D    LDA $0D         LOOK AT VALUE OF ARGUMENT
.,B37F F0 03    BEQ $B384       =0 MEANS REAL, =$FF MEANS STRING
.,B381 20 A6 B6 JSR $B6A6       STRING, SO SET IT FREE IS TEMP
.,B384 20 26 B5 JSR $B526       COLLECT ALL THE GARBAGE IN SIGHT
.,B387 38       SEC             COMPUTE SPACE BETWEEN ARRAYS AND
.,B388 A5 33    LDA $33         STRING TEMP AREA
.,B38A E5 31    SBC $31         
.,B38C A8       TAY             
.,B38D A5 34    LDA $34         
.,B38F E5 32    SBC $32         FREE SPACE IN Y,A
                                FALL INTO GIVAYF TO FLOAT THE VALUE
                                NOTE THAT VALUES OVER 32767 WILL RETURN AS NEGATIVE

                                *** FLOAT THE SIGNED INTEGER IN A,Y
.,B391 A2 00    LDX #$00        MARK FAC VALUE TYPE REAL
.,B393 86 0D    STX $0D         
.,B395 85 62    STA $62         SAVE VALUE FROM A,Y IN MANTISSA
.,B397 84 63    STY $63         
.,B399 A2 90    LDX #$90        SET EXPONENT TO 2^16
.,B39B 4C 44 BC JMP $BC44       CONVERT TO SIGNED FP

                                *** "POS" FUNCTION
                                RETURNS CURRENT LINE POSITION FROM MON.CH
.,B39E 38       SEC
.,B39F 20 F0 FF JSR $FFF0

                                *** FLOAT (Y) INTO FAC, GIVING VALUE 0-255
.,B3A2 A9 00    LDA #$00        MSB = 0
.,B3A4 F0 EB    BEQ $B391       ...ALWAYS

                                *** CHECK FOR DIRECT OR RUNNING MODE
                                *** GIVING ERROR IF DIRECT MODE
.,B3A6 A6 3A    LDX $3A         =$FF IF DIRECT MODE
.,B3A8 E8       INX             MAKES $FF INTO ZERO
.,B3A9 D0 A0    BNE $B34B       RETURN IF RUNNING MODE
.,B3AB A2 15    LDX #$15        DIRECT MODE, GIVE ERROR
.:B3AD 2C       .BYTE $2C       TRICK TO SKIP NEXT 2 BYTES

.,B3AE A2 1B    LDX #$1B        UNDEFINDED FUNCTION ERROR
.,B3B0 4C 37 A4 JMP $A437       

                                *** "DEF" STATEMENT
.,B3B3 20 E1 B3 JSR $B3E1       PARSE "FN", FUNCTION NAME
.,B3B6 20 A6 B3 JSR $B3A6       ERROR IF IN DIRECT MODE
.,B3B9 20 FA AE JSR $AEFA       NEED "("
.,B3BC A9 80    LDA #$80        FLAG PTRGET THAT CALLED FROM "DEF FN"
.,B3BE 85 10    STA $10         ALLOW ONLY SIMPLE FP VARIABLE FOR ARG
.,B3C0 20 8B B0 JSR $B08B       GET PNTR TO ARGUMENT
.,B3C3 20 8D AD JSR $AD8D       MUST BE NUMERIC
.,B3C6 20 F7 AE JSR $AEF7       MUST HAVE ")" NOW
.,B3C9 A9 B2    LDA #$B2        NOW NEED "="
.,B3CB 20 FF AE JSR $AEFF       OR ELSE SYNTAX ERROR
.,B3CE 48       PHA             SAVE CHAR AFTER "="
.,B3CF A5 48    LDA $48         SAVE PNTR TO ARGUMENT
.,B3D1 48       PHA             
.,B3D2 A5 47    LDA $47         
.,B3D4 48       PHA             
.,B3D5 A5 7B    LDA $7B         SAVE TXTPTR
.,B3D7 48       PHA             
.,B3D8 A5 7A    LDA $7A         
.,B3DA 48       PHA             
.,B3DB 20 F8 A8 JSR $A8F8       SCAN TO NEXT STATEMENT
.,B3DE 4C 4F B4 JMP $B44F       STORE ABOVE 5 BYTES IN "VALUE"

                                *** COMMON ROUTINE FOR "DEFFN" AND "FN", TO
                                *** PARSE "FN" AND THE FUNCTION NAME
.,B3E1 A9 A5    LDA #$A5        MUST NOW SEE "FN" TOKEN
.,B3E3 20 FF AE JSR $AEFF       OR ELSE SYNTAX ERROR
.,B3E6 09 80    ORA #$80        SET SIGN BIT ON 1ST CHAR OF NAME,
.,B3E8 85 10    STA $10         MAKING $C0 < SUBFLG < $DB
.,B3EA 20 92 B0 JSR $B092       WHICH TELLS PTRGET WHO CALLED
.,B3ED 85 4E    STA $4E         FOUND VALID FUNCTION NAME, SO
.,B3EF 84 4F    STY $4F         SAVE ADDRESS
.,B3F1 4C 8D AD JMP $AD8D       MUST BE NUMERIC

                                *** "FN" FUNCTION CALL
.,B3F4 20 E1 B3 JSR $B3E1       PARSE "FN", FUNCTION NAME
.,B3F7 A5 4F    LDA $4F         STACK FUNCTION ADDRESS
.,B3F9 48       PHA             IN CASE OF A NESTED FN CALL
.,B3FA A5 4E    LDA $4E         
.,B3FC 48       PHA             
.,B3FD 20 F1 AE JSR $AEF1       MUST NOW HAVE "(EXPRESSION)"
.,B400 20 8D AD JSR $AD8D       MUST BE NUMERIC EXPRESSION
.,B403 68       PLA             GET FUNCTION ADDRESS BACK
.,B404 85 4E    STA $4E         
.,B406 68       PLA             
.,B407 85 4F    STA $4F         
.,B409 A0 02    LDY #$02        POINT AT ADD OF ARGUMENT VARIABLE
.,B40B B1 4E    LDA ($4E),Y     
.,B40D 85 47    STA $47         
.,B40F AA       TAX             
.,B410 C8       INY             
.,B411 B1 4E    LDA ($4E),Y     
.,B413 F0 99    BEQ $B3AE       UNDEFINED FUNCTION
.,B415 85 48    STA $48         
.,B417 C8       INY             Y=4 NOW
.,B418 B1 47    LDA ($47),Y     SAVE OLD VALUE OF ARGUMENT VARIABLE
.,B41A 48       PHA             ON STACK, IN CASE ALSO USED AS
.,B41B 88       DEY             A NORMAL VARIABLE!
.,B41C 10 FA    BPL $B418       
.,B41E A4 48    LDY $48         (Y,X)= ADDRESS, STORE FAC IN VARIABLE
.,B420 20 D4 BB JSR $BBD4       
.,B423 A5 7B    LDA $7B         REMEMBER TXTPTR AFTER FN CALL
.,B425 48       PHA             
.,B426 A5 7A    LDA $7A         
.,B428 48       PHA             
.,B429 B1 4E    LDA ($4E),Y     Y=0 FROM MOVMF
.,B42B 85 7A    STA $7A         POINT TO FUNCTION DEF'N
.,B42D C8       INY             
.,B42E B1 4E    LDA ($4E),Y     
.,B430 85 7B    STA $7B         
.,B432 A5 48    LDA $48         SAVE ADDRESS OF ARGUMENT VARIABLE
.,B434 48       PHA             
.,B435 A5 47    LDA $47         
.,B437 48       PHA             
.,B438 20 8A AD JSR $AD8A       EVALUATE THE FUNCTION EXPRESSION
.,B43B 68       PLA             GET ADDRESS OF ARGUMENT VARIABLE
.,B43C 85 4E    STA $4E         AND SAVE IT
.,B43E 68       PLA             
.,B43F 85 4F    STA $4F         
.,B441 20 79 00 JSR $0079       MUST BE AT ":" OR EOL
.,B444 F0 03    BEQ $B449       WE ARE
.,B446 4C 08 AF JMP $AF08       WE ARE NOT, SLYNTAX ERROR
.,B449 68       PLA             RETRIEVE TXTPTR AFTER "FN" CALL
.,B44A 85 7A    STA $7A         
.,B44C 68       PLA             
.,B44D 85 7B    STA $7B         
                                STACK NOW HAS 5-BYTE VALUE
                                OF THE ARGUMENT VARIABLE,
                                AND FNCNAM POINTS AT THE VARIABLE

                                *** STORE FIVE BYTES FROM STACK AT (FNCNAM)
.,B44F A0 00    LDY #$00        
.,B451 68       PLA             
.,B452 91 4E    STA ($4E),Y     
.,B454 68       PLA             
.,B455 C8       INY             
.,B456 91 4E    STA ($4E),Y     
.,B458 68       PLA             
.,B459 C8       INY             
.,B45A 91 4E    STA ($4E),Y     
.,B45C 68       PLA             
.,B45D C8       INY             
.,B45E 91 4E    STA ($4E),Y     
.,B460 68       PLA             
.,B461 C8       INY             
.,B462 91 4E    STA ($4E),Y     
.,B464 60       RTS             

                                *** "STR$" FUNCTION
.,B465 20 8D AD JSR $AD8D       EXPRESSION MUST BE NUMERIC
.,B468 A0 00    LDY #$00        START STRING AT STACK-1 ($00FF)
                                SO STRLIT CAN DIFFRENTIATE STR$ CALLS
.,B46A 20 DF BD JSR $BDDF       CONVERT FAC TO STRING
.,B46D 68       PLA             POP RETURN OFF STACK
.,B46E 68       PLA             
.,B46F A9 FF    LDA #$FF        POINT TO STACK-1
.,B471 A0 00    LDY #$00        (WHICH=0)
.,B473 F0 12    BEQ $B487       ...ALWAYS, CREATE DESC &amp; MOVE STRING

                                GET SPACE AND MAKE DESCRIPTOR FOR STRING WHOSE
                                ADDRESS IS IN FAC+3,4 AND WHOSE LENGTH IS IN A-REG
.,B475 A6 64    LDX $64         Y,X = STRING ADDRESS
.,B477 A4 65    LDY $65         
.,B479 86 50    STX $50         
.,B47B 84 51    STY $51         

                                GET SPACE AND MAKE DESCRIPTOR FOR STRING WHOSE
                                ADDRESS IS IN Y,X AND WHOSE LENGTH IS IN A-REG
.,B47D 20 F4 B4 JSR $B4F4       A HOLDS LENGTH
.,B480 86 62    STX $62         SAVE DESCRIPTOR IN FAC
.,B482 84 63    STY $63         ---FAC--- --FAC+1-- --FAC+2--
.,B484 85 61    STA $61         <LENGTH>  <ADDR-LO> <ADDR-HI>
.,B486 60       RTS

                                BUILD A DESCRIPTOR FOR STRING STARTING AT Y,A
                                AND TERMINATED BY $00 OR QUOTATION MARK
                                RETURN WITH DESCRIPTOR IN A TEMPORARY
                                AND ADDRESS OF DESCRIPTOR IN FAC+3,4
.,B487 A2 22    LDX #$22        SET UP LITERAL SCAN TO STOP ON
.,B489 86 07    STX $07         QUOTATION MARK OR $00
.,B48B 86 08    STX $08         

                                BUILD A DESCRIPTOR FOR STRING STARTING AT Y,A
                                AND TERMINATED BY $00, (CHARAC), OR (ENDCHR)
                                RETURN WITH DESCRIPTOR IN A TEMPORARY
                                AND ADDRESS OF DESCRIPTOR IN FAC+3,4
.,B48D 85 6F    STA $6F         SAVE ADDRESS OF STRING
.,B48F 84 70    STY $70         
.,B491 85 62    STA $62         ...AGAIN
.,B493 84 63    STY $63         
.,B495 A0 FF    LDY #$FF        
.,B497 C8       INY             FIND END OF STRING
.,B498 B1 6F    LDA ($6F),Y     NEXT STRING CHAR
.,B49A F0 0C    BEQ $B4A8       END OF STRING
.,B49C C5 07    CMP $07         ALTERNATE TERMINATOR # 1?
.,B49E F0 04    BEQ $B4A4       YES
.,B4A0 C5 08    CMP $08         ALTERNATE TERMINATOR # 2?
.,B4A2 D0 F3    BNE $B497       NO, KEEP SCANNING
.,B4A4 C9 22    CMP #$22        IS STRING ENDED WITH QUOTE MARK?
.,B4A6 F0 01    BEQ $B4A9       YES, C=1 TO INCLUDE " IN STRING
.,B4A8 18       CLC             
.,B4A9 84 61    STY $61         SAVE LENGTH
.,B4AB 98       TYA             
.,B4AC 65 6F    ADC $6F         COMPUTE ADDRESS OF END OF STRING
.,B4AE 85 71    STA $71         (OF 00 BYTE, OR JUST AFTER ")
.,B4B0 A6 70    LDX $70         
.,B4B2 90 01    BCC $B4B5       
.,B4B4 E8       INX             
.,B4B5 86 72    STX $72         
.,B4B7 A5 70    LDA $70         WHERE DOES THE STRING START?
.,B4B9 F0 04    BEQ $B4BF       PAGE 0, MUST BE FROM STR$ FUNCTION
.,B4BB C9 02    CMP #$02        PAGE 2?
.,B4BD D0 0B    BNE $B4CA       NO, NOT PAGE 0 OR 2
.,B4BF 98       TYA             LENGTH OF STRING
.,B4C0 20 75 B4 JSR $B475       MAKE SPACE FOR STRING
.,B4C3 A6 6F    LDX $6F         
.,B4C5 A4 70    LDY $70         
.,B4C7 20 88 B6 JSR $B688       MOVE IT IN

                                STORE DESCRIPTOR IN TEMPORARY DESCRIPTOR STACK
                                THE DESCRIPTOR IS NOW IN FAC, FAC+1, FAC+2
                                PUT ADDRESS OF TEMP DESCRIPTOR IN FAC+3,4
.,B4CA A6 16    LDX $16         POINTER TO NEXT TEMP STRING SLOT
.,B4CC E0 22    CPX #$22        MAX OF 3 TEMP STRINGS
.,B4CE D0 05    BNE $B4D5       ROOM FOR ANOTHER ONE
.,B4D0 A2 19    LDX #$19        TOO MANY, FORMULA TOO COMPLEX
.,B4D2 4C 37 A4 JMP $A437       

.,B4D5 A5 61    LDA $61         COPY TEMP DESCRIPTOR INTO TEMP STACK
.,B4D7 95 00    STA $00,X       
.,B4D9 A5 62    LDA $62         
.,B4DB 95 01    STA $01,X       
.,B4DD A5 63    LDA $63         
.,B4DF 95 02    STA $02,X       
.,B4E1 A0 00    LDY #$00        
.,B4E3 86 64    STX $64         ADDRESS OF TEMP DESCRIPTOR
.,B4E5 84 65    STY $65         IN Y,X AND FAC+3,4
.,B4E7 84 70    STY $70
.,B4E9 88       DEY             Y=$FF
.,B4EA 84 0D    STY $0D         FLAG (FAC ) AS STRING
.,B4EC 86 17    STX $17         INDEX OF LAST POINTER
.,B4EE E8       INX             UPDATE FOR NEXT TEMP ENTRY
.,B4EF E8       INX             
.,B4F0 E8       INX             
.,B4F1 86 16    STX $16         
.,B4F3 60       RTS             

                                MAKE SPACE FOR STRING AT BOTTOM OF STRING SPACE
                                (A)=# BYTES SPACE TO MAKE
                                RETURN WITH (A) SAME,
                                       AND Y,X = ADDRESS OF SPACE ALLOCATED
.,B4F4 46 0F    LSR $0F         CLEAR SIGNBIT OF FLAG
.,B4F6 48       PHA             A HOLDS LENGTH
.,B4F7 49 FF    EOR #$FF        GET -LENGTH
.,B4F9 38       SEC             
.,B4FA 65 33    ADC $33         COMPUTE STARTING ADDRESS OF SPACE
.,B4FC A4 34    LDY $34         FOR THE STRING
.,B4FE B0 01    BCS $B501       
.,B500 88       DEY             
.,B501 C4 32    CPY $32         SEE IF FITS IN REMAINING MEMORY
.,B503 90 11    BCC $B516       NO, TRY GARBAGE
.,B505 D0 04    BNE $B50B       YES, IT FITS
.,B507 C5 31    CMP $31         HAVE TO CHECK LOWER BYTES
.,B509 90 0B    BCC $B516       NOT ENUF ROOM YET
.,B50B 85 33    STA $33         THERE IS ROOM SO SAVE NEW FRETOP
.,B50D 84 34    STY $34         
.,B50F 85 35    STA $35         
.,B511 84 36    STY $36         
.,B513 AA       TAX             ADDR IN Y,X
.,B514 68       PLA             LENGTH IN A
.,B515 60       RTS             
.,B516 A2 10    LDX #$10        
.,B518 A5 0F    LDA $0F         GARBAGE DONE YET?
.,B51A 30 B6    BMI $B4D2       YES, MEMORY IS REALLY FULL
.,B51C 20 26 B5 JSR $B526       NO, TRY COLLECTING NOW
.,B51F A9 80    LDA #$80        FLAG THAT COLLECTED GARBAGE ALREADY
.,B521 85 0F    STA $0F         
.,B523 68       PLA             GET STRING LENGTH AGAIN
.,B524 D0 D0    BNE $B4F6       ...ALWAYS

                                SHOVE ALL REFERENCED STRINGS AS HIGH AS POSSIBLE
                                IN MEMORY (AGAINST HIMEM)
                                FREEING UP SPACE BELOW STRING AREA DOWN TO STREND.
.,B526 A6 37    LDX $37         COLLECT FROM TOP DOWN
.,B528 A5 38    LDA $38         
.,B52A 86 33    STX $33         ONE PASS THROUGH ALL VARS
.,B52C 85 34    STA $34         FOR EACH ACTIVE STRING!
.,B52E A0 00    LDY #$00        
.,B530 84 4F    STY $4F         FLAG IN CASE NO STRINGS TO COLLECT
.,B532 84 4E    STY $4E
.,B534 A5 31    LDA $31         
.,B536 A6 32    LDX $32         
.,B538 85 5F    STA $5F         
.,B53A 86 60    STX $60         

                                START BY COLLECTING TEMPORARIES
.,B53C A9 19    LDA #$19        
.,B53E A2 00    LDX #$00        
.,B540 85 22    STA $22         
.,B542 86 23    STX $23         
.,B544 C5 16    CMP $16         FINISHED WITH TEMPS YET?
.,B546 F0 05    BEQ $B54D       YES, NOW DO SIMPLE VARIABLES
.,B548 20 C7 B5 JSR $B5C7       DO A TEMP
.,B54B F0 F7    BEQ $B544       ...ALWAYS

                                NOW COLLECT SIMPLE VARIABLES
.,B54D A9 07    LDA #$07        LENGTH OF EACH VARIABLE IS 7 BYTES
.,B54F 85 53    STA $53         
.,B551 A5 2D    LDA $2D         START AT BEGINNING OF VARTAB
.,B553 A6 2E    LDX $2E         
.,B555 85 22    STA $22         
.,B557 86 23    STX $23         
.,B559 E4 30    CPX $30         FINISHED WITH SIMPLE VARIABLES?
.,B55B D0 04    BNE $B561       NO
.,B55D C5 2F    CMP $2F         MAYBE, CHECK LO-BYTE
.,B55F F0 05    BEQ $B566       YES, NOW DO ARRAYS
.,B561 20 BD B5 JSR $B5BD       
.,B564 F0 F3    BEQ $B559       ...ALWAYS

                                NOW COLLECT ARRAY VARIABLES
.,B566 85 58    STA $58         
.,B568 86 59    STX $59         
.,B56A A9 03    LDA #$03        DESCRIPTORS IN ARRAYS ARE 3-BYTES EACH
.,B56C 85 53    STA $53         
.,B56E A5 58    LDA $58         COMPARE TO END OF ARRAYS
.,B570 A6 59    LDX $59         
.,B572 E4 32    CPX $32         FINISHED WITH ARRAYS YET?
.,B574 D0 07    BNE $B57D       NOT YET
.,B576 C5 31    CMP $31         MAYBE, CHECK LO-BYTE
.,B578 D0 03    BNE $B57D       NOT FINISHED YET
.,B57A 4C 06 B6 JMP $B606       FINISHED
.,B57D 85 22    STA $22         SET UP PNTR TO START OF ARRAY
.,B57F 86 23    STX $23         
.,B581 A0 00    LDY #$00        POINT AT NAME OF ARRAY
.,B583 B1 22    LDA ($22),Y     
.,B585 AA       TAX             1ST LETTER OF NAME IN X-REG
.,B586 C8       INY             
.,B587 B1 22    LDA ($22),Y     
.,B589 08       PHP             STATUS FROM SECOND LETTER OF NAME
.,B58A C8       INY             
.,B58B B1 22    LDA ($22),Y     OFFSET TO NEXT ARRAY
.,B58D 65 58    ADC $58         (CARRY ALWAYS CLEAR)
.,B58F 85 58    STA $58         CALCULATE START OF NEXT ARRAY
.,B591 C8       INY             
.,B592 B1 22    LDA ($22),Y     HI-BYTE OF OFFSET
.,B594 65 59    ADC $59         
.,B596 85 59    STA $59         
.,B598 28       PLP             GET STATUS FROM 2ND CHAR OF NAME
.,B599 10 D3    BPL $B56E       NOT A STRING ARRAY
.,B59B 8A       TXA             SET STATUS WITH 1ST CHAR OF NAME
.,B59C 30 D0    BMI $B56E       NOT A STRING ARRAY
.,B59E C8       INY             
.,B59F B1 22    LDA ($22),Y     # OF DIMENSIONS FOR THIS ARRAY
.,B5A1 A0 00    LDY #$00        
.,B5A3 0A       ASL             PREAMBLE SIZE = 2*#DIMS + 5
.,B5A4 69 05    ADC #$05        
.,B5A6 65 22    ADC $22         MAKE INDEX POINT AT FIRST ELEMENT
.,B5A8 85 22    STA $22         IN THE ARRAY
.,B5AA 90 02    BCC $B5AE       
.,B5AC E6 23    INC $23         
.,B5AE A6 23    LDX $23         STEP THRU EACH STRING IN THIS ARRAY
.,B5B0 E4 59    CPX $59         ARRAY DONE?
.,B5B2 D0 04    BNE $B5B8       NO, PROCESS NEXT ELEMENT
.,B5B4 C5 58    CMP $58         MAYBE, CHECK LO-BYTE
.,B5B6 F0 BA    BEQ $B572       YES, MOVE TO NEXT ARRAY
.,B5B8 20 C7 B5 JSR $B5C7       PROCESS THE ARRAY
.,B5BB F0 F3    BEQ $B5B0       ...ALWAYS

                                PROCESS A SIMPLE VARIABLE
.,B5BD B1 22    LDA ($22),Y     LOOK AT 1ST CHAR OF NAME
.,B5BF 30 35    BMI $B5F6       NOT A STRING VARIABLE
.,B5C1 C8       INY             
.,B5C2 B1 22    LDA ($22),Y     LOOK AT 2ND CHAR OF NAME
.,B5C4 10 30    BPL $B5F6       NOT A STRING VARIABLE
.,B5C6 C8       INY             

                                IF STRING IS NOT EMPTY, CHECK IF IT IS HIGHEST
.,B5C7 B1 22    LDA ($22),Y     GET LENGTH OF STRING
.,B5C9 F0 2B    BEQ $B5F6       IGNORE STRING IF LENGTH IS ZERO
.,B5CB C8       INY             
.,B5CC B1 22    LDA ($22),Y     GET ADDRESS OF STRING
.,B5CE AA       TAX             
.,B5CF C8       INY             
.,B5D0 B1 22    LDA ($22),Y     
.,B5D2 C5 34    CMP $34         CHECK IF ALREADY COLLECTED
.,B5D4 90 06    BCC $B5DC       NO, BELOW FRETOP
.,B5D6 D0 1E    BNE $B5F6       YES, ABOVE FRETOP
.,B5D8 E4 33    CPX $33         MAYBE, CHECK LO-BYTE
.,B5DA B0 1A    BCS $B5F6       YES, ABOVE FRETOP
.,B5DC C5 60    CMP $60         ABOVE HIGHEST STRING FOUND?
.,B5DE 90 16    BCC $B5F6       NO, IGNORE FOR NOW
.,B5E0 D0 04    BNE $B5E6       YES, THIS IS THE NEW HIGHEST
.,B5E2 E4 5F    CPX $5F         MAYBE, TRY LO-BYTE
.,B5E4 90 10    BCC $B5F6       NO, IGNORE FOR NOW
.,B5E6 86 5F    STX $5F         MAKE THIS THE HIGHEST STRING
.,B5E8 85 60    STA $60         
.,B5EA A5 22    LDA $22         SAVE ADDRESS OF DESCRIPTOR TOO
.,B5EC A6 23    LDX $23         
.,B5EE 85 4E    STA $4E         
.,B5F0 86 4F    STX $4F         
.,B5F2 A5 53    LDA $53         
.,B5F4 85 55    STA $55         

                                ADD (DSCLEN) TO PNTR IN INDEX
                                RETURN WITH Y=0, PNTR ALSO IN X,A
.,B5F6 A5 53    LDA $53         BUMP TO NEXT VARIABLE
.,B5F8 18       CLC             
.,B5F9 65 22    ADC $22         
.,B5FB 85 22    STA $22         
.,B5FD 90 02    BCC $B601       
.,B5FF E6 23    INC $23         

.,B601 A6 23    LDX $23         
.,B603 A0 00    LDY #$00        
.,B605 60       RTS             

                                FOUND HIGHEST NON-EMPTY STRING, SO MOVE IT
                                TO TOP AND GO BACK FOR ANOTHER
.,B606 A5 4F    LDA $4F
.,B608 05 4E    ORA $4E
.,B60A F0 F5    BEQ $B601
.,B60C A5 55    LDA $55
.,B60E 29 04    AND #$04
.,B610 4A       LSR
.,B611 A8       TAY
.,B612 85 55    STA $55
.,B614 B1 4E    LDA ($4E),Y
.,B616 65 5F    ADC $5F
.,B618 85 5A    STA $5A
.,B61A A5 60    LDA $60
.,B61C 69 00    ADC #$00
.,B61E 85 5B    STA $5B
.,B620 A5 33    LDA $33
.,B622 A6 34    LDX $34
.,B624 85 58    STA $58
.,B626 86 59    STX $59
.,B628 20 BF A3 JSR $A3BF
.,B62B A4 55    LDY $55
.,B62D C8       INY
.,B62E A5 58    LDA $58
.,B630 91 4E    STA ($4E),Y
.,B632 AA       TAX
.,B633 E6 59    INC $59
.,B635 A5 59    LDA $59
.,B637 C8       INY
.,B638 91 4E    STA ($4E),Y
.,B63A 4C 2A B5 JMP $B52A

                                *** CONCATENATE TWO STRINGS
.,B63D A5 65    LDA $65         SAVE ADDRESS OF FIRST DESCRIPTOR
.,B63F 48       PHA             
.,B640 A5 64    LDA $64         
.,B642 48       PHA             
.,B643 20 83 AE JSR $AE83       GET SECOND STRING ELEMENT
.,B646 20 8F AD JSR $AD8F       MUST BE A STRING
.,B649 68       PLA             RECOVER ADDRES OF 1ST DESCRIPTOR
.,B64A 85 6F    STA $6F         
.,B64C 68       PLA             
.,B64D 85 70    STA $70         
.,B64F A0 00    LDY #$00        
.,B651 B1 6F    LDA ($6F),Y     ADD LENGTHS, GET CONCATENATED SIZE
.,B653 18       CLC             
.,B654 71 64    ADC ($64),Y     
.,B656 90 05    BCC $B65D       OK IF < $100
.,B658 A2 17    LDX #$17        
.,B65A 4C 37 A4 JMP $A437       
.,B65D 20 75 B4 JSR $B475       GET SPACE FOR CONCATENATED STRINGS
.,B660 20 7A B6 JSR $B67A       MOVE 1ST STRING
.,B663 A5 50    LDA $50         
.,B665 A4 51    LDY $51         
.,B667 20 AA B6 JSR $B6AA       
.,B66A 20 8C B6 JSR $B68C       MOVE 2ND STRING
.,B66D A5 6F    LDA $6F         
.,B66F A4 70    LDY $70         
.,B671 20 AA B6 JSR $B6AA       
.,B674 20 CA B4 JSR $B4CA       SET UP DESCRIPTOR
.,B677 4C B8 AD JMP $ADB8       FINISH EXPRESSION

                                GET STRING DESCRIPTOR POINTED AT BY (STRNG1)
                                AND MOVE DESCRIBED STRING TO (FRESPC)
.,B67A A0 00    LDY #$00        
.,B67C B1 6F    LDA ($6F),Y     
.,B67E 48       PHA             LENGTH
.,B67F C8       INY             
.,B680 B1 6F    LDA ($6F),Y     
.,B682 AA       TAX             PUT STRING POINTER IN X,Y
.,B683 C8       INY             
.,B684 B1 6F    LDA ($6F),Y     
.,B686 A8       TAY             
.,B687 68       PLA             RETRIEVE LENGTH

                                MOVE STRING AT (Y,X) WITH LENGTH (A)
                                TO DESTINATION WHOSE ADDRESS IS IN FRESPC,FRESPC+1
.,B688 86 22    STX $22         PUT POINTER IN INDEX
.,B68A 84 23    STY $23         
.,B68C A8       TAY             LENGTH TO Y-REG
.,B68D F0 0A    BEQ $B699       IF LENGTH IS ZERO, FINISHED
.,B68F 48       PHA             SAVE LENGTH ON STACK
.,B690 88       DEY             MOVE BYTES FROM (INDEX) TO (FRESPC)
.,B691 B1 22    LDA ($22),Y     
.,B693 91 35    STA ($35),Y     
.,B695 98       TYA             TEST IF ANY LEFT TO MOVE
.,B696 D0 F8    BNE $B690       YES, KEEP MOVING
.,B698 68       PLA             NO, FINISHED.  GET LENGTH
.,B699 18       CLC             AND ADD TO FRESPC, SO
.,B69A 65 35    ADC $35         FRESPC POINTS TO NEXT HIGHER
.,B69C 85 35    STA $35         BYTE.  (USED BY CONCATENATION)
.,B69E 90 02    BCC $B6A2       
.,B6A0 E6 36    INC $36         
.,B6A2 60       RTS             

                                IF (FAC) IS A TEMPORARY STRING, RELEASE DESCRIPTOR
.,B6A3 20 8F AD JSR $AD8F       LAST RESULT A STRING?

                                IF STRING DESCRIPTOR POINTED TO BY FAC+3,4 IS
                                A TEMPORARY STRING, RELEASE IT.
.,B6A6 A5 64    LDA $64         GET DESCRIPTOR POINTER
.,B6A8 A4 65    LDY $65         

                                IF STRING DESCRIPTOR WHOSE ADDRESS IS IN Y,A IS
                                A TEMPORARY STRING, RELEASE IT.
.,B6AA 85 22    STA $22         SAVE THE ADDRESS OF THE DESCRIPTOR
.,B6AC 84 23    STY $23         
.,B6AE 20 DB B6 JSR $B6DB       FREE DESCRIPTOR IF IT IS TEMPORARY
.,B6B1 08       PHP             REMEMBER IF TEMP
.,B6B2 A0 00    LDY #$00        POINT AT LENGTH OF STRING
.,B6B4 B1 22    LDA ($22),Y     
.,B6B6 48       PHA             SAVE LENGTH ON STACK
.,B6B7 C8       INY             
.,B6B8 B1 22    LDA ($22),Y     
.,B6BA AA       TAX             GET ADDRESS OF STRING IN Y,X
.,B6BB C8       INY             
.,B6BC B1 22    LDA ($22),Y     
.,B6BE A8       TAY             
.,B6BF 68       PLA             LENGTH IN A
.,B6C0 28       PLP             RETRIEVE STATUS, Z=1 IF TEMP
.,B6C1 D0 13    BNE $B6D6       NOT A TEMPORARY STRING
.,B6C3 C4 34    CPY $34         IS IT THE LOWEST STRING?
.,B6C5 D0 0F    BNE $B6D6       NO
.,B6C7 E4 33    CPX $33         
.,B6C9 D0 0B    BNE $B6D6       NO
.,B6CB 48       PHA             YES, PUSH LENGTH AGAIN
.,B6CC 18       CLC             RECOVER THE SPACE USED BY
.,B6CD 65 33    ADC $33         THE STRING
.,B6CF 85 33    STA $33         
.,B6D1 90 02    BCC $B6D5       
.,B6D3 E6 34    INC $34         
.,B6D5 68       PLA             RETRIEVE LENGTH AGAIN
.,B6D6 86 22    STX $22         ADDRESS OF STRING IN Y,X
.,B6D8 84 23    STY $23         LENGTH OF STRING IN A-REG
.,B6DA 60       RTS             

                                RELEASE TEMPORARY DESCRIPTOR IF Y,A = LASTPT
.,B6DB C4 18    CPY $18         COMPARE Y,A TO LATEST TEMP
.,B6DD D0 0C    BNE $B6EB       NOT SAME ONE, CANNOT RELEASE
.,B6DF C5 17    CMP $17         
.,B6E1 D0 08    BNE $B6EB       NOT SAME ONE, CANNOT RELEASE
.,B6E3 85 16    STA $16         UPDATE TEMPT FOR NEXT TEMP
.,B6E5 E9 03    SBC #$03        BACK OFF LASTPT
.,B6E7 85 17    STA $17         
.,B6E9 A0 00    LDY #$00        NOW Y,A POINTS TO TOP TEMP
.,B6EB 60       RTS             Z=0 IF NOT TEMP, Z=1 IF TEMP

                                *** "CHR$" FUNCTION
.,B6EC 20 A1 B7 JSR $B7A1       CONVERT ARGUMENT TO BYTE IN X
.,B6EF 8A       TXA             
.,B6F0 48       PHA             SAVE IT
.,B6F1 A9 01    LDA #$01        GET SPACE FOR STRING OF LENGTH 1
.,B6F3 20 7D B4 JSR $B47D       
.,B6F6 68       PLA             RECALL THE CHARACTER
.,B6F7 A0 00    LDY #$00        PUT IN STRING
.,B6F9 91 62    STA ($62),Y     
.,B6FB 68       PLA             POP RETURN ADDRESS
.,B6FC 68       PLA             
.,B6FD 4C CA B4 JMP $B4CA       MAKE IT A TEMPORARY STRING

                                *** "LEFT$" FUNCTION
.,B700 20 61 B7 JSR $B761       
.,B703 D1 50    CMP ($50),Y     COMPARE 1ST PARAMETER TO LENGTH
.,B705 98       TYA             Y=A=0
.,B706 90 04    BCC $B70C       1ST PARAMETER SMALLER, USE IT
.,B708 B1 50    LDA ($50),Y     1ST IS LONGER, USE STRING LENGTH
.,B70A AA       TAX             IN X-REG
.,B70B 98       TYA             Y=A=0 AGAIN
.,B70C 48       PHA             PUSH LEFT END OF SUBSTRING
.,B70D 8A       TXA             
.,B70E 48       PHA             PUSH LENGTH OF SUBSTRING
.,B70F 20 7D B4 JSR $B47D       MAKE ROOM FOR STRING OF (A) BYTES
.,B712 A5 50    LDA $50         RELEASE PARAMETER STRING IF TEMP
.,B714 A4 51    LDY $51         
.,B716 20 AA B6 JSR $B6AA       
.,B719 68       PLA             GET LENGTH OF SUBSTRING
.,B71A A8       TAY             IN Y-REG
.,B71B 68       PLA             GET LEFT END OF SUBSTRING
.,B71C 18       CLC             ADD TO POINTER TO STRING
.,B71D 65 22    ADC $22         
.,B71F 85 22    STA $22         
.,B721 90 02    BCC $B725       
.,B723 E6 23    INC $23         
.,B725 98       TYA             LENGTH
.,B726 20 8C B6 JSR $B68C       COPY STRING INTO SPACE
.,B729 4C CA B4 JMP $B4CA       ADD TO TEMPS

                                *** "RIGHT$" FUNCTION
.,B72C 20 61 B7 JSR $B761       
.,B72F 18       CLC             COMPUTE LENGTH-WIDTH OF SUBSTRING
.,B730 F1 50    SBC ($50),Y     TO GET STARTING POINT IN STRING
.,B732 49 FF    EOR #$FF        
.,B734 4C 06 B7 JMP $B706       JOIN LEFT$

                                *** "MID$" FUNCTION
.,B737 A9 FF    LDA #$FF        FLAG WHETHER 2ND PARAMETER
.,B739 85 65    STA $65         
.,B73B 20 79 00 JSR $0079       SEE IF ")" YET
.,B73E C9 29    CMP #$29        
.,B740 F0 06    BEQ $B748       YES, NO 2ND PARAMETER
.,B742 20 FD AE JSR $AEFD       NO, MUST HAVE COMMA
.,B745 20 9E B7 JSR $B79E       GET 2ND PARAM IN X-REG
.,B748 20 61 B7 JSR $B761       
.,B74B F0 4B    BEQ $B798
.,B74D CA       DEX             1ST PARAMETER - 1
.,B74E 8A       TXA             
.,B74F 48       PHA             
.,B750 18       CLC             
.,B751 A2 00    LDX #$00        
.,B753 F1 50    SBC ($50),Y     
.,B755 B0 B6    BCS $B70D       
.,B757 49 FF    EOR #$FF        
.,B759 C5 65    CMP $65         USE SMALLER OF TWO
.,B75B 90 B1    BCC $B70E       
.,B75D A5 65    LDA $65         
.,B75F B0 AD    BCS $B70E       ...ALWAYS

                                *** COMMON SETUP ROUTINE FOR LEFT$, RIGHT$, MID$
                                REQUIRE ")"; POP RETURN ADRS, GET DESCRIPTOR
                                ADDRESS, GET 1ST PARAMETER OF COMMAND
.,B761 20 F7 AE JSR $AEF7       REQUIRE ")"
.,B764 68       PLA             SAVE RETURN ADDRESS
.,B765 A8       TAY             IN Y-REG AND LENGTH
.,B766 68       PLA             
.,B767 85 55    STA $55         
.,B769 68       PLA             POP PREVIOUS RETURN ADDRESS
.,B76A 68       PLA             (FROM GOROUT).
.,B76B 68       PLA             RETRIEVE 1ST PARAMETER
.,B76C AA       TAX             
.,B76D 68       PLA             GET ADDRESS OF STRING DESCRIPTOR
.,B76E 85 50    STA $50         
.,B770 68       PLA             
.,B771 85 51    STA $51         
.,B773 A5 55    LDA $55         RESTORE RETURN ADDRESS
.,B775 48       PHA             
.,B776 98       TYA             
.,B777 48       PHA             
.,B778 A0 00    LDY #$00        
.,B77A 8A       TXA             GET 1ST PARAMETER IN A-REG
.,B77B 60       RTS             

                                *** "LEN" FUNCTION
.,B77C 20 82 B7 JSR $B782       GET LENTGH IN Y-REG, MAKE FAC NUMERIC
.,B77F 4C A2 B3 JMP $B3A2       FLOAT Y-REG INTO FAC

                                IF LAST RESULT IS A TEMPORARY STRING, FREE IT
                                MAKE VALTYP NUMERIC, RETURN LENGTH IN Y-REG
.,B782 20 A3 B6 JSR $B6A3       IF LAST RESULT IS A STRING, FREE IT
.,B785 A2 00    LDX #$00        MAKE VALTYP NUMERIC
.,B787 86 0D    STX $0D         
.,B789 A8       TAY             LENGTH OF STRING TO Y-REG
.,B78A 60       RTS             

                                *** "ASC" FUNCTION
.,B78B 20 82 B7 JSR $B782       GET STRING, GET LENGTH IN Y-REG
.,B78E F0 08    BEQ $B798       ERROR IF LENGTH 0
.,B790 A0 00    LDY #$00        
.,B792 B1 22    LDA ($22),Y     GET 1ST CHAR OF STRING
.,B794 A8       TAY             
.,B795 4C A2 B3 JMP $B3A2       FLOAT Y-REG INTO FAC

.,B798 4C 48 B2 JMP $B248       ILLEGAL QUANTITY ERROR

                                *** SCAN TO NEXT CHARACTER AND CONVERT EXPRESSION
                                *** TO SINGLE BYTE IN X-REG
.,B79B 20 73 00 JSR $0073       

                                *** EVALUATE EXPRESSION AT TXTPTR, AND
                                *** CONVERT IT TO SINGLE BYTE IN X-REG
.,B79E 20 8A AD JSR $AD8A       

                                *** CONVERT (FAC) TO SINGLE BYTE INTEGER IN X-REG
.,B7A1 20 B8 B1 JSR $B1B8       CONVERT IF IN RANGE -32767 TO +32767
.,B7A4 A6 64    LDX $64         HI-BYTE MUST BE ZERO
.,B7A6 D0 F0    BNE $B798       VALUE > 255, ERROR
.,B7A8 A6 65    LDX $65         VALUE IN X-REG
.,B7AA 4C 79 00 JMP $0079       GET NEXT CHAR IN A-REG

                                *** "VAL" FUNCTION
.,B7AD 20 82 B7 JSR $B782       GET POINTER TO STRING IN INDEX
.,B7B0 D0 03    BNE $B7B5       LENGTH NON-ZERO
.,B7B2 4C F7 B8 JMP $B8F7       RETURN 0 IF LENGTH=0
.,B7B5 A6 7A    LDX $7A         SAVE CURRENT TXTPTR
.,B7B7 A4 7B    LDY $7B         
.,B7B9 86 71    STX $71         
.,B7BB 84 72    STY $72         
.,B7BD A6 22    LDX $22         
.,B7BF 86 7A    STX $7A         POINT TXTPTR TO START OF STRING
.,B7C1 18       CLC             
.,B7C2 65 22    ADC $22         ADD LENGTH
.,B7C4 85 24    STA $24         POINT DEST TO END OF STRING + 1
.,B7C6 A6 23    LDX $23         
.,B7C8 86 7B    STX $7B         
.,B7CA 90 01    BCC $B7CD       
.,B7CC E8       INX             
.,B7CD 86 25    STX $25         
.,B7CF A0 00    LDY #$00        SAVE BYTE THAT FOLLOWS STRING
.,B7D1 B1 24    LDA ($24),Y     ON STACK
.,B7D3 48       PHA             
.,B7D4 98       TYA             AND STORE $00 IN ITS PLACE
.,B7D5 91 24    STA ($24),Y     
                                <<< THAT CAUSES A BUG IF HIMEM = $BFFF, >>>
                                <<< BECAUSE STORING $00 AT $C000 IS NO  >>>
                                <<< USE; $C000 WILL ALWAYS BE LAST CHAR >>>
                                <<< TYPED, SO FIN WON'T TERMINATE UNTIL >>>
                                <<< IT SEES A ZERO AT $C010!            >>>
.,B7D7 20 79 00 JSR $0079       PRIME THE PUMP
.,B7DA 20 F3 BC JSR $BCF3       EVALUATE STRING
.,B7DD 68       PLA             GET BYTE THAT SHOULD FOLLOW STRING
.,B7DE A0 00    LDY #$00        AND PUT IT BACK
.,B7E0 91 24    STA ($24),Y     
                                RESTORE TXTPTR

                                *** COPY STRNG2 INTO TXTPTR
.,B7E2 A6 71    LDX $71         
.,B7E4 A4 72    LDY $72         
.,B7E6 86 7A    STX $7A         
.,B7E8 84 7B    STY $7B         
.,B7EA 60       RTS             

                                *** EVALUATE "EXP1,EXP2"
                                CONVERT EXP1 TO 16-BIT NUMBER IN LINNUM
                                CONVERT EXP2 TO 8-BIT NUMBER IN X-REG
.,B7EB 20 8A AD JSR $AD8A       
.,B7EE 20 F7 B7 JSR $B7F7       

                                *** EVALUATE ",EXPRESSION"
                                CONVERT EXPRESSION TO SINGLE BYTE IN X-REG
.,B7F1 20 FD AE JSR $AEFD       MUST HAVE COMMA FIRST
.,B7F4 4C 9E B7 JMP $B79E       CONVERT EXPRESSION TO BYTE IN X-REG

                                *** CONVERT (FAC) TO A 16-BIT VALUE IN LINNUM
.,B7F7 A5 66    LDA $66         FAC < 2^16?
.,B7F9 30 9D    BMI $B798
.,B7FB A5 61    LDA $61
.,B7FD C9 91    CMP #$91        
.,B7FF B0 97    BCS $B798       NO, ILLEGAL QUANTITY
.,B801 20 9B BC JSR $BC9B       CONVERT TO INTEGER
.,B804 A5 64    LDA $64         COPY IT INTO LINNUM
.,B806 A4 65    LDY $65         
.,B808 84 14    STY $14         TO LINNUM
.,B80A 85 15    STA $15         
.,B80C 60       RTS             

                                *** "PEEK" FUNCTION
.,B80D A5 15    LDA $15         SAVE (LINNUM) ON STACK DURING PEEK
.,B80F 48       PHA             
.,B810 A5 14    LDA $14         
.,B812 48       PHA             
.,B813 20 F7 B7 JSR $B7F7       GET ADDRESS PEEKING AT
.,B816 A0 00    LDY #$00        
.,B818 B1 14    LDA ($14),Y     TAKE A QUICK LOOK
.,B81A A8       TAY             VALUE IN Y-REG
.,B81B 68       PLA             RESTORE LINNUM FROM STACK
.,B81C 85 14    STA $14         
.,B81E 68       PLA             
.,B81F 85 15    STA $15         
.,B821 4C A2 B3 JMP $B3A2       FLOAT Y-REG INTO FAC

                                *** "POKE" STATEMENT
.,B824 20 EB B7 JSR $B7EB       GET THE ADDRESS AND VALUE
.,B827 8A       TXA             VALUE IN A,
.,B828 A0 00    LDY #$00        
.,B82A 91 14    STA ($14),Y     STORE IT AWAY,
.,B82C 60       RTS             AND THAT'S ALL FOR TODAY

                                *** "WAIT" STATEMENT
.,B82D 20 EB B7 JSR $B7EB       GET ADDRESS IN LINNUM, MASK IN X
.,B830 86 49    STX $49         SAVE MASK
.,B832 A2 00    LDX #$00        
.,B834 20 79 00 JSR $0079       ANOTHER PARAMETER?
.,B837 F0 03    BEQ $B83C       NO, USE $00 FOR EXCLUSIVE-OR
.,B839 20 F1 B7 JSR $B7F1       GET XOR-MASK
.,B83C 86 4A    STX $4A         SAVE XOR-MASK HERE
.,B83E A0 00    LDY #$00        
.,B840 B1 14    LDA ($14),Y     GET BYTE AT ADDRESS
.,B842 45 4A    EOR $4A         INVERT SPECIFIED BITS
.,B844 25 49    AND $49         SELECT SPECIFIED BITS
.,B846 F0 F8    BEQ $B840       LOOP TILL NOT 0
.,B848 60       RTS             

                                *** ADD 0.5 TO FAC
.,B849 A9 11    LDA #$11        FAC+1/2 -> FAC
.,B84B A0 BF    LDY #$BF        
.,B84D 4C 67 B8 JMP $B867       

                                *** FAC = (Y,A) - FAC
.,B850 20 8C BA JSR $BA8C       

                                *** FAC = ARG - FAC
.,B853 A5 66    LDA $66         COMPLEMENT FAC AND ADD
.,B855 49 FF    EOR #$FF        
.,B857 85 66    STA $66         
.,B859 45 6E    EOR $6E         FIX SGNCPR TOO
.,B85B 85 6F    STA $6F         
.,B85D A5 61    LDA $61         MAKE STATUS SHOW FAC EXPONENT
.,B85F 4C 6A B8 JMP $B86A       JOIN FADD

                                *** SHIFT SMALLER ARGUMENT MORE THAN 7 BITS
.,B862 20 99 B9 JSR $B999       ALIGN RADIX BY SHIFTING
.,B865 90 3C    BCC $B8A3       ...ALWAYS

                                *** FAC = (Y,A) + FAC
.,B867 20 8C BA JSR $BA8C       

                                *** FAC = ARG + FAC
.,B86A D0 03    BNE $B86F       FAC IS NON-ZERO
.,B86C 4C FC BB JMP $BBFC       FAC = 0 + ARG
.,B86F A6 70    LDX $70         
.,B871 86 56    STX $56         
.,B873 A2 69    LDX #$69        SET UP TO SHIFT ARG
.,B875 A5 69    LDA $69         EXPONENT

.,B877 A8       TAY             
.,B878 F0 CE    BEQ $B848       IF ARG=0, WE ARE FINISHED
.,B87A 38       SEC             
.,B87B E5 61    SBC $61         GET DIFFNCE OF EXP
.,B87D F0 24    BEQ $B8A3       GO ADD IF SAME EXP
.,B87F 90 12    BCC $B893       ARG HAS SMALLER EXPONENT
.,B881 84 61    STY $61         EXP HAS SMALLER EXPONENT
.,B883 A4 6E    LDY $6E         
.,B885 84 66    STY $66         
.,B887 49 FF    EOR #$FF        COMPLEMENT SHIFT COUNT
.,B889 69 00    ADC #$00        CARRY WAS SET
.,B88B A0 00    LDY #$00        
.,B88D 84 56    STY $56         
.,B88F A2 61    LDX #$61        SET UP TO SHIFT FAC
.,B891 D0 04    BNE $B897       ...ALWAYS
.,B893 A0 00    LDY #$00        
.,B895 84 70    STY $70         
.,B897 C9 F9    CMP #$F9        SHIFT MORE THAN 7 BITS?
.,B899 30 C7    BMI $B862       YES
.,B89B A8       TAY             INDEX TO # OF SHIFTS
.,B89C A5 70    LDA $70         
.,B89E 56 01    LSR $01,X       START SHIFTING...
.,B8A0 20 B0 B9 JSR $B9B0       ...COMPLETE SHIFTING
.,B8A3 24 6F    BIT $6F         DO FAC AND ARG HAVE SAME SIGNS?
.,B8A5 10 57    BPL $B8FE       YES, ADD THE MANTISSAS
.,B8A7 A0 61    LDY #$61        NO, SUBTRACT SMALLER FROM LARGER
.,B8A9 E0 69    CPX #$69        WHICH WAS ADJUSTED?
.,B8AB F0 02    BEQ $B8AF       IF ARG, DO FAC-ARG
.,B8AD A0 69    LDY #$69        IF FAC, DO ARG-FAC
.,B8AF 38       SEC             SUBTRACT SMALLER FROM LARGER (WE HOPE)
.,B8B0 49 FF    EOR #$FF        (IF EXPONENTS WERE EQUAL, WE MIGHT BE
.,B8B2 65 56    ADC $56         SUBTRACTING LARGER FROM SMALLER)
.,B8B4 85 70    STA $70         
.,B8B6 B9 04 00 LDA $0004,Y     
.,B8B9 F5 04    SBC $04,X       
.,B8BB 85 65    STA $65         
.,B8BD B9 03 00 LDA $0003,Y     
.,B8C0 F5 03    SBC $03,X       
.,B8C2 85 64    STA $64         
.,B8C4 B9 02 00 LDA $0002,Y     
.,B8C7 F5 02    SBC $02,X       
.,B8C9 85 63    STA $63         
.,B8CB B9 01 00 LDA $0001,Y     
.,B8CE F5 01    SBC $01,X       
.,B8D0 85 62    STA $62         

                                *** NORMALIZE VALUE IN FAC
.,B8D2 B0 03    BCS $B8D7       
.,B8D4 20 47 B9 JSR $B947       

.,B8D7 A0 00    LDY #$00        SHIFT UP SIGNIF DIGIT
.,B8D9 98       TYA             START A=0, COUNT SHIFTS IN A-REG
.,B8DA 18       CLC             
.,B8DB A6 62    LDX $62         LOOK AT MOST SIGNIFICANT BYTE
.,B8DD D0 4A    BNE $B929       SOME 1-BITS HERE
.,B8DF A6 63    LDX $63         HI-BYTE OF MANTISSA STILL ZERO,
.,B8E1 86 62    STX $62         SO DO A FAST 8-BIT SHUFFLE
.,B8E3 A6 64    LDX $64         
.,B8E5 86 63    STX $63         
.,B8E7 A6 65    LDX $65         
.,B8E9 86 64    STX $64         
.,B8EB A6 70    LDX $70         
.,B8ED 86 65    STX $65         
.,B8EF 84 70    STY $70         ZERO EXTENSION BYTE
.,B8F1 69 08    ADC #$08        BUMP SHIFT COUNT
.,B8F3 C9 20    CMP #$20        DONE 4 TIMES YET?
.,B8F5 D0 E4    BNE $B8DB       NO, STILL MIGHT BE SOME 1'S
                                YES, VALUE OF FAC IS ZERO

                                *** SET FAC = 0
                                (ONLY NECESSARY TO ZERO EXPONENT AND SIGN CELLS)
.,B8F7 A9 00    LDA #$00        
.,B8F9 85 61    STA $61         
.,B8FB 85 66    STA $66         
.,B8FD 60       RTS             

                                *** ADD MANTISSAS OF FAC AND ARG INTO FAC
.,B8FE 65 56    ADC $56         
.,B900 85 70    STA $70         
.,B902 A5 65    LDA $65         
.,B904 65 6D    ADC $6D         
.,B906 85 65    STA $65         
.,B908 A5 64    LDA $64         
.,B90A 65 6C    ADC $6C         
.,B90C 85 64    STA $64         
.,B90E A5 63    LDA $63         
.,B910 65 6B    ADC $6B         
.,B912 85 63    STA $63         
.,B914 A5 62    LDA $62         
.,B916 65 6A    ADC $6A         
.,B918 85 62    STA $62         
.,B91A 4C 36 B9 JMP $B936       

                                *** FINISH NORMALIZING FAC
.,B91D 69 01    ADC #$01        COUNT BITS SHIFTED
.,B91F 06 70    ASL $70         
.,B921 26 65    ROL $65         
.,B923 26 64    ROL $64         
.,B925 26 63    ROL $63         
.,B927 26 62    ROL $62         

.,B929 10 F2    BPL $B91D       UNTIL TOP BIT = 1
.,B92B 38       SEC             
.,B92C E5 61    SBC $61         ADJUST EXPONENT BY BITS SHIFTED
.,B92E B0 C7    BCS $B8F7       UNDERFLOW, RETURN ZERO
.,B930 49 FF    EOR #$FF        
.,B932 69 01    ADC #$01        2'S COMPLEMENT
.,B934 85 61    STA $61         CARRY=0 NOW

.,B936 90 0E    BCC $B946       UNLESS MANTISSA CARRIED

.,B938 E6 61    INC $61         MANTISSA CARRIED, SO SHIFT RIGHT
.,B93A F0 42    BEQ $B97E       OVERFLOW IF EXPONENT TOO BIG
.,B93C 66 62    ROR $62         
.,B93E 66 63    ROR $63         
.,B940 66 64    ROR $64         
.,B942 66 65    ROR $65         
.,B944 66 70    ROR $70         
.,B946 60       RTS             

                                *** 2'S COMPLEMENT OF FAC
.,B947 A5 66    LDA $66         
.,B949 49 FF    EOR #$FF        
.,B94B 85 66    STA $66         

                                *** 2'S COMPLEMENT OF FAC MANTISSA ONLY
.,B94D A5 62    LDA $62         
.,B94F 49 FF    EOR #$FF        
.,B951 85 62    STA $62         
.,B953 A5 63    LDA $63         
.,B955 49 FF    EOR #$FF        
.,B957 85 63    STA $63         
.,B959 A5 64    LDA $64         
.,B95B 49 FF    EOR #$FF        
.,B95D 85 64    STA $64         
.,B95F A5 65    LDA $65         
.,B961 49 FF    EOR #$FF        
.,B963 85 65    STA $65         
.,B965 A5 70    LDA $70         
.,B967 49 FF    EOR #$FF        
.,B969 85 70    STA $70         
.,B96B E6 70    INC $70         START INCREMENTING MANTISSA
.,B96D D0 0E    BNE $B97D       

                                *** INCREMENT FAC MANTISSA
.,B96F E6 65    INC $65         ADD CARRY FROM EXTRA
.,B971 D0 0A    BNE $B97D       
.,B973 E6 64    INC $64         
.,B975 D0 06    BNE $B97D       
.,B977 E6 63    INC $63         
.,B979 D0 02    BNE $B97D       
.,B97B E6 62    INC $62         
.,B97D 60       RTS             

.,B97E A2 0F    LDX #$0F        
.,B980 4C 37 A4 JMP $A437       

                                *** SHIFT 1,X THRU 5,X RIGHT
                                (A) = NEGATIVE OF SHIFT COUNT
                                (X) = POINTER TO BYTES TO BE SHIFTED
                                RETURN WITH (Y)=0, CARRY=0, EXTENSION BITS IN A-REG
.,B983 A2 25    LDX #$25        SHIFT RESULT RIGHT
.,B985 B4 04    LDY $04,X       SHIFT 8 BITS RIGHT
.,B987 84 70    STY $70         
.,B989 B4 03    LDY $03,X       
.,B98B 94 04    STY $04,X       
.,B98D B4 02    LDY $02,X       
.,B98F 94 03    STY $03,X       
.,B991 B4 01    LDY $01,X       
.,B993 94 02    STY $02,X       
.,B995 A4 68    LDY $68         $00 IF +, $FF IF -
.,B997 94 01    STY $01,X       

                                *** MAIN ENTRY TO RIGHT SHIFT SUBROUTINE
.,B999 69 08    ADC #$08        
.,B99B 30 E8    BMI $B985       STILL MORE THAN 8 BITS TO GO
.,B99D F0 E6    BEQ $B985       EXACTLY 8 MORE BITS TO GO
.,B99F E9 08    SBC #$08        UNDO ADC ABOVE
.,B9A1 A8       TAY             REMAINING SHIFT COUNT
.,B9A2 A5 70    LDA $70         
.,B9A4 B0 14    BCS $B9BA       FINISHED SHIFTING
.,B9A6 16 01    ASL $01,X       SIGN -> CARRY (SIGN EXTENSION)
.,B9A8 90 02    BCC $B9AC       SIGN +
.,B9AA F6 01    INC $01,X       PUT SIGN IN LSB
.,B9AC 76 01    ROR $01,X       RESTORE VALUE, SIGN STILL IN CARRY
.,B9AE 76 01    ROR $01,X       START RIGHT SHIFT, INSERTING SIGN

                                *** ENTER HERE FOR SHORT SHIFTS WITH NO SIGN EXTENSION
.,B9B0 76 02    ROR $02,X       
.,B9B2 76 03    ROR $03,X       
.,B9B4 76 04    ROR $04,X       
.,B9B6 6A       ROR             EXTENSION
.,B9B7 C8       INY             COUNT THE SHIFT
.,B9B8 D0 EC    BNE $B9A6       
.,B9BA 18       CLC             RETURN WITH CARRY CLEAR
.,B9BB 60       RTS             

.:B9BC 81 00 00 00 00
.:B9C1 03                       # OF COEFFICIENTS - 1
.:B9C2 7F 5E 56 CB 79           X^7 +
.:B9C7 80 13 9B 0B 64           X^5 +
.:B9CC 80 76 38 93 16           X^3 +
.:B9D1 82 38 AA 3B 20           X

.:B9D6 80 35 04 F3 34           SQR(1/2)
.:B9DB 81 35 04 F3 34           SQR(TWO)
.:B9E0 80 80 00 00 00           -1/2
.:B9E5 80 31 72 17 F8           LOG(2)


                                *** "LOG" FUNCTION
.,B9EA 20 2B BC JSR $BC2B       GET -1,0,+1 IN A-REG FOR FAC
.,B9ED F0 02    BEQ $B9F1       LOG (0) IS ILLEGAL
.,B9EF 10 03    BPL $B9F4       >0 IS OK
.,B9F1 4C 48 B2 JMP $B248       <= 0 IS NO GOOD
.,B9F4 A5 61    LDA $61         FIRST GET LOG BASE 2
.,B9F6 E9 7F    SBC #$7F        SAVE UNBIASED EXPONENT
.,B9F8 48       PHA             
.,B9F9 A9 80    LDA #$80        NORMALIZE BETWEEN .5 AND 1
.,B9FB 85 61    STA $61         
.,B9FD A9 D6    LDA #$D6        
.,B9FF A0 B9    LDY #$B9        
.,BA01 20 67 B8 JSR $B867       COMPUTE VIA SERIES OF ODD
.,BA04 A9 DB    LDA #$DB        POWERS OF
.,BA06 A0 B9    LDY #$B9        (SQR(2)X-1)/(SQR(2)X+1)
.,BA08 20 0F BB JSR $BB0F       
.,BA0B A9 BC    LDA #$BC        
.,BA0D A0 B9    LDY #$B9        
.,BA0F 20 50 B8 JSR $B850       
.,BA12 A9 C1    LDA #$C1        
.,BA14 A0 B9    LDY #$B9        
.,BA16 20 43 E0 JSR $E043       
.,BA19 A9 E0    LDA #$E0        
.,BA1B A0 B9    LDY #$B9        
.,BA1D 20 67 B8 JSR $B867       
.,BA20 68       PLA             
.,BA21 20 7E BD JSR $BD7E       ADD ORIGINAL EXPONENT
.,BA24 A9 E5    LDA #$E5        MULTIPLY BY LOG(2) TO FORM
.,BA26 A0 B9    LDY #$B9        NATURAL LOG OF X

                                *** FAC = (Y,A) * FAC
.,BA28 20 8C BA JSR $BA8C       

                                *** FAC = ARG * FAC
.,BA2B D0 03    BNE $BA30       FAC .NE. ZERO
.,BA2D 4C 8B BA JMP $BA8B       FAC = 0 * ARG = 0

.,BA30 20 B7 BA JSR $BAB7       
.,BA33 A9 00    LDA #$00        
.,BA35 85 26    STA $26         INIT PRODUCT = 0
.,BA37 85 27    STA $27         
.,BA39 85 28    STA $28         
.,BA3B 85 29    STA $29         
.,BA3D A5 70    LDA $70         
.,BA3F 20 59 BA JSR $BA59       
.,BA42 A5 65    LDA $65         
.,BA44 20 59 BA JSR $BA59       
.,BA47 A5 64    LDA $64         
.,BA49 20 59 BA JSR $BA59       
.,BA4C A5 63    LDA $63         
.,BA4E 20 59 BA JSR $BA59       
.,BA51 A5 62    LDA $62         
.,BA53 20 5E BA JSR $BA5E       
.,BA56 4C 8F BB JMP $BB8F       

                                *** MULTIPLY ARG BY (A) INTO RESULT
.,BA59 D0 03    BNE $BA5E       THIS BYTE NON-ZERO
.,BA5B 4C 83 B9 JMP $B983       (A)=0, JUST SHIFT ARG RIGHT 8

.,BA5E 4A       LSR             SHIFT BIT INTO CARRY
.,BA5F 09 80    ORA #$80        SUPPLY SENTINEL BIT
.,BA61 A8       TAY             REMAINING MULTIPLIER TO Y
.,BA62 90 19    BCC $BA7D       THIS MULTIPLIER BIT = 0
.,BA64 18       CLC             = 1, SO ADD ARG TO RESULT
.,BA65 A5 29    LDA $29         
.,BA67 65 6D    ADC $6D         
.,BA69 85 29    STA $29         
.,BA6B A5 28    LDA $28         
.,BA6D 65 6C    ADC $6C         
.,BA6F 85 28    STA $28         
.,BA71 A5 27    LDA $27         
.,BA73 65 6B    ADC $6B         
.,BA75 85 27    STA $27         
.,BA77 A5 26    LDA $26         
.,BA79 65 6A    ADC $6A         
.,BA7B 85 26    STA $26         
.,BA7D 66 26    ROR $26         SHIFT RESULT RIGHT 1
.,BA7F 66 27    ROR $27         
.,BA81 66 28    ROR $28         
.,BA83 66 29    ROR $29         
.,BA85 66 70    ROR $70         
.,BA87 98       TYA             REMAINING MULTIPLIER
.,BA88 4A       LSR             LSB INTO CARRY
.,BA89 D0 D6    BNE $BA61       IF SENTINEL STILL HERE, MULTIPLY
.,BA8B 60       RTS             8 X 32 COMPLETED

                                *** UNPACK NUMBER AT (Y,A) INTO ARG
.,BA8C 85 22    STA $22         USE INDEX FOR PNTR
.,BA8E 84 23    STY $23         
.,BA90 A0 04    LDY #$04        FIVE BYTES TO MOVE
.,BA92 B1 22    LDA ($22),Y     
.,BA94 85 6D    STA $6D         
.,BA96 88       DEY             
.,BA97 B1 22    LDA ($22),Y     
.,BA99 85 6C    STA $6C         
.,BA9B 88       DEY             
.,BA9C B1 22    LDA ($22),Y     
.,BA9E 85 6B    STA $6B         
.,BAA0 88       DEY             
.,BAA1 B1 22    LDA ($22),Y     
.,BAA3 85 6E    STA $6E         
.,BAA5 45 66    EOR $66         SET COMBINED SIGN FOR MULT/DIV
.,BAA7 85 6F    STA $6F         
.,BAA9 A5 6E    LDA $6E         TURN ON NORMALIZED INVISIBLE BIT
.,BAAB 09 80    ORA #$80        TO COMPLETE MANTISSA
.,BAAD 85 6A    STA $6A         
.,BAAF 88       DEY             
.,BAB0 B1 22    LDA ($22),Y     
.,BAB2 85 69    STA $69         EXPONENT
.,BAB4 A5 61    LDA $61         SET STATUS BITS ON FAC EXPONENT
.,BAB6 60       RTS             

                                *** ADD EXPONENTS OF ARG AND FAC
                                (CALLED BY FMULT AND FDIV)
                                ALSO CHECK FOR OVERFLOW, AND SET RESULT SIGN
.,BAB7 A5 69    LDA $69         

.,BAB9 F0 1F    BEQ $BADA       IF ARG=0, RESULT IS ZERO
.,BABB 18       CLC             
.,BABC 65 61    ADC $61         
.,BABE 90 04    BCC $BAC4       IN RANGE
.,BAC0 30 1D    BMI $BADF       OVERFLOW
.,BAC2 18       CLC             
.:BAC3 2C       .BYTE $2C       TRICK TO SKIP
.,BAC4 10 14    BPL $BADA       OVERFLOW
.,BAC6 69 80    ADC #$80        RE-BIAS
.,BAC8 85 61    STA $61         RESULT
.,BACA D0 03    BNE $BACF       
.,BACC 4C FB B8 JMP $B8FB       RESULT IS ZERO
                                <<< CRAZY TO JUMP WAY BACK THERE! >>>
                                <<< SAME IDENTICAL CODE IS BELOW! >>>
                                <<< INSTEAD OF BNE .2, JMP STA.IN.FAC.SIGN   >>>
                                <<< ONLY NEEDED BEQ .3            >>>
.,BACF A5 6F    LDA $6F         SET SIGN OF RESULT
.,BAD1 85 66    STA $66         
.,BAD3 60       RTS             

                                IF (FAC) IS POSITIVE, GIVE "OVERFLOW" ERROR
                                IF (FAC) IS NEGATIVE, SET FAC=0, POP ONE RETURN, AND RTS
                                CALLED FROM "EXP" FUNCTION
.,BAD4 A5 66    LDA $66         
.,BAD6 49 FF    EOR #$FF        
.,BAD8 30 05    BMI $BADF       ERROR IF POSITIVE #

                                *** POP RETURN ADDRESS AND SET FAC=0
.,BADA 68       PLA             
.,BADB 68       PLA             
.,BADC 4C F7 B8 JMP $B8F7       

.,BADF 4C 7E B9 JMP $B97E       

                                *** MULTIPLY FAC BY 10
.,BAE2 20 0C BC JSR $BC0C       
.,BAE5 AA       TAX             TEXT FAC EXPONENT
.,BAE6 F0 10    BEQ $BAF8       FINISHED IF FAC=0
.,BAE8 18       CLC             
.,BAE9 69 02    ADC #$02        ADD 2 TO EXPONENT GIVES (FAC)*4
.,BAEB B0 F2    BCS $BADF       OVERFLOW
.,BAED A2 00    LDX #$00        
.,BAEF 86 6F    STX $6F         
.,BAF1 20 77 B8 JSR $B877       MAKES (FAC)*5
.,BAF4 E6 61    INC $61         *2, MAKES (FAC)*10
.,BAF6 F0 E7    BEQ $BADF       OVERFLOW
.,BAF8 60       RTS             

.:BAF9 84 20 00 00 00           10


                                *** DIVIDE FAC BY 10
.,BAFE 20 0C BC JSR $BC0C       
.,BB01 A9 F9    LDA #$F9        SET UP TO PUT
.,BB03 A0 BA    LDY #$BA        10 IN FAC
.,BB05 A2 00    LDX #$00        

                                *** FAC = ARG / (Y,A)
.,BB07 86 6F    STX $6F         
.,BB09 20 A2 BB JSR $BBA2       
.,BB0C 4C 12 BB JMP $BB12       DIVIDE ARG BY FAC

                                *** FAC = (Y,A) / FAC
.,BB0F 20 8C BA JSR $BA8C       

                                *** FAC = ARG / FAC
.,BB12 F0 76    BEQ $BB8A       FAC = 0, DIVIDE BY ZERO ERROR
.,BB14 20 1B BC JSR $BC1B       
.,BB17 A9 00    LDA #$00        NEGATE FAC EXPONENT, SO
.,BB19 38       SEC             ADD.EXPONENTS FORMS DIFFERENCE
.,BB1A E5 61    SBC $61         
.,BB1C 85 61    STA $61         
.,BB1E 20 B7 BA JSR $BAB7       
.,BB21 E6 61    INC $61         
.,BB23 F0 BA    BEQ $BADF       OVERFLOW
.,BB25 A2 FC    LDX #$FC        INDEX FOR RESULT
.,BB27 A9 01    LDA #$01        SENTINEL
.,BB29 A4 6A    LDY $6A         SEE IF FAC CAN BE SUBTRACTED
.,BB2B C4 62    CPY $62         
.,BB2D D0 10    BNE $BB3F       
.,BB2F A4 6B    LDY $6B         
.,BB31 C4 63    CPY $63         
.,BB33 D0 0A    BNE $BB3F       
.,BB35 A4 6C    LDY $6C         
.,BB37 C4 64    CPY $64         
.,BB39 D0 04    BNE $BB3F       
.,BB3B A4 6D    LDY $6D         
.,BB3D C4 65    CPY $65         
.,BB3F 08       PHP             SAVE THE ANSWER, AND ALSO ROLL THE
.,BB40 2A       ROL             BIT INTO THE QUOTIENT, SENTINEL OUT
.,BB41 90 09    BCC $BB4C       NO SENTINEL, STILL NOT 8 TRIPS
.,BB43 E8       INX             8 TRIPS, STORE BYTE OF QUOTIENT
.,BB44 95 29    STA $29,X       
.,BB46 F0 32    BEQ $BB7A       32-BITS COMPLETED
.,BB48 10 34    BPL $BB7E       FINAL EXIT WHEN X=1
.,BB4A A9 01    LDA #$01        RE-START SENTINEL
.,BB4C 28       PLP             GET ANSWER, CAN FAC BE SUBTRACTED?
.,BB4D B0 0E    BCS $BB5D       YES, DO IT
.,BB4F 06 6D    ASL $6D         NO, SHIFT ARG LEFT
.,BB51 26 6C    ROL $6C         
.,BB53 26 6B    ROL $6B         
.,BB55 26 6A    ROL $6A         
.,BB57 B0 E6    BCS $BB3F       ANOTHER TRIP
.,BB59 30 CE    BMI $BB29       HAVE TO COMPARE FIRST
.,BB5B 10 E2    BPL $BB3F       ...ALWAYS
.,BB5D A8       TAY             SAVE QUOTIENT/SENTINEL BYTE
.,BB5E A5 6D    LDA $6D         SUBTRACT FAC FROM ARG ONCE
.,BB60 E5 65    SBC $65         
.,BB62 85 6D    STA $6D         
.,BB64 A5 6C    LDA $6C         
.,BB66 E5 64    SBC $64         
.,BB68 85 6C    STA $6C         
.,BB6A A5 6B    LDA $6B         
.,BB6C E5 63    SBC $63         
.,BB6E 85 6B    STA $6B         
.,BB70 A5 6A    LDA $6A         
.,BB72 E5 62    SBC $62         
.,BB74 85 6A    STA $6A         
.,BB76 98       TYA             RESTORE QUOTIENT/SENTINEL BYTE
.,BB77 4C 4F BB JMP $BB4F       GO TO SHIFT ARG AND CONTINUE

.,BB7A A9 40    LDA #$40        DO A FEW EXTENSION BITS
.,BB7C D0 CE    BNE $BB4C       ...ALWAYS

.,BB7E 0A       ASL             LEFT JUSTIFY THE EXTENSION BITS WE DID
.,BB7F 0A       ASL             
.,BB80 0A       ASL             
.,BB81 0A       ASL             
.,BB82 0A       ASL             
.,BB83 0A       ASL             
.,BB84 85 70    STA $70         
.,BB86 28       PLP             
.,BB87 4C 8F BB JMP $BB8F       

.,BB8A A2 14    LDX #$14        
.,BB8C 4C 37 A4 JMP $A437       

                                *** COPY RESULT INTO FAC MANTISSA, AND NORMALIZE
.,BB8F A5 26    LDA $26         
.,BB91 85 62    STA $62         
.,BB93 A5 27    LDA $27         
.,BB95 85 63    STA $63         
.,BB97 A5 28    LDA $28         
.,BB99 85 64    STA $64         
.,BB9B A5 29    LDA $29         
.,BB9D 85 65    STA $65         
.,BB9F 4C D7 B8 JMP $B8D7       

                                *** UNPACK (Y,A) INTO FAC
.,BBA2 85 22    STA $22         USE INDEX FOR PNTR
.,BBA4 84 23    STY $23         
.,BBA6 A0 04    LDY #$04        PICK UP 5 BYTES
.,BBA8 B1 22    LDA ($22),Y     
.,BBAA 85 65    STA $65         
.,BBAC 88       DEY             
.,BBAD B1 22    LDA ($22),Y     
.,BBAF 85 64    STA $64         
.,BBB1 88       DEY             
.,BBB2 B1 22    LDA ($22),Y     
.,BBB4 85 63    STA $63         
.,BBB6 88       DEY             
.,BBB7 B1 22    LDA ($22),Y     
.,BBB9 85 66    STA $66         FIRST BIT IS SIGN
.,BBBB 09 80    ORA #$80        SET NORMALIZED INVISIBLE BIT
.,BBBD 85 62    STA $62         
.,BBBF 88       DEY             
.,BBC0 B1 22    LDA ($22),Y     
.,BBC2 85 61    STA $61         EXPONENT
.,BBC4 84 70    STY $70         Y=0
.,BBC6 60       RTS             

                                *** ROUND FAC, STORE IN TEMP2
.,BBC7 A2 5C    LDX #$5C        PACK FAC INTO TEMP2
.:BBC9 2C       .BYTE $2C       TRICK TO BRANCH

                                *** ROUND FAC, STORE IN TEMP1
.,BBCA A2 57    LDX #$57        PACK FAC INTO TEMP1
.,BBCC A0 00    LDY #$00        HI-BYTE OF TEMP1 SAME AS TEMP2
.,BBCE F0 04    BEQ $BBD4       ...ALWAYS

                                *** ROUND FAC, AND STORE WHERE FORPNT POINTS
.,BBD0 A6 49    LDX $49         
.,BBD2 A4 4A    LDY $4A         

                                *** ROUND FAC, AND STORE AT (Y,X)
.,BBD4 20 1B BC JSR $BC1B       ROUND VALUE IN FAC USING EXTENSION
.,BBD7 86 22    STX $22         USE INDEX FOR PNTR
.,BBD9 84 23    STY $23         
.,BBDB A0 04    LDY #$04        STORING 5 PACKED BYTES
.,BBDD A5 65    LDA $65         
.,BBDF 91 22    STA ($22),Y     
.,BBE1 88       DEY             
.,BBE2 A5 64    LDA $64         
.,BBE4 91 22    STA ($22),Y     
.,BBE6 88       DEY             
.,BBE7 A5 63    LDA $63         
.,BBE9 91 22    STA ($22),Y     
.,BBEB 88       DEY             
.,BBEC A5 66    LDA $66         PACK SIGN IN TOP BIT OF MANTISSA
.,BBEE 09 7F    ORA #$7F        
.,BBF0 25 62    AND $62         
.,BBF2 91 22    STA ($22),Y     
.,BBF4 88       DEY             
.,BBF5 A5 61    LDA $61         EXPONENT
.,BBF7 91 22    STA ($22),Y     
.,BBF9 84 70    STY $70         ZERO THE EXTENSION
.,BBFB 60       RTS             

                                *** COPY ARG INTO FAC
.,BBFC A5 6E    LDA $6E         COPY SIGN
.,BBFE 85 66    STA $66         
.,BC00 A2 05    LDX #$05        MOVE 5 BYTES
.,BC02 B5 68    LDA $68,X       
.,BC04 95 60    STA $60,X       
.,BC06 CA       DEX             
.,BC07 D0 F9    BNE $BC02       
.,BC09 86 70    STX $70         ZERO EXTENSION
.,BC0B 60       RTS             

                                *** ROUND FAC AND COPY TO ARG
.,BC0C 20 1B BC JSR $BC1B       ROUND FAC USING EXTENSION
.,BC0F A2 06    LDX #$06        COPY 6 BYTES, INCLUDES SIGN
.,BC11 B5 60    LDA $60,X       
.,BC13 95 68    STA $68,X       
.,BC15 CA       DEX             
.,BC16 D0 F9    BNE $BC11       
.,BC18 86 70    STX $70         ZERO FAC EXTENSION
.,BC1A 60       RTS             

                                *** ROUND FAC USING EXTENSION BYTE
.,BC1B A5 61    LDA $61         
.,BC1D F0 FB    BEQ $BC1A       FAC = 0, RETURN
.,BC1F 06 70    ASL $70         IS FAC.EXTENSION >= 128?
.,BC21 90 F7    BCC $BC1A       NO, FINISHED

                                *** INCREMENT MANTISSA AND RE-NORMALIZE IF CARRY
.,BC23 20 6F B9 JSR $B96F       YES, INCREMENT FAC
.,BC26 D0 F2    BNE $BC1A       HIGH BYTE HAS BITS, FINISHED
.,BC28 4C 38 B9 JMP $B938       HI-BYTE=0, SO SHIFT LEFT

                                *** TEST FAC FOR ZERO AND SIGN
                                FAC > 0, RETURN +1
                                FAC = 0, RETURN  0
                                FAC < 0, RETURN -1
.,BC2B A5 61    LDA $61         CHECK SIGN OF FAC AND
.,BC2D F0 09    BEQ $BC38       RETURN -1,0,1 IN A-REG

.,BC2F A5 66    LDA $66         

.,BC31 2A       ROL             MSBIT TO CARRY
.,BC32 A9 FF    LDA #$FF        -1
.,BC34 B0 02    BCS $BC38       MSBIT = 1
.,BC36 A9 01    LDA #$01        +1
.,BC38 60       RTS             

                                *** "SGN" FUNCTION
.,BC39 20 2B BC JSR $BC2B       CONVERT FAC TO -1,0,1

                                *** CONVERT (A) INTO FAC, AS SIGNED VALUE -128 TO +127
.,BC3C 85 62    STA $62         PUT IN HIGH BYTE OF MANTISSA
.,BC3E A9 00    LDA #$00        CLEAR 2ND BYTE OF MANTISSA
.,BC40 85 63    STA $63         
.,BC42 A2 88    LDX #$88        USE EXPONENT 2^9

                                *** FLOAT UNSIGNED VALUE IN FAC+1,2
                                (X) = EXPONENT
.,BC44 A5 62    LDA $62         MSBIT=0, SET CARRY; =1, CLEAR CARRY
.,BC46 49 FF    EOR #$FF        
.,BC48 2A       ROL             

                                *** FLOAT UNSIGNED VALUE IN FAC+1,2
                                (X) = EXPONENT
                                C=0 TO MAKE VALUE NEGATIVE
                                C=1 TO MAKE VALUE POSITIVE
.,BC49 A9 00    LDA #$00        CLEAR LOWER 16-BITS OF MANTISSA
.,BC4B 85 65    STA $65         
.,BC4D 85 64    STA $64         
.,BC4F 86 61    STX $61         STORE EXPONENT
.,BC51 85 70    STA $70         CLEAR EXTENSION
.,BC53 85 66    STA $66         MAKE SIGN POSITIVE
.,BC55 4C D2 B8 JMP $B8D2       IF C=0, WILL NEGATE FAC

                                *** "ABS" FUNCTION
.,BC58 46 66    LSR $66         CHANGE SIGN TO +
.,BC5A 60       RTS             

                                *** COMPARE FAC WITH PACKED # AT (Y,A)
                                RETURN A=1,0,-1 AS (Y,A) IS <,=,> FAC
.,BC5B 85 24    STA $24         USE DEST FOR PNTR

                                *** SPECIAL ENTRY FROM "NEXT" PROCESSOR
                                "DEST" ALREADY SET UP
.,BC5D 84 25    STY $25         
.,BC5F A0 00    LDY #$00        GET EXPONENT OF COMPARAND
.,BC61 B1 24    LDA ($24),Y     
.,BC63 C8       INY             POINT AT NEXT BYTE
.,BC64 AA       TAX             EXPONENT TO X-REG
.,BC65 F0 C4    BEQ $BC2B       IF COMPARAND=0, "SIGN" COMPARES FAC
.,BC67 B1 24    LDA ($24),Y     GET HI-BYTE OF MANTISSA
.,BC69 45 66    EOR $66         COMPARE WITH FAC SIGN
.,BC6B 30 C2    BMI $BC2F       DIFFERENT SIGNS, "SIGN" GIVES ANSWER
.,BC6D E4 61    CPX $61         SAME SIGN, SO COMPARE EXPONENTS
.,BC6F D0 21    BNE $BC92       DIFFERENT, SO SUFFICIENT TEST
.,BC71 B1 24    LDA ($24),Y     SAME EXPONENT, COMPARE MANTISSA
.,BC73 09 80    ORA #$80        SET INVISIBLE NORMALIZED BIT
.,BC75 C5 62    CMP $62         
.,BC77 D0 19    BNE $BC92       NOT SAME, SO SUFFICIENT
.,BC79 C8       INY             SAME, COMPARE MORE MANTISSA
.,BC7A B1 24    LDA ($24),Y     
.,BC7C C5 63    CMP $63         
.,BC7E D0 12    BNE $BC92       NOT SAME, SO SUFFICIENT
.,BC80 C8       INY             SAME, COMPARE MORE MANTISSA
.,BC81 B1 24    LDA ($24),Y     
.,BC83 C5 64    CMP $64         
.,BC85 D0 0B    BNE $BC92       NOT SAME, SO SUFFICIENT
.,BC87 C8       INY             SAME, COMPARE REST OF MANTISSA
.,BC88 A9 7F    LDA #$7F        ARTIFICIAL EXTENSION BYTE FOR COMPARAND
.,BC8A C5 70    CMP $70         
.,BC8C B1 24    LDA ($24),Y     
.,BC8E E5 65    SBC $65         
.,BC90 F0 28    BEQ $BCBA       NUMBERS ARE EQUAL, RETURN (A)=0
.,BC92 A5 66    LDA $66         NUMBERS ARE DIFFERENT
.,BC94 90 02    BCC $BC98       FAC IS LARGER MAGNITUDE
.,BC96 49 FF    EOR #$FF        FAC IS SMALLER MAGNITUDE
                                <<<  NOTE THAT ABOVE THREE LINES CAN BE SHORTENED: >>>
                                <<<  .1  ROR              PUT CARRY INTO SIGN BIT  >>>
                                <<<      EOR FAC.SIGN     TOGGLE WITH SIGN OF FAC  >>>
.,BC98 4C 31 BC JMP $BC31       CONVERT +1 OR -1

                                *** QUICK INTEGER FUNCTION
                                CONVERTS FP VALUE IN FAC TO INTEGER VALUE
                                IN FAC+1...FAC+4, BY SHIFTING RIGHT WITH SIGN
                                EXTENSION UNTIL FRACTIONAL BITS ARE OUT.

                                THIS SUBROUTINE ASSUMES THE EXPONENT < 32.
.,BC9B A5 61    LDA $61         LOOK AT FAC EXPONENT
.,BC9D F0 4A    BEQ $BCE9       FAC=0, SO FINISHED
.,BC9F 38       SEC             GET -(NUMBER OF FRACTIONAL BITS)
.,BCA0 E9 A0    SBC #$A0        IN A-REG FOR SHIFT COUNT
.,BCA2 24 66    BIT $66         CHECK SIGN OF FAC
.,BCA4 10 09    BPL $BCAF       POSITIVE, CONTINUE
.,BCA6 AA       TAX             NEGATIVE, SO COMPLEMENT MANTISSA
.,BCA7 A9 FF    LDA #$FF        AND SET SIGN EXTENSION FOR SHIFT
.,BCA9 85 68    STA $68         
.,BCAB 20 4D B9 JSR $B94D       
.,BCAE 8A       TXA             RESTORE BIT COUNT TO A-REG
.,BCAF A2 61    LDX #$61        POINT SHIFT SUBROUTINE AT FAC
.,BCB1 C9 F9    CMP #$F9        MORE THAN 7 BITS TO SHIFT?
.,BCB3 10 06    BPL $BCBB       NO, SHORT SHIFT
.,BCB5 20 99 B9 JSR $B999       YES, USE GENERAL ROUTINE
.,BCB8 84 68    STY $68         Y=0, CLEAR SIGN EXTENSION
.,BCBA 60       RTS             

.,BCBB A8       TAY             SAVE SHIFT COUNT
.,BCBC A5 66    LDA $66         GET SIGN BIT
.,BCBE 29 80    AND #$80        
.,BCC0 46 62    LSR $62         START RIGHT SHIFT
.,BCC2 05 62    ORA $62         AND MERGE WITH SIGN
.,BCC4 85 62    STA $62         
.,BCC6 20 B0 B9 JSR $B9B0       JUMP INTO MIDDLE OF SHIFTER
.,BCC9 84 68    STY $68         Y=0, CLEAR SIGN EXTENSION
.,BCCB 60       RTS             

                                *** "INT" FUNCTION
                                USES QINT TO CONVERT (FAC) TO INTEGER FORM,
                                AND THEN REFLOATS THE INTEGER.
                                <<< A FASTER APPROACH WOULD SIMPLY CLEAR >>>
                                <<< THE FRACTIONAL BITS BY ZEROING THEM  >>>
.,BCCC A5 61    LDA $61         CHECK IF EXPONENT < 32
.,BCCE C9 A0    CMP #$A0        BECAUSE IF > 31 THERE IS NO FRACTION
.,BCD0 B0 20    BCS $BCF2       NO FRACTION, WE ARE FINISHED
.,BCD2 20 9B BC JSR $BC9B       USE GENERAL INTEGER CONVERSION
.,BCD5 84 70    STY $70         Y=0, CLEAR EXTENSION
.,BCD7 A5 66    LDA $66         GET SIGN OF VALUE
.,BCD9 84 66    STY $66         Y=0, CLEAR SIGN
.,BCDB 49 80    EOR #$80        TOGGLE ACTUAL SIGN
.,BCDD 2A       ROL             AND SAVE IN CARRY
.,BCDE A9 A0    LDA #$A0        SET EXPONENT TO 32
.,BCE0 85 61    STA $61         BECAUSE 4-BYTE INTEGER NOW
.,BCE2 A5 65    LDA $65         SAVE LOW 8-BITS OF INTEGER FORM
.,BCE4 85 07    STA $07         FOR EXP AND POWER
.,BCE6 4C D2 B8 JMP $B8D2       NORMALIZE TO FINISH CONVERSION

.,BCE9 85 62    STA $62         FAC=0, SO CLEAR ALL 4 BYTES FOR
.,BCEB 85 63    STA $63         INTEGER VERSION
.,BCED 85 64    STA $64         
.,BCEF 85 65    STA $65         
.,BCF1 A8       TAY             Y=0 TOO
.,BCF2 60       RTS             

                                *** CONVERT STRING TO FP VALUE IN FAC
                                STRING POINTED TO BY TXTPTR
                                FIRST CHAR ALREADY SCANNED BY CHRGET
                                (A) = FIRST CHAR, C=0 IF DIGIT.
.,BCF3 A0 00    LDY #$00        CLEAR WORKING AREA ($99...$A3)
.,BCF5 A2 0A    LDX #$0A        TMPEXP, EXPON, DPFLG, EXPSGN, FAC, SERLEN
.,BCF7 94 5D    STY $5D,X       
.,BCF9 CA       DEX             
.,BCFA 10 FB    BPL $BCF7       

.,BCFC 90 0F    BCC $BD0D       FIRST CHAR IS A DIGIT
.,BCFE C9 2D    CMP #$2D        CHECK FOR LEADING SIGN
.,BD00 D0 04    BNE $BD06       NOT MINUS
.,BD02 86 67    STX $67         MINUS, SET SERLEN = $FF FOR FLAG
.,BD04 F0 04    BEQ $BD0A       ...ALWAYS
.,BD06 C9 2B    CMP #$2B        MIGHT BE PLUS
.,BD08 D0 05    BNE $BD0F       NOT PLUS EITHER, CHECK DECIMAL POINT

.,BD0A 20 73 00 JSR $0073       GET NEXT CHAR OF STRING

.,BD0D 90 5B    BCC $BD6A       INSERT THIS DIGIT

.,BD0F C9 2E    CMP #$2E        CHECK FOR DECIMAL POINT
.,BD11 F0 2E    BEQ $BD41       YES
.,BD13 C9 45    CMP #$45        CHECK FOR EXPONENT PART
.,BD15 D0 30    BNE $BD47       NO, END OF NUMBER
.,BD17 20 73 00 JSR $0073       YES, START CONVERTING EXPONENT
.,BD1A 90 17    BCC $BD33       EXPONENT DIGIT
.,BD1C C9 AB    CMP #$AB        NEGATIVE EXPONENT?
.,BD1E F0 0E    BEQ $BD2E       YES
.,BD20 C9 2D    CMP #$2D        MIGHT NOT BE TOKENIZED YET
.,BD22 F0 0A    BEQ $BD2E       YES, IT IS NEGATIVE
.,BD24 C9 AA    CMP #$AA        OPTIONAL "+"
.,BD26 F0 08    BEQ $BD30       YES
.,BD28 C9 2B    CMP #$2B        MIGHT NOT BE TOKENIZED YET
.,BD2A F0 04    BEQ $BD30       YES, FOUND "+"
.,BD2C D0 07    BNE $BD35       ...ALWAYS, NUMBER COMPLETED
.,BD2E 66 60    ROR $60         C=1, SET FLAG NEGATIVE

.,BD30 20 73 00 JSR $0073       GET NEXT DIGIT OF EXPONENT

.,BD33 90 5C    BCC $BD91       CHAR IS A DIGIT OF EXPONENT

.,BD35 24 60    BIT $60         END OF NUMBER, CHECK EXP SIGN
.,BD37 10 0E    BPL $BD47       POSITIVE EXPONENT
.,BD39 A9 00    LDA #$00        NEGATIVE EXPONENT
.,BD3B 38       SEC             MAKE 2'S COMPLEMENT OF EXPONENT
.,BD3C E5 5E    SBC $5E         
.,BD3E 4C 49 BD JMP $BD49       

                                *** FOUND A DECIMAL POINT
.,BD41 66 5F    ROR $5F         C=1, SET DPFLG FOR DECIMAL POINT
.,BD43 24 5F    BIT $5F         CHECK IF PREVIOUS DEC. PT.
.,BD45 50 C3    BVC $BD0A       NO PREVIOUS DECIMAL POINT
                                A SECOND DECIMAL POINT IS TAKEN AS A TERMINATOR
                                TO THE NUMERIC STRING.
                                "A=11..22" WILL GIVE A SYNTAX ERROR, BECAUSE
                                IT IS TWO NUMBERS WITH NO OPERATOR BETWEEN.
                                "PRINT 11..22" GIVES NO ERROR, BECAUSE IT IS
                                JUST THE CONCATENATION OF TWO NUMBERS.

                                NUMBER TERMINATED, ADJUST EXPONENT NOW
.,BD47 A5 5E    LDA $5E         E-VALUE
.,BD49 38       SEC             MODIFY WITH COUNT OF DIGITS
.,BD4A E5 5D    SBC $5D         AFTER THE DECIMAL POINT
.,BD4C 85 5E    STA $5E         COMPLETE CURRENT EXPONENT
.,BD4E F0 12    BEQ $BD62       NO ADJUST NEEDED IF EXP=0
.,BD50 10 09    BPL $BD5B       EXP>0, MULTIPLY BY TEN
.,BD52 20 FE BA JSR $BAFE       EXP<0, DIVIDE BY TEN
.,BD55 E6 5E    INC $5E         UNTIL EXP=0
.,BD57 D0 F9    BNE $BD52       
.,BD59 F0 07    BEQ $BD62       ...ALWAYS, WE ARE FINISHED
.,BD5B 20 E2 BA JSR $BAE2       EXP>0, MULTIPLY BKY TEN
.,BD5E C6 5E    DEC $5E         UNTIL EXP=0
.,BD60 D0 F9    BNE $BD5B       
.,BD62 A5 67    LDA $67         IS WHOLE NUMBER NEGATIVE?
.,BD64 30 01    BMI $BD67       YES
.,BD66 60       RTS             NO, RETURN, WHOLE JOB DONE!
.,BD67 4C B4 BF JMP $BFB4       NEGATIVE NUMBER, SO NEGATE FAC

                                *** ACCUMULATE A DIGIT INTO FAC
.,BD6A 48       PHA             SAVE DIGIT
.,BD6B 24 5F    BIT $5F         SEEN A DECIMAL POINT YET?
.,BD6D 10 02    BPL $BD71       NO, STILL IN INTEGER PART
.,BD6F E6 5D    INC $5D         YES, COUNT THE FRACTIONAL DIGIT
.,BD71 20 E2 BA JSR $BAE2       FAC = FAC * 10
.,BD74 68       PLA             CURRENT DIGIT
.,BD75 38       SEC             <<<SHORTER HERE TO JUST "AND #$0F">>>
.,BD76 E9 30    SBC #$30        <<<TO CONVERT ASCII TO BINARY FORM>>>
.,BD78 20 7E BD JSR $BD7E       ADD THE DIGIT
.,BD7B 4C 0A BD JMP $BD0A       GO BACK FOR MORE

                                *** ADD (A) TO FAC
.,BD7E 48       PHA             SAVE ADDEND
.,BD7F 20 0C BC JSR $BC0C       
.,BD82 68       PLA             GET ADDEND AGAIN
.,BD83 20 3C BC JSR $BC3C       CONVERT TO FP VALUE IN FAC
.,BD86 A5 6E    LDA $6E         
.,BD88 45 66    EOR $66         
.,BD8A 85 6F    STA $6F         
.,BD8C A6 61    LDX $61         TO SIGNAL IF FAC=0
.,BD8E 4C 6A B8 JMP $B86A       PERFORM THE ADDITION

                                *** ACCUMULATE DIGIT OF EXPONENT
.,BD91 A5 5E    LDA $5E         CHECK CURRENT VALUE
.,BD93 C9 0A    CMP #$0A        FOR MORE THAN 2 DIGITS
.,BD95 90 09    BCC $BDA0       NO, THIS IS 1ST OR 2ND DIGIT
.,BD97 A9 64    LDA #$64        EXPONENT TOO BIG
.,BD99 24 60    BIT $60         UNLESS IT IS NEGATIVE
.,BD9B 30 11    BMI $BDAE       LARGE NEGATIVE EXPONENT MAKES FAC=0
.,BD9D 4C 7E B9 JMP $B97E       LARGE POSITIVE EXPONENT IS ERROR
.,BDA0 0A       ASL             EXPONENT TIMES 10
.,BDA1 0A       ASL             
.,BDA2 18       CLC             
.,BDA3 65 5E    ADC $5E         
.,BDA5 0A       ASL             
.,BDA6 18       CLC             <<< ASL ALREADY DID THIS! >>>
.,BDA7 A0 00    LDY #$00        ADD THE NEW DIGIT
.,BDA9 71 7A    ADC ($7A),Y     BUT THIS IS IN ASCII,
.,BDAB 38       SEC             SO ADJUST BACK TO BINARY
.,BDAC E9 30    SBC #$30        
.,BDAE 85 5E    STA $5E         NEW VALUE
.,BDB0 4C 30 BD JMP $BD30       BACK FOR MORE

.:BDB3 9B 3E BC 1F FD           99,999,999.9
.:BDB8 9E 6E 6B 27 FD           999,999,999
.:BDBD 9E 6E 6B 28 00           1,000,000,000


                                *** PRINT "IN <LINE #>"
.,BDC2 A9 71    LDA #$71        PRINT " IN "
.,BDC4 A0 A3    LDY #$A3        
.,BDC6 20 DA BD JSR $BDDA       
.,BDC9 A5 3A    LDA $3A         
.,BDCB A6 39    LDX $39         

                                *** PRINT A,X AS DECIMAL INTEGER
.,BDCD 85 62    STA $62         PRINT A,X IN DECIMAL
.,BDCF 86 63    STX $63         
.,BDD1 A2 90    LDX #$90        EXPONENT = 2^16
.,BDD3 38       SEC             CONVERT UNSIGNED
.,BDD4 20 49 BC JSR $BC49       CONVERT LINE # TO FP

                                *** CONVERT (FAC) TO STRING, AND PRINT IT
.,BDD7 20 DF BD JSR $BDDF       CONVERT (FAC) TO STRING AT STACK

                                *** PRINT STRING STARTING AT Y,A
.,BDDA 4C 1E AB JMP $AB1E       PRINT STRING AT A,Y

                                *** CONVERT (FAC) TO STRING STARTING AT STACK
                                RETURN WITH (Y,A) POINTING AT STRING
.,BDDD A0 01    LDY #$01        NORMAL ENTRY PUTS STRING AT STACK...
.,BDDF A9 20    LDA #$20
.,BDE1 24 66    BIT $66
.,BDE3 10 02    BPL $BDE7
.,BDE5 A9 2D    LDA #$2D

                                *** "STR$" FUNCTION ENTERS HERE, WITH (Y)=0
                                SO THAT RESULT STRING STARTS AT STACK-1
                                (THIS IS USED AS A FLAG)
.,BDE7 99 FF 00 STA $00FF,Y     EMIT "-"
.,BDEA 85 66    STA $66         MAKE FAC.SIGN POSITIVE ($2D)
.,BDEC 84 71    STY $71         SAVE STRING PNTR
.,BDEE C8       INY             
.,BDEF A9 30    LDA #$30        IN CASE (FAC)=0
.,BDF1 A6 61    LDX $61         NUMBER=0?
.,BDF3 D0 03    BNE $BDF8       NO, (FAC) NOT ZERO
.,BDF5 4C 04 BF JMP $BF04       YES, FINISHED

.,BDF8 A9 00    LDA #$00        STARTING VALUE FOR TMPEXP
.,BDFA E0 80    CPX #$80        ANY INTEGER PART?
.,BDFC F0 02    BEQ $BE00       NO, BTWN .5 AND .999999999
.,BDFE B0 09    BCS $BE09       YES

.,BE00 A9 BD    LDA #$BD        MULTIPLY BY 1E9
.,BE02 A0 BD    LDY #$BD        TO GIVE ADJUSTMENT A HEAD START
.,BE04 20 28 BA JSR $BA28       
.,BE07 A9 F7    LDA #$F7        EXPONENT ADJUSTMENT
.,BE09 85 5D    STA $5D         0 OR -9

                                *** ADJUST UNTIL 1E8 <= (FAC) <1E9
.,BE0B A9 B8    LDA #$B8        
.,BE0D A0 BD    LDY #$BD        
.,BE0F 20 5B BC JSR $BC5B       COMPARE TO 1E9-1
.,BE12 F0 1E    BEQ $BE32       (FAC) = 1E9-1
.,BE14 10 12    BPL $BE28       TOO LARGE, DIVIDE BY TEN
.,BE16 A9 B3    LDA #$B3        COMPARE TO 1E8-.1
.,BE18 A0 BD    LDY #$BD        
.,BE1A 20 5B BC JSR $BC5B       COMPARE TO 1E8-.1
.,BE1D F0 02    BEQ $BE21       (FAC) = 1E8-.1
.,BE1F 10 0E    BPL $BE2F       IN RANGE, ADJUSTMENT FINISHED
.,BE21 20 E2 BA JSR $BAE2       TOO SMALL, MULTIPLY BY TEN
.,BE24 C6 5D    DEC $5D         KEEP TRACK OF MULTIPLIES
.,BE26 D0 EE    BNE $BE16       ...ALWAYS
.,BE28 20 FE BA JSR $BAFE       TOO LARGE, DIVIDE BY TEN
.,BE2B E6 5D    INC $5D         KEEP TRACK OF DIVISIONS
.,BE2D D0 DC    BNE $BE0B       ...ALWAYS

.,BE2F 20 49 B8 JSR $B849       ROUND ADJUSTED RESULT
.,BE32 20 9B BC JSR $BC9B       CONVERT ADJUSTED VALUE TO 32-BIT INTEGER

                                FAC+1...FAC+4 IS NOW IN INTEGER FORM
                                WITH POWER OF TEN ADJUSTMENT IN TMPEXP

                                IF -10 < TMPEXP > 1, PRINT IN DECIMAL FORM
                                OTHERWISE, PRINT IN EXPONENTIAL FORM
.,BE35 A2 01    LDX #$01        ASSUME 1 DIGIT BEFORE "."
.,BE37 A5 5D    LDA $5D         CHECK RANGE
.,BE39 18       CLC             
.,BE3A 69 0A    ADC #$0A        
.,BE3C 30 09    BMI $BE47       < .01, USE EXPONENTIAL FORM
.,BE3E C9 0B    CMP #$0B        
.,BE40 B0 06    BCS $BE48       >= 1E10, USE EXPONENTIAL FORM
.,BE42 69 FF    ADC #$FF        LESS 1 GIVES INDEX FOR "."
.,BE44 AA       TAX             
.,BE45 A9 02    LDA #$02        SET REMAINING EXPONENT = 0
.,BE47 38       SEC             COMPUTE REMAINING EXPONENT
.,BE48 E9 02    SBC #$02        
.,BE4A 85 5E    STA $5E         VALUE FOR "E+XX" OR "E-XX"
.,BE4C 86 5D    STX $5D         INDEX FOR DECIMAL POINT
.,BE4E 8A       TXA             SEE IF "." COMES FIRST
.,BE4F F0 02    BEQ $BE53       YES
.,BE51 10 13    BPL $BE66       NO, LATER
.,BE53 A4 71    LDY $71         GET INDEX INTO STRING BEING BUILT
.,BE55 A9 2E    LDA #$2E        STORE A DECIMAL POINT
.,BE57 C8       INY             
.,BE58 99 FF 00 STA $00FF,Y     
.,BE5B 8A       TXA             SEE IF NEED ".0"
.,BE5C F0 06    BEQ $BE64       NO
.,BE5E A9 30    LDA #$30        YES, STORE "0"
.,BE60 C8       INY             
.,BE61 99 FF 00 STA $00FF,Y     
.,BE64 84 71    STY $71         SAVE OUTPUT INDEX AGAIN

                                NOW DIVIDE BY POWERS OF TEN TO GET SUCCESSIVE DIGITS
.,BE66 A0 00    LDY #$00        INDEX TO TABLE OF POWERS OF TEN
.,BE68 A2 80    LDX #$80        STARTING VALUE FOR DIGIT WITH DIRECTION
.,BE6A A5 65    LDA $65         START BY ADDING -100000000 UNTIL
.,BE6C 18       CLC             OVERSHOOT.  THEN ADD +10000000,
.,BE6D 79 19 BF ADC $BF19,Y     THEN ADD -1000000, THEN ADD
.,BE70 85 65    STA $65         +100000, AND SO ON.
.,BE72 A5 64    LDA $64         THE # OF TIMES EACH POWER IS ADDED
.,BE74 79 18 BF ADC $BF18,Y     IS 1 MORE THAN CORRESPONDING DIGIT
.,BE77 85 64    STA $64         
.,BE79 A5 63    LDA $63         
.,BE7B 79 17 BF ADC $BF17,Y     
.,BE7E 85 63    STA $63         
.,BE80 A5 62    LDA $62         
.,BE82 79 16 BF ADC $BF16,Y     
.,BE85 85 62    STA $62         
.,BE87 E8       INX             COUNT THE ADD
.,BE88 B0 04    BCS $BE8E       IF C=1 AND X NEGATIVE, KEEP ADDING
.,BE8A 10 DE    BPL $BE6A       IF C=0 AND X POSITIVE, KEEP ADDING
.,BE8C 30 02    BMI $BE90       IF C=0 AND X NEGATIVE, WE OVERSHOT
.,BE8E 30 DA    BMI $BE6A       IF C=1 AND X POSITIVE, WE OVERSHOT
.,BE90 8A       TXA             OVERSHOT, SO MAKE X INTO A DIGIT
.,BE91 90 04    BCC $BE97       HOW DEPENDS ON DIRECTION WE WERE GOING
.,BE93 49 FF    EOR #$FF        DIGIT = 9-X
.,BE95 69 0A    ADC #$0A        
.,BE97 69 2F    ADC #$2F        MAKE DIGIT INTO ASCII
.,BE99 C8       INY             ADVANCE TO NEXT SMALLER POWER OF TEN
.,BE9A C8       INY             
.,BE9B C8       INY             
.,BE9C C8       INY             
.,BE9D 84 47    STY $47         SAVE PNTR TO POWERS
.,BE9F A4 71    LDY $71         GET OUTPUT PNTR
.,BEA1 C8       INY             STORE THE DIGIT
.,BEA2 AA       TAX             SAVE DIGIT, HI-BIT IS DIRECTION
.,BEA3 29 7F    AND #$7F        MAKE SURE $30...$39 FOR STRING
.,BEA5 99 FF 00 STA $00FF,Y     
.,BEA8 C6 5D    DEC $5D         COUNT THE DIGIT
.,BEAA D0 06    BNE $BEB2       NOT TIME FOR "." YET
.,BEAC A9 2E    LDA #$2E        TIME, SO STORE THE DECIMAL POINT
.,BEAE C8       INY             
.,BEAF 99 FF 00 STA $00FF,Y     
.,BEB2 84 71    STY $71         SAVE OUTPUT PNTR AGAIN
.,BEB4 A4 47    LDY $47         GET PNTR TO POWERS
.,BEB6 8A       TXA             GET DIGIT WITH HI-BIT = DIRECTION
.,BEB7 49 FF    EOR #$FF        CHANGE DIRECTION
.,BEB9 29 80    AND #$80        $00 IF ADDING, $80 IF SUBTRACTING
.,BEBB AA       TAX             
.,BEBC C0 24    CPY #$24        
.,BEBE F0 04    BEQ $BEC4
.,BEC0 C0 3C    CPY #$3C
.,BEC2 D0 A6    BNE $BE6A       NOT FINISHED YET

                                NINE DIGITS HAVE BEEN STORED IN STRING.  NOW LOOK
                                BACK AND LOP OFF TRAILING ZEROES AND A TRAILING
                                DECIMAL POINT.
.,BEC4 A4 71    LDY $71         POINTS AT LAST STORED CHAR
.,BEC6 B9 FF 00 LDA $00FF,Y     SEE IF LOPPABLE
.,BEC9 88       DEY             
.,BECA C9 30    CMP #$30        SUPPRESS TRAILING ZEROES
.,BECC F0 F8    BEQ $BEC6       YES, KEEP LOOPING
.,BECE C9 2E    CMP #$2E        SUPPRESS TRAILING DECIMAL POINT
.,BED0 F0 01    BEQ $BED3       ".", SO WRITE OVER IT
.,BED2 C8       INY             NOT ".", SO INCLUDE IN STRING AGAIN
.,BED3 A9 2B    LDA #$2B        PREPARE FOR POSITIVE EXPONENT "E+XX"
.,BED5 A6 5E    LDX $5E         SEE IF ANY E-VALUE
.,BED7 F0 2E    BEQ $BF07       NO, JUST MARK END OF STRING
.,BED9 10 08    BPL $BEE3       YES, AND IT IS POSITIVE
.,BEDB A9 00    LDA #$00        YES, AND IT IS NEGATIVE
.,BEDD 38       SEC             COMPLEMENT THE VALUE
.,BEDE E5 5E    SBC $5E         
.,BEE0 AA       TAX             GET MAGNITUDE IN X
.,BEE1 A9 2D    LDA #$2D        E SIGN
.,BEE3 99 01 01 STA $0101,Y     STORE SIGN IN STRING
.,BEE6 A9 45    LDA #$45        STORE "E" IN STRING BEFORE SIGN
.,BEE8 99 00 01 STA $0100,Y     
.,BEEB 8A       TXA             EXPONENT MAGNITUDE IN A-REG
.,BEEC A2 2F    LDX #$2F        SEED FOR EXPONENT DIGIT
.,BEEE 38       SEC             CONVERT TO DECIMAL
.,BEEF E8       INX             COUNT THE SUBTRACTION
.,BEF0 E9 0A    SBC #$0A        TEN'S DIGIT
.,BEF2 B0 FB    BCS $BEEF       MORE TENS TO SUBTRACT
.,BEF4 69 3A    ADC #$3A        CONVERT REMAINDER TO ONE'S DIGIT
.,BEF6 99 03 01 STA $0103,Y     STORE ONE'S DIGIT
.,BEF9 8A       TXA             
.,BEFA 99 02 01 STA $0102,Y     STORE TEN'S DIGIT
.,BEFD A9 00    LDA #$00        MARK END OF STRING WITH $00
.,BEFF 99 04 01 STA $0104,Y     
.,BF02 F0 08    BEQ $BF0C       ...ALWAYS
.,BF04 99 FF 00 STA $00FF,Y     STORE "0" IN ASCII
.,BF07 A9 00    LDA #$00        STORE $00 ON END OF STRING
.,BF09 99 00 01 STA $0100,Y     
.,BF0C A9 00    LDA #$00        POINT Y,A AT BEGINNING OF STRING
.,BF0E A0 01    LDY #$01        (STR$ STARTED STRING AT STACK-1, BUT
.,BF10 60       RTS             STR$ DOESN'T USE Y,A ANYWAY.)

.:BF11 80 00 00 00 00

                                *** POWERS OF 10 FROM 1E8 DOWN TO 1,
                                AS 32-BIT INTEGERS, WITH ALTERNATING SIGNS
.:BF16 FA 0A 1F 00              -100000000
.:BF1A 00 98 96 80              10000000
.:BF1E FF F0 BD C0              -1000000
.:BF22 00 01 86 A0              100000
.:BF26 FF FF D8 F0              -10000
.:BF2A 00 00 03 E8              1000
.:BF2E FF FF FF 9C              -100
.:BF32 00 00 00 0A              10
.:BF36 FF FF FF FF              -1

.:BF3A FF DF 0A 80              
.:BF3E 00 03 4B C0              
.:BF42 FF FF 73 60              
.:BF46 00 00 0E 10              
.:BF4A FF FF FD A8              
.:BF4E 00 00 00 3C              

.:BF52 EC

.:BF53 AA AA AA AA AA
.:BF58 AA AA AA AA AA AA AA AA
.:BF60 AA AA AA AA AA AA AA AA
.:BF68 AA AA AA AA AA AA AA AA
.:BF70 AA


                                *** "SQR" FUNCTION
                                <<< UNFORTUNATELY, RATHER THAN A NEWTON-RAPHSON >>>
                                <<< ITERATION, MS BASIC USES EXPONENTIATION     >>>
                                <<< SQR(X) = X^.5                               >>>
.,BF71 20 0C BC JSR $BC0C       
.,BF74 A9 11    LDA #$11        SET UP POWER OF 0.5
.,BF76 A0 BF    LDY #$BF        
.,BF78 20 A2 BB JSR $BBA2       

                                *** EXPONENTIATION OPERATION
                                ARG ^ FAC  =  EXP( LOG(ARG) * FAC )
.,BF7B F0 70    BEQ $BFED       IF FAC=0, ARG^FAC=EXP(0)
.,BF7D A5 69    LDA $69         IF ARG=0, ARG^FAC=0
.,BF7F D0 03    BNE $BF84       NEITHER IS ZERO
.,BF81 4C F9 B8 JMP $B8F9       SET FAC = 0
.,BF84 A2 4E    LDX #$4E        SAVE FAC IN TEMP3
.,BF86 A0 00    LDY #$00        
.,BF88 20 D4 BB JSR $BBD4       
.,BF8B A5 6E    LDA $6E         NORMALLY, ARG MUST BE POSITIVE
.,BF8D 10 0F    BPL $BF9E       IT IS POSITIVE, SO ALL IS WELL
.,BF8F 20 CC BC JSR $BCCC       NEGATIVE, BUT OK IF INTEGRAL POWER
.,BF92 A9 4E    LDA #$4E        SEE IF INT(FAC)=FAC
.,BF94 A0 00    LDY #$00        
.,BF96 20 5B BC JSR $BC5B       IS IT AN INTEGER POWER?
.,BF99 D0 03    BNE $BF9E       NOT INTEGRAL,  WILL CAUSE ERROR LATER
.,BF9B 98       TYA             MAKE ARG SIGN + AS IT IS MOVED TO FAC
.,BF9C A4 07    LDY $07         INTEGRAL, SO ALLOW NEGATIVE ARG
.,BF9E 20 FE BB JSR $BBFE       MOVE ARGUMENT TO FAC
.,BFA1 98       TYA             SAVE FLAG FOR NEGATIVE ARG (0=+)
.,BFA2 48       PHA             
.,BFA3 20 EA B9 JSR $B9EA       GET LOG(ARG)
.,BFA6 A9 4E    LDA #$4E        MULTIPLY BY POWER
.,BFA8 A0 00    LDY #$00        
.,BFAA 20 28 BA JSR $BA28       
.,BFAD 20 ED BF JSR $BFED       E ^ LOG(FAC)
.,BFB0 68       PLA             GET FLAG FOR NEGATIVE ARG
.,BFB1 4A       LSR             <<<LSR,BCC COULD BE MERELY BPL>>>
.,BFB2 90 0A    BCC $BFBE       NOT NEGATIVE, FINISHED
                                NEGATIVE ARG, SO NEGATE RESULT

                                *** NEGATE VALUE IN FAC
.,BFB4 A5 61    LDA $61         IF FAC=0, NO NEED TO COMPLEMENT
.,BFB6 F0 06    BEQ $BFBE       YES, FAC=0
.,BFB8 A5 66    LDA $66         NO, SO TOGGLE SIGN
.,BFBA 49 FF    EOR #$FF        
.,BFBC 85 66    STA $66         
.,BFBE 60       RTS             

.:BFBF 81 38 AA 3B 29           LOG(E) TO BASE 2
.:BFC4 07                       ( # OF TERMS IN POLYNOMIAL) - 1
.:BFC5 71 34 58 3E 56           (LOG(2)^7)/8!
.:BFCA 74 16 7E B3 1B           (LOG(2)^6)/7!
.:BFCF 77 2F EE E3 85           (LOG(2)^5)/6!
.:BFD4 7A 1D 84 1C 2A           (LOG(2)^4)/5!
.:BFD9 7C 63 59 58 0A           (LOG(2)^3)/4!
.:BFDE 7E 75 FD E7 C6           (LOG(2)^2)/3!
.:BFE3 80 31 72 18 10           LOG(2)/2!
.:BFE8 81 00 00 00 00           1


                                *** "EXP" FUNCTION
                                FAC = E ^ FAC
.,BFED A9 BF    LDA #$BF        CONVERT TO POWER OF TWO PROBLEM
.,BFEF A0 BF    LDY #$BF        E^X = 2^(LOG2(E)*X)
.,BFF1 20 28 BA JSR $BA28       
.,BFF4 A5 70    LDA $70         NON-STANDARD ROUNDING HERE
.,BFF6 69 50    ADC #$50        ROUND UP IF EXTENSION > $AF
.,BFF8 90 03    BCC $BFFD       NO, DON'T ROUND UP
.,BFFA 20 23 BC JSR $BC23       
.,BFFD 4C 00 E0 JMP $E000
.,E000 85 56    STA $56         STRANGE VALUE
.,E002 20 0F BC JSR $BC0F       COPY FAC INTO ARG
.,E005 A5 61    LDA $61         MAXIMUM EXPONENT IS < 128
.,E007 C9 88    CMP #$88        WITHIN RANGE?
.,E009 90 03    BCC $E00E       YES
.,E00B 20 D4 BA JSR $BAD4       OVERFLOW IF +, RETURN 0.0 IF -
.,E00E 20 CC BC JSR $BCCC       GET INT(FAC)
.,E011 A5 07    LDA $07         THIS IS THE INETGRAL PART OF THE POWER
.,E013 18       CLC             ADD TO EXPONENT BIAS + 1
.,E014 69 81    ADC #$81        
.,E016 F0 F3    BEQ $E00B       OVERFLOW
.,E018 38       SEC             BACK OFF TO NORMAL BIAS
.,E019 E9 01    SBC #$01        
.,E01B 48       PHA             SAVE EXPONENT

.,E01C A2 05    LDX #$05        SWAP ARG AND FAC
.,E01E B5 69    LDA $69,X       <<< WHY SWAP? IT IS DOING      >>>
.,E020 B4 61    LDY $61,X       <<< -(A-B) WHEN (B-A) IS THE   >>>
.,E022 95 61    STA $61,X       <<< SAME THING!                >>>
.,E024 94 69    STY $69,X       
.,E026 CA       DEX             
.,E027 10 F5    BPL $E01E       
.,E029 A5 56    LDA $56         
.,E02B 85 70    STA $70         
.,E02D 20 53 B8 JSR $B853       POWER-INT(POWER) --> FRACTIONAL PART
.,E030 20 B4 BF JSR $BFB4       
.,E033 A9 C4    LDA #$C4        
.,E035 A0 BF    LDY #$BF        
.,E037 20 59 E0 JSR $E059       COMPUTE F(X) ON FRACTIONAL PART
.,E03A A9 00    LDA #$00        
.,E03C 85 6F    STA $6F         
.,E03E 68       PLA             GET EXPONENT
.,E03F 20 B9 BA JSR $BAB9       
.,E042 60       RTS             <<< WASTED BYTE HERE, COULD HAVE >>>
                                <<< JUST USED "JMP ADD.EXPO..."  >>>

                                *** ODD POLYNOMIAL SUBROUTINE
                                F(X) = X * P(X^2)

                                WHERE:  X IS VALUE IN FAC
                                        Y,A POINTS AT COEFFICIENT TABLE
                                        FIRST BYTE OF COEFF. TABLE IS N
                                        COEFFICIENTS FOLLOW, HIGHEST POWER FIRST

                                P(X^2) COMPUTED USING NORMAL POLYNOMIAL SUBROUTINE

.,E043 85 71    STA $71         SAVE ADDRESS OF COEFFICIENT TABLE
.,E045 84 72    STY $72         
.,E047 20 CA BB JSR $BBCA       
.,E04A A9 57    LDA #$57        Y=0 ALREADY, SO Y,A POINTS AT TEMP1
.,E04C 20 28 BA JSR $BA28       FORM X^2
.,E04F 20 5D E0 JSR $E05D       DO SERIES IN X^2
.,E052 A9 57    LDA #$57        GET X AGAIN
.,E054 A0 00    LDY #$00        
.,E056 4C 28 BA JMP $BA28       MULTIPLY X BY P(X^2) AND EXIT

                                *** NORMAL POLYNOMIAL SUBROUTINE
                                P(X) = C(0)*X^N + C(1)*X^(N-1) + ... + C(N)

                                WHERE:  X IS VALUE IN FAC
                                        Y,A POINTS AT COEFFICIENT TABLE
                                        FIRST BYTE OF COEFF. TABLE IS N
                                        COEFFICIENTS FOLLOW, HIGHEST POWER FIRST
.,E059 85 71    STA $71         POINTER TO COEFFICIENT TABLE
.,E05B 84 72    STY $72         

.,E05D 20 C7 BB JSR $BBC7       
.,E060 B1 71    LDA ($71),Y     GET N
.,E062 85 67    STA $67         SAVE N
.,E064 A4 71    LDY $71         BUMP PNTR TO HIGHEST COEFFICIENT
.,E066 C8       INY             AND GET PNTR INTO Y,A
.,E067 98       TYA             
.,E068 D0 02    BNE $E06C       
.,E06A E6 72    INC $72         
.,E06C 85 71    STA $71         
.,E06E A4 72    LDY $72         
.,E070 20 28 BA JSR $BA28       ACCUMULATE SERIES TERMS
.,E073 A5 71    LDA $71         BUMP PNTR TO NEXT COEFFICIENT
.,E075 A4 72    LDY $72         
.,E077 18       CLC             
.,E078 69 05    ADC #$05        
.,E07A 90 01    BCC $E07D       
.,E07C C8       INY             
.,E07D 85 71    STA $71         
.,E07F 84 72    STY $72         
.,E081 20 67 B8 JSR $B867       ADD NEXT COEFFICIENT
.,E084 A9 5C    LDA #$5C        POINT AT X AGAIN
.,E086 A0 00    LDY #$00        
.,E088 C6 67    DEC $67         IF SERIES NOT FINISHED,
.,E08A D0 E4    BNE $E070       THEN ADD ANOTHER TERM
.,E08C 60       RTS             FINISHED

.:E08D 98 35 44 7A 00           RND 1
.:E092 68 28 B1 46 00           RND 2


                                *** "RND" FUNCTION
.,E097 20 2B BC JSR $BC2B       REDUCE ARGUMENT TO -1, 0, OR +1
.,E09A 30 37    BMI $E0D3       = -1, USE CURRENT ARGUMENT FOR SEED
.,E09C D0 20    BNE $E0BE
.,E09E 20 F3 FF JSR $FFF3
.,E0A1 86 22    STX $22
.,E0A3 84 23    STY $23
.,E0A5 A0 04    LDY #$04
.,E0A7 B1 22    LDA ($22),Y
.,E0A9 85 62    STA $62
.,E0AB C8       INY
.,E0AC B1 22    LDA ($22),Y
.,E0AE 85 64    STA $64
.,E0B0 A0 08    LDY #$08
.,E0B2 B1 22    LDA ($22),Y
.,E0B4 85 63    STA $63
.,E0B6 C8       INY
.,E0B7 B1 22    LDA ($22),Y
.,E0B9 85 65    STA $65
.,E0BB 4C E3 E0 JMP $E0E3
.,E0BE A9 8B    LDA #$8B        USE CURRENT SEED
.,E0C0 A0 00    LDY #$00        
.,E0C2 20 A2 BB JSR $BBA2       
.,E0C5 A9 8D    LDA #$8D        VERY POOR RND ALGORITHM
.,E0C7 A0 E0    LDY #$E0        
.,E0C9 20 28 BA JSR $BA28       
.,E0CC A9 92    LDA #$92        ALSO, CONSTANTS ARE TRUNCATED
.,E0CE A0 E0    LDY #$E0        <<<THIS DOES NOTHING, DUE TO >>>
                                <<<SMALL EXPONENT            >>>
.,E0D0 20 67 B8 JSR $B867       
.,E0D3 A6 65    LDX $65         SHUFFLE HI AND LO BYTES
.,E0D5 A5 62    LDA $62         TO SUPPOSEDLY MAKE IT MORE RANDOM
.,E0D7 85 65    STA $65         
.,E0D9 86 62    STX $62         
.,E0DB A6 63    LDX $63
.,E0DD A5 64    LDA $64         MAKE IT POSITIVE
.,E0DF 85 63    STA $63         
.,E0E1 86 64    STX $64
.,E0E3 A9 00    LDA #$00        A SOMEWHAT RANDOM EXTENSION
.,E0E5 85 66    STA $66         
.,E0E7 A5 61    LDA $61         EXPONENT TO MAKE VALUE < 1.0
.,E0E9 85 70    STA $70         
.,E0EB A9 80    LDA #$80
.,E0ED 85 61    STA $61
.,E0EF 20 D7 B8 JSR $B8D7       
.,E0F2 A2 8B    LDX #$8B        MOVE FAC TO RND SEED
.,E0F4 A0 00    LDY #$00        
.,E0F6 4C D4 BB JMP $BBD4       

.,E0F9 C9 F0    CMP #$F0
.,E0FB D0 07    BNE $E104
.,E0FD 84 38    STY $38
.,E0FF 86 37    STX $37
.,E101 4C 63 A6 JMP $A663
.,E104 AA       TAX
.,E105 D0 02    BNE $E109
.,E107 A2 1E    LDX #$1E
.,E109 4C 37 A4 JMP $A437
.,E10C 20 D2 FF JSR $FFD2
.,E10F B0 E8    BCS $E0F9
.,E111 60       RTS
.,E112 20 CF FF JSR $FFCF
.,E115 B0 E2    BCS $E0F9
.,E117 60       RTS
.,E118 20 AD E4 JSR $E4AD
.,E11B B0 DC    BCS $E0F9
.,E11D 60       RTS
.,E11E 20 C6 FF JSR $FFC6
.,E121 B0 D6    BCS $E0F9
.,E123 60       RTS
.,E124 20 E4 FF JSR $FFE4
.,E127 B0 D0    BCS $E0F9
.,E129 60       RTS
.,E12A 20 8A AD JSR $AD8A
.,E12D 20 F7 B7 JSR $B7F7
.,E130 A9 E1    LDA #$E1
.,E132 48       PHA
.,E133 A9 46    LDA #$46
.,E135 48       PHA
.,E136 AD 0F 03 LDA $030F
.,E139 48       PHA
.,E13A AD 0C 03 LDA $030C
.,E13D AE 0D 03 LDX $030D
.,E140 AC 0E 03 LDY $030E
.,E143 28       PLP
.,E144 6C 14 00 JMP ($0014)
.,E147 08       PHP
.,E148 8D 0C 03 STA $030C
.,E14B 8E 0D 03 STX $030D
.,E14E 8C 0E 03 STY $030E
.,E151 68       PLA
.,E152 8D 0F 03 STA $030F
.,E155 60       RTS
.,E156 20 D4 E1 JSR $E1D4
.,E159 A6 2D    LDX $2D
.,E15B A4 2E    LDY $2E
.,E15D A9 2B    LDA #$2B
.,E15F 20 D8 FF JSR $FFD8
.,E162 B0 95    BCS $E0F9
.,E164 60       RTS
.,E165 A9 01    LDA #$01
.:E167 2C       .BYTE $2C
.,E168 A9 00    LDA #$00
.,E16A 85 0A    STA $0A
.,E16C 20 D4 E1 JSR $E1D4
.,E16F A5 0A    LDA $0A
.,E171 A6 2B    LDX $2B
.,E173 A4 2C    LDY $2C
.,E175 20 D5 FF JSR $FFD5
.,E178 B0 57    BCS $E1D1
.,E17A A5 0A    LDA $0A
.,E17C F0 17    BEQ $E195
.,E17E A2 1C    LDX #$1C
.,E180 20 B7 FF JSR $FFB7
.,E183 29 10    AND #$10
.,E185 D0 17    BNE $E19E
.,E187 A5 7A    LDA $7A
.,E189 C9 02    CMP #$02
.,E18B F0 07    BEQ $E194
.,E18D A9 64    LDA #$64
.,E18F A0 A3    LDY #$A3
.,E191 4C 1E AB JMP $AB1E
.,E194 60       RTS
.,E195 20 B7 FF JSR $FFB7
.,E198 29 BF    AND #$BF
.,E19A F0 05    BEQ $E1A1
.,E19C A2 1D    LDX #$1D
.,E19E 4C 37 A4 JMP $A437
.,E1A1 A5 7B    LDA $7B
.,E1A3 C9 02    CMP #$02
.,E1A5 D0 0E    BNE $E1B5
.,E1A7 86 2D    STX $2D
.,E1A9 84 2E    STY $2E
.,E1AB A9 76    LDA #$76
.,E1AD A0 A3    LDY #$A3
.,E1AF 20 1E AB JSR $AB1E
.,E1B2 4C 2A A5 JMP $A52A
.,E1B5 20 8E A6 JSR $A68E
.,E1B8 20 33 A5 JSR $A533
.,E1BB 4C 77 A6 JMP $A677
.,E1BE 20 19 E2 JSR $E219
.,E1C1 20 C0 FF JSR $FFC0
.,E1C4 B0 0B    BCS $E1D1
.,E1C6 60       RTS
.,E1C7 20 19 E2 JSR $E219
.,E1CA A5 49    LDA $49
.,E1CC 20 C3 FF JSR $FFC3
.,E1CF 90 C3    BCC $E194
.,E1D1 4C F9 E0 JMP $E0F9
.,E1D4 A9 00    LDA #$00
.,E1D6 20 BD FF JSR $FFBD
.,E1D9 A2 01    LDX #$01
.,E1DB A0 00    LDY #$00
.,E1DD 20 BA FF JSR $FFBA
.,E1E0 20 06 E2 JSR $E206
.,E1E3 20 57 E2 JSR $E257
.,E1E6 20 06 E2 JSR $E206
.,E1E9 20 00 E2 JSR $E200
.,E1EC A0 00    LDY #$00
.,E1EE 86 49    STX $49
.,E1F0 20 BA FF JSR $FFBA
.,E1F3 20 06 E2 JSR $E206
.,E1F6 20 00 E2 JSR $E200
.,E1F9 8A       TXA
.,E1FA A8       TAY
.,E1FB A6 49    LDX $49
.,E1FD 4C BA FF JMP $FFBA
.,E200 20 0E E2 JSR $E20E
.,E203 4C 9E B7 JMP $B79E
.,E206 20 79 00 JSR $0079
.,E209 D0 02    BNE $E20D
.,E20B 68       PLA
.,E20C 68       PLA
.,E20D 60       RTS
.,E20E 20 FD AE JSR $AEFD
.,E211 20 79 00 JSR $0079
.,E214 D0 F7    BNE $E20D
.,E216 4C 08 AF JMP $AF08
.,E219 A9 00    LDA #$00
.,E21B 20 BD FF JSR $FFBD
.,E21E 20 11 E2 JSR $E211
.,E221 20 9E B7 JSR $B79E
.,E224 86 49    STX $49
.,E226 8A       TXA
.,E227 A2 01    LDX #$01
.,E229 A0 00    LDY #$00
.,E22B 20 BA FF JSR $FFBA
.,E22E 20 06 E2 JSR $E206
.,E231 20 00 E2 JSR $E200
.,E234 86 4A    STX $4A
.,E236 A0 00    LDY #$00
.,E238 A5 49    LDA $49
.,E23A E0 03    CPX #$03
.,E23C 90 01    BCC $E23F
.,E23E 88       DEY
.,E23F 20 BA FF JSR $FFBA
.,E242 20 06 E2 JSR $E206
.,E245 20 00 E2 JSR $E200
.,E248 8A       TXA
.,E249 A8       TAY
.,E24A A6 4A    LDX $4A
.,E24C A5 49    LDA $49
.,E24E 20 BA FF JSR $FFBA
.,E251 20 06 E2 JSR $E206
.,E254 20 0E E2 JSR $E20E
.,E257 20 9E AD JSR $AD9E
.,E25A 20 A3 B6 JSR $B6A3
.,E25D A6 22    LDX $22
.,E25F A4 23    LDY $23
.,E261 4C BD FF JMP $FFBD


                                *** "COS" FUNCTION
.,E264 A9 E0    LDA #$E0        COS(X)=SIN(X + PI/2)
.,E266 A0 E2    LDY #$E2        
.,E268 20 67 B8 JSR $B867       

                                *** "SIN" FUNCTION
.,E26B 20 0C BC JSR $BC0C       
.,E26E A9 E5    LDA #$E5        REMOVE MULTIPLES OF 2*PI
.,E270 A0 E2    LDY #$E2        BY DIVIDING AND SAVING
.,E272 A6 6E    LDX $6E         THE FRACTIONAL PART
.,E274 20 07 BB JSR $BB07       USE SIGN OF ARGUMENT
.,E277 20 0C BC JSR $BC0C       
.,E27A 20 CC BC JSR $BCCC       TAKE INTEGER PART
.,E27D A9 00    LDA #$00        <<< WASTED LINES, BECAUSE FSUBT >>>
.,E27F 85 6F    STA $6F         <<< CHANGES SGNCPR AGAIN        >>>
.,E281 20 53 B8 JSR $B853       SUBTRACT TO GET FRACTIONAL PART

                                *** (FAC) = ANGLE AS A FRACTION OF A FULL CIRCLE
                                NOW FOLD THE RANGE INTO A QUARTER CIRCLE

                                <<< THERE ARE MUCH SIMPLER WAYS TO DO THIS >>>
.,E284 A9 EA    LDA #$EA        1/4 - FRACTION MAKES
.,E286 A0 E2    LDY #$E2        -3/4 <= FRACTION < 1/4
.,E288 20 50 B8 JSR $B850       
.,E28B A5 66    LDA $66         TEST SIGN OF RESULT
.,E28D 48       PHA             SAVE SIGN FOR LATER UNFOLDING
.,E28E 10 0D    BPL $E29D       ALREADY 0...1/4
.,E290 20 49 B8 JSR $B849       ADD 1/2 TO SHIFT TO -1/4...1/2
.,E293 A5 66    LDA $66         TEST SIGN
.,E295 30 09    BMI $E2A0       -1/4...0
                                0...1/2
.,E297 A5 12    LDA $12         SIGNFLG INITIALIZED = 0 IN "TAN"
.,E299 49 FF    EOR #$FF        FUNCTION
.,E29B 85 12    STA $12         "TAN" IS ONLY USER OF SIGNFLG TOO

                                IF FALL THRU, RANGE IS 0...1/2
                                IF BRANCH HERE, RANGE IS 0...1/4
.,E29D 20 B4 BF JSR $BFB4       

                                IF FALL THRU, RANGE IS -1/2...0
                                IF BRANCH HERE, RANGE IS -1/4...0
.,E2A0 A9 EA    LDA #$EA        ADD 1/4 TO SHIFT RANGE
.,E2A2 A0 E2    LDY #$E2        TO -1/4...1/4
.,E2A4 20 67 B8 JSR $B867       
.,E2A7 68       PLA             GET SAVED SIGN FROM ABOVE
.,E2A8 10 03    BPL $E2AD       
.,E2AA 20 B4 BF JSR $BFB4       MAKE RANGE 0...1/4
.,E2AD A9 EF    LDA #$EF        DO STANDARD SIN SERIES
.,E2AF A0 E2    LDY #$E2        
.,E2B1 4C 43 E0 JMP $E043       

                                *** "TAN" FUNCTION
                                COMPUTE TAN(X) = SIN(X) / COS(X)
.,E2B4 20 CA BB JSR $BBCA       
.,E2B7 A9 00    LDA #$00        SIGNFLG WILL BE TOGGLED IF 2ND OR 3RD
.,E2B9 85 12    STA $12         QUADRANT
.,E2BB 20 6B E2 JSR $E26B       GET SIN(X)
.,E2BE A2 4E    LDX #$4E        SAVE SIN(X) IN TEMP3
.,E2C0 A0 00    LDY #$00        
.,E2C2 20 F6 E0 JSR $E0F6       <<<FUNNY WAY TO CALL MOVMF! >>>
.,E2C5 A9 57    LDA #$57        RETRIEVE X
.,E2C7 A0 00    LDY #$00        
.,E2C9 20 A2 BB JSR $BBA2       
.,E2CC A9 00    LDA #$00        AND COMPUTE COS(X)
.,E2CE 85 66    STA $66         
.,E2D0 A5 12    LDA $12         
.,E2D2 20 DC E2 JSR $E2DC       WEIRD &amp; DANGEROUS WAY TO GET INTO SIN
.,E2D5 A9 4E    LDA #$4E        NOW FORM SIN/COS
.,E2D7 A0 00    LDY #$00        
.,E2D9 4C 0F BB JMP $BB0F       

.,E2DC 48       PHA             SHAME, SHAME!
.,E2DD 4C 9D E2 JMP $E29D       

.:E2E0 81 49 0F DA A2           PI/2
.:E2E5 83 49 0F DA A2           2*PI
.:E2EA 7F 00 00 00 00           1/4
.:E2EF 05                       POWER OF POLYNOMIAL
.:E2F0 84 E6 1A 2D 1B           (2PI)^11/11!
.:E2F5 86 28 07 FB F8           (2PI)^9/9!
.:E2FA 87 99 68 89 01           (2PI)^7/7!
.:E2FF 87 23 35 DF E1           (2PI)^5/5!
.:E304 86 A5 5D E7 28           (2PI)^3/3!
.:E309 83 49 0F DA A2           2PI


                                *** "ATN" FUNCTION
.,E30E A5 66    LDA $66         FOLD THE ARGUMENT RANGE FIRST
.,E310 48       PHA             SAVE SIGN FOR LATER UNFOLDING
.,E311 10 03    BPL $E316       .GE. 0
.,E313 20 B4 BF JSR $BFB4       .LT. 0, SO COMPLEMENT
.,E316 A5 61    LDA $61         IF .GE. 1, FORM RECIPROCAL
.,E318 48       PHA             SAVE FOR LATER UNFOLDING
.,E319 C9 81    CMP #$81        (EXPONENT FOR .GE. 1
.,E31B 90 07    BCC $E324       X < 1
.,E31D A9 BC    LDA #$BC        FORM 1/X
.,E31F A0 B9    LDY #$B9        
.,E321 20 0F BB JSR $BB0F       

                                0 <= X <= 1
                                0 <= ATN(X) <= PI/8
.,E324 A9 3E    LDA #$3E        COMPUTE POLYNOMIAL APPROXIMATION
.,E326 A0 E3    LDY #$E3        
.,E328 20 43 E0 JSR $E043       
.,E32B 68       PLA             START TO UNFOLD
.,E32C C9 81    CMP #$81        WAS IT .GE. 1?
.,E32E 90 07    BCC $E337       NO
.,E330 A9 E0    LDA #$E0        YES, SUBTRACT FROM PI/2
.,E332 A0 E2    LDY #$E2        
.,E334 20 50 B8 JSR $B850       
.,E337 68       PLA             WAS IT NEGATIVE?
.,E338 10 03    BPL $E33D       NO
.,E33A 4C B4 BF JMP $BFB4       YES, COMPLEMENT
.,E33D 60       RTS             

.:E33E 0B                       POWER OF POLYNOMIAL
.:E33F 76 B3 83 BD D3
.:E344 79 1E F4 A6 F5
.:E349 7B 83 FC B0 10
.:E34E 7C 0C 1F 67 CA
.:E353 7C DE 53 CB C1
.:E358 7D 14 64 70 4C
.:E35D 7D B7 EA 51 7A
.:E362 7D 63 30 88 7E
.:E367 7E 92 44 99 3A
.:E36C 7E 4C CC 91 C7
.:E371 7F AA AA AA 13
.:E376 81 00 00 00 00

.,E37B 20 CC FF JSR $FFCC
.,E37E A9 00    LDA #$00
.,E380 85 13    STA $13
.,E382 20 7A A6 JSR $A67A
.,E385 58       CLI
.,E386 A2 80    LDX #$80
.,E388 6C 00 03 JMP ($0300)
.,E38B 8A       TXA
.,E38C 30 03    BMI $E391
.,E38E 4C 3A A4 JMP $A43A
.,E391 4C 74 A4 JMP $A474
.,E394 20 53 E4 JSR $E453
.,E397 20 BF E3 JSR $E3BF
.,E39A 20 22 E4 JSR $E422
.,E39D A2 FB    LDX #$FB
.,E39F 9A       TXS
.,E3A0 D0 E4    BNE $E386


                                *** GENERIC COPY OF CHRGET SUBROUTINE
                                WHICH IS COPIED INTO $00B1...$00C8 DURING INITIALIZATION

                                CORNELIS BONGERS DESCRIBED SEVERAL IMPROVEMENTS
                                TO CHRGET IN MICRO MAGAZINE OR CALL A.P.P.L.E.
                                (I DON'T REMEMBER WHICH OR EXACTLY WHEN)
.,E3A2 E6 7A    INC $7A         
.,E3A4 D0 02    BNE $E3A8       
.,E3A6 E6 7B    INC $7B         
.,E3A8 AD 60 EA LDA $EA60       <<< ACTUAL ADDRESS FILLED IN LATER >>>
.,E3AB C9 3A    CMP #$3A        EOS, ALSO TOP OF NUMERIC RANGE
.,E3AD B0 0A    BCS $E3B9       NOT NUMBER, MIGHT BE EOS
.,E3AF C9 20    CMP #$20        IGNORE BLANKS
.,E3B1 F0 EF    BEQ $E3A2       
.,E3B3 38       SEC             TEST FOR NUMERIC RANGE IN WAY THAT
.,E3B4 E9 30    SBC #$30        CLEARS CARRY IF CHAR IS DIGIT
.,E3B6 38       SEC             AND LEAVES CHAR IN A-REG
.,E3B7 E9 D0    SBC #$D0        
.,E3B9 60       RTS             


                                *** INITIAL VALUE FOR RANDOM NUMBER
                                ALSO COPIED IN ALONG WITH CHRGET, BUT ERRONEOUSLY:
                                <<< THE LAST BYTE IS NOT COPIED >>>
.:E3BA 80 4F C7 52 58           APPROX. = .811635157

.,E3BF A9 4C    LDA #$4C
.,E3C1 85 54    STA $54
.,E3C3 8D 10 03 STA $0310
.,E3C6 A9 48    LDA #$48
.,E3C8 A0 B2    LDY #$B2
.,E3CA 8D 11 03 STA $0311
.,E3CD 8C 12 03 STY $0312
.,E3D0 A9 91    LDA #$91
.,E3D2 A0 B3    LDY #$B3
.,E3D4 85 05    STA $05
.,E3D6 84 06    STY $06
.,E3D8 A9 AA    LDA #$AA        POINT "USR" TO ILLEGAL QUANTITY
.,E3DA A0 B1    LDY #$B1        ERROR, UNTIL USER SETS IT UP
.,E3DC 85 03    STA $03         
.,E3DE 84 04    STY $04         

                                *** MOVE GENERIC CHRGET AND RANDOM SEED INTO PLACE
                                <<< NOTE THAT LOOP VALUE IS WRONG!          >>>
                                <<< THE LAST BYTE OF THE RANDOM SEED IS NOT >>>
                                <<< COPIED INTO PAGE ZERO!                  >>>
.,E3E0 A2 1C    LDX #$1C        
.,E3E2 BD A2 E3 LDA $E3A2,X     
.,E3E5 95 73    STA $73,X       
.,E3E7 CA       DEX             
.,E3E8 10 F8    BPL $E3E2       

.,E3EA A9 03    LDA #$03        SET LENGTH OF TEMP. STRING DESCRIPTORS
.,E3EC 85 53    STA $53         FOR GARBAGE COLLECTION SUBROUTINE
.,E3EE A9 00    LDA #$00
.,E3F0 85 68    STA $68
.,E3F2 85 13    STA $13
.,E3F4 85 18    STA $18
.,E3F6 A2 01    LDX #$01        SET UP FAKE FORWARD LINK
.,E3F8 8E FD 01 STX $01FD       
.,E3FB 8E FC 01 STX $01FC       
.,E3FE A2 19    LDX #$19        INIT INDEX TO TEMP STRING DESCRIPTORS
.,E400 86 16    STX $16         
.,E402 38       SEC
.,E403 20 9C FF JSR $FF9C
.,E406 86 2B    STX $2B
.,E408 84 2C    STY $2C
.,E40A 38       SEC
.,E40B 20 99 FF JSR $FF99
.,E40E 86 37    STX $37
.,E410 84 38    STY $38
.,E412 86 33    STX $33
.,E414 84 34    STY $34
.,E416 A0 00    LDY #$00
.,E418 98       TYA
.,E419 91 2B    STA ($2B),Y
.,E41B E6 2B    INC $2B
.,E41D D0 02    BNE $E421
.,E41F E6 2C    INC $2C
.,E421 60       RTS
.,E422 A5 2B    LDA $2B
.,E424 A4 2C    LDY $2C
.,E426 20 08 A4 JSR $A408
.,E429 A9 73    LDA #$73
.,E42B A0 E4    LDY #$E4
.,E42D 20 1E AB JSR $AB1E
.,E430 A5 37    LDA $37
.,E432 38       SEC
.,E433 E5 2B    SBC $2B
.,E435 AA       TAX
.,E436 A5 38    LDA $38
.,E438 E5 2C    SBC $2C
.,E43A 20 CD BD JSR $BDCD
.,E43D A9 60    LDA #$60
.,E43F A0 E4    LDY #$E4
.,E441 20 1E AB JSR $AB1E
.,E444 4C 44 A6 JMP $A644

.:E447 8B E3 83 A4 7C A5 1A A7
.:E44F E4 A7 86 AE

.,E453 A2 0B    LDX #$0B
.,E455 BD 47 E4 LDA $E447,X
.,E458 9D 00 03 STA $0300,X
.,E45B CA       DEX
.,E45C 10 F7    BPL $E455
.,E45E 60       RTS
