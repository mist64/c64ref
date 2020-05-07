- Fully Commented Commodore 64 ROM Disassembly (Marko Mäkelä)
-
- CBMBASIC and KERNAL
-
- The comments have been taken from
-    Commodore 64 BASIC/KERNAL ROM Disassembly
-      Version 1.0 (June 1994), by Marko Mäkelä
-
- The ROM is the 901227-03 version ($FF80 = 3).
-
- Converted and formatted by Michael Steil <mist64@mac.com>
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

.:A000 94 E3                    RESET
.:A002 7B E3                    Warm Start

                                *** CBMBASIC
.:A004 43 42 4D 42 41 53 49 43  

                                *** address table for commands
                                (address minus 1 used)
.:A00C 30 A8                    end
.:A00E 41 A7                    for
.:A010 1D AD                    next
.:A012 F7 A8                    data
.:A014 A4 AB                    input#
.:A016 BE AB                    input
.:A018 80 B0                    dim
.:A01A 05 AC                    read
.:A01C A4 A9                    let
.:A01E 9F A8                    goto
.:A020 70 A8                    run
.:A022 27 A9                    if
.:A024 1C A8                    restore
.:A026 82 A8                    gosub
.:A028 D1 A8                    return
.:A02A 3A A9                    rem
.:A02C 2E A8                    stop
.:A02E 4A A9                    on
.:A030 2C B8                    wait
.:A032 67 E1                    load
.:A034 55 E1                    save
.:A036 64 E1                    verify
.:A038 B2 B3                    def
.:A03A 23 B8                    poke
.:A03C 7F AA                    print#
.:A03E 9F AA                    print
.:A040 56 A8                    cont
.:A042 9B A6                    list
.:A044 5D A6                    clr
.:A046 85 AA                    cmd
.:A048 29 E1                    sys
.:A04A BD E1                    open
.:A04C C6 E1                    close
.:A04E 7A AB                    get
.:A050 41 A6                    new

                                *** address table for functions
.:A052 39 BC                    sgn
.:A054 CC BC                    int
.:A056 58 BC                    abs
.:A058 10 03                    usr
.:A05A 7D B3                    fre
.:A05C 9E B3                    pos
.:A05E 71 BF                    sqr
.:A060 97 E0                    rnd
.:A062 EA B9                    log
.:A064 ED BF                    exp
.:A066 64 E2                    cos
.:A068 6B E2                    sin
.:A06A B4 E2                    tan
.:A06C 0E E3                    atn
.:A06E 0D B8                    peek
.:A070 7C B7                    len
.:A072 65 B4                    str$
.:A074 AD B7                    val
.:A076 8B B7                    asc
.:A078 EC B6                    chr$
.:A07A 00 B7                    left$
.:A07C 2C B7                    right$
.:A07E 37 B7                    mid$

                                *** priority and address table for operators
                                (address minus 1 used)
.:A080 79 69 B8                 plus
.:A083 79 52 B8                 minus
.:A086 7B 2A BA                 multiply
.:A089 7B 11 BB                 divide
.:A08C 7F 7A BF                 power
.:A08F 50 E8 AF                 AND
.:A092 46 E5 AF                 OR
.:A095 7D B3 BF                 negative
.:A098 5A D3 AE                 NOT
.:A09B 64 15 B0                 greater / equal / less

                                *** table of commands
                                each ended with a +$80
.:A09E 45 4E C4                 end
.:A0A1 46 4F D2                 for
.:A0A4 4E 45 58 D4              next
.:A0A8 44 41 54 C1              data
.:A0AC 49 4E 50 55 54 A3        input#
.:A0B2 49 4E 50 55 D4           input
.:A0B7 44 49 CD                 dim
.:A0BA 52 45 41 C4              read
.:A0BE 4C 45 D4                 let
.:A0C1 47 4F 54 CF              goto
.:A0C5 52 55 CE                 run
.:A0C8 49 C6                    if
.:A0CA 52 45 53 54 4F 52 C5     restore
.:A0D1 47 4F 53 55 C2           gosub
.:A0D6 52 45 54 55 52 CE        return
.:A0DC 52 45 CD                 rem
.:A0DF 53 54 4F D0              stop
.:A0E3 4F CE                    on
.:A0E5 57 41 49 D4              wait
.:A0E9 4C 4F 41 C4              load
.:A0ED 53 41 56 C5              save
.:A0F1 56 45 52 49 46 D9        verify
.:A0F7 44 45 C6                 def
.:A0FA 50 4F 4B C5              poke
.:A0FE 50 52 49 4E 54 A3        print#
.:A104 50 52 49 4E D4           print
.:A109 43 4F 4E D4              cont
.:A10D 4C 49 53 D4              list
.:A111 43 4C D2                 clr
.:A114 43 4D C4                 cmd
.:A117 53 59 D3                 sys
.:A11A 4F 50 45 CE              open
.:A11E 43 4C 4F 53 C5           close
.:A123 47 45 D4                 get
.:A126 4E 45 D7                 new

                                *** table of functions
                                each ended with a +$80
.:A129 54 41 42 A8              tab(
.:A12D 54 CF                    to
.:A12F 46 CE                    fn
.:A131 53 50 43 A8              spc(
.:A135 54 48 45 CE              then
.:A139 4E 4F D4                 not
.:A13C 53 54 45 D0              step
.:A140 AB                       plus
.:A141 AD                       minus
.:A142 AA                       multiply
.:A143 AF                       divide
.:A144 DE                       power
.:A145 41 4E C4                 and
.:A148 4F D2                    on
.:A14A BE                       greater
.:A14B BD                       equal
.:A14C BC                       less
.:A14D 53 47 CE                 sgn
.:A150 49 4E D4                 int
.:A153 41 42 D3                 abs
.:A156 55 53 D2                 usr
.:A159 46 52 C5                 fre
.:A15C 50 4F D3                 pos
.:A15F 53 51 D2                 sqr
.:A162 52 4E C4                 rnd
.:A165 4C 4F C7                 log
.:A168 45 58 D0                 exp
.:A16B 43 4F D3                 cos
.:A16E 53 49 CE                 sin
.:A171 54 41 CE                 tan
.:A174 41 54 CE                 atn
.:A177 50 45 45 CB              peek
.:A17B 4C 45 CE                 len
.:A17E 53 54 52 A4              str$
.:A182 56 41 CC                 val
.:A185 41 53 C3                 asc
.:A188 43 48 52 A4              chr$
.:A18C 4C 45 46 54 A4           left$
.:A191 52 49 47 48 54 A4        right$
.:A197 4D 49 44 A4              mid$

                                *** other commands
.:A198 49 44 A4 47 CF           
.:A19D 00                       

                                *** table of error messages
                                each ended with a +$80
.:A19E 54 4F 4F 20 4D 41 4E 59  too many files
.:A1A6 20 46 49 4C 45 D3
.:A1AC 46 49 4C 45 20 4F 50 45  file open
.:A1B4 CE
.:A1B5 46 49 4C 45 20 4E 4F 54  file not open
.:A1BD 20 4F 50 45 CE
.:A1C2 46 49 4C 45 20 4E 4F 54  file not found
.:A1CA 20 46 4F 55 4E C4
.:A1D0 44 45 56 49 43 45 20 4E  device not present
.:A1D8 4F 54 20 50 52 45 53 45
.:A1E0 4E D4
.:A1E2 4E 4F 54 20 49 4E 50 55  not input file
.:A1EA 54 20 46 49 4C C5
.:A1F0 4E 4F 54 20 4F 55 54 50  not output file
.:A1F8 55 54 20 46 49 4C C5
.:A1FF 4D 49 53 53 49 4E 47 20  missing file name
.:A207 46 49 4C 45 20 4E 41 4D
.:A20F C5
.:A210 49 4C 4C 45 47 41 4C 20  illegal device number
.:A218 44 45 56 49 43 45 20 4E
.:A220 55 4D 42 45 D2
.:A225 4E 45 58 54 20 57 49 54  next without for
.:A22D 48 4F 55 54 20 46 4F D2
.:A235 53 59 4E 54 41 D8        syntax
.:A23B 52 45 54 55 52 4E 20 57  return without gosub
.:A243 49 54 48 4F 55 54 20 47
.:A24B 4F 53 55 C2
.:A24F 4F 55 54 20 4F 46 20 44  out of data
.:A257 41 54 C1
.:A25A 49 4C 4C 45 47 41 4C 20  illegal quantity
.:A262 51 55 41 4E 54 49 54 D9
.:A26A 4F 56 45 52 46 4C 4F D7  overflow
.:A272 4F 55 54 20 4F 46 20 4D  out of memory
.:A27A 45 4D 4F 52 D9
.:A27F 55 4E 44 45 46 27 44 20  undef'd statement
.:A287 53 54 41 54 45 4D 45 4E
.:A28F D4
.:A290 42 41 44 20 53 55 42 53  bad subscript
.:A298 43 52 49 50 D4
.:A29D 52 45 44 49 4D 27 44 20  redim'd array
.:A2A5 41 52 52 41 D9
.:A2AA 44 49 56 49 53 49 4F 4E  division by zero
.:A2B2 20 42 59 20 5A 45 52 CF
.:A2BA 49 4C 4C 45 47 41 4C 20  illegal direct
.:A2C2 44 49 52 45 43 D4
.:A2C8 54 59 50 45 20 4D 49 53  type mismatch
.:A2D0 4D 41 54 43 C8
.:A2D5 53 54 52 49 4E 47 20 54  string to long
.:A2DD 4F 4F 20 4C 4F 4E C7
.:A2E4 46 49 4C 45 20 44 41 54  file data
.:A2EC C1
.:A2ED 46 4F 52 4D 55 4C 41 20  formula too complex
.:A2D5 54 4F 4F 20 43 4F 4D 50
.:A2DD 4C 45 D8
.:A300 43 41 4E 27 54 20 43 4F  can't continue
.:A308 4E 54 49 4E 55 C5
.:A30E 55 4E 44 45 46 27 44 20  undef'd function
.:A316 46 55 4E 43 54 49 4F CE
.:A31E 56 45 52 49 46 D9        verify
.:A324 4C 4F 41 C4              load

                                *** error message address locations
.:A328 9E A1                    01 too many files
.:A32A AC A1                    02 file open
.:A32C B5 A1                    03 file not open
.:A32E C2 A1                    04 file not found
.:A330 D0 A1                    05 device not present
.:A332 E2 A1                    06 not input file
.:A334 F0 A1                    07 not output file
.:A336 FF A1                    08 missing file name
.:A338 10 A2                    09 illegal device number
.:A33A 25 A2                    0A next without for
.:A33C 35 A2                    0B syntax
.:A33E 3B A2                    0C return without gosub
.:A340 4F A2                    0D out of data
.:A342 5A A2                    0E illegal quantity
.:A344 6A A2                    0F overflow
.:A346 72 A2                    10 out of memory
.:A348 7F A2                    11 undef'd statment
.:A34A 90 A2                    12 bad subscript
.:A34C 9D A2                    13 redim'd array
.:A34E AA A2                    14 devision by zero
.:A350 BA A2                    15 illegal direct
.:A352 C8 A2                    16 type mismatch
.:A354 D5 A2                    17 string too long
.:A356 E4 A2                    18 file data
.:A358 ED A2                    19 formula too complex
.:A35A 00 A3                    1A can't continue
.:A35C 0E A3                    1B undef'd function
.:A35E 1E A3                    1C verify
.:A360 24 A3                    1D load
.:A362 83 A3                    1E break

                                *** other messages
.:A364 0D 4F 4B 0D 00           ok
.:A369 20 20 45 52 52 4F 52 00  error
.:A371 20 49 4E 20 00           in
.:A376 0D 0A 52 45 41 44 59 2E  ready.
.:A37D 0D 0A 00
.:A381 0D 0A 42 52 45 41 4B 00  break
.:A389 A0

                                *** search for "for" blocks on stack
.,A38A BA       TSX             
.,A38B E8       INX             
.,A38C E8       INX             
.,A38D E8       INX             
.,A38E E8       INX             
.,A38F BD 01 01 LDA $0101,X     
.,A392 C9 81    CMP #$81        for block code
.,A394 D0 21    BNE $A3B7       
.,A396 A5 4A    LDA $4A         
.,A398 D0 0A    BNE $A3A4       
.,A39A BD 02 01 LDA $0102,X     
.,A39D 85 49    STA $49         
.,A39F BD 03 01 LDA $0103,X     
.,A3A2 85 4A    STA $4A         
.,A3A4 DD 03 01 CMP $0103,X     
.,A3A7 D0 07    BNE $A3B0       
.,A3A9 A5 49    LDA $49         
.,A3AB DD 02 01 CMP $0102,X     
.,A3AE F0 07    BEQ $A3B7       
.,A3B0 8A       TXA             
.,A3B1 18       CLC             
.,A3B2 69 12    ADC #$12        
.,A3B4 AA       TAX             
.,A3B5 D0 D8    BNE $A38F       
.,A3B7 60       RTS             

                                *** move bytes after check for space
.,A3B8 20 08 A4 JSR $A408       
.,A3BB 85 31    STA $31         
.,A3BD 84 32    STY $32         

                                *** move bytes routine
                                $5F/$60 source start address
                                $5A/$5B source end address
                                $58/$59 destination end address
.,A3BF 38       SEC             
.,A3C0 A5 5A    LDA $5A         
.,A3C2 E5 5F    SBC $5F         
.,A3C4 85 22    STA $22         
.,A3C6 A8       TAY             
.,A3C7 A5 5B    LDA $5B         
.,A3C9 E5 60    SBC $60         
.,A3CB AA       TAX             
.,A3CC E8       INX             
.,A3CD 98       TYA             
.,A3CE F0 23    BEQ $A3F3       
.,A3D0 A5 5A    LDA $5A         
.,A3D2 38       SEC             
.,A3D3 E5 22    SBC $22         
.,A3D5 85 5A    STA $5A         
.,A3D7 B0 03    BCS $A3DC       
.,A3D9 C6 5B    DEC $5B         
.,A3DB 38       SEC             
.,A3DC A5 58    LDA $58         
.,A3DE E5 22    SBC $22         
.,A3E0 85 58    STA $58         
.,A3E2 B0 08    BCS $A3EC       
.,A3E4 C6 59    DEC $59         
.,A3E6 90 04    BCC $A3EC       
.,A3E8 B1 5A    LDA ($5A),Y     
.,A3EA 91 58    STA ($58),Y     
.,A3EC 88       DEY             
.,A3ED D0 F9    BNE $A3E8       
.,A3EF B1 5A    LDA ($5A),Y     
.,A3F1 91 58    STA ($58),Y     
.,A3F3 C6 5B    DEC $5B         
.,A3F5 C6 59    DEC $59         
.,A3F7 CA       DEX             
.,A3F8 D0 F2    BNE $A3EC       
.,A3FA 60       RTS             

                                *** test for 2 * A bytes free on stack
.,A3FB 0A       ASL             
.,A3FC 69 3E    ADC #$3E        
.,A3FE B0 35    BCS $A435       
.,A400 85 22    STA $22         
.,A402 BA       TSX             
.,A403 E4 22    CPX $22         
.,A405 90 2E    BCC $A435       
.,A407 60       RTS             

                                *** array area overflow check
.,A408 C4 34    CPY $34         
.,A40A 90 28    BCC $A434       
.,A40C D0 04    BNE $A412       
.,A40E C5 33    CMP $33         
.,A410 90 22    BCC $A434       
.,A412 48       PHA             
.,A413 A2 09    LDX #$09        
.,A415 98       TYA             
.,A416 48       PHA             
.,A417 B5 57    LDA $57,X       
.,A419 CA       DEX             
.,A41A 10 FA    BPL $A416       
.,A41C 20 26 B5 JSR $B526       
.,A41F A2 F7    LDX #$F7        
.,A421 68       PLA             
.,A422 95 61    STA $61,X       
.,A424 E8       INX             
.,A425 30 FA    BMI $A421       
.,A427 68       PLA             
.,A428 A8       TAY             
.,A429 68       PLA             
.,A42A C4 34    CPY $34         
.,A42C 90 06    BCC $A434       
.,A42E D0 05    BNE $A435       
.,A430 C5 33    CMP $33         
.,A432 B0 01    BCS $A435       
.,A434 60       RTS             

                                *** out of memory error
.,A435 A2 10    LDX #$10        error number

                                *** handle error messages
.,A437 6C 00 03 JMP ($0300)     normally A43A

                                *** standard error message handler
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
.,A465 A9 69    LDA #$69        low  A369
.,A467 A0 A3    LDY #$A3        high A369
.,A469 20 1E AB JSR $AB1E       
.,A46C A4 3A    LDY $3A         
.,A46E C8       INY             
.,A46F F0 03    BEQ $A474       
.,A471 20 C2 BD JSR $BDC2       
.,A474 A9 76    LDA #$76        low A376
.,A476 A0 A3    LDY #$A3        low A376
.,A478 20 1E AB JSR $AB1E       
.,A47B A9 80    LDA #$80        
.,A47D 20 90 FF JSR $FF90       
.,A480 6C 02 03 JMP ($0302)     normally A483

                                *** standard warm start routine
.,A483 20 60 A5 JSR $A560       
.,A486 86 7A    STX $7A         
.,A488 84 7B    STY $7B         
.,A48A 20 73 00 JSR $0073       
.,A48D AA       TAX             
.,A48E F0 F0    BEQ $A480       
.,A490 A2 FF    LDX #$FF        
.,A492 86 3A    STX $3A         
.,A494 90 06    BCC $A49C       
.,A496 20 79 A5 JSR $A579       
.,A499 4C E1 A7 JMP $A7E1       

                                *** handle insert/delete basic lines
.,A49C 20 6B A9 JSR $A96B       
.,A49F 20 79 A5 JSR $A579       
.,A4A2 84 0B    STY $0B         
.,A4A4 20 13 A6 JSR $A613       
.,A4A7 90 44    BCC $A4ED       

                                *** delete old line
.,A4A9 A0 01    LDY #$01        
.,A4AB B1 5F    LDA ($5F),Y     
.,A4AD 85 23    STA $23         
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
.,A4DF B1 22    LDA ($22),Y     
.,A4E1 91 24    STA ($24),Y     
.,A4E3 C8       INY             
.,A4E4 D0 F9    BNE $A4DF       
.,A4E6 E6 23    INC $23         
.,A4E8 E6 25    INC $25         
.,A4EA CA       DEX             
.,A4EB D0 F2    BNE $A4DF       

                                *** insert new line
.,A4ED 20 59 A6 JSR $A659       
.,A4F0 20 33 A5 JSR $A533       
.,A4F3 AD 00 02 LDA $0200       
.,A4F6 F0 88    BEQ $A480       
.,A4F8 18       CLC             
.,A4F9 A5 2D    LDA $2D         
.,A4FB 85 5A    STA $5A         
.,A4FD 65 0B    ADC $0B         
.,A4FF 85 58    STA $58         
.,A501 A4 2E    LDY $2E         
.,A503 84 5B    STY $5B         
.,A505 90 01    BCC $A508       
.,A507 C8       INY             
.,A508 84 59    STY $59         
.,A50A 20 B8 A3 JSR $A3B8       
.,A50D A5 14    LDA $14         
.,A50F A4 15    LDY $15         
.,A511 8D FE 01 STA $01FE       
.,A514 8C FF 01 STY $01FF       
.,A517 A5 31    LDA $31         
.,A519 A4 32    LDY $32         
.,A51B 85 2D    STA $2D         
.,A51D 84 2E    STY $2E         
.,A51F A4 0B    LDY $0B         
.,A521 88       DEY             
.,A522 B9 FC 01 LDA $01FC,Y     
.,A525 91 5F    STA ($5F),Y     
.,A527 88       DEY             
.,A528 10 F8    BPL $A522       
.,A52A 20 59 A6 JSR $A659       
.,A52D 20 33 A5 JSR $A533       
.,A530 4C 80 A4 JMP $A480       

                                *** relink basic program
.,A533 A5 2B    LDA $2B         
.,A535 A4 2C    LDY $2C         
.,A537 85 22    STA $22         
.,A539 84 23    STY $23         
.,A53B 18       CLC             
.,A53C A0 01    LDY #$01        
.,A53E B1 22    LDA ($22),Y     
.,A540 F0 1D    BEQ $A55F       
.,A542 A0 04    LDY #$04        
.,A544 C8       INY             
.,A545 B1 22    LDA ($22),Y     
.,A547 D0 FB    BNE $A544       
.,A549 C8       INY             
.,A54A 98       TYA             
.,A54B 65 22    ADC $22         
.,A54D AA       TAX             
.,A54E A0 00    LDY #$00        
.,A550 91 22    STA ($22),Y     
.,A552 A5 23    LDA $23         
.,A554 69 00    ADC #$00        
.,A556 C8       INY             
.,A557 91 22    STA ($22),Y     
.,A559 86 22    STX $22         
.,A55B 85 23    STA $23         
.,A55D 90 DD    BCC $A53C       
.,A55F 60       RTS             

                                *** get statement into buffer
.,A560 A2 00    LDX #$00        
.,A562 20 12 E1 JSR $E112       
.,A565 C9 0D    CMP #$0D        
.,A567 F0 0D    BEQ $A576       
.,A569 9D 00 02 STA $0200,X     
.,A56C E8       INX             
.,A56D E0 59    CPX #$59        
.,A56F 90 F1    BCC $A562       
.,A571 A2 17    LDX #$17        error number
.,A573 4C 37 A4 JMP $A437       
.,A576 4C CA AA JMP $AACA       goto end of line

                                *** crunch tokens
.,A579 6C 04 03 JMP ($0304)     normally A57C

                                *** standard token cruncher
.,A57C A6 7A    LDX $7A         
.,A57E A0 04    LDY #$04        
.,A580 84 0F    STY $0F         
.,A582 BD 00 02 LDA $0200,X     
.,A585 10 07    BPL $A58E       
.,A587 C9 FF    CMP #$FF        PI
.,A589 F0 3E    BEQ $A5C9       
.,A58B E8       INX             
.,A58C D0 F4    BNE $A582       
.,A58E C9 20    CMP #$20        space
.,A590 F0 37    BEQ $A5C9       
.,A592 85 08    STA $08         
.,A594 C9 22    CMP #$22        quote mark
.,A596 F0 56    BEQ $A5EE       
.,A598 24 0F    BIT $0F         
.,A59A 70 2D    BVS $A5C9       
.,A59C C9 3F    CMP #$3F        question mark
.,A59E D0 04    BNE $A5A4       
.,A5A0 A9 99    LDA #$99        PRINT code
.,A5A2 D0 25    BNE $A5C9       
.,A5A4 C9 30    CMP #$30        0
.,A5A6 90 04    BCC $A5AC       
.,A5A8 C9 3C    CMP #$3C        
.,A5AA 90 1D    BCC $A5C9       
.,A5AC 84 71    STY $71         
.,A5AE A0 00    LDY #$00        
.,A5B0 84 0B    STY $0B         
.,A5B2 88       DEY             
.,A5B3 86 7A    STX $7A         
.,A5B5 CA       DEX             
.,A5B6 C8       INY             
.,A5B7 E8       INX             
.,A5B8 BD 00 02 LDA $0200,X     
.,A5BB 38       SEC             
.,A5BC F9 9E A0 SBC $A09E,Y     
.,A5BF F0 F5    BEQ $A5B6       
.,A5C1 C9 80    CMP #$80        
.,A5C3 D0 30    BNE $A5F5       
.,A5C5 05 0B    ORA $0B         
.,A5C7 A4 71    LDY $71         
.,A5C9 E8       INX             
.,A5CA C8       INY             
.,A5CB 99 FB 01 STA $01FB,Y     
.,A5CE B9 FB 01 LDA $01FB,Y     
.,A5D1 F0 36    BEQ $A609       
.,A5D3 38       SEC             
.,A5D4 E9 3A    SBC #$3A        colon
.,A5D6 F0 04    BEQ $A5DC       
.,A5D8 C9 49    CMP #$49        DATA code
.,A5DA D0 02    BNE $A5DE       
.,A5DC 85 0F    STA $0F         
.,A5DE 38       SEC             
.,A5DF E9 55    SBC #$55        REM code
.,A5E1 D0 9F    BNE $A582       
.,A5E3 85 08    STA $08         
.,A5E5 BD 00 02 LDA $0200,X     
.,A5E8 F0 DF    BEQ $A5C9       
.,A5EA C5 08    CMP $08         
.,A5EC F0 DB    BEQ $A5C9       
.,A5EE C8       INY             
.,A5EF 99 FB 01 STA $01FB,Y     
.,A5F2 E8       INX             
.,A5F3 D0 F0    BNE $A5E5       
.,A5F5 A6 7A    LDX $7A         
.,A5F7 E6 0B    INC $0B         
.,A5F9 C8       INY             
.,A5FA B9 9D A0 LDA $A09D,Y     
.,A5FD 10 FA    BPL $A5F9       
.,A5FF B9 9E A0 LDA $A09E,Y     
.,A602 D0 B4    BNE $A5B8       
.,A604 BD 00 02 LDA $0200,X     
.,A607 10 BE    BPL $A5C7       
.,A609 99 FD 01 STA $01FD,Y     
.,A60C C6 7B    DEC $7B         
.,A60E A9 FF    LDA #$FF        
.,A610 85 7A    STA $7A         
.,A612 60       RTS             

                                *** search for a line in a program
.,A613 A5 2B    LDA $2B         
.,A615 A6 2C    LDX $2C         
.,A617 A0 01    LDY #$01        
.,A619 85 5F    STA $5F         
.,A61B 86 60    STX $60         
.,A61D B1 5F    LDA ($5F),Y     
.,A61F F0 1F    BEQ $A640       
.,A621 C8       INY             
.,A622 C8       INY             
.,A623 A5 15    LDA $15         
.,A625 D1 5F    CMP ($5F),Y     
.,A627 90 18    BCC $A641       
.,A629 F0 03    BEQ $A62E       
.,A62B 88       DEY             
.,A62C D0 09    BNE $A637       
.,A62E A5 14    LDA $14         
.,A630 88       DEY             
.,A631 D1 5F    CMP ($5F),Y     
.,A633 90 0C    BCC $A641       
.,A635 F0 0A    BEQ $A641       
.,A637 88       DEY             
.,A638 B1 5F    LDA ($5F),Y     
.,A63A AA       TAX             
.,A63B 88       DEY             
.,A63C B1 5F    LDA ($5F),Y     
.,A63E B0 D7    BCS $A617       
.,A640 18       CLC             
.,A641 60       RTS             

                                *** NEW command
.,A642 D0 FD    BNE $A641       
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
.,A659 20 8E A6 JSR $A68E       
.,A65C A9 00    LDA #$00        

                                *** CLR command
.,A65E D0 2D    BNE $A68D       
.,A660 20 E7 FF JSR $FFE7       
.,A663 A5 37    LDA $37         
.,A665 A4 38    LDY $38         
.,A667 85 33    STA $33         
.,A669 84 34    STY $34         
.,A66B A5 2D    LDA $2D         
.,A66D A4 2E    LDY $2E         
.,A66F 85 2F    STA $2F         
.,A671 84 30    STY $30         
.,A673 85 31    STA $31         
.,A675 84 32    STY $32         
.,A677 20 1D A8 JSR $A81D       

                                *** reset stack and program pointers
.,A67A A2 19    LDX #$19        
.,A67C 86 16    STX $16         
.,A67E 68       PLA             
.,A67F A8       TAY             
.,A680 68       PLA             
.,A681 A2 FA    LDX #$FA        
.,A683 9A       TXS             
.,A684 48       PHA             
.,A685 98       TYA             
.,A686 48       PHA             
.,A687 A9 00    LDA #$00        
.,A689 85 3E    STA $3E         
.,A68B 85 10    STA $10         
.,A68D 60       RTS             

                                *** set current character pointer to start of basic - 1
.,A68E 18       CLC             
.,A68F A5 2B    LDA $2B         
.,A691 69 FF    ADC #$FF        
.,A693 85 7A    STA $7A         
.,A695 A5 2C    LDA $2C         
.,A697 69 FF    ADC #$FF        
.,A699 85 7B    STA $7B         
.,A69B 60       RTS             

                                *** LIST command
.,A69C 90 06    BCC $A6A4       
.,A69E F0 04    BEQ $A6A4       
.,A6A0 C9 AB    CMP #$AB        
.,A6A2 D0 E9    BNE $A68D       
.,A6A4 20 6B A9 JSR $A96B       
.,A6A7 20 13 A6 JSR $A613       
.,A6AA 20 79 00 JSR $0079       
.,A6AD F0 0C    BEQ $A6BB       
.,A6AF C9 AB    CMP #$AB        
.,A6B1 D0 8E    BNE $A641       
.,A6B3 20 73 00 JSR $0073       
.,A6B6 20 6B A9 JSR $A96B       
.,A6B9 D0 86    BNE $A641       
.,A6BB 68       PLA             
.,A6BC 68       PLA             
.,A6BD A5 14    LDA $14         
.,A6BF 05 15    ORA $15         
.,A6C1 D0 06    BNE $A6C9       
.,A6C3 A9 FF    LDA #$FF        
.,A6C5 85 14    STA $14         
.,A6C7 85 15    STA $15         

                                *** list lines from $5F/$60 to $14/$15
.,A6C9 A0 01    LDY #$01        
.,A6CB 84 0F    STY $0F         
.,A6CD B1 5F    LDA ($5F),Y     
.,A6CF F0 43    BEQ $A714       
.,A6D1 20 2C A8 JSR $A82C       
.,A6D4 20 D7 AA JSR $AAD7       
.,A6D7 C8       INY             
.,A6D8 B1 5F    LDA ($5F),Y     
.,A6DA AA       TAX             
.,A6DB C8       INY             
.,A6DC B1 5F    LDA ($5F),Y     
.,A6DE C5 15    CMP $15         
.,A6E0 D0 04    BNE $A6E6       
.,A6E2 E4 14    CPX $14         
.,A6E4 F0 02    BEQ $A6E8       
.,A6E6 B0 2C    BCS $A714       
.,A6E8 84 49    STY $49         
.,A6EA 20 CD BD JSR $BDCD       
.,A6ED A9 20    LDA #$20        
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
.,A705 D0 10    BNE $A717       
.,A707 A8       TAY             
.,A708 B1 5F    LDA ($5F),Y     
.,A70A AA       TAX             
.,A70B C8       INY             
.,A70C B1 5F    LDA ($5F),Y     
.,A70E 86 5F    STX $5F         
.,A710 85 60    STA $60         
.,A712 D0 B5    BNE $A6C9       
.,A714 4C 86 E3 JMP $E386       

                                *** print tokens routine
.,A717 6C 06 03 JMP ($0306)     normally A71A

                                *** standard token printer
.,A71A 10 D7    BPL $A6F3       
.,A71C C9 FF    CMP #$FF        
.,A71E F0 D3    BEQ $A6F3       
.,A720 24 0F    BIT $0F         
.,A722 30 CF    BMI $A6F3       
.,A724 38       SEC             
.,A725 E9 7F    SBC #$7F        
.,A727 AA       TAX             
.,A728 84 49    STY $49         
.,A72A A0 FF    LDY #$FF        
.,A72C CA       DEX             
.,A72D F0 08    BEQ $A737       
.,A72F C8       INY             
.,A730 B9 9E A0 LDA $A09E,Y     
.,A733 10 FA    BPL $A72F       
.,A735 30 F5    BMI $A72C       

                                *** print keyword
.,A737 C8       INY             
.,A738 B9 9E A0 LDA $A09E,Y     
.,A73B 30 B2    BMI $A6EF       
.,A73D 20 47 AB JSR $AB47       
.,A740 D0 F5    BNE $A737       

                                *** FOR command
.,A742 A9 80    LDA #$80        
.,A744 85 10    STA $10         
.,A746 20 A5 A9 JSR $A9A5       
.,A749 20 8A A3 JSR $A38A       
.,A74C D0 05    BNE $A753       
.,A74E 8A       TXA             
.,A74F 69 0F    ADC #$0F        
.,A751 AA       TAX             
.,A752 9A       TXS             
.,A753 68       PLA             
.,A754 68       PLA             
.,A755 A9 09    LDA #$09        
.,A757 20 FB A3 JSR $A3FB       
.,A75A 20 06 A9 JSR $A906       
.,A75D 18       CLC             
.,A75E 98       TYA             
.,A75F 65 7A    ADC $7A         
.,A761 48       PHA             
.,A762 A5 7B    LDA $7B         
.,A764 69 00    ADC #$00        
.,A766 48       PHA             
.,A767 A5 3A    LDA $3A         
.,A769 48       PHA             
.,A76A A5 39    LDA $39         
.,A76C 48       PHA             
.,A76D A9 A4    LDA #$A4        
.,A76F 20 FF AE JSR $AEFF       
.,A772 20 8D AD JSR $AD8D       
.,A775 20 8A AD JSR $AD8A       
.,A778 A5 66    LDA $66         
.,A77A 09 7F    ORA #$7F        
.,A77C 25 62    AND $62         
.,A77E 85 62    STA $62         
.,A780 A9 8B    LDA #$8B        low  A78B
.,A782 A0 A7    LDY #$A7        high A78B
.,A784 85 22    STA $22         
.,A786 84 23    STY $23         
.,A788 4C 43 AE JMP $AE43       
.,A78B A9 BC    LDA #$BC        low  B9BC
.,A78D A0 B9    LDY #$B9        high B9BC
.,A78F 20 A2 BB JSR $BBA2       
.,A792 20 79 00 JSR $0079       
.,A795 C9 A9    CMP #$A9        
.,A797 D0 06    BNE $A79F       
.,A799 20 73 00 JSR $0073       
.,A79C 20 8A AD JSR $AD8A       
.,A79F 20 2B BC JSR $BC2B       
.,A7A2 20 38 AE JSR $AE38       
.,A7A5 A5 4A    LDA $4A         
.,A7A7 48       PHA             
.,A7A8 A5 49    LDA $49         
.,A7AA 48       PHA             
.,A7AB A9 81    LDA #$81        FOR block code
.,A7AD 48       PHA             

                                *** execute next statement
.,A7AE 20 2C A8 JSR $A82C       
.,A7B1 A5 7A    LDA $7A         
.,A7B3 A4 7B    LDY $7B         
.,A7B5 C0 02    CPY #$02        
.,A7B7 EA       NOP             
.,A7B8 F0 04    BEQ $A7BE       
.,A7BA 85 3D    STA $3D         
.,A7BC 84 3E    STY $3E         
.,A7BE A0 00    LDY #$00        
.,A7C0 B1 7A    LDA ($7A),Y     
.,A7C2 D0 43    BNE $A807       
.,A7C4 A0 02    LDY #$02        
.,A7C6 B1 7A    LDA ($7A),Y     
.,A7C8 18       CLC             
.,A7C9 D0 03    BNE $A7CE       
.,A7CB 4C 4B A8 JMP $A84B       
.,A7CE C8       INY             
.,A7CF B1 7A    LDA ($7A),Y     
.,A7D1 85 39    STA $39         
.,A7D3 C8       INY             
.,A7D4 B1 7A    LDA ($7A),Y     
.,A7D6 85 3A    STA $3A         
.,A7D8 98       TYA             
.,A7D9 65 7A    ADC $7A         
.,A7DB 85 7A    STA $7A         
.,A7DD 90 02    BCC $A7E1       
.,A7DF E6 7B    INC $7B         
.,A7E1 6C 08 03 JMP ($0308)     normally A7E4

                                *** execute a statement
.,A7E4 20 73 00 JSR $0073       
.,A7E7 20 ED A7 JSR $A7ED       
.,A7EA 4C AE A7 JMP $A7AE       

                                *** execute command in A
.,A7ED F0 3C    BEQ $A82B       
.,A7EF E9 80    SBC #$80        
.,A7F1 90 11    BCC $A804       
.,A7F3 C9 23    CMP #$23        
.,A7F5 B0 17    BCS $A80E       
.,A7F7 0A       ASL             
.,A7F8 A8       TAY             
.,A7F9 B9 0D A0 LDA $A00D,Y     
.,A7FC 48       PHA             
.,A7FD B9 0C A0 LDA $A00C,Y     
.,A800 48       PHA             
.,A801 4C 73 00 JMP $0073       
.,A804 4C A5 A9 JMP $A9A5       
.,A807 C9 3A    CMP #$3A        colon
.,A809 F0 D6    BEQ $A7E1       
.,A80B 4C 08 AF JMP $AF08       
.,A80E C9 4B    CMP #$4B        GO code
.,A810 D0 F9    BNE $A80B       
.,A812 20 73 00 JSR $0073       
.,A815 A9 A4    LDA #$A4        TO code
.,A817 20 FF AE JSR $AEFF       
.,A81A 4C A0 A8 JMP $A8A0       do GOTO

                                *** RESTORE command
.,A81D 38       SEC             
.,A81E A5 2B    LDA $2B         
.,A820 E9 01    SBC #$01        
.,A822 A4 2C    LDY $2C         
.,A824 B0 01    BCS $A827       
.,A826 88       DEY             
.,A827 85 41    STA $41         
.,A829 84 42    STY $42         
.,A82B 60       RTS             
.,A82C 20 E1 FF JSR $FFE1       test stop key

                                *** STOP command
.,A82F B0 01    BCS $A832       

                                *** END command
.,A831 18       CLC             
.,A832 D0 3C    BNE $A870       
.,A834 A5 7A    LDA $7A         
.,A836 A4 7B    LDY $7B         
.,A838 A6 3A    LDX $3A         
.,A83A E8       INX             
.,A83B F0 0C    BEQ $A849       
.,A83D 85 3D    STA $3D         
.,A83F 84 3E    STY $3E         
.,A841 A5 39    LDA $39         
.,A843 A4 3A    LDY $3A         
.,A845 85 3B    STA $3B         
.,A847 84 3C    STY $3C         
.,A849 68       PLA             
.,A84A 68       PLA             
.,A84B A9 81    LDA #$81        low  A381
.,A84D A0 A3    LDY #$A3        high A381
.,A84F 90 03    BCC $A854       
.,A851 4C 69 A4 JMP $A469       
.,A854 4C 86 E3 JMP $E386       

                                *** CONT command
.,A857 D0 17    BNE $A870       
.,A859 A2 1A    LDX #$1A        error number
.,A85B A4 3E    LDY $3E         
.,A85D D0 03    BNE $A862       
.,A85F 4C 37 A4 JMP $A437       
.,A862 A5 3D    LDA $3D         
.,A864 85 7A    STA $7A         
.,A866 84 7B    STY $7B         
.,A868 A5 3B    LDA $3B         
.,A86A A4 3C    LDY $3C         
.,A86C 85 39    STA $39         
.,A86E 84 3A    STY $3A         
.,A870 60       RTS             

                                *** RUN command
.,A871 08       PHP             
.,A872 A9 00    LDA #$00        
.,A874 20 90 FF JSR $FF90       
.,A877 28       PLP             
.,A878 D0 03    BNE $A87D       
.,A87A 4C 59 A6 JMP $A659       
.,A87D 20 60 A6 JSR $A660       do CLR
.,A880 4C 97 A8 JMP $A897       do GOTO

                                *** GOSUB command
.,A883 A9 03    LDA #$03        
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

                                *** GOTO command
.,A8A0 20 6B A9 JSR $A96B       
.,A8A3 20 09 A9 JSR $A909       
.,A8A6 38       SEC             
.,A8A7 A5 39    LDA $39         
.,A8A9 E5 14    SBC $14         
.,A8AB A5 3A    LDA $3A         
.,A8AD E5 15    SBC $15         
.,A8AF B0 0B    BCS $A8BC       
.,A8B1 98       TYA             
.,A8B2 38       SEC             
.,A8B3 65 7A    ADC $7A         
.,A8B5 A6 7B    LDX $7B         
.,A8B7 90 07    BCC $A8C0       
.,A8B9 E8       INX             
.,A8BA B0 04    BCS $A8C0       
.,A8BC A5 2B    LDA $2B         
.,A8BE A6 2C    LDX $2C         
.,A8C0 20 17 A6 JSR $A617       
.,A8C3 90 1E    BCC $A8E3       
.,A8C5 A5 5F    LDA $5F         
.,A8C7 E9 01    SBC #$01        
.,A8C9 85 7A    STA $7A         
.,A8CB A5 60    LDA $60         
.,A8CD E9 00    SBC #$00        
.,A8CF 85 7B    STA $7B         
.,A8D1 60       RTS             

                                *** RETURN command
.,A8D2 D0 FD    BNE $A8D1       
.,A8D4 A9 FF    LDA #$FF        
.,A8D6 85 4A    STA $4A         
.,A8D8 20 8A A3 JSR $A38A       
.,A8DB 9A       TXS             
.,A8DC C9 8D    CMP #$8D        
.,A8DE F0 0B    BEQ $A8EB       
.,A8E0 A2 0C    LDX #$0C        
.:A8E2 2C       .BYTE $2C       
.,A8E3 A2 11    LDX #$02        
.,A8E5 4C 37 A4 JMP $A437       
.,A8E8 4C 08 AF JMP $AF08       

                                *** remove GOSUB block from stack
.,A8EB 68       PLA             
.,A8EC 68       PLA             
.,A8ED 85 39    STA $39         
.,A8EF 68       PLA             
.,A8F0 85 3A    STA $3A         
.,A8F2 68       PLA             
.,A8F3 85 7A    STA $7A         
.,A8F5 68       PLA             
.,A8F6 85 7B    STA $7B         

                                *** DATA command
.,A8F8 20 06 A9 JSR $A906       
.,A8FB 98       TYA             
.,A8FC 18       CLC             
.,A8FD 65 7A    ADC $7A         
.,A8FF 85 7A    STA $7A         
.,A901 90 02    BCC $A905       
.,A903 E6 7B    INC $7B         
.,A905 60       RTS             

                                *** get end of statement
.,A906 A2 3A    LDX #$3A        colon
.:A908 2C       .BYTE $2C       

                                *** get end of line
.,A909 A2 00    LDX #$00        
.,A90B 86 07    STX $07         
.,A90D A0 00    LDY #$00        
.,A90F 84 08    STY $08         
.,A911 A5 08    LDA $08         
.,A913 A6 07    LDX $07         
.,A915 85 07    STA $07         
.,A917 86 08    STX $08         
.,A919 B1 7A    LDA ($7A),Y     
.,A91B F0 E8    BEQ $A905       
.,A91D C5 08    CMP $08         
.,A91F F0 E4    BEQ $A905       
.,A921 C8       INY             
.,A922 C9 22    CMP #$22        quote mark
.,A924 D0 F3    BNE $A919       
.,A926 F0 E9    BEQ $A911       

                                *** IF command
.,A928 20 9E AD JSR $AD9E       
.,A92B 20 79 00 JSR $0079       
.,A92E C9 89    CMP #$89        
.,A930 F0 05    BEQ $A937       
.,A932 A9 A7    LDA #$A7        
.,A934 20 FF AE JSR $AEFF       
.,A937 A5 61    LDA $61         
.,A939 D0 05    BNE $A940       

                                *** REM command
.,A93B 20 09 A9 JSR $A909       
.,A93E F0 BB    BEQ $A8FB       

                                *** THEN part of IF
.,A940 20 79 00 JSR $0079       
.,A943 B0 03    BCS $A948       
.,A945 4C A0 A8 JMP $A8A0       do GOTO
.,A948 4C ED A7 JMP $A7ED       

                                *** ON command
.,A94B 20 9E B7 JSR $B79E       
.,A94E 48       PHA             
.,A94F C9 8D    CMP #$8D        GOSUB code
.,A951 F0 04    BEQ $A957       
.,A953 C9 89    CMP #$89        GOTO code
.,A955 D0 91    BNE $A8E8       
.,A957 C6 65    DEC $65         
.,A959 D0 04    BNE $A95F       
.,A95B 68       PLA             
.,A95C 4C EF A7 JMP $A7EF       
.,A95F 20 73 00 JSR $0073       
.,A962 20 6B A9 JSR $A96B       
.,A965 C9 2C    CMP #$2C        comma
.,A967 F0 EE    BEQ $A957       
.,A969 68       PLA             
.,A96A 60       RTS             

                                *** get decimal number into $14/$15
.,A96B A2 00    LDX #$00        
.,A96D 86 14    STX $14         
.,A96F 86 15    STX $15         
.,A971 B0 F7    BCS $A96A       
.,A973 E9 2F    SBC #$2F        
.,A975 85 07    STA $07         
.,A977 A5 15    LDA $15         
.,A979 85 22    STA $22         
.,A97B C9 19    CMP #$19        
.,A97D B0 D4    BCS $A953       
.,A97F A5 14    LDA $14         
.,A981 0A       ASL             times 2
.,A982 26 22    ROL $22         
.,A984 0A       ASL             times 2
.,A985 26 22    ROL $22         
.,A987 65 14    ADC $14         add original
.,A989 85 14    STA $14         
.,A98B A5 22    LDA $22         
.,A98D 65 15    ADC $15         
.,A98F 85 15    STA $15         
.,A991 06 14    ASL $14         times 2
.,A993 26 15    ROL $15         = times 10 overall
.,A995 A5 14    LDA $14         
.,A997 65 07    ADC $07         
.,A999 85 14    STA $14         
.,A99B 90 02    BCC $A99F       
.,A99D E6 15    INC $15         
.,A99F 20 73 00 JSR $0073       
.,A9A2 4C 71 A9 JMP $A971       

                                *** LET command
.,A9A5 20 8B B0 JSR $B08B       
.,A9A8 85 49    STA $49         
.,A9AA 84 4A    STY $4A         
.,A9AC A9 B2    LDA #$B2        equals code
.,A9AE 20 FF AE JSR $AEFF       
.,A9B1 A5 0E    LDA $0E         
.,A9B3 48       PHA             
.,A9B4 A5 0D    LDA $0D         
.,A9B6 48       PHA             
.,A9B7 20 9E AD JSR $AD9E       
.,A9BA 68       PLA             
.,A9BB 2A       ROL             
.,A9BC 20 90 AD JSR $AD90       
.,A9BF D0 18    BNE $A9D9       
.,A9C1 68       PLA             
.,A9C2 10 12    BPL $A9D6       

                                *** assign to integer
.,A9C4 20 1B BC JSR $BC1B       
.,A9C7 20 BF B1 JSR $B1BF       
.,A9CA A0 00    LDY #$00        
.,A9CC A5 64    LDA $64         
.,A9CE 91 49    STA ($49),Y     
.,A9D0 C8       INY             
.,A9D1 A5 65    LDA $65         
.,A9D3 91 49    STA ($49),Y     
.,A9D5 60       RTS             

                                *** assign to float
.,A9D6 4C D0 BB JMP $BBD0       

                                *** assign to string
.,A9D9 68       PLA             
.,A9DA A4 4A    LDY $4A         
.,A9DC C0 BF    CPY #$BF        
.,A9DE D0 4C    BNE $AA2C       

                                *** assign to TI$
.,A9E0 20 A6 B6 JSR $B6A6       
.,A9E3 C9 06    CMP #$06        length 6
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

                                *** add next digit to float accum
.,AA1D B1 22    LDA ($22),Y     
.,AA1F 20 80 00 JSR $0080       
.,AA22 90 03    BCC $AA27       
.,AA24 4C 48 B2 JMP $B248       
.,AA27 E9 2F    SBC #$2F        
.,AA29 4C 7E BD JMP $BD7E       

                                *** assign to string variable
.,AA2C A0 02    LDY #$02        
.,AA2E B1 64    LDA ($64),Y     
.,AA30 C5 34    CMP $34         
.,AA32 90 17    BCC $AA4B       
.,AA34 D0 07    BNE $AA3D       
.,AA36 88       DEY             
.,AA37 B1 64    LDA ($64),Y     
.,AA39 C5 33    CMP $33         
.,AA3B 90 0E    BCC $AA4B       
.,AA3D A4 65    LDY $65         
.,AA3F C4 2E    CPY $2E         
.,AA41 90 08    BCC $AA4B       
.,AA43 D0 0D    BNE $AA52       
.,AA45 A5 64    LDA $64         
.,AA47 C5 2D    CMP $2D         
.,AA49 B0 07    BCS $AA52       
.,AA4B A5 64    LDA $64         
.,AA4D A4 65    LDY $65         
.,AA4F 4C 68 AA JMP $AA68       
.,AA52 A0 00    LDY #$00        
.,AA54 B1 64    LDA ($64),Y     
.,AA56 20 75 B4 JSR $B475       
.,AA59 A5 50    LDA $50         
.,AA5B A4 51    LDY $51         
.,AA5D 85 6F    STA $6F         
.,AA5F 84 70    STY $70         
.,AA61 20 7A B6 JSR $B67A       
.,AA64 A9 61    LDA #$61        low  0061
.,AA66 A0 00    LDY #$00        high 0061

                                *** move descriptor into variable
.,AA68 85 50    STA $50         
.,AA6A 84 51    STY $51         
.,AA6C 20 DB B6 JSR $B6DB       
.,AA6F A0 00    LDY #$00        
.,AA71 B1 50    LDA ($50),Y     
.,AA73 91 49    STA ($49),Y     
.,AA75 C8       INY             
.,AA76 B1 50    LDA ($50),Y     
.,AA78 91 49    STA ($49),Y     
.,AA7A C8       INY             
.,AA7B B1 50    LDA ($50),Y     
.,AA7D 91 49    STA ($49),Y     
.,AA7F 60       RTS             

                                *** PRINT# comand
.,AA80 20 86 AA JSR $AA86       
.,AA83 4C B5 AB JMP $ABB5       

                                *** CMD command
.,AA86 20 9E B7 JSR $B79E       
.,AA89 F0 05    BEQ $AA90       
.,AA8B A9 2C    LDA #$2C        comma
.,AA8D 20 FF AE JSR $AEFF       
.,AA90 08       PHP             
.,AA91 86 13    STX $13         
.,AA93 20 18 E1 JSR $E118       
.,AA96 28       PLP             
.,AA97 4C A0 AA JMP $AAA0       do PRINT
.,AA9A 20 21 AB JSR $AB21       
.,AA9D 20 79 00 JSR $0079       

                                *** PRINT command
.,AAA0 F0 35    BEQ $AAD7       
.,AAA2 F0 43    BEQ $AAE7       
.,AAA4 C9 A3    CMP #$A3        TAB( code
.,AAA6 F0 50    BEQ $AAF8       
.,AAA8 C9 A6    CMP #$A6        SPC( code
.,AAAA 18       CLC             
.,AAAB F0 4B    BEQ $AAF8       
.,AAAD C9 2C    CMP #$2C        comma
.,AAAF F0 37    BEQ $AAE8       
.,AAB1 C9 3B    CMP #$3B        semi-colon
.,AAB3 F0 5E    BEQ $AB13       
.,AAB5 20 9E AD JSR $AD9E       
.,AAB8 24 0D    BIT $0D         
.,AABA 30 DE    BMI $AA9A       
.,AABC 20 DD BD JSR $BDDD       
.,AABF 20 87 B4 JSR $B487       
.,AAC2 20 21 AB JSR $AB21       
.,AAC5 20 3B AB JSR $AB3B       
.,AAC8 D0 D3    BNE $AA9D       

                                *** end statement in buffer and screen
.,AACA A9 00    LDA #$00        
.,AACC 9D 00 02 STA $0200,X     
.,AACF A2 FF    LDX #$FF        
.,AAD1 A0 01    LDY #$01        
.,AAD3 A5 13    LDA $13         
.,AAD5 D0 10    BNE $AAE7       

                                *** end line on CMD output file
.,AAD7 A9 0D    LDA #$0D        
.,AAD9 20 47 AB JSR $AB47       
.,AADC 24 13    BIT $13         
.,AADE 10 05    BPL $AAE5       
.,AAE0 A9 0A    LDA #$0A        
.,AAE2 20 47 AB JSR $AB47       
.,AAE5 49 FF    EOR #$FF        
.,AAE7 60       RTS             

                                *** routine for printing TAB( and SPC(
.,AAE8 38       SEC             
.,AAE9 20 F0 FF JSR $FFF0       
.,AAEC 98       TYA             
.,AAED 38       SEC             
.,AAEE E9 0A    SBC #$0A        
.,AAF0 B0 FC    BCS $AAEE       
.,AAF2 49 FF    EOR #$FF        
.,AAF4 69 01    ADC #$01        
.,AAF6 D0 16    BNE $AB0E       
.,AAF8 08       PHP             
.,AAF9 38       SEC             
.,AAFA 20 F0 FF JSR $FFF0       
.,AAFD 84 09    STY $09         
.,AAFF 20 9B B7 JSR $B79B       
.,AB02 C9 29    CMP #$29        )
.,AB04 D0 59    BNE $AB5F       
.,AB06 28       PLP             
.,AB07 90 06    BCC $AB0F       
.,AB09 8A       TXA             
.,AB0A E5 09    SBC $09         
.,AB0C 90 05    BCC $AB13       
.,AB0E AA       TAX             
.,AB0F E8       INX             
.,AB10 CA       DEX             
.,AB11 D0 06    BNE $AB19       
.,AB13 20 73 00 JSR $0073       
.,AB16 4C A2 AA JMP $AAA2       
.,AB19 20 3B AB JSR $AB3B       
.,AB1C D0 F2    BNE $AB10       

                                *** print string form AY
.,AB1E 20 87 B4 JSR $B487       

                                *** print string from $22/$23
.,AB21 20 A6 B6 JSR $B6A6       
.,AB24 AA       TAX             
.,AB25 A0 00    LDY #$00        
.,AB27 E8       INX             
.,AB28 CA       DEX             
.,AB29 F0 BC    BEQ $AAE7       
.,AB2B B1 22    LDA ($22),Y     
.,AB2D 20 47 AB JSR $AB47       
.,AB30 C8       INY             
.,AB31 C9 0D    CMP #$0D        
.,AB33 D0 F3    BNE $AB28       
.,AB35 20 E5 AA JSR $AAE5       
.,AB38 4C 28 AB JMP $AB28       

                                *** print character on CMD output file
.,AB3B A5 13    LDA $13         
.,AB3D F0 03    BEQ $AB42       
.,AB3F A9 20    LDA #$20        space
.:AB41 2C       .BYTE $2C       
.,AB42 A9 1D    LDA #$1D        csr right
.:AB44 2C       .BYTE $2C       
.,AB45 A9 3F    LDA #$3F        question mark
.,AB47 20 0C E1 JSR $E10C       
.,AB4A 29 FF    AND #$FF        
.,AB4C 60       RTS             

                                *** read errors
.,AB4D A5 11    LDA $11         
.,AB4F F0 11    BEQ $AB62       
.,AB51 30 04    BMI $AB57       
.,AB53 A0 FF    LDY #$FF        
.,AB55 D0 04    BNE $AB5B       
.,AB57 A5 3F    LDA $3F         
.,AB59 A4 40    LDY $40         
.,AB5B 85 39    STA $39         
.,AB5D 84 3A    STY $3A         
.,AB5F 4C 08 AF JMP $AF08       
.,AB62 A5 13    LDA $13         
.,AB64 F0 05    BEQ $AB6B       
.,AB66 A2 18    LDX #$18        
.,AB68 4C 37 A4 JMP $A437       
.,AB6B A9 0C    LDA #$0C        low  AD0C
.,AB6D A0 AD    LDY #$AD        high AD0C
.,AB6F 20 1E AB JSR $AB1E       
.,AB72 A5 3D    LDA $3D         
.,AB74 A4 3E    LDY $3E         
.,AB76 85 7A    STA $7A         
.,AB78 84 7B    STY $7B         
.,AB7A 60       RTS             

                                *** GET command
.,AB7B 20 A6 B3 JSR $B3A6       
.,AB7E C9 23    CMP #$23        #
.,AB80 D0 10    BNE $AB92       
.,AB82 20 73 00 JSR $0073       
.,AB85 20 9E B7 JSR $B79E       
.,AB88 A9 2C    LDA #$2C        comma
.,AB8A 20 FF AE JSR $AEFF       
.,AB8D 86 13    STX $13         
.,AB8F 20 1E E1 JSR $E11E       
.,AB92 A2 01    LDX #$01        
.,AB94 A0 02    LDY #$02        
.,AB96 A9 00    LDA #$00        
.,AB98 8D 01 02 STA $0201       
.,AB9B A9 40    LDA #$40        GET code
.,AB9D 20 0F AC JSR $AC0F       
.,ABA0 A6 13    LDX $13         
.,ABA2 D0 13    BNE $ABB7       
.,ABA4 60       RTS             

                                *** INPUT# command
.,ABA5 20 9E B7 JSR $B79E       
.,ABA8 A9 2C    LDA #$2C        comma
.,ABAA 20 FF AE JSR $AEFF       
.,ABAD 86 13    STX $13         
.,ABAF 20 1E E1 JSR $E11E       
.,ABB2 20 CE AB JSR $ABCE       
.,ABB5 A5 13    LDA $13         
.,ABB7 20 CC FF JSR $FFCC       
.,ABBA A2 00    LDX #$00        
.,ABBC 86 13    STX $13         
.,ABBE 60       RTS             

                                *** INPUT command
.,ABBF C9 22    CMP #$22        quote mark
.,ABC1 D0 0B    BNE $ABCE       
.,ABC3 20 BD AE JSR $AEBD       
.,ABC6 A9 3B    LDA #$3B        semi-colon
.,ABC8 20 FF AE JSR $AEFF       
.,ABCB 20 21 AB JSR $AB21       
.,ABCE 20 A6 B3 JSR $B3A6       
.,ABD1 A9 2C    LDA #$2C        comma
.,ABD3 8D FF 01 STA $01FF       
.,ABD6 20 F9 AB JSR $ABF9       
.,ABD9 A5 13    LDA $13         
.,ABDB F0 0D    BEQ $ABEA       
.,ABDD 20 B7 FF JSR $FFB7       
.,ABE0 29 02    AND #$02        
.,ABE2 F0 06    BEQ $ABEA       
.,ABE4 20 B5 AB JSR $ABB5       
.,ABE7 4C F8 A8 JMP $A8F8       do DATA
.,ABEA AD 00 02 LDA $0200       
.,ABED D0 1E    BNE $AC0D       
.,ABEF A5 13    LDA $13         
.,ABF1 D0 E3    BNE $ABD6       
.,ABF3 20 06 A9 JSR $A906       
.,ABF6 4C FB A8 JMP $A8FB       

                                *** get line into input buffer
.,ABF9 A5 13    LDA $13         
.,ABFB D0 06    BNE $AC03       
.,ABFD 20 45 AB JSR $AB45       
.,AC00 20 3B AB JSR $AB3B       
.,AC03 4C 60 A5 JMP $A560       

                                *** READ command
.,AC06 A6 41    LDX $41         
.,AC08 A4 42    LDY $42         
.,AC0A A9 98    LDA #$98        READ code
.:AC0C 2C       .BYTE $2C       
.,AC0D A9 00    LDA #$00        
.,AC0F 85 11    STA $11         
.,AC11 86 43    STX $43         
.,AC13 84 44    STY $44         
.,AC15 20 8B B0 JSR $B08B       
.,AC18 85 49    STA $49         
.,AC1A 84 4A    STY $4A         
.,AC1C A5 7A    LDA $7A         
.,AC1E A4 7B    LDY $7B         
.,AC20 85 4B    STA $4B         
.,AC22 84 4C    STY $4C         
.,AC24 A6 43    LDX $43         
.,AC26 A4 44    LDY $44         
.,AC28 86 7A    STX $7A         
.,AC2A 84 7B    STY $7B         
.,AC2C 20 79 00 JSR $0079       
.,AC2F D0 20    BNE $AC51       
.,AC31 24 11    BIT $11         
.,AC33 50 0C    BVC $AC41       
.,AC35 20 24 E1 JSR $E124       
.,AC38 8D 00 02 STA $0200       
.,AC3B A2 FF    LDX #$FF        
.,AC3D A0 01    LDY #$01        
.,AC3F D0 0C    BNE $AC4D       
.,AC41 30 75    BMI $ACB8       
.,AC43 A5 13    LDA $13         
.,AC45 D0 03    BNE $AC4A       
.,AC47 20 45 AB JSR $AB45       
.,AC4A 20 F9 AB JSR $ABF9       
.,AC4D 86 7A    STX $7A         
.,AC4F 84 7B    STY $7B         
.,AC51 20 73 00 JSR $0073       
.,AC54 24 0D    BIT $0D         
.,AC56 10 31    BPL $AC89       
.,AC58 24 11    BIT $11         
.,AC5A 50 09    BVC $AC65       
.,AC5C E8       INX             
.,AC5D 86 7A    STX $7A         
.,AC5F A9 00    LDA #$00        
.,AC61 85 07    STA $07         
.,AC63 F0 0C    BEQ $AC71       
.,AC65 85 07    STA $07         
.,AC67 C9 22    CMP #$22        quote mark
.,AC69 F0 07    BEQ $AC72       
.,AC6B A9 3A    LDA #$3A        colon
.,AC6D 85 07    STA $07         
.,AC6F A9 2C    LDA #$2C        comma
.,AC71 18       CLC             
.,AC72 85 08    STA $08         
.,AC74 A5 7A    LDA $7A         
.,AC76 A4 7B    LDY $7B         
.,AC78 69 00    ADC #$00        
.,AC7A 90 01    BCC $AC7D       
.,AC7C C8       INY             
.,AC7D 20 8D B4 JSR $B48D       
.,AC80 20 E2 B7 JSR $B7E2       
.,AC83 20 DA A9 JSR $A9DA       
.,AC86 4C 91 AC JMP $AC91       
.,AC89 20 F3 BC JSR $BCF3       
.,AC8C A5 0E    LDA $0E         
.,AC8E 20 C2 A9 JSR $A9C2       
.,AC91 20 79 00 JSR $0079       
.,AC94 F0 07    BEQ $AC9D       
.,AC96 C9 2C    CMP #$2C        comma
.,AC98 F0 03    BEQ $AC9D       
.,AC9A 4C 4D AB JMP $AB4D       
.,AC9D A5 7A    LDA $7A         
.,AC9F A4 7B    LDY $7B         
.,ACA1 85 43    STA $43         
.,ACA3 84 44    STY $44         
.,ACA5 A5 4B    LDA $4B         
.,ACA7 A4 4C    LDY $4C         
.,ACA9 85 7A    STA $7A         
.,ACAB 84 7B    STY $7B         
.,ACAD 20 79 00 JSR $0079       
.,ACB0 F0 2D    BEQ $ACDF       
.,ACB2 20 FD AE JSR $AEFD       
.,ACB5 4C 15 AC JMP $AC15       
.,ACB8 20 06 A9 JSR $A906       
.,ACBB C8       INY             
.,ACBC AA       TAX             
.,ACBD D0 12    BNE $ACD1       
.,ACBF A2 0D    LDX #$0D        error number
.,ACC1 C8       INY             
.,ACC2 B1 7A    LDA ($7A),Y     
.,ACC4 F0 6C    BEQ $AD32       
.,ACC6 C8       INY             
.,ACC7 B1 7A    LDA ($7A),Y     
.,ACC9 85 3F    STA $3F         
.,ACCB C8       INY             
.,ACCC B1 7A    LDA ($7A),Y     
.,ACCE C8       INY             
.,ACCF 85 40    STA $40         
.,ACD1 20 FB A8 JSR $A8FB       
.,ACD4 20 79 00 JSR $0079       
.,ACD7 AA       TAX             
.,ACD8 E0 83    CPX #$83        DATA code
.,ACDA D0 DC    BNE $ACB8       
.,ACDC 4C 51 AC JMP $AC51       
.,ACDF A5 43    LDA $43         
.,ACE1 A4 44    LDY $44         
.,ACE3 A6 11    LDX $11         
.,ACE5 10 03    BPL $ACEA       
.,ACE7 4C 27 A8 JMP $A827       
.,ACEA A0 00    LDY #$00        
.,ACEC B1 43    LDA ($43),Y     
.,ACEE F0 0B    BEQ $ACFB       
.,ACF0 A5 13    LDA $13         
.,ACF2 D0 07    BNE $ACFB       
.,ACF4 A9 FC    LDA #$FC        low  ACFC
.,ACF6 A0 AC    LDY #$AC        high ACFC
.,ACF8 4C 1E AB JMP $AB1E       
.,ACFB 60       RTS             

                                *** messages used dring READ
.:ACFC 3F 45 58 54 52 41 20 49  ?EXTRA IGNORED
.:AD04 47 4E 4F 52 45 44 0D 00  
.:AD0C 3F 52 45 44 4F 20 46 52  ?REDO FROM START
.:AD14 4F 4D 20 53 54 41 52 54  
.:AD1C 0D 00                    

                                *** NEXT command
.,AD1E D0 04    BNE $AD24       
.,AD20 A0 00    LDY #$00        
.,AD22 F0 03    BEQ $AD27       
.,AD24 20 8B B0 JSR $B08B       
.,AD27 85 49    STA $49         
.,AD29 84 4A    STY $4A         
.,AD2B 20 8A A3 JSR $A38A       
.,AD2E F0 05    BEQ $AD35       
.,AD30 A2 0A    LDX #$0A        error number
.,AD32 4C 37 A4 JMP $A437       
.,AD35 9A       TXS             
.,AD36 8A       TXA             
.,AD37 18       CLC             
.,AD38 69 04    ADC #$04        
.,AD3A 48       PHA             
.,AD3B 69 06    ADC #$06        
.,AD3D 85 24    STA $24         
.,AD3F 68       PLA             
.,AD40 A0 01    LDY #$01        
.,AD42 20 A2 BB JSR $BBA2       
.,AD45 BA       TSX             
.,AD46 BD 09 01 LDA $0109,X     
.,AD49 85 66    STA $66         
.,AD4B A5 49    LDA $49         
.,AD4D A4 4A    LDY $4A         
.,AD4F 20 67 B8 JSR $B867       
.,AD52 20 D0 BB JSR $BBD0       
.,AD55 A0 01    LDY #$01        
.,AD57 20 5D BC JSR $BC5D       
.,AD5A BA       TSX             
.,AD5B 38       SEC             
.,AD5C FD 09 01 SBC $0109,X     
.,AD5F F0 17    BEQ $AD78       
.,AD61 BD 0F 01 LDA $010F,X     
.,AD64 85 39    STA $39         
.,AD66 BD 10 01 LDA $0110,X     
.,AD69 85 3A    STA $3A         
.,AD6B BD 12 01 LDA $0112,X     
.,AD6E 85 7A    STA $7A         
.,AD70 BD 11 01 LDA $0111,X     
.,AD73 85 7B    STA $7B         
.,AD75 4C AE A7 JMP $A7AE       
.,AD78 8A       TXA             
.,AD79 69 11    ADC #$11        
.,AD7B AA       TAX             
.,AD7C 9A       TXS             
.,AD7D 20 79 00 JSR $0079       
.,AD80 C9 2C    CMP #$2C        comma
.,AD82 D0 F1    BNE $AD75       
.,AD84 20 73 00 JSR $0073       
.,AD87 20 24 AD JSR $AD24       

                                *** get next non-string value
.,AD8A 20 9E AD JSR $AD9E       
.,AD8D 18       CLC             
.:AD8E 24       .BYTE $24       

                                *** check value to be string
.,AD8F 38       SEC             

                                *** check value according to C flag
.,AD90 24 0D    BIT $0D         
.,AD92 30 03    BMI $AD97       
.,AD94 B0 03    BCS $AD99       
.,AD96 60       RTS             
.,AD97 B0 FD    BCS $AD96       
.,AD99 A2 16    LDX #$16        
.,AD9B 4C 37 A4 JMP $A437       

                                *** evaluate expression
.,AD9E A6 7A    LDX $7A         
.,ADA0 D0 02    BNE $ADA4       
.,ADA2 C6 7B    DEC $7B         
.,ADA4 C6 7A    DEC $7A         
.,ADA6 A2 00    LDX #$00        
.:ADA8 24       .BYTE $24       
.,ADA9 48       PHA             
.,ADAA 8A       TXA             
.,ADAB 48       PHA             
.,ADAC A9 01    LDA #$01        
.,ADAE 20 FB A3 JSR $A3FB       
.,ADB1 20 83 AE JSR $AE83       
.,ADB4 A9 00    LDA #$00        
.,ADB6 85 4D    STA $4D         
.,ADB8 20 79 00 JSR $0079       
.,ADBB 38       SEC             
.,ADBC E9 B1    SBC #$B1        code for greater than
.,ADBE 90 17    BCC $ADD7       
.,ADC0 C9 03    CMP #$03        
.,ADC2 B0 13    BCS $ADD7       
.,ADC4 C9 01    CMP #$01        
.,ADC6 2A       ROL             
.,ADC7 49 01    EOR #$01        
.,ADC9 45 4D    EOR $4D         
.,ADCB C5 4D    CMP $4D         
.,ADCD 90 61    BCC $AE30       
.,ADCF 85 4D    STA $4D         
.,ADD1 20 73 00 JSR $0073       
.,ADD4 4C BB AD JMP $ADBB       
.,ADD7 A6 4D    LDX $4D         
.,ADD9 D0 2C    BNE $AE07       
.,ADDB B0 7B    BCS $AE58       
.,ADDD 69 07    ADC #$07        
.,ADDF 90 77    BCC $AE58       
.,ADE1 65 0D    ADC $0D         
.,ADE3 D0 03    BNE $ADE8       
.,ADE5 4C 3D B6 JMP $B63D       
.,ADE8 69 FF    ADC #$FF        
.,ADEA 85 22    STA $22         
.,ADEC 0A       ASL             
.,ADED 65 22    ADC $22         
.,ADEF A8       TAY             
.,ADF0 68       PLA             
.,ADF1 D9 80 A0 CMP $A080,Y     
.,ADF4 B0 67    BCS $AE5D       
.,ADF6 20 8D AD JSR $AD8D       
.,ADF9 48       PHA             
.,ADFA 20 20 AE JSR $AE20       
.,ADFD 68       PLA             
.,ADFE A4 4B    LDY $4B         
.,AE00 10 17    BPL $AE19       
.,AE02 AA       TAX             
.,AE03 F0 56    BEQ $AE5B       
.,AE05 D0 5F    BNE $AE66       
.,AE07 46 0D    LSR $0D         
.,AE09 8A       TXA             
.,AE0A 2A       ROL             
.,AE0B A6 7A    LDX $7A         
.,AE0D D0 02    BNE $AE11       
.,AE0F C6 7B    DEC $7B         
.,AE11 C6 7A    DEC $7A         
.,AE13 A0 1B    LDY #$1B        
.,AE15 85 4D    STA $4D         
.,AE17 D0 D7    BNE $ADF0       
.,AE19 D9 80 A0 CMP $A080,Y     
.,AE1C B0 48    BCS $AE66       
.,AE1E 90 D9    BCC $ADF9       

                                *** recursive entry for evaluation of expressions
.,AE20 B9 82 A0 LDA $A082,Y     
.,AE23 48       PHA             
.,AE24 B9 81 A0 LDA $A081,Y     
.,AE27 48       PHA             
.,AE28 20 33 AE JSR $AE33       
.,AE2B A5 4D    LDA $4D         
.,AE2D 4C A9 AD JMP $ADA9       
.,AE30 4C 08 AF JMP $AF08       

                                *** save rounded value of left operand
.,AE33 A5 66    LDA $66         
.,AE35 BE 80 A0 LDX $A080,Y     
.,AE38 A8       TAY             
.,AE39 68       PLA             pull return address
.,AE3A 85 22    STA $22         
.,AE3C E6 22    INC $22         
.,AE3E 68       PLA             and store in $22/$23
.,AE3F 85 23    STA $23         
.,AE41 98       TYA             
.,AE42 48       PHA             
.,AE43 20 1B BC JSR $BC1B       
.,AE46 A5 65    LDA $65         
.,AE48 48       PHA             
.,AE49 A5 64    LDA $64         
.,AE4B 48       PHA             
.,AE4C A5 63    LDA $63         
.,AE4E 48       PHA             
.,AE4F A5 62    LDA $62         
.,AE51 48       PHA             
.,AE52 A5 61    LDA $61         
.,AE54 48       PHA             
.,AE55 6C 22 00 JMP ($0022)     return to caller

                                *** apply operator
.,AE58 A0 FF    LDY #$FF        
.,AE5A 68       PLA             
.,AE5B F0 23    BEQ $AE80       
.,AE5D C9 64    CMP #$64        
.,AE5F F0 03    BEQ $AE64       
.,AE61 20 8D AD JSR $AD8D       
.,AE64 84 4B    STY $4B         
.,AE66 68       PLA             
.,AE67 4A       LSR             
.,AE68 85 12    STA $12         
.,AE6A 68       PLA             
.,AE6B 85 69    STA $69         
.,AE6D 68       PLA             
.,AE6E 85 6A    STA $6A         
.,AE70 68       PLA             
.,AE71 85 6B    STA $6B         
.,AE73 68       PLA             
.,AE74 85 6C    STA $6C         
.,AE76 68       PLA             
.,AE77 85 6D    STA $6D         
.,AE79 68       PLA             
.,AE7A 85 6E    STA $6E         
.,AE7C 45 66    EOR $66         
.,AE7E 85 6F    STA $6F         
.,AE80 A5 61    LDA $61         
.,AE82 60       RTS             

                                *** get arithmetic element routine
.,AE83 6C 0A 03 JMP ($030A)     normally AE86

                                *** standard arithmetic element
.,AE86 A9 00    LDA #$00        
.,AE88 85 0D    STA $0D         
.,AE8A 20 73 00 JSR $0073       
.,AE8D B0 03    BCS $AE92       
.,AE8F 4C F3 BC JMP $BCF3       
.,AE92 20 13 B1 JSR $B113       
.,AE95 90 03    BCC $AE9A       
.,AE97 4C 28 AF JMP $AF28       
.,AE9A C9 FF    CMP #$FF        PI
.,AE9C D0 0F    BNE $AEAD       
.,AE9E A9 A8    LDA #$A8        low  AEA8
.,AEA0 A0 AE    LDY #$AE        high AEA8
.,AEA2 20 A2 BB JSR $BBA2       
.,AEA5 4C 73 00 JMP $0073       

                                *** float value of PI
.:AEA8 82 49 0F DA A1           
.,AEAD C9 2E    CMP #$2E        decimal point
.,AEAF F0 DE    BEQ $AE8F       
.,AEB1 C9 AB    CMP #$AB        plus code
.,AEB3 F0 58    BEQ $AF0D       
.,AEB5 C9 AA    CMP #$AA        times code
.,AEB7 F0 D1    BEQ $AE8A       
.,AEB9 C9 22    CMP #$22        quote mark
.,AEBB D0 0F    BNE $AECC       
.,AEBD A5 7A    LDA $7A         
.,AEBF A4 7B    LDY $7B         
.,AEC1 69 00    ADC #$00        
.,AEC3 90 01    BCC $AEC6       
.,AEC5 C8       INY             
.,AEC6 20 87 B4 JSR $B487       
.,AEC9 4C E2 B7 JMP $B7E2       
.,AECC C9 A8    CMP #$A8        NOT code
.,AECE D0 13    BNE $AEE3       
.,AED0 A0 18    LDY #$18        
.,AED2 D0 3B    BNE $AF0F       

                                *** NOT operator
.,AED4 20 BF B1 JSR $B1BF       
.,AED7 A5 65    LDA $65         
.,AED9 49 FF    EOR #$FF        
.,AEDB A8       TAY             
.,AEDC A5 64    LDA $64         
.,AEDE 49 FF    EOR #$FF        
.,AEE0 4C 91 B3 JMP $B391       

                                *** GET operand
.,AEE3 C9 A5    CMP #$A5        
.,AEE5 D0 03    BNE $AEEA       
.,AEE7 4C F4 B3 JMP $B3F4       
.,AEEA C9 B4    CMP #$B4        SGN code or higher
.,AEEC 90 03    BCC $AEF1       
.,AEEE 4C A7 AF JMP $AFA7       
.,AEF1 20 FA AE JSR $AEFA       
.,AEF4 20 9E AD JSR $AD9E       

                                *** check and skip characters
.,AEF7 A9 29    LDA #$29        )
.:AEF9 2C       .BYTE $2C       
.,AEFA A9 28    LDA #$28        (
.:AEFC 2C       .BYTE $2C       
.,AEFD A9 2C    LDA #$2C        comma
.,AEFF A0 00    LDY #$00        
.,AF01 D1 7A    CMP ($7A),Y     
.,AF03 D0 03    BNE $AF08       
.,AF05 4C 73 00 JMP $0073       
.,AF08 A2 0B    LDX #$0B        error number
.,AF0A 4C 37 A4 JMP $A437       

                                *** recursive geet value
.,AF0D A0 15    LDY #$15        
.,AF0F 68       PLA             
.,AF10 68       PLA             
.,AF11 4C FA AD JMP $ADFA       

                                *** check variable pointer range
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

                                *** get value of variable
.,AF28 20 8B B0 JSR $B08B       
.,AF2B 85 64    STA $64         
.,AF2D 84 65    STY $65         
.,AF2F A6 45    LDX $45         
.,AF31 A4 46    LDY $46         
.,AF33 A5 0D    LDA $0D         
.,AF35 F0 26    BEQ $AF5D       
.,AF37 A9 00    LDA #$00        
.,AF39 85 70    STA $70         
.,AF3B 20 14 AF JSR $AF14       
.,AF3E 90 1C    BCC $AF5C       
.,AF40 E0 54    CPX #$54        T
.,AF42 D0 18    BNE $AF5C       
.,AF44 C0 C9    CPY #$C9        I$
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
.,AF5F 10 0D    BPL $AF6E       
.,AF61 A0 00    LDY #$00        
.,AF63 B1 64    LDA ($64),Y     
.,AF65 AA       TAX             
.,AF66 C8       INY             
.,AF67 B1 64    LDA ($64),Y     
.,AF69 A8       TAY             
.,AF6A 8A       TXA             
.,AF6B 4C 91 B3 JMP $B391       
.,AF6E 20 14 AF JSR $AF14       
.,AF71 90 2D    BCC $AFA0       
.,AF73 E0 54    CPX #$54        T
.,AF75 D0 1B    BNE $AF92       
.,AF77 C0 49    CPY #$49        I
.,AF79 D0 25    BNE $AFA0       
.,AF7B 20 84 AF JSR $AF84       
.,AF7E 98       TYA             
.,AF7F A2 A0    LDX #$A0        
.,AF81 4C 4F BC JMP $BC4F       

                                *** get time in float accu
.,AF84 20 DE FF JSR $FFDE       
.,AF87 86 64    STX $64         
.,AF89 84 63    STY $63         
.,AF8B 85 65    STA $65         
.,AF8D A0 00    LDY #$00        
.,AF8F 84 62    STY $62         
.,AF91 60       RTS             

                                *** continue of get value of variable
.,AF92 E0 53    CPX #$53        S
.,AF94 D0 0A    BNE $AFA0       
.,AF96 C0 54    CPY #$54        T
.,AF98 D0 06    BNE $AFA0       
.,AF9A 20 B7 FF JSR $FFB7       
.,AF9D 4C 3C BC JMP $BC3C       
.,AFA0 A5 64    LDA $64         
.,AFA2 A4 65    LDY $65         
.,AFA4 4C A2 BB JMP $BBA2       

                                *** apply function
.,AFA7 0A       ASL             
.,AFA8 48       PHA             
.,AFA9 AA       TAX             
.,AFAA 20 73 00 JSR $0073       
.,AFAD E0 8F    CPX #$8F        
.,AFAF 90 20    BCC $AFD1       
.,AFB1 20 FA AE JSR $AEFA       
.,AFB4 20 9E AD JSR $AD9E       
.,AFB7 20 FD AE JSR $AEFD       
.,AFBA 20 8F AD JSR $AD8F       
.,AFBD 68       PLA             
.,AFBE AA       TAX             
.,AFBF A5 65    LDA $65         
.,AFC1 48       PHA             
.,AFC2 A5 64    LDA $64         
.,AFC4 48       PHA             
.,AFC5 8A       TXA             
.,AFC6 48       PHA             
.,AFC7 20 9E B7 JSR $B79E       
.,AFCA 68       PLA             
.,AFCB A8       TAY             
.,AFCC 8A       TXA             
.,AFCD 48       PHA             
.,AFCE 4C D6 AF JMP $AFD6       
.,AFD1 20 F1 AE JSR $AEF1       
.,AFD4 68       PLA             
.,AFD5 A8       TAY             
.,AFD6 B9 EA 9F LDA $9FEA,Y     
.,AFD9 85 55    STA $55         
.,AFDB B9 EB 9F LDA $9FEB,Y     
.,AFDE 85 56    STA $56         
.,AFE0 20 54 00 JSR $0054       
.,AFE3 4C 8D AD JMP $AD8D       

                                *** OR operator
.,AFE6 A0 FF    LDY #$FF        
.:AFE8 2C       .BYTE $2C       

                                *** AND operator
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

                                *** greater/equal/less operator
.,B016 20 90 AD JSR $AD90       
.,B019 B0 13    BCS $B02E       
.,B01B A5 6E    LDA $6E         
.,B01D 09 7F    ORA #$7F        
.,B01F 25 6A    AND $6A         
.,B021 85 6A    STA $6A         
.,B023 A9 69    LDA #$69        
.,B025 A0 00    LDY #$00        
.,B027 20 5B BC JSR $BC5B       
.,B02A AA       TAX             
.,B02B 4C 61 B0 JMP $B061       
.,B02E A9 00    LDA #$00        
.,B030 85 0D    STA $0D         
.,B032 C6 4D    DEC $4D         
.,B034 20 A6 B6 JSR $B6A6       
.,B037 85 61    STA $61         
.,B039 86 62    STX $62         
.,B03B 84 63    STY $63         
.,B03D A5 6C    LDA $6C         
.,B03F A4 6D    LDY $6D         
.,B041 20 AA B6 JSR $B6AA       
.,B044 86 6C    STX $6C         
.,B046 84 6D    STY $6D         
.,B048 AA       TAX             
.,B049 38       SEC             
.,B04A E5 61    SBC $61         
.,B04C F0 08    BEQ $B056       
.,B04E A9 01    LDA #$01        
.,B050 90 04    BCC $B056       
.,B052 A6 61    LDX $61         
.,B054 A9 FF    LDA #$FF        
.,B056 85 66    STA $66         
.,B058 A0 FF    LDY #$FF        
.,B05A E8       INX             
.,B05B C8       INY             
.,B05C CA       DEX             
.,B05D D0 07    BNE $B066       
.,B05F A6 66    LDX $66         
.,B061 30 0F    BMI $B072       
.,B063 18       CLC             
.,B064 90 0C    BCC $B072       
.,B066 B1 6C    LDA ($6C),Y     
.,B068 D1 62    CMP ($62),Y     
.,B06A F0 EF    BEQ $B05B       
.,B06C A2 FF    LDX #$FF        
.,B06E B0 02    BCS $B072       
.,B070 A2 01    LDX #$01        
.,B072 E8       INX             
.,B073 8A       TXA             
.,B074 2A       ROL             
.,B075 25 12    AND $12         
.,B077 F0 02    BEQ $B07B       
.,B079 A9 FF    LDA #$FF        
.,B07B 4C 3C BC JMP $BC3C       

                                *** DIM command
.,B07E 20 FD AE JSR $AEFD       
.,B081 AA       TAX             
.,B082 20 90 B0 JSR $B090       
.,B085 20 79 00 JSR $0079       
.,B088 D0 F4    BNE $B07E       
.,B08A 60       RTS             

                                *** get name and pointer to a variable
.,B08B A2 00    LDX #$00        
.,B08D 20 79 00 JSR $0079       
.,B090 86 0C    STX $0C         
.,B092 85 45    STA $45         
.,B094 20 79 00 JSR $0079       
.,B097 20 13 B1 JSR $B113       
.,B09A B0 03    BCS $B09F       
.,B09C 4C 08 AF JMP $AF08       
.,B09F A2 00    LDX #$00        
.,B0A1 86 0D    STX $0D         
.,B0A3 86 0E    STX $0E         
.,B0A5 20 73 00 JSR $0073       
.,B0A8 90 05    BCC $B0AF       
.,B0AA 20 13 B1 JSR $B113       
.,B0AD 90 0B    BCC $B0BA       
.,B0AF AA       TAX             
.,B0B0 20 73 00 JSR $0073       
.,B0B3 90 FB    BCC $B0B0       
.,B0B5 20 13 B1 JSR $B113       
.,B0B8 B0 F6    BCS $B0B0       
.,B0BA C9 24    CMP #$24        $
.,B0BC D0 06    BNE $B0C4       
.,B0BE A9 FF    LDA #$FF        
.,B0C0 85 0D    STA $0D         
.,B0C2 D0 10    BNE $B0D4       
.,B0C4 C9 25    CMP #$25        %
.,B0C6 D0 13    BNE $B0DB       
.,B0C8 A5 10    LDA $10         
.,B0CA D0 D0    BNE $B09C       
.,B0CC A9 80    LDA #$80        
.,B0CE 85 0E    STA $0E         
.,B0D0 05 45    ORA $45         
.,B0D2 85 45    STA $45         
.,B0D4 8A       TXA             
.,B0D5 09 80    ORA #$80        
.,B0D7 AA       TAX             
.,B0D8 20 73 00 JSR $0073       
.,B0DB 86 46    STX $46         
.,B0DD 38       SEC             
.,B0DE 05 10    ORA $10         
.,B0E0 E9 28    SBC #$28        (
.,B0E2 D0 03    BNE $B0E7       
.,B0E4 4C D1 B1 JMP $B1D1       
.,B0E7 A0 00    LDY #$00        
.,B0E9 84 10    STY $10         
.,B0EB A5 2D    LDA $2D         
.,B0ED A6 2E    LDX $2E         
.,B0EF 86 60    STX $60         
.,B0F1 85 5F    STA $5F         
.,B0F3 E4 30    CPX $30         
.,B0F5 D0 04    BNE $B0FB       
.,B0F7 C5 2F    CMP $2F         
.,B0F9 F0 22    BEQ $B11D       
.,B0FB A5 45    LDA $45         
.,B0FD D1 5F    CMP ($5F),Y     
.,B0FF D0 08    BNE $B109       
.,B101 A5 46    LDA $46         
.,B103 C8       INY             
.,B104 D1 5F    CMP ($5F),Y     
.,B106 F0 7D    BEQ $B185       
.,B108 88       DEY             
.,B109 18       CLC             
.,B10A A5 5F    LDA $5F         
.,B10C 69 07    ADC #$07        
.,B10E 90 E1    BCC $B0F1       
.,B110 E8       INX             
.,B111 D0 DC    BNE $B0EF       

                                *** check character in A
                                C=1 if alphabetic, C=0 if not
.,B113 C9 41    CMP #$41        A
.,B115 90 05    BCC $B11C       
.,B117 E9 5B    SBC #$5B        Z
.,B119 38       SEC             
.,B11A E9 A5    SBC #$A5        
.,B11C 60       RTS             

                                *** variable not found
.,B11D 68       PLA             
.,B11E 48       PHA             
.,B11F C9 2A    CMP #$2A        
.,B121 D0 05    BNE $B128       
.,B123 A9 13    LDA #$13        
.,B125 A0 BF    LDY #$BF        
.,B127 60       RTS             
.,B128 A5 45    LDA $45         
.,B12A A4 46    LDY $46         
.,B12C C9 54    CMP #$54        T
.,B12E D0 0B    BNE $B13B       
.,B130 C0 C9    CPY #$C9        I$
.,B132 F0 EF    BEQ $B123       
.,B134 C0 49    CPY #$49        I
.,B136 D0 03    BNE $B13B       
.,B138 4C 08 AF JMP $AF08       
.,B13B C9 53    CMP #$53        S
.,B13D D0 04    BNE $B143       
.,B13F C0 54    CPY #$54        T
.,B141 F0 F5    BEQ $B138       
.,B143 A5 2F    LDA $2F         
.,B145 A4 30    LDY $30         
.,B147 85 5F    STA $5F         
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
.,B15D 20 B8 A3 JSR $A3B8       
.,B160 A5 58    LDA $58         
.,B162 A4 59    LDY $59         
.,B164 C8       INY             
.,B165 85 2F    STA $2F         
.,B167 84 30    STY $30         
.,B169 A0 00    LDY #$00        
.,B16B A5 45    LDA $45         
.,B16D 91 5F    STA ($5F),Y     
.,B16F C8       INY             
.,B170 A5 46    LDA $46         
.,B172 91 5F    STA ($5F),Y     
.,B174 A9 00    LDA #$00        
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

                                *** variable found
.,B185 A5 5F    LDA $5F         
.,B187 18       CLC             
.,B188 69 02    ADC #$02        
.,B18A A4 60    LDY $60         
.,B18C 90 01    BCC $B18F       
.,B18E C8       INY             
.,B18F 85 47    STA $47         
.,B191 84 48    STY $48         
.,B193 60       RTS             

                                *** compute pointer to array body
.,B194 A5 0B    LDA $0B         
.,B196 0A       ASL             
.,B197 69 05    ADC #$05        
.,B199 65 5F    ADC $5F         
.,B19B A4 60    LDY $60         
.,B19D 90 01    BCC $B1A0       
.,B19F C8       INY             
.,B1A0 85 58    STA $58         
.,B1A2 84 59    STY $59         
.,B1A4 60       RTS             

                                *** float number for conversion to integer
.:B1A5 90 80 00 00 00           

                                *** routine to convert float to fixed point
.,B1AA 20 BF B1 JSR $B1BF       
.,B1AD A5 64    LDA $64         
.,B1AF A4 65    LDY $65         
.,B1B1 60       RTS             

                                *** convert value from statement to integer
.,B1B2 20 73 00 JSR $0073       
.,B1B5 20 9E AD JSR $AD9E       
.,B1B8 20 8D AD JSR $AD8D       
.,B1BB A5 66    LDA $66         
.,B1BD 30 0D    BMI $B1CC       

                                *** convert float number to integer
.,B1BF A5 61    LDA $61         
.,B1C1 C9 90    CMP #$90        
.,B1C3 90 09    BCC $B1CE       
.,B1C5 A9 A5    LDA #$A5        low  B1A5
.,B1C7 A0 B1    LDY #$B1        high B1A5
.,B1C9 20 5B BC JSR $BC5B       
.,B1CC D0 7A    BNE $B248       
.,B1CE 4C 9B BC JMP $BC9B       

                                *** get pointer to dimensioned variable
.,B1D1 A5 0C    LDA $0C         
.,B1D3 05 0E    ORA $0E         
.,B1D5 48       PHA             
.,B1D6 A5 0D    LDA $0D         
.,B1D8 48       PHA             
.,B1D9 A0 00    LDY #$00        
.,B1DB 98       TYA             
.,B1DC 48       PHA             
.,B1DD A5 46    LDA $46         
.,B1DF 48       PHA             
.,B1E0 A5 45    LDA $45         
.,B1E2 48       PHA             
.,B1E3 20 B2 B1 JSR $B1B2       
.,B1E6 68       PLA             
.,B1E7 85 45    STA $45         
.,B1E9 68       PLA             
.,B1EA 85 46    STA $46         
.,B1EC 68       PLA             
.,B1ED A8       TAY             
.,B1EE BA       TSX             
.,B1EF BD 02 01 LDA $0102,X     
.,B1F2 48       PHA             
.,B1F3 BD 01 01 LDA $0101,X     
.,B1F6 48       PHA             
.,B1F7 A5 64    LDA $64         
.,B1F9 9D 02 01 STA $0102,X     
.,B1FC A5 65    LDA $65         
.,B1FE 9D 01 01 STA $0101,X     
.,B201 C8       INY             
.,B202 20 79 00 JSR $0079       
.,B205 C9 2C    CMP #$2C        comma
.,B207 F0 D2    BEQ $B1DB       
.,B209 84 0B    STY $0B         
.,B20B 20 F7 AE JSR $AEF7       
.,B20E 68       PLA             
.,B20F 85 0D    STA $0D         
.,B211 68       PLA             
.,B212 85 0E    STA $0E         
.,B214 29 7F    AND #$7F        
.,B216 85 0C    STA $0C         
.,B218 A6 2F    LDX $2F         
.,B21A A5 30    LDA $30         
.,B21C 86 5F    STX $5F         
.,B21E 85 60    STA $60         
.,B220 C5 32    CMP $32         
.,B222 D0 04    BNE $B228       
.,B224 E4 31    CPX $31         
.,B226 F0 39    BEQ $B261       
.,B228 A0 00    LDY #$00        
.,B22A B1 5F    LDA ($5F),Y     
.,B22C C8       INY             
.,B22D C5 45    CMP $45         
.,B22F D0 06    BNE $B237       
.,B231 A5 46    LDA $46         
.,B233 D1 5F    CMP ($5F),Y     
.,B235 F0 16    BEQ $B24D       
.,B237 C8       INY             
.,B238 B1 5F    LDA ($5F),Y     
.,B23A 18       CLC             
.,B23B 65 5F    ADC $5F         
.,B23D AA       TAX             
.,B23E C8       INY             
.,B23F B1 5F    LDA ($5F),Y     
.,B241 65 60    ADC $60         
.,B243 90 D7    BCC $B21C       
.,B245 A2 12    LDX #$12        error number
.:B247 2C       .BYTE $2C       
.,B248 A2 0E    LDX #$0E        error number
.,B24A 4C 37 A4 JMP $A437       
.,B24D A2 13    LDX #$13        error number
.,B24F A5 0C    LDA $0C         
.,B251 D0 F7    BNE $B24A       
.,B253 20 94 B1 JSR $B194       
.,B256 A5 0B    LDA $0B         
.,B258 A0 04    LDY #$04        
.,B25A D1 5F    CMP ($5F),Y     
.,B25C D0 E7    BNE $B245       
.,B25E 4C EA B2 JMP $B2EA       

                                *** allocate array
.,B261 20 94 B1 JSR $B194       
.,B264 20 08 A4 JSR $A408       
.,B267 A0 00    LDY #$00        
.,B269 84 72    STY $72         
.,B26B A2 05    LDX #$05        
.,B26D A5 45    LDA $45         
.,B26F 91 5F    STA ($5F),Y     
.,B271 10 01    BPL $B274       
.,B273 CA       DEX             
.,B274 C8       INY             
.,B275 A5 46    LDA $46         
.,B277 91 5F    STA ($5F),Y     
.,B279 10 02    BPL $B27D       
.,B27B CA       DEX             
.,B27C CA       DEX             
.,B27D 86 71    STX $71         
.,B27F A5 0B    LDA $0B         
.,B281 C8       INY             
.,B282 C8       INY             
.,B283 C8       INY             
.,B284 91 5F    STA ($5F),Y     
.,B286 A2 0B    LDX #$0B        
.,B288 A9 00    LDA #$00        
.,B28A 24 0C    BIT $0C         
.,B28C 50 08    BVC $B296       
.,B28E 68       PLA             
.,B28F 18       CLC             
.,B290 69 01    ADC #$01        
.,B292 AA       TAX             
.,B293 68       PLA             
.,B294 69 00    ADC #$00        
.,B296 C8       INY             
.,B297 91 5F    STA ($5F),Y     
.,B299 C8       INY             
.,B29A 8A       TXA             
.,B29B 91 5F    STA ($5F),Y     
.,B29D 20 4C B3 JSR $B34C       
.,B2A0 86 71    STX $71         
.,B2A2 85 72    STA $72         
.,B2A4 A4 22    LDY $22         
.,B2A6 C6 0B    DEC $0B         
.,B2A8 D0 DC    BNE $B286       
.,B2AA 65 59    ADC $59         
.,B2AC B0 5D    BCS $B30B       
.,B2AE 85 59    STA $59         
.,B2B0 A8       TAY             
.,B2B1 8A       TXA             
.,B2B2 65 58    ADC $58         
.,B2B4 90 03    BCC $B2B9       
.,B2B6 C8       INY             
.,B2B7 F0 52    BEQ $B30B       
.,B2B9 20 08 A4 JSR $A408       
.,B2BC 85 31    STA $31         
.,B2BE 84 32    STY $32         
.,B2C0 A9 00    LDA #$00        
.,B2C2 E6 72    INC $72         
.,B2C4 A4 71    LDY $71         
.,B2C6 F0 05    BEQ $B2CD       
.,B2C8 88       DEY             
.,B2C9 91 58    STA ($58),Y     
.,B2CB D0 FB    BNE $B2C8       
.,B2CD C6 59    DEC $59         
.,B2CF C6 72    DEC $72         
.,B2D1 D0 F5    BNE $B2C8       
.,B2D3 E6 59    INC $59         
.,B2D5 38       SEC             
.,B2D6 A5 31    LDA $31         
.,B2D8 E5 5F    SBC $5F         
.,B2DA A0 02    LDY #$02        
.,B2DC 91 5F    STA ($5F),Y     
.,B2DE A5 32    LDA $32         
.,B2E0 C8       INY             
.,B2E1 E5 60    SBC $60         
.,B2E3 91 5F    STA ($5F),Y     
.,B2E5 A5 0C    LDA $0C         
.,B2E7 D0 62    BNE $B34B       
.,B2E9 C8       INY             

                                *** compute reference to array element
.,B2EA B1 5F    LDA ($5F),Y     
.,B2EC 85 0B    STA $0B         
.,B2EE A9 00    LDA #$00        
.,B2F0 85 71    STA $71         
.,B2F2 85 72    STA $72         
.,B2F4 C8       INY             
.,B2F5 68       PLA             
.,B2F6 AA       TAX             
.,B2F7 85 64    STA $64         
.,B2F9 68       PLA             
.,B2FA 85 65    STA $65         
.,B2FC D1 5F    CMP ($5F),Y     
.,B2FE 90 0E    BCC $B30E       
.,B300 D0 06    BNE $B308       
.,B302 C8       INY             
.,B303 8A       TXA             
.,B304 D1 5F    CMP ($5F),Y     
.,B306 90 07    BCC $B30F       
.,B308 4C 45 B2 JMP $B245       
.,B30B 4C 35 A4 JMP $A435       
.,B30E C8       INY             
.,B30F A5 72    LDA $72         
.,B311 05 71    ORA $71         
.,B313 18       CLC             
.,B314 F0 0A    BEQ $B320       
.,B316 20 4C B3 JSR $B34C       
.,B319 8A       TXA             
.,B31A 65 64    ADC $64         
.,B31C AA       TAX             
.,B31D 98       TYA             
.,B31E A4 22    LDY $22         
.,B320 65 65    ADC $65         
.,B322 86 71    STX $71         
.,B324 C6 0B    DEC $0B         
.,B326 D0 CA    BNE $B2F2       
.,B328 85 72    STA $72         
.,B32A A2 05    LDX #$05        
.,B32C A5 45    LDA $45         
.,B32E 10 01    BPL $B331       
.,B330 CA       DEX             
.,B331 A5 46    LDA $46         
.,B333 10 02    BPL $B337       
.,B335 CA       DEX             
.,B336 CA       DEX             
.,B337 86 28    STX $28         
.,B339 A9 00    LDA #$00        
.,B33B 20 55 B3 JSR $B355       
.,B33E 8A       TXA             
.,B33F 65 58    ADC $58         
.,B341 85 47    STA $47         
.,B343 98       TYA             
.,B344 65 59    ADC $59         
.,B346 85 48    STA $48         
.,B348 A8       TAY             
.,B349 A5 47    LDA $47         
.,B34B 60       RTS             

                                *** XY = XA = length * limit from array data
.,B34C 84 22    STY $22         
.,B34E B1 5F    LDA ($5F),Y     
.,B350 85 28    STA $28         
.,B352 88       DEY             
.,B353 B1 5F    LDA ($5F),Y     
.,B355 85 29    STA $29         
.,B357 A9 10    LDA #$10        
.,B359 85 5D    STA $5D         
.,B35B A2 00    LDX #$00        
.,B35D A0 00    LDY #$00        
.,B35F 8A       TXA             
.,B360 0A       ASL             
.,B361 AA       TAX             
.,B362 98       TYA             
.,B363 2A       ROL             
.,B364 A8       TAY             
.,B365 B0 A4    BCS $B30B       
.,B367 06 71    ASL $71         
.,B369 26 72    ROL $72         
.,B36B 90 0B    BCC $B378       
.,B36D 18       CLC             
.,B36E 8A       TXA             
.,B36F 65 28    ADC $28         
.,B371 AA       TAX             
.,B372 98       TYA             
.,B373 65 29    ADC $29         
.,B375 A8       TAY             
.,B376 B0 93    BCS $B30B       
.,B378 C6 5D    DEC $5D         
.,B37A D0 E3    BNE $B35F       
.,B37C 60       RTS             

                                *** FRE function
.,B37D A5 0D    LDA $0D         
.,B37F F0 03    BEQ $B384       
.,B381 20 A6 B6 JSR $B6A6       
.,B384 20 26 B5 JSR $B526       
.,B387 38       SEC             
.,B388 A5 33    LDA $33         
.,B38A E5 31    SBC $31         
.,B38C A8       TAY             
.,B38D A5 34    LDA $34         
.,B38F E5 32    SBC $32         

                                *** routine to convert integer to float
.,B391 A2 00    LDX #$00        
.,B393 86 0D    STX $0D         
.,B395 85 62    STA $62         
.,B397 84 63    STY $63         
.,B399 A2 90    LDX #$90        
.,B39B 4C 44 BC JMP $BC44       

                                *** POS function
.,B39E 38       SEC             
.,B39F 20 F0 FF JSR $FFF0       
.,B3A2 A9 00    LDA #$00        
.,B3A4 F0 EB    BEQ $B391       

                                *** check for non-direct mode
.,B3A6 A6 3A    LDX $3A         
.,B3A8 E8       INX             
.,B3A9 D0 A0    BNE $B34B       
.,B3AB A2 15    LDX #$15        error number
.:B3AD 2C       .BYTE $2C       
.,B3AE A2 1B    LDX #$1B        error number
.,B3B0 4C 37 A4 JMP $A437       

                                *** DEF command
.,B3B3 20 E1 B3 JSR $B3E1       
.,B3B6 20 A6 B3 JSR $B3A6       
.,B3B9 20 FA AE JSR $AEFA       
.,B3BC A9 80    LDA #$80        
.,B3BE 85 10    STA $10         
.,B3C0 20 8B B0 JSR $B08B       
.,B3C3 20 8D AD JSR $AD8D       
.,B3C6 20 F7 AE JSR $AEF7       
.,B3C9 A9 B2    LDA #$B2        
.,B3CB 20 FF AE JSR $AEFF       
.,B3CE 48       PHA             
.,B3CF A5 48    LDA $48         
.,B3D1 48       PHA             
.,B3D2 A5 47    LDA $47         
.,B3D4 48       PHA             
.,B3D5 A5 7B    LDA $7B         
.,B3D7 48       PHA             
.,B3D8 A5 7A    LDA $7A         
.,B3DA 48       PHA             
.,B3DB 20 F8 A8 JSR $A8F8       
.,B3DE 4C 4F B4 JMP $B44F       

                                *** get function name
.,B3E1 A9 A5    LDA #$A5        
.,B3E3 20 FF AE JSR $AEFF       
.,B3E6 09 80    ORA #$80        
.,B3E8 85 10    STA $10         
.,B3EA 20 92 B0 JSR $B092       
.,B3ED 85 4E    STA $4E         
.,B3EF 84 4F    STY $4F         
.,B3F1 4C 8D AD JMP $AD8D       

                                *** expand FN call
.,B3F4 20 E1 B3 JSR $B3E1       
.,B3F7 A5 4F    LDA $4F         
.,B3F9 48       PHA             
.,B3FA A5 4E    LDA $4E         
.,B3FC 48       PHA             
.,B3FD 20 F1 AE JSR $AEF1       
.,B400 20 8D AD JSR $AD8D       
.,B403 68       PLA             
.,B404 85 4E    STA $4E         
.,B406 68       PLA             
.,B407 85 4F    STA $4F         
.,B409 A0 02    LDY #$02        
.,B40B B1 4E    LDA ($4E),Y     
.,B40D 85 47    STA $47         
.,B40F AA       TAX             
.,B410 C8       INY             
.,B411 B1 4E    LDA ($4E),Y     
.,B413 F0 99    BEQ $B3AE       
.,B415 85 48    STA $48         
.,B417 C8       INY             
.,B418 B1 47    LDA ($47),Y     
.,B41A 48       PHA             
.,B41B 88       DEY             
.,B41C 10 FA    BPL $B418       
.,B41E A4 48    LDY $48         
.,B420 20 D4 BB JSR $BBD4       
.,B423 A5 7B    LDA $7B         
.,B425 48       PHA             
.,B426 A5 7A    LDA $7A         
.,B428 48       PHA             
.,B429 B1 4E    LDA ($4E),Y     
.,B42B 85 7A    STA $7A         
.,B42D C8       INY             
.,B42E B1 4E    LDA ($4E),Y     
.,B430 85 7B    STA $7B         
.,B432 A5 48    LDA $48         
.,B434 48       PHA             
.,B435 A5 47    LDA $47         
.,B437 48       PHA             
.,B438 20 8A AD JSR $AD8A       
.,B43B 68       PLA             
.,B43C 85 4E    STA $4E         
.,B43E 68       PLA             
.,B43F 85 4F    STA $4F         
.,B441 20 79 00 JSR $0079       
.,B444 F0 03    BEQ $B449       
.,B446 4C 08 AF JMP $AF08       
.,B449 68       PLA             
.,B44A 85 7A    STA $7A         
.,B44C 68       PLA             
.,B44D 85 7B    STA $7B         
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

                                *** STR$ function
.,B465 20 8D AD JSR $AD8D       
.,B468 A0 00    LDY #$00        
.,B46A 20 DF BD JSR $BDDF       
.,B46D 68       PLA             
.,B46E 68       PLA             
.,B46F A9 FF    LDA #$FF        
.,B471 A0 00    LDY #$00        
.,B473 F0 12    BEQ $B487       
.,B475 A6 64    LDX $64         
.,B477 A4 65    LDY $65         
.,B479 86 50    STX $50         
.,B47B 84 51    STY $51         

                                *** allocate area according to A
.,B47D 20 F4 B4 JSR $B4F4       
.,B480 86 62    STX $62         
.,B482 84 63    STY $63         
.,B484 85 61    STA $61         
.,B486 60       RTS             

                                *** get description of string into float accu
.,B487 A2 22    LDX #$22        quote mark
.,B489 86 07    STX $07         
.,B48B 86 08    STX $08         
.,B48D 85 6F    STA $6F         
.,B48F 84 70    STY $70         
.,B491 85 62    STA $62         
.,B493 84 63    STY $63         
.,B495 A0 FF    LDY #$FF        
.,B497 C8       INY             
.,B498 B1 6F    LDA ($6F),Y     
.,B49A F0 0C    BEQ $B4A8       
.,B49C C5 07    CMP $07         
.,B49E F0 04    BEQ $B4A4       
.,B4A0 C5 08    CMP $08         
.,B4A2 D0 F3    BNE $B497       
.,B4A4 C9 22    CMP #$22        quote mark
.,B4A6 F0 01    BEQ $B4A9       
.,B4A8 18       CLC             
.,B4A9 84 61    STY $61         
.,B4AB 98       TYA             
.,B4AC 65 6F    ADC $6F         
.,B4AE 85 71    STA $71         
.,B4B0 A6 70    LDX $70         
.,B4B2 90 01    BCC $B4B5       
.,B4B4 E8       INX             
.,B4B5 86 72    STX $72         
.,B4B7 A5 70    LDA $70         
.,B4B9 F0 04    BEQ $B4BF       
.,B4BB C9 02    CMP #$02        
.,B4BD D0 0B    BNE $B4CA       
.,B4BF 98       TYA             
.,B4C0 20 75 B4 JSR $B475       
.,B4C3 A6 6F    LDX $6F         
.,B4C5 A4 70    LDY $70         
.,B4C7 20 88 B6 JSR $B688       

                                *** save descriptor from $61-$63 on stack
.,B4CA A6 16    LDX $16         
.,B4CC E0 22    CPX #$22        
.,B4CE D0 05    BNE $B4D5       
.,B4D0 A2 19    LDX #$19        
.,B4D2 4C 37 A4 JMP $A437       
.,B4D5 A5 61    LDA $61         
.,B4D7 95 00    STA $00,X       
.,B4D9 A5 62    LDA $62         
.,B4DB 95 01    STA $01,X       
.,B4DD A5 63    LDA $63         
.,B4DF 95 02    STA $02,X       
.,B4E1 A0 00    LDY #$00        
.,B4E3 86 64    STX $64         
.,B4E5 84 65    STY $65         
.,B4E7 84 70    STY $70         
.,B4E9 88       DEY             
.,B4EA 84 0D    STY $0D         
.,B4EC 86 17    STX $17         
.,B4EE E8       INX             
.,B4EF E8       INX             
.,B4F0 E8       INX             
.,B4F1 86 16    STX $16         
.,B4F3 60       RTS             

                                *** allocate number of bytes in A
.,B4F4 46 0F    LSR $0F         
.,B4F6 48       PHA             
.,B4F7 49 FF    EOR #$FF        
.,B4F9 38       SEC             
.,B4FA 65 33    ADC $33         
.,B4FC A4 34    LDY $34         
.,B4FE B0 01    BCS $B501       
.,B500 88       DEY             
.,B501 C4 32    CPY $32         
.,B503 90 11    BCC $B516       
.,B505 D0 04    BNE $B50B       
.,B507 C5 31    CMP $31         
.,B509 90 0B    BCC $B516       
.,B50B 85 33    STA $33         
.,B50D 84 34    STY $34         
.,B50F 85 35    STA $35         
.,B511 84 36    STY $36         
.,B513 AA       TAX             
.,B514 68       PLA             
.,B515 60       RTS             
.,B516 A2 10    LDX #$10        
.,B518 A5 0F    LDA $0F         
.,B51A 30 B6    BMI $B4D2       
.,B51C 20 26 B5 JSR $B526       
.,B51F A9 80    LDA #$80        
.,B521 85 0F    STA $0F         
.,B523 68       PLA             
.,B524 D0 D0    BNE $B4F6       

                                *** string garbage clean up
.,B526 A6 37    LDX $37         
.,B528 A5 38    LDA $38         
.,B52A 86 33    STX $33         
.,B52C 85 34    STA $34         
.,B52E A0 00    LDY #$00        
.,B530 84 4F    STY $4F         
.,B532 84 4E    STY $4E         
.,B534 A5 31    LDA $31         
.,B536 A6 32    LDX $32         
.,B538 85 5F    STA $5F         
.,B53A 86 60    STX $60         
.,B53C A9 19    LDA #$19        low  0019
.,B53E A2 00    LDX #$00        high 0019
.,B540 85 22    STA $22         
.,B542 86 23    STX $23         
.,B544 C5 16    CMP $16         
.,B546 F0 05    BEQ $B54D       
.,B548 20 C7 B5 JSR $B5C7       
.,B54B F0 F7    BEQ $B544       
.,B54D A9 07    LDA #$07        
.,B54F 85 53    STA $53         
.,B551 A5 2D    LDA $2D         
.,B553 A6 2E    LDX $2E         
.,B555 85 22    STA $22         
.,B557 86 23    STX $23         
.,B559 E4 30    CPX $30         
.,B55B D0 04    BNE $B561       
.,B55D C5 2F    CMP $2F         
.,B55F F0 05    BEQ $B566       
.,B561 20 BD B5 JSR $B5BD       
.,B564 F0 F3    BEQ $B559       
.,B566 85 58    STA $58         
.,B568 86 59    STX $59         
.,B56A A9 03    LDA #$03        
.,B56C 85 53    STA $53         
.,B56E A5 58    LDA $58         
.,B570 A6 59    LDX $59         
.,B572 E4 32    CPX $32         
.,B574 D0 07    BNE $B57D       
.,B576 C5 31    CMP $31         
.,B578 D0 03    BNE $B57D       
.,B57A 4C 06 B6 JMP $B606       
.,B57D 85 22    STA $22         
.,B57F 86 23    STX $23         
.,B581 A0 00    LDY #$00        
.,B583 B1 22    LDA ($22),Y     
.,B585 AA       TAX             
.,B586 C8       INY             
.,B587 B1 22    LDA ($22),Y     
.,B589 08       PHP             
.,B58A C8       INY             
.,B58B B1 22    LDA ($22),Y     
.,B58D 65 58    ADC $58         
.,B58F 85 58    STA $58         
.,B591 C8       INY             
.,B592 B1 22    LDA ($22),Y     
.,B594 65 59    ADC $59         
.,B596 85 59    STA $59         
.,B598 28       PLP             
.,B599 10 D3    BPL $B56E       
.,B59B 8A       TXA             
.,B59C 30 D0    BMI $B56E       
.,B59E C8       INY             
.,B59F B1 22    LDA ($22),Y     
.,B5A1 A0 00    LDY #$00        
.,B5A3 0A       ASL             
.,B5A4 69 05    ADC #$05        
.,B5A6 65 22    ADC $22         
.,B5A8 85 22    STA $22         
.,B5AA 90 02    BCC $B5AE       
.,B5AC E6 23    INC $23         
.,B5AE A6 23    LDX $23         
.,B5B0 E4 59    CPX $59         
.,B5B2 D0 04    BNE $B5B8       
.,B5B4 C5 58    CMP $58         
.,B5B6 F0 BA    BEQ $B572       
.,B5B8 20 C7 B5 JSR $B5C7       
.,B5BB F0 F3    BEQ $B5B0       

                                *** check string area
.,B5BD B1 22    LDA ($22),Y     
.,B5BF 30 35    BMI $B5F6       
.,B5C1 C8       INY             
.,B5C2 B1 22    LDA ($22),Y     
.,B5C4 10 30    BPL $B5F6       
.,B5C6 C8       INY             

                                *** check string area
.,B5C7 B1 22    LDA ($22),Y     
.,B5C9 F0 2B    BEQ $B5F6       
.,B5CB C8       INY             
.,B5CC B1 22    LDA ($22),Y     
.,B5CE AA       TAX             
.,B5CF C8       INY             
.,B5D0 B1 22    LDA ($22),Y     
.,B5D2 C5 34    CMP $34         
.,B5D4 90 06    BCC $B5DC       
.,B5D6 D0 1E    BNE $B5F6       
.,B5D8 E4 33    CPX $33         
.,B5DA B0 1A    BCS $B5F6       
.,B5DC C5 60    CMP $60         
.,B5DE 90 16    BCC $B5F6       
.,B5E0 D0 04    BNE $B5E6       
.,B5E2 E4 5F    CPX $5F         
.,B5E4 90 10    BCC $B5F6       
.,B5E6 86 5F    STX $5F         
.,B5E8 85 60    STA $60         
.,B5EA A5 22    LDA $22         
.,B5EC A6 23    LDX $23         
.,B5EE 85 4E    STA $4E         
.,B5F0 86 4F    STX $4F         
.,B5F2 A5 53    LDA $53         
.,B5F4 85 55    STA $55         
.,B5F6 A5 53    LDA $53         
.,B5F8 18       CLC             
.,B5F9 65 22    ADC $22         
.,B5FB 85 22    STA $22         
.,B5FD 90 02    BCC $B601       
.,B5FF E6 23    INC $23         
.,B601 A6 23    LDX $23         
.,B603 A0 00    LDY #$00        
.,B605 60       RTS             

                                *** continuation of garbage clean up
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

                                *** joining strings
.,B63D A5 65    LDA $65         
.,B63F 48       PHA             
.,B640 A5 64    LDA $64         
.,B642 48       PHA             
.,B643 20 83 AE JSR $AE83       
.,B646 20 8F AD JSR $AD8F       
.,B649 68       PLA             
.,B64A 85 6F    STA $6F         
.,B64C 68       PLA             
.,B64D 85 70    STA $70         
.,B64F A0 00    LDY #$00        
.,B651 B1 6F    LDA ($6F),Y     
.,B653 18       CLC             
.,B654 71 64    ADC ($64),Y     
.,B656 90 05    BCC $B65D       
.,B658 A2 17    LDX #$17        
.,B65A 4C 37 A4 JMP $A437       
.,B65D 20 75 B4 JSR $B475       
.,B660 20 7A B6 JSR $B67A       
.,B663 A5 50    LDA $50         
.,B665 A4 51    LDY $51         
.,B667 20 AA B6 JSR $B6AA       
.,B66A 20 8C B6 JSR $B68C       
.,B66D A5 6F    LDA $6F         
.,B66F A4 70    LDY $70         
.,B671 20 AA B6 JSR $B6AA       
.,B674 20 CA B4 JSR $B4CA       
.,B677 4C B8 AD JMP $ADB8       

                                *** move string
.,B67A A0 00    LDY #$00        
.,B67C B1 6F    LDA ($6F),Y     
.,B67E 48       PHA             
.,B67F C8       INY             
.,B680 B1 6F    LDA ($6F),Y     
.,B682 AA       TAX             
.,B683 C8       INY             
.,B684 B1 6F    LDA ($6F),Y     
.,B686 A8       TAY             
.,B687 68       PLA             

                                *** move string with length A, pointer in XY
.,B688 86 22    STX $22         
.,B68A 84 23    STY $23         
.,B68C A8       TAY             
.,B68D F0 0A    BEQ $B699       
.,B68F 48       PHA             
.,B690 88       DEY             
.,B691 B1 22    LDA ($22),Y     
.,B693 91 35    STA ($35),Y     
.,B695 98       TYA             
.,B696 D0 F8    BNE $B690       
.,B698 68       PLA             
.,B699 18       CLC             
.,B69A 65 35    ADC $35         
.,B69C 85 35    STA $35         
.,B69E 90 02    BCC $B6A2       
.,B6A0 E6 36    INC $36         
.,B6A2 60       RTS             

                                *** de-allocate temporary string
.,B6A3 20 8F AD JSR $AD8F       
.,B6A6 A5 64    LDA $64         
.,B6A8 A4 65    LDY $65         
.,B6AA 85 22    STA $22         
.,B6AC 84 23    STY $23         
.,B6AE 20 DB B6 JSR $B6DB       
.,B6B1 08       PHP             
.,B6B2 A0 00    LDY #$00        
.,B6B4 B1 22    LDA ($22),Y     
.,B6B6 48       PHA             
.,B6B7 C8       INY             
.,B6B8 B1 22    LDA ($22),Y     
.,B6BA AA       TAX             
.,B6BB C8       INY             
.,B6BC B1 22    LDA ($22),Y     
.,B6BE A8       TAY             
.,B6BF 68       PLA             
.,B6C0 28       PLP             
.,B6C1 D0 13    BNE $B6D6       
.,B6C3 C4 34    CPY $34         
.,B6C5 D0 0F    BNE $B6D6       
.,B6C7 E4 33    CPX $33         
.,B6C9 D0 0B    BNE $B6D6       
.,B6CB 48       PHA             
.,B6CC 18       CLC             
.,B6CD 65 33    ADC $33         
.,B6CF 85 33    STA $33         
.,B6D1 90 02    BCC $B6D5       
.,B6D3 E6 34    INC $34         
.,B6D5 68       PLA             
.,B6D6 86 22    STX $22         
.,B6D8 84 23    STY $23         
.,B6DA 60       RTS             

                                *** check descriptor stack
.,B6DB C4 18    CPY $18         
.,B6DD D0 0C    BNE $B6EB       
.,B6DF C5 17    CMP $17         
.,B6E1 D0 08    BNE $B6EB       
.,B6E3 85 16    STA $16         
.,B6E5 E9 03    SBC #$03        
.,B6E7 85 17    STA $17         
.,B6E9 A0 00    LDY #$00        
.,B6EB 60       RTS             

                                *** CHR$ function
.,B6EC 20 A1 B7 JSR $B7A1       
.,B6EF 8A       TXA             
.,B6F0 48       PHA             
.,B6F1 A9 01    LDA #$01        
.,B6F3 20 7D B4 JSR $B47D       
.,B6F6 68       PLA             
.,B6F7 A0 00    LDY #$00        
.,B6F9 91 62    STA ($62),Y     
.,B6FB 68       PLA             
.,B6FC 68       PLA             
.,B6FD 4C CA B4 JMP $B4CA       

                                *** LEFT$ function
.,B700 20 61 B7 JSR $B761       
.,B703 D1 50    CMP ($50),Y     
.,B705 98       TYA             
.,B706 90 04    BCC $B70C       
.,B708 B1 50    LDA ($50),Y     
.,B70A AA       TAX             
.,B70B 98       TYA             
.,B70C 48       PHA             
.,B70D 8A       TXA             
.,B70E 48       PHA             
.,B70F 20 7D B4 JSR $B47D       
.,B712 A5 50    LDA $50         
.,B714 A4 51    LDY $51         
.,B716 20 AA B6 JSR $B6AA       
.,B719 68       PLA             
.,B71A A8       TAY             
.,B71B 68       PLA             
.,B71C 18       CLC             
.,B71D 65 22    ADC $22         
.,B71F 85 22    STA $22         
.,B721 90 02    BCC $B725       
.,B723 E6 23    INC $23         
.,B725 98       TYA             
.,B726 20 8C B6 JSR $B68C       
.,B729 4C CA B4 JMP $B4CA       

                                *** RIGHT$ function
.,B72C 20 61 B7 JSR $B761       
.,B72F 18       CLC             
.,B730 F1 50    SBC ($50),Y     
.,B732 49 FF    EOR #$FF        
.,B734 4C 06 B7 JMP $B706       

                                *** MID$ function
.,B737 A9 FF    LDA #$FF        default 3 parameter
.,B739 85 65    STA $65         
.,B73B 20 79 00 JSR $0079       
.,B73E C9 29    CMP #$29        )
.,B740 F0 06    BEQ $B748       
.,B742 20 FD AE JSR $AEFD       
.,B745 20 9E B7 JSR $B79E       
.,B748 20 61 B7 JSR $B761       
.,B74B F0 4B    BEQ $B798       
.,B74D CA       DEX             
.,B74E 8A       TXA             
.,B74F 48       PHA             
.,B750 18       CLC             
.,B751 A2 00    LDX #$00        
.,B753 F1 50    SBC ($50),Y     
.,B755 B0 B6    BCS $B70D       
.,B757 49 FF    EOR #$FF        
.,B759 C5 65    CMP $65         
.,B75B 90 B1    BCC $B70E       
.,B75D A5 65    LDA $65         
.,B75F B0 AD    BCS $B70E       

                                *** get first 2 parameters for
                                LEFT$, RIGHT$ and MID$
.,B761 20 F7 AE JSR $AEF7       
.,B764 68       PLA             
.,B765 A8       TAY             
.,B766 68       PLA             
.,B767 85 55    STA $55         
.,B769 68       PLA             
.,B76A 68       PLA             
.,B76B 68       PLA             
.,B76C AA       TAX             
.,B76D 68       PLA             
.,B76E 85 50    STA $50         
.,B770 68       PLA             
.,B771 85 51    STA $51         
.,B773 A5 55    LDA $55         
.,B775 48       PHA             
.,B776 98       TYA             
.,B777 48       PHA             
.,B778 A0 00    LDY #$00        
.,B77A 8A       TXA             
.,B77B 60       RTS             

                                *** LEN function
.,B77C 20 82 B7 JSR $B782       
.,B77F 4C A2 B3 JMP $B3A2       
.,B782 20 A3 B6 JSR $B6A3       
.,B785 A2 00    LDX #$00        
.,B787 86 0D    STX $0D         
.,B789 A8       TAY             
.,B78A 60       RTS             

                                *** ASC function
.,B78B 20 82 B7 JSR $B782       
.,B78E F0 08    BEQ $B798       
.,B790 A0 00    LDY #$00        
.,B792 B1 22    LDA ($22),Y     
.,B794 A8       TAY             
.,B795 4C A2 B3 JMP $B3A2       
.,B798 4C 48 B2 JMP $B248       

                                *** fetch integer value in X and check range
.,B79B 20 73 00 JSR $0073       
.,B79E 20 8A AD JSR $AD8A       
.,B7A1 20 B8 B1 JSR $B1B8       
.,B7A4 A6 64    LDX $64         
.,B7A6 D0 F0    BNE $B798       
.,B7A8 A6 65    LDX $65         
.,B7AA 4C 79 00 JMP $0079       

                                *** VAL function
.,B7AD 20 82 B7 JSR $B782       
.,B7B0 D0 03    BNE $B7B5       
.,B7B2 4C F7 B8 JMP $B8F7       
.,B7B5 A6 7A    LDX $7A         
.,B7B7 A4 7B    LDY $7B         
.,B7B9 86 71    STX $71         
.,B7BB 84 72    STY $72         
.,B7BD A6 22    LDX $22         
.,B7BF 86 7A    STX $7A         
.,B7C1 18       CLC             
.,B7C2 65 22    ADC $22         
.,B7C4 85 24    STA $24         
.,B7C6 A6 23    LDX $23         
.,B7C8 86 7B    STX $7B         
.,B7CA 90 01    BCC $B7CD       
.,B7CC E8       INX             
.,B7CD 86 25    STX $25         
.,B7CF A0 00    LDY #$00        
.,B7D1 B1 24    LDA ($24),Y     
.,B7D3 48       PHA             
.,B7D4 98       TYA             
.,B7D5 91 24    STA ($24),Y     
.,B7D7 20 79 00 JSR $0079       
.,B7DA 20 F3 BC JSR $BCF3       
.,B7DD 68       PLA             
.,B7DE A0 00    LDY #$00        
.,B7E0 91 24    STA ($24),Y     
.,B7E2 A6 71    LDX $71         
.,B7E4 A4 72    LDY $72         
.,B7E6 86 7A    STX $7A         
.,B7E8 84 7B    STY $7B         
.,B7EA 60       RTS             

                                *** get address into $14/$15 and integer in X
.,B7EB 20 8A AD JSR $AD8A       
.,B7EE 20 F7 B7 JSR $B7F7       
.,B7F1 20 FD AE JSR $AEFD       
.,B7F4 4C 9E B7 JMP $B79E       

                                *** convert float ti integer in $14/$15
.,B7F7 A5 66    LDA $66         
.,B7F9 30 9D    BMI $B798       
.,B7FB A5 61    LDA $61         
.,B7FD C9 91    CMP #$91        
.,B7FF B0 97    BCS $B798       
.,B801 20 9B BC JSR $BC9B       
.,B804 A5 64    LDA $64         
.,B806 A4 65    LDY $65         
.,B808 84 14    STY $14         
.,B80A 85 15    STA $15         
.,B80C 60       RTS             

                                *** PEEK function
.,B80D A5 15    LDA $15         
.,B80F 48       PHA             
.,B810 A5 14    LDA $14         
.,B812 48       PHA             
.,B813 20 F7 B7 JSR $B7F7       
.,B816 A0 00    LDY #$00        
.,B818 B1 14    LDA ($14),Y     
.,B81A A8       TAY             
.,B81B 68       PLA             
.,B81C 85 14    STA $14         
.,B81E 68       PLA             
.,B81F 85 15    STA $15         
.,B821 4C A2 B3 JMP $B3A2       

                                *** POKE command
.,B824 20 EB B7 JSR $B7EB       
.,B827 8A       TXA             
.,B828 A0 00    LDY #$00        
.,B82A 91 14    STA ($14),Y     
.,B82C 60       RTS             

                                *** WAIT command
.,B82D 20 EB B7 JSR $B7EB       
.,B830 86 49    STX $49         
.,B832 A2 00    LDX #$00        
.,B834 20 79 00 JSR $0079       
.,B837 F0 03    BEQ $B83C       
.,B839 20 F1 B7 JSR $B7F1       
.,B83C 86 4A    STX $4A         
.,B83E A0 00    LDY #$00        
.,B840 B1 14    LDA ($14),Y     
.,B842 45 4A    EOR $4A         
.,B844 25 49    AND $49         
.,B846 F0 F8    BEQ $B840       
.,B848 60       RTS             

                                *** add 0.5 to float accu (rounding)
.,B849 A9 11    LDA #$11        low  BF11
.,B84B A0 BF    LDY #$BF        high BF11
.,B84D 4C 67 B8 JMP $B867       

                                *** minus operator
.,B850 20 8C BA JSR $BA8C       
.,B853 A5 66    LDA $66         
.,B855 49 FF    EOR #$FF        
.,B857 85 66    STA $66         
.,B859 45 6E    EOR $6E         
.,B85B 85 6F    STA $6F         
.,B85D A5 61    LDA $61         
.,B85F 4C 6A B8 JMP $B86A       
.,B862 20 99 B9 JSR $B999       
.,B865 90 3C    BCC $B8A3       

                                *** add float indexed by AY to float accu
.,B867 20 8C BA JSR $BA8C       

                                *** plus operator
.,B86A D0 03    BNE $B86F       
.,B86C 4C FC BB JMP $BBFC       
.,B86F A6 70    LDX $70         
.,B871 86 56    STX $56         
.,B873 A2 69    LDX #$69        
.,B875 A5 69    LDA $69         
.,B877 A8       TAY             
.,B878 F0 CE    BEQ $B848       
.,B87A 38       SEC             
.,B87B E5 61    SBC $61         
.,B87D F0 24    BEQ $B8A3       
.,B87F 90 12    BCC $B893       
.,B881 84 61    STY $61         
.,B883 A4 6E    LDY $6E         
.,B885 84 66    STY $66         
.,B887 49 FF    EOR #$FF        
.,B889 69 00    ADC #$00        
.,B88B A0 00    LDY #$00        
.,B88D 84 56    STY $56         
.,B88F A2 61    LDX #$61        
.,B891 D0 04    BNE $B897       
.,B893 A0 00    LDY #$00        
.,B895 84 70    STY $70         
.,B897 C9 F9    CMP #$F9        
.,B899 30 C7    BMI $B862       
.,B89B A8       TAY             
.,B89C A5 70    LDA $70         
.,B89E 56 01    LSR $01,X       
.,B8A0 20 B0 B9 JSR $B9B0       
.,B8A3 24 6F    BIT $6F         
.,B8A5 10 57    BPL $B8FE       
.,B8A7 A0 61    LDY #$61        
.,B8A9 E0 69    CPX #$69        
.,B8AB F0 02    BEQ $B8AF       
.,B8AD A0 69    LDY #$69        
.,B8AF 38       SEC             
.,B8B0 49 FF    EOR #$FF        
.,B8B2 65 56    ADC $56         
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
.,B8D2 B0 03    BCS $B8D7       
.,B8D4 20 47 B9 JSR $B947       
.,B8D7 A0 00    LDY #$00        
.,B8D9 98       TYA             
.,B8DA 18       CLC             
.,B8DB A6 62    LDX $62         
.,B8DD D0 4A    BNE $B929       
.,B8DF A6 63    LDX $63         
.,B8E1 86 62    STX $62         
.,B8E3 A6 64    LDX $64         
.,B8E5 86 63    STX $63         
.,B8E7 A6 65    LDX $65         
.,B8E9 86 64    STX $64         
.,B8EB A6 70    LDX $70         
.,B8ED 86 65    STX $65         
.,B8EF 84 70    STY $70         
.,B8F1 69 08    ADC #$08        
.,B8F3 C9 20    CMP #$20        
.,B8F5 D0 E4    BNE $B8DB       
.,B8F7 A9 00    LDA #$00        
.,B8F9 85 61    STA $61         
.,B8FB 85 66    STA $66         
.,B8FD 60       RTS             

                                *** add fractions
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

                                *** postshift
.,B91D 69 01    ADC #$01        
.,B91F 06 70    ASL $70         
.,B921 26 65    ROL $65         
.,B923 26 64    ROL $64         
.,B925 26 63    ROL $63         
.,B927 26 62    ROL $62         
.,B929 10 F2    BPL $B91D       
.,B92B 38       SEC             
.,B92C E5 61    SBC $61         
.,B92E B0 C7    BCS $B8F7       
.,B930 49 FF    EOR #$FF        
.,B932 69 01    ADC #$01        
.,B934 85 61    STA $61         
.,B936 90 0E    BCC $B946       
.,B938 E6 61    INC $61         
.,B93A F0 42    BEQ $B97E       
.,B93C 66 62    ROR $62         
.,B93E 66 63    ROR $63         
.,B940 66 64    ROR $64         
.,B942 66 65    ROR $65         
.,B944 66 70    ROR $70         
.,B946 60       RTS             

                                *** negate float accu
.,B947 A5 66    LDA $66         
.,B949 49 FF    EOR #$FF        
.,B94B 85 66    STA $66         
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
.,B96B E6 70    INC $70         
.,B96D D0 0E    BNE $B97D       

                                *** increment fraction
.,B96F E6 65    INC $65         
.,B971 D0 0A    BNE $B97D       
.,B973 E6 64    INC $64         
.,B975 D0 06    BNE $B97D       
.,B977 E6 63    INC $63         
.,B979 D0 02    BNE $B97D       
.,B97B E6 62    INC $62         
.,B97D 60       RTS             
.,B97E A2 0F    LDX #$0F        error number
.,B980 4C 37 A4 JMP $A437       

                                *** preshift
.,B983 A2 25    LDX #$25        
.,B985 B4 04    LDY $04,X       
.,B987 84 70    STY $70         
.,B989 B4 03    LDY $03,X       
.,B98B 94 04    STY $04,X       
.,B98D B4 02    LDY $02,X       
.,B98F 94 03    STY $03,X       
.,B991 B4 01    LDY $01,X       
.,B993 94 02    STY $02,X       
.,B995 A4 68    LDY $68         
.,B997 94 01    STY $01,X       
.,B999 69 08    ADC #$08        
.,B99B 30 E8    BMI $B985       
.,B99D F0 E6    BEQ $B985       
.,B99F E9 08    SBC #$08        
.,B9A1 A8       TAY             
.,B9A2 A5 70    LDA $70         
.,B9A4 B0 14    BCS $B9BA       
.,B9A6 16 01    ASL $01,X       
.,B9A8 90 02    BCC $B9AC       
.,B9AA F6 01    INC $01,X       
.,B9AC 76 01    ROR $01,X       
.,B9AE 76 01    ROR $01,X       
.,B9B0 76 02    ROR $02,X       
.,B9B2 76 03    ROR $03,X       
.,B9B4 76 04    ROR $04,X       
.,B9B6 6A       ROR             
.,B9B7 C8       INY             
.,B9B8 D0 EC    BNE $B9A6       
.,B9BA 18       CLC             
.,B9BB 60       RTS             

                                *** 1
.:B9BC 81 00 00 00 00           

                                *** LOG polynomial table
.:B9C1 03                       degree 4
.:B9C2 7F 5E 56 CB 79           
.:B9C7 80 13 9B 0B 64           
.:B9CC 80 76 38 93 16           
.:B9D1 82 38 AA 3B 20           

                                *** 0,5 * SQR(2)
.:B9D6 80 35 04 F3 34           

                                *** SQR(2)
.:B9DB 81 35 04 F3 34           

                                *** -0.5
.:B9E0 80 80 00 00 00           

                                *** LOG(2)
.:B9E5 80 31 72 17 F8           

                                *** LOG function
.,B9EA 20 2B BC JSR $BC2B       
.,B9ED F0 02    BEQ $B9F1       
.,B9EF 10 03    BPL $B9F4       
.,B9F1 4C 48 B2 JMP $B248       
.,B9F4 A5 61    LDA $61         
.,B9F6 E9 7F    SBC #$7F        
.,B9F8 48       PHA             
.,B9F9 A9 80    LDA #$80        
.,B9FB 85 61    STA $61         
.,B9FD A9 D6    LDA #$D6        low  B9D6
.,B9FF A0 B9    LDY #$B9        high B9D6
.,BA01 20 67 B8 JSR $B867       
.,BA04 A9 DB    LDA #$DB        low  B9DB
.,BA06 A0 B9    LDY #$B9        high B9DB
.,BA08 20 0F BB JSR $BB0F       
.,BA0B A9 BC    LDA #$BC        low  B9BC
.,BA0D A0 B9    LDY #$B9        high B9BC
.,BA0F 20 50 B8 JSR $B850       
.,BA12 A9 C1    LDA #$C1        low  B9C1
.,BA14 A0 B9    LDY #$B9        high B9C1
.,BA16 20 43 E0 JSR $E043       
.,BA19 A9 E0    LDA #$E0        low  B9E0
.,BA1B A0 B9    LDY #$B9        high B9E0
.,BA1D 20 67 B8 JSR $B867       
.,BA20 68       PLA             
.,BA21 20 7E BD JSR $BD7E       
.,BA24 A9 E5    LDA #$E5        low  B9E5
.,BA26 A0 B9    LDY #$B9        high B9E5
.,BA28 20 8C BA JSR $BA8C       

                                *** times operator
.,BA2B D0 03    BNE $BA30       
.,BA2D 4C 8B BA JMP $BA8B       
.,BA30 20 B7 BA JSR $BAB7       
.,BA33 A9 00    LDA #$00        
.,BA35 85 26    STA $26         
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
.,BA59 D0 03    BNE $BA5E       
.,BA5B 4C 83 B9 JMP $B983       
.,BA5E 4A       LSR             
.,BA5F 09 80    ORA #$80        
.,BA61 A8       TAY             
.,BA62 90 19    BCC $BA7D       
.,BA64 18       CLC             
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
.,BA7D 66 26    ROR $26         
.,BA7F 66 27    ROR $27         
.,BA81 66 28    ROR $28         
.,BA83 66 29    ROR $29         
.,BA85 66 70    ROR $70         
.,BA87 98       TYA             
.,BA88 4A       LSR             
.,BA89 D0 D6    BNE $BA61       
.,BA8B 60       RTS             

                                *** move float indexed by AY into second float accu
.,BA8C 85 22    STA $22         
.,BA8E 84 23    STY $23         
.,BA90 A0 04    LDY #$04        
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
.,BAA5 45 66    EOR $66         
.,BAA7 85 6F    STA $6F         
.,BAA9 A5 6E    LDA $6E         
.,BAAB 09 80    ORA #$80        
.,BAAD 85 6A    STA $6A         
.,BAAF 88       DEY             
.,BAB0 B1 22    LDA ($22),Y     
.,BAB2 85 69    STA $69         
.,BAB4 A5 61    LDA $61         
.,BAB6 60       RTS             

                                *** add exponents
.,BAB7 A5 69    LDA $69         
.,BAB9 F0 1F    BEQ $BADA       
.,BABB 18       CLC             
.,BABC 65 61    ADC $61         
.,BABE 90 04    BCC $BAC4       
.,BAC0 30 1D    BMI $BADF       
.,BAC2 18       CLC             
.:BAC3 2C       .BYTE $2C       
.,BAC4 10 14    BPL $BADA       
.,BAC6 69 80    ADC #$80        
.,BAC8 85 61    STA $61         
.,BACA D0 03    BNE $BACF       
.,BACC 4C FB B8 JMP $B8FB       
.,BACF A5 6F    LDA $6F         
.,BAD1 85 66    STA $66         
.,BAD3 60       RTS             
.,BAD4 A5 66    LDA $66         
.,BAD6 49 FF    EOR #$FF        
.,BAD8 30 05    BMI $BADF       
.,BADA 68       PLA             
.,BADB 68       PLA             
.,BADC 4C F7 B8 JMP $B8F7       
.,BADF 4C 7E B9 JMP $B97E       

                                *** multiply float accu by 10
.,BAE2 20 0C BC JSR $BC0C       
.,BAE5 AA       TAX             
.,BAE6 F0 10    BEQ $BAF8       
.,BAE8 18       CLC             
.,BAE9 69 02    ADC #$02        
.,BAEB B0 F2    BCS $BADF       
.,BAED A2 00    LDX #$00        
.,BAEF 86 6F    STX $6F         
.,BAF1 20 77 B8 JSR $B877       
.,BAF4 E6 61    INC $61         
.,BAF6 F0 E7    BEQ $BADF       
.,BAF8 60       RTS             

                                *** constant 10 for division
.:BAF9 84 20 00 00 00           

                                *** divide float by 10
.,BAFE 20 0C BC JSR $BC0C       
.,BB01 A9 F9    LDA #$F9        low  BAF9
.,BB03 A0 BA    LDY #$BA        high BAF9
.,BB05 A2 00    LDX #$00        
.,BB07 86 6F    STX $6F         
.,BB09 20 A2 BB JSR $BBA2       
.,BB0C 4C 12 BB JMP $BB12       

                                *** divide number indexed by AY by float accu
.,BB0F 20 8C BA JSR $BA8C       

                                *** divide operator
.,BB12 F0 76    BEQ $BB8A       
.,BB14 20 1B BC JSR $BC1B       
.,BB17 A9 00    LDA #$00        
.,BB19 38       SEC             
.,BB1A E5 61    SBC $61         
.,BB1C 85 61    STA $61         
.,BB1E 20 B7 BA JSR $BAB7       
.,BB21 E6 61    INC $61         
.,BB23 F0 BA    BEQ $BADF       
.,BB25 A2 FC    LDX #$FC        
.,BB27 A9 01    LDA #$01        
.,BB29 A4 6A    LDY $6A         
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
.,BB3F 08       PHP             
.,BB40 2A       ROL             
.,BB41 90 09    BCC $BB4C       
.,BB43 E8       INX             
.,BB44 95 29    STA $29,X       
.,BB46 F0 32    BEQ $BB7A       
.,BB48 10 34    BPL $BB7E       
.,BB4A A9 01    LDA #$01        
.,BB4C 28       PLP             
.,BB4D B0 0E    BCS $BB5D       
.,BB4F 06 6D    ASL $6D         
.,BB51 26 6C    ROL $6C         
.,BB53 26 6B    ROL $6B         
.,BB55 26 6A    ROL $6A         
.,BB57 B0 E6    BCS $BB3F       
.,BB59 30 CE    BMI $BB29       
.,BB5B 10 E2    BPL $BB3F       
.,BB5D A8       TAY             
.,BB5E A5 6D    LDA $6D         
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
.,BB76 98       TYA             
.,BB77 4C 4F BB JMP $BB4F       
.,BB7A A9 40    LDA #$40        
.,BB7C D0 CE    BNE $BB4C       
.,BB7E 0A       ASL             
.,BB7F 0A       ASL             
.,BB80 0A       ASL             
.,BB81 0A       ASL             
.,BB82 0A       ASL             
.,BB83 0A       ASL             
.,BB84 85 70    STA $70         
.,BB86 28       PLP             
.,BB87 4C 8F BB JMP $BB8F       
.,BB8A A2 14    LDX #$14        error number
.,BB8C 4C 37 A4 JMP $A437       
.,BB8F A5 26    LDA $26         
.,BB91 85 62    STA $62         
.,BB93 A5 27    LDA $27         
.,BB95 85 63    STA $63         
.,BB97 A5 28    LDA $28         
.,BB99 85 64    STA $64         
.,BB9B A5 29    LDA $29         
.,BB9D 85 65    STA $65         
.,BB9F 4C D7 B8 JMP $B8D7       
.,BBA2 85 22    STA $22         
.,BBA4 84 23    STY $23         
.,BBA6 A0 04    LDY #$04        
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
.,BBB9 85 66    STA $66         
.,BBBB 09 80    ORA #$80        
.,BBBD 85 62    STA $62         
.,BBBF 88       DEY             
.,BBC0 B1 22    LDA ($22),Y     
.,BBC2 85 61    STA $61         
.,BBC4 84 70    STY $70         
.,BBC6 60       RTS             

                                *** store float accu at $5C-$60
.,BBC7 A2 5C    LDX #$5C        low  005C
.:BBC9 2C       .BYTE $2C       

                                *** store float accu at $57-$5B
.,BBCA A2 57    LDX #$57        low  0057
.,BBCC A0 00    LDY #$00        high 0057
.,BBCE F0 04    BEQ $BBD4       

                                *** store float accu in index at $49/$4A
.,BBD0 A6 49    LDX $49         
.,BBD2 A4 4A    LDY $4A         

                                *** store float accu in index XY
.,BBD4 20 1B BC JSR $BC1B       
.,BBD7 86 22    STX $22         
.,BBD9 84 23    STY $23         
.,BBDB A0 04    LDY #$04        
.,BBDD A5 65    LDA $65         
.,BBDF 91 22    STA ($22),Y     
.,BBE1 88       DEY             
.,BBE2 A5 64    LDA $64         
.,BBE4 91 22    STA ($22),Y     
.,BBE6 88       DEY             
.,BBE7 A5 63    LDA $63         
.,BBE9 91 22    STA ($22),Y     
.,BBEB 88       DEY             
.,BBEC A5 66    LDA $66         
.,BBEE 09 7F    ORA #$7F        
.,BBF0 25 62    AND $62         
.,BBF2 91 22    STA ($22),Y     
.,BBF4 88       DEY             
.,BBF5 A5 61    LDA $61         
.,BBF7 91 22    STA ($22),Y     
.,BBF9 84 70    STY $70         
.,BBFB 60       RTS             

                                *** move second float accu into first
.,BBFC A5 6E    LDA $6E         
.,BBFE 85 66    STA $66         
.,BC00 A2 05    LDX #$05        
.,BC02 B5 68    LDA $68,X       
.,BC04 95 60    STA $60,X       
.,BC06 CA       DEX             
.,BC07 D0 F9    BNE $BC02       
.,BC09 86 70    STX $70         
.,BC0B 60       RTS             

                                *** move rounded float accu into second
.,BC0C 20 1B BC JSR $BC1B       
.,BC0F A2 06    LDX #$06        
.,BC11 B5 60    LDA $60,X       
.,BC13 95 68    STA $68,X       
.,BC15 CA       DEX             
.,BC16 D0 F9    BNE $BC11       
.,BC18 86 70    STX $70         
.,BC1A 60       RTS             

                                *** round float accu according to guard bit
.,BC1B A5 61    LDA $61         
.,BC1D F0 FB    BEQ $BC1A       
.,BC1F 06 70    ASL $70         
.,BC21 90 F7    BCC $BC1A       
.,BC23 20 6F B9 JSR $B96F       
.,BC26 D0 F2    BNE $BC1A       
.,BC28 4C 38 B9 JMP $B938       

                                *** get sign of float accu in A
.,BC2B A5 61    LDA $61         
.,BC2D F0 09    BEQ $BC38       
.,BC2F A5 66    LDA $66         
.,BC31 2A       ROL             
.,BC32 A9 FF    LDA #$FF        
.,BC34 B0 02    BCS $BC38       
.,BC36 A9 01    LDA #$01        
.,BC38 60       RTS             

                                *** SGN function
.,BC39 20 2B BC JSR $BC2B       

                                *** move signed number from A into float accu
.,BC3C 85 62    STA $62         
.,BC3E A9 00    LDA #$00        
.,BC40 85 63    STA $63         
.,BC42 A2 88    LDX #$88        
.,BC44 A5 62    LDA $62         
.,BC46 49 FF    EOR #$FF        
.,BC48 2A       ROL             
.,BC49 A9 00    LDA #$00        
.,BC4B 85 65    STA $65         
.,BC4D 85 64    STA $64         
.,BC4F 86 61    STX $61         
.,BC51 85 70    STA $70         
.,BC53 85 66    STA $66         
.,BC55 4C D2 B8 JMP $B8D2       

                                *** ABS function
.,BC58 46 66    LSR $66         
.,BC5A 60       RTS             

                                *** compare float accu to float indexed by XY
.,BC5B 85 24    STA $24         
.,BC5D 84 25    STY $25         
.,BC5F A0 00    LDY #$00        
.,BC61 B1 24    LDA ($24),Y     
.,BC63 C8       INY             
.,BC64 AA       TAX             
.,BC65 F0 C4    BEQ $BC2B       
.,BC67 B1 24    LDA ($24),Y     
.,BC69 45 66    EOR $66         
.,BC6B 30 C2    BMI $BC2F       
.,BC6D E4 61    CPX $61         
.,BC6F D0 21    BNE $BC92       
.,BC71 B1 24    LDA ($24),Y     
.,BC73 09 80    ORA #$80        
.,BC75 C5 62    CMP $62         
.,BC77 D0 19    BNE $BC92       
.,BC79 C8       INY             
.,BC7A B1 24    LDA ($24),Y     
.,BC7C C5 63    CMP $63         
.,BC7E D0 12    BNE $BC92       
.,BC80 C8       INY             
.,BC81 B1 24    LDA ($24),Y     
.,BC83 C5 64    CMP $64         
.,BC85 D0 0B    BNE $BC92       
.,BC87 C8       INY             
.,BC88 A9 7F    LDA #$7F        
.,BC8A C5 70    CMP $70         
.,BC8C B1 24    LDA ($24),Y     
.,BC8E E5 65    SBC $65         
.,BC90 F0 28    BEQ $BCBA       
.,BC92 A5 66    LDA $66         
.,BC94 90 02    BCC $BC98       
.,BC96 49 FF    EOR #$FF        
.,BC98 4C 31 BC JMP $BC31       

                                *** convert float to a 4 byte signed integer
.,BC9B A5 61    LDA $61         
.,BC9D F0 4A    BEQ $BCE9       
.,BC9F 38       SEC             
.,BCA0 E9 A0    SBC #$A0        
.,BCA2 24 66    BIT $66         
.,BCA4 10 09    BPL $BCAF       
.,BCA6 AA       TAX             
.,BCA7 A9 FF    LDA #$FF        
.,BCA9 85 68    STA $68         
.,BCAB 20 4D B9 JSR $B94D       
.,BCAE 8A       TXA             
.,BCAF A2 61    LDX #$61        
.,BCB1 C9 F9    CMP #$F9        
.,BCB3 10 06    BPL $BCBB       
.,BCB5 20 99 B9 JSR $B999       
.,BCB8 84 68    STY $68         
.,BCBA 60       RTS             
.,BCBB A8       TAY             
.,BCBC A5 66    LDA $66         
.,BCBE 29 80    AND #$80        
.,BCC0 46 62    LSR $62         
.,BCC2 05 62    ORA $62         
.,BCC4 85 62    STA $62         
.,BCC6 20 B0 B9 JSR $B9B0       
.,BCC9 84 68    STY $68         
.,BCCB 60       RTS             

                                *** INT function
.,BCCC A5 61    LDA $61         
.,BCCE C9 A0    CMP #$A0        
.,BCD0 B0 20    BCS $BCF2       
.,BCD2 20 9B BC JSR $BC9B       
.,BCD5 84 70    STY $70         
.,BCD7 A5 66    LDA $66         
.,BCD9 84 66    STY $66         
.,BCDB 49 80    EOR #$80        
.,BCDD 2A       ROL             
.,BCDE A9 A0    LDA #$A0        
.,BCE0 85 61    STA $61         
.,BCE2 A5 65    LDA $65         
.,BCE4 85 07    STA $07         
.,BCE6 4C D2 B8 JMP $B8D2       

                                *** clear float accu
.,BCE9 85 62    STA $62         
.,BCEB 85 63    STA $63         
.,BCED 85 64    STA $64         
.,BCEF 85 65    STA $65         
.,BCF1 A8       TAY             
.,BCF2 60       RTS             

                                *** convert string to float in float accu
.,BCF3 A0 00    LDY #$00        
.,BCF5 A2 0A    LDX #$0A        
.,BCF7 94 5D    STY $5D,X       
.,BCF9 CA       DEX             
.,BCFA 10 FB    BPL $BCF7       
.,BCFC 90 0F    BCC $BD0D       
.,BCFE C9 2D    CMP #$2D        minus
.,BD00 D0 04    BNE $BD06       
.,BD02 86 67    STX $67         
.,BD04 F0 04    BEQ $BD0A       
.,BD06 C9 2B    CMP #$2B        plus
.,BD08 D0 05    BNE $BD0F       
.,BD0A 20 73 00 JSR $0073       
.,BD0D 90 5B    BCC $BD6A       
.,BD0F C9 2E    CMP #$2E        decimal point
.,BD11 F0 2E    BEQ $BD41       
.,BD13 C9 45    CMP #$45        E
.,BD15 D0 30    BNE $BD47       
.,BD17 20 73 00 JSR $0073       
.,BD1A 90 17    BCC $BD33       
.,BD1C C9 AB    CMP #$AB        minus code
.,BD1E F0 0E    BEQ $BD2E       
.,BD20 C9 2D    CMP #$2D        minus
.,BD22 F0 0A    BEQ $BD2E       
.,BD24 C9 AA    CMP #$AA        plus code
.,BD26 F0 08    BEQ $BD30       
.,BD28 C9 2B    CMP #$2B        plus
.,BD2A F0 04    BEQ $BD30       
.,BD2C D0 07    BNE $BD35       
.,BD2E 66 60    ROR $60         
.,BD30 20 73 00 JSR $0073       
.,BD33 90 5C    BCC $BD91       
.,BD35 24 60    BIT $60         
.,BD37 10 0E    BPL $BD47       
.,BD39 A9 00    LDA #$00        
.,BD3B 38       SEC             
.,BD3C E5 5E    SBC $5E         
.,BD3E 4C 49 BD JMP $BD49       
.,BD41 66 5F    ROR $5F         
.,BD43 24 5F    BIT $5F         
.,BD45 50 C3    BVC $BD0A       
.,BD47 A5 5E    LDA $5E         
.,BD49 38       SEC             
.,BD4A E5 5D    SBC $5D         
.,BD4C 85 5E    STA $5E         
.,BD4E F0 12    BEQ $BD62       
.,BD50 10 09    BPL $BD5B       
.,BD52 20 FE BA JSR $BAFE       
.,BD55 E6 5E    INC $5E         
.,BD57 D0 F9    BNE $BD52       
.,BD59 F0 07    BEQ $BD62       
.,BD5B 20 E2 BA JSR $BAE2       
.,BD5E C6 5E    DEC $5E         
.,BD60 D0 F9    BNE $BD5B       
.,BD62 A5 67    LDA $67         
.,BD64 30 01    BMI $BD67       
.,BD66 60       RTS             
.,BD67 4C B4 BF JMP $BFB4       
.,BD6A 48       PHA             
.,BD6B 24 5F    BIT $5F         
.,BD6D 10 02    BPL $BD71       
.,BD6F E6 5D    INC $5D         
.,BD71 20 E2 BA JSR $BAE2       
.,BD74 68       PLA             
.,BD75 38       SEC             
.,BD76 E9 30    SBC #$30        0
.,BD78 20 7E BD JSR $BD7E       
.,BD7B 4C 0A BD JMP $BD0A       

                                *** add signed integer from A to float accu
.,BD7E 48       PHA             
.,BD7F 20 0C BC JSR $BC0C       
.,BD82 68       PLA             
.,BD83 20 3C BC JSR $BC3C       
.,BD86 A5 6E    LDA $6E         
.,BD88 45 66    EOR $66         
.,BD8A 85 6F    STA $6F         
.,BD8C A6 61    LDX $61         
.,BD8E 4C 6A B8 JMP $B86A       

                                *** get exponent of number from string
.,BD91 A5 5E    LDA $5E         
.,BD93 C9 0A    CMP #$0A        
.,BD95 90 09    BCC $BDA0       
.,BD97 A9 64    LDA #$64        
.,BD99 24 60    BIT $60         
.,BD9B 30 11    BMI $BDAE       
.,BD9D 4C 7E B9 JMP $B97E       
.,BDA0 0A       ASL             
.,BDA1 0A       ASL             
.,BDA2 18       CLC             
.,BDA3 65 5E    ADC $5E         
.,BDA5 0A       ASL             
.,BDA6 18       CLC             
.,BDA7 A0 00    LDY #$00        
.,BDA9 71 7A    ADC ($7A),Y     
.,BDAB 38       SEC             
.,BDAC E9 30    SBC #$30        0
.,BDAE 85 5E    STA $5E         
.,BDB0 4C 30 BD JMP $BD30       

                                *** constants for float to string conversion
.:BDB3 9B 3E BC 1F FD           
.:BDB8 9E 6E 6B 27 FD           
.:BDBD 9E 6E 6B 28 00           

                                *** print IN followed by line number
.,BDC2 A9 71    LDA #$71        low  A371
.,BDC4 A0 A3    LDY #$A3        high A371
.,BDC6 20 DA BD JSR $BDDA       
.,BDC9 A5 3A    LDA $3A         
.,BDCB A6 39    LDX $39         

                                *** print number from AX
.,BDCD 85 62    STA $62         
.,BDCF 86 63    STX $63         
.,BDD1 A2 90    LDX #$90        
.,BDD3 38       SEC             
.,BDD4 20 49 BC JSR $BC49       
.,BDD7 20 DF BD JSR $BDDF       
.,BDDA 4C 1E AB JMP $AB1E       

                                *** convert number in float accu to string
.,BDDD A0 01    LDY #$01        
.,BDDF A9 20    LDA #$20        
.,BDE1 24 66    BIT $66         
.,BDE3 10 02    BPL $BDE7       
.,BDE5 A9 2D    LDA #$2D        minus
.,BDE7 99 FF 00 STA $00FF,Y     
.,BDEA 85 66    STA $66         
.,BDEC 84 71    STY $71         
.,BDEE C8       INY             
.,BDEF A9 30    LDA #$30        0
.,BDF1 A6 61    LDX $61         
.,BDF3 D0 03    BNE $BDF8       
.,BDF5 4C 04 BF JMP $BF04       
.,BDF8 A9 00    LDA #$00        
.,BDFA E0 80    CPX #$80        
.,BDFC F0 02    BEQ $BE00       
.,BDFE B0 09    BCS $BE09       
.,BE00 A9 BD    LDA #$BD        low  BDBD
.,BE02 A0 BD    LDY #$BD        high BDBD
.,BE04 20 28 BA JSR $BA28       
.,BE07 A9 F7    LDA #$F7        
.,BE09 85 5D    STA $5D         
.,BE0B A9 B8    LDA #$B8        low  BDB8
.,BE0D A0 BD    LDY #$BD        high BDB8
.,BE0F 20 5B BC JSR $BC5B       
.,BE12 F0 1E    BEQ $BE32       
.,BE14 10 12    BPL $BE28       
.,BE16 A9 B3    LDA #$B3        low  BDB3
.,BE18 A0 BD    LDY #$BD        high BDB3
.,BE1A 20 5B BC JSR $BC5B       
.,BE1D F0 02    BEQ $BE21       
.,BE1F 10 0E    BPL $BE2F       
.,BE21 20 E2 BA JSR $BAE2       
.,BE24 C6 5D    DEC $5D         
.,BE26 D0 EE    BNE $BE16       
.,BE28 20 FE BA JSR $BAFE       
.,BE2B E6 5D    INC $5D         
.,BE2D D0 DC    BNE $BE0B       
.,BE2F 20 49 B8 JSR $B849       
.,BE32 20 9B BC JSR $BC9B       
.,BE35 A2 01    LDX #$01        
.,BE37 A5 5D    LDA $5D         
.,BE39 18       CLC             
.,BE3A 69 0A    ADC #$0A        
.,BE3C 30 09    BMI $BE47       
.,BE3E C9 0B    CMP #$0B        
.,BE40 B0 06    BCS $BE48       
.,BE42 69 FF    ADC #$FF        
.,BE44 AA       TAX             
.,BE45 A9 02    LDA #$02        
.,BE47 38       SEC             
.,BE48 E9 02    SBC #$02        
.,BE4A 85 5E    STA $5E         
.,BE4C 86 5D    STX $5D         
.,BE4E 8A       TXA             
.,BE4F F0 02    BEQ $BE53       
.,BE51 10 13    BPL $BE66       
.,BE53 A4 71    LDY $71         
.,BE55 A9 2E    LDA #$2E        decimal point
.,BE57 C8       INY             
.,BE58 99 FF 00 STA $00FF,Y     
.,BE5B 8A       TXA             
.,BE5C F0 06    BEQ $BE64       
.,BE5E A9 30    LDA #$30        0
.,BE60 C8       INY             
.,BE61 99 FF 00 STA $00FF,Y     
.,BE64 84 71    STY $71         
.,BE66 A0 00    LDY #$00        
.,BE68 A2 80    LDX #$80        
.,BE6A A5 65    LDA $65         
.,BE6C 18       CLC             
.,BE6D 79 19 BF ADC $BF19,Y     
.,BE70 85 65    STA $65         
.,BE72 A5 64    LDA $64         
.,BE74 79 18 BF ADC $BF18,Y     
.,BE77 85 64    STA $64         
.,BE79 A5 63    LDA $63         
.,BE7B 79 17 BF ADC $BF17,Y     
.,BE7E 85 63    STA $63         
.,BE80 A5 62    LDA $62         
.,BE82 79 16 BF ADC $BF16,Y     
.,BE85 85 62    STA $62         
.,BE87 E8       INX             
.,BE88 B0 04    BCS $BE8E       
.,BE8A 10 DE    BPL $BE6A       
.,BE8C 30 02    BMI $BE90       
.,BE8E 30 DA    BMI $BE6A       
.,BE90 8A       TXA             
.,BE91 90 04    BCC $BE97       
.,BE93 49 FF    EOR #$FF        
.,BE95 69 0A    ADC #$0A        
.,BE97 69 2F    ADC #$2F        
.,BE99 C8       INY             
.,BE9A C8       INY             
.,BE9B C8       INY             
.,BE9C C8       INY             
.,BE9D 84 47    STY $47         
.,BE9F A4 71    LDY $71         
.,BEA1 C8       INY             
.,BEA2 AA       TAX             
.,BEA3 29 7F    AND #$7F        
.,BEA5 99 FF 00 STA $00FF,Y     
.,BEA8 C6 5D    DEC $5D         
.,BEAA D0 06    BNE $BEB2       
.,BEAC A9 2E    LDA #$2E        
.,BEAE C8       INY             
.,BEAF 99 FF 00 STA $00FF,Y     
.,BEB2 84 71    STY $71         
.,BEB4 A4 47    LDY $47         
.,BEB6 8A       TXA             
.,BEB7 49 FF    EOR #$FF        
.,BEB9 29 80    AND #$80        
.,BEBB AA       TAX             
.,BEBC C0 24    CPY #$24        
.,BEBE F0 04    BEQ $BEC4       
.,BEC0 C0 3C    CPY #$3C        
.,BEC2 D0 A6    BNE $BE6A       
.,BEC4 A4 71    LDY $71         
.,BEC6 B9 FF 00 LDA $00FF,Y     
.,BEC9 88       DEY             
.,BECA C9 30    CMP #$30        0
.,BECC F0 F8    BEQ $BEC6       
.,BECE C9 2E    CMP #$2E        decimal point
.,BED0 F0 01    BEQ $BED3       
.,BED2 C8       INY             
.,BED3 A9 2B    LDA #$2B        plus
.,BED5 A6 5E    LDX $5E         
.,BED7 F0 2E    BEQ $BF07       
.,BED9 10 08    BPL $BEE3       
.,BEDB A9 00    LDA #$00        
.,BEDD 38       SEC             
.,BEDE E5 5E    SBC $5E         
.,BEE0 AA       TAX             
.,BEE1 A9 2D    LDA #$2D        minus
.,BEE3 99 01 01 STA $0101,Y     
.,BEE6 A9 45    LDA #$45        
.,BEE8 99 00 01 STA $0100,Y     
.,BEEB 8A       TXA             
.,BEEC A2 2F    LDX #$2F        
.,BEEE 38       SEC             
.,BEEF E8       INX             
.,BEF0 E9 0A    SBC #$0A        
.,BEF2 B0 FB    BCS $BEEF       
.,BEF4 69 3A    ADC #$3A        
.,BEF6 99 03 01 STA $0103,Y     
.,BEF9 8A       TXA             
.,BEFA 99 02 01 STA $0102,Y     
.,BEFD A9 00    LDA #$00        
.,BEFF 99 04 01 STA $0104,Y     
.,BF02 F0 08    BEQ $BF0C       
.,BF04 99 FF 00 STA $00FF,Y     
.,BF07 A9 00    LDA #$00        
.,BF09 99 00 01 STA $0100,Y     
.,BF0C A9 00    LDA #$00        low  0100
.,BF0E A0 01    LDY #$01        high 0100
.,BF10 60       RTS             

                                *** 0.5
.:BF11 80 00                    

                                *** divisors for decimal conversion
.:BF16 FA 0A 1F 00              
.:BF1A 00 98 96 80              
.:BF1E FF F0 BD C0              
.:BF22 00 01 86 A0              
.:BF26 FF FF D8 F0              
.:BF2A 00 00 03 E8              
.:BF2E FF FF FF 9C              
.:BF32 00 00 00 0A              
.:BF36 FF FF FF FF              

                                *** divisors for time conversion
.:BF3A FF DF 0A 80              
.:BF3E 00 03 4B C0              
.:BF42 FF FF 73 60              
.:BF46 00 00 0E 10              
.:BF4A FF FF FD A8              
.:BF4E 00 00 00 3C              

                                *** unused
                                is this some version id?
.:BF52 EC                       

                                *** unused
.:BF53 AA AA AA AA AA           
.:BF58 AA AA AA AA AA AA AA AA  
.:BF60 AA AA AA AA AA AA AA AA  
.:BF68 AA AA AA AA AA AA AA AA  
.:BF70 AA                       

                                *** SQR function
.,BF71 20 0C BC JSR $BC0C       
.,BF74 A9 11    LDA #$11        
.,BF76 A0 BF    LDY #$BF        
.,BF78 20 A2 BB JSR $BBA2       

                                *** power operator
.,BF7B F0 70    BEQ $BFED       
.,BF7D A5 69    LDA $69         
.,BF7F D0 03    BNE $BF84       
.,BF81 4C F9 B8 JMP $B8F9       
.,BF84 A2 4E    LDX #$4E        low  004E
.,BF86 A0 00    LDY #$00        high 004E
.,BF88 20 D4 BB JSR $BBD4       
.,BF8B A5 6E    LDA $6E         
.,BF8D 10 0F    BPL $BF9E       
.,BF8F 20 CC BC JSR $BCCC       
.,BF92 A9 4E    LDA #$4E        low  004E
.,BF94 A0 00    LDY #$00        high 004E
.,BF96 20 5B BC JSR $BC5B       
.,BF99 D0 03    BNE $BF9E       
.,BF9B 98       TYA             
.,BF9C A4 07    LDY $07         
.,BF9E 20 FE BB JSR $BBFE       
.,BFA1 98       TYA             
.,BFA2 48       PHA             
.,BFA3 20 EA B9 JSR $B9EA       
.,BFA6 A9 4E    LDA #$4E        low  004E
.,BFA8 A0 00    LDY #$00        high 004E
.,BFAA 20 28 BA JSR $BA28       
.,BFAD 20 ED BF JSR $BFED       
.,BFB0 68       PLA             
.,BFB1 4A       LSR             
.,BFB2 90 0A    BCC $BFBE       

                                *** minus operator
.,BFB4 A5 61    LDA $61         
.,BFB6 F0 06    BEQ $BFBE       
.,BFB8 A5 66    LDA $66         
.,BFBA 49 FF    EOR #$FF        
.,BFBC 85 66    STA $66         
.,BFBE 60       RTS             

                                *** floating point constands for EXP
                                1/LOG(2)
.:BFBF 81 38 AA 3B 29           

                                *** EXP polynomial table
.:BFC4 07                       degree 8
.:BFC5 71 34 58 3E 56           
.:BFCA 74 16 7E B3 1B           
.:BFCF 77 2F EE E3 85           
.:BFD4 7A 1D 84 1C 2A           
.:BFD9 7C 63 59 58 0A           
.:BFDE 7E 75 FD E7 C6           
.:BFE3 80 31 72 18 10           
.:BFE8 81 00 00 00 00           

                                *** EXP command
.,BFED A9 BF    LDA #$BF        
.,BFEF A0 BF    LDY #$BF        
.,BFF1 20 28 BA JSR $BA28       
.,BFF4 A5 70    LDA $70         
.,BFF6 69 50    ADC #$50        
.,BFF8 90 03    BCC $BFFD       
.,BFFA 20 23 BC JSR $BC23       
.,BFFD 4C 00 E0 JMP $E000       

                                *** continuation of EXP function
.,E000 85 56    STA $56         
.,E002 20 0F BC JSR $BC0F       
.,E005 A5 61    LDA $61         
.,E007 C9 88    CMP #$88        
.,E009 90 03    BCC $E00E       
.,E00B 20 D4 BA JSR $BAD4       
.,E00E 20 CC BC JSR $BCCC       
.,E011 A5 07    LDA $07         
.,E013 18       CLC             
.,E014 69 81    ADC #$81        
.,E016 F0 F3    BEQ $E00B       
.,E018 38       SEC             
.,E019 E9 01    SBC #$01        
.,E01B 48       PHA             
.,E01C A2 05    LDX #$05        
.,E01E B5 69    LDA $69,X       
.,E020 B4 61    LDY $61,X       
.,E022 95 61    STA $61,X       
.,E024 94 69    STY $69,X       
.,E026 CA       DEX             
.,E027 10 F5    BPL $E01E       
.,E029 A5 56    LDA $56         
.,E02B 85 70    STA $70         
.,E02D 20 53 B8 JSR $B853       
.,E030 20 B4 BF JSR $BFB4       
.,E033 A9 C4    LDA #$C4        
.,E035 A0 BF    LDY #$BF        
.,E037 20 59 E0 JSR $E059       
.,E03A A9 00    LDA #$00        
.,E03C 85 6F    STA $6F         
.,E03E 68       PLA             
.,E03F 20 B9 BA JSR $BAB9       
.,E042 60       RTS             

                                *** compute odd degrees for SIN and ATN
.,E043 85 71    STA $71         
.,E045 84 72    STY $72         
.,E047 20 CA BB JSR $BBCA       
.,E04A A9 57    LDA #$57        
.,E04C 20 28 BA JSR $BA28       
.,E04F 20 5D E0 JSR $E05D       
.,E052 A9 57    LDA #$57        
.,E054 A0 00    LDY #$00        
.,E056 4C 28 BA JMP $BA28       

                                *** compute polynomials according to table indexed by AY
.,E059 85 71    STA $71         
.,E05B 84 72    STY $72         
.,E05D 20 C7 BB JSR $BBC7       
.,E060 B1 71    LDA ($71),Y     
.,E062 85 67    STA $67         
.,E064 A4 71    LDY $71         
.,E066 C8       INY             
.,E067 98       TYA             
.,E068 D0 02    BNE $E06C       
.,E06A E6 72    INC $72         
.,E06C 85 71    STA $71         
.,E06E A4 72    LDY $72         
.,E070 20 28 BA JSR $BA28       
.,E073 A5 71    LDA $71         
.,E075 A4 72    LDY $72         
.,E077 18       CLC             
.,E078 69 05    ADC #$05        
.,E07A 90 01    BCC $E07D       
.,E07C C8       INY             
.,E07D 85 71    STA $71         
.,E07F 84 72    STY $72         
.,E081 20 67 B8 JSR $B867       
.,E084 A9 5C    LDA #$5C        
.,E086 A0 00    LDY #$00        
.,E088 C6 67    DEC $67         
.,E08A D0 E4    BNE $E070       
.,E08C 60       RTS             

                                *** float numbers for RND
.:E08D 98 35 44 7A 00           
.:E092 68 28 B1 46 00           

                                *** RND function
.,E097 20 2B BC JSR $BC2B       
.,E09A 30 37    BMI $E0D3       
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
.,E0BE A9 8B    LDA #$8B        
.,E0C0 A0 00    LDY #$00        
.,E0C2 20 A2 BB JSR $BBA2       
.,E0C5 A9 8D    LDA #$8D        
.,E0C7 A0 E0    LDY #$E0        
.,E0C9 20 28 BA JSR $BA28       
.,E0CC A9 92    LDA #$92        
.,E0CE A0 E0    LDY #$E0        
.,E0D0 20 67 B8 JSR $B867       
.,E0D3 A6 65    LDX $65         
.,E0D5 A5 62    LDA $62         
.,E0D7 85 65    STA $65         
.,E0D9 86 62    STX $62         
.,E0DB A6 63    LDX $63         
.,E0DD A5 64    LDA $64         
.,E0DF 85 63    STA $63         
.,E0E1 86 64    STX $64         
.,E0E3 A9 00    LDA #$00        
.,E0E5 85 66    STA $66         
.,E0E7 A5 61    LDA $61         
.,E0E9 85 70    STA $70         
.,E0EB A9 80    LDA #$80        
.,E0ED 85 61    STA $61         
.,E0EF 20 D7 B8 JSR $B8D7       
.,E0F2 A2 8B    LDX #$8B        
.,E0F4 A0 00    LDY #$00        
.,E0F6 4C D4 BB JMP $BBD4       

                                *** handle errors for direct I/O
                                calls from basic
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

                                *** SYS command
.,E12A 20 8A AD JSR $AD8A       
.,E12D 20 F7 B7 JSR $B7F7       
.,E130 A9 E1    LDA #$E1        low  E146
.,E132 48       PHA             
.,E133 A9 46    LDA #$46        high E146
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

                                *** SAVE command
.,E156 20 D4 E1 JSR $E1D4       
.,E159 A6 2D    LDX $2D         
.,E15B A4 2E    LDY $2E         
.,E15D A9 2B    LDA #$2B        
.,E15F 20 D8 FF JSR $FFD8       
.,E162 B0 95    BCS $E0F9       
.,E164 60       RTS             

                                *** VERIFY command
.,E165 A9 01    LDA #$01        
.:E167 2C       .BYTE $2C       

                                *** LOAD command
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

                                *** OPEN command
.,E1BE 20 19 E2 JSR $E219       
.,E1C1 20 C0 FF JSR $FFC0       
.,E1C4 B0 0B    BCS $E1D1       
.,E1C6 60       RTS             

                                *** CLOSE command
.,E1C7 20 19 E2 JSR $E219       
.,E1CA A5 49    LDA $49         
.,E1CC 20 C3 FF JSR $FFC3       
.,E1CF 90 C3    BCC $E194       
.,E1D1 4C F9 E0 JMP $E0F9       

                                *** set parameters for load/verify/save
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

                                *** skip comma and get integer in X
.,E200 20 0E E2 JSR $E20E       
.,E203 4C 9E B7 JMP $B79E       

                                *** get character and check for end of line
.,E206 20 79 00 JSR $0079       
.,E209 D0 02    BNE $E20D       
.,E20B 68       PLA             
.,E20C 68       PLA             
.,E20D 60       RTS             

                                *** check for comma and skip it
.,E20E 20 FD AE JSR $AEFD       
.,E211 20 79 00 JSR $0079       
.,E214 D0 F7    BNE $E20D       
.,E216 4C 08 AF JMP $AF08       

                                *** get open/close parameters
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

                                *** COS function
.,E264 A9 E0    LDA #$E0        low  E2E0
.,E266 A0 E2    LDY #$E2        high E2E0
.,E268 20 67 B8 JSR $B867       

                                *** SIN function
.,E26B 20 0C BC JSR $BC0C       
.,E26E A9 E5    LDA #$E5        low  E2E5
.,E270 A0 E2    LDY #$E2        high E2E5
.,E272 A6 6E    LDX $6E         
.,E274 20 07 BB JSR $BB07       
.,E277 20 0C BC JSR $BC0C       
.,E27A 20 CC BC JSR $BCCC       
.,E27D A9 00    LDA #$00        
.,E27F 85 6F    STA $6F         
.,E281 20 53 B8 JSR $B853       
.,E284 A9 EA    LDA #$EA        low  E2EA
.,E286 A0 E2    LDY #$E2        high E2EA
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
.,E2A0 A9 EA    LDA #$EA        low  E2EA
.,E2A2 A0 E2    LDY #$E2        high E2EA
.,E2A4 20 67 B8 JSR $B867       
.,E2A7 68       PLA             
.,E2A8 10 03    BPL $E2AD       
.,E2AA 20 B4 BF JSR $BFB4       
.,E2AD A9 EF    LDA #$EF        
.,E2AF A0 E2    LDY #$E2        
.,E2B1 4C 43 E0 JMP $E043       

                                *** TAN function
.,E2B4 20 CA BB JSR $BBCA       
.,E2B7 A9 00    LDA #$00        
.,E2B9 85 12    STA $12         
.,E2BB 20 6B E2 JSR $E26B       
.,E2BE A2 4E    LDX #$4E        low  004E
.,E2C0 A0 00    LDY #$00        high 004E
.,E2C2 20 F6 E0 JSR $E0F6       
.,E2C5 A9 57    LDA #$57        low  005F
.,E2C7 A0 00    LDY #$00        high 005F
.,E2C9 20 A2 BB JSR $BBA2       
.,E2CC A9 00    LDA #$00        
.,E2CE 85 66    STA $66         
.,E2D0 A5 12    LDA $12         
.,E2D2 20 DC E2 JSR $E2DC       
.,E2D5 A9 4E    LDA #$4E        low  004E
.,E2D7 A0 00    LDY #$00        high 004E
.,E2D9 4C 0F BB JMP $BB0F       
.,E2DC 48       PHA             
.,E2DD 4C 9D E2 JMP $E29D       

                                *** float numbers for SIN, COS and TAN
                                0.5 * PI
.:E2E0 81 49 0F DA A2           

                                *** 2 * PI
.:E2E5 83 49 0F DA A2           

                                *** 0,25
.:E2EA 7F 00 00 00 00           

                                *** polynomial table
.:E2EF 05                       degree 6
.:E2F0 84 E6 1A 2D 1B           
.:E2F5 86 28 07 FB F8           
.:E2FA 87 99 68 89 01           
.:E2FF 87 23 35 DF E1           
.:E304 86 A5 5D E7 28           
.:E309 83 49 0F DA A2           

                                *** ATN function
.,E30E A5 66    LDA $66         
.,E310 48       PHA             
.,E311 10 03    BPL $E316       
.,E313 20 B4 BF JSR $BFB4       
.,E316 A5 61    LDA $61         
.,E318 48       PHA             
.,E319 C9 81    CMP #$81        
.,E31B 90 07    BCC $E324       
.,E31D A9 BC    LDA #$BC        low  B9BC
.,E31F A0 B9    LDY #$B9        high B9BC
.,E321 20 0F BB JSR $BB0F       
.,E324 A9 3E    LDA #$3E        low  E33E
.,E326 A0 E3    LDY #$E3        high E33E
.,E328 20 43 E0 JSR $E043       
.,E32B 68       PLA             
.,E32C C9 81    CMP #$81        
.,E32E 90 07    BCC $E337       
.,E330 A9 E0    LDA #$E0        low  E2E0
.,E332 A0 E2    LDY #$E2        high E2E0
.,E334 20 50 B8 JSR $B850       
.,E337 68       PLA             
.,E338 10 03    BPL $E33D       
.,E33A 4C B4 BF JMP $BFB4       
.,E33D 60       RTS             

                                *** float numbers for ATN
                                polynomial table
.:E33E 0B                       degree 12
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

                                *** warm start entry
.,E37B 20 CC FF JSR $FFCC       
.,E37E A9 00    LDA #$00        
.,E380 85 13    STA $13         
.,E382 20 7A A6 JSR $A67A       
.,E385 58       CLI             
.,E386 A2 80    LDX #$80        
.,E388 6C 00 03 JMP ($0300)     normally E38B

                                *** handle error messages
.,E38B 8A       TXA             
.,E38C 30 03    BMI $E391       
.,E38E 4C 3A A4 JMP $A43A       
.,E391 4C 74 A4 JMP $A474       

                                *** RESET routine
.,E394 20 53 E4 JSR $E453       
.,E397 20 BF E3 JSR $E3BF       
.,E39A 20 22 E4 JSR $E422       
.,E39D A2 FB    LDX #$FB        
.,E39F 9A       TXS             
.,E3A0 D0 E4    BNE $E386       

                                *** character fetch code for zero page $0073-$008F
.,E3A2 E6 7A    INC $7A         
.,E3A4 D0 02    BNE $E3A8       
.,E3A6 E6 7B    INC $7B         
.,E3A8 AD 60 EA LDA $EA60       
.,E3AB C9 3A    CMP #$3A        colon
.,E3AD B0 0A    BCS $E3B9       
.,E3AF C9 20    CMP #$20        space
.,E3B1 F0 EF    BEQ $E3A2       
.,E3B3 38       SEC             
.,E3B4 E9 30    SBC #$30        0
.,E3B6 38       SEC             
.,E3B7 E9 D0    SBC #$D0        
.,E3B9 60       RTS             

                                *** first RND seed value
.:E3BA 80 4F C7 52 58           

                                *** initialisation of basic
.,E3BF A9 4C    LDA #$4C        
.,E3C1 85 54    STA $54         
.,E3C3 8D 10 03 STA $0310       
.,E3C6 A9 48    LDA #$48        low  B248
.,E3C8 A0 B2    LDY #$B2        high B248
.,E3CA 8D 11 03 STA $0311       
.,E3CD 8C 12 03 STY $0312       
.,E3D0 A9 91    LDA #$91        lowh B391
.,E3D2 A0 B3    LDY #$B3        high B391
.,E3D4 85 05    STA $05         
.,E3D6 84 06    STY $06         
.,E3D8 A9 AA    LDA #$AA        low  B1AA
.,E3DA A0 B1    LDY #$B1        high B1AA
.,E3DC 85 03    STA $03         
.,E3DE 84 04    STY $04         
.,E3E0 A2 1C    LDX #$1C        
.,E3E2 BD A2 E3 LDA $E3A2,X     
.,E3E5 95 73    STA $73,X       
.,E3E7 CA       DEX             
.,E3E8 10 F8    BPL $E3E2       
.,E3EA A9 03    LDA #$03        
.,E3EC 85 53    STA $53         
.,E3EE A9 00    LDA #$00        
.,E3F0 85 68    STA $68         
.,E3F2 85 13    STA $13         
.,E3F4 85 18    STA $18         
.,E3F6 A2 01    LDX #$01        
.,E3F8 8E FD 01 STX $01FD       
.,E3FB 8E FC 01 STX $01FC       
.,E3FE A2 19    LDX #$19        
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

                                *** print BASIC start up messages
.,E422 A5 2B    LDA $2B         
.,E424 A4 2C    LDY $2C         
.,E426 20 08 A4 JSR $A408       
.,E429 A9 73    LDA #$73        low  E473
.,E42B A0 E4    LDY #$E4        high E473
.,E42D 20 1E AB JSR $AB1E       
.,E430 A5 37    LDA $37         
.,E432 38       SEC             
.,E433 E5 2B    SBC $2B         
.,E435 AA       TAX             
.,E436 A5 38    LDA $38         
.,E438 E5 2C    SBC $2C         
.,E43A 20 CD BD JSR $BDCD       
.,E43D A9 60    LDA #$60        low  E460
.,E43F A0 E4    LDY #$E4        high E460
.,E441 20 1E AB JSR $AB1E       
.,E444 4C 44 A6 JMP $A644       

                                *** vectors for $0300-$030B
.:E447 8B E3                    
.:E449 83 A4                    
.:E44B 7C A5                    
.:E44D 1A A7                    
.:E44F E4 A7                    
.:E451 86 AE                    

                                *** initialise vectors
.,E453 A2 0B    LDX #$0B        
.,E455 BD 47 E4 LDA $E447,X     
.,E458 9D 00 03 STA $0300,X     
.,E45B CA       DEX             
.,E45C 10 F7    BPL $E455       
.,E45E 60       RTS             

                                *** startup messages
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

                                *** set output device
.,E4AD 48       PHA             
.,E4AE 20 C9 FF JSR $FFC9       
.,E4B1 AA       TAX             
.,E4B2 68       PLA             
.,E4B3 90 01    BCC $E4B6       
.,E4B5 8A       TXA             
.,E4B6 60       RTS             

                                *** unused
.:E4B7 AA AA AA AA AA AA AA AA  
.:E4BF AA AA AA AA AA AA AA AA  
.:E4C7 AA AA AA AA AA AA AA AA  
.:E4CF AA AA AA AA AA           
.,E4D3 85 A9    STA $A9         
.,E4D5 A9 01    LDA #$01        
.,E4D7 85 AB    STA $AB         
.,E4D9 60       RTS             

                                *** clear byte in color ram
.,E4DA AD 21 D0 LDA $D021       
.,E4DD 91 F3    STA ($F3),Y     
.,E4DF 60       RTS             

                                *** pause after finding a file on casette
.,E4E0 69 02    ADC #$02        
.,E4E2 A4 91    LDY $91         
.,E4E4 C8       INY             
.,E4E5 D0 04    BNE $E4EB       
.,E4E7 C5 A1    CMP $A1         
.,E4E9 D0 F7    BNE $E4E2       
.,E4EB 60       RTS             

                                *** baud rate factor table
.:E4EC 19 26                    50
.:E4EE 44 19                    75
.:E4F0 1A 11                    110
.:E4F2 E8 0D                    134.5
.:E4F4 70 0C                    150
.:E4F6 06 06                    300
.:E4F8 D1 02                    600
.:E4FA 37 01                    1200
.:E4FC AE 00                    1800
.:E4FE 69 00                    2400

                                *** read base address of I/O device into XY
.,E500 A2 00    LDX #$00        low  DC00
.,E502 A0 DC    LDY #$DC        high DC00
.,E504 60       RTS             

                                *** read screen size
.,E505 A2 28    LDX #$28        40 columns
.,E507 A0 19    LDY #$19        25 rows
.,E509 60       RTS             

                                *** read/set XY cursor position
.,E50A B0 07    BCS $E513       
.,E50C 86 D6    STX $D6         
.,E50E 84 D3    STY $D3         
.,E510 20 6C E5 JSR $E56C       
.,E513 A6 D6    LDX $D6         
.,E515 A4 D3    LDY $D3         
.,E517 60       RTS             

                                *** initialise screen and keyboard
.,E518 20 A0 E5 JSR $E5A0       
.,E51B A9 00    LDA #$00        
.,E51D 8D 91 02 STA $0291       
.,E520 85 CF    STA $CF         
.,E522 A9 48    LDA #$48        low  EB48
.,E524 8D 8F 02 STA $028F       
.,E527 A9 EB    LDA #$EB        high EB48
.,E529 8D 90 02 STA $0290       
.,E52C A9 0A    LDA #$0A        
.,E52E 8D 89 02 STA $0289       
.,E531 8D 8C 02 STA $028C       
.,E534 A9 0E    LDA #$0E        
.,E536 8D 86 02 STA $0286       
.,E539 A9 04    LDA #$04        
.,E53B 8D 8B 02 STA $028B       
.,E53E A9 0C    LDA #$0C        
.,E540 85 CD    STA $CD         
.,E542 85 CC    STA $CC         
.,E544 AD 88 02 LDA $0288       
.,E547 09 80    ORA #$80        
.,E549 A8       TAY             
.,E54A A9 00    LDA #$00        
.,E54C AA       TAX             
.,E54D 94 D9    STY $D9,X       
.,E54F 18       CLC             
.,E550 69 28    ADC #$28        
.,E552 90 01    BCC $E555       
.,E554 C8       INY             
.,E555 E8       INX             
.,E556 E0 1A    CPX #$1A        
.,E558 D0 F3    BNE $E54D       
.,E55A A9 FF    LDA #$FF        
.,E55C 95 D9    STA $D9,X       
.,E55E A2 18    LDX #$18        
.,E560 20 FF E9 JSR $E9FF       
.,E563 CA       DEX             
.,E564 10 FA    BPL $E560       
.,E566 A0 00    LDY #$00        
.,E568 84 D3    STY $D3         
.,E56A 84 D6    STY $D6         

                                *** set address of curent screen line
.,E56C A6 D6    LDX $D6         
.,E56E A5 D3    LDA $D3         
.,E570 B4 D9    LDY $D9,X       
.,E572 30 08    BMI $E57C       
.,E574 18       CLC             
.,E575 69 28    ADC #$28        
.,E577 85 D3    STA $D3         
.,E579 CA       DEX             
.,E57A 10 F4    BPL $E570       
.,E57C 20 F0 E9 JSR $E9F0       
.,E57F A9 27    LDA #$27        
.,E581 E8       INX             
.,E582 B4 D9    LDY $D9,X       
.,E584 30 06    BMI $E58C       
.,E586 18       CLC             
.,E587 69 28    ADC #$28        
.,E589 E8       INX             
.,E58A 10 F6    BPL $E582       
.,E58C 85 D5    STA $D5         
.,E58E 4C 24 EA JMP $EA24       
.,E591 E4 C9    CPX $C9         
.,E593 F0 03    BEQ $E598       
.,E595 4C ED E6 JMP $E6ED       
.,E598 60       RTS             
.,E599 EA       NOP             

                                *** this code is unused by kernel
                                since no other part of the
                                rom jumps to this location!
.,E59A 20 A0 E5 JSR $E5A0       
.,E59D 4C 66 E5 JMP $E566       

                                *** initialise vic chip
.,E5A0 A9 03    LDA #$03        
.,E5A2 85 9A    STA $9A         
.,E5A4 A9 00    LDA #$00        
.,E5A6 85 99    STA $99         
.,E5A8 A2 2F    LDX #$2F        
.,E5AA BD B8 EC LDA $ECB8,X     
.,E5AD 9D FF CF STA $CFFF,X     
.,E5B0 CA       DEX             
.,E5B1 D0 F7    BNE $E5AA       
.,E5B3 60       RTS             

                                *** get character from keyboard buffer
.,E5B4 AC 77 02 LDY $0277       
.,E5B7 A2 00    LDX #$00        
.,E5B9 BD 78 02 LDA $0278,X     
.,E5BC 9D 77 02 STA $0277,X     
.,E5BF E8       INX             
.,E5C0 E4 C6    CPX $C6         
.,E5C2 D0 F5    BNE $E5B9       
.,E5C4 C6 C6    DEC $C6         
.,E5C6 98       TYA             
.,E5C7 58       CLI             
.,E5C8 18       CLC             
.,E5C9 60       RTS             

                                *** wait for return for keyboard
.,E5CA 20 16 E7 JSR $E716       
.,E5CD A5 C6    LDA $C6         
.,E5CF 85 CC    STA $CC         
.,E5D1 8D 92 02 STA $0292       
.,E5D4 F0 F7    BEQ $E5CD       
.,E5D6 78       SEI             
.,E5D7 A5 CF    LDA $CF         
.,E5D9 F0 0C    BEQ $E5E7       
.,E5DB A5 CE    LDA $CE         
.,E5DD AE 87 02 LDX $0287       
.,E5E0 A0 00    LDY #$00        
.,E5E2 84 CF    STY $CF         
.,E5E4 20 13 EA JSR $EA13       
.,E5E7 20 B4 E5 JSR $E5B4       
.,E5EA C9 83    CMP #$83        
.,E5EC D0 10    BNE $E5FE       
.,E5EE A2 09    LDX #$09        
.,E5F0 78       SEI             
.,E5F1 86 C6    STX $C6         
.,E5F3 BD E6 EC LDA $ECE6,X     
.,E5F6 9D 76 02 STA $0276,X     
.,E5F9 CA       DEX             
.,E5FA D0 F7    BNE $E5F3       
.,E5FC F0 CF    BEQ $E5CD       
.,E5FE C9 0D    CMP #$0D        
.,E600 D0 C8    BNE $E5CA       
.,E602 A4 D5    LDY $D5         
.,E604 84 D0    STY $D0         
.,E606 B1 D1    LDA ($D1),Y     
.,E608 C9 20    CMP #$20        
.,E60A D0 03    BNE $E60F       
.,E60C 88       DEY             
.,E60D D0 F7    BNE $E606       
.,E60F C8       INY             
.,E610 84 C8    STY $C8         
.,E612 A0 00    LDY #$00        
.,E614 8C 92 02 STY $0292       
.,E617 84 D3    STY $D3         
.,E619 84 D4    STY $D4         
.,E61B A5 C9    LDA $C9         
.,E61D 30 1B    BMI $E63A       
.,E61F A6 D6    LDX $D6         
.,E621 20 ED E6 JSR $E6ED       
.,E624 E4 C9    CPX $C9         
.,E626 D0 12    BNE $E63A       
.,E628 A5 CA    LDA $CA         
.,E62A 85 D3    STA $D3         
.,E62C C5 C8    CMP $C8         
.,E62E 90 0A    BCC $E63A       
.,E630 B0 2B    BCS $E65D       

                                *** get character from device 0 or 3
.,E632 98       TYA             
.,E633 48       PHA             
.,E634 8A       TXA             
.,E635 48       PHA             
.,E636 A5 D0    LDA $D0         
.,E638 F0 93    BEQ $E5CD       

                                *** get character from current screen line
.,E63A A4 D3    LDY $D3         
.,E63C B1 D1    LDA ($D1),Y     
.,E63E 85 D7    STA $D7         
.,E640 29 3F    AND #$3F        
.,E642 06 D7    ASL $D7         
.,E644 24 D7    BIT $D7         
.,E646 10 02    BPL $E64A       
.,E648 09 80    ORA #$80        
.,E64A 90 04    BCC $E650       
.,E64C A6 D4    LDX $D4         
.,E64E D0 04    BNE $E654       
.,E650 70 02    BVS $E654       
.,E652 09 40    ORA #$40        
.,E654 E6 D3    INC $D3         
.,E656 20 84 E6 JSR $E684       
.,E659 C4 C8    CPY $C8         
.,E65B D0 17    BNE $E674       
.,E65D A9 00    LDA #$00        
.,E65F 85 D0    STA $D0         
.,E661 A9 0D    LDA #$0D        
.,E663 A6 99    LDX $99         
.,E665 E0 03    CPX #$03        
.,E667 F0 06    BEQ $E66F       
.,E669 A6 9A    LDX $9A         
.,E66B E0 03    CPX #$03        
.,E66D F0 03    BEQ $E672       
.,E66F 20 16 E7 JSR $E716       
.,E672 A9 0D    LDA #$0D        
.,E674 85 D7    STA $D7         
.,E676 68       PLA             
.,E677 AA       TAX             
.,E678 68       PLA             
.,E679 A8       TAY             
.,E67A A5 D7    LDA $D7         
.,E67C C9 DE    CMP #$DE        screen PI code
.,E67E D0 02    BNE $E682       
.,E680 A9 FF    LDA #$FF        petscii PI code
.,E682 18       CLC             
.,E683 60       RTS             

                                *** check for quote mark and set flag
.,E684 C9 22    CMP #$22        quote mark
.,E686 D0 08    BNE $E690       
.,E688 A5 D4    LDA $D4         
.,E68A 49 01    EOR #$01        
.,E68C 85 D4    STA $D4         
.,E68E A9 22    LDA #$22        quote mark
.,E690 60       RTS             

                                *** fill screen at current position
.,E691 09 40    ORA #$40        
.,E693 A6 C7    LDX $C7         
.,E695 F0 02    BEQ $E699       
.,E697 09 80    ORA #$80        
.,E699 A6 D8    LDX $D8         
.,E69B F0 02    BEQ $E69F       
.,E69D C6 D8    DEC $D8         
.,E69F AE 86 02 LDX $0286       
.,E6A2 20 13 EA JSR $EA13       
.,E6A5 20 B6 E6 JSR $E6B6       

                                *** return from output to the screen
.,E6A8 68       PLA             
.,E6A9 A8       TAY             
.,E6AA A5 D8    LDA $D8         
.,E6AC F0 02    BEQ $E6B0       
.,E6AE 46 D4    LSR $D4         
.,E6B0 68       PLA             
.,E6B1 AA       TAX             
.,E6B2 68       PLA             
.,E6B3 18       CLC             
.,E6B4 58       CLI             
.,E6B5 60       RTS             

                                *** get/insert new line
.,E6B6 20 B3 E8 JSR $E8B3       
.,E6B9 E6 D3    INC $D3         
.,E6BB A5 D5    LDA $D5         
.,E6BD C5 D3    CMP $D3         
.,E6BF B0 3F    BCS $E700       
.,E6C1 C9 4F    CMP #$4F        
.,E6C3 F0 32    BEQ $E6F7       
.,E6C5 AD 92 02 LDA $0292       
.,E6C8 F0 03    BEQ $E6CD       
.,E6CA 4C 67 E9 JMP $E967       
.,E6CD A6 D6    LDX $D6         
.,E6CF E0 19    CPX #$19        
.,E6D1 90 07    BCC $E6DA       
.,E6D3 20 EA E8 JSR $E8EA       
.,E6D6 C6 D6    DEC $D6         
.,E6D8 A6 D6    LDX $D6         
.,E6DA 16 D9    ASL $D9,X       
.,E6DC 56 D9    LSR $D9,X       
.,E6DE E8       INX             
.,E6DF B5 D9    LDA $D9,X       
.,E6E1 09 80    ORA #$80        
.,E6E3 95 D9    STA $D9,X       
.,E6E5 CA       DEX             
.,E6E6 A5 D5    LDA $D5         
.,E6E8 18       CLC             
.,E6E9 69 28    ADC #$28        
.,E6EB 85 D5    STA $D5         
.,E6ED B5 D9    LDA $D9,X       
.,E6EF 30 03    BMI $E6F4       
.,E6F1 CA       DEX             
.,E6F2 D0 F9    BNE $E6ED       
.,E6F4 4C F0 E9 JMP $E9F0       
.,E6F7 C6 D6    DEC $D6         
.,E6F9 20 7C E8 JSR $E87C       
.,E6FC A9 00    LDA #$00        
.,E6FE 85 D3    STA $D3         
.,E700 60       RTS             

                                *** move backwards over a line boundary
.,E701 A6 D6    LDX $D6         
.,E703 D0 06    BNE $E70B       
.,E705 86 D3    STX $D3         
.,E707 68       PLA             
.,E708 68       PLA             
.,E709 D0 9D    BNE $E6A8       
.,E70B CA       DEX             
.,E70C 86 D6    STX $D6         
.,E70E 20 6C E5 JSR $E56C       
.,E711 A4 D5    LDY $D5         
.,E713 84 D3    STY $D3         
.,E715 60       RTS             

                                *** put a character to screen
.,E716 48       PHA             
.,E717 85 D7    STA $D7         
.,E719 8A       TXA             
.,E71A 48       PHA             
.,E71B 98       TYA             
.,E71C 48       PHA             
.,E71D A9 00    LDA #$00        
.,E71F 85 D0    STA $D0         
.,E721 A4 D3    LDY $D3         
.,E723 A5 D7    LDA $D7         
.,E725 10 03    BPL $E72A       
.,E727 4C D4 E7 JMP $E7D4       
.,E72A C9 0D    CMP #$0D        return code
.,E72C D0 03    BNE $E731       
.,E72E 4C 91 E8 JMP $E891       
.,E731 C9 20    CMP #$20        
.,E733 90 10    BCC $E745       
.,E735 C9 60    CMP #$60        
.,E737 90 04    BCC $E73D       
.,E739 29 DF    AND #$DF        
.,E73B D0 02    BNE $E73F       
.,E73D 29 3F    AND #$3F        
.,E73F 20 84 E6 JSR $E684       
.,E742 4C 93 E6 JMP $E693       
.,E745 A6 D8    LDX $D8         
.,E747 F0 03    BEQ $E74C       
.,E749 4C 97 E6 JMP $E697       
.,E74C C9 14    CMP #$14        delete code
.,E74E D0 2E    BNE $E77E       
.,E750 98       TYA             
.,E751 D0 06    BNE $E759       
.,E753 20 01 E7 JSR $E701       
.,E756 4C 73 E7 JMP $E773       
.,E759 20 A1 E8 JSR $E8A1       
.,E75C 88       DEY             
.,E75D 84 D3    STY $D3         
.,E75F 20 24 EA JSR $EA24       
.,E762 C8       INY             
.,E763 B1 D1    LDA ($D1),Y     
.,E765 88       DEY             
.,E766 91 D1    STA ($D1),Y     
.,E768 C8       INY             
.,E769 B1 F3    LDA ($F3),Y     
.,E76B 88       DEY             
.,E76C 91 F3    STA ($F3),Y     
.,E76E C8       INY             
.,E76F C4 D5    CPY $D5         
.,E771 D0 EF    BNE $E762       
.,E773 A9 20    LDA #$20        space
.,E775 91 D1    STA ($D1),Y     
.,E777 AD 86 02 LDA $0286       
.,E77A 91 F3    STA ($F3),Y     
.,E77C 10 4D    BPL $E7CB       
.,E77E A6 D4    LDX $D4         
.,E780 F0 03    BEQ $E785       
.,E782 4C 97 E6 JMP $E697       
.,E785 C9 12    CMP #$12        reverse code
.,E787 D0 02    BNE $E78B       
.,E789 85 C7    STA $C7         
.,E78B C9 13    CMP #$13        home code
.,E78D D0 03    BNE $E792       
.,E78F 20 66 E5 JSR $E566       
.,E792 C9 1D    CMP #$1D        csr right
.,E794 D0 17    BNE $E7AD       
.,E796 C8       INY             
.,E797 20 B3 E8 JSR $E8B3       
.,E79A 84 D3    STY $D3         
.,E79C 88       DEY             
.,E79D C4 D5    CPY $D5         
.,E79F 90 09    BCC $E7AA       
.,E7A1 C6 D6    DEC $D6         
.,E7A3 20 7C E8 JSR $E87C       
.,E7A6 A0 00    LDY #$00        
.,E7A8 84 D3    STY $D3         
.,E7AA 4C A8 E6 JMP $E6A8       
.,E7AD C9 11    CMP #$11        csr down
.,E7AF D0 1D    BNE $E7CE       
.,E7B1 18       CLC             
.,E7B2 98       TYA             
.,E7B3 69 28    ADC #$28        
.,E7B5 A8       TAY             
.,E7B6 E6 D6    INC $D6         
.,E7B8 C5 D5    CMP $D5         
.,E7BA 90 EC    BCC $E7A8       
.,E7BC F0 EA    BEQ $E7A8       
.,E7BE C6 D6    DEC $D6         
.,E7C0 E9 28    SBC #$28        
.,E7C2 90 04    BCC $E7C8       
.,E7C4 85 D3    STA $D3         
.,E7C6 D0 F8    BNE $E7C0       
.,E7C8 20 7C E8 JSR $E87C       
.,E7CB 4C A8 E6 JMP $E6A8       
.,E7CE 20 CB E8 JSR $E8CB       
.,E7D1 4C 44 EC JMP $EC44       

                                *** put shifted chars to screen
.,E7D4 29 7F    AND #$7F        remove shift bit
.,E7D6 C9 7F    CMP #$7F        code for PI
.,E7D8 D0 02    BNE $E7DC       
.,E7DA A9 5E    LDA #$5E        screen PI
.,E7DC C9 20    CMP #$20        
.,E7DE 90 03    BCC $E7E3       
.,E7E0 4C 91 E6 JMP $E691       
.,E7E3 C9 0D    CMP #$0D        shift return
.,E7E5 D0 03    BNE $E7EA       
.,E7E7 4C 91 E8 JMP $E891       
.,E7EA A6 D4    LDX $D4         
.,E7EC D0 3F    BNE $E82D       
.,E7EE C9 14    CMP #$14        insert
.,E7F0 D0 37    BNE $E829       
.,E7F2 A4 D5    LDY $D5         
.,E7F4 B1 D1    LDA ($D1),Y     
.,E7F6 C9 20    CMP #$20        
.,E7F8 D0 04    BNE $E7FE       
.,E7FA C4 D3    CPY $D3         
.,E7FC D0 07    BNE $E805       
.,E7FE C0 4F    CPY #$4F        
.,E800 F0 24    BEQ $E826       
.,E802 20 65 E9 JSR $E965       
.,E805 A4 D5    LDY $D5         
.,E807 20 24 EA JSR $EA24       
.,E80A 88       DEY             
.,E80B B1 D1    LDA ($D1),Y     
.,E80D C8       INY             
.,E80E 91 D1    STA ($D1),Y     
.,E810 88       DEY             
.,E811 B1 F3    LDA ($F3),Y     
.,E813 C8       INY             
.,E814 91 F3    STA ($F3),Y     
.,E816 88       DEY             
.,E817 C4 D3    CPY $D3         
.,E819 D0 EF    BNE $E80A       
.,E81B A9 20    LDA #$20        
.,E81D 91 D1    STA ($D1),Y     
.,E81F AD 86 02 LDA $0286       
.,E822 91 F3    STA ($F3),Y     
.,E824 E6 D8    INC $D8         
.,E826 4C A8 E6 JMP $E6A8       
.,E829 A6 D8    LDX $D8         
.,E82B F0 05    BEQ $E832       
.,E82D 09 40    ORA #$40        
.,E82F 4C 97 E6 JMP $E697       
.,E832 C9 11    CMP #$11        csr up
.,E834 D0 16    BNE $E84C       
.,E836 A6 D6    LDX $D6         
.,E838 F0 37    BEQ $E871       
.,E83A C6 D6    DEC $D6         
.,E83C A5 D3    LDA $D3         
.,E83E 38       SEC             
.,E83F E9 28    SBC #$28        
.,E841 90 04    BCC $E847       
.,E843 85 D3    STA $D3         
.,E845 10 2A    BPL $E871       
.,E847 20 6C E5 JSR $E56C       
.,E84A D0 25    BNE $E871       
.,E84C C9 12    CMP #$12        reverse off
.,E84E D0 04    BNE $E854       
.,E850 A9 00    LDA #$00        
.,E852 85 C7    STA $C7         
.,E854 C9 1D    CMP #$1D        csr left
.,E856 D0 12    BNE $E86A       
.,E858 98       TYA             
.,E859 F0 09    BEQ $E864       
.,E85B 20 A1 E8 JSR $E8A1       
.,E85E 88       DEY             
.,E85F 84 D3    STY $D3         
.,E861 4C A8 E6 JMP $E6A8       
.,E864 20 01 E7 JSR $E701       
.,E867 4C A8 E6 JMP $E6A8       
.,E86A C9 13    CMP #$13        clr code
.,E86C D0 06    BNE $E874       
.,E86E 20 44 E5 JSR $E544       
.,E871 4C A8 E6 JMP $E6A8       
.,E874 09 80    ORA #$80        
.,E876 20 CB E8 JSR $E8CB       
.,E879 4C 4F EC JMP $EC4F       

                                *** set next line number
.,E87C 46 C9    LSR $C9         
.,E87E A6 D6    LDX $D6         
.,E880 E8       INX             
.,E881 E0 19    CPX #$19        
.,E883 D0 03    BNE $E888       
.,E885 20 EA E8 JSR $E8EA       
.,E888 B5 D9    LDA $D9,X       
.,E88A 10 F4    BPL $E880       
.,E88C 86 D6    STX $D6         
.,E88E 4C 6C E5 JMP $E56C       

                                *** action for return
.,E891 A2 00    LDX #$00        
.,E893 86 D8    STX $D8         
.,E895 86 C7    STX $C7         
.,E897 86 D4    STX $D4         
.,E899 86 D3    STX $D3         
.,E89B 20 7C E8 JSR $E87C       
.,E89E 4C A8 E6 JMP $E6A8       

                                *** move cursor to previous line if
                                at start of line
.,E8A1 A2 02    LDX #$02        
.,E8A3 A9 00    LDA #$00        
.,E8A5 C5 D3    CMP $D3         
.,E8A7 F0 07    BEQ $E8B0       
.,E8A9 18       CLC             
.,E8AA 69 28    ADC #$28        
.,E8AC CA       DEX             
.,E8AD D0 F6    BNE $E8A5       
.,E8AF 60       RTS             
.,E8B0 C6 D6    DEC $D6         
.,E8B2 60       RTS             

                                *** move cursor to next line if
                                at end of line
.,E8B3 A2 02    LDX #$02        
.,E8B5 A9 27    LDA #$27        
.,E8B7 C5 D3    CMP $D3         
.,E8B9 F0 07    BEQ $E8C2       
.,E8BB 18       CLC             
.,E8BC 69 28    ADC #$28        
.,E8BE CA       DEX             
.,E8BF D0 F6    BNE $E8B7       
.,E8C1 60       RTS             
.,E8C2 A6 D6    LDX $D6         
.,E8C4 E0 19    CPX #$19        
.,E8C6 F0 02    BEQ $E8CA       
.,E8C8 E6 D6    INC $D6         
.,E8CA 60       RTS             

                                *** check for colour change codes
.,E8CB A2 0F    LDX #$0F        
.,E8CD DD DA E8 CMP $E8DA,X     
.,E8D0 F0 04    BEQ $E8D6       
.,E8D2 CA       DEX             
.,E8D3 10 F8    BPL $E8CD       
.,E8D5 60       RTS             
.,E8D6 8E 86 02 STX $0286       
.,E8D9 60       RTS             

                                *** colour key codes
.:E8DA 90                       
.:E8E2 81                       

                                *** scroll screen
.,E8EA A5 AC    LDA $AC         
.,E8EC 48       PHA             
.,E8ED A5 AD    LDA $AD         
.,E8EF 48       PHA             
.,E8F0 A5 AE    LDA $AE         
.,E8F2 48       PHA             
.,E8F3 A5 AF    LDA $AF         
.,E8F5 48       PHA             
.,E8F6 A2 FF    LDX #$FF        
.,E8F8 C6 D6    DEC $D6         
.,E8FA C6 C9    DEC $C9         
.,E8FC CE A5 02 DEC $02A5       
.,E8FF E8       INX             
.,E900 20 F0 E9 JSR $E9F0       
.,E903 E0 18    CPX #$18        
.,E905 B0 0C    BCS $E913       
.,E907 BD F1 EC LDA $ECF1,X     
.,E90A 85 AC    STA $AC         
.,E90C B5 DA    LDA $DA,X       
.,E90E 20 C8 E9 JSR $E9C8       
.,E911 30 EC    BMI $E8FF       
.,E913 20 FF E9 JSR $E9FF       
.,E916 A2 00    LDX #$00        
.,E918 B5 D9    LDA $D9,X       
.,E91A 29 7F    AND #$7F        
.,E91C B4 DA    LDY $DA,X       
.,E91E 10 02    BPL $E922       
.,E920 09 80    ORA #$80        
.,E922 95 D9    STA $D9,X       
.,E924 E8       INX             
.,E925 E0 18    CPX #$18        
.,E927 D0 EF    BNE $E918       
.,E929 A5 F1    LDA $F1         
.,E92B 09 80    ORA #$80        
.,E92D 85 F1    STA $F1         
.,E92F A5 D9    LDA $D9         
.,E931 10 C3    BPL $E8F6       
.,E933 E6 D6    INC $D6         
.,E935 EE A5 02 INC $02A5       
.,E938 A9 7F    LDA #$7F        
.,E93A 8D 00 DC STA $DC00       
.,E93D AD 01 DC LDA $DC01       
.,E940 C9 FB    CMP #$FB        
.,E942 08       PHP             
.,E943 A9 7F    LDA #$7F        
.,E945 8D 00 DC STA $DC00       
.,E948 28       PLP             
.,E949 D0 0B    BNE $E956       
.,E94B A0 00    LDY #$00        
.,E94D EA       NOP             
.,E94E CA       DEX             
.,E94F D0 FC    BNE $E94D       
.,E951 88       DEY             
.,E952 D0 F9    BNE $E94D       
.,E954 84 C6    STY $C6         
.,E956 A6 D6    LDX $D6         
.,E958 68       PLA             
.,E959 85 AF    STA $AF         
.,E95B 68       PLA             
.,E95C 85 AE    STA $AE         
.,E95E 68       PLA             
.,E95F 85 AD    STA $AD         
.,E961 68       PLA             
.,E962 85 AC    STA $AC         
.,E964 60       RTS             

                                *** insert blank line in screen
.,E965 A6 D6    LDX $D6         
.,E967 E8       INX             
.,E968 B5 D9    LDA $D9,X       
.,E96A 10 FB    BPL $E967       
.,E96C 8E A5 02 STX $02A5       
.,E96F E0 18    CPX #$18        
.,E971 F0 0E    BEQ $E981       
.,E973 90 0C    BCC $E981       
.,E975 20 EA E8 JSR $E8EA       
.,E978 AE A5 02 LDX $02A5       
.,E97B CA       DEX             
.,E97C C6 D6    DEC $D6         
.,E97E 4C DA E6 JMP $E6DA       
.,E981 A5 AC    LDA $AC         
.,E983 48       PHA             
.,E984 A5 AD    LDA $AD         
.,E986 48       PHA             
.,E987 A5 AE    LDA $AE         
.,E989 48       PHA             
.,E98A A5 AF    LDA $AF         
.,E98C 48       PHA             
.,E98D A2 19    LDX #$19        
.,E98F CA       DEX             
.,E990 20 F0 E9 JSR $E9F0       
.,E993 EC A5 02 CPX $02A5       
.,E996 90 0E    BCC $E9A6       
.,E998 F0 0C    BEQ $E9A6       
.,E99A BD EF EC LDA $ECEF,X     
.,E99D 85 AC    STA $AC         
.,E99F B5 D8    LDA $D8,X       
.,E9A1 20 C8 E9 JSR $E9C8       
.,E9A4 30 E9    BMI $E98F       
.,E9A6 20 FF E9 JSR $E9FF       
.,E9A9 A2 17    LDX #$17        
.,E9AB EC A5 02 CPX $02A5       
.,E9AE 90 0F    BCC $E9BF       
.,E9B0 B5 DA    LDA $DA,X       
.,E9B2 29 7F    AND #$7F        
.,E9B4 B4 D9    LDY $D9,X       
.,E9B6 10 02    BPL $E9BA       
.,E9B8 09 80    ORA #$80        
.,E9BA 95 DA    STA $DA,X       
.,E9BC CA       DEX             
.,E9BD D0 EC    BNE $E9AB       
.,E9BF AE A5 02 LDX $02A5       
.,E9C2 20 DA E6 JSR $E6DA       
.,E9C5 4C 58 E9 JMP $E958       

                                *** move one screen line
.,E9C8 29 03    AND #$03        
.,E9CA 0D 88 02 ORA $0288       
.,E9CD 85 AD    STA $AD         
.,E9CF 20 E0 E9 JSR $E9E0       
.,E9D2 A0 27    LDY #$27        
.,E9D4 B1 AC    LDA ($AC),Y     
.,E9D6 91 D1    STA ($D1),Y     
.,E9D8 B1 AE    LDA ($AE),Y     
.,E9DA 91 F3    STA ($F3),Y     
.,E9DC 88       DEY             
.,E9DD 10 F5    BPL $E9D4       
.,E9DF 60       RTS             

                                *** set colour and screen addresses
.,E9E0 20 24 EA JSR $EA24       
.,E9E3 A5 AC    LDA $AC         
.,E9E5 85 AE    STA $AE         
.,E9E7 A5 AD    LDA $AD         
.,E9E9 29 03    AND #$03        
.,E9EB 09 D8    ORA #$D8        
.,E9ED 85 AF    STA $AF         
.,E9EF 60       RTS             

                                *** fetch screen addresses
.,E9F0 BD F0 EC LDA $ECF0,X     
.,E9F3 85 D1    STA $D1         
.,E9F5 B5 D9    LDA $D9,X       
.,E9F7 29 03    AND #$03        
.,E9F9 0D 88 02 ORA $0288       
.,E9FC 85 D2    STA $D2         
.,E9FE 60       RTS             

                                *** clear one screen line
.,E9FF A0 27    LDY #$27        
.,EA01 20 F0 E9 JSR $E9F0       
.,EA04 20 24 EA JSR $EA24       
.,EA07 20 DA E4 JSR $E4DA       
.,EA0A A9 20    LDA #$20        
.,EA0C 91 D1    STA ($D1),Y     
.,EA0E 88       DEY             
.,EA0F 10 F6    BPL $EA07       
.,EA11 60       RTS             
.,EA12 EA       NOP             

                                *** set cursor flash timing and colour memory addresses
.,EA13 A8       TAY             
.,EA14 A9 02    LDA #$02set the 
.,EA16 85 CD    STA $CD         
.,EA18 20 24 EA JSR $EA24       
.,EA1B 98       TYA             

                                *** put a char on the screen
.,EA1C A4 D3    LDY $D3         
.,EA1E 91 D1    STA ($D1),Y     
.,EA20 8A       TXA             
.,EA21 91 F3    STA ($F3),Y     
.,EA23 60       RTS             

                                *** set colour memory adress parallel to screen
.,EA24 A5 D1    LDA $D1         
.,EA26 85 F3    STA $F3         
.,EA28 A5 D2    LDA $D2         
.,EA2A 29 03    AND #$03        
.,EA2C 09 D8    ORA #$D8        
.,EA2E 85 F4    STA $F4         
.,EA30 60       RTS             

                                *** normal IRQ interrupt
.,EA31 20 EA FF JSR $FFEA       do clock
.,EA34 A5 CC    LDA $CC         flash cursor
.,EA36 D0 29    BNE $EA61       
.,EA38 C6 CD    DEC $CD         
.,EA3A D0 25    BNE $EA61       
.,EA3C A9 14    LDA #$14        
.,EA3E 85 CD    STA $CD         
.,EA40 A4 D3    LDY $D3         
.,EA42 46 CF    LSR $CF         
.,EA44 AE 87 02 LDX $0287       
.,EA47 B1 D1    LDA ($D1),Y     
.,EA49 B0 11    BCS $EA5C       
.,EA4B E6 CF    INC $CF         
.,EA4D 85 CE    STA $CE         
.,EA4F 20 24 EA JSR $EA24       
.,EA52 B1 F3    LDA ($F3),Y     
.,EA54 8D 87 02 STA $0287       
.,EA57 AE 86 02 LDX $0286       
.,EA5A A5 CE    LDA $CE         
.,EA5C 49 80    EOR #$80        
.,EA5E 20 1C EA JSR $EA1C       display cursor
.,EA61 A5 01    LDA $01         checl cassette sense
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
.,EA7E AD 0D DC LDA $DC0D       
.,EA81 68       PLA             
.,EA82 A8       TAY             
.,EA83 68       PLA             
.,EA84 AA       TAX             
.,EA85 68       PLA             
.,EA86 40       RTI             

                                *** scan keyboard
.,EA87 A9 00    LDA #$00        
.,EA89 8D 8D 02 STA $028D       
.,EA8C A0 40    LDY #$40        
.,EA8E 84 CB    STY $CB         
.,EA90 8D 00 DC STA $DC00       
.,EA93 AE 01 DC LDX $DC01       
.,EA96 E0 FF    CPX #$FF        
.,EA98 F0 61    BEQ $EAFB       
.,EA9A A8       TAY             
.,EA9B A9 81    LDA #$81        
.,EA9D 85 F5    STA $F5         
.,EA9F A9 EB    LDA #$EB        
.,EAA1 85 F6    STA $F6         
.,EAA3 A9 FE    LDA #$FE        
.,EAA5 8D 00 DC STA $DC00       
.,EAA8 A2 08    LDX #$08        
.,EAAA 48       PHA             
.,EAAB AD 01 DC LDA $DC01       
.,EAAE CD 01 DC CMP $DC01       
.,EAB1 D0 F8    BNE $EAAB       
.,EAB3 4A       LSR             
.,EAB4 B0 16    BCS $EACC       
.,EAB6 48       PHA             
.,EAB7 B1 F5    LDA ($F5),Y     
.,EAB9 C9 05    CMP #$05        
.,EABB B0 0C    BCS $EAC9       
.,EABD C9 03    CMP #$03        
.,EABF F0 08    BEQ $EAC9       
.,EAC1 0D 8D 02 ORA $028D       
.,EAC4 8D 8D 02 STA $028D       
.,EAC7 10 02    BPL $EACB       
.,EAC9 84 CB    STY $CB         
.,EACB 68       PLA             
.,EACC C8       INY             
.,EACD C0 41    CPY #$41        
.,EACF B0 0B    BCS $EADC       
.,EAD1 CA       DEX             
.,EAD2 D0 DF    BNE $EAB3       
.,EAD4 38       SEC             
.,EAD5 68       PLA             
.,EAD6 2A       ROL             
.,EAD7 8D 00 DC STA $DC00       
.,EADA D0 CC    BNE $EAA8       
.,EADC 68       PLA             
.,EADD 6C 8F 02 JMP ($028F)     
.,EAE0 A4 CB    LDY $CB         
.,EAE2 B1 F5    LDA ($F5),Y     
.,EAE4 AA       TAX             
.,EAE5 C4 C5    CPY $C5         
.,EAE7 F0 07    BEQ $EAF0       
.,EAE9 A0 10    LDY #$10        
.,EAEB 8C 8C 02 STY $028C       
.,EAEE D0 36    BNE $EB26       
.,EAF0 29 7F    AND #$7F        
.,EAF2 2C 8A 02 BIT $028A       
.,EAF5 30 16    BMI $EB0D       
.,EAF7 70 49    BVS $EB42       
.,EAF9 C9 7F    CMP #$7F        
.,EAFB F0 29    BEQ $EB26       
.,EAFD C9 14    CMP #$14        delete
.,EAFF F0 0C    BEQ $EB0D       
.,EB01 C9 20    CMP #$20        space
.,EB03 F0 08    BEQ $EB0D       
.,EB05 C9 1D    CMP #$1D        csr right/left
.,EB07 F0 04    BEQ $EB0D       
.,EB09 C9 11    CMP #$11        csr up/down
.,EB0B D0 35    BNE $EB42       
.,EB0D AC 8C 02 LDY $028C       
.,EB10 F0 05    BEQ $EB17       
.,EB12 CE 8C 02 DEC $028C       
.,EB15 D0 2B    BNE $EB42       
.,EB17 CE 8B 02 DEC $028B       
.,EB1A D0 26    BNE $EB42       
.,EB1C A0 04    LDY #$04        
.,EB1E 8C 8B 02 STY $028B       
.,EB21 A4 C6    LDY $C6         
.,EB23 88       DEY             
.,EB24 10 1C    BPL $EB42       
.,EB26 A4 CB    LDY $CB         
.,EB28 84 C5    STY $C5         
.,EB2A AC 8D 02 LDY $028D       
.,EB2D 8C 8E 02 STY $028E       
.,EB30 E0 FF    CPX #$FF        
.,EB32 F0 0E    BEQ $EB42       
.,EB34 8A       TXA             
.,EB35 A6 C6    LDX $C6         
.,EB37 EC 89 02 CPX $0289       
.,EB3A B0 06    BCS $EB42       
.,EB3C 9D 77 02 STA $0277,X     
.,EB3F E8       INX             
.,EB40 86 C6    STX $C6         
.,EB42 A9 7F    LDA #$7F        
.,EB44 8D 00 DC STA $DC00       
.,EB47 60       RTS             
.,EB48 AD 8D 02 LDA $028D       
.,EB4B C9 03    CMP #$03        
.,EB4D D0 15    BNE $EB64       
.,EB4F CD 8E 02 CMP $028E       
.,EB52 F0 EE    BEQ $EB42       
.,EB54 AD 91 02 LDA $0291       
.,EB57 30 1D    BMI $EB76       
.,EB59 AD 18 D0 LDA $D018       
.,EB5C 49 02    EOR #$02        
.,EB5E 8D 18 D0 STA $D018       
.,EB61 4C 76 EB JMP $EB76       

                                *** select keyboard table
.,EB64 0A       ASL             
.,EB65 C9 08    CMP #$08        
.,EB67 90 02    BCC $EB6B       
.,EB69 A9 06    LDA #$06        
.,EB6B AA       TAX             
.,EB6C BD 79 EB LDA $EB79,X     
.,EB6F 85 F5    STA $F5         
.,EB71 BD 7A EB LDA $EB7A,X     
.,EB74 85 F6    STA $F6         
.,EB76 4C E0 EA JMP $EAE0       

                                *** table addresses
.:EB79 81 EB                    standard
.:EB7B C2 EB                    shift
.:EB7D 03 EC                    commodore key
.:EB7F 78 EC                    control

                                *** standard keyboard table
.:EB81 14 0D 1D 88 85 86 87 11  
.:EB89 33 57 41 34 5A 53 45 01  
.:EB91 35 52 44 36 43 46 54 58  
.:EB99 37 59 47 38 42 48 55 56  
.:EBA1 39 49 4A 30 4D 4B 4F 4E  
.:EBA9 2B 50 4C 2D 2E 3A 40 2C  
.:EBB1 5C 2A 3B 13 01 3D 5E 2F  
.:EBB9 31 5F 04 32 20 02 51 03  
.:EBC1 FF                       

                                *** shift keyboard table
.:EBC2 94 8D 9D 8C 89 8A 8B 91  
.:EBCA 23 D7 C1 24 DA D3 C5 01  
.:EBD2 25 D2 C4 26 C3 C6 D4 D8  
.:EBDA 27 D9 C7 28 C2 C8 D5 D6  
.:EBE2 29 C9 CA 30 CD CB CF CE  
.:EBEA DB D0 CC DD 3E 5B BA 3C  
.:EBF2 A9 C0 5D 93 01 3D DE 3F  
.:EBFA 21 5F 04 22 A0 02 D1 83  
.:EC02 FF                       

                                *** commodore key keyboard table
.:EC03 94 8D 9D 8C 89 8A 8B 91  
.:EC0B 96 B3 B0 97 AD AE B1 01  
.:EC13 98 B2 AC 99 BC BB A3 BD  
.:EC1B 9A B7 A5 9B BF B4 B8 BE  
.:EC23 29 A2 B5 30 A7 A1 B9 AA  
.:EC2B A6 AF B6 DC 3E 5B A4 3C  
.:EC33 A8 DF 5D 93 01 3D DE 3F  
.:EC3B 81 5F 04 95 A0 02 AB 83  
.:EC43 FF                       

                                *** check for special petscii codes
.,EC44 C9 0E    CMP #$0E        
.,EC46 D0 07    BNE $EC4F       
.,EC48 AD 18 D0 LDA $D018       
.,EC4B 09 02    ORA #$02        
.,EC4D D0 09    BNE $EC58       
.,EC4F C9 8E    CMP #$8E        
.,EC51 D0 0B    BNE $EC5E       
.,EC53 AD 18 D0 LDA $D018       
.,EC56 29 FD    AND #$FD        
.,EC58 8D 18 D0 STA $D018       
.,EC5B 4C A8 E6 JMP $E6A8       

                                *** shift + commodore key check
.,EC5E C9 08    CMP #$08        
.,EC60 D0 07    BNE $EC69       
.,EC62 A9 80    LDA #$80        
.,EC64 0D 91 02 ORA $0291       
.,EC67 30 09    BMI $EC72       
.,EC69 C9 09    CMP #$09        
.,EC6B D0 EE    BNE $EC5B       
.,EC6D A9 7F    LDA #$7F        
.,EC6F 2D 91 02 AND $0291       
.,EC72 8D 91 02 STA $0291       
.,EC75 4C A8 E6 JMP $E6A8       

                                *** control keyboard table
.:EC78 FF FF FF FF FF FF FF FF  
.:EC80 1C 17 01 9F 1A 13 05 FF  
.:EC88 9C 12 04 1E 03 06 14 18  
.:EC90 1F 19 07 9E 02 08 15 16  
.:EC98 12 09 0A 92 0D 0B 0F 0E  
.:ECA0 FF 10 0C FF FF 1B 00 FF  
.:ECA8 1C FF 1D FF FF 1F 1E FF  
.:ECB0 90 06 FF 05 FF FF 11 FF  
.:ECB8 FF                       

                                *** default values for VIC chip
.:ECB9 00 00                    sprite 1 x,y
.:ECBB 00 00                    sprite 2 x,y
.:ECBD 00 00                    sprite 3 x,y
.:ECBF 00 00                    sprite 4 x,y
.:ECC1 00 00                    sprite 5 x,y
.:ECC3 00 00                    sprite 6 x,y
.:ECC5 00 00                    sprite 7 x,y
.:ECC7 00 00                    sprite 8 x,y
.:ECC9 00                       
.:ECCA 9B                       
.:ECCB 37                       
.:ECCC 00                       
.:ECCD 00                       
.:ECCE 00                       
.:ECCF 08                       
.:ECD0 00                       sprite Y expand
.:ECD1 14                       
.:ECD2 0F                       
.:ECD3 00                       
.:ECD4 00                       
.:ECD5 00                       sprite multi-colour
.:ECD6 00                       sprite X expand
.:ECD7 00                       
.:ECD8 00                       
.:ECD9 0E                       boarder colour
.:ECDA 06                       background colour
.:ECDB 01                       
.:ECDC 02                       
.:ECDD 03                       
.:ECDE 04                       
.:ECDF 00                       sprite colour
.:ECE0 01                       sprite colour
.:ECE1 02                       sprite colour
.:ECE2 03                       sprite colour
.:ECE3 04                       sprite colour
.:ECE4 05                       sprite colour
.:ECE5 06                       sprite colour
.:ECE6 07                       sprite colour

                                *** load
.:ECE7 4C 4F 41 44 0D

                                *** run
.:ECEC 52 55 4E 0D

                                *** low bytes of screen line addresses
.:ECF0 00 28 50 78 A0 C8 F0 18  
.:ECF8 40 68 90 B8 E0 08 30 58  
.:ED00 80 A8 D0 F8 20 48 70 98  
.:ED08 C0                       

                                *** send talk on serial bus
.,ED09 09 40    ORA #$40        
.:ED0B 2C       .BYTE $2C       

                                *** send listen on serial bus
.,ED0C 09 20    ORA #$20        
.,ED0E 20 A4 F0 JSR $F0A4       
.,ED11 48       PHA             
.,ED12 24 94    BIT $94         
.,ED14 10 0A    BPL $ED20       
.,ED16 38       SEC             
.,ED17 66 A3    ROR $A3         
.,ED19 20 40 ED JSR $ED40       
.,ED1C 46 94    LSR $94         
.,ED1E 46 A3    LSR $A3         
.,ED20 68       PLA             
.,ED21 85 95    STA $95         
.,ED23 78       SEI             
.,ED24 20 97 EE JSR $EE97       
.,ED27 C9 3F    CMP #$3F        
.,ED29 D0 03    BNE $ED2E       
.,ED2B 20 85 EE JSR $EE85       
.,ED2E AD 00 DD LDA $DD00       
.,ED31 09 08    ORA #$08        
.,ED33 8D 00 DD STA $DD00       
.,ED36 78       SEI             
.,ED37 20 8E EE JSR $EE8E       
.,ED3A 20 97 EE JSR $EE97       
.,ED3D 20 B3 EE JSR $EEB3       

                                *** send byte from $95 on serial bus
.,ED40 78       SEI             
.,ED41 20 97 EE JSR $EE97       
.,ED44 20 A9 EE JSR $EEA9       
.,ED47 B0 64    BCS $EDAD       
.,ED49 20 85 EE JSR $EE85       
.,ED4C 24 A3    BIT $A3         
.,ED4E 10 0A    BPL $ED5A       
.,ED50 20 A9 EE JSR $EEA9       
.,ED53 90 FB    BCC $ED50       
.,ED55 20 A9 EE JSR $EEA9       
.,ED58 B0 FB    BCS $ED55       
.,ED5A 20 A9 EE JSR $EEA9       
.,ED5D 90 FB    BCC $ED5A       
.,ED5F 20 8E EE JSR $EE8E       
.,ED62 A9 08    LDA #$08        
.,ED64 85 A5    STA $A5         
.,ED66 AD 00 DD LDA $DD00       
.,ED69 CD 00 DD CMP $DD00       
.,ED6C D0 F8    BNE $ED66       
.,ED6E 0A       ASL             
.,ED6F 90 3F    BCC $EDB0       
.,ED71 66 95    ROR $95         
.,ED73 B0 05    BCS $ED7A       
.,ED75 20 A0 EE JSR $EEA0       
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
.,ED8E C6 A5    DEC $A5         
.,ED90 D0 D4    BNE $ED66       
.,ED92 A9 04    LDA #$04        
.,ED94 8D 07 DC STA $DC07       
.,ED97 A9 19    LDA #$19        
.,ED99 8D 0F DC STA $DC0F       
.,ED9C AD 0D DC LDA $DC0D       
.,ED9F AD 0D DC LDA $DC0D       
.,EDA2 29 02    AND #$02        
.,EDA4 D0 0A    BNE $EDB0       
.,EDA6 20 A9 EE JSR $EEA9       
.,EDA9 B0 F4    BCS $ED9F       
.,EDAB 58       CLI             
.,EDAC 60       RTS             
.,EDAD A9 80    LDA #$80        
.:EDAF 2C       .BYTE $2C       
.,EDB0 A9 03    LDA #$03        
.,EDB2 20 1C FE JSR $FE1C       
.,EDB5 58       CLI             
.,EDB6 18       CLC             
.,EDB7 90 4A    BCC $EE03       

                                *** send secondary address (listen) on serial bus
.,EDB9 85 95    STA $95         
.,EDBB 20 36 ED JSR $ED36       
.,EDBE AD 00 DD LDA $DD00       
.,EDC1 29 F7    AND #$F7        
.,EDC3 8D 00 DD STA $DD00       
.,EDC6 60       RTS             

                                *** send secondary address (talk) on serial bus
.,EDC7 85 95    STA $95         
.,EDC9 20 36 ED JSR $ED36       
.,EDCC 78       SEI             
.,EDCD 20 A0 EE JSR $EEA0       
.,EDD0 20 BE ED JSR $EDBE       
.,EDD3 20 85 EE JSR $EE85       
.,EDD6 20 A9 EE JSR $EEA9       
.,EDD9 30 FB    BMI $EDD6       
.,EDDB 58       CLI             
.,EDDC 60       RTS             

                                *** output byte on serial bus
.,EDDD 24 94    BIT $94         
.,EDDF 30 05    BMI $EDE6       
.,EDE1 38       SEC             
.,EDE2 66 94    ROR $94         
.,EDE4 D0 05    BNE $EDEB       
.,EDE6 48       PHA             
.,EDE7 20 40 ED JSR $ED40       
.,EDEA 68       PLA             
.,EDEB 85 95    STA $95         
.,EDED 18       CLC             
.,EDEE 60       RTS             

                                *** send talk on serial bus
.,EDEF 78       SEI             
.,EDF0 20 8E EE JSR $EE8E       
.,EDF3 AD 00 DD LDA $DD00       
.,EDF6 09 08    ORA #$08        
.,EDF8 8D 00 DD STA $DD00       
.,EDFB A9 5F    LDA #$5F        
.:EDFD 2C       .BYTE $2C       

                                *** send unlisten on serial bus
.,EDFE A9 3F    LDA #$3F        
.,EE00 20 11 ED JSR $ED11       
.,EE03 20 BE ED JSR $EDBE       
.,EE06 8A       TXA             
.,EE07 A2 0A    LDX #$0A        
.,EE09 CA       DEX             
.,EE0A D0 FD    BNE $EE09       
.,EE0C AA       TAX             
.,EE0D 20 85 EE JSR $EE85       
.,EE10 4C 97 EE JMP $EE97       

                                *** input byte on serial bus
.,EE13 78       SEI             
.,EE14 A9 00    LDA #$00        
.,EE16 85 A5    STA $A5         
.,EE18 20 85 EE JSR $EE85       
.,EE1B 20 A9 EE JSR $EEA9       
.,EE1E 10 FB    BPL $EE1B       
.,EE20 A9 01    LDA #$01        
.,EE22 8D 07 DC STA $DC07       
.,EE25 A9 19    LDA #$19        
.,EE27 8D 0F DC STA $DC0F       
.,EE2A 20 97 EE JSR $EE97       
.,EE2D AD 0D DC LDA $DC0D       
.,EE30 AD 0D DC LDA $DC0D       
.,EE33 29 02    AND #$02        
.,EE35 D0 07    BNE $EE3E       
.,EE37 20 A9 EE JSR $EEA9       
.,EE3A 30 F4    BMI $EE30       
.,EE3C 10 18    BPL $EE56       
.,EE3E A5 A5    LDA $A5         
.,EE40 F0 05    BEQ $EE47       
.,EE42 A9 02    LDA #$02        
.,EE44 4C B2 ED JMP $EDB2       
.,EE47 20 A0 EE JSR $EEA0       
.,EE4A 20 85 EE JSR $EE85       
.,EE4D A9 40    LDA #$40        
.,EE4F 20 1C FE JSR $FE1C       
.,EE52 E6 A5    INC $A5         
.,EE54 D0 CA    BNE $EE20       
.,EE56 A9 08    LDA #$08        
.,EE58 85 A5    STA $A5         
.,EE5A AD 00 DD LDA $DD00       
.,EE5D CD 00 DD CMP $DD00       
.,EE60 D0 F8    BNE $EE5A       
.,EE62 0A       ASL             
.,EE63 10 F5    BPL $EE5A       
.,EE65 66 A4    ROR $A4         
.,EE67 AD 00 DD LDA $DD00       
.,EE6A CD 00 DD CMP $DD00       
.,EE6D D0 F8    BNE $EE67       
.,EE6F 0A       ASL             
.,EE70 30 F5    BMI $EE67       
.,EE72 C6 A5    DEC $A5         
.,EE74 D0 E4    BNE $EE5A       
.,EE76 20 A0 EE JSR $EEA0       
.,EE79 24 90    BIT $90         
.,EE7B 50 03    BVC $EE80       
.,EE7D 20 06 EE JSR $EE06       
.,EE80 A5 A4    LDA $A4         
.,EE82 58       CLI             
.,EE83 18       CLC             
.,EE84 60       RTS             

                                *** set serial clock line low
.,EE85 AD 00 DD LDA $DD00       
.,EE88 29 EF    AND #$EF        
.,EE8A 8D 00 DD STA $DD00       
.,EE8D 60       RTS             

                                *** set serial clock line high
.,EE8E AD 00 DD LDA $DD00       
.,EE91 09 10    ORA #$10        
.,EE93 8D 00 DD STA $DD00       
.,EE96 60       RTS             

                                *** set serial data line low
.,EE97 AD 00 DD LDA $DD00       
.,EE9A 29 DF    AND #$DF        
.,EE9C 8D 00 DD STA $DD00       
.,EE9F 60       RTS             

                                *** set serial data line high
.,EEA0 AD 00 DD LDA $DD00       
.,EEA3 09 20    ORA #$20        
.,EEA5 8D 00 DD STA $DD00       
.,EEA8 60       RTS             
.,EEA9 AD 00 DD LDA $DD00       
.,EEAC CD 00 DD CMP $DD00       
.,EEAF D0 F8    BNE $EEA9       
.,EEB1 0A       ASL             
.,EEB2 60       RTS             

                                *** delay 1 millisecond
.,EEB3 8A       TXA             
.,EEB4 A2 B8    LDX #$B8        
.,EEB6 CA       DEX             
.,EEB7 D0 FD    BNE $EEB6       
.,EEB9 AA       TAX             
.,EEBA 60       RTS             

                                *** set next bit to transmit on RS-232
.,EEBB A5 B4    LDA $B4         
.,EEBD F0 47    BEQ $EF06       
.,EEBF 30 3F    BMI $EF00       
.,EEC1 46 B6    LSR $B6         
.,EEC3 A2 00    LDX #$00        
.,EEC5 90 01    BCC $EEC8       
.,EEC7 CA       DEX             
.,EEC8 8A       TXA             
.,EEC9 45 BD    EOR $BD         
.,EECB 85 BD    STA $BD         
.,EECD C6 B4    DEC $B4         
.,EECF F0 06    BEQ $EED7       
.,EED1 8A       TXA             
.,EED2 29 04    AND #$04        
.,EED4 85 B5    STA $B5         
.,EED6 60       RTS             
.,EED7 A9 20    LDA #$20        
.,EED9 2C 94 02 BIT $0294       
.,EEDC F0 14    BEQ $EEF2       
.,EEDE 30 1C    BMI $EEFC       
.,EEE0 70 14    BVS $EEF6       
.,EEE2 A5 BD    LDA $BD         
.,EEE4 D0 01    BNE $EEE7       
.,EEE6 CA       DEX             
.,EEE7 C6 B4    DEC $B4         
.,EEE9 AD 93 02 LDA $0293       
.,EEEC 10 E3    BPL $EED1       
.,EEEE C6 B4    DEC $B4         
.,EEF0 D0 DF    BNE $EED1       
.,EEF2 E6 B4    INC $B4         
.,EEF4 D0 F0    BNE $EEE6       
.,EEF6 A5 BD    LDA $BD         
.,EEF8 F0 ED    BEQ $EEE7       
.,EEFA D0 EA    BNE $EEE6       
.,EEFC 70 E9    BVS $EEE7       
.,EEFE 50 E6    BVC $EEE6       
.,EF00 E6 B4    INC $B4         
.,EF02 A2 FF    LDX #$FF        
.,EF04 D0 CB    BNE $EED1       
.,EF06 AD 94 02 LDA $0294       
.,EF09 4A       LSR             
.,EF0A 90 07    BCC $EF13       
.,EF0C 2C 01 DD BIT $DD01       
.,EF0F 10 1D    BPL $EF2E       
.,EF11 50 1E    BVC $EF31       
.,EF13 A9 00    LDA #$00        
.,EF15 85 BD    STA $BD         
.,EF17 85 B5    STA $B5         
.,EF19 AE 98 02 LDX $0298       
.,EF1C 86 B4    STX $B4         
.,EF1E AC 9D 02 LDY $029D       
.,EF21 CC 9E 02 CPY $029E       
.,EF24 F0 13    BEQ $EF39       
.,EF26 B1 F9    LDA ($F9),Y     
.,EF28 85 B6    STA $B6         
.,EF2A EE 9D 02 INC $029D       
.,EF2D 60       RTS             

                                *** handle RS-232 errors
.,EF2E A9 40    LDA #$40        
.:EF30 2C       .BYTE $2C       
.,EF31 A9 10    LDA #$10        
.,EF33 0D 97 02 ORA $0297       
.,EF36 8D 97 02 STA $0297       
.,EF39 A9 01    LDA #$01        
.,EF3B 8D 0D DD STA $DD0D       
.,EF3E 4D A1 02 EOR $02A1       
.,EF41 09 80    ORA #$80        
.,EF43 8D A1 02 STA $02A1       
.,EF46 8D 0D DD STA $DD0D       
.,EF49 60       RTS             

                                *** check control register
.,EF4A A2 09    LDX #$09        
.,EF4C A9 20    LDA #$20        
.,EF4E 2C 93 02 BIT $0293       
.,EF51 F0 01    BEQ $EF54       
.,EF53 CA       DEX             
.,EF54 50 02    BVC $EF58       
.,EF56 CA       DEX             
.,EF57 CA       DEX             
.,EF58 60       RTS             

                                *** add bit input on RS-232 bus to word being input
.,EF59 A6 A9    LDX $A9         
.,EF5B D0 33    BNE $EF90       
.,EF5D C6 A8    DEC $A8         
.,EF5F F0 36    BEQ $EF97       
.,EF61 30 0D    BMI $EF70       
.,EF63 A5 A7    LDA $A7         
.,EF65 45 AB    EOR $AB         
.,EF67 85 AB    STA $AB         
.,EF69 46 A7    LSR $A7         
.,EF6B 66 AA    ROR $AA         
.,EF6D 60       RTS             

                                *** handle end of word for RS-232 input
.,EF6E C6 A8    DEC $A8         
.,EF70 A5 A7    LDA $A7         
.,EF72 F0 67    BEQ $EFDB       
.,EF74 AD 93 02 LDA $0293       
.,EF77 0A       ASL             
.,EF78 A9 01    LDA #$01        
.,EF7A 65 A8    ADC $A8         
.,EF7C D0 EF    BNE $EF6D       

                                *** enable byte reception
.,EF7E A9 90    LDA #$90        
.,EF80 8D 0D DD STA $DD0D       
.,EF83 0D A1 02 ORA $02A1       
.,EF86 8D A1 02 STA $02A1       
.,EF89 85 A9    STA $A9         
.,EF8B A9 02    LDA #$02        
.,EF8D 4C 3B EF JMP $EF3B       

                                *** receiver start bit test
.,EF90 A5 A7    LDA $A7         
.,EF92 D0 EA    BNE $EF7E       
.,EF94 4C D3 E4 JMP $E4D3       

                                *** put received data into RS-232 buffer
.,EF97 AC 9B 02 LDY $029B       
.,EF9A C8       INY             
.,EF9B CC 9C 02 CPY $029C       
.,EF9E F0 2A    BEQ $EFCA       
.,EFA0 8C 9B 02 STY $029B       
.,EFA3 88       DEY             
.,EFA4 A5 AA    LDA $AA         
.,EFA6 AE 98 02 LDX $0298       
.,EFA9 E0 09    CPX #$09        
.,EFAB F0 04    BEQ $EFB1       
.,EFAD 4A       LSR             
.,EFAE E8       INX             
.,EFAF D0 F8    BNE $EFA9       
.,EFB1 91 F7    STA ($F7),Y     
.,EFB3 A9 20    LDA #$20        
.,EFB5 2C 94 02 BIT $0294       
.,EFB8 F0 B4    BEQ $EF6E       
.,EFBA 30 B1    BMI $EF6D       
.,EFBC A5 A7    LDA $A7         
.,EFBE 45 AB    EOR $AB         
.,EFC0 F0 03    BEQ $EFC5       
.,EFC2 70 A9    BVS $EF6D       
.:EFC4 2C       .BYTE $2C       
.,EFC5 50 A6    BVC $EF6D       
.,EFC7 A9 01    LDA #$01        
.:EFC9 2C       .BYTE $2C       
.,EFCA A9 04    LDA #$04        
.:EFCC 2C       .BYTE $2C       
.,EFCD A9 80    LDA #$80        
.:EFCF 2C       .BYTE $2C       
.,EFD0 A9 02    LDA #$02        
.,EFD2 0D 97 02 ORA $0297       
.,EFD5 8D 97 02 STA $0297       
.,EFD8 4C 7E EF JMP $EF7E       
.,EFDB A5 AA    LDA $AA         
.,EFDD D0 F1    BNE $EFD0       
.,EFDF F0 EC    BEQ $EFCD       

                                *** output of RS-232 device
.,EFE1 85 9A    STA $9A         
.,EFE3 AD 94 02 LDA $0294       
.,EFE6 4A       LSR             
.,EFE7 90 29    BCC $F012       
.,EFE9 A9 02    LDA #$02        
.,EFEB 2C 01 DD BIT $DD01       
.,EFEE 10 1D    BPL $F00D       
.,EFF0 D0 20    BNE $F012       
.,EFF2 AD A1 02 LDA $02A1       
.,EFF5 29 02    AND #$02        
.,EFF7 D0 F9    BNE $EFF2       
.,EFF9 2C 01 DD BIT $DD01       
.,EFFC 70 FB    BVS $EFF9       
.,EFFE AD 01 DD LDA $DD01       
.,F001 09 02    ORA #$02        
.,F003 8D 01 DD STA $DD01       
.,F006 2C 01 DD BIT $DD01       
.,F009 70 07    BVS $F012       
.,F00B 30 F9    BMI $F006       
.,F00D A9 40    LDA #$40        
.,F00F 8D 97 02 STA $0297       
.,F012 18       CLC             
.,F013 60       RTS             

                                *** buffer char to output on RS-232
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

                                *** initalise RS-232 input
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

                                *** get next character from RS-232 input buffer
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

                                *** protect serial/casette routine from RS-232 NMI's
.,F0A4 48       PHA             
.,F0A5 AD A1 02 LDA $02A1       
.,F0A8 F0 11    BEQ $F0BB       
.,F0AA AD A1 02 LDA $02A1       
.,F0AD 29 03    AND #$03        
.,F0AF D0 F9    BNE $F0AA       
.,F0B1 A9 10    LDA #$10        
.,F0B3 8D 0D DD STA $DD0D       
.,F0B6 A9 00    LDA #$00        
.,F0B8 8D A1 02 STA $02A1       
.,F0BB 68       PLA             
.,F0BC 60       RTS             

                                *** kernal I/O messages
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

                                *** print kernal message indexed by Y
.,F12B 24 9D    BIT $9D         
.,F12D 10 0D    BPL $F13C       
.,F12F B9 BD F0 LDA $F0BD,Y     
.,F132 08       PHP             
.,F133 29 7F    AND #$7F        
.,F135 20 D2 FF JSR $FFD2       
.,F138 C8       INY             
.,F139 28       PLP             
.,F13A 10 F3    BPL $F12F       
.,F13C 18       CLC             
.,F13D 60       RTS             

                                *** get a character
.,F13E A5 99    LDA $99         
.,F140 D0 08    BNE $F14A       
.,F142 A5 C6    LDA $C6         
.,F144 F0 0F    BEQ $F155       
.,F146 78       SEI             
.,F147 4C B4 E5 JMP $E5B4       
.,F14A C9 02    CMP #$02        
.,F14C D0 18    BNE $F166       
.,F14E 84 97    STY $97         
.,F150 20 86 F0 JSR $F086       
.,F153 A4 97    LDY $97         
.,F155 18       CLC             
.,F156 60       RTS             

                                *** input a character
.,F157 A5 99    LDA $99         
.,F159 D0 0B    BNE $F166       
.,F15B A5 D3    LDA $D3         
.,F15D 85 CA    STA $CA         
.,F15F A5 D6    LDA $D6         
.,F161 85 C9    STA $C9         
.,F163 4C 32 E6 JMP $E632       
.,F166 C9 03    CMP #$03        
.,F168 D0 09    BNE $F173       
.,F16A 85 D0    STA $D0         
.,F16C A5 D5    LDA $D5         
.,F16E 85 C8    STA $C8         
.,F170 4C 32 E6 JMP $E632       
.,F173 B0 38    BCS $F1AD       
.,F175 C9 02    CMP #$02        
.,F177 F0 3F    BEQ $F1B8       
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

                                *** read a byte from cassette buffer
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
.,F1AD A5 90    LDA $90         
.,F1AF F0 04    BEQ $F1B5       
.,F1B1 A9 0D    LDA #$0D        
.,F1B3 18       CLC             
.,F1B4 60       RTS             

                                *** read a byte from serial bus
.,F1B5 4C 13 EE JMP $EE13       

                                *** read a byte from RS-232 bus
.,F1B8 20 4E F1 JSR $F14E       
.,F1BB B0 F7    BCS $F1B4       
.,F1BD C9 00    CMP #$00        
.,F1BF D0 F2    BNE $F1B3       
.,F1C1 AD 97 02 LDA $0297       
.,F1C4 29 60    AND #$60        
.,F1C6 D0 E9    BNE $F1B1       
.,F1C8 F0 EE    BEQ $F1B8       

                                *** output a character
.,F1CA 48       PHA             
.,F1CB A5 9A    LDA $9A         
.,F1CD C9 03    CMP #$03        
.,F1CF D0 04    BNE $F1D5       
.,F1D1 68       PLA             
.,F1D2 4C 16 E7 JMP $E716       
.,F1D5 90 04    BCC $F1DB       
.,F1D7 68       PLA             
.,F1D8 4C DD ED JMP $EDDD       
.,F1DB 4A       LSR             
.,F1DC 68       PLA             
.,F1DD 85 9E    STA $9E         
.,F1DF 8A       TXA             
.,F1E0 48       PHA             
.,F1E1 98       TYA             
.,F1E2 48       PHA             
.,F1E3 90 23    BCC $F208       
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
.,F208 20 17 F0 JSR $F017       
.,F20B 4C FC F1 JMP $F1FC       

                                *** set input device
.,F20E 20 0F F3 JSR $F30F       
.,F211 F0 03    BEQ $F216       
.,F213 4C 01 F7 JMP $F701       
.,F216 20 1F F3 JSR $F31F       
.,F219 A5 BA    LDA $BA         
.,F21B F0 16    BEQ $F233       
.,F21D C9 03    CMP #$03        
.,F21F F0 12    BEQ $F233       
.,F221 B0 14    BCS $F237       
.,F223 C9 02    CMP #$02        
.,F225 D0 03    BNE $F22A       
.,F227 4C 4D F0 JMP $F04D       
.,F22A A6 B9    LDX $B9         
.,F22C E0 60    CPX #$60        
.,F22E F0 03    BEQ $F233       
.,F230 4C 0A F7 JMP $F70A       
.,F233 85 99    STA $99         
.,F235 18       CLC             
.,F236 60       RTS             

                                *** set serial bus input device
.,F237 AA       TAX             
.,F238 20 09 ED JSR $ED09       
.,F23B A5 B9    LDA $B9         
.,F23D 10 06    BPL $F245       
.,F23F 20 CC ED JSR $EDCC       
.,F242 4C 48 F2 JMP $F248       
.,F245 20 C7 ED JSR $EDC7       
.,F248 8A       TXA             
.,F249 24 90    BIT $90         
.,F24B 10 E6    BPL $F233       
.,F24D 4C 07 F7 JMP $F707       

                                *** set output device
.,F250 20 0F F3 JSR $F30F       
.,F253 F0 03    BEQ $F258       
.,F255 4C 01 F7 JMP $F701       
.,F258 20 1F F3 JSR $F31F       
.,F25B A5 BA    LDA $BA         
.,F25D D0 03    BNE $F262       
.,F25F 4C 0D F7 JMP $F70D       
.,F262 C9 03    CMP #$03        
.,F264 F0 0F    BEQ $F275       
.,F266 B0 11    BCS $F279       
.,F268 C9 02    CMP #$02        
.,F26A D0 03    BNE $F26F       
.,F26C 4C E1 EF JMP $EFE1       
.,F26F A6 B9    LDX $B9         
.,F271 E0 60    CPX #$60        
.,F273 F0 EA    BEQ $F25F       
.,F275 85 9A    STA $9A         
.,F277 18       CLC             
.,F278 60       RTS             

                                *** set serial bus output device
.,F279 AA       TAX             
.,F27A 20 0C ED JSR $ED0C       
.,F27D A5 B9    LDA $B9         
.,F27F 10 05    BPL $F286       
.,F281 20 BE ED JSR $EDBE       
.,F284 D0 03    BNE $F289       
.,F286 20 B9 ED JSR $EDB9       
.,F289 8A       TXA             
.,F28A 24 90    BIT $90         
.,F28C 10 E7    BPL $F275       
.,F28E 4C 07 F7 JMP $F707       

                                *** close a file
.,F291 20 14 F3 JSR $F314       
.,F294 F0 02    BEQ $F298       
.,F296 18       CLC             
.,F297 60       RTS             
.,F298 20 1F F3 JSR $F31F       
.,F29B 8A       TXA             
.,F29C 48       PHA             
.,F29D A5 BA    LDA $BA         
.,F29F F0 50    BEQ $F2F1       
.,F2A1 C9 03    CMP #$03        
.,F2A3 F0 4C    BEQ $F2F1       
.,F2A5 B0 47    BCS $F2EE       
.,F2A7 C9 02    CMP #$02        
.,F2A9 D0 1D    BNE $F2C8       
.,F2AB 68       PLA             
.,F2AC 20 F2 F2 JSR $F2F2       
.,F2AF 20 83 F4 JSR $F483       
.,F2B2 20 27 FE JSR $FE27       
.,F2B5 A5 F8    LDA $F8         
.,F2B7 F0 01    BEQ $F2BA       
.,F2B9 C8       INY             
.,F2BA A5 FA    LDA $FA         
.,F2BC F0 01    BEQ $F2BF       
.,F2BE C8       INY             
.,F2BF A9 00    LDA #$00        
.,F2C1 85 F8    STA $F8         
.,F2C3 85 FA    STA $FA         
.,F2C5 4C 7D F4 JMP $F47D       

                                *** close cassette device
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

                                *** close serial bus device
.,F2EE 20 42 F6 JSR $F642       
.,F2F1 68       PLA             

                                *** reorganise file tables
.,F2F2 AA       TAX             
.,F2F3 C6 98    DEC $98         
.,F2F5 E4 98    CPX $98         
.,F2F7 F0 14    BEQ $F30D       
.,F2F9 A4 98    LDY $98         
.,F2FB B9 59 02 LDA $0259,Y     
.,F2FE 9D 59 02 STA $0259,X     
.,F301 B9 63 02 LDA $0263,Y     
.,F304 9D 63 02 STA $0263,X     
.,F307 B9 6D 02 LDA $026D,Y     
.,F30A 9D 6D 02 STA $026D,X     
.,F30D 18       CLC             
.,F30E 60       RTS             

                                *** check X against logical file table
.,F30F A9 00    LDA #$00        
.,F311 85 90    STA $90         
.,F313 8A       TXA             
.,F314 A6 98    LDX $98         
.,F316 CA       DEX             
.,F317 30 15    BMI $F32E       
.,F319 DD 59 02 CMP $0259,X     
.,F31C D0 F8    BNE $F316       
.,F31E 60       RTS             

                                *** set file parameters depending on X
.,F31F BD 59 02 LDA $0259,X     
.,F322 85 B8    STA $B8         
.,F324 BD 63 02 LDA $0263,X     
.,F327 85 BA    STA $BA         
.,F329 BD 6D 02 LDA $026D,X     
.,F32C 85 B9    STA $B9         
.,F32E 60       RTS             

                                *** close all files
.,F32F A9 00    LDA #$00        
.,F331 85 98    STA $98         

                                *** restore I/O to default devices
.,F333 A2 03    LDX #$03        
.,F335 E4 9A    CPX $9A         
.,F337 B0 03    BCS $F33C       
.,F339 20 FE ED JSR $EDFE       
.,F33C E4 99    CPX $99         
.,F33E B0 03    BCS $F343       
.,F340 20 EF ED JSR $EDEF       
.,F343 86 9A    STX $9A         
.,F345 A9 00    LDA #$00        
.,F347 85 99    STA $99         
.,F349 60       RTS             

                                *** open a file
.,F34A A6 B8    LDX $B8         
.,F34C D0 03    BNE $F351       
.,F34E 4C 0A F7 JMP $F70A       
.,F351 20 0F F3 JSR $F30F       
.,F354 D0 03    BNE $F359       
.,F356 4C FE F6 JMP $F6FE       
.,F359 A6 98    LDX $98         
.,F35B E0 0A    CPX #$0A        
.,F35D 90 03    BCC $F362       
.,F35F 4C FB F6 JMP $F6FB       
.,F362 E6 98    INC $98         
.,F364 A5 B8    LDA $B8         
.,F366 9D 59 02 STA $0259,X     
.,F369 A5 B9    LDA $B9         
.,F36B 09 60    ORA #$60        
.,F36D 85 B9    STA $B9         
.,F36F 9D 6D 02 STA $026D,X     
.,F372 A5 BA    LDA $BA         
.,F374 9D 63 02 STA $0263,X     
.,F377 F0 5A    BEQ $F3D3       
.,F379 C9 03    CMP #$03        
.,F37B F0 56    BEQ $F3D3       
.,F37D 90 05    BCC $F384       
.,F37F 20 D5 F3 JSR $F3D5       
.,F382 90 4F    BCC $F3D3       
.,F384 C9 02    CMP #$02        
.,F386 D0 03    BNE $F38B       
.,F388 4C 09 F4 JMP $F409       

                                *** open for cassette device
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

                                *** open cassette for input
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

                                *** open for serial bus devices
.,F3D5 A5 B9    LDA $B9         
.,F3D7 30 FA    BMI $F3D3       
.,F3D9 A4 B7    LDY $B7         
.,F3DB F0 F6    BEQ $F3D3       
.,F3DD A9 00    LDA #$00        
.,F3DF 85 90    STA $90         
.,F3E1 A5 BA    LDA $BA         
.,F3E3 20 0C ED JSR $ED0C       
.,F3E6 A5 B9    LDA $B9         
.,F3E8 09 F0    ORA #$F0        
.,F3EA 20 B9 ED JSR $EDB9       
.,F3ED A5 90    LDA $90         
.,F3EF 10 05    BPL $F3F6       
.,F3F1 68       PLA             
.,F3F2 68       PLA             
.,F3F3 4C 07 F7 JMP $F707       
.,F3F6 A5 B7    LDA $B7         
.,F3F8 F0 0C    BEQ $F406       
.,F3FA A0 00    LDY #$00        
.,F3FC B1 BB    LDA ($BB),Y     
.,F3FE 20 DD ED JSR $EDDD       
.,F401 C8       INY             
.,F402 C4 B7    CPY $B7         
.,F404 D0 F6    BNE $F3FC       
.,F406 4C 54 F6 JMP $F654       

                                *** open RS-232 device
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

                                *** initialise CIA2
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

                                *** load ram from a device
.,F49E 86 C3    STX $C3         
.,F4A0 84 C4    STY $C4         
.,F4A2 6C 30 03 JMP ($0330)     normally F4A5

                                *** standard load ram entry
.,F4A5 85 93    STA $93         
.,F4A7 A9 00    LDA #$00        
.,F4A9 85 90    STA $90         
.,F4AB A5 BA    LDA $BA         
.,F4AD D0 03    BNE $F4B2       
.,F4AF 4C 13 F7 JMP $F713       
.,F4B2 C9 03    CMP #$03        
.,F4B4 F0 F9    BEQ $F4AF       
.,F4B6 90 7B    BCC $F533       
.,F4B8 A4 B7    LDY $B7         
.,F4BA D0 03    BNE $F4BF       
.,F4BC 4C 10 F7 JMP $F710       
.,F4BF A6 B9    LDX $B9         
.,F4C1 20 AF F5 JSR $F5AF       
.,F4C4 A9 60    LDA #$60        
.,F4C6 85 B9    STA $B9         
.,F4C8 20 D5 F3 JSR $F3D5       
.,F4CB A5 BA    LDA $BA         
.,F4CD 20 09 ED JSR $ED09       
.,F4D0 A5 B9    LDA $B9         
.,F4D2 20 C7 ED JSR $EDC7       
.,F4D5 20 13 EE JSR $EE13       
.,F4D8 85 AE    STA $AE         
.,F4DA A5 90    LDA $90         
.,F4DC 4A       LSR             
.,F4DD 4A       LSR             
.,F4DE B0 50    BCS $F530       
.,F4E0 20 13 EE JSR $EE13       
.,F4E3 85 AF    STA $AF         
.,F4E5 8A       TXA             
.,F4E6 D0 08    BNE $F4F0       
.,F4E8 A5 C3    LDA $C3         
.,F4EA 85 AE    STA $AE         
.,F4EC A5 C4    LDA $C4         
.,F4EE 85 AF    STA $AF         
.,F4F0 20 D2 F5 JSR $F5D2       
.,F4F3 A9 FD    LDA #$FD        
.,F4F5 25 90    AND $90         
.,F4F7 85 90    STA $90         
.,F4F9 20 E1 FF JSR $FFE1       
.,F4FC D0 03    BNE $F501       
.,F4FE 4C 33 F6 JMP $F633       
.,F501 20 13 EE JSR $EE13       
.,F504 AA       TAX             
.,F505 A5 90    LDA $90         
.,F507 4A       LSR             
.,F508 4A       LSR             
.,F509 B0 E8    BCS $F4F3       
.,F50B 8A       TXA             
.,F50C A4 93    LDY $93         
.,F50E F0 0C    BEQ $F51C       
.,F510 A0 00    LDY #$00        
.,F512 D1 AE    CMP ($AE),Y     
.,F514 F0 08    BEQ $F51E       
.,F516 A9 10    LDA #$10        
.,F518 20 1C FE JSR $FE1C       
.:F51B 2C       .BYTE $2C       
.,F51C 91 AE    STA ($AE),Y     
.,F51E E6 AE    INC $AE         
.,F520 D0 02    BNE $F524       
.,F522 E6 AF    INC $AF         
.,F524 24 90    BIT $90         
.,F526 50 CB    BVC $F4F3       
.,F528 20 EF ED JSR $EDEF       
.,F52B 20 42 F6 JSR $F642       
.,F52E 90 79    BCC $F5A9       
.,F530 4C 04 F7 JMP $F704       
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
.,F5A9 18       CLC             
.,F5AA A6 AE    LDX $AE         
.,F5AC A4 AF    LDY $AF         
.,F5AE 60       RTS             

                                *** handle messages for loading
.,F5AF A5 9D    LDA $9D         
.,F5B1 10 1E    BPL $F5D1       
.,F5B3 A0 0C    LDY #$0C        
.,F5B5 20 2F F1 JSR $F12F       
.,F5B8 A5 B7    LDA $B7         
.,F5BA F0 15    BEQ $F5D1       
.,F5BC A0 17    LDY #$17        
.,F5BE 20 2F F1 JSR $F12F       
.,F5C1 A4 B7    LDY $B7         
.,F5C3 F0 0C    BEQ $F5D1       
.,F5C5 A0 00    LDY #$00        
.,F5C7 B1 BB    LDA ($BB),Y     
.,F5C9 20 D2 FF JSR $FFD2       
.,F5CC C8       INY             
.,F5CD C4 B7    CPY $B7         
.,F5CF D0 F6    BNE $F5C7       
.,F5D1 60       RTS             

                                *** do load/verify message
.,F5D2 A0 49    LDY #$49        
.,F5D4 A5 93    LDA $93         
.,F5D6 F0 02    BEQ $F5DA       
.,F5D8 A0 59    LDY #$59        
.,F5DA 4C 2B F1 JMP $F12B       

                                *** save ram to a device
.,F5DD 86 AE    STX $AE         
.,F5DF 84 AF    STY $AF         
.,F5E1 AA       TAX             
.,F5E2 B5 00    LDA $00,X       
.,F5E4 85 C1    STA $C1         
.,F5E6 B5 01    LDA $01,X       
.,F5E8 85 C2    STA $C2         
.,F5EA 6C 32 03 JMP ($0332)     normally F5ED

                                *** standard save ram entry
.,F5ED A5 BA    LDA $BA         
.,F5EF D0 03    BNE $F5F4       
.,F5F1 4C 13 F7 JMP $F713       
.,F5F4 C9 03    CMP #$03        
.,F5F6 F0 F9    BEQ $F5F1       
.,F5F8 90 5F    BCC $F659       
.,F5FA A9 61    LDA #$61        
.,F5FC 85 B9    STA $B9         
.,F5FE A4 B7    LDY $B7         
.,F600 D0 03    BNE $F605       
.,F602 4C 10 F7 JMP $F710       
.,F605 20 D5 F3 JSR $F3D5       
.,F608 20 8F F6 JSR $F68F       
.,F60B A5 BA    LDA $BA         
.,F60D 20 0C ED JSR $ED0C       
.,F610 A5 B9    LDA $B9         
.,F612 20 B9 ED JSR $EDB9       
.,F615 A0 00    LDY #$00        
.,F617 20 8E FB JSR $FB8E       
.,F61A A5 AC    LDA $AC         
.,F61C 20 DD ED JSR $EDDD       
.,F61F A5 AD    LDA $AD         
.,F621 20 DD ED JSR $EDDD       
.,F624 20 D1 FC JSR $FCD1       
.,F627 B0 16    BCS $F63F       
.,F629 B1 AC    LDA ($AC),Y     
.,F62B 20 DD ED JSR $EDDD       
.,F62E 20 E1 FF JSR $FFE1       
.,F631 D0 07    BNE $F63A       
.,F633 20 42 F6 JSR $F642       
.,F636 A9 00    LDA #$00        
.,F638 38       SEC             
.,F639 60       RTS             
.,F63A 20 DB FC JSR $FCDB       
.,F63D D0 E5    BNE $F624       
.,F63F 20 FE ED JSR $EDFE       

                                *** close serial bus device
.,F642 24 B9    BIT $B9         
.,F644 30 11    BMI $F657       
.,F646 A5 BA    LDA $BA         
.,F648 20 0C ED JSR $ED0C       
.,F64B A5 B9    LDA $B9         
.,F64D 29 EF    AND #$EF        
.,F64F 09 E0    ORA #$E0        
.,F651 20 B9 ED JSR $EDB9       
.,F654 20 FE ED JSR $EDFE       
.,F657 18       CLC             
.,F658 60       RTS             
.,F659 4A       LSR             
.,F65A B0 03    BCS $F65F       
.,F65C 4C 13 F7 JMP $F713       

                                *** save ram to cassette
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

                                *** do saving message and filename
.,F68F A5 9D    LDA $9D         
.,F691 10 FB    BPL $F68E       
.,F693 A0 51    LDY #$51        
.,F695 20 2F F1 JSR $F12F       
.,F698 4C C1 F5 JMP $F5C1       

                                *** increment real time clock
.,F69B A2 00    LDX #$00        
.,F69D E6 A2    INC $A2         
.,F69F D0 06    BNE $F6A7       
.,F6A1 E6 A1    INC $A1         
.,F6A3 D0 02    BNE $F6A7       
.,F6A5 E6 A0    INC $A0         
.,F6A7 38       SEC             
.,F6A8 A5 A2    LDA $A2         
.,F6AA E9 01    SBC #$01        
.,F6AC A5 A1    LDA $A1         
.,F6AE E9 1A    SBC #$1A        
.,F6B0 A5 A0    LDA $A0         
.,F6B2 E9 4F    SBC #$4F        
.,F6B4 90 06    BCC $F6BC       
.,F6B6 86 A0    STX $A0         
.,F6B8 86 A1    STX $A1         
.,F6BA 86 A2    STX $A2         
.,F6BC AD 01 DC LDA $DC01       
.,F6BF CD 01 DC CMP $DC01       
.,F6C2 D0 F8    BNE $F6BC       
.,F6C4 AA       TAX             
.,F6C5 30 13    BMI $F6DA       
.,F6C7 A2 BD    LDX #$BD        
.,F6C9 8E 00 DC STX $DC00       
.,F6CC AE 01 DC LDX $DC01       
.,F6CF EC 01 DC CPX $DC01       
.,F6D2 D0 F8    BNE $F6CC       
.,F6D4 8D 00 DC STA $DC00       
.,F6D7 E8       INX             
.,F6D8 D0 02    BNE $F6DC       
.,F6DA 85 91    STA $91         
.,F6DC 60       RTS             

                                *** read real time clock
.,F6DD 78       SEI             
.,F6DE A5 A2    LDA $A2         
.,F6E0 A6 A1    LDX $A1         
.,F6E2 A4 A0    LDY $A0         

                                *** set real time clock
.,F6E4 78       SEI             
.,F6E5 85 A2    STA $A2         
.,F6E7 86 A1    STX $A1         
.,F6E9 84 A0    STY $A0         
.,F6EB 58       CLI             
.,F6EC 60       RTS             

                                *** test STOP key
.,F6ED A5 91    LDA $91         
.,F6EF C9 7F    CMP #$7F        
.,F6F1 D0 07    BNE $F6FA       
.,F6F3 08       PHP             
.,F6F4 20 CC FF JSR $FFCC       
.,F6F7 85 C6    STA $C6         
.,F6F9 28       PLP             
.,F6FA 60       RTS             

                                *** handle I/O errors
.,F6FB A9 01    LDA #$01        too many files
.:F6FD 2C       .BYTE $2C       
.,F6FE A9 02    LDA #$02        file open
.:F700 2C       .BYTE $2C       
.,F701 A9 03    LDA #$03        file not open
.:F703 2C       .BYTE $2C       
.,F704 A9 04    LDA #$04        file not found
.:F706 2C       .BYTE $2C       
.,F707 A9 05    LDA #$05        device not present
.:F709 2C       .BYTE $2C       
.,F70A A9 06    LDA #$06        not input file
.:F70C 2C       .BYTE $2C       
.,F70D A9 07    LDA #$07        not output file
.:F70F 2C       .BYTE $2C       
.,F710 A9 08    LDA #$08        file name missing
.:F712 2C       .BYTE $2C       
.,F713 A9 09    LDA #$09        illegal device no.
.,F715 48       PHA             
.,F716 20 CC FF JSR $FFCC       
.,F719 A0 00    LDY #$00        
.,F71B 24 9D    BIT $9D         
.,F71D 50 0A    BVC $F729       
.,F71F 20 2F F1 JSR $F12F       
.,F722 68       PLA             
.,F723 48       PHA             
.,F724 09 30    ORA #$30        
.,F726 20 D2 FF JSR $FFD2       
.,F729 68       PLA             
.,F72A 38       SEC             
.,F72B 60       RTS             

                                *** get next file header from cassette
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

                                *** write a special block to cassette with code in A
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

                                *** set tape buffer pointer in XY
.,F7D0 A6 B2    LDX $B2         
.,F7D2 A4 B3    LDY $B3         
.,F7D4 C0 02    CPY #$02        
.,F7D6 60       RTS             

                                *** set cassette buffer to I/O area
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

                                *** search tape for a file name
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

                                *** add 1 to tape index and test for overflow
.,F80D 20 D0 F7 JSR $F7D0       
.,F810 E6 A6    INC $A6         
.,F812 A4 A6    LDY $A6         
.,F814 C0 C0    CPY #$C0        
.,F816 60       RTS             

                                *** handle messages and
                                test cassette buttons for read
.,F817 20 2E F8 JSR $F82E       
.,F81A F0 1A    BEQ $F836       
.,F81C A0 1B    LDY #$1B        
.,F81E 20 2F F1 JSR $F12F       
.,F821 20 D0 F8 JSR $F8D0       
.,F824 20 2E F8 JSR $F82E       
.,F827 D0 F8    BNE $F821       
.,F829 A0 6A    LDY #$6A        
.,F82B 4C 2F F1 JMP $F12F       

                                *** test sense line for a button
                                depressed on cassette
.,F82E A9 10    LDA #$10        
.,F830 24 01    BIT $01         
.,F832 D0 02    BNE $F836       
.,F834 24 01    BIT $01         
.,F836 18       CLC             
.,F837 60       RTS             

                                *** set messages and test cassette line
                                for input
.,F838 20 2E F8 JSR $F82E       
.,F83B F0 F9    BEQ $F836       
.,F83D A0 2E    LDY #$2E        
.,F83F D0 DD    BNE $F81E       

                                *** read a block from cassette
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

                                *** write a block from cassette
.,F864 20 D7 F7 JSR $F7D7       
.,F867 A9 14    LDA #$14        
.,F869 85 AB    STA $AB         
.,F86B 20 38 F8 JSR $F838       
.,F86E B0 6C    BCS $F8DC       
.,F870 78       SEI             
.,F871 A9 82    LDA #$82        
.,F873 A2 08    LDX #$08        

                                *** common code for cassette read and write
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

                                *** handle stop key during cassette operations
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

                                *** schedule CIA1 timer A depending on X
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

                                *** cassette read IRQ routine
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

                                *** receive next byte from cassette
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

                                *** move save/load address into $AC/$AD
.,FB8E A5 C2    LDA $C2         
.,FB90 85 AD    STA $AD         
.,FB92 A5 C1    LDA $C1         
.,FB94 85 AC    STA $AC         
.,FB96 60       RTS             

                                *** initalise cassette read/write variables
.,FB97 A9 08    LDA #$08        
.,FB99 85 A3    STA $A3         
.,FB9B A9 00    LDA #$00        
.,FB9D 85 A4    STA $A4         
.,FB9F 85 A8    STA $A8         
.,FBA1 85 9B    STA $9B         
.,FBA3 85 A9    STA $A9         
.,FBA5 60       RTS             

                                *** schedule CIA1 timer B and
                                invert casette write line
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

                                *** IRQ routine for cassette write B
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

                                *** IRQ routine for cassette write A
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

                                *** switch from cassette IRQ to default IRQ
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

                                *** terminate cassette I/O
.,FCB8 20 93 FC JSR $FC93       
.,FCBB F0 97    BEQ $FC54       

                                *** set IRQ vector depending on X
.,FCBD BD 93 FD LDA $FD93,X     
.,FCC0 8D 14 03 STA $0314       
.,FCC3 BD 94 FD LDA $FD94,X     
.,FCC6 8D 15 03 STA $0315       
.,FCC9 60       RTS             

                                *** stop cassette motor
.,FCCA A5 01    LDA $01         
.,FCCC 09 20    ORA #$20        
.,FCCE 85 01    STA $01         
.,FCD0 60       RTS             

                                *** compare $AC/$AD with $AE/$AF
.,FCD1 38       SEC             
.,FCD2 A5 AC    LDA $AC         
.,FCD4 E5 AE    SBC $AE         
.,FCD6 A5 AD    LDA $AD         
.,FCD8 E5 AF    SBC $AF         
.,FCDA 60       RTS             

                                *** increment $AC/$AD
.,FCDB E6 AC    INC $AC         
.,FCDD D0 02    BNE $FCE1       
.,FCDF E6 AD    INC $AD         
.,FCE1 60       RTS             

                                *** RESET routine
.,FCE2 A2 FF    LDX #$FF        
.,FCE4 78       SEI             
.,FCE5 9A       TXS             
.,FCE6 D8       CLD             
.,FCE7 20 02 FD JSR $FD02       
.,FCEA D0 03    BNE $FCEF       
.,FCEC 6C 00 80 JMP ($8000)     start cartridge
.,FCEF 8E 16 D0 STX $D016       
.,FCF2 20 A3 FD JSR $FDA3       
.,FCF5 20 50 FD JSR $FD50       
.,FCF8 20 15 FD JSR $FD15       
.,FCFB 20 5B FF JSR $FF5B       
.,FCFE 58       CLI             
.,FCFF 6C 00 A0 JMP ($A000)     start basic

                                *** check for a cartridge
.,FD02 A2 05    LDX #$05        
.,FD04 BD 0F FD LDA $FD0F,X     
.,FD07 DD 03 80 CMP $8003,X     
.,FD0A D0 03    BNE $FD0F       
.,FD0C CA       DEX             
.,FD0D D0 F5    BNE $FD04       
.,FD0F 60       RTS             

                                *** CBM80
.:FD10 C3 C2 CD 38 30           

                                *** restore I/O vectors
.,FD15 A2 30    LDX #$30        low  FD30
.,FD17 A0 FD    LDY #$FD        high FD30
.,FD19 18       CLC             

                                *** set I/O vectors depending on XY
.,FD1A 86 C3    STX $C3         
.,FD1C 84 C4    STY $C4         
.,FD1E A0 1F    LDY #$1F        
.,FD20 B9 14 03 LDA $0314,Y     
.,FD23 B0 02    BCS $FD27       
.,FD25 B1 C3    LDA ($C3),Y     
.,FD27 91 C3    STA ($C3),Y     
.,FD29 99 14 03 STA $0314,Y     
.,FD2C 88       DEY             
.,FD2D 10 F1    BPL $FD20       
.,FD2F 60       RTS             

                                *** vectors for OS at $0314-$0333
.:FD30 31 EA                    IRQ
.:FD32 66 FE                    BRK
.:FD34 47 FE                    NMI
.:FD36 4A F3                    open
.:FD38 91 F2                    close
.:FD3A 0E F2                    set input dev
.:FD3C 50 F2                    set output dev
.:FD3E 33 F3                    restore I/O
.:FD40 57 F1                    input
.:FD42 CA F1                    output
.:FD44 ED F6                    test stop key
.:FD46 3E F1                    get
.:FD48 2F F3                    abort I/O
.:FD4A 66 FE                    unused (BRK)
.:FD4C A5 F4                    load ram
.:FD4E ED F5                    save ram

                                *** initalise memory pointers
.,FD50 A9 00    LDA #$00        
.,FD52 A8       TAY             
.,FD53 99 02 00 STA $0002,Y     
.,FD56 99 00 02 STA $0200,Y     
.,FD59 99 00 03 STA $0300,Y     
.,FD5C C8       INY             
.,FD5D D0 F4    BNE $FD53       
.,FD5F A2 3C    LDX #$3C        
.,FD61 A0 03    LDY #$03        
.,FD63 86 B2    STX $B2         
.,FD65 84 B3    STY $B3         
.,FD67 A8       TAY             
.,FD68 A9 03    LDA #$03        
.,FD6A 85 C2    STA $C2         
.,FD6C E6 C2    INC $C2         
.,FD6E B1 C1    LDA ($C1),Y     
.,FD70 AA       TAX             
.,FD71 A9 55    LDA #$55        
.,FD73 91 C1    STA ($C1),Y     
.,FD75 D1 C1    CMP ($C1),Y     
.,FD77 D0 0F    BNE $FD88       
.,FD79 2A       ROL             
.,FD7A 91 C1    STA ($C1),Y     
.,FD7C D1 C1    CMP ($C1),Y     
.,FD7E D0 08    BNE $FD88       
.,FD80 8A       TXA             
.,FD81 91 C1    STA ($C1),Y     
.,FD83 C8       INY             
.,FD84 D0 E8    BNE $FD6E       
.,FD86 F0 E4    BEQ $FD6C       
.,FD88 98       TYA             
.,FD89 AA       TAX             
.,FD8A A4 C2    LDY $C2         
.,FD8C 18       CLC             
.,FD8D 20 2D FE JSR $FE2D       
.,FD90 A9 08    LDA #$08        
.,FD92 8D 82 02 STA $0282       
.,FD95 A9 04    LDA #$04        
.,FD97 8D 88 02 STA $0288       
.,FD9A 60       RTS             

                                *** IRQ vectors
.:FD9B 6A FC                    cassette write A
.:FD9D CD FB                    cassette write B
.:FD9F 31 EA                    standard IRQ
.:FDA1 2C F9                    cassette read

                                *** initaliase I/O devices
.,FDA3 A9 7F    LDA #$7F        
.,FDA5 8D 0D DC STA $DC0D       
.,FDA8 8D 0D DD STA $DD0D       
.,FDAB 8D 00 DC STA $DC00       
.,FDAE A9 08    LDA #$08        
.,FDB0 8D 0E DC STA $DC0E       
.,FDB3 8D 0E DD STA $DD0E       
.,FDB6 8D 0F DC STA $DC0F       
.,FDB9 8D 0F DD STA $DD0F       
.,FDBC A2 00    LDX #$00        
.,FDBE 8E 03 DC STX $DC03       
.,FDC1 8E 03 DD STX $DD03       
.,FDC4 8E 18 D4 STX $D418       
.,FDC7 CA       DEX             
.,FDC8 8E 02 DC STX $DC02       
.,FDCB A9 07    LDA #$07        
.,FDCD 8D 00 DD STA $DD00       
.,FDD0 A9 3F    LDA #$3F        
.,FDD2 8D 02 DD STA $DD02       
.,FDD5 A9 E7    LDA #$E7        
.,FDD7 85 01    STA $01         
.,FDD9 A9 2F    LDA #$2F        
.,FDDB 85 00    STA $00         

                                *** initalise TAL1/TAH1 fpr 1/60 of a second
.,FDDD AD A6 02 LDA $02A6       
.,FDE0 F0 0A    BEQ $FDEC       
.,FDE2 A9 25    LDA #$25        
.,FDE4 8D 04 DC STA $DC04       
.,FDE7 A9 40    LDA #$40        
.,FDE9 4C F3 FD JMP $FDF3       
.,FDEC A9 95    LDA #$95        
.,FDEE 8D 04 DC STA $DC04       
.,FDF1 A9 42    LDA #$42        
.,FDF3 8D 05 DC STA $DC05       
.,FDF6 4C 6E FF JMP $FF6E       

                                *** initalise file name parameters
.,FDF9 85 B7    STA $B7         
.,FDFB 86 BB    STX $BB         
.,FDFD 84 BC    STY $BC         
.,FDFF 60       RTS             

                                *** inatalise file parameters
.,FE00 85 B8    STA $B8         
.,FE02 86 BA    STX $BA         
.,FE04 84 B9    STY $B9         
.,FE06 60       RTS             

                                *** read I/O status word
.,FE07 A5 BA    LDA $BA         
.,FE09 C9 02    CMP #$02        
.,FE0B D0 0D    BNE $FE1A       
.,FE0D AD 97 02 LDA $0297       
.,FE10 48       PHA             
.,FE11 A9 00    LDA #$00        
.,FE13 8D 97 02 STA $0297       
.,FE16 68       PLA             
.,FE17 60       RTS             

                                *** control kernel messages
.,FE18 85 9D    STA $9D         

                                *** read ST
.,FE1A A5 90    LDA $90         

                                *** add A to ST
.,FE1C 05 90    ORA $90         
.,FE1E 85 90    STA $90         
.,FE20 60       RTS             

                                *** set timeout on serail bus
.,FE21 8D 85 02 STA $0285       
.,FE24 60       RTS             

                                *** read/set top of memory
.,FE25 90 06    BCC $FE2D       
.,FE27 AE 83 02 LDX $0283       
.,FE2A AC 84 02 LDY $0284       
.,FE2D 8E 83 02 STX $0283       
.,FE30 8C 84 02 STY $0284       
.,FE33 60       RTS             

                                *** read/set bottom of memory
.,FE34 90 06    BCC $FE3C       
.,FE36 AE 81 02 LDX $0281       
.,FE39 AC 82 02 LDY $0282       
.,FE3C 8E 81 02 STX $0281       
.,FE3F 8C 82 02 STY $0282       
.,FE42 60       RTS             

                                *** NMI entry
.,FE43 78       SEI             
.,FE44 6C 18 03 JMP ($0318)     normally FE47

                                *** standard NMI routine
.,FE47 48       PHA             
.,FE48 8A       TXA             
.,FE49 48       PHA             
.,FE4A 98       TYA             
.,FE4B 48       PHA             
.,FE4C A9 7F    LDA #$7F        
.,FE4E 8D 0D DD STA $DD0D       
.,FE51 AC 0D DD LDY $DD0D       
.,FE54 30 1C    BMI $FE72       
.,FE56 20 02 FD JSR $FD02       
.,FE59 D0 03    BNE $FE5E       
.,FE5B 6C 02 80 JMP ($8002)     cartridge warm start
.,FE5E 20 BC F6 JSR $F6BC       
.,FE61 20 E1 FF JSR $FFE1       
.,FE64 D0 0C    BNE $FE72       

                                *** BRK routine
.,FE66 20 15 FD JSR $FD15       
.,FE69 20 A3 FD JSR $FDA3       
.,FE6C 20 18 E5 JSR $E518       
.,FE6F 6C 02 A0 JMP ($A002)     

                                *** internal NMI
.,FE72 98       TYA             
.,FE73 2D A1 02 AND $02A1       
.,FE76 AA       TAX             
.,FE77 29 01    AND #$01        
.,FE79 F0 28    BEQ $FEA3       
.,FE7B AD 00 DD LDA $DD00       
.,FE7E 29 FB    AND #$FB        
.,FE80 05 B5    ORA $B5         
.,FE82 8D 00 DD STA $DD00       
.,FE85 AD A1 02 LDA $02A1       
.,FE88 8D 0D DD STA $DD0D       
.,FE8B 8A       TXA             
.,FE8C 29 12    AND #$12        
.,FE8E F0 0D    BEQ $FE9D       
.,FE90 29 02    AND #$02        
.,FE92 F0 06    BEQ $FE9A       
.,FE94 20 D6 FE JSR $FED6       
.,FE97 4C 9D FE JMP $FE9D       
.,FE9A 20 07 FF JSR $FF07       
.,FE9D 20 BB EE JSR $EEBB       
.,FEA0 4C B6 FE JMP $FEB6       
.,FEA3 8A       TXA             
.,FEA4 29 02    AND #$02        
.,FEA6 F0 06    BEQ $FEAE       
.,FEA8 20 D6 FE JSR $FED6       
.,FEAB 4C B6 FE JMP $FEB6       
.,FEAE 8A       TXA             
.,FEAF 29 10    AND #$10        
.,FEB1 F0 03    BEQ $FEB6       
.,FEB3 20 07 FF JSR $FF07       
.,FEB6 AD A1 02 LDA $02A1       
.,FEB9 8D 0D DD STA $DD0D       
.,FEBC 68       PLA             
.,FEBD A8       TAY             
.,FEBE 68       PLA             
.,FEBF AA       TAX             
.,FEC0 68       PLA             
.,FEC1 40       RTI             

                                *** baud rate tables
.:FEC2 C1 27                    50
.:FEC4 3E 1A                    75
.:FEC6 C5 11                    110
.:FEC8 74 0E                    134.5
.:FECA ED 0C                    150
.:FECC 45 06                    300
.:FECE F0 02                    600
.:FED0 46 01                    1200
.:FED2 B8 00                    1800
.:FED4 71 00                    2400

                                *** input next bit on RS-232 and schedule TB2
.,FED6 AD 01 DD LDA $DD01       
.,FED9 29 01    AND #$01        
.,FEDB 85 A7    STA $A7         
.,FEDD AD 06 DD LDA $DD06       
.,FEE0 E9 1C    SBC #$1C        
.,FEE2 6D 99 02 ADC $0299       
.,FEE5 8D 06 DD STA $DD06       
.,FEE8 AD 07 DD LDA $DD07       
.,FEEB 6D 9A 02 ADC $029A       
.,FEEE 8D 07 DD STA $DD07       
.,FEF1 A9 11    LDA #$11        
.,FEF3 8D 0F DD STA $DD0F       
.,FEF6 AD A1 02 LDA $02A1       
.,FEF9 8D 0D DD STA $DD0D       
.,FEFC A9 FF    LDA #$FF        
.,FEFE 8D 06 DD STA $DD06       
.,FF01 8D 07 DD STA $DD07       
.,FF04 4C 59 EF JMP $EF59       

                                *** schedule TB2 using baud rate factor
.,FF07 AD 95 02 LDA $0295       
.,FF0A 8D 06 DD STA $DD06       
.,FF0D AD 96 02 LDA $0296       
.,FF10 8D 07 DD STA $DD07       
.,FF13 A9 11    LDA #$11        
.,FF15 8D 0F DD STA $DD0F       
.,FF18 A9 12    LDA #$12        
.,FF1A 4D A1 02 EOR $02A1       
.,FF1D 8D A1 02 STA $02A1       
.,FF20 A9 FF    LDA #$FF        
.,FF22 8D 06 DD STA $DD06       
.,FF25 8D 07 DD STA $DD07       
.,FF28 AE 98 02 LDX $0298       
.,FF2B 86 A8    STX $A8         
.,FF2D 60       RTS             

                                *** continuation of baud rate calculation
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
.,FF43 08       PHP             
.,FF44 68       PLA             
.,FF45 29 EF    AND #$EF        
.,FF47 48       PHA             

                                *** IRQ entry point
.,FF48 48       PHA             
.,FF49 8A       TXA             
.,FF4A 48       PHA             
.,FF4B 98       TYA             
.,FF4C 48       PHA             
.,FF4D BA       TSX             
.,FF4E BD 04 01 LDA $0104,X     
.,FF51 29 10    AND #$10        
.,FF53 F0 03    BEQ $FF58       
.,FF55 6C 16 03 JMP ($0316)     normally FE66
.,FF58 6C 14 03 JMP ($0314)     normally EA31

                                *** addition to I/O device initalisation
.,FF5B 20 18 E5 JSR $E518       
.,FF5E AD 12 D0 LDA $D012       
.,FF61 D0 FB    BNE $FF5E       
.,FF63 AD 19 D0 LDA $D019       
.,FF66 29 01    AND #$01        
.,FF68 8D A6 02 STA $02A6       
.,FF6B 4C DD FD JMP $FDDD       

                                *** end of scheduling TA for 1/60 second IRQ's
.,FF6E A9 81    LDA #$81        
.,FF70 8D 0D DC STA $DC0D       
.,FF73 AD 0E DC LDA $DC0E       
.,FF76 29 80    AND #$80        
.,FF78 09 11    ORA #$11        
.,FF7A 8D 0E DC STA $DC0E       
.,FF7D 4C 8E EE JMP $EE8E       
.:FF80 03                       kernal version number

                                *** kernal vectors
.,FF81 4C 5B FF JMP $FF5B       initalise screen and keyboard
.,FF84 4C A3 FD JMP $FDA3       initalise I/O devices
.,FF87 4C 50 FD JMP $FD50       initalise memory pointers
.,FF8A 4C 15 FD JMP $FD15       restore I/O vectors
.,FF8D 4C 1A FD JMP $FD1A       set I/O vectors from XY
.,FF90 4C 18 FE JMP $FE18       control kernal messages
.,FF93 4C B9 ED JMP $EDB9       read secondary address after listen
.,FF96 4C C7 ED JMP $EDC7       read secondary address after talk
.,FF99 4C 25 FE JMP $FE25       read/set top of memory
.,FF9C 4C 34 FE JMP $FE34       read/set bottom of memory
.,FF9F 4C 87 EA JMP $EA87       scan keyboard
.,FFA2 4C 21 FE JMP $FE21       set timout for serial bus
.,FFA5 4C 13 EE JMP $EE13       input on serial bus
.,FFA8 4C DD ED JMP $EDDD       output byte on serial bus
.,FFAB 4C EF ED JMP $EDEF       send untalk on serial bus
.,FFAE 4C FE ED JMP $EDFE       send unlisten on serial bus
.,FFB1 4C 0C ED JMP $ED0C       send listen on serial bus
.,FFB4 4C 09 ED JMP $ED09       send talk on serial bus
.,FFB7 4C 07 FE JMP $FE07       read I/O status word
.,FFBA 4C 00 FE JMP $FE00       set file parameters
.,FFBD 4C F9 FD JMP $FDF9       set filename parameters
.,FFC0 6C 1A 03 JMP ($031A)     (F34A) open a file
.,FFC3 6C 1C 03 JMP ($031C)     (F291) close a file
.,FFC6 6C 1E 03 JMP ($031E)     (F20E) set input device
.,FFC9 6C 20 03 JMP ($0320)     (F250) set output device
.,FFCC 6C 22 03 JMP ($0322)     (F333) restore I/O devices to default
.,FFCF 6C 24 03 JMP ($0324)     (F157) input char on current device
.,FFD2 6C 26 03 JMP ($0326)     (F1CA) output char on current device
.,FFD5 4C 9E F4 JMP $F49E       load ram from device
.,FFD8 4C DD F5 JMP $F5DD       save ram to device
.,FFDB 4C E4 F6 JMP $F6E4       set real time clock
.,FFDE 4C DD F6 JMP $F6DD       read real time clock
.,FFE1 6C 28 03 JMP ($0328)     (F6ED) check stop key
.,FFE4 6C 2A 03 JMP ($032A)     (F13E) get a character
.,FFE7 6C 2C 03 JMP ($032C)     (F32F) close all channels and files
.,FFEA 4C 9B F6 JMP $F69B       increment real time clock
.,FFED 4C 05 E5 JMP $E505       read organisation of screen into XY
.,FFF0 4C 0A E5 JMP $E50A       read/set XY cursor position
.,FFF3 4C 00 E5 JMP $E500       read base address of I/O devices

                                *** unused
.:FFF6 52 52 42 59              
.:FFFA 43 FE                    NMI vector
.:FFFC E2 FC                    RESET vector
.:FFFE 48 FF                    IRQ/BRK vector
