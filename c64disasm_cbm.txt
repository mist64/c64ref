- Fully Commented Commodore 64 KERNAL ROM Disassembly (English, "CBM")
-
- The comments have been taken from
-    The original C64 KERNAL source by Commodore (901227-03)
-    https://github.com/mist64/cbmsrc
-    https://www.pagetable.com/?p=894
-
- The comments here are basically a complete copy of the original
- source code, lined up with the version in the C64 ROM.
- This way, even all variable names are intact.
-
- Converted and formatted by Michael Steil <mist64@mac.com>
-
- Corrections (formatting, lining up) welcome at:
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
# * 32 leading spaces and ".LIB" indicate a heading.
# * Otherwise, 32 leading spaces indicate an overflow comment.
# The encoding is UTF-8.

                                .LIB   DISCLAIMER
                                ;****************************************
                                ;*                                      *
                                ;* KK  K EEEEE RRRR  NN  N  AAA  LL     *
                                ;* KK KK EE    RR  R NNN N AA  A LL     *
                                ;* KKK   EE    RR  R NNN N AA  A LL     *
                                ;* KKK   EEEE  RRRR  NNNNN AAAAA LL     *
                                ;* KK K  EE    RR  R NN NN AA  A LL     *
                                ;* KK KK EE    RR  R NN NN AA  A LL     *
                                ;* KK KK EEEEE RR  R NN NN AA  A LLLLL  *
                                ;*                                      *
                                ;***************************************
                                ;
                                ;***************************************
                                ;* PET KERNAL                          *
                                ;*   MEMORY AND I/O DEPENDENT ROUTINES *
                                ;* DRIVING THE HARDWARE OF THE         *
                                ;* FOLLOWING CBM MODELS:               *
                                ;*   COMMODORE 64 OR MODIFED VIC-40    *
                                ;* COPYRIGHT (C) 1982 BY               *
                                ;* COMMODORE BUSINESS MACHINES (CBM)   *
                                ;***************************************
                                ;****LISTING DATE --1200 14 MAY 1982****
                                ;***************************************
                                ;* THIS SOFTWARE IS FURNISHED FOR USE  *
                                ;* USE IN THE VIC OR COMMODORE COMPUTER*
                                ;* SERIES ONLY.                        *
                                ;*                                     *
                                ;* COPIES THEREOF MAY NOT BE PROVIDED  *
                                ;* OR MADE AVAILABLE FOR USE ON ANY    *
                                ;* OTHER SYSTEM.                       *
                                ;*                                     *
                                ;* THE INFORMATION IN THIS DOCUMENT IS *
                                ;* SUBJECT TO CHANGE WITHOUT NOTICE.   *
                                ;*                                     *
                                ;* NO RESPONSIBILITY IS ASSUMED FOR    *
                                ;* RELIABILITY OF THIS SOFTWARE. RSR   *
                                ;*                                     *
                                ;***************************************
                                .END
                                .LIB   DECLARE
                                *=$0000                ;DECLARE 6510 PORTS
                                D6510  *=*+1           ;6510 DATA DIRECTION REGISTER
                                R6510  *=*+1           ;6510 DATA REGISTER
                                *=$0002                ;MISS 6510 REGS
                                ;VIRTUAL REGS FOR MACHINE LANGUAGE MONITOR
                                PCH    *=*+1
                                PCL    *=*+1
                                FLGS   *=*+1
                                ACC    *=*+1
                                XR     *=*+1
                                YR     *=*+1
                                SP     *=*+1
                                INVH   *=*+1           ;USER MODIFIABLE IRQ
                                INVL   *=*+1
                                *      =$90
                                STATUS *=*+1           ;I/O OPERATION STATUS BYTE
                                ; CRFAC *=*+2 ;CORRECTION FACTOR (UNUSED)
                                STKEY  *=*+1           ;STOP KEY FLAG
                                SVXT   *=*+1           ;TEMPORARY
                                VERCK  *=*+1           ;LOAD OR VERIFY FLAG
                                C3P0   *=*+1           ;IEEE BUFFERED CHAR FLAG
                                BSOUR  *=*+1           ;CHAR BUFFER FOR IEEE
                                SYNO   *=*+1           ;CASSETTE SYNC #
                                XSAV   *=*+1           ;TEMP FOR BASIN
                                LDTND  *=*+1           ;INDEX TO LOGICAL FILE
                                DFLTN  *=*+1           ;DEFAULT INPUT DEVICE #
                                DFLTO  *=*+1           ;DEFAULT OUTPUT DEVICE #
                                PRTY   *=*+1           ;CASSETTE PARITY
                                DPSW   *=*+1           ;CASSETTE DIPOLE SWITCH
                                MSGFLG *=*+1           ;OS MESSAGE FLAG
                                PTR1                   ;CASSETTE ERROR PASS1
                                T1     *=*+1           ;TEMPORARY 1
                                TMPC
                                PTR2                   ;CASSETTE ERROR PASS2
                                T2     *=*+1           ;TEMPORARY 2
                                TIME   *=*+3           ;24 HOUR CLOCK IN 1/60TH SECONDS
                                R2D2                   ;SERIAL BUS USAGE
                                PCNTR  *=*+1           ;CASSETTE STUFF
                                ; PTCH *=*+1  (UNUSED)
                                BSOUR1                 ;TEMP USED BY SERIAL ROUTINE
                                FIRT   *=*+1
                                COUNT                  ;TEMP USED BY SERIAL ROUTINE
                                CNTDN  *=*+1           ;CASSETTE SYNC COUNTDOWN
                                BUFPT  *=*+1           ;CASSETTE BUFFER POINTER
                                INBIT                  ;RS-232 RCVR INPUT BIT STORAGE
                                SHCNL  *=*+1           ;CASSETTE SHORT COUNT
                                BITCI                  ;RS-232 RCVR BIT COUNT IN
                                RER    *=*+1           ;CASSETTE READ ERROR
                                RINONE                 ;RS-232 RCVR FLAG FOR START BIT CHECK
                                REZ    *=*+1           ;CASSETE READING ZEROES
                                RIDATA                 ;RS-232 RCVR BYTE BUFFER
                                RDFLG  *=*+1           ;CASSETTE READ MODE
                                RIPRTY                 ;RS-232 RCVR PARITY STORAGE
                                SHCNH  *=*+1           ;CASSETTE SHORT CNT
                                SAL    *=*+1
                                SAH    *=*+1
                                EAL    *=*+1
                                EAH    *=*+1
                                CMP0   *=*+1
                                TEMP   *=*+1
                                TAPE1  *=*+2           ;ADDRESS OF TAPE BUFFER #1Y.
                                BITTS                  ;RS-232 TRNS BIT COUNT
                                SNSW1  *=*+1
                                NXTBIT                 ;RS-232 TRNS NEXT BIT TO BE SENT
                                DIFF   *=*+1
                                RODATA                 ;RS-232 TRNS BYTE BUFFER
                                PRP    *=*+1
                                FNLEN  *=*+1           ;LENGTH CURRENT FILE N STR
                                LA     *=*+1           ;CURRENT FILE LOGICAL ADDR
                                SA     *=*+1           ;CURRENT FILE 2ND ADDR
                                FA     *=*+1           ;CURRENT FILE PRIMARY ADDR
                                FNADR  *=*+2           ;ADDR CURRENT FILE NAME STR
                                ROPRTY                 ;RS-232 TRNS PARITY BUFFER
                                OCHAR  *=*+1
                                FSBLK  *=*+1           ;CASSETTE READ BLOCK COUNT
                                MYCH   *=*+1
                                CAS1   *=*+1           ;CASSETTE MANUAL/CONTROLLED SWITCH
                                TMP0
                                STAL   *=*+1
                                STAH   *=*+1
                                MEMUSS                 ;CASSETTE LOAD TEMPS (2 BYTES)
                                TMP2   *=*+2
                                ;
                                ;VARIABLES FOR SCREEN EDITOR
                                ;
                                LSTX   *=*+1           ;KEY SCAN INDEX
                                ; SFST *=*+1 ;KEYBOARD SHIFT FLAG (UNUSED)
                                NDX    *=*+1           ;INDEX TO KEYBOARD Q
                                RVS    *=*+1           ;RVS FIELD ON FLAG
                                INDX   *=*+1
                                LSXP   *=*+1           ;X POS AT START
                                LSTP   *=*+1
                                SFDX   *=*+1           ;SHIFT MODE ON PRINT
                                BLNSW  *=*+1           ;CURSOR BLINK ENAB
                                BLNCT  *=*+1           ;COUNT TO TOGGLE CUR
                                GDBLN  *=*+1           ;CHAR BEFORE CURSOR
                                BLNON  *=*+1           ;ON/OFF BLINK FLAG
                                CRSW   *=*+1           ;INPUT VS GET FLAG
                                PNT    *=*+2           ;POINTER TO ROW
                                ; POINT *=*+1   (UNUSED)
                                PNTR   *=*+1           ;POINTER TO COLUMN
                                QTSW   *=*+1           ;QUOTE SWITCH
                                LNMX   *=*+1           ;40/80 MAX POSITON
                                TBLX   *=*+1
                                DATA   *=*+1
                                INSRT  *=*+1           ;INSERT MODE FLAG
                                LDTB1  *=*+26          ;LINE FLAGS+ENDSPACE
                                USER   *=*+2           ;SCREEN EDITOR COLOR IP
                                KEYTAB *=*+2           ;KEYSCAN TABLE INDIRECT
                                ;RS-232 Z-PAGE
                                RIBUF  *=*+2           ;RS-232 INPUT BUFFER POINTER
                                ROBUF  *=*+2           ;RS-232 OUTPUT BUFFER POINTER
                                FREKZP *=*+4           ;FREE KERNAL ZERO PAGE 9/24/80
                                BASZPT *=*+1           ;LOCATION ($00FF) USED BY BASIC
                                *=$100 
                                BAD    *=*+1
                                *=$200
                                BUF    *=*+89          ;BASIC/MONITOR BUFFER
                                ; TABLES FOR OPEN FILES
                                ;
                                LAT    *=*+10          ;LOGICAL FILE NUMBERS
                                FAT    *=*+10          ;PRIMARY DEVICE NUMBERS
                                SAT    *=*+10          ;SECONDARY ADDRESSES
                                ; SYSTEM STORAGE
                                ;
                                KEYD   *=*+10          ;IRQ KEYBOARD BUFFER
                                MEMSTR *=*+2           ;START OF MEMORY
                                MEMSIZ *=*+2           ;TOP OF MEMORY
                                TIMOUT *=*+1           ;IEEE TIMEOUT FLAG
                                ; SCREEN EDITOR STORAGE
                                ;
                                COLOR  *=*+1           ;ACTIV COLOR NYBBLE
                                GDCOL  *=*+1           ;ORIGINAL COLOR BEFORE CURSOR
                                HIBASE *=*+1           ;BASE LOCATION OF SCREEN (TOP)
                                XMAX   *=*+1
                                RPTFLG *=*+1           ;KEY REPEAT FLAG
                                KOUNT  *=*+1
                                DELAY  *=*+1
                                SHFLAG *=*+1           ;SHIFT FLAG BYTE
                                LSTSHF *=*+1           ;LAST SHIFT PATTERN
                                KEYLOG *=*+2           ;INDIRECT FOR KEYBOARD TABLE SETUP
                                MODE   *=*+1           ;0-PET MODE, 1-CATTACANNA
                                AUTODN *=*+1           ;AUTO SCROLL DOWN FLAG(=0 ON,<>0 OFF)
                                ; RS-232 STORAGE
                                ;
                                M51CTR *=*+1           ;6551 CONTROL REGISTER
                                M51CDR *=*+1           ;6551 COMMAND REGISTER
                                M51AJB *=*+2           ;NON STANDARD (BITTIME/2-100)
                                RSSTAT *=*+1           ; RS-232 STATUS REGISTER
                                BITNUM *=*+1           ;NUMBER OF BITS TO SEND (FAST RESPONSE)
                                BAUDOF *=*+2           ;BAUD RATE FULL BIT TIME (CREATED BY OPEN)
                                ;
                                ; RECIEVER STORAGE
                                ;
                                ; INBIT *=*+1 ;INPUT BIT STORAGE
                                ; BITCI *=*+1 ;BIT COUNT IN
                                ; RINONE *=*+1 ;FLAG FOR START BIT CHECK
                                ; RIDATA *=*+1 ;BYTE IN BUFFER
                                ; RIPRTY *=*+1 ;BYTE IN PARITY STORAGE
                                RIDBE  *=*+1           ;INPUT BUFFER INDEX TO END
                                RIDBS  *=*+1           ;INPUT BUFFER POINTER TO START
                                ;
                                ; TRANSMITTER STORAGE
                                ;
                                ; BITTS *=*+1 ;# OF BITS TO BE SENT
                                ; NXTBIT *=*+1 ;NEXT BIT TO BE SENT
                                ; ROPRTY *=*+1 ;PARITY OF BYTE SENT
                                ; RODATA *=*+1 ;BYTE BUFFER OUT
                                RODBS  *=*+1           ;OUTPUT BUFFER INDEX TO START
                                RODBE  *=*+1           ;OUTPUT BUFFER INDEX TO END
                                ;
                                IRQTMP *=*+2           ;HOLDS IRQ DURING TAPE OPS
                                ;
                                ; TEMP SPACE FOR VIC-40 VARIABLES ****
                                ;
                                ENABL  *=*+1           ;RS-232 ENABLES (REPLACES IER)
                                CASTON *=*+1           ;TOD SENSE DURING CASSETTES
                                KIKA26 *=*+1           ;TEMP STORAGE FOR CASSETTE READ ROUTINE
                                STUPID *=*+1           ;TEMP D1IRQ INDICATOR FOR CASSETTE READ
                                LINTMP *=*+1           ;TEMPORARY FOR LINE INDEX
                                *=$0300                ;REM PROGRAM INDIRECTS(10)
                                *=$0300+20             ;REM KERNAL/OS INDIRECTS(20)
                                CINV   *=*+2           ;IRQ RAM VECTOR
                                CBINV  *=*+2           ;BRK INSTR RAM VECTOR
                                NMINV  *=*+2           ;NMI RAM VECTOR
                                IOPEN  *=*+2           ;INDIRECTS FOR CODE
                                ICLOSE *=*+2           ; CONFORMS TO KERNAL SPEC 8/19/80
                                ICHKIN *=*+2
                                ICKOUT *=*+2
                                ICLRCH *=*+2
                                IBASIN *=*+2
                                IBSOUT *=*+2
                                ISTOP  *=*+2
                                IGETIN *=*+2
                                ICLALL *=*+2
                                USRCMD *=*+2
                                ILOAD  *=*+2
                                ISAVE  *=*+2           ;SAVESP
                                *=$0300+60
                                TBUFFR *=*+192         ;CASSETTE DATA BUFFER
                                *      =$400
                                VICSCN *=*+1024
                                RAMLOC
                                ; I/O DEVICES
                                ;
                                *      =$D000
                                VICREG =*              ;VIC REGISTERS
                                *      =$D400
                                SIDREG =*              ;SID REGISTERS
                                *      =$D800
                                VICCOL *=*+1024        ;VIC COLOR NYBBLES
                                *      =$DC00          ;DEVICE1 6526 (PAGE1 IRQ)
                                COLM                   ;KEYBOARD MATRIX
                                D1PRA  *=*+1
                                ROWS                   ;KEYBOARD MATRIX
                                D1PRB  *=*+1
                                D1DDRA *=*+1
                                D1DDRB *=*+1
                                D1T1L  *=*+1
                                D1T1H  *=*+1
                                D1T2L  *=*+1
                                D1T2H  *=*+1
                                D1TOD1 *=*+1
                                D1TODS *=*+1
                                D1TODM *=*+1
                                D1TODH *=*+1
                                D1SDR  *=*+1
                                D1ICR  *=*+1
                                D1CRA  *=*+1
                                D1CRB  *=*+1
                                *      =$DD00          ;DEVICE2 6526 (PAGE2 NMI)
                                D2PRA  *=*+1
                                D2PRB  *=*+1
                                D2DDRA *=*+1
                                D2DDRB *=*+1
                                D2T1L  *=*+1
                                D2T1H  *=*+1
                                D2T2L  *=*+1
                                D2T2H  *=*+1
                                D2TOD1 *=*+1
                                D2TODS *=*+1
                                D2TODM *=*+1
                                D2TODH *=*+1
                                D2SDR  *=*+1
                                D2ICR  *=*+1
                                D2CRA  *=*+1
                                D2CRB  *=*+1
                                TIMRB  =$19            ;6526 CRB ENABLE ONE-SHOT TB
                                ;TAPE BLOCK TYPES
                                ;
                                EOT    =5              ;END OF TAPE
                                BLF    =1              ;BASIC LOAD FILE
                                BDF    =2              ;BASIC DATA FILE
                                PLF    =3              ;FIXED PROGRAM TYPE
                                BDFH   =4              ;BASIC DATA FILE HEADER
                                BUFSZ  =192            ;BUFFER SIZE
                                ;
                                ;SCREEN EDITOR CONSTANTS
                                ;
                                LLEN   =40             ;SINGLE LINE 40 COLUMNS
                                LLEN2  =80             ;DOUBLE LINE = 80 COLUMNS
                                NLINES =25             ;25 ROWS ON SCREEN
                                WHITE  =$01            ;WHITE SCREEN COLOR
                                BLUE   =$06            ;BLUE CHAR COLOR
                                CR     =$D             ;CARRIAGE RETURN
                                .END
                                *=$E500                ;START OF VIC-40 KERNAL

                                .LIB   EDITOR.1
                                MAXCHR=80
                                NWRAP=2                ;MAX NUMBER OF PHYSICAL LINES PER LOGICAL LINE
                                ;
                                ;UNDEFINED FUNCTION ENTRY
                                ;
                                ; UNDEFD LDX #0
                                ; UNDEF2 LDA UNMSG,X
                                ; JSR PRT
                                ; INX
                                ; CPX #UNMSG2-UNMSG
                                ; BNE UNDEF2
                                ; SEC
                                ; RTS
                                ;
                                ; UNMSG .BYT $D,'?ADVANCED FUNCTION NOT AVAILABLE',$D
                                ; UNMSG2
                                ;
                                ;RETURN ADDRESS OF 6526
                                ;
.,E500 A2 00    LDX #$00        IOBASE LDX #<D1PRA
.,E502 A0 DC    LDY #$DC        LDY    #>D1PRA
.,E504 60       RTS             RTS
                                ;
                                ;RETURN MAX ROWS,COLS OF SCREEN
                                ;
.,E505 A2 28    LDX #$28        SCRORG LDX #LLEN
.,E507 A0 19    LDY #$19        LDY    #NLINES
.,E509 60       RTS             RTS
                                ;
                                ;READ/PLOT CURSOR POSITION
                                ;
.,E50A B0 07    BCS $E513       PLOT   BCS PLOT10
.,E50C 86 D6    STX $D6         STX    TBLX
.,E50E 84 D3    STY $D3         STY    PNTR
.,E510 20 6C E5 JSR $E56C       JSR    STUPT
.,E513 A6 D6    LDX $D6         PLOT10 LDX TBLX
.,E515 A4 D3    LDY $D3         LDY    PNTR
.,E517 60       RTS             RTS
                                ;INITIALIZE I/O
                                ;
                                CINT
                                ;
                                ; ESTABLISH SCREEN MEMORY
                                ;
.,E518 20 A0 E5 JSR $E5A0              JSR PANIC       ;SET UP VIC
                                ;
.,E51B A9 00    LDA #$00               LDA #0          ;MAKE SURE WE'RE IN PET MODE
.,E51D 8D 91 02 STA $0291              STA MODE
.,E520 85 CF    STA $CF                STA BLNON       ;WE DONT HAVE A GOOD CHAR FROM THE SCREEN YET
.,E522 A9 48    LDA #$48               LDA #<SHFLOG    ;SET SHIFT LOGIC INDIRECTS
.,E524 8D 8F 02 STA $028F              STA KEYLOG
.,E527 A9 EB    LDA #$EB               LDA #>SHFLOG
.,E529 8D 90 02 STA $0290              STA KEYLOG+1
.,E52C A9 0A    LDA #$0A               LDA #10
.,E52E 8D 89 02 STA $0289              STA XMAX        ;MAXIMUM TYPE AHEAD BUFFER SIZE
.,E531 8D 8C 02 STA $028C              STA DELAY
.,E534 A9 0E    LDA #$0E               LDA #$E         ;INIT COLOR TO LIGHT BLUE<<<<<<<<<<
.,E536 8D 86 02 STA $0286              STA COLOR
.,E539 A9 04    LDA #$04               LDA #4
.,E53B 8D 8B 02 STA $028B              STA KOUNT       ;DELAY BETWEEN KEY REPEATS
.,E53E A9 0C    LDA #$0C               LDA #$C
.,E540 85 CD    STA $CD                STA BLNCT
.,E542 85 CC    STA $CC                STA BLNSW
.,E544 AD 88 02 LDA $0288              CLSR LDA HIBASE ;FILL HI BYTE PTR TABLE
.,E547 09 80    ORA #$80               ORA #$80
.,E549 A8       TAY                    TAY
.,E54A A9 00    LDA #$00               LDA #0
.,E54C AA       TAX                    TAX
.,E54D 94 D9    STY $D9,X              LPS1 STY LDTB1,X
.,E54F 18       CLC                    CLC
.,E550 69 28    ADC #$28               ADC #LLEN
.,E552 90 01    BCC $E555              BCC LPS2
.,E554 C8       INY                    INY             ;CARRY BUMP HI BYTE
.,E555 E8       INX                    LPS2 INX
.,E556 E0 1A    CPX #$1A               CPX #NLINES+1   ;DONE # OF LINES?
.,E558 D0 F3    BNE $E54D              BNE LPS1        ;NO...
.,E55A A9 FF    LDA #$FF               LDA #$FF        ;TAG END OF LINE TABLE
.,E55C 95 D9    STA $D9,X              STA LDTB1,X
.,E55E A2 18    LDX #$18               LDX #NLINES-1   ;CLEAR FROM THE BOTTOM LINE UP
.,E560 20 FF E9 JSR $E9FF       CLEAR1 JSR CLRLN       ;SEE SCROLL ROUTINES
.,E563 CA       DEX                    DEX
.,E564 10 FA    BPL $E560              BPL CLEAR1
                                ;HOME FUNCTION
                                ;
.,E566 A0 00    LDY #$00        NXTD   LDY #0
.,E568 84 D3    STY $D3         STY    PNTR            ;LEFT COLUMN
.,E56A 84 D6    STY $D6         STY    TBLX            ;TOP LINE
                                ;
                                ;MOVE CURSOR TO TBLX,PNTR
                                ;
                                STUPT
.,E56C A6 D6    LDX $D6                LDX TBLX        ;GET CURENT LINE INDEX
.,E56E A5 D3    LDA $D3                LDA PNTR        ;GET CHARACTER POINTER
.,E570 B4 D9    LDY $D9,X       FNDSTR LDY LDTB1,X     ;FIND BEGINING OF LINE
.,E572 30 08    BMI $E57C              BMI STOK        ;BRANCH IF START FOUND
.,E574 18       CLC                    CLC
.,E575 69 28    ADC #$28               ADC #LLEN       ;ADJUST POINTER
.,E577 85 D3    STA $D3                STA PNTR
.,E579 CA       DEX                    DEX
.,E57A 10 F4    BPL $E570              BPL FNDSTR
                                ;
.,E57C 20 F0 E9 JSR $E9F0       STOK   JSR SETPNT      ;SET UP PNT INDIRECT 901227-03**********
                                ;
.,E57F A9 27    LDA #$27               LDA #LLEN-1
.,E581 E8       INX                    INX
.,E582 B4 D9    LDY $D9,X       FNDEND LDY LDTB1,X
.,E584 30 06    BMI $E58C              BMI STDONE
.,E586 18       CLC                    CLC
.,E587 69 28    ADC #$28               ADC #LLEN
.,E589 E8       INX                    INX
.,E58A 10 F6    BPL $E582              BPL FNDEND
                                STDONE
.,E58C 85 D5    STA $D5                STA LNMX
.,E58E 4C 24 EA JMP $EA24              JMP SCOLOR      ;MAKE COLOR POINTER FOLLOW 901227-03**********
                                ; THIS IS A PATCH FOR INPUT LOGIC 901227-03**********
                                ;   FIXES INPUT"XXXXXXX-40-XXXXX";A$ PROBLEM
                                ;
.,E591 E4 C9    CPX $C9         FINPUT CPX LSXP        ;CHECK IF ON SAME LINE
.,E593 F0 03    BEQ $E598              BEQ FINPUX      ;YES..RETURN TO SEND
.,E595 4C ED E6 JMP $E6ED              JMP FINDST      ;CHECK IF WE WRAPPED DOWN...
.,E598 60       RTS             FINPUX RTS
.,E599 EA       NOP                    NOP             ;KEEP THE SPACE THE SAME...
                                ;PANIC NMI ENTRY
                                ;
.,E59A 20 A0 E5 JSR $E5A0       VPAN   JSR PANIC       ;FIX VIC SCREEN
.,E59D 4C 66 E5 JMP $E566       JMP    NXTD            ;HOME CURSOR
.,E5A0 A9 03    LDA #$03        PANIC  LDA #3          ;RESET DEFAULT I/O
.,E5A2 85 9A    STA $9A         STA    DFLTO
.,E5A4 A9 00    LDA #$00        LDA    #0
.,E5A6 85 99    STA $99         STA    DFLTN
                                ;INIT VIC
                                ;
.,E5A8 A2 2F    LDX #$2F        INITV  LDX #47         ;LOAD ALL VIC REGS ***
.,E5AA BD B8 EC LDA $ECB8,X     PX4    LDA TVIC-1,X
.,E5AD 9D FF CF STA $CFFF,X            STA VICREG-1,X
.,E5B0 CA       DEX             DEX
.,E5B1 D0 F7    BNE $E5AA       BNE    PX4
.,E5B3 60       RTS             RTS
                                ;
                                ;REMOVE CHARACTER FROM QUEUE
                                ;
.,E5B4 AC 77 02 LDY $0277       LP2    LDY KEYD
.,E5B7 A2 00    LDX #$00        LDX    #0
.,E5B9 BD 78 02 LDA $0278,X     LP1    LDA KEYD+1,X
.,E5BC 9D 77 02 STA $0277,X     STA    KEYD,X
.,E5BF E8       INX             INX
.,E5C0 E4 C6    CPX $C6         CPX    NDX
.,E5C2 D0 F5    BNE $E5B9       BNE    LP1
.,E5C4 C6 C6    DEC $C6         DEC    NDX
.,E5C6 98       TYA             TYA
.,E5C7 58       CLI             CLI
.,E5C8 18       CLC             CLC                    ;GOOD RETURN
.,E5C9 60       RTS             RTS
                                ;
.,E5CA 20 16 E7 JSR $E716       LOOP4  JSR PRT
                                LOOP3
.,E5CD A5 C6    LDA $C6         LDA    NDX
.,E5CF 85 CC    STA $CC         STA    BLNSW
.,E5D1 8D 92 02 STA $0292       STA    AUTODN          ;TURN ON AUTO SCROLL DOWN
.,E5D4 F0 F7    BEQ $E5CD       BEQ    LOOP3
.,E5D6 78       SEI             SEI
.,E5D7 A5 CF    LDA $CF         LDA    BLNON
.,E5D9 F0 0C    BEQ $E5E7       BEQ    LP21
.,E5DB A5 CE    LDA $CE         LDA    GDBLN
.,E5DD AE 87 02 LDX $0287       LDX    GDCOL           ;RESTORE ORIGINAL COLOR
.,E5E0 A0 00    LDY #$00        LDY    #0
.,E5E2 84 CF    STY $CF         STY    BLNON
.,E5E4 20 13 EA JSR $EA13       JSR    DSPP
.,E5E7 20 B4 E5 JSR $E5B4       LP21   JSR LP2
.,E5EA C9 83    CMP #$83        CMP    #$83            ;RUN KEY?
.,E5EC D0 10    BNE $E5FE              BNE LP22
.,E5EE A2 09    LDX #$09               LDX #9
.,E5F0 78       SEI                    SEI
.,E5F1 86 C6    STX $C6                STX NDX
.,E5F3 BD E6 EC LDA $ECE6,X     LP23   LDA RUNTB-1,X
.,E5F6 9D 76 02 STA $0276,X            STA KEYD-1,X
.,E5F9 CA       DEX                    DEX
.,E5FA D0 F7    BNE $E5F3              BNE LP23
.,E5FC F0 CF    BEQ $E5CD              BEQ LOOP3
.,E5FE C9 0D    CMP #$0D        LP22   CMP #$D
.,E600 D0 C8    BNE $E5CA       BNE    LOOP4
.,E602 A4 D5    LDY $D5         LDY    LNMX
.,E604 84 D0    STY $D0         STY    CRSW
.,E606 B1 D1    LDA ($D1),Y     CLP5   LDA (PNT)Y
.,E608 C9 20    CMP #$20        CMP    #'
.,E60A D0 03    BNE $E60F       BNE    CLP6
.,E60C 88       DEY             DEY
.,E60D D0 F7    BNE $E606       BNE    CLP5
.,E60F C8       INY             CLP6   INY
.,E610 84 C8    STY $C8         STY    INDX
.,E612 A0 00    LDY #$00        LDY    #0
.,E614 8C 92 02 STY $0292              STY AUTODN      ;TURN OFF AUTO SCROLL DOWN
.,E617 84 D3    STY $D3         STY    PNTR
.,E619 84 D4    STY $D4         STY    QTSW
.,E61B A5 C9    LDA $C9         LDA    LSXP
.,E61D 30 1B    BMI $E63A       BMI    LOP5
.,E61F A6 D6    LDX $D6                LDX TBLX
.,E621 20 ED E6 JSR $E6ED              JSR FINDST      ;FIND 1ST PHYSICAL LINE
.,E624 E4 C9    CPX $C9                CPX LSXP
.,E626 D0 12    BNE $E63A       BNE    LOP5
.,E628 A5 CA    LDA $CA         LDA    LSTP
.,E62A 85 D3    STA $D3         STA    PNTR
.,E62C C5 C8    CMP $C8         CMP    INDX
.,E62E 90 0A    BCC $E63A       BCC    LOP5
.,E630 B0 2B    BCS $E65D       BCS    CLP2
                                ;INPUT A LINE UNTIL CARRIAGE RETURN
                                ;
.,E632 98       TYA             LOOP5  TYA
.,E633 48       PHA             PHA
.,E634 8A       TXA             TXA
.,E635 48       PHA             PHA
.,E636 A5 D0    LDA $D0         LDA    CRSW
.,E638 F0 93    BEQ $E5CD       BEQ    LOOP3
.,E63A A4 D3    LDY $D3         LOP5   LDY PNTR
.,E63C B1 D1    LDA ($D1),Y     LDA    (PNT)Y
                                NOTONE
.,E63E 85 D7    STA $D7         STA    DATA
.,E640 29 3F    AND #$3F        LOP51  AND #$3F
.,E642 06 D7    ASL $D7         ASL    DATA
.,E644 24 D7    BIT $D7         BIT    DATA
.,E646 10 02    BPL $E64A       BPL    LOP54
.,E648 09 80    ORA #$80        ORA    #$80
.,E64A 90 04    BCC $E650       LOP54  BCC LOP52
.,E64C A6 D4    LDX $D4         LDX    QTSW
.,E64E D0 04    BNE $E654       BNE    LOP53
.,E650 70 02    BVS $E654       LOP52  BVS LOP53
.,E652 09 40    ORA #$40        ORA    #$40
.,E654 E6 D3    INC $D3         LOP53  INC PNTR
.,E656 20 84 E6 JSR $E684       JSR    QTSWC
.,E659 C4 C8    CPY $C8         CPY    INDX
.,E65B D0 17    BNE $E674       BNE    CLP1
.,E65D A9 00    LDA #$00        CLP2   LDA #0
.,E65F 85 D0    STA $D0         STA    CRSW
.,E661 A9 0D    LDA #$0D        LDA    #$D
.,E663 A6 99    LDX $99         LDX    DFLTN           ;FIX GETS FROM SCREEN
.,E665 E0 03    CPX #$03        CPX    #3              ;IS IT THE SCREEN?
.,E667 F0 06    BEQ $E66F       BEQ    CLP2A
.,E669 A6 9A    LDX $9A         LDX    DFLTO
.,E66B E0 03    CPX #$03        CPX    #3
.,E66D F0 03    BEQ $E672       BEQ    CLP21
.,E66F 20 16 E7 JSR $E716       CLP2A  JSR PRT
.,E672 A9 0D    LDA #$0D        CLP21  LDA #$D
.,E674 85 D7    STA $D7         CLP1   STA DATA
.,E676 68       PLA             PLA
.,E677 AA       TAX             TAX
.,E678 68       PLA             PLA
.,E679 A8       TAY             TAY
.,E67A A5 D7    LDA $D7         LDA    DATA
.,E67C C9 DE    CMP #$DE        CMP    #$DE            ;IS IT <PI> ?
.,E67E D0 02    BNE $E682       BNE    CLP7
.,E680 A9 FF    LDA #$FF        LDA    #$FF
.,E682 18       CLC             CLP7   CLC
.,E683 60       RTS             RTS
.,E684 C9 22    CMP #$22        QTSWC  CMP #$22
.,E686 D0 08    BNE $E690       BNE    QTSWL
.,E688 A5 D4    LDA $D4         LDA    QTSW
.,E68A 49 01    EOR #$01        EOR    #$1
.,E68C 85 D4    STA $D4         STA    QTSW
.,E68E A9 22    LDA #$22        LDA    #$22
.,E690 60       RTS             QTSWL  RTS
.,E691 09 40    ORA #$40        NXT33  ORA #$40
.,E693 A6 C7    LDX $C7         NXT3   LDX RVS
.,E695 F0 02    BEQ $E699       BEQ    NVS
.,E697 09 80    ORA #$80        NC3    ORA #$80
.,E699 A6 D8    LDX $D8         NVS    LDX INSRT
.,E69B F0 02    BEQ $E69F       BEQ    NVS1
.,E69D C6 D8    DEC $D8         DEC    INSRT
.,E69F AE 86 02 LDX $0286       NVS1   LDX COLOR PUT COLOR ON SCREEN
.,E6A2 20 13 EA JSR $EA13       JSR    DSPP
.,E6A5 20 B6 E6 JSR $E6B6              JSR WLOGIC      ;CHECK FOR WRAPAROUND
.,E6A8 68       PLA             LOOP2  PLA
.,E6A9 A8       TAY             TAY
.,E6AA A5 D8    LDA $D8         LDA    INSRT
.,E6AC F0 02    BEQ $E6B0       BEQ    LOP2
.,E6AE 46 D4    LSR $D4         LSR    QTSW
.,E6B0 68       PLA             LOP2   PLA
.,E6B1 AA       TAX             TAX
.,E6B2 68       PLA             PLA
.,E6B3 18       CLC             CLC                    ;GOOD RETURN
.,E6B4 58       CLI             CLI
.,E6B5 60       RTS             RTS
                                WLOGIC
.,E6B6 20 B3 E8 JSR $E8B3              JSR CHKDWN      ;MAYBE WE SHOULD WE INCREMENT TBLX
.,E6B9 E6 D3    INC $D3                INC PNTR        ;BUMP CHARCTER POINTER
.,E6BB A5 D5    LDA $D5                LDA LNMX        ;
.,E6BD C5 D3    CMP $D3                CMP PNTR        ;IF LNMX IS LESS THAN PNTR
.,E6BF B0 3F    BCS $E700              BCS WLGRTS      ;BRANCH IF LNMX>=PNTR
.,E6C1 C9 4F    CMP #$4F               CMP #MAXCHR-1   ;PAST MAX CHARACTERS
.,E6C3 F0 32    BEQ $E6F7              BEQ WLOG10      ;BRANCH IF SO
.,E6C5 AD 92 02 LDA $0292              LDA AUTODN      ;SHOULD WE AUTO SCROLL DOWN?
.,E6C8 F0 03    BEQ $E6CD              BEQ WLOG20      ;BRANCH IF NOT
.,E6CA 4C 67 E9 JMP $E967       JMP    BMT1            ;ELSE DECIDE WHICH WAY TO SCROLL
                                WLOG20
.,E6CD A6 D6    LDX $D6                LDX TBLX        ;SEE IF WE SHOULD SCROLL DOWN
.,E6CF E0 19    CPX #$19               CPX #NLINES
.,E6D1 90 07    BCC $E6DA              BCC WLOG30      ;BRANCH IF NOT
.,E6D3 20 EA E8 JSR $E8EA              JSR SCROL       ;ELSE DO THE SCROL UP
.,E6D6 C6 D6    DEC $D6                DEC TBLX        ;AND ADJUST CURENT LINE#
.,E6D8 A6 D6    LDX $D6                LDX TBLX
.,E6DA 16 D9    ASL $D9,X       WLOG30 ASL LDTB1,X     ;WRAP THE LINE
.,E6DC 56 D9    LSR $D9,X              LSR LDTB1,X
.,E6DE E8       INX                    INX             ;INDEX TO NEXT LLINE
.,E6DF B5 D9    LDA $D9,X              LDA LDTB1,X     ;GET HIGH ORDER BYTE OF ADDRESS
.,E6E1 09 80    ORA #$80               ORA #$80        ;MAKE IT A NON-CONTINUATION LINE
.,E6E3 95 D9    STA $D9,X              STA LDTB1,X     ;AND PUT IT BACK
.,E6E5 CA       DEX                    DEX             ;GET BACK TO CURRENT LINE
.,E6E6 A5 D5    LDA $D5                LDA LNMX        ;CONTINUE THE BYTES TAKEN OUT
.,E6E8 18       CLC                    CLC
.,E6E9 69 28    ADC #$28               ADC #LLEN
.,E6EB 85 D5    STA $D5                STA LNMX
                                FINDST
.,E6ED B5 D9    LDA $D9,X              LDA LDTB1,X     ;IS THIS THE FIRST LINE?
.,E6EF 30 03    BMI $E6F4              BMI FINX        ;BRANCH IF SO
.,E6F1 CA       DEX                    DEX             ;ELSE BACKUP 1
.,E6F2 D0 F9    BNE $E6ED              BNE FINDST
                                FINX
.,E6F4 4C F0 E9 JMP $E9F0              JMP SETPNT      ;MAKE SURE PNT IS RIGHT
.,E6F7 C6 D6    DEC $D6         WLOG10 DEC TBLX
.,E6F9 20 7C E8 JSR $E87C              JSR NXLN
.,E6FC A9 00    LDA #$00               LDA #0
.,E6FE 85 D3    STA $D3                STA PNTR        ;POINT TO FIRST BYTE
.,E700 60       RTS             WLGRTS RTS
.,E701 A6 D6    LDX $D6         BKLN   LDX TBLX
.,E703 D0 06    BNE $E70B              BNE BKLN1
.,E705 86 D3    STX $D3                STX PNTR
.,E707 68       PLA                    PLA
.,E708 68       PLA                    PLA
.,E709 D0 9D    BNE $E6A8              BNE LOOP2
                                ;
.,E70B CA       DEX             BKLN1  DEX
.,E70C 86 D6    STX $D6                STX TBLX
.,E70E 20 6C E5 JSR $E56C              JSR STUPT
.,E711 A4 D5    LDY $D5                LDY LNMX
.,E713 84 D3    STY $D3                STY PNTR
.,E715 60       RTS                    RTS
                                ;PRINT ROUTINE
                                ;
.,E716 48       PHA             PRT    PHA
.,E717 85 D7    STA $D7         STA    DATA
.,E719 8A       TXA             TXA
.,E71A 48       PHA             PHA
.,E71B 98       TYA             TYA
.,E71C 48       PHA             PHA
.,E71D A9 00    LDA #$00        LDA    #0
.,E71F 85 D0    STA $D0         STA    CRSW
.,E721 A4 D3    LDY $D3         LDY    PNTR
.,E723 A5 D7    LDA $D7         LDA    DATA
.,E725 10 03    BPL $E72A       BPL    *+5
.,E727 4C D4 E7 JMP $E7D4       JMP    NXTX
.,E72A C9 0D    CMP #$0D        CMP    #$D
.,E72C D0 03    BNE $E731       BNE    NJT1
.,E72E 4C 91 E8 JMP $E891       JMP    NXT1
.,E731 C9 20    CMP #$20        NJT1   CMP #'
.,E733 90 10    BCC $E745       BCC    NTCN
.,E735 C9 60    CMP #$60        CMP    #$60            ;LOWER CASE?
.,E737 90 04    BCC $E73D       BCC    NJT8            ;NO...
.,E739 29 DF    AND #$DF        AND    #$DF            ;YES...MAKE SCREEN LOWER
.,E73B D0 02    BNE $E73F       BNE    NJT9            ;ALWAYS
.,E73D 29 3F    AND #$3F        NJT8   AND #$3F
.,E73F 20 84 E6 JSR $E684       NJT9   JSR QTSWC
.,E742 4C 93 E6 JMP $E693       JMP    NXT3
.,E745 A6 D8    LDX $D8         NTCN   LDX INSRT
.,E747 F0 03    BEQ $E74C       BEQ    CNC3X
.,E749 4C 97 E6 JMP $E697       JMP    NC3
.,E74C C9 14    CMP #$14        CNC3X  CMP #$14
.,E74E D0 2E    BNE $E77E       BNE    NTCN1
.,E750 98       TYA             TYA
.,E751 D0 06    BNE $E759       BNE    BAK1UP
.,E753 20 01 E7 JSR $E701              JSR BKLN
.,E756 4C 73 E7 JMP $E773              JMP BK2
.,E759 20 A1 E8 JSR $E8A1       BAK1UP JSR CHKBAK      ;SHOULD WE DEC TBLX
.,E75C 88       DEY                    DEY
.,E75D 84 D3    STY $D3         STY    PNTR
.,E75F 20 24 EA JSR $EA24       BK1    JSR SCOLOR      ;FIX COLOR PTRS
.,E762 C8       INY             BK15   INY
.,E763 B1 D1    LDA ($D1),Y     LDA    (PNT)Y
.,E765 88       DEY             DEY
.,E766 91 D1    STA ($D1),Y     STA    (PNT)Y
.,E768 C8       INY             INY
.,E769 B1 F3    LDA ($F3),Y     LDA    (USER)Y
.,E76B 88       DEY             DEY
.,E76C 91 F3    STA ($F3),Y     STA    (USER)Y
.,E76E C8       INY             INY
.,E76F C4 D5    CPY $D5         CPY    LNMX
.,E771 D0 EF    BNE $E762       BNE    BK15
.,E773 A9 20    LDA #$20        BK2    LDA #'
.,E775 91 D1    STA ($D1),Y     STA    (PNT)Y
.,E777 AD 86 02 LDA $0286       LDA    COLOR
.,E77A 91 F3    STA ($F3),Y     STA    (USER)Y
.,E77C 10 4D    BPL $E7CB       BPL    JPL3
.,E77E A6 D4    LDX $D4         NTCN1  LDX QTSW
.,E780 F0 03    BEQ $E785       BEQ    NC3W
.,E782 4C 97 E6 JMP $E697       CNC3   JMP NC3
.,E785 C9 12    CMP #$12        NC3W   CMP #$12
.,E787 D0 02    BNE $E78B       BNE    NC1
.,E789 85 C7    STA $C7         STA    RVS
.,E78B C9 13    CMP #$13        NC1    CMP #$13
.,E78D D0 03    BNE $E792       BNE    NC2
.,E78F 20 66 E5 JSR $E566       JSR    NXTD
.,E792 C9 1D    CMP #$1D        NC2    CMP #$1D
.,E794 D0 17    BNE $E7AD       BNE    NCX2
.,E796 C8       INY             INY
.,E797 20 B3 E8 JSR $E8B3              JSR CHKDWN
.,E79A 84 D3    STY $D3         STY    PNTR
.,E79C 88       DEY             DEY
.,E79D C4 D5    CPY $D5         CPY    LNMX
.,E79F 90 09    BCC $E7AA       BCC    NCZ2
.,E7A1 C6 D6    DEC $D6                DEC TBLX
.,E7A3 20 7C E8 JSR $E87C       JSR    NXLN
.,E7A6 A0 00    LDY #$00        LDY    #0
.,E7A8 84 D3    STY $D3         JPL4   STY PNTR
.,E7AA 4C A8 E6 JMP $E6A8       NCZ2   JMP LOOP2
.,E7AD C9 11    CMP #$11        NCX2   CMP #$11
.,E7AF D0 1D    BNE $E7CE       BNE    COLR1
.,E7B1 18       CLC             CLC
.,E7B2 98       TYA             TYA
.,E7B3 69 28    ADC #$28        ADC    #LLEN
.,E7B5 A8       TAY             TAY
.,E7B6 E6 D6    INC $D6                INC TBLX
.,E7B8 C5 D5    CMP $D5         CMP    LNMX
.,E7BA 90 EC    BCC $E7A8       BCC    JPL4
.,E7BC F0 EA    BEQ $E7A8       BEQ    JPL4
.,E7BE C6 D6    DEC $D6                DEC TBLX
.,E7C0 E9 28    SBC #$28        CURS10 SBC #LLEN
.,E7C2 90 04    BCC $E7C8              BCC GOTDWN
.,E7C4 85 D3    STA $D3                STA PNTR
.,E7C6 D0 F8    BNE $E7C0              BNE CURS10
.,E7C8 20 7C E8 JSR $E87C       GOTDWN JSR NXLN
.,E7CB 4C A8 E6 JMP $E6A8       JPL3   JMP LOOP2
.,E7CE 20 CB E8 JSR $E8CB       COLR1  JSR CHKCOL      ;CHECK FOR A COLOR
.,E7D1 4C 44 EC JMP $EC44              JMP LOWER       ;WAS JMP LOOP2
                                ;CHECK COLOR
                                ;
                                ;SHIFTED KEYS
                                ;
                                NXTX
                                KEEPIT
.,E7D4 29 7F    AND #$7F        AND    #$7F
.,E7D6 C9 7F    CMP #$7F        CMP    #$7F
.,E7D8 D0 02    BNE $E7DC       BNE    NXTX1
.,E7DA A9 5E    LDA #$5E        LDA    #$5E
                                NXTX1
                                NXTXA
.,E7DC C9 20    CMP #$20               CMP #$20        ;IS IT A FUNCTION KEY
.,E7DE 90 03    BCC $E7E3       BCC    UHUH
.,E7E0 4C 91 E6 JMP $E691       JMP    NXT33
                                UHUH
.,E7E3 C9 0D    CMP #$0D        CMP    #$D
.,E7E5 D0 03    BNE $E7EA       BNE    UP5
.,E7E7 4C 91 E8 JMP $E891       JMP    NXT1
.,E7EA A6 D4    LDX $D4         UP5    LDX  QTSW
.,E7EC D0 3F    BNE $E82D       BNE    UP6
.,E7EE C9 14    CMP #$14        CMP    #$14
.,E7F0 D0 37    BNE $E829       BNE    UP9
.,E7F2 A4 D5    LDY $D5         LDY    LNMX
.,E7F4 B1 D1    LDA ($D1),Y     LDA    (PNT)Y
.,E7F6 C9 20    CMP #$20        CMP    #'
.,E7F8 D0 04    BNE $E7FE       BNE    INS3
.,E7FA C4 D3    CPY $D3         CPY    PNTR
.,E7FC D0 07    BNE $E805       BNE    INS1
.,E7FE C0 4F    CPY #$4F        INS3   CPY #MAXCHR-1
.,E800 F0 24    BEQ $E826       BEQ    INSEXT          ;EXIT IF LINE TOO LONG
.,E802 20 65 E9 JSR $E965       JSR    NEWLIN          ;SCROLL DOWN 1
.,E805 A4 D5    LDY $D5         INS1   LDY LNMX
.,E807 20 24 EA JSR $EA24       JSR    SCOLOR
.,E80A 88       DEY             INS2   DEY
.,E80B B1 D1    LDA ($D1),Y     LDA    (PNT)Y
.,E80D C8       INY             INY
.,E80E 91 D1    STA ($D1),Y     STA    (PNT)Y
.,E810 88       DEY             DEY
.,E811 B1 F3    LDA ($F3),Y     LDA    (USER)Y
.,E813 C8       INY             INY
.,E814 91 F3    STA ($F3),Y     STA    (USER)Y
.,E816 88       DEY             DEY
.,E817 C4 D3    CPY $D3         CPY    PNTR
.,E819 D0 EF    BNE $E80A       BNE    INS2
.,E81B A9 20    LDA #$20        LDA    #$20
.,E81D 91 D1    STA ($D1),Y     STA    (PNT)Y
.,E81F AD 86 02 LDA $0286       LDA    COLOR
.,E822 91 F3    STA ($F3),Y     STA    (USER)Y
.,E824 E6 D8    INC $D8         INC    INSRT
.,E826 4C A8 E6 JMP $E6A8       INSEXT JMP LOOP2
.,E829 A6 D8    LDX $D8         UP9    LDX INSRT
.,E82B F0 05    BEQ $E832       BEQ    UP2
.,E82D 09 40    ORA #$40        UP6    ORA #$40
.,E82F 4C 97 E6 JMP $E697       JMP    NC3
.,E832 C9 11    CMP #$11        UP2    CMP #$11
.,E834 D0 16    BNE $E84C       BNE    NXT2
.,E836 A6 D6    LDX $D6         LDX    TBLX
.,E838 F0 37    BEQ $E871              BEQ JPL2
.,E83A C6 D6    DEC $D6                DEC TBLX
.,E83C A5 D3    LDA $D3                LDA PNTR
.,E83E 38       SEC                    SEC
.,E83F E9 28    SBC #$28               SBC #LLEN
.,E841 90 04    BCC $E847              BCC UPALIN
.,E843 85 D3    STA $D3                STA PNTR
.,E845 10 2A    BPL $E871              BPL JPL2
.,E847 20 6C E5 JSR $E56C       UPALIN JSR STUPT
.,E84A D0 25    BNE $E871       BNE    JPL2
.,E84C C9 12    CMP #$12        NXT2   CMP #$12
.,E84E D0 04    BNE $E854       BNE    NXT6
.,E850 A9 00    LDA #$00        LDA    #0
.,E852 85 C7    STA $C7         STA    RVS
.,E854 C9 1D    CMP #$1D        NXT6   CMP #$1D
.,E856 D0 12    BNE $E86A       BNE    NXT61
.,E858 98       TYA                    TYA
.,E859 F0 09    BEQ $E864       BEQ    BAKBAK
.,E85B 20 A1 E8 JSR $E8A1       JSR    CHKBAK
.,E85E 88       DEY             DEY
.,E85F 84 D3    STY $D3         STY    PNTR
.,E861 4C A8 E6 JMP $E6A8              JMP LOOP2
.,E864 20 01 E7 JSR $E701       BAKBAK JSR BKLN
.,E867 4C A8 E6 JMP $E6A8       JMP    LOOP2
.,E86A C9 13    CMP #$13        NXT61  CMP #$13
.,E86C D0 06    BNE $E874       BNE    SCCL
.,E86E 20 44 E5 JSR $E544       JSR    CLSR
.,E871 4C A8 E6 JMP $E6A8       JPL2   JMP LOOP2
                                SCCL
.,E874 09 80    ORA #$80        ORA    #$80            ;MAKE IT UPPER CASE
.,E876 20 CB E8 JSR $E8CB       JSR    CHKCOL          ;TRY FOR COLOR
.,E879 4C 4F EC JMP $EC4F              JMP UPPER       ;WAS JMP LOOP2
                                ;
.,E87C 46 C9    LSR $C9         NXLN   LSR LSXP
.,E87E A6 D6    LDX $D6         LDX    TBLX
.,E880 E8       INX             NXLN2  INX
.,E881 E0 19    CPX #$19        CPX    #NLINES         ;OFF BOTTOM?
.,E883 D0 03    BNE $E888       BNE    NXLN1           ;NO...
.,E885 20 EA E8 JSR $E8EA       JSR    SCROL           ;YES...SCROLL
.,E888 B5 D9    LDA $D9,X       NXLN1  LDA LDTB1,X     ;DOUBLE LINE?
.,E88A 10 F4    BPL $E880       BPL    NXLN2           ;YES...SCROLL AGAIN
.,E88C 86 D6    STX $D6         STX    TBLX
.,E88E 4C 6C E5 JMP $E56C       JMP    STUPT
                                NXT1
.,E891 A2 00    LDX #$00        LDX    #0
.,E893 86 D8    STX $D8         STX    INSRT
.,E895 86 C7    STX $C7         STX    RVS
.,E897 86 D4    STX $D4         STX    QTSW
.,E899 86 D3    STX $D3         STX    PNTR
.,E89B 20 7C E8 JSR $E87C       JSR    NXLN
.,E89E 4C A8 E6 JMP $E6A8       JPL5   JMP LOOP2
                                ;
                                ;
                                ; CHECK FOR A DECREMENT TBLX
                                ;
.,E8A1 A2 02    LDX #$02        CHKBAK LDX #NWRAP
.,E8A3 A9 00    LDA #$00               LDA #0
.,E8A5 C5 D3    CMP $D3         CHKLUP CMP PNTR
.,E8A7 F0 07    BEQ $E8B0              BEQ BACK
.,E8A9 18       CLC                    CLC
.,E8AA 69 28    ADC #$28               ADC #LLEN
.,E8AC CA       DEX                    DEX
.,E8AD D0 F6    BNE $E8A5              BNE CHKLUP
.,E8AF 60       RTS                    RTS
                                ;
.,E8B0 C6 D6    DEC $D6         BACK   DEC TBLX
.,E8B2 60       RTS                    RTS
                                ;
                                ; CHECK FOR INCREMENT TBLX
                                ;
.,E8B3 A2 02    LDX #$02        CHKDWN LDX #NWRAP
.,E8B5 A9 27    LDA #$27               LDA #LLEN-1
.,E8B7 C5 D3    CMP $D3         DWNCHK CMP PNTR
.,E8B9 F0 07    BEQ $E8C2              BEQ DNLINE
.,E8BB 18       CLC                    CLC
.,E8BC 69 28    ADC #$28               ADC #LLEN
.,E8BE CA       DEX                    DEX
.,E8BF D0 F6    BNE $E8B7              BNE DWNCHK
.,E8C1 60       RTS                    RTS
                                ;
.,E8C2 A6 D6    LDX $D6         DNLINE LDX TBLX
.,E8C4 E0 19    CPX #$19               CPX #NLINES
.,E8C6 F0 02    BEQ $E8CA              BEQ DWNBYE
.,E8C8 E6 D6    INC $D6                INC TBLX
                                ;
.,E8CA 60       RTS             DWNBYE RTS
                                CHKCOL
.,E8CB A2 0F    LDX #$0F               LDX #15         ;THERE'S 15 COLORS
.,E8CD DD DA E8 CMP $E8DA,X     CHK1A  CMP COLTAB,X
.,E8D0 F0 04    BEQ $E8D6              BEQ CHK1B
.,E8D2 CA       DEX                    DEX
.,E8D3 10 F8    BPL $E8CD              BPL CHK1A
.,E8D5 60       RTS                    RTS
                                ;
                                CHK1B
.,E8D6 8E 86 02 STX $0286              STX COLOR       ;CHANGE THE COLOR
.,E8D9 60       RTS                    RTS
                                COLTAB
                                ;BLK,WHT,RED,CYAN,MAGENTA,GRN,BLUE,YELLOW
.:E8DA 90 05 1C 9F 9C 1E 1F 9E  .BYT   $90,$05,$1C,$9F,$9C,$1E,$1F,$9E
.:E8E2 81 95 96 97 98 99 9A 9B  .BYT   $81,$95,$96,$97,$98,$99,$9A,$9B
                                .END
                                ;.LIB CONKAT (JAPAN CONVERSION TABLES)
                                .LIB   EDITOR.2
                                ;SCREEN SCROLL ROUTINE
                                ;
.,E8EA A5 AC    LDA $AC         SCROL  LDA SAL
.,E8EC 48       PHA             PHA
.,E8ED A5 AD    LDA $AD         LDA    SAH
.,E8EF 48       PHA             PHA
.,E8F0 A5 AE    LDA $AE         LDA    EAL
.,E8F2 48       PHA             PHA
.,E8F3 A5 AF    LDA $AF         LDA    EAH
.,E8F5 48       PHA             PHA
                                ;
                                ;   S C R O L L   U P
                                ;
.,E8F6 A2 FF    LDX #$FF        SCRO0  LDX #$FF
.,E8F8 C6 D6    DEC $D6                DEC TBLX
.,E8FA C6 C9    DEC $C9                DEC LSXP
.,E8FC CE A5 02 DEC $02A5              DEC LINTMP
.,E8FF E8       INX             SCR10  INX             ;GOTO NEXT LINE
.,E900 20 F0 E9 JSR $E9F0              JSR SETPNT      ;POINT TO 'TO' LINE
.,E903 E0 18    CPX #$18               CPX #NLINES-1   ;DONE?
.,E905 B0 0C    BCS $E913              BCS SCR41       ;BRANCH IF SO
                                ;
.,E907 BD F1 EC LDA $ECF1,X            LDA LDTB2+1,X   ;SETUP FROM PNTR
.,E90A 85 AC    STA $AC                STA SAL
.,E90C B5 DA    LDA $DA,X              LDA LDTB1+1,X
.,E90E 20 C8 E9 JSR $E9C8              JSR SCRLIN      ;SCROLL THIS LINE UP1
.,E911 30 EC    BMI $E8FF              BMI SCR10
                                ;
                                SCR41
.,E913 20 FF E9 JSR $E9FF              JSR CLRLN
                                ;
.,E916 A2 00    LDX #$00        LDX    #0              ;SCROLL HI BYTE POINTERS
.,E918 B5 D9    LDA $D9,X       SCRL5  LDA LDTB1,X
.,E91A 29 7F    AND #$7F        AND    #$7F
.,E91C B4 DA    LDY $DA,X       LDY    LDTB1+1,X
.,E91E 10 02    BPL $E922       BPL    SCRL3
.,E920 09 80    ORA #$80        ORA    #$80
.,E922 95 D9    STA $D9,X       SCRL3  STA LDTB1,X
.,E924 E8       INX             INX
.,E925 E0 18    CPX #$18        CPX    #NLINES-1
.,E927 D0 EF    BNE $E918       BNE    SCRL5
                                ;
.,E929 A5 F1    LDA $F1         LDA    LDTB1+NLINES-1
.,E92B 09 80    ORA #$80        ORA    #$80
.,E92D 85 F1    STA $F1         STA    LDTB1+NLINES-1
.,E92F A5 D9    LDA $D9         LDA    LDTB1           ;DOUBLE LINE?
.,E931 10 C3    BPL $E8F6       BPL    SCRO0           ;YES...SCROLL AGAIN
                                ;
.,E933 E6 D6    INC $D6                INC TBLX
.,E935 EE A5 02 INC $02A5              INC LINTMP
.,E938 A9 7F    LDA #$7F               LDA #$7F        ;CHECK FOR CONTROL KEY
.,E93A 8D 00 DC STA $DC00              STA COLM        ;DROP LINE 2 ON PORT B
.,E93D AD 01 DC LDA $DC01              LDA ROWS
.,E940 C9 FB    CMP #$FB               CMP #$FB        ;SLOW SCROLL KEY?(CONTROL)
.,E942 08       PHP                    PHP             ;SAVE STATUS. RESTORE PORT B
.,E943 A9 7F    LDA #$7F               LDA #$7F        ;FOR STOP KEY CHECK
.,E945 8D 00 DC STA $DC00              STA COLM
.,E948 28       PLP                    PLP
.,E949 D0 0B    BNE $E956       BNE    MLP42
                                ;
.,E94B A0 00    LDY #$00        LDY    #0
.,E94D EA       NOP             MLP4   NOP             ;DELAY
.,E94E CA       DEX             DEX
.,E94F D0 FC    BNE $E94D       BNE    MLP4
.,E951 88       DEY             DEY
.,E952 D0 F9    BNE $E94D       BNE    MLP4
.,E954 84 C6    STY $C6         STY    NDX             ;CLEAR KEY QUEUE BUFFER
                                ;
.,E956 A6 D6    LDX $D6         MLP42  LDX TBLX
                                ;
.,E958 68       PLA             PULIND PLA             ;RESTORE OLD INDIRECTS
.,E959 85 AF    STA $AF         STA    EAH
.,E95B 68       PLA             PLA
.,E95C 85 AE    STA $AE         STA    EAL
.,E95E 68       PLA             PLA
.,E95F 85 AD    STA $AD         STA    SAH
.,E961 68       PLA             PLA
.,E962 85 AC    STA $AC         STA    SAL
.,E964 60       RTS             RTS
                                NEWLIN
.,E965 A6 D6    LDX $D6                LDX TBLX
.,E967 E8       INX             BMT1   INX
                                ; CPX #NLINES ;EXCEDED THE NUMBER OF LINES ???
                                ; BEQ BMT2 ;VIC-40 CODE
.,E968 B5 D9    LDA $D9,X              LDA LDTB1,X     ;FIND LAST DISPLAY LINE OF THIS LINE
.,E96A 10 FB    BPL $E967              BPL BMT1        ;TABLE END MARK=>$FF WILL ABORT...ALSO
.,E96C 8E A5 02 STX $02A5       BMT2   STX LINTMP      ;FOUND IT
                                ;GENERATE A NEW LINE
.,E96F E0 18    CPX #$18        CPX    #NLINES-1       ;IS ONE LINE FROM BOTTOM?
.,E971 F0 0E    BEQ $E981       BEQ    NEWLX           ;YES...JUST CLEAR LAST
.,E973 90 0C    BCC $E981       BCC    NEWLX           ;<NLINES...INSERT LINE
.,E975 20 EA E8 JSR $E8EA              JSR SCROL       ;SCROLL EVERYTHING
.,E978 AE A5 02 LDX $02A5              LDX LINTMP
.,E97B CA       DEX                    DEX
.,E97C C6 D6    DEC $D6                DEC TBLX
.,E97E 4C DA E6 JMP $E6DA              JMP WLOG30
.,E981 A5 AC    LDA $AC         NEWLX  LDA SAL
.,E983 48       PHA             PHA
.,E984 A5 AD    LDA $AD         LDA    SAH
.,E986 48       PHA             PHA
.,E987 A5 AE    LDA $AE         LDA    EAL
.,E989 48       PHA             PHA
.,E98A A5 AF    LDA $AF         LDA    EAH
.,E98C 48       PHA             PHA
.,E98D A2 19    LDX #$19               LDX #NLINES
.,E98F CA       DEX             SCD10  DEX
.,E990 20 F0 E9 JSR $E9F0              JSR SETPNT      ;SET UP TO ADDR
.,E993 EC A5 02 CPX $02A5              CPX LINTMP
.,E996 90 0E    BCC $E9A6              BCC SCR40
.,E998 F0 0C    BEQ $E9A6              BEQ SCR40       ;BRANCH IF FINISHED
.,E99A BD EF EC LDA $ECEF,X            LDA LDTB2-1,X   ;SET FROM ADDR
.,E99D 85 AC    STA $AC                STA SAL
.,E99F B5 D8    LDA $D8,X              LDA LDTB1-1,X
.,E9A1 20 C8 E9 JSR $E9C8              JSR SCRLIN      ;SCROLL THIS LINE DOWN
.,E9A4 30 E9    BMI $E98F              BMI SCD10
                                SCR40
.,E9A6 20 FF E9 JSR $E9FF              JSR CLRLN
.,E9A9 A2 17    LDX #$17               LDX #NLINES-2
                                SCRD21
.,E9AB EC A5 02 CPX $02A5              CPX LINTMP      ;DONE?
.,E9AE 90 0F    BCC $E9BF              BCC SCRD22      ;BRANCH IF SO
.,E9B0 B5 DA    LDA $DA,X              LDA LDTB1+1,X
.,E9B2 29 7F    AND #$7F               AND #$7F
.,E9B4 B4 D9    LDY $D9,X              LDY LDTB1,X     ;WAS IT CONTINUED
.,E9B6 10 02    BPL $E9BA              BPL SCRD19      ;BRANCH IF SO
.,E9B8 09 80    ORA #$80               ORA #$80
.,E9BA 95 DA    STA $DA,X       SCRD19 STA LDTB1+1,X
.,E9BC CA       DEX                    DEX
.,E9BD D0 EC    BNE $E9AB              BNE SCRD21
                                SCRD22
.,E9BF AE A5 02 LDX $02A5              LDX LINTMP
.,E9C2 20 DA E6 JSR $E6DA              JSR WLOG30
                                ;
.,E9C5 4C 58 E9 JMP $E958              JMP PULIND      ;GO PUL OLD INDIRECTS AND RETURN
                                ;
                                ; SCROLL LINE FROM SAL TO PNT
                                ; AND COLORS FROM EAL TO USER
                                ;
                                SCRLIN
.,E9C8 29 03    AND #$03               AND #$03        ;CLEAR ANY GARBAGE STUFF
.,E9CA 0D 88 02 ORA $0288              ORA HIBASE      ;PUT IN HIORDER BITS
.,E9CD 85 AD    STA $AD                STA SAL+1
.,E9CF 20 E0 E9 JSR $E9E0              JSR TOFROM      ;COLOR TO & FROM ADDRS
.,E9D2 A0 27    LDY #$27               LDY #LLEN-1
                                SCD20
.,E9D4 B1 AC    LDA ($AC),Y            LDA (SAL)Y
.,E9D6 91 D1    STA ($D1),Y            STA (PNT)Y
.,E9D8 B1 AE    LDA ($AE),Y            LDA (EAL)Y
.,E9DA 91 F3    STA ($F3),Y            STA (USER)Y
.,E9DC 88       DEY                    DEY
.,E9DD 10 F5    BPL $E9D4              BPL SCD20
.,E9DF 60       RTS                    RTS
                                ;
                                ; DO COLOR TO AND FROM ADDRESSES
                                ; FROM CHARACTER TO AND FROM ADRS
                                ;
                                TOFROM
.,E9E0 20 24 EA JSR $EA24              JSR SCOLOR
.,E9E3 A5 AC    LDA $AC                LDA SAL         ;CHARACTER FROM
.,E9E5 85 AE    STA $AE                STA EAL         ;MAKE COLOR FROM
.,E9E7 A5 AD    LDA $AD                LDA SAL+1
.,E9E9 29 03    AND #$03               AND #$03
.,E9EB 09 D8    ORA #$D8               ORA #>VICCOL
.,E9ED 85 AF    STA $AF                STA EAL+1
.,E9EF 60       RTS                    RTS
                                ;
                                ; SET UP PNT AND Y
                                ; FROM .X
                                ;
.,E9F0 BD F0 EC LDA $ECF0,X     SETPNT LDA LDTB2,X
.,E9F3 85 D1    STA $D1                STA PNT
.,E9F5 B5 D9    LDA $D9,X              LDA LDTB1,X
.,E9F7 29 03    AND #$03               AND #$03
.,E9F9 0D 88 02 ORA $0288              ORA HIBASE
.,E9FC 85 D2    STA $D2                STA PNT+1
.,E9FE 60       RTS                    RTS
                                ;
                                ; CLEAR THE LINE POINTED TO BY .X
                                ;
.,E9FF A0 27    LDY #$27        CLRLN  LDY #LLEN-1
.,EA01 20 F0 E9 JSR $E9F0              JSR SETPNT
.,EA04 20 24 EA JSR $EA24              JSR SCOLOR
.,EA07 20 DA E4 JSR $E4DA       CLR10  JSR CPATCH      ;REVERSED ORDER FROM 901227-02
.,EA0A A9 20    LDA #$20               LDA #$20        ;STORE A SPACE
.,EA0C 91 D1    STA ($D1),Y            STA (PNT)Y     ;TO DISPLAY
.,EA0E 88       DEY                    DEY
.,EA0F 10 F6    BPL $EA07              BPL CLR10
.,EA11 60       RTS                    RTS
.,EA12 .A       NOP                    NOP
                                ;
                                ;PUT A CHAR ON THE SCREEN
                                ;
.,EA13 A8       TAY             DSPP   TAY             ;SAVE CHAR
.,EA14 A9 02    LDA #$02        LDA    #2
.,EA16 85 CD    STA $CD         STA    BLNCT           ;BLINK CURSOR
.,EA18 20 24 EA JSR $EA24       JSR    SCOLOR          ;SET COLOR PTR
.,EA1B 98       TYA             TYA                    ;RESTORE COLOR
.,EA1C A4 D3    LDY $D3         DSPP2  LDY PNTR        ;GET COLUMN
.,EA1E 91 D1    STA ($D1),Y     STA    (PNT)Y          ;CHAR TO SCREEN
.,EA20 8A       TXA             TXA
.,EA21 91 F3    STA ($F3),Y     STA    (USER)Y         ;COLOR TO SCREEN
.,EA23 60       RTS             RTS
.,EA24 A5 D1    LDA $D1         SCOLOR LDA PNT         ;GENERATE COLOR PTR
.,EA26 85 F3    STA $F3         STA    USER
.,EA28 A5 D2    LDA $D2         LDA    PNT+1
.,EA2A 29 03    AND #$03        AND    #$03
.,EA2C 09 D8    ORA #$D8        ORA    #>VICCOL        ;VIC COLOR RAM
.,EA2E 85 F4    STA $F4         STA    USER+1
.,EA30 60       RTS             RTS
.,EA31 20 EA FF JSR $FFEA       KEY    JSR $FFEA       ;UPDATE JIFFY CLOCK
.,EA34 A5 CC    LDA $CC                LDA BLNSW       ;BLINKING CRSR ?
.,EA36 D0 29    BNE $EA61              BNE KEY4        ;NO
.,EA38 C6 CD    DEC $CD                DEC BLNCT       ;TIME TO BLINK ?
.,EA3A D0 25    BNE $EA61              BNE KEY4        ;NO
.,EA3C A9 14    LDA #$14               LDA #20         ;RESET BLINK COUNTER
.,EA3E 85 CD    STA $CD         REPDO  STA BLNCT
.,EA40 A4 D3    LDY $D3                LDY PNTR        ;CURSOR POSITION
.,EA42 46 CF    LSR $CF                LSR BLNON       ;CARRY SET IF ORIGINAL CHAR
.,EA44 AE 87 02 LDX $0287              LDX GDCOL       ;GET CHAR ORIGINAL COLOR
.,EA47 B1 D1    LDA ($D1),Y            LDA (PNT)Y      ;GET CHARACTER
.,EA49 B0 11    BCS $EA5C              BCS KEY5        ;BRANCH IF NOT NEEDED
                                ;
.,EA4B E6 CF    INC $CF                INC BLNON       ;SET TO 1
.,EA4D 85 CE    STA $CE                STA GDBLN       ;SAVE ORIGINAL CHAR
.,EA4F 20 24 EA JSR $EA24              JSR SCOLOR
.,EA52 B1 F3    LDA ($F3),Y            LDA (USER)Y     ;GET ORIGINAL COLOR
.,EA54 8D 87 02 STA $0287              STA GDCOL       ;SAVE IT
.,EA57 AE 86 02 LDX $0286              LDX COLOR       ;BLINK IN THIS COLOR
.,EA5A A5 CE    LDA $CE                LDA GDBLN       ;WITH ORIGINAL CHARACTER
                                ;
.,EA5C 49 80    EOR #$80        KEY5   EOR #$80        ;BLINK IT
.,EA5E 20 1C EA JSR $EA1C              JSR DSPP2       ;DISPLAY IT
                                ;
.,EA61 A5 01    LDA $01         KEY4   LDA R6510       ;GET CASSETTE SWITCHES
.,EA63 29 10    AND #$10               AND #$10        ;IS SWITCH DOWN ?
.,EA65 F0 0A    BEQ $EA71              BEQ KEY3        ;BRANCH IF SO
                                ;
.,EA67 A0 00    LDY #$00        LDY    #0
.,EA69 84 C0    STY $C0                STY CAS1        ;CASSETTE OFF SWITCH
                                ;
.,EA6B A5 01    LDA $01                LDA R6510
.,EA6D 09 20    ORA #$20               ORA #$20
.,EA6F D0 08    BNE $EA79              BNE KL24        ;BRANCH IF MOTOR IS OFF
                                ;
.,EA71 A5 C0    LDA $C0         KEY3   LDA CAS1
.,EA73 D0 06    BNE $EA7B              BNE KL2
                                ;
.,EA75 A5 01    LDA $01                LDA R6510
.,EA77 29 1F    AND #$1F               AND #%011111    ;TURN MOTOR ON
                                ;
                                KL24
.,EA79 85 01    STA $01                STA R6510
                                ;
.,EA7B 20 87 EA JSR $EA87       KL2    JSR SCNKEY      ;SCAN KEYBOARD
                                ;
.,EA7E AD 0D DC LDA $DC0D       KPREND LDA D1ICR       ;CLEAR INTERUPT FLAGS
.,EA81 68       PLA                    PLA             ;RESTORE REGISTERS
.,EA82 A8       TAY                    TAY
.,EA83 68       PLA                    PLA
.,EA84 AA       TAX                    TAX
.,EA85 68       PLA                    PLA
.,EA86 40       RTI                    RTI             ;EXIT FROM IRQ ROUTINES
                                ; ****** GENERAL KEYBOARD SCAN ******
                                ;
.,EA87 A9 00    LDA #$00        SCNKEY LDA #$00
.,EA89 8D 8D 02 STA $028D              STA SHFLAG
.,EA8C A0 40    LDY #$40               LDY #64         ;LAST KEY INDEX
.,EA8E 84 CB    STY $CB                STY SFDX        ;NULL KEY FOUND
.,EA90 8D 00 DC STA $DC00              STA COLM        ;RAISE ALL LINES
.,EA93 AE 01 DC LDX $DC01              LDX ROWS        ;CHECK FOR A KEY DOWN
.,EA96 E0 FF    CPX #$FF               CPX #$FF        ;NO KEYS DOWN?
.,EA98 F0 61    BEQ $EAFB              BEQ SCNOUT      ;BRANCH IF NONE
.,EA9A A8       TAY                    TAY             ;.A=0 LDY #0
.,EA9B A9 81    LDA #$81               LDA #<MODE1
.,EA9D 85 F5    STA $F5                STA KEYTAB
.,EA9F A9 EB    LDA #$EB               LDA #>MODE1
.,EAA1 85 F6    STA $F6                STA KEYTAB+1
.,EAA3 A9 FE    LDA #$FE               LDA #$FE        ;START WITH 1ST COLUMN
.,EAA5 8D 00 DC STA $DC00              STA COLM
.,EAA8 A2 08    LDX #$08        SCN20  LDX #8          ;8 ROW KEYBOARD
.,EAAA 48       PHA                    PHA             ;SAVE COLUMN OUTPUT INFO
.,EAAB AD 01 DC LDA $DC01       SCN22  LDA ROWS
.,EAAE CD 01 DC CMP $DC01              CMP ROWS        ;DEBOUNCE KEYBOARD
.,EAB1 D0 F8    BNE $EAAB              BNE SCN22
.,EAB3 4A       LSR             SCN30  LSR A           ;LOOK FOR KEY DOWN
.,EAB4 B0 16    BCS $EACC              BCS CKIT        ;NONE
.,EAB6 48       PHA                    PHA
.,EAB7 B1 F5    LDA ($F5),Y            LDA (KEYTAB),Y  ;GET CHAR CODE
.,EAB9 C9 05    CMP #$05               CMP #$05
.,EABB B0 0C    BCS $EAC9              BCS SPCK2       ;IF NOT SPECIAL KEY GO ON
.,EABD C9 03    CMP #$03               CMP #$03        ;COULD IT BE A STOP KEY?
.,EABF F0 08    BEQ $EAC9              BEQ SPCK2       ;BRANCH IF SO
.,EAC1 0D 8D 02 ORA $028D              ORA SHFLAG
.,EAC4 8D 8D 02 STA $028D              STA SHFLAG      ;PUT SHIFT BIT IN FLAG BYTE
.,EAC7 10 02    BPL $EACB              BPL CKUT
                                SPCK2
.,EAC9 84 CB    STY $CB                STY SFDX        ;SAVE KEY NUMBER
.,EACB 68       PLA             CKUT   PLA
.,EACC C8       INY             CKIT   INY
.,EACD C0 41    CPY #$41               CPY #65
.,EACF B0 0B    BCS $EADC              BCS CKIT1       ;BRANCH IF FINISHED
.,EAD1 CA       DEX                    DEX
.,EAD2 D0 DF    BNE $EAB3              BNE SCN30
.,EAD4 38       SEC                    SEC
.,EAD5 68       PLA                    PLA             ;RELOAD COLUMN INFO
.,EAD6 2A       ROL                    ROL A
.,EAD7 8D 00 DC STA $DC00              STA COLM        ;NEXT COLUMN ON KEYBOARD
.,EADA D0 CC    BNE $EAA8              BNE SCN20       ;ALWAYS BRANCH
.,EADC 68       PLA             CKIT1  PLA             ;DUMP COLUMN OUTPUT...ALL DONE
.,EADD 6C 8F 02 JMP ($028F)            JMP (KEYLOG)    ;EVALUATE SHIFT FUNCTIONS
.,EAE0 A4 CB    LDY $CB         REKEY  LDY SFDX        ;GET KEY INDEX
.,EAE2 B1 F5    LDA ($F5),Y            LDA (KEYTAB)Y   ;GET CHAR CODE
.,EAE4 AA       TAX                    TAX             ;SAVE THE CHAR
.,EAE5 C4 C5    CPY $C5                CPY LSTX        ;SAME AS PREV CHAR INDEX?
.,EAE7 F0 07    BEQ $EAF0              BEQ RPT10       ;YES
.,EAE9 A0 10    LDY #$10               LDY #$10        ;NO - RESET DELAY BEFORE REPEAT
.,EAEB 8C 8C 02 STY $028C              STY DELAY
.,EAEE D0 36    BNE $EB26              BNE CKIT2       ;ALWAYS
.,EAF0 29 7F    AND #$7F        RPT10  AND #$7F        ;UNSHIFT IT
.,EAF2 2C 8A 02 BIT $028A              BIT RPTFLG      ;CHECK FOR REPEAT DISABLE
.,EAF5 30 16    BMI $EB0D              BMI RPT20       ;YES
.,EAF7 70 49    BVS $EB42              BVS SCNRTS
.,EAF9 C9 7F    CMP #$7F               CMP #$7F        ;NO KEYS ?
.,EAFB F0 29    BEQ $EB26       SCNOUT BEQ CKIT2       ;YES - GET OUT
.,EAFD C9 14    CMP #$14               CMP #$14        ;AN INST/DEL KEY ?
.,EAFF F0 0C    BEQ $EB0D              BEQ RPT20       ;YES - REPEAT IT
.,EB01 C9 20    CMP #$20               CMP #$20        ;A SPACE KEY ?
.,EB03 F0 08    BEQ $EB0D              BEQ RPT20       ;YES
.,EB05 C9 1D    CMP #$1D               CMP #$1D        ;A CRSR LEFT/RIGHT ?
.,EB07 F0 04    BEQ $EB0D              BEQ RPT20       ;YES
.,EB09 C9 11    CMP #$11               CMP #$11        ;A CRSR UP/DWN ?
.,EB0B D0 35    BNE $EB42              BNE SCNRTS      ;NO - EXIT
.,EB0D AC 8C 02 LDY $028C       RPT20  LDY DELAY       ;TIME TO REPEAT ?
.,EB10 F0 05    BEQ $EB17              BEQ RPT40       ;YES
.,EB12 CE 8C 02 DEC $028C              DEC DELAY
.,EB15 D0 2B    BNE $EB42              BNE SCNRTS
.,EB17 CE 8B 02 DEC $028B       RPT40  DEC KOUNT       ;TIME FOR NEXT REPEAT ?
.,EB1A D0 26    BNE $EB42              BNE SCNRTS      ;NO
.,EB1C A0 04    LDY #$04               LDY #4          ;YES - RESET CTR
.,EB1E 8C 8B 02 STY $028B              STY KOUNT
.,EB21 A4 C6    LDY $C6                LDY NDX         ;NO REPEAT IF QUEUE FULL
.,EB23 88       DEY                    DEY
.,EB24 10 1C    BPL $EB42              BPL SCNRTS
                                CKIT2
.,EB26 A4 CB    LDY $CB                LDY SFDX        ;GET INDEX OF KEY
.,EB28 84 C5    STY $C5                STY LSTX        ;SAVE THIS INDEX TO KEY FOUND
.,EB2A AC 8D 02 LDY $028D              LDY SHFLAG      ;UPDATE SHIFT STATUS
.,EB2D 8C 8E 02 STY $028E              STY LSTSHF
.,EB30 E0 FF    CPX #$FF        CKIT3  CPX #$FF        ;A NULL KEY OR NO KEY ?
.,EB32 F0 0E    BEQ $EB42              BEQ SCNRTS      ;BRANCH IF SO
.,EB34 8A       TXA                    TXA             ;NEED X AS INDEX SO...
.,EB35 A6 C6    LDX $C6                LDX NDX         ;GET # OF CHARS IN KEY QUEUE
.,EB37 EC 89 02 CPX $0289              CPX XMAX        ;IRQ BUFFER FULL ?
.,EB3A B0 06    BCS $EB42              BCS SCNRTS      ;YES - NO MORE INSERT
                                PUTQUE
.,EB3C 9D 77 02 STA $0277,X            STA KEYD,X      ;PUT RAW DATA HERE
.,EB3F E8       INX                    INX
.,EB40 86 C6    STX $C6                STX NDX         ;UPDATE KEY QUEUE COUNT
.,EB42 A9 7F    LDA #$7F        SCNRTS LDA #$7F        ;SETUP PB7 FOR STOP KEY SENSE
.,EB44 8D 00 DC STA $DC00              STA COLM
.,EB47 60       RTS                    RTS
                                ;
                                ; SHIFT LOGIC
                                ;
                                SHFLOG
.,EB48 AD 8D 02 LDA $028D              LDA SHFLAG
.,EB4B C9 03    CMP #$03               CMP #$03        ;COMMODORE SHIFT COMBINATION?
.,EB4D D0 15    BNE $EB64              BNE KEYLG2      ;BRANCH IF NOT
.,EB4F CD 8E 02 CMP $028E              CMP LSTSHF      ;DID I DO THIS ALREADY
.,EB52 F0 EE    BEQ $EB42              BEQ SCNRTS      ;BRANCH IF SO
.,EB54 AD 91 02 LDA $0291              LDA MODE
.,EB57 30 1D    BMI $EB76              BMI SHFOUT      ;DONT SHIFT IF ITS MINUS
.,EB59 AD 18 D0 LDA $D018       SWITCH LDA VICREG+24   ;**********************************:
.,EB5C 49 02    EOR #$02               EOR #$02        ;TURN ON OTHER CASE
.,EB5E 8D 18 D0 STA $D018              STA VICREG+24   ;POINT THE VIC THERE
.,EB61 4C 76 EB JMP $EB76              JMP SHFOUT
                                ;
                                KEYLG2
.,EB64 0A       ASL                    ASL A
.,EB65 C9 08    CMP #$08               CMP #$08        ;WAS IT A CONTROL KEY
.,EB67 90 02    BCC $EB6B              BCC NCTRL       ;BRANCH IF NOT
.,EB69 A9 06    LDA #$06               LDA #6          ;ELSE USE TABLE #4
                                ;
                                NCTRL
                                NOTKAT
.,EB6B AA       TAX                    TAX
.,EB6C BD 79 EB LDA $EB79,X            LDA KEYCOD,X
.,EB6F 85 F5    STA $F5                STA KEYTAB
.,EB71 BD 7A EB LDA $EB7A,X            LDA KEYCOD+1,X
.,EB74 85 F6    STA $F6                STA KEYTAB+1
                                SHFOUT
.,EB76 4C E0 EA JMP $EAE0              JMP REKEY
                                .END
                                .LIB   EDITOR.3
                                KEYCOD                 ;KEYBOARD MODE 'DISPATCH'
                                       .WORD MODE1
                                       .WORD MODE2
                                       .WORD MODE3
.:EB79 81 EB C2 EB 03 EC 78 EC         .WORD CONTRL    ;CONTROL KEYS
                                ;
                                ; COTTACONNA MODE
                                ;
                                ;.WORD MODE1  ;PET MODE1
                                ;.WORD MODE2  ;PET MODE2
                                ;.WORD CCTTA3 ;DUMMY WORD
                                ;.WORD CONTRL
                                ;
                                ; EXTENDED KATAKANA MODE
                                ;
                                ;.WORD CCTTA2 ;KATAKANA CHARACTERS
                                ;.WORD CCTTA3 ;LIMITED GRAPHICS
                                ;.WORD CCTTA3 ;DUMMY
                                ;.WORD CONTRL
                                MODE1
                                ;DEL,3,5,7,9,+,YEN SIGN,1
.:EB81 14 0D 1D 88 85 86 87 11  .BYT   $14,$0D,$1D,$88,$85,$86,$87,$11
                                ;RETURN,W,R,Y,I,P,*,LEFT ARROW
.:EB89 33 57 41 34 5A 53 45 01  .BYT   $33,$57,$41,$34,$5A,$53,$45,$01
                                ;RT CRSR,A,D,G,J,L,;,CTRL
.:EB91 35 52 44 36 43 46 54 58  .BYT   $35,$52,$44,$36,$43,$46,$54,$58
                                ;F4,4,6,8,0,-,HOME,2
.:EB99 37 59 47 38 42 48 55 56  .BYT   $37,$59,$47,$38,$42,$48,$55,$56
                                ;F1,Z,C,B,M,.,R.SHIFTT,SPACE
.:EBA1 39 49 4A 30 4D 4B 4F 4E  .BYT   $39,$49,$4A,$30,$4D,$4B,$4F,$4E
                                ;F2,S,F,H,K,:,=,COM.KEY
.:EBA9 2B 50 4C 2D 2E 3A 40 2C  .BYT   $2B,$50,$4C,$2D,$2E,$3A,$40,$2C
                                ;F3,E,T,U,O,@,EXP,Q
.:EBB1 5C 2A 3B 13 01 3D 5E 2F  .BYT   $5C,$2A,$3B,$13,$01,$3D,$5E,$2F
                                ;CRSR DWN,L.SHIFT,X,V,N,,,/,STOP
.:EBB9 31 5F 04 32 20 02 51 03  .BYT   $31,$5F,$04,$32,$20,$02,$51,$03
.:EBC1 FF                       .BYT   $FF             ;END OF TABLE NULL
                                MODE2                  ;SHIFT
                                ;INS,%,',),+,YEN,!
.:EBC2 94 8D 9D 8C 89 8A 8B 91  .BYT   $94,$8D,$9D,$8C,$89,$8A,$8B,$91
                                ;SRETURN,W,R,Y,I,P,*,SLEFT ARROW
.:EBCA 23 D7 C1 24 DA D3 C5 01  .BYT   $23,$D7,$C1,$24,$DA,$D3,$C5,$01
                                ;LF.CRSR,A,D,G,J,L,;,CTRL
.:EBD2 25 D2 C4 26 C3 C6 D4 D8  .BYT   $25,$D2,$C4,$26,$C3,$C6,$D4,$D8
                                ;,$,&,(,      ,"
.:EBDA 27 D9 C7 28 C2 C8 D5 D6  .BYT   $27,$D9,$C7,$28,$C2,$C8,$D5,$D6
                                ;F5,Z,C,B,M,.,R.SHIFT,SSPACE
.:EBE2 29 C9 CA 30 CD CB CF CE  .BYT   $29,$C9,$CA,$30,$CD,$CB,$CF,$CE
                                ;F6,S,F,H,K,:,=,SCOM.KEY
.:EBEA DB D0 CC DD 3E 5B BA 3C  .BYT   $DB,$D0,$CC,$DD,$3E,$5B,$BA,$3C
                                ;F7,E,T,U,O,@,PI,G
.:EBF2 A9 C0 5D 93 01 3D DE 3F  .BYT   $A9,$C0,$5D,$93,$01,$3D,$DE,$3F
                                ;CRSR DWN,L.SHIFT,X,V,N,,,/,RUN
.:EBFA 21 5F 04 22 A0 02 D1 83  .BYT   $21,$5F,$04,$22,$A0,$02,$D1,$83
.:EC02 FF                       .BYT   $FF             ;END OF TABLE NULL
                                ;
                                MODE3                  ;LEFT WINDOW GRAHPICS
                                ;INS,C10,C12,C14,9,+,POUND SIGN,C8
.:EC03 94 8D 9D 8C 89 8A 8B 91  .BYT   $94,$8D,$9D,$8C,$89,$8A,$8B,$91
                                ;RETURN,W,R,Y,I,P,*,LFT.ARROW
.:EC0B 96 B3 B0 97 AD AE B1 01  .BYT   $96,$B3,$B0,$97,$AD,$AE,$B1,$01
                                ;LF.CRSR,A,D,G,J,L,;,CTRL
.:EC13 98 B2 AC 99 BC BB A3 BD  .BYT   $98,$B2,$AC,$99,$BC,$BB,$A3,$BD
                                ;F8,C11,C13,C15,0,-,HOME,C9
.:EC1B 9A B7 A5 9B BF B4 B8 BE  .BYT   $9A,$B7,$A5,$9B,$BF,$B4,$B8,$BE
                                ;F2,Z,C,B,M,.,R.SHIFT,SPACE
.:EC23 29 A2 B5 30 A7 A1 B9 AA  .BYT   $29,$A2,$B5,$30,$A7,$A1,$B9,$AA
                                ;F4,S,F,H,K,:,=,COM.KEY
.:EC2B A6 AF B6 DC 3E 5B A4 3C  .BYT   $A6,$AF,$B6,$DC,$3E,$5B,$A4,$3C
                                ;F6,E,T,U,O,@,PI,Q
.:EC33 A8 DF 5D 93 01 3D DE 3F  .BYT   $A8,$DF,$5D,$93,$01,$3D,$DE,$3F
                                ;CRSR.UP,L.SHIFT,X,V,N,,,/,STOP
.:EC3B 81 5F 04 95 A0 02 AB 83  .BYT   $81,$5F,$04,$95,$A0,$02,$AB,$83
.:EC43 FF                       .BYT   $FF             ;END OF TABLE NULL
                                ;CCTTA2 ;WAS CCTTA2 IN JAPANESE VERSION
                                LOWER
.,EC44 C9 0E    CMP #$0E               CMP #$0E        ;DOES HE WANT LOWER CASE?
.,EC46 D0 07    BNE $EC4F              BNE UPPER       ;BRANCH IF NOT
.,EC48 AD 18 D0 LDA $D018              LDA VICREG+24   ;ELSE SET VIC TO POINT TO LOWER CASE
.,EC4B 09 02    ORA #$02               ORA #$02
.,EC4D D0 09    BNE $EC58              BNE ULSET       ;JMP
                                UPPER
.,EC4F C9 8E    CMP #$8E               CMP #$8E        ;DOES HE WANT UPPER CASE
.,EC51 D0 0B    BNE $EC5E              BNE LOCK        ;BRANCH IF NOT
.,EC53 AD 18 D0 LDA $D018              LDA VICREG+24   ;MAKE SURE VIC POINT TO UPPER/PET SET
.,EC56 29 FD    AND #$FD               AND #$FF-$02
.,EC58 8D 18 D0 STA $D018       ULSET  STA VICREG+24
.,EC5B 4C A8 E6 JMP $E6A8       OUTHRE JMP LOOP2
                                LOCK
.,EC5E C9 08    CMP #$08               CMP #8          ;DOES HE WANT TO LOCK IN THIS MODE?
.,EC60 D0 07    BNE $EC69              BNE UNLOCK      ;BRANCH IF NOT
.,EC62 A9 80    LDA #$80               LDA #$80        ;ELSE SET LOCK SWITCH ON
.,EC64 0D 91 02 ORA $0291              ORA MODE        ;DON'T HURT ANYTHING - JUST IN CASE
.,EC67 30 09    BMI $EC72              BMI LEXIT
                                UNLOCK
.,EC69 C9 09    CMP #$09               CMP #9          ;DOES HE WANT TO UNLOCK THE KEYBOARD?
.,EC6B D0 EE    BNE $EC5B              BNE OUTHRE      ;BRANCH IF NOT
.,EC6D A9 7F    LDA #$7F               LDA #$7F        ;CLEAR THE LOCK SWITCH
.,EC6F 2D 91 02 AND $0291              AND MODE        ;DONT HURT ANYTHING
.,EC72 8D 91 02 STA $0291       LEXIT  STA MODE
.,EC75 4C A8 E6 JMP $E6A8              JMP LOOP2       ;GET OUT
                                ;CCTTA3
                                ;.BYT $04,$FF,$FF,$FF,$FF,$FF,$E2,$9D
                                ;RUN-K24-K31
                                ;.BYT $83,$01,$FF,$FF,$FF,$FF,$FF,$91
                                ;K32-K39.F5
                                ;.BYT $A0,$FF,$FF,$FF,$FF,$EE,$01,$89
                                ;CO.KEY,K40-K47.F6
                                ;.BYT $02,$FF,$FF,$FF,$FF,$E1,$FD,$8A
                                ;K48-K55
                                ;.BYT $FF,$FF,$FF,$FF,$FF,$B0,$E0,$8B
                                ;K56-K63
                                ;.BYT $F2,$F4,$F6,$FF,$F0,$ED,$93,$8C
                                ;.BYT $FF ;END OF TABLE NULL
                                CONTRL
                                ;NULL,RED,PURPLE,BLUE,RVS ,NULL,NULL,BLACK
.:EC78 FF FF FF FF FF FF FF FF  .BYT   $FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF
                                ;NULL, W  ,REVERSE, Y  , I  , P  ,NULL,MUSIC
.:EC80 1C 17 01 9F 1A 13 05 FF  .BYT   $1C,$17,$01,$9F,$1A,$13,$05,$FF
.:EC88 9C 12 04 1E 03 06 14 18  .BYT   $9C,$12,$04,$1E,$03,$06,$14,$18
                                ;NULL,CYAN,GREEN,YELLOW,RVS OFF,NULL,NULL,WHITE
.:EC90 1F 19 07 9E 02 08 15 16  .BYT   $1F,$19,$07,$9E,$02,$08,$15,$16
.:EC98 12 09 0A 92 0D 0B 0F 0E  .BYT   $12,$09,$0A,$92,$0D,$0B,$0F,$0E
.:ECA0 FF 10 0C FF FF 1B 00 FF  .BYT   $FF,$10,$0C,$FF,$FF,$1B,$00,$FF
.:ECA8 1C FF 1D FF FF 1F 1E FF  .BYT   $1C,$FF,$1D,$FF,$FF,$1F,$1E,$FF
.:ECB0 90 06 FF 05 FF FF 11 FF  .BYT   $90,$06,$FF,$05,$FF,$FF,$11,$FF
.:ECB8 FF                       .BYT   $FF             ;END OF TABLE NULL
                                TVIC
                                .BYT   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ;SPRITES (0-16)
                                .BYT   $1B,0,0,0,0,$08,0,$14,0,0,0,0,0,0,0 ;DATA (17-31)
.:ECB9 00 00 00 00 00 00 00 00  .BYT   14,6,1,2,3,4,0,1,2,3,4,5,6,7 ;32-46
                                ;
.:ECE7 4C 4F 41 44 0D 52 55 4E  RUNTB  .BYT 'LOAD',$D,'RUN',$D
                                ;
                                LINZ0  = VICSCN
                                LINZ1  = LINZ0+LLEN
                                LINZ2  = LINZ1+LLEN
                                LINZ3  = LINZ2+LLEN
                                LINZ4  = LINZ3+LLEN
                                LINZ5  = LINZ4+LLEN
                                LINZ6  = LINZ5+LLEN
                                LINZ7  = LINZ6+LLEN
                                LINZ8  = LINZ7+LLEN
                                LINZ9  = LINZ8+LLEN
                                LINZ10 = LINZ9+LLEN
                                LINZ11 = LINZ10+LLEN
                                LINZ12 = LINZ11+LLEN
                                LINZ13 = LINZ12+LLEN
                                LINZ14 = LINZ13+LLEN
                                LINZ15 = LINZ14+LLEN
                                LINZ16 = LINZ15+LLEN
                                LINZ17 = LINZ16+LLEN
                                LINZ18 = LINZ17+LLEN
                                LINZ19 = LINZ18+LLEN
                                LINZ20 = LINZ19+LLEN
                                LINZ21 = LINZ20+LLEN
                                LINZ22 = LINZ21+LLEN
                                LINZ23 = LINZ22+LLEN
                                LINZ24 = LINZ23+LLEN
                                ;****** SCREEN LINES LO BYTE TABLE ******
                                ;
                                LDTB2
                                       .BYTE <LINZ0
                                       .BYTE <LINZ1
                                       .BYTE <LINZ2
                                       .BYTE <LINZ3
                                       .BYTE <LINZ4
                                       .BYTE <LINZ5
                                       .BYTE <LINZ6
                                       .BYTE <LINZ7
                                       .BYTE <LINZ8
                                       .BYTE <LINZ9
                                       .BYTE <LINZ10
                                       .BYTE <LINZ11
                                       .BYTE <LINZ12
                                       .BYTE <LINZ13
                                       .BYTE <LINZ14
                                       .BYTE <LINZ15
                                       .BYTE <LINZ16
                                       .BYTE <LINZ17
                                       .BYTE <LINZ18
                                       .BYTE <LINZ19
                                       .BYTE <LINZ20
                                       .BYTE <LINZ21
                                       .BYTE <LINZ22
                                       .BYTE <LINZ23
.:ECF0 00 28 50 78 A0 C8 F0 18         .BYTE <LINZ24
                                       .END
                                .LIB   SERIAL4.0
                                ;COMMAND SERIAL BUS DEVICE TO TALK
                                ;
.,ED09 09 40    ORA #$40        TALK   ORA #$40        ;MAKE A TALK ADR
.:ED0B 2C       .BYTE $2C       .BYT   $2C             ;SKIP TWO BYTES
                                ;COMMAND SERIAL BUS DEVICE TO LISTEN
                                ;
.,ED0C 09 20    ORA #$20        LISTN  ORA #$20        ;MAKE A LISTEN ADR
.,ED0E 20 A4 F0 JSR $F0A4       JSR    RSP232          ;PROTECT SELF FROM RS232 NMI'S
.,ED11 48       PHA             LIST1  PHA
                                ;
                                ;
.,ED12 24 94    BIT $94         BIT    C3P0            ;CHARACTER LEFT IN BUF?
.,ED14 10 0A    BPL $ED20       BPL    LIST2           ;NO...
                                ;
                                ;SEND BUFFERED CHARACTER
                                ;
.,ED16 38       SEC             SEC                    ;SET EOI FLAG
.,ED17 66 A3    ROR $A3         ROR    R2D2
                                ;
.,ED19 20 40 ED JSR $ED40       JSR    ISOUR           ;SEND LAST CHARACTER
                                ;
.,ED1C 46 94    LSR $94         LSR    C3P0            ;BUFFER CLEAR FLAG
.,ED1E 46 A3    LSR $A3         LSR    R2D2            ;CLEAR EOI FLAG
                                ;
                                ;
.,ED20 68       PLA             LIST2  PLA             ;TALK/LISTEN ADDRESS
.,ED21 85 95    STA $95         STA    BSOUR
.,ED23 78       SEI             SEI
.,ED24 20 97 EE JSR $EE97       JSR    DATAHI
.,ED27 C9 3F    CMP #$3F        CMP    #$3F            ;CLKHI ONLY ON UNLISTEN
.,ED29 D0 03    BNE $ED2E       BNE    LIST5
.,ED2B 20 85 EE JSR $EE85       JSR    CLKHI
                                ;
.,ED2E AD 00 DD LDA $DD00       LIST5  LDA D2PRA       ;ASSERT ATTENTION
.,ED31 09 08    ORA #$08        ORA    #$08
.,ED33 8D 00 DD STA $DD00       STA    D2PRA
                                ;
.,ED36 78       SEI             ISOURA SEI
.,ED37 20 8E EE JSR $EE8E       JSR    CLKLO           ;SET CLOCK LINE LOW
.,ED3A 20 97 EE JSR $EE97       JSR    DATAHI
.,ED3D 20 B3 EE JSR $EEB3       JSR    W1MS            ;DELAY 1 MS
.,ED40 78       SEI             ISOUR  SEI             ;NO IRQ'S ALLOWED
.,ED41 20 97 EE JSR $EE97              JSR DATAHI      ;MAKE SURE DATA IS RELEASED
.,ED44 20 A9 EE JSR $EEA9              JSR DEBPIA      ;DATA SHOULD BE LOW
.,ED47 B0 64    BCS $EDAD              BCS NODEV
.,ED49 20 85 EE JSR $EE85              JSR CLKHI       ;CLOCK LINE HIGH
.,ED4C 24 A3    BIT $A3                BIT R2D2        ;EOI FLAG TEST
.,ED4E 10 0A    BPL $ED5A              BPL NOEOI
                                ; DO THE EOI
.,ED50 20 A9 EE JSR $EEA9       ISR02  JSR DEBPIA      ;WAIT FOR DATA TO GO HIGH
.,ED53 90 FB    BCC $ED50              BCC ISR02
                                ;
.,ED55 20 A9 EE JSR $EEA9       ISR03  JSR DEBPIA      ;WAIT FOR DATA TO GO LOW
.,ED58 B0 FB    BCS $ED55              BCS ISR03
                                ;
.,ED5A 20 A9 EE JSR $EEA9       NOEOI  JSR DEBPIA      ;WAIT FOR DATA HIGH
.,ED5D 90 FB    BCC $ED5A       BCC    NOEOI
.,ED5F 20 8E EE JSR $EE8E       JSR    CLKLO           ;SET CLOCK LOW
                                ;
                                ; SET TO SEND DATA
                                ;
.,ED62 A9 08    LDA #$08        LDA    #$08            ;COUNT 8 BITS
.,ED64 85 A5    STA $A5         STA    COUNT
                                ;
                                ISR01
.,ED66 AD 00 DD LDA $DD00       LDA    D2PRA           ;DEBOUNCE THE BUS
.,ED69 CD 00 DD CMP $DD00       CMP    D2PRA
.,ED6C D0 F8    BNE $ED66       BNE    ISR01
.,ED6E 0A       ASL             ASL    A               ;SET THE FLAGS
.,ED6F 90 3F    BCC $EDB0       BCC    FRMERR          ;DATA MUST BE HI
                                ;
.,ED71 66 95    ROR $95         ROR    BSOUR           ;NEXT BIT INTO CARRY
.,ED73 B0 05    BCS $ED7A       BCS    ISRHI
.,ED75 20 A0 EE JSR $EEA0       JSR    DATALO
.,ED78 D0 03    BNE $ED7D       BNE    ISRCLK
.,ED7A 20 97 EE JSR $EE97       ISRHI  JSR DATAHI
.,ED7D 20 85 EE JSR $EE85       ISRCLK JSR CLKHI       ;CLOCK HI
.,ED80 EA       NOP             NOP
.,ED81 EA       NOP             NOP
.,ED82 EA       NOP             NOP
.,ED83 EA       NOP             NOP
.,ED84 AD 00 DD LDA $DD00       LDA    D2PRA
.,ED87 29 DF    AND #$DF        AND    #$FF-$20        ;DATA HIGH
.,ED89 09 10    ORA #$10        ORA    #$10            ;CLOCK LOW
.,ED8B 8D 00 DD STA $DD00       STA    D2PRA
.,ED8E C6 A5    DEC $A5         DEC    COUNT
.,ED90 D0 D4    BNE $ED66       BNE    ISR01
.,ED92 A9 04    LDA #$04        LDA    #$04            ;SET TIMER FOR 1MS
.,ED94 8D 07 DC STA $DC07       STA    D1T2H
.,ED97 A9 19    LDA #$19        LDA    #TIMRB          ;TRIGGER TIMER
.,ED99 8D 0F DC STA $DC0F       STA    D1CRB
.,ED9C AD 0D DC LDA $DC0D       LDA    D1ICR           ;CLEAR THE TIMER FLAGS<<<<<<<<<<<<<
.,ED9F AD 0D DC LDA $DC0D       ISR04  LDA D1ICR
.,EDA2 29 02    AND #$02        AND    #$02
.,EDA4 D0 0A    BNE $EDB0       BNE    FRMERR
.,EDA6 20 A9 EE JSR $EEA9       JSR    DEBPIA
.,EDA9 B0 F4    BCS $ED9F       BCS    ISR04
.,EDAB 58       CLI             CLI                    ;LET IRQ'S CONTINUE
.,EDAC 60       RTS             RTS
                                ;
                                NODEV                  ;DEVICE NOT PRESENT ERROR
.,EDAD A9 80    LDA #$80        LDA    #$80
.:EDAF 2C       .BYTE $2C       .BYT   $2C
                                FRMERR                 ;FRAMING ERROR
.,EDB0 A9 03    LDA #$03        LDA    #$03
.,EDB2 20 1C FE JSR $FE1C       CSBERR JSR UDST        ;COMMODORE SERIAL BUSS ERROR ENTRY
.,EDB5 58       CLI             CLI                    ;IRQ'S WERE OFF...TURN ON
.,EDB6 18       CLC             CLC                    ;MAKE SURE NO KERNAL ERROR RETURNED
.,EDB7 90 4A    BCC $EE03       BCC    DLABYE          ;TURN ATN OFF ,RELEASE ALL LINES
                                ;
                                ;SEND SECONDARY ADDRESS AFTER LISTEN
                                ;
.,EDB9 85 95    STA $95         SECND  STA BSOUR       ;BUFFER CHARACTER
.,EDBB 20 36 ED JSR $ED36       JSR    ISOURA          ;SEND IT
                                ;RELEASE ATTENTION AFTER LISTEN
                                ;
.,EDBE AD 00 DD LDA $DD00       SCATN  LDA D2PRA
.,EDC1 29 F7    AND #$F7        AND    #$FF-$08
.,EDC3 8D 00 DD STA $DD00       STA    D2PRA           ;RELEASE ATTENTION
.,EDC6 60       RTS             RTS
                                ;TALK SECOND ADDRESS
                                ;
.,EDC7 85 95    STA $95         TKSA   STA BSOUR       ;BUFFER CHARACTER
.,EDC9 20 36 ED JSR $ED36       JSR    ISOURA          ;SEND SECOND ADDR
                                TKATN                  ;SHIFT OVER TO LISTENER
.,EDCC 78       SEI             SEI                    ;NO IRQ'S HERE
.,EDCD 20 A0 EE JSR $EEA0       JSR    DATALO          ;DATA LINE LOW
.,EDD0 20 BE ED JSR $EDBE       JSR    SCATN
.,EDD3 20 85 EE JSR $EE85       JSR    CLKHI           ;CLOCK LINE HIGH JSR/RTS
.,EDD6 20 A9 EE JSR $EEA9       TKATN1 JSR DEBPIA      ;WAIT FOR CLOCK TO GO LOW
.,EDD9 30 FB    BMI $EDD6       BMI    TKATN1
.,EDDB 58       CLI             CLI                    ;IRQ'S OKAY NOW
.,EDDC 60       RTS             RTS
                                ;BUFFERED OUTPUT TO SERIAL BUS
                                ;
.,EDDD 24 94    BIT $94         CIOUT  BIT C3P0        ;BUFFERED CHAR?
.,EDDF 30 05    BMI $EDE6       BMI    CI2             ;YES...SEND LAST
                                ;
.,EDE1 38       SEC             SEC                    ;NO...
.,EDE2 66 94    ROR $94         ROR    C3P0            ;SET BUFFERED CHAR FLAG
.,EDE4 D0 05    BNE $EDEB       BNE    CI4             ;BRANCH ALWAYS
                                ;
.,EDE6 48       PHA             CI2    PHA             ;SAVE CURRENT CHAR
.,EDE7 20 40 ED JSR $ED40       JSR    ISOUR           ;SEND LAST CHAR
.,EDEA 68       PLA             PLA                    ;RESTORE CURRENT CHAR
.,EDEB 85 95    STA $95         CI4    STA BSOUR       ;BUFFER CURRENT CHAR
.,EDED 18       CLC             CLC                    ;CARRY-GOOD EXIT
.,EDEE 60       RTS             RTS
                                ;SEND UNTALK COMMAND ON SERIAL BUS
                                ;
.,EDEF 78       SEI             UNTLK  SEI
.,EDF0 20 8E EE JSR $EE8E       JSR    CLKLO
.,EDF3 AD 00 DD LDA $DD00       LDA    D2PRA           ;PULL ATN
.,EDF6 09 08    ORA #$08        ORA    #$08
.,EDF8 8D 00 DD STA $DD00       STA    D2PRA
.,EDFB A9 5F    LDA #$5F        LDA    #$5F            ;UNTALK COMMAND
.:EDFD 2C       .BYTE $2C       .BYT   $2C             ;SKIP TWO BYTES
                                ;SEND UNLISTEN COMMAND ON SERIAL BUS
                                ;
.,EDFE A9 3F    LDA #$3F        UNLSN  LDA #$3F        ;UNLISTEN COMMAND
.,EE00 20 11 ED JSR $ED11              JSR LIST1       ;SEND IT
                                ;
                                ; RELEASE ALL LINES
.,EE03 20 BE ED JSR $EDBE       DLABYE JSR SCATN       ;ALWAYS RELEASE ATN
                                ; DELAY THEN RELEASE CLOCK AND DATA
                                ;
.,EE06 8A       TXA             DLADLH TXA             ;DELAY APPROX 60 US
.,EE07 A2 0A    LDX #$0A               LDX #10
.,EE09 CA       DEX             DLAD00 DEX
.,EE0A D0 FD    BNE $EE09              BNE DLAD00
.,EE0C AA       TAX                    TAX
.,EE0D 20 85 EE JSR $EE85              JSR CLKHI
.,EE10 4C 97 EE JMP $EE97              JMP DATAHI
                                ;INPUT A BYTE FROM SERIAL BUS
                                ;
                                ACPTR
.,EE13 78       SEI                    SEI             ;NO IRQ ALLOWED
.,EE14 A9 00    LDA #$00               LDA #$00        ;SET EOI/ERROR FLAG
.,EE16 85 A5    STA $A5                STA COUNT
.,EE18 20 85 EE JSR $EE85              JSR CLKHI       ;MAKE SURE CLOCK LINE IS RELEASED
.,EE1B 20 A9 EE JSR $EEA9       ACP00A JSR DEBPIA      ;WAIT FOR CLOCK HIGH
.,EE1E 10 FB    BPL $EE1B              BPL ACP00A
                                ;
                                EOIACP
.,EE20 A9 01    LDA #$01               LDA #$01        ;SET TIMER 2 FOR 256US
.,EE22 8D 07 DC STA $DC07              STA D1T2H
.,EE25 A9 19    LDA #$19               LDA #TIMRB
.,EE27 8D 0F DC STA $DC0F              STA D1CRB
.,EE2A 20 97 EE JSR $EE97              JSR DATAHI      ;DATA LINE HIGH (MAKES TIMMING MORE LIKE VIC-20
.,EE2D AD 0D DC LDA $DC0D              LDA D1ICR       ;CLEAR THE TIMER FLAGS<<<<<<<<<<<<
.,EE30 AD 0D DC LDA $DC0D       ACP00  LDA D1ICR
.,EE33 29 02    AND #$02               AND #$02        ;CHECK THE TIMER
.,EE35 D0 07    BNE $EE3E              BNE ACP00B      ;RAN OUT.....
.,EE37 20 A9 EE JSR $EEA9              JSR DEBPIA      ;CHECK THE CLOCK LINE
.,EE3A 30 F4    BMI $EE30              BMI ACP00       ;NO NOT YET
.,EE3C 10 18    BPL $EE56              BPL ACP01       ;YES.....
                                ;
.,EE3E A5 A5    LDA $A5         ACP00B LDA COUNT       ;CHECK FOR ERROR (TWICE THRU TIMEOUTS)
.,EE40 F0 05    BEQ $EE47              BEQ ACP00C
.,EE42 A9 02    LDA #$02               LDA #2
.,EE44 4C B2 ED JMP $EDB2              JMP CSBERR      ; ST = 2 READ TIMEOUT
                                ;
                                ; TIMER RAN OUT DO AN EOI THING
                                ;
.,EE47 20 A0 EE JSR $EEA0       ACP00C JSR DATALO      ;DATA LINE LOW
.,EE4A 20 85 EE JSR $EE85              JSR CLKHI       ; DELAY AND THEN SET DATAHI (FIX FOR 40US C64)
.,EE4D A9 40    LDA #$40               LDA #$40
.,EE4F 20 1C FE JSR $FE1C              JSR UDST        ;OR AN EOI BIT INTO STATUS
.,EE52 E6 A5    INC $A5                INC COUNT       ;GO AROUND AGAIN FOR ERROR CHECK ON EOI
.,EE54 D0 CA    BNE $EE20              BNE EOIACP
                                ;
                                ; DO THE BYTE TRANSFER
                                ;
.,EE56 A9 08    LDA #$08        ACP01  LDA #08         ;SET UP COUNTER
.,EE58 85 A5    STA $A5                STA COUNT
                                ;
.,EE5A AD 00 DD LDA $DD00       ACP03  LDA D2PRA       ;WAIT FOR CLOCK HIGH
.,EE5D CD 00 DD CMP $DD00       CMP    D2PRA           ;DEBOUNCE
.,EE60 D0 F8    BNE $EE5A       BNE    ACP03
.,EE62 0A       ASL             ASL    A               ;SHIFT DATA INTO CARRY
.,EE63 10 F5    BPL $EE5A       BPL    ACP03           ;CLOCK STILL LOW...
.,EE65 66 A4    ROR $A4         ROR    BSOUR1          ;ROTATE DATA IN
                                ;
.,EE67 AD 00 DD LDA $DD00       ACP03A LDA D2PRA       ;WAIT FOR CLOCK LOW
.,EE6A CD 00 DD CMP $DD00       CMP    D2PRA           ;DEBOUNCE
.,EE6D D0 F8    BNE $EE67       BNE    ACP03A
.,EE6F 0A       ASL             ASL    A
.,EE70 30 F5    BMI $EE67       BMI    ACP03A
.,EE72 C6 A5    DEC $A5         DEC    COUNT
.,EE74 D0 E4    BNE $EE5A       BNE    ACP03           ;MORE BITS.....
                                ;...EXIT...
.,EE76 20 A0 EE JSR $EEA0              JSR DATALO      ;DATA LOW
.,EE79 24 90    BIT $90                BIT STATUS      ;CHECK FOR EOI
.,EE7B 50 03    BVC $EE80              BVC ACP04       ;NONE...
                                ;
.,EE7D 20 06 EE JSR $EE06              JSR DLADLH      ;DELAY THEN SET DATA HIGH
                                ;
.,EE80 A5 A4    LDA $A4         ACP04  LDA BSOUR1
.,EE82 58       CLI                    CLI             ;IRQ IS OK
.,EE83 18       CLC                    CLC             ;GOOD EXIT
.,EE84 60       RTS                    RTS
                                ;
                                CLKHI                  ;SET CLOCK LINE HIGH (INVERTED)
.,EE85 AD 00 DD LDA $DD00              LDA D2PRA
.,EE88 29 EF    AND #$EF               AND #$FF-$10
.,EE8A 8D 00 DD STA $DD00              STA D2PRA
.,EE8D 60       RTS                    RTS
                                ;
                                CLKLO                  ;SET CLOCK LINE LOW  (INVERTED)
.,EE8E AD 00 DD LDA $DD00              LDA D2PRA
.,EE91 09 10    ORA #$10               ORA #$10
.,EE93 8D 00 DD STA $DD00              STA D2PRA
.,EE96 60       RTS                    RTS
                                ;
                                ;
                                DATAHI                 ;SET DATA LINE HIGH (INVERTED)
.,EE97 AD 00 DD LDA $DD00              LDA D2PRA
.,EE9A 29 DF    AND #$DF               AND #$FF-$20
.,EE9C 8D 00 DD STA $DD00              STA D2PRA
.,EE9F 60       RTS                    RTS
                                ;
                                DATALO                 ;SET DATA LINE LOW  (INVERTED)
.,EEA0 AD 00 DD LDA $DD00              LDA D2PRA
.,EEA3 09 20    ORA #$20               ORA #$20
.,EEA5 8D 00 DD STA $DD00              STA D2PRA
.,EEA8 60       RTS                    RTS
                                                       ;
.,EEA9 AD 00 DD LDA $DD00       DEBPIA LDA D2PRA       ;DEBOUNCE THE PIA
.,EEAC CD 00 DD CMP $DD00              CMP D2PRA
.,EEAF D0 F8    BNE $EEA9              BNE DEBPIA
.,EEB1 0A       ASL                    ASL A           ;SHIFT THE DATA BIT INTO THE CARRY...
.,EEB2 60       RTS                    RTS             ;...AND THE CLOCK INTO NEG FLAG
                                ;
                                W1MS                   ;DELAY 1MS USING LOOP
.,EEB3 8A       TXA                    TXA             ;SAVE .X
.,EEB4 A2 B8    LDX #$B8               LDX #200-16     ;1000US-(1000/500*8=#40US HOLDS)
.,EEB6 CA       DEX             W1MS1  DEX             ;5US LOOP
.,EEB7 D0 FD    BNE $EEB6              BNE W1MS1
.,EEB9 AA       TAX                    TAX             ;RESTORE .X
.,EEBA 60       RTS                    RTS
                                .END
                                .LIB   RS232TRANS
                                ; RSTRAB - ENTRY FOR NMI CONTINUE ROUTINE
                                ; RSTBGN - ENTRY FOR START TRANSMITTER
                                ;
                                ;   RSR - 8/18/80
                                ;
                                ; VARIABLES USED
                                ;   BITTS - # OF BITS TO BE SENT (<>0 NOT DONE)
                                ;   NXTBIT - BYTE CONTAINS NEXT BIT TO BE SENT
                                ;   ROPRTY - BYTE CONTAINS PARITY BIT CALCULATED
                                ;   RODATA - STORES DATA BYTE CURRENTLY BEING TRANSMITTED
                                ;   RODBS - OUTPUT BUFFER INDEX START
                                ;   RODBE - OUTPUT BUFFER INDEX END
                                ;   IF RODBS=RODBE THEN BUFFER EMPTY
                                ;   ROBUF - INDIRECT POINTER TO DATA BUFFER
                                ;   RSSTAT - RS-232 STATUS BYTE
                                ;
                                ;   XXX US - NORMAL BIT PATH
                                ;   XXX US - WORST CASE PARITY BIT PATH
                                ;   XXX US - STOP BIT PATH
                                ;   XXX US - START BIT PATH
                                ;
.,EEBB A5 B4    LDA $B4         RSTRAB LDA BITTS       ;CHECK FOR PLACE IN BYTE...
.,EEBD F0 47    BEQ $EF06              BEQ RSTBGN      ;...DONE, =0 START NEXT
                                ;
.,EEBF 30 3F    BMI $EF00              BMI RST050      ;...DOING STOP BITS
                                ;
.,EEC1 46 B6    LSR $B6                LSR RODATA      ;SHIFT DATA INTO CARRY
.,EEC3 A2 00    LDX #$00               LDX #00         ;PREPARE FOR A ZERO
.,EEC5 90 01    BCC $EEC8              BCC RST005      ;YES...A ZERO
.,EEC7 CA       DEX                    DEX             ;NO...MAKE AN $FF
.,EEC8 8A       TXA             RST005 TXA             ;READY TO SEND
                                ;
.,EEC9 45 BD    EOR $BD                EOR ROPRTY      ;CALC INTO PARITY
.,EECB 85 BD    STA $BD                STA ROPRTY
                                ;
.,EECD C6 B4    DEC $B4                DEC BITTS       ;BIT COUNT DOWN
.,EECF F0 06    BEQ $EED7              BEQ RST010      ;WANT A PARITY INSTEAD
                                ;
.,EED1 8A       TXA             RSTEXT TXA             ;CALC BIT WHOLE TO SEND
.,EED2 29 04    AND #$04               AND #$04        ;GOES OUT D2PA2
.,EED4 85 B5    STA $B5                STA NXTBIT
.,EED6 60       RTS                    RTS
                                ; CALCULATE PARITY
                                ;  NXTBIT =0 UPON ENTRY
                                ;
.,EED7 A9 20    LDA #$20        RST010 LDA #$20        ;CHECK 6551 REG BITS
.,EED9 2C 94 02 BIT $0294              BIT M51CDR
.,EEDC F0 14    BEQ $EEF2              BEQ RSPNO       ;...NO PARITY, SEND A STOP
.,EEDE 30 1C    BMI $EEFC              BMI RST040      ;...NOT REAL PARITY
.,EEE0 70 14    BVS $EEF6              BVS RST030      ;...EVEN PARITY
                                ;
.,EEE2 A5 BD    LDA $BD                LDA ROPRTY      ;CALC ODD PARITY
.,EEE4 D0 01    BNE $EEE7              BNE RSPEXT      ;CORRECT GUESS
                                ;
.,EEE6 CA       DEX             RSWEXT DEX             ;WRONG GUESS...ITS A ONE
                                ;
.,EEE7 C6 B4    DEC $B4         RSPEXT DEC BITTS       ;ONE STOP BIT ALWAYS
.,EEE9 AD 93 02 LDA $0293              LDA M51CTR      ;CHECK # OF STOP BITS
.,EEEC 10 E3    BPL $EED1              BPL RSTEXT      ;...ONE
.,EEEE C6 B4    DEC $B4                DEC BITTS       ;...TWO
.,EEF0 D0 DF    BNE $EED1              BNE RSTEXT      ;JUMP
                                ;
                                RSPNO                  ;LINE TO SEND CANNOT BE PB0
.,EEF2 E6 B4    INC $B4                INC BITTS       ;COUNTS AS ONE STOP BIT
.,EEF4 D0 F0    BNE $EEE6              BNE RSWEXT      ;JUMP TO FLIP TO ONE
                                ;
.,EEF6 A5 BD    LDA $BD         RST030 LDA ROPRTY      ;EVEN PARITY
.,EEF8 F0 ED    BEQ $EEE7              BEQ RSPEXT      ;CORRECT GUESS...EXIT
.,EEFA D0 EA    BNE $EEE6              BNE RSWEXT      ;WRONG...FLIP AND EXIT
                                ;
.,EEFC 70 E9    BVS $EEE7       RST040 BVS RSPEXT      ;WANTED SPACE
.,EEFE 50 E6    BVC $EEE6              BVC RSWEXT      ; WANTED MARK
                                ; STOP BITS
                                ;
.,EF00 E6 B4    INC $B4         RST050 INC BITTS       ;STOP BIT COUNT TOWARDS ZERO
.,EF02 A2 FF    LDX #$FF               LDX #$FF        ;SEND STOP BIT
.,EF04 D0 CB    BNE $EED1              BNE RSTEXT      ;JUMP TO EXIT
                                ;
                                ; RSTBGN - ENTRY TO START BYTE TRANS
                                ;
.,EF06 AD 94 02 LDA $0294       RSTBGN LDA M51CDR      ;CHECK FOR 3/X LINE
.,EF09 4A       LSR                    LSR A
.,EF0A 90 07    BCC $EF13              BCC RST060      ;3 LINE...NO CHECK
.,EF0C 2C 01 DD BIT $DD01              BIT D2PRB       ;CHECK FOR...
.,EF0F 10 1D    BPL $EF2E              BPL DSRERR      ;...DSR ERROR
.,EF11 50 1E    BVC $EF31              BVC CTSERR      ;...CTS ERROR
                                ;
                                ; SET UP TO SEND NEXT BYTE
                                ;
.,EF13 A9 00    LDA #$00        RST060 LDA #0
.,EF15 85 BD    STA $BD                STA ROPRTY      ;ZERO PARITY
.,EF17 85 B5    STA $B5                STA NXTBIT      ;SEND START BIT
.,EF19 AE 98 02 LDX $0298              LDX BITNUM      ;GET # OF BITS
.,EF1C 86 B4    STX $B4         RST070 STX BITTS       ;BITTS=#OF BITTS+1
                                ;
.,EF1E AC 9D 02 LDY $029D       RST080 LDY RODBS       ;CHECK BUFFER POINTERS
.,EF21 CC 9E 02 CPY $029E              CPY RODBE
.,EF24 F0 13    BEQ $EF39              BEQ RSODNE      ;ALL DONE...
                                ;
.,EF26 B1 F9    LDA ($F9),Y            LDA (ROBUF)Y    ;GET DATA...
.,EF28 85 B6    STA $B6                STA RODATA      ;...INTO BYTE BUFFER
.,EF2A EE 9D 02 INC $029D              INC RODBS       ;MOVE POINTER TO NEXT
.,EF2D 60       RTS                    RTS
                                ; SET ERRORS
                                ;
.,EF2E A9 40    LDA #$40        DSRERR LDA #$40        ;DSR GONE ERROR
.:EF30 2C       .BYTE $2C              .BYT $2C
.,EF31 A9 10    LDA #$10        CTSERR LDA #$10        ;CTS GONE ERROR
.,EF33 0D 97 02 ORA $0297              ORA RSSTAT
.,EF36 8D 97 02 STA $0297              STA RSSTAT
                                ;
                                ; ERRORS TURN OFF T1
                                ;
.,EF39 A9 01    LDA #$01        RSODNE LDA #$01        ;KILL T1 NMI
                                ;ENTRY TO TURN OFF AN ENABLED NMI...
.,EF3B 8D 0D DD STA $DD0D       OENABL STA D2ICR       ;TOSS BAD/OLD NMI
.,EF3E 4D A1 02 EOR $02A1              EOR ENABL       ;FLIP ENABLE
.,EF41 09 80    ORA #$80               ORA #$80        ;ENABLE GOOD NMI'S
.,EF43 8D A1 02 STA $02A1              STA ENABL
.,EF46 8D 0D DD STA $DD0D              STA D2ICR
.,EF49 60       RTS                    RTS
                                ; BITCNT - CAL # OF BITS TO BE SENT
                                ;   RETURNS #OF BITS+1
                                ;
.,EF4A A2 09    LDX #$09        BITCNT LDX #9          ;CALC WORD LENGTH
.,EF4C A9 20    LDA #$20               LDA #$20
.,EF4E 2C 93 02 BIT $0293              BIT M51CTR
.,EF51 F0 01    BEQ $EF54              BEQ BIT010
.,EF53 CA       DEX                    DEX             ;BIT 5 HIGH IS A 7 OR 5
.,EF54 50 02    BVC $EF58       BIT010 BVC BIT020
.,EF56 CA       DEX                    DEX             ;BIT 6 HIGH IS A 6 OR 5
.,EF57 CA       DEX                    DEX
.,EF58 60       RTS             BIT020 RTS
                                .END
                                .LIB   RS232RCVR
                                ; RSRCVR - NMI ROUTINE TO COLLECT
                                ;  DATA INTO BYTES
                                ;
                                ; RSR 8/18/80
                                ;
                                ; VARIABLES USED
                                ;   INBIT - INPUT BIT VALUE
                                ;   BITCI - BIT COUNT IN
                                ;   RINONE - FLAG FOR START BIT CHECK <>0 START BIT
                                ;   RIDATA - BYTE INPUT BUFFER
                                ;   RIPRTY - HOLDS BYTE INPUT PARITY
                                ;   RIBUF - INDIRECT POINTER TO DATA BUFFER
                                ;   RIDBE - INPUT BUFFER INDEX TO END
                                ;   RIDBS - INPUT BUFFER POINTER TO START
                                ;   IF RIDBE=RIDBS THEN INPUT BUFFER EMPTY
                                ;
.,EF59 A6 A9    LDX $A9         RSRCVR LDX RINONE      ;CHECK FOR START BIT
.,EF5B D0 33    BNE $EF90              BNE RSRTRT      ;WAS START BIT
                                ;
.,EF5D C6 A8    DEC $A8                DEC BITCI       ;CHECK WHERE WE ARE IN INPUT...
.,EF5F F0 36    BEQ $EF97              BEQ RSR030      ;HAVE A FULL BYTE
.,EF61 30 0D    BMI $EF70              BMI RSR020      ;GETTING STOP BITS
                                ;
                                ; CALC PARITY
                                ;
.,EF63 A5 A7    LDA $A7                LDA INBIT       ;GET DATA UP
.,EF65 45 AB    EOR $AB                EOR RIPRTY      ;CALC NEW PARITY
.,EF67 85 AB    STA $AB                STA RIPRTY
                                ;
                                ; SHIFT DATA BIT IN
                                ;
.,EF69 46 A7    LSR $A7                LSR INBIT       ;IN BIT POS 0
.,EF6B 66 AA    ROR $AA                ROR RIDATA      ;C INTO DATA
                                ;
                                ; EXIT
                                ;
.,EF6D 60       RTS             RSREXT RTS
                                ; HAVE STOP BIT, SO STORE IN BUFFER
                                ;
.,EF6E C6 A8    DEC $A8         RSR018 DEC BITCI       ;NO PARITY, DEC SO CHECK WORKS
.,EF70 A5 A7    LDA $A7         RSR020 LDA INBIT       ;GET DATA...
.,EF72 F0 67    BEQ $EFDB              BEQ RSR060      ;...ZERO, AN ERROR?
                                ;
.,EF74 AD 93 02 LDA $0293              LDA M51CTR      ;CHECK FOR CORRECT # OF STOP BITS
.,EF77 0A       ASL                    ASL A           ;CARRY TELL HOW MAY STOP BITS
.,EF78 A9 01    LDA #$01               LDA #01
.,EF7A 65 A8    ADC $A8                ADC BITCI
.,EF7C D0 EF    BNE $EF6D              BNE RSREXT      ;NO..EXIT
                                ;
                                ; RSRABL - ENABLE TO RECIEVE A BYTE
                                ;
.,EF7E A9 90    LDA #$90        RSRABL LDA #$90        ;ENABLE FLAG FOR NEXT BYTE
.,EF80 8D 0D DD STA $DD0D              STA D2ICR       ;TOSS BAD/OLD NMI
.,EF83 0D A1 02 ORA $02A1              ORA ENABL       ;MARK IN ENABLE REGISTER***********
.,EF86 8D A1 02 STA $02A1              STA ENABL       ;RE-ENABLED BY JMP OENABL
.,EF89 85 A9    STA $A9                STA RINONE      ;FLAG FOR START BIT
                                ;
.,EF8B A9 02    LDA #$02        RSRSXT LDA #$02        ;DISABLE T2
.,EF8D 4C 3B EF JMP $EF3B              JMP OENABL      ;FLIP-OFF ENABL***************
                                ; RECIEVER START BIT CHECK
                                ;
.,EF90 A5 A7    LDA $A7         RSRTRT LDA INBIT       ;CHECK IF SPACE
.,EF92 D0 EA    BNE $EF7E              BNE RSRABL      ;BAD...TRY AGAIN
.,EF94 85 A9    STA $A9                STA RINONE      ;GOOD...DISABLE FLAG
.,EF96 60       RTS                    RTS             ;AND EXIT
                                ;
                                ; PUT DATA IN BUFFER (AT PARITY TIME)
                                ;
.,EF97 AC 9B 02 LDY $029B       RSR030 LDY RIDBE       ;GET END
.,EF9A C8       INY                    INY
.,EF9B CC 9C 02 CPY $029C              CPY RIDBS       ;HAVE WE PASSED START?
.,EF9E F0 2A    BEQ $EFCA              BEQ RECERR      ;YES...ERROR
                                ;
.,EFA0 8C 9B 02 STY $029B              STY RIDBE       ;MOVE RIDBE FOWARD
.,EFA3 88       DEY                    DEY
                                ;
.,EFA4 A5 AA    LDA $AA                LDA RIDATA      ;GET BYTE BUFFER UP
.,EFA6 AE 98 02 LDX $0298              LDX BITNUM      ;SHIFT UNTILL FULL BYTE
.,EFA9 E0 09    CPX #$09        RSR031 CPX #9          ;ALWAYS 8 BITS
.,EFAB F0 04    BEQ $EFB1              BEQ RSR032
.,EFAD 4A       LSR                    LSR A           ;FILL WITH ZEROS
.,EFAE E8       INX                    INX
.,EFAF D0 F8    BNE $EFA9              BNE RSR031
                                ;
.,EFB1 91 F7    STA ($F7),Y     RSR032 STA (RIBUF)Y    ;DATA TO PAGE BUFFER
                                ;
                                ; PARITY CHECKING
                                ;
.,EFB3 A9 20    LDA #$20               LDA #$20        ;CHECK 6551 COMMAND REGISTER
.,EFB5 2C 94 02 BIT $0294              BIT M51CDR
.,EFB8 F0 B4    BEQ $EF6E              BEQ RSR018      ;NO PARITY BIT SO STOP BIT
.,EFBA 30 B1    BMI $EF6D              BMI RSREXT      ;NO PARITY CHECK
                                ;
                                ; CHECK CALC PARITY
                                ;
.,EFBC A5 A7    LDA $A7                LDA INBIT
.,EFBE 45 AB    EOR $AB                EOR RIPRTY      ;PUT IN WITH PARITY
.,EFC0 F0 03    BEQ $EFC5              BEQ RSR050      ;EVEN PARITY
.,EFC2 70 A9    BVS $EF6D              BVS RSREXT      ;ODD...OKAY SO EXIT
.:EFC4 2C       .BYTE $2C              .BYT $2C        ;SKIP TWO
.,EFC5 50 A6    BVC $EF6D       RSR050 BVC RSREXT      ;EVEN...OKAY SO EXIT
                                ;
                                ; ERRORS REPORTED
.,EFC7 A9 01    LDA #$01               LDA #1          ;PARITY ERROR
.:EFC9 2C       .BYTE $2C              .BYT $2C
.,EFCA A9 04    LDA #$04        RECERR LDA #$4         ;RECIEVER OVERRUN
.:EFCC 2C       .BYTE $2C       .BYT   $2C
.,EFCD A9 80    LDA #$80        BREAKE LDA #$80        ;BREAK DETECTED
.:EFCF 2C       .BYTE $2C              .BYT $2C
.,EFD0 A9 02    LDA #$02        FRAMEE LDA #$02        ;FRAME ERROR
.,EFD2 0D 97 02 ORA $0297       ERR232 ORA RSSTAT
.,EFD5 8D 97 02 STA $0297              STA RSSTAT
.,EFD8 4C 7E EF JMP $EF7E              JMP RSRABL      ;BAD EXIT SO HANG ##????????##
                                ;
                                ; CHECK FOR ERRORS
                                ;
.,EFDB A5 AA    LDA $AA         RSR060 LDA RIDATA      ;EXPECTING STOP...
.,EFDD D0 F1    BNE $EFD0              BNE FRAMEE      ;FRAME ERROR
.,EFDF F0 EC    BEQ $EFCD              BEQ BREAKE      ;COULD BE A BREAK
                                .END
                                .LIB   RS232INOUT
                                ; OUTPUT A FILE OVER USR PORT
                                ;  USING RS232
                                ;
.,EFE1 85 9A    STA $9A         CKO232 STA DFLTO       ;SET DEFAULT OUT
.,EFE3 AD 94 02 LDA $0294              LDA M51CDR      ;CHECK FOR 3/X LINE
.,EFE6 4A       LSR                    LSR A
.,EFE7 90 29    BCC $F012              BCC CKO100      ;3LINE...NO TURN AROUND
                                ;
                                ;*TURN AROUND LOGIC
                                ;
                                ; CHECK FOR DSR AND RTS
                                ;
.,EFE9 A9 02    LDA #$02               LDA #$02        ;BIT RTS IS ON
.,EFEB 2C 01 DD BIT $DD01              BIT D2PRB
.,EFEE 10 1D    BPL $F00D              BPL CKDSRX      ;NO DSR...ERROR
.,EFF0 D0 20    BNE $F012              BNE CKO100      ;RTS...OUTPUTING OR FULL DUPLEX
                                ;
                                ; CHECK FOR ACTIVE INPUT
                                ;  RTS WILL BE LOW IF CURRENTLY INPUTING
                                ;
.,EFF2 AD A1 02 LDA $02A1       CKO020 LDA ENABL
.,EFF5 29 02    AND #$02               AND #$02        ;LOOK AT IER FOR T2
.,EFF7 D0 F9    BNE $EFF2              BNE CKO020      ;HANG UNTILL INPUT DONE
                                ;
                                ; WAIT FOR CTS TO BE OFF AS SPEC REQS
                                ;
.,EFF9 2C 01 DD BIT $DD01       CKO030 BIT D2PRB
.,EFFC 70 FB    BVS $EFF9              BVS CKO030
                                ;
                                ; TURN ON RTS
                                ;
.,EFFE AD 01 DD LDA $DD01              LDA D2PRB
.,F001 09 02    ORA #$02               ORA #$02
.,F003 8D 01 DD STA $DD01              STA D2PRB
                                ;
                                ; WAIT FOR CTS TO GO ON
                                ;
.,F006 2C 01 DD BIT $DD01       CKO040 BIT D2PRB
.,F009 70 07    BVS $F012              BVS CKO100      ;DONE...
.,F00B 30 F9    BMI $F006              BMI CKO040      ;WE STILL HAVE DSR
                                ;
.,F00D A9 40    LDA #$40        CKDSRX LDA #$40        ;A DATA SET READY ERROR
.,F00F 8D 97 02 STA $0297              STA RSSTAT      ;MAJOR ERROR....WILL REQUIRE REOPEN
                                ;
.,F012 18       CLC             CKO100 CLC             ;NO ERROR
.,F013 60       RTS                    RTS
                                ;
                                ; BSO232 - OUTPUT A CHAR RS232
                                ;   DATA PASSED IN T1 FROM BSOUT
                                ;
                                ; HANG LOOP FOR BUFFER FULL
                                ;
.,F014 20 28 F0 JSR $F028       BSOBAD JSR BSO100      ;KEEP TRYING TO START SYSTEM...
                                ;
                                ; BUFFER HANDLER
                                ;
.,F017 AC 9E 02 LDY $029E       BSO232 LDY RODBE
.,F01A C8       INY                    INY
.,F01B CC 9D 02 CPY $029D              CPY RODBS       ;CHECK FOR BUFFER FULL
.,F01E F0 F4    BEQ $F014              BEQ BSOBAD      ;HANG IF SO...TRYING TO RESTART
.,F020 8C 9E 02 STY $029E              STY RODBE       ;INDICATE NEW START
.,F023 88       DEY                    DEY
.,F024 A5 9E    LDA $9E                LDA T1          ;GET DATA...
.,F026 91 F9    STA ($F9),Y            STA (ROBUF)Y    ;STORE DATA
                                ;
                                ; SET UP IF NECESSARY TO OUTPUT
                                ;
.,F028 AD A1 02 LDA $02A1       BSO100 LDA ENABL       ;CHECK FOR A T1 NMI ENABLE
.,F02B 4A       LSR                    LSR A           ;BIT 0
.,F02C B0 1E    BCS $F04C              BCS BSO120      ;RUNNING....SO EXIT
                                ;
                                ; SET UP T1 NMI'S
                                ;
.,F02E A9 10    LDA #$10        BSO110 LDA #$10        ;TURN OFF TIMER TO PREVENT FALSE START...
.,F030 8D 0E DD STA $DD0E              STA D2CRA
.,F033 AD 99 02 LDA $0299              LDA BAUDOF      ;SET UP TIMER1
.,F036 8D 04 DD STA $DD04              STA D2T1L
.,F039 AD 9A 02 LDA $029A              LDA BAUDOF+1
.,F03C 8D 05 DD STA $DD05              STA D2T1H
.,F03F A9 81    LDA #$81               LDA #$81
.,F041 20 3B EF JSR $EF3B              JSR OENABL
.,F044 20 06 EF JSR $EF06              JSR RSTBGN      ;SET UP TO SEND (WILL STOP ON CTS OR DSR ERROR)
.,F047 A9 11    LDA #$11               LDA #$11        ;TURN ON TIMER
.,F049 8D 0E DD STA $DD0E              STA D2CRA
.,F04C 60       RTS             BSO120 RTS
                                ; INPUT A FILE OVER USER PORT
                                ;  USING RS232
                                ;
.,F04D 85 99    STA $99         CKI232 STA DFLTN       ;SET DEFAULT INPUT
                                ;
.,F04F AD 94 02 LDA $0294              LDA M51CDR      ;CHECK FOR 3/X LINE
.,F052 4A       LSR                    LSR A
.,F053 90 28    BCC $F07D              BCC CKI100      ;3 LINE...NO HANDSHAKE
                                ;
.,F055 29 08    AND #$08               AND #$08        ;FULL/HALF CHECK (BYTE SHIFTED ABOVE)
.,F057 F0 24    BEQ $F07D              BEQ CKI100      ;FULL...NO HANDSHAKE
                                ;
                                ;*TURN AROUND LOGIC
                                ;
                                ; CHECK IF DSR AND NOT RTS
                                ;
.,F059 A9 02    LDA #$02               LDA #$02        ;BIT RTS IS ON
.,F05B 2C 01 DD BIT $DD01              BIT D2PRB
.,F05E 10 AD    BPL $F00D              BPL CKDSRX      ;NO DSR...ERROR
.,F060 F0 22    BEQ $F084              BEQ CKI110      ;RTS LOW...IN CORRECT MODE
                                ;
                                ; WAIT FOR ACTIVE OUTPUT TO BE DONE
                                ;
.,F062 AD A1 02 LDA $02A1       CKI010 LDA ENABL
.,F065 4A       LSR                    LSR A           ;CHECK T1 (BIT 0)
.,F066 B0 FA    BCS $F062              BCS CKI010
                                ;
                                ; TURN OFF RTS
                                ;
.,F068 AD 01 DD LDA $DD01              LDA D2PRB
.,F06B 29 FD    AND #$FD               AND #$FF-02
.,F06D 8D 01 DD STA $DD01              STA D2PRB
                                ;
                                ; WAIT FOR DCD TO GO HIGH (IN SPEC)
                                ;
.,F070 AD 01 DD LDA $DD01       CKI020 LDA D2PRB
.,F073 29 04    AND #$04               AND #$04
.,F075 F0 F9    BEQ $F070              BEQ CKI020
                                ;
                                ; ENABLE FLAG FOR RS232 INPUT
                                ;
.,F077 A9 90    LDA #$90        CKI080 LDA #$90
.,F079 18       CLC                    CLC             ;NO ERROR
.,F07A 4C 3B EF JMP $EF3B              JMP OENABL      ;FLAG IN ENABL**********
                                ;
                                ; IF NOT 3 LINE HALF THEN...
                                ;  SEE IF WE NEED TO TURN ON FLAG
                                ;
.,F07D AD A1 02 LDA $02A1       CKI100 LDA ENABL       ;CHECK FOR FLAG OR T2 ACTIVE
.,F080 29 12    AND #$12               AND #$12
.,F082 F0 F3    BEQ $F077              BEQ CKI080      ;NO NEED TO TURN ON
.,F084 18       CLC             CKI110 CLC             ;NO ERROR
.,F085 60       RTS                    RTS
                                ; BSI232 - INPUT A CHAR RS232
                                ;
                                ; BUFFER HANDLER
                                ;
.,F086 AD 97 02 LDA $0297       BSI232 LDA RSSTAT      ;GET STATUS UP TO CHANGE...
.,F089 AC 9C 02 LDY $029C              LDY RIDBS       ;GET LAST BYTE ADDRESS
.,F08C CC 9B 02 CPY $029B              CPY RIDBE       ;SEE IF BUFFER EMPTY
.,F08F F0 0B    BEQ $F09C              BEQ BSI010      ;RETURN A NULL IF NO CHAR
                                ;
.,F091 29 F7    AND #$F7               AND #$FF-$08    ;CLEAR BUFFER EMPTY STATUS
.,F093 8D 97 02 STA $0297              STA RSSTAT
.,F096 B1 F7    LDA ($F7),Y            LDA (RIBUF)Y    ;GET LAST CHAR
.,F098 EE 9C 02 INC $029C              INC RIDBS       ;INC TO NEXT POS
                                ;
                                ; RECEIVER ALWAYS RUNS
                                ;
.,F09B 60       RTS                    RTS
                                ;
.,F09C 09 08    ORA #$08        BSI010 ORA #$08        ;SET BUFFER EMPTY STATUS
.,F09E 8D 97 02 STA $0297              STA RSSTAT
.,F0A1 A9 00    LDA #$00               LDA #$0         ;RETURN A NULL
.,F0A3 60       RTS                    RTS
                                ; RSP232 - PROTECT SERIAL/CASS FROM RS232 NMI'S
                                ;
.,F0A4 48       PHA             RSP232 PHA             ;SAVE .A
.,F0A5 AD A1 02 LDA $02A1              LDA ENABL       ;DOES RS232 HAVE ANY ENABLES?
.,F0A8 F0 11    BEQ $F0BB              BEQ RSPOK       ;NO...
.,F0AA AD A1 02 LDA $02A1       RSPOFF LDA ENABL       ;WAIT UNTILL DONE
.,F0AD 29 03    AND #$03               AND #%00000011  ; WITH T1 & T2
.,F0AF D0 F9    BNE $F0AA              BNE RSPOFF
.,F0B1 A9 10    LDA #$10               LDA #%00010000  ; DISABLE FLAG (NEED TO RENABLE IN USER CODE)
.,F0B3 8D 0D DD STA $DD0D              STA D2ICR       ;TURN OF ENABL************
.,F0B6 A9 00    LDA #$00               LDA #0
.,F0B8 8D A1 02 STA $02A1              STA ENABL       ;CLEAR ALL ENABLS
.,F0BB 68       PLA             RSPOK  PLA             ;ALL DONE
.,F0BC 60       RTS                    RTS
                                .END
                                .LIB   MESSAGES
                                MS1    .BYT $D,'I/O ERROR ',$A3
                                MS5    .BYT $D,'SEARCHING',$A0
                                MS6    .BYT 'FOR',$A0
                                MS7    .BYT $D,'PRESS PLAY ON TAP',$C5
                                MS8    .BYT 'PRESS RECORD & PLAY ON TAP',$C5
                                MS10   .BYT $D,'LOADIN',$C7
                                MS11   .BYT $D,'SAVING',$A0
                                MS21   .BYT $D,'VERIFYIN',$C7
                                MS17   .BYT $D,'FOUND',$A0
                                MS18   .BYT $D,'OK',$8D
                                ; MS34 .BYT $D,'MONITOR',$8D
.:F0BD 0D 49 2F 4F 20 45 52 52  ; MS36 .BYT $D,'BREA',$CB
                                ;PRINT MESSAGE TO SCREEN ONLY IF
                                ;OUTPUT ENABLED
                                ;
.,F12B 24 9D    BIT $9D         SPMSG  BIT MSGFLG      ;PRINTING MESSAGES?
.,F12D 10 0D    BPL $F13C       BPL    MSG10           ;NO...
.,F12F B9 BD F0 LDA $F0BD,Y     MSG    LDA MS1,Y
.,F132 08       PHP             PHP
.,F133 29 7F    AND #$7F        AND    #$7F
.,F135 20 D2 FF JSR $FFD2       JSR    BSOUT
.,F138 C8       INY             INY
.,F139 28       PLP             PLP
.,F13A 10 F3    BPL $F12F       BPL    MSG
.,F13C 18       CLC             MSG10  CLC
.,F13D 60       RTS             RTS
                                .END
                                .LIB   CHANNELIO
                                ;***************************************
                                ;* GETIN -- GET CHARACTER FROM CHANNEL *
                                ;*      CHANNEL IS DETERMINED BY DFLTN.*
                                ;* IF DEVICE IS 0, KEYBOARD QUEUE IS   *
                                ;* EXAMINED AND A CHARACTER REMOVED IF *
                                ;* AVAILABLE.  IF QUEUE IS EMPTY, Z    *
                                ;* FLAG IS RETURNED SET.  DEVICES 1-31 *
                                ;* ADVANCE TO BASIN.                   *
                                ;***************************************
                                ;
.,F13E A5 99    LDA $99         NGETIN LDA DFLTN       ;CHECK DEVICE
.,F140 D0 08    BNE $F14A       BNE    GN10            ;NOT KEYBOARD
                                ;
.,F142 A5 C6    LDA $C6         LDA    NDX             ;QUEUE INDEX
.,F144 F0 0F    BEQ $F155       BEQ    GN20            ;NOBODY THERE...EXIT
                                ;
.,F146 78       SEI             SEI
.,F147 4C B4 E5 JMP $E5B4       JMP    LP2             ;GO REMOVE A CHARACTER
                                ;
.,F14A C9 02    CMP #$02        GN10   CMP #2          ;IS IT RS-232
.,F14C D0 18    BNE $F166       BNE    BN10            ;NO...USE BASIN
                                ;
.,F14E 84 97    STY $97         GN232  STY XSAV        ;SAVE .Y, USED IN RS232
.,F150 20 86 F0 JSR $F086              JSR BSI232
.,F153 A4 97    LDY $97                LDY XSAV        ;RESTORE .Y
.,F155 18       CLC             GN20   CLC             ;GOOD RETURN
.,F156 60       RTS                    RTS
                                ;***************************************
                                ;* BASIN-- INPUT CHARACTER FROM CHANNEL*
                                ;*     INPUT DIFFERS FROM GET ON DEVICE*
                                ;* #0 FUNCTION WHICH IS KEYBOARD. THE  *
                                ;* SCREEN EDITOR MAKES READY AN ENTIRE *
                                ;* LINE WHICH IS PASSED CHAR BY CHAR   *
                                ;* UP TO THE CARRIAGE RETURN.  OTHER   *
                                ;* DEVICES ARE:                        *
                                ;*      0 -- KEYBOARD                  *
                                ;*      1 -- CASSETTE #1               *
                                ;*      2 -- RS232                     *
                                ;*      3 -- SCREEN                    *
                                ;*   4-31 -- SERIAL BUS                *
                                ;***************************************
                                ;
.,F157 A5 99    LDA $99         NBASIN LDA DFLTN       ;CHECK DEVICE
.,F159 D0 0B    BNE $F166       BNE    BN10            ;IS NOT KEYBOARD...
                                ;
                                ;INPUT FROM KEYBOARD
                                ;
.,F15B A5 D3    LDA $D3         LDA    PNTR            ;SAVE CURRENT...
.,F15D 85 CA    STA $CA         STA    LSTP            ;... CURSOR COLUMN
.,F15F A5 D6    LDA $D6         LDA    TBLX            ;SAVE CURRENT...
.,F161 85 C9    STA $C9         STA    LSXP            ;... LINE NUMBER
.,F163 4C 32 E6 JMP $E632       JMP    LOOP5           ;BLINK CURSOR UNTIL RETURN
                                ;
.,F166 C9 03    CMP #$03        BN10   CMP #3          ;IS INPUT FROM SCREEN?
.,F168 D0 09    BNE $F173       BNE    BN20            ;NO...
                                ;
.,F16A 85 D0    STA $D0         STA    CRSW            ;FAKE A CARRIAGE RETURN
.,F16C A5 D5    LDA $D5         LDA    LNMX            ;SAY WE ENDED...
.,F16E 85 C8    STA $C8         STA    INDX            ;...UP ON THIS LINE
.,F170 4C 32 E6 JMP $E632       JMP    LOOP5           ;PICK UP CHARACTERS
                                ;
.,F173 B0 38    BCS $F1AD       BN20   BCS BN30        ;DEVICES >3
.,F175 C9 02    CMP #$02        CMP    #2              ;RS232?
.,F177 F0 3F    BEQ $F1B8       BEQ    BN50
                                ;
                                ;INPUT FROM CASSETTE BUFFERS
                                ;
.,F179 86 97    STX $97         STX    XSAV
.,F17B 20 99 F1 JSR $F199       JSR    JTGET
.,F17E B0 16    BCS $F196       BCS    JTG37           ;STOP KEY/ERROR
.,F180 48       PHA             PHA
.,F181 20 99 F1 JSR $F199       JSR    JTGET
.,F184 B0 0D    BCS $F193       BCS    JTG36           ;STOP KEY/ERROR
.,F186 D0 05    BNE $F18D       BNE    JTG35           ;NOT AN END OF FILE
.,F188 A9 40    LDA #$40        LDA    #64             ;TELL USER EOF
.,F18A 20 1C FE JSR $FE1C       JSR    UDST            ;IN STATUS
.,F18D C6 A6    DEC $A6         JTG35  DEC BUFPT
.,F18F A6 97    LDX $97         LDX    XSAV            ;.X PRESERVED
.,F191 68       PLA             PLA                    ;CHARACTER RETURNED
                                ;C-CLEAR FROM JTGET
.,F192 60       RTS             RTS                    ;ALL DONE
                                ;
.,F193 AA       TAX             JTG36  TAX             ;SAVE ERROR INFO
.,F194 68       PLA             PLA                    ;TOSS DATA
.,F195 8A       TXA             TXA                    ;RESTORE ERROR
.,F196 A6 97    LDX $97         JTG37  LDX XSAV        ;RETURN
.,F198 60       RTS             RTS                    ;ERROR RETURN C-SET FROM JTGET
                                ;GET A CHARACTER FROM APPROPRIATE
                                ;CASSETTE BUFFER
                                ;
.,F199 20 0D F8 JSR $F80D       JTGET  JSR JTP20       ;BUFFER POINTER WRAP?
.,F19C D0 0B    BNE $F1A9       BNE    JTG10           ;NO...
.,F19E 20 41 F8 JSR $F841       JSR    RBLK            ;YES...READ NEXT BLOCK
.,F1A1 B0 11    BCS $F1B4       BCS    BN33            ;STOP KEY PRESSED
.,F1A3 A9 00    LDA #$00        LDA    #0
.,F1A5 85 A6    STA $A6         STA    BUFPT           ;POINT TO BEGIN.
.,F1A7 F0 F0    BEQ $F199       BEQ    JTGET           ;BRANCH ALWAYS
                                ;
.,F1A9 B1 B2    LDA ($B2),Y     JTG10  LDA (TAPE1)Y    ;GET CHAR FROM BUF
.,F1AB 18       CLC             CLC                    ;GOOD RETURN
.,F1AC 60       RTS             RTS
                                ;INPUT FROM SERIAL BUS
                                ;
.,F1AD A5 90    LDA $90         BN30   LDA STATUS      ;STATUS FROM LAST
.,F1AF F0 04    BEQ $F1B5       BEQ    BN35            ;WAS GOOD
.,F1B1 A9 0D    LDA #$0D        BN31   LDA #$D         ;BAD...ALL DONE
.,F1B3 18       CLC             BN32   CLC             ;VALID DATA
.,F1B4 60       RTS             BN33   RTS
                                ;
.,F1B5 4C 13 EE JMP $EE13       BN35   JMP ACPTR       ;GOOD...HANDSHAKE
                                ;
                                ;INPUT FROM RS232
                                ;
.,F1B8 20 4E F1 JSR $F14E       BN50   JSR GN232       ;GET INFO
.,F1BB B0 F7    BCS $F1B4       BCS    BN33            ;ERROR RETURN
.,F1BD C9 00    CMP #$00        CMP    #00
.,F1BF D0 F2    BNE $F1B3       BNE    BN32            ;GOOD DATA...EXIT
.,F1C1 AD 97 02 LDA $0297       LDA    RSSTAT          ;CHECK FOR DSR OR DCD ERROR
.,F1C4 29 60    AND #$60        AND    #$60
.,F1C6 D0 E9    BNE $F1B1       BNE    BN31            ;AN ERROR...EXIT WITH C/R
.,F1C8 F0 EE    BEQ $F1B8       BEQ    BN50            ;NO ERROR...STAY IN LOOP
                                ;***************************************
                                ;* BSOUT -- OUT CHARACTER TO CHANNEL   *
                                ;*     DETERMINED BY VARIABLE DFLTO:   *
                                ;*     0 -- INVALID                    *
                                ;*     1 -- CASSETTE #1                *
                                ;*     2 -- RS232                      *
                                ;*     3 -- SCREEN                     *
                                ;*  4-31 -- SERIAL BUS                 *
                                ;***************************************
                                ;
.,F1CA 48       PHA             NBSOUT PHA             ;PRESERVE .A
.,F1CB A5 9A    LDA $9A         LDA    DFLTO           ;CHECK DEVICE
.,F1CD C9 03    CMP #$03        CMP    #3              ;IS IT THE SCREEN?
.,F1CF D0 04    BNE $F1D5       BNE    BO10            ;NO...
                                ;
                                ;PRINT TO CRT
                                ;
.,F1D1 68       PLA             PLA                    ;RESTORE DATA
.,F1D2 4C 16 E7 JMP $E716       JMP    PRT             ;PRINT ON CRT
                                ;
                                BO10
.,F1D5 90 04    BCC $F1DB       BCC    BO20            ;DEVICE 1 OR 2
                                ;
                                ;PRINT TO SERIAL BUS
                                ;
.,F1D7 68       PLA             PLA
.,F1D8 4C DD ED JMP $EDDD       JMP    CIOUT
                                ;
                                ;PRINT TO CASSETTE DEVICES
                                ;
.,F1DB 4A       LSR             BO20   LSR A           ;RS232?
.,F1DC 68       PLA             PLA                    ;GET DATA OFF STACK...
                                ;
.,F1DD 85 9E    STA $9E         CASOUT STA T1          ;PASS DATA IN T1
                                ; CASOUT MUST BE ENTERED WITH CARRY SET!!!
                                ;PRESERVE REGISTERS
                                ;
.,F1DF 8A       TXA             TXA
.,F1E0 48       PHA             PHA
.,F1E1 98       TYA             TYA
.,F1E2 48       PHA             PHA
.,F1E3 90 23    BCC $F208       BCC    BO50            ;C-CLR MEANS DFLTO=2 (RS232)
                                ;
.,F1E5 20 0D F8 JSR $F80D       JSR    JTP20           ;CHECK BUFFER POINTER
.,F1E8 D0 0E    BNE $F1F8       BNE    JTP10           ;HAS NOT REACHED END
.,F1EA 20 64 F8 JSR $F864       JSR    WBLK            ;WRITE FULL BUFFER
.,F1ED B0 0E    BCS $F1FD       BCS    RSTOR           ;ABORT ON STOP KEY
                                ;
                                ;PUT BUFFER TYPE BYTE
                                ;
.,F1EF A9 02    LDA #$02        LDA    #BDF
.,F1F1 A0 00    LDY #$00        LDY    #0
.,F1F3 91 B2    STA ($B2),Y     STA    (TAPE1)Y
                                ;
                                ;RESET BUFFER POINTER
                                ;
.,F1F5 C8       INY             INY                    ;MAKE .Y=1
.,F1F6 84 A6    STY $A6         STY    BUFPT           ;BUFPT=1
                                ;
.,F1F8 A5 9E    LDA $9E         JTP10  LDA T1
.,F1FA 91 B2    STA ($B2),Y     STA    (TAPE1)Y        ;DATA TO BUFFER
                                ;
                                ;RESTORE .X AND .Y
                                ;
.,F1FC 18       CLC             RSTOA  CLC             ;GOOD RETURN
.,F1FD 68       PLA             RSTOR  PLA
.,F1FE A8       TAY             TAY
.,F1FF 68       PLA             PLA
.,F200 AA       TAX             TAX
.,F201 A5 9E    LDA $9E         LDA    T1              ;GET .A FOR RETURN
.,F203 90 02    BCC $F207       BCC    RSTOR1          ;NO ERROR
.,F205 A9 00    LDA #$00        LDA    #00             ;STOP ERROR IF C-SET
.,F207 60       RTS             RSTOR1 RTS
                                ;
                                ;OUTPUT TO RS232
                                ;
.,F208 20 17 F0 JSR $F017       BO50   JSR BSO232      ;PASS DATA THROUGH VARIABLE T1
.,F20B 4C FC F1 JMP $F1FC       JMP    RSTOA           ;GO RESTORE ALL..ALWAYS GOOD
                                .END
                                .LIB   OPENCHANNEL
                                ;***************************************
                                ;* CHKIN -- OPEN CHANNEL FOR INPUT     *
                                ;*                                     *
                                ;* THE NUMBER OF THE LOGICAL FILE TO BE*
                                ;* OPENED FOR INPUT IS PASSED IN .X.   *
                                ;* CHKIN SEARCHES THE LOGICAL FILE     *
                                ;* TO LOOK UP DEVICE AND COMMAND INFO. *
                                ;* ERRORS ARE REPORTED IF THE DEVICE   *
                                ;* WAS NOT OPENED FOR INPUT ,(E.G.     *
                                ;* CASSETTE WRITE FILE), OR THE LOGICAL*
                                ;* FILE HAS NO REFERENCE IN THE TABLES.*
                                ;* DEVICE 0, (KEYBOARD), AND DEVICE 3  *
                                ;* (SCREEN), REQUIRE NO TABLE ENTRIES  *
                                ;* AND ARE HANDLED SEPARATE.           *
                                ;***************************************
                                ;
.,F20E 20 0F F3 JSR $F30F       NCHKIN JSR LOOKUP      ;SEE IF FILE KNOWN
.,F211 F0 03    BEQ $F216       BEQ    JX310           ;YUP...
                                ;
.,F213 4C 01 F7 JMP $F701       JMP    ERROR3          ;NO...FILE NOT OPEN
                                ;
.,F216 20 1F F3 JSR $F31F       JX310  JSR JZ100       ;EXTRACT FILE INFO
                                ;
.,F219 A5 BA    LDA $BA         LDA    FA
.,F21B F0 16    BEQ $F233       BEQ    JX320           ;IS KEYBOARD...DONE.
                                ;
                                ;COULD BE SCREEN, KEYBOARD, OR SERIAL
                                ;
.,F21D C9 03    CMP #$03        CMP    #3
.,F21F F0 12    BEQ $F233       BEQ    JX320           ;IS SCREEN...DONE.
.,F221 B0 14    BCS $F237       BCS    JX330           ;IS SERIAL...ADDRESS IT
.,F223 C9 02    CMP #$02        CMP    #2              ;RS232?
.,F225 D0 03    BNE $F22A       BNE    JX315           ;NO...
                                ;
.,F227 4C 4D F0 JMP $F04D       JMP    CKI232
                                ;
                                ;SOME EXTRA CHECKS FOR TAPE
                                ;
.,F22A A6 B9    LDX $B9         JX315  LDX SA
.,F22C E0 60    CPX #$60        CPX    #$60            ;IS COMMAND A READ?
.,F22E F0 03    BEQ $F233       BEQ    JX320           ;YES...O.K....DONE
                                ;
.,F230 4C 0A F7 JMP $F70A       JMP    ERROR6          ;NOT INPUT FILE
                                ;
.,F233 85 99    STA $99         JX320  STA DFLTN       ;ALL INPUT COME FROM HERE
                                ;
.,F235 18       CLC             CLC                    ;GOOD EXIT
.,F236 60       RTS             RTS
                                ;
                                ;AN SERIAL DEVICE HAS TO BE A TALKER
                                ;
.,F237 AA       TAX             JX330  TAX             ;DEVICE # FOR DFLTO
.,F238 20 09 ED JSR $ED09       JSR    TALK            ;TELL HIM TO TALK
                                ;
.,F23B A5 B9    LDA $B9         LDA    SA              ;A SECOND?
.,F23D 10 06    BPL $F245       BPL    JX340           ;YES...SEND IT
.,F23F 20 CC ED JSR $EDCC       JSR    TKATN           ;NO...LET GO
.,F242 4C 48 F2 JMP $F248       JMP    JX350
                                ;
.,F245 20 C7 ED JSR $EDC7       JX340  JSR TKSA        ;SEND SECOND
                                ;
.,F248 8A       TXA             JX350  TXA
.,F249 24 90    BIT $90         BIT    STATUS          ;DID HE LISTEN?
.,F24B 10 E6    BPL $F233       BPL    JX320           ;YES
                                ;
.,F24D 4C 07 F7 JMP $F707       JMP    ERROR5          ;DEVICE NOT PRESENT
                                ;***************************************
                                ;* CHKOUT -- OPEN CHANNEL FOR OUTPUT     *
                                ;*                                     *
                                ;* THE NUMBER OF THE LOGICAL FILE TO BE*
                                ;* OPENED FOR OUTPUT IS PASSED IN .X.  *
                                ;* CHKOUT SEARCHES THE LOGICAL FILE    *
                                ;* TO LOOK UP DEVICE AND COMMAND INFO. *
                                ;* ERRORS ARE REPORTED IF THE DEVICE   *
                                ;* WAS NOT OPENED FOR INPUT ,(E.G.     *
                                ;* KEYBOARD), OR THE LOGICAL FILE HAS   *
                                ;* REFERENCE IN THE TABLES.             *
                                ;* DEVICE 0, (KEYBOARD), AND DEVICE 3  *
                                ;* (SCREEN), REQUIRE NO TABLE ENTRIES  *
                                ;* AND ARE HANDLED SEPARATE.           *
                                ;***************************************
                                ;
.,F250 20 0F F3 JSR $F30F       NCKOUT JSR LOOKUP      ;IS FILE IN TABLE?
.,F253 F0 03    BEQ $F258       BEQ    CK5             ;YES...
                                ;
.,F255 4C 01 F7 JMP $F701       JMP    ERROR3          ;NO...FILE NOT OPEN
                                ;
.,F258 20 1F F3 JSR $F31F       CK5    JSR JZ100       ;EXTRACT TABLE INFO
                                ;
.,F25B A5 BA    LDA $BA         LDA    FA              ;IS IT KEYBOARD?
.,F25D D0 03    BNE $F262       BNE    CK10            ;NO...SOMETHING ELSE.
                                ;
.,F25F 4C 0D F7 JMP $F70D       CK20   JMP ERROR7      ;YES...NOT OUTPUT FILE
                                ;
                                ;COULD BE SCREEN,SERIAL,OR TAPES
                                ;
.,F262 C9 03    CMP #$03        CK10   CMP #3
.,F264 F0 0F    BEQ $F275       BEQ    CK30            ;IS SCREEN...DONE
.,F266 B0 11    BCS $F279       BCS    CK40            ;IS SERIAL...ADDRESS IT
.,F268 C9 02    CMP #$02        CMP    #2              ;RS232?
.,F26A D0 03    BNE $F26F       BNE    CK15
                                ;
.,F26C 4C E1 EF JMP $EFE1       JMP    CKO232
                                ;
                                ;
                                ;SPECIAL TAPE CHANNEL HANDLING
                                ;
.,F26F A6 B9    LDX $B9         CK15   LDX SA
.,F271 E0 60    CPX #$60        CPX    #$60            ;IS COMMAND READ?
.,F273 F0 EA    BEQ $F25F       BEQ    CK20            ;YES...ERROR
                                ;
.,F275 85 9A    STA $9A         CK30   STA DFLTO       ;ALL OUTPUT GOES HERE
                                ;
.,F277 18       CLC             CLC                    ;GOOD EXIT
.,F278 60       RTS             RTS
                                ;
.,F279 AA       TAX             CK40   TAX             ;SAVE DEVICE FOR DFLTO
.,F27A 20 0C ED JSR $ED0C       JSR    LISTN           ;TELL HIM TO LISTEN
                                ;
.,F27D A5 B9    LDA $B9         LDA    SA              ;IS THERE A SECOND?
.,F27F 10 05    BPL $F286       BPL    CK50            ;YES...
                                ;
.,F281 20 BE ED JSR $EDBE       JSR    SCATN           ;NO...RELEASE LINES
.,F284 D0 03    BNE $F289       BNE    CK60            ;BRANCH ALWAYS
                                ;
.,F286 20 B9 ED JSR $EDB9       CK50   JSR SECND       ;SEND SECOND...
                                ;
.,F289 8A       TXA             CK60   TXA
.,F28A 24 90    BIT $90         BIT    STATUS          ;DID HE LISTEN?
.,F28C 10 E7    BPL $F275       BPL    CK30            ;YES...FINISH UP
                                ;
.,F28E 4C 07 F7 JMP $F707       JMP    ERROR5          ;NO...DEVICE NOT PRESENT
                                .END
                                .LIB   CLOSE
                                ;***************************************
                                ;* CLOSE -- CLOSE LOGICAL FILE       *
                                ;*                                   *
                                ;*     THE LOGICAL FILE NUMBER OF THE*
                                ;* FILE TO BE CLOSED IS PASSED IN .A.*
                                ;* KEYBOARD, SCREEN, AND FILES NOT   *
                                ;* OPEN PASS STRAIGHT THROUGH. TAPE  *
                                ;* FILES OPEN FOR WRITE ARE CLOSED BY*
                                ;* DUMPING THE LAST BUFFER AND       *
                                ;* CONDITIONALLY WRITING AN END OF   *
                                ;* TAPE BLOCK.SERIAL FILES ARE CLOSED*
                                ;* BY SENDING A CLOSE FILE COMMAND IF*
                                ;* A SECONDARY ADDRESS WAS SPECIFIED *
                                ;* IN ITS OPEN COMMAND.              *
                                ;***************************************
                                ;
.,F291 20 14 F3 JSR $F314       NCLOSE JSR JLTLK       ;LOOK FILE UP
.,F294 F0 02    BEQ $F298       BEQ    JX050           ;OPEN...
.,F296 18       CLC             CLC                    ;ELSE RETURN
.,F297 60       RTS             RTS
                                ;
.,F298 20 1F F3 JSR $F31F       JX050  JSR JZ100       ;EXTRACT TABLE DATA
.,F29B 8A       TXA             TXA                    ;SAVE TABLE INDEX
.,F29C 48       PHA             PHA
                                ;
.,F29D A5 BA    LDA $BA         LDA    FA              ;CHECK DEVICE NUMBER
.,F29F F0 50    BEQ $F2F1       BEQ    JX150           ;IS KEYBOARD...DONE
.,F2A1 C9 03    CMP #$03        CMP    #3
.,F2A3 F0 4C    BEQ $F2F1       BEQ    JX150           ;IS SCREEN...DONE
.,F2A5 B0 47    BCS $F2EE       BCS    JX120           ;IS SERIAL...PROCESS
.,F2A7 C9 02    CMP #$02        CMP    #2              ;RS232?
.,F2A9 D0 1D    BNE $F2C8       BNE    JX115           ;NO...
                                ;
                                ; RS-232 CLOSE
                                ;
                                ; REMOVE FILE FROM TABLES
.,F2AB 68       PLA                    PLA
.,F2AC 20 F2 F2 JSR $F2F2              JSR JXRMV
                                ;
.,F2AF 20 83 F4 JSR $F483              JSR CLN232      ;CLEAN UP RS232 FOR CLOSE
                                ;
                                ; DEALLOCATE BUFFERS
                                ;
.,F2B2 20 27 FE JSR $FE27              JSR GETTOP      ;GET MEMSIZ
.,F2B5 A5 F8    LDA $F8                LDA RIBUF+1     ;CHECK INPUT ALLOCATION
.,F2B7 F0 01    BEQ $F2BA              BEQ CLS010      ;NOT...ALLOCATED
.,F2B9 C8       INY                    INY
.,F2BA A5 FA    LDA $FA         CLS010 LDA ROBUF+1     ;CHECK OUTPUT ALLOCATION
.,F2BC F0 01    BEQ $F2BF              BEQ CLS020
.,F2BE C8       INY                    INY
.,F2BF A9 00    LDA #$00        CLS020 LDA #00         ;DEALLOCATE
.,F2C1 85 F8    STA $F8                STA RIBUF+1
.,F2C3 85 FA    STA $FA                STA ROBUF+1
                                ; FLAG TOP OF MEMORY CHANGE
.,F2C5 4C 7D F4 JMP $F47D              JMP MEMTCF      ;GO SET NEW TOP
                                ;
                                ;CLOSE CASSETTE FILE
                                ;
.,F2C8 A5 B9    LDA $B9         JX115  LDA SA          ;WAS IT A TAPE READ?
.,F2CA 29 0F    AND #$0F        AND    #$F
.,F2CC F0 23    BEQ $F2F1       BEQ    JX150           ;YES
                                ;
.,F2CE 20 D0 F7 JSR $F7D0       JSR    ZZZ             ;NO. . .IT IS WRITE
.,F2D1 A9 00    LDA #$00        LDA    #0              ;END OF FILE CHARACTER
.,F2D3 38       SEC             SEC                    ;NEED TO SET CARRY FOR CASOUT (ELSE RS232 OUTPUT!)
.,F2D4 20 DD F1 JSR $F1DD       JSR    CASOUT          ;PUT IN END OF FILE
.,F2D7 20 64 F8 JSR $F864       JSR    WBLK
.,F2DA 90 04    BCC $F2E0       BCC    JX117           ;NO ERRORS...
.,F2DC 68       PLA             PLA                    ;CLEAN STACK FOR ERROR
.,F2DD A9 00    LDA #$00        LDA    #0              ;BREAK KEY ERROR
.,F2DF 60       RTS             RTS
                                ;
.,F2E0 A5 B9    LDA $B9         JX117  LDA SA
.,F2E2 C9 62    CMP #$62        CMP    #$62            ;WRITE END OF TAPE BLOCK?
.,F2E4 D0 0B    BNE $F2F1       BNE    JX150           ;NO...
                                ;
.,F2E6 A9 05    LDA #$05        LDA    #EOT
.,F2E8 20 6A F7 JSR $F76A       JSR    TAPEH           ;WRITE END OF TAPE BLOCK
.,F2EB 4C F1 F2 JMP $F2F1       JMP    JX150
                                ;
                                ;CLOSE AN SERIAL FILE
                                ;
.,F2EE 20 42 F6 JSR $F642       JX120  JSR CLSEI
                                ;
                                ;ENTRY TO REMOVE A GIVE LOGICAL FILE
                                ;FROM TABLE OF LOGICAL, PRIMARY,
                                ;AND SECONDARY ADDRESSES
                                ;
.,F2F1 68       PLA             JX150  PLA             ;GET TABLE INDEX OFF STACK
                                ;
                                ; JXRMV - ENTRY TO USE AS AN RS-232 SUBROUTINE
                                ;
.,F2F2 AA       TAX             JXRMV  TAX
.,F2F3 C6 98    DEC $98         DEC    LDTND
.,F2F5 E4 98    CPX $98         CPX    LDTND           ;IS DELETED FILE AT END?
.,F2F7 F0 14    BEQ $F30D       BEQ    JX170           ;YES...DONE
                                ;
                                ;DELETE ENTRY IN MIDDLE BY MOVING
                                ;LAST ENTRY TO THAT POSITION.
                                ;
.,F2F9 A4 98    LDY $98         LDY    LDTND
.,F2FB B9 59 02 LDA $0259,Y     LDA    LAT,Y
.,F2FE 9D 59 02 STA $0259,X     STA    LAT,X
.,F301 B9 63 02 LDA $0263,Y     LDA    FAT,Y
.,F304 9D 63 02 STA $0263,X     STA    FAT,X
.,F307 B9 6D 02 LDA $026D,Y     LDA    SAT,Y
.,F30A 9D 6D 02 STA $026D,X     STA    SAT,X
                                ;
.,F30D 18       CLC             JX170  CLC             ;CLOSE EXIT
.,F30E 60       RTS             JX175  RTS
                                ;LOOKUP TABLIZED LOGICAL FILE DATA
                                ;
.,F30F A9 00    LDA #$00        LOOKUP LDA #0
.,F311 85 90    STA $90         STA    STATUS
.,F313 8A       TXA             TXA
.,F314 A6 98    LDX $98         JLTLK  LDX LDTND
.,F316 CA       DEX             JX600  DEX
.,F317 30 15    BMI $F32E       BMI    JZ101
.,F319 DD 59 02 CMP $0259,X     CMP    LAT,X
.,F31C D0 F8    BNE $F316       BNE    JX600
.,F31E 60       RTS             RTS
                                ;ROUTINE TO FETCH TABLE ENTRIES
                                ;
.,F31F BD 59 02 LDA $0259,X     JZ100  LDA LAT,X
.,F322 85 B8    STA $B8         STA    LA
.,F324 BD 63 02 LDA $0263,X     LDA    FAT,X
.,F327 85 BA    STA $BA         STA    FA
.,F329 BD 6D 02 LDA $026D,X     LDA    SAT,X
.,F32C 85 B9    STA $B9         STA    SA
.,F32E 60       RTS             JZ101  RTS
                                .END
                                .LIB   CLALL
                                ;***************************************
                                ;* CLALL -- CLOSE ALL LOGICAL FILES  *
                                ;*      DELETES ALL TABLE ENTRIES AND*
                                ;* RESTORES DEFAULT I/O CHANNELS     *
                                ;* AND CLEARS IEEE PORT DEVICES      *
                                ;*************************************
                                ;
.,F32F A9 00    LDA #$00        NCLALL LDA #0
.,F331 85 98    STA $98         STA    LDTND           ;FORGET ALL FILES
                                ;********************************************
                                ;* CLRCH -- CLEAR CHANNELS                  *
                                ;*   UNLISTEN OR UNTALK IEEE DEVICES, BUT   *
                                ;* LEAVE OTHERS ALONE.  DEFAULT CHANNELS    *
                                ;* ARE RESTORED.                            *
                                ;********************************************
                                ;
.,F333 A2 03    LDX #$03        NCLRCH LDX #3
.,F335 E4 9A    CPX $9A         CPX    DFLTO           ;IS OUTPUT CHANNEL IEEE?
.,F337 B0 03    BCS $F33C       BCS    JX750           ;NO...
                                ;
.,F339 20 FE ED JSR $EDFE       JSR    UNLSN           ;YES...UNLISTEN IT
                                ;
.,F33C E4 99    CPX $99         JX750  CPX DFLTN       ;IS INPUT CHANNEL IEEE?
.,F33E B0 03    BCS $F343       BCS    CLALL2          ;NO...
                                ;
.,F340 20 EF ED JSR $EDEF       JSR    UNTLK           ;YES...UNTALK IT
                                ;
                                ;RESTORE DEFAULT VALUES
                                ;
                                ;
.,F343 86 9A    STX $9A         CLALL2 STX DFLTO       ;OUTPUT CHAN=3=SCREEN
.,F345 A9 00    LDA #$00        LDA    #0
.,F347 85 99    STA $99         STA    DFLTN           ;INPUT CHAN=0=KEYBOARD
.,F349 60       RTS             RTS
                                .END
                                .LIB   OPEN
                                ;***********************************
                                ;*                                 *
                                ;* OPEN FUNCTION                   *
                                ;*                                 *
                                ;* CREATES AN ENTRY IN THE LOGICAL *
                                ;* FILES TABLES CONSISTING OF      *
                                ;* LOGICAL FILE NUMBER--LA, DEVICE *
                                ;* NUMBER--FA, AND SECONDARY CMD-- *
                                ;* SA.                             *
                                ;*                                 *
                                ;* A FILE NAME DESCRIPTOR, FNADR & *
                                ;* FNLEN ARE PASSED TO THIS ROUTINE*
                                ;*                                 *
                                ;***********************************
                                ;
.,F34A A6 B8    LDX $B8         NOPEN  LDX LA          ;CHECK FILE #
.,F34C D0 03    BNE $F351       BNE    OP98            ;IS NOT THE KEYBOARD
                                ;
.,F34E 4C 0A F7 JMP $F70A       JMP    ERROR6          ;NOT INPUT FILE...
                                ;
.,F351 20 0F F3 JSR $F30F       OP98   JSR LOOKUP      ;SEE IF IN TABLE
.,F354 D0 03    BNE $F359       BNE    OP100           ;NOT FOUND...O.K.
                                ;
.,F356 4C FE F6 JMP $F6FE       JMP    ERROR2          ;FILE OPEN
                                ;
.,F359 A6 98    LDX $98         OP100  LDX LDTND       ;LOGICAL DEVICE TABLE END
.,F35B E0 0A    CPX #$0A        CPX    #10             ;MAXIMUM # OF OPEN FILES
.,F35D 90 03    BCC $F362       BCC    OP110           ;LESS THAN 10...O.K.
                                ;
.,F35F 4C FB F6 JMP $F6FB       JMP    ERROR1          ;TOO MANY FILES
                                ;
.,F362 E6 98    INC $98         OP110  INC LDTND       ;NEW FILE
.,F364 A5 B8    LDA $B8         LDA    LA
.,F366 9D 59 02 STA $0259,X     STA    LAT,X           ;STORE LOGICAL FILE #
.,F369 A5 B9    LDA $B9         LDA    SA
.,F36B 09 60    ORA #$60        ORA    #$60            ;MAKE SA AN SERIAL COMMAND
.,F36D 85 B9    STA $B9         STA    SA
.,F36F 9D 6D 02 STA $026D,X     STA    SAT,X           ;STORE COMMAND #
.,F372 A5 BA    LDA $BA         LDA    FA
.,F374 9D 63 02 STA $0263,X     STA    FAT,X           ;STORE DEVICE #
                                ;
                                ;PERFORM DEVICE SPECIFIC OPEN TASKS
                                ;
.,F377 F0 5A    BEQ $F3D3       BEQ    OP175           ;IS KEYBOARD...DONE.
.,F379 C9 03    CMP #$03        CMP    #3
.,F37B F0 56    BEQ $F3D3       BEQ    OP175           ;IS SCREEN...DONE.
.,F37D 90 05    BCC $F384       BCC    OP150           ;ARE CASSETTES 1 & 2
                                ;
.,F37F 20 D5 F3 JSR $F3D5       JSR    OPENI           ;IS ON SERIAL...OPEN IT
.,F382 90 4F    BCC $F3D3       BCC    OP175           ;BRANCH ALWAYS...DONE
                                ;
                                ;PERFORM TAPE OPEN STUFF
                                ;
.,F384 C9 02    CMP #$02        OP150  CMP #2
.,F386 D0 03    BNE $F38B       BNE    OP152
                                ;
.,F388 4C 09 F4 JMP $F409       JMP    OPN232
                                ;
.,F38B 20 D0 F7 JSR $F7D0       OP152  JSR ZZZ         ;SEE IF TAPE BUFFER
.,F38E B0 03    BCS $F393       BCS    OP155           ;YES
                                ;
.,F390 4C 13 F7 JMP $F713       JMP    ERROR9          ;NO...DEALLOCATED
                                ;
.,F393 A5 B9    LDA $B9         OP155  LDA SA
.,F395 29 0F    AND #$0F        AND    #$F             ;MASK OFF COMMAND
.,F397 D0 1F    BNE $F3B8       BNE    OP200           ;NON ZERO IS TAPE WRITE
                                ;
                                ;OPEN CASSETE TAPE FILE TO READ
                                ;
.,F399 20 17 F8 JSR $F817       JSR    CSTE1           ;TELL "PRESS PLAY"
.,F39C B0 36    BCS $F3D4       BCS    OP180           ;STOP KEY PRESSED
                                ;
.,F39E 20 AF F5 JSR $F5AF       JSR    LUKING          ;TELL USER "SEARCHING"
                                ;
.,F3A1 A5 B7    LDA $B7         LDA    FNLEN
.,F3A3 F0 0A    BEQ $F3AF       BEQ    OP170           ;LOOKING FOR ANY FILE
                                ;
.,F3A5 20 EA F7 JSR $F7EA       JSR    FAF             ;LOOKING FOR NAMED FILE
.,F3A8 90 18    BCC $F3C2       BCC    OP171           ;FOUND IT!!!
.,F3AA F0 28    BEQ $F3D4       BEQ    OP180           ;STOP KEY PRESSED
                                ;
.,F3AC 4C 04 F7 JMP $F704       OP160  JMP ERROR4      ;FILE NOT FOUND
                                ;
.,F3AF 20 2C F7 JSR $F72C       OP170  JSR FAH         ;GET ANY OLD HEADER
.,F3B2 F0 20    BEQ $F3D4       BEQ    OP180           ;STOP KEY PRESSED
.,F3B4 90 0C    BCC $F3C2       BCC    OP171           ;ALL O.K.
.,F3B6 B0 F4    BCS $F3AC       BCS    OP160           ;FILE NOT FOUND...
                                ;
                                ;OPEN CASSETTE TAPE FOR WRITE
                                ;
.,F3B8 20 38 F8 JSR $F838       OP200  JSR CSTE2       ;TELL "PRESS PLAY AND RECORD"
.,F3BB B0 17    BCS $F3D4       BCS    OP180           ;STOP KEY PRESSED
.,F3BD A9 04    LDA #$04        LDA    #BDFH           ;DATA FILE HEADER TYPE
.,F3BF 20 6A F7 JSR $F76A       JSR    TAPEH           ;WRITE IT
                                ;
                                ;FINISH OPEN FOR TAPE READ/WRITE
                                ;
.,F3C2 A9 BF    LDA #$BF        OP171  LDA #BUFSZ-1    ;ASSUME FORCE READ
                                ;
.,F3C4 A4 B9    LDY $B9         LDY    SA
.,F3C6 C0 60    CPY #$60        CPY    #$60            ;OPEN FOR READ?
.,F3C8 F0 07    BEQ $F3D1       BEQ    OP172
                                ;
                                ;SET POINTERS FOR BUFFERING DATA
                                ;
.,F3CA A0 00    LDY #$00        LDY    #0
.,F3CC A9 02    LDA #$02        LDA    #BDF            ;TYPE FLAG FOR BLOCK
.,F3CE 91 B2    STA ($B2),Y     STA    (TAPE1)Y        ;TO BEGIN OF BUFFER
.,F3D0 98       TYA             TYA
                                ;
.,F3D1 85 A6    STA $A6         OP172  STA BUFPT       ;POINT TO DATA
.,F3D3 18       CLC             OP175  CLC             ;FLAG GOOD OPEN
.,F3D4 60       RTS             OP180  RTS             ;EXIT IN PEACE
.,F3D5 A5 B9    LDA $B9         OPENI  LDA SA
.,F3D7 30 FA    BMI $F3D3       BMI    OP175           ;NO SA...DONE
                                ;
.,F3D9 A4 B7    LDY $B7         LDY    FNLEN
.,F3DB F0 F6    BEQ $F3D3       BEQ    OP175           ;NO FILE NAME...DONE
                                ;
.,F3DD A9 00    LDA #$00        LDA    #0              ;CLEAR THE SERIAL STATUS
.,F3DF 85 90    STA $90         STA    STATUS
                                ;
.,F3E1 A5 BA    LDA $BA         LDA    FA
.,F3E3 20 0C ED JSR $ED0C       JSR    LISTN           ;DEVICE LA TO LISTEN
                                ;
.,F3E6 A5 B9    LDA $B9         LDA    SA
.,F3E8 09 F0    ORA #$F0        ORA    #$F0
.,F3EA 20 B9 ED JSR $EDB9       JSR    SECND
                                ;
.,F3ED A5 90    LDA $90         LDA    STATUS          ;ANYBODY HOME?
.,F3EF 10 05    BPL $F3F6       BPL    OP35            ;YES...CONTINUE
                                ;
                                ;THIS ROUTINE IS CALLED BY OTHER
                                ;KERNAL ROUTINES WHICH ARE CALLED
                                ;DIRECTLY BY OS.  KILL RETURN
                                ;ADDRESS TO RETURN TO OS.
                                ;
.,F3F1 68       PLA             PLA
.,F3F2 68       PLA             PLA
.,F3F3 4C 07 F7 JMP $F707       JMP    ERROR5          ;DEVICE NOT PRESENT
                                ;
.,F3F6 A5 B7    LDA $B7         OP35   LDA FNLEN
.,F3F8 F0 0C    BEQ $F406       BEQ    OP45            ;NO NAME...DONE SEQUENCE
                                ;
                                ;SEND FILE NAME OVER SERIAL
                                ;
.,F3FA A0 00    LDY #$00        LDY    #0
.,F3FC B1 BB    LDA ($BB),Y     OP40   LDA (FNADR)Y
.,F3FE 20 DD ED JSR $EDDD       JSR    CIOUT
.,F401 C8       INY             INY
.,F402 C4 B7    CPY $B7         CPY    FNLEN
.,F404 D0 F6    BNE $F3FC       BNE    OP40
                                ;
.,F406 4C 54 F6 JMP $F654       OP45   JMP CUNLSN      ;JSR UNLSN: CLC: RTS
                                ; OPN232 - OPEN AN RS-232 OR PARALLEL PORT FILE
                                ;
                                ; VARIABLES INITILIZED
                                ;   BITNUM - # OF BITS TO BE SENT CALC FROM M51CTR
                                ;   BAUDOF - BAUD RATE FULL
                                ;   RSSTAT - RS-232 STATUS REG
                                ;   M51CTR - 6551 CONTROL REG
                                ;   M51CDR - 6551 COMMAND REG
                                ;   M51AJB - USER BAUD RATE (CLOCK/BAUD/2-100)
                                ;   ENABL  - 6526 NMI ENABLES (1-NMI BIT ON)
                                ;
.,F409 20 83 F4 JSR $F483       OPN232 JSR CLN232      ;SET UP RS232, .Y=0 ON RETURN
                                ;
                                ; PASS PRAMS TO M51REGS
                                ;
.,F40C 8C 97 02 STY $0297              STY RSSTAT      ;CLEAR STATUS
                                ;
.,F40F C4 B7    CPY $B7         OPN020 CPY FNLEN       ;CHECK IF AT END OF FILENAME
.,F411 F0 0A    BEQ $F41D              BEQ OPN025      ;YES...
                                ;
.,F413 B1 BB    LDA ($BB),Y            LDA (FNADR)Y    ;MOVE DATA
.,F415 99 93 02 STA $0293,Y            STA M51CTR,Y    ;TO M51REGS
.,F418 C8       INY                    INY
.,F419 C0 04    CPY #$04               CPY #4          ;ONLY 4 POSSIBLE PRAMS
.,F41B D0 F2    BNE $F40F              BNE OPN020
                                ;
                                ; CALC # OF BITS
                                ;
.,F41D 20 4A EF JSR $EF4A       OPN025 JSR BITCNT
.,F420 8E 98 02 STX $0298              STX BITNUM
                                ;
                                ; CALC BAUD RATE
                                ;
.,F423 AD 93 02 LDA $0293              LDA M51CTR
.,F426 29 0F    AND #$0F               AND #$0F
.,F428 F0 1C    BEQ $F446              BNE OPN010
                                ;
                                ; CALCULATE START-TEST RATE...
                                ;  DIFFERENT THAN ORIGINAL RELEASE 901227-01
                                ;
.,F42A 0A       ASL                    ASL A           ;GET OFFSET INTO TABLES
.,F42B AA       TAX                    TAX
.,F42C AD A6 02 LDA $02A6              LDA PALNTS      ;GET TV STANDARD
.,F42F D0 09    BNE $F43A              BNE OPN026
.,F431 BC C1 FE LDY $FEC1,X            LDY BAUDO-1,X   ;NTSC STANDARD
.,F434 BD C0 FE LDA $FEC0,X            LDA BAUDO-2,X
.,F437 4C 40 F4 JMP $F440              JMP OPN027
                                ;
.,F43A BC EB E4 LDY $E4EB,X     OPN026 LDY BAUDOP-1,X  ;PAL STANDARD
.,F43D BD EA E4 LDA $E4EA,X            LDA BAUDOP-2,X
.,F440 8C 96 02 STY $0296       OPN027 STY M51AJB+1    ;HOLD START RATE IN M51AJB
.,F443 8D 95 02 STA $0295              STA M51AJB
.,F446 AD 95 02 LDA $0295       OPN028 LDA M51AJB      ;CALCULATE BAUD RATE
.,F449 0A       ASL                    ASL
.,F44A 20 2E FF JSR $FF2E              JSR POPEN       ;GOTO PATCH AREA
                                ;
                                ; CHECK FOR 3/X LINE RESPONSE
                                ;
.,F44D AD 94 02 LDA $0294       OPN030 LDA M51CDR      ;BIT 0 OF M51CDR
.,F450 4A       LSR                    LSR A
.,F451 90 09    BCC $F45C              BCC OPN050      ;...3 LINE
                                ;
                                ; CHECK FOR X LINE PROPER STATES
                                ;
.,F453 AD 01 DD LDA $DD01              LDA D2PRB
.,F456 0A       ASL                    ASL A
.,F457 B0 03    BCS $F45C              BCS OPN050
.,F459 20 0D F0 JSR $F00D              JMP CKDSRX      ;NO DATA SET...DSR ERROR EXIT
                                ;
                                ; SET UP BUFFER POINTERS (DBE=DBS)
                                ;
.,F45C AD 9B 02 LDA $029B       OPN050 LDA RIDBE
.,F45F 8D 9C 02 STA $029C              STA RIDBS
.,F462 AD 9E 02 LDA $029E              LDA RODBE
.,F465 8D 9D 02 STA $029D              STA RODBS
                                ;
                                ; ALLOCATE BUFFERS
                                ;
.,F468 20 27 FE JSR $FE27       OPN055 JSR GETTOP      ;GET MEMSIZ
.,F46B A5 F8    LDA $F8                LDA RIBUF+1     ;IN ALLOCATION...
.,F46D D0 05    BNE $F474              BNE OPN060      ;ALREADY
.,F46F 88       DEY                    DEY             ;THERE GOES 256 BYTES
.,F470 84 F8    STY $F8                STY RIBUF+1
.,F472 86 F7    STX $F7                STX RIBUF
.,F474 A5 FA    LDA $FA         OPN060 LDA ROBUF+1     ;OUT ALLOCATION...
.,F476 D0 05    BNE $F47D              BNE MEMTCF      ;ALREAY
.,F478 88       DEY                    DEY             ;THERE GOES 256 BYTES
.,F479 84 FA    STY $FA                STY ROBUF+1
.,F47B 86 F9    STX $F9                STX ROBUF
.,F47D 38       SEC             MEMTCF SEC             ;SIGNAL TOP OF MEMORY CHANGE
.,F47E A9 F0    LDA #$F0               LDA #$F0
.,F480 4C 2D FE JMP $FE2D              JMP SETTOP      ;TOP CHANGED
                                ;
                                ; CLN232 - CLEAN UP 232 SYSTEM FOR OPEN/CLOSE
                                ;  SET UP DDRB AND CB2 FOR RS-232
                                ;
.,F483 A9 7F    LDA #$7F        CLN232 LDA #$7F        ;CLEAR NMI'S
.,F485 8D 0D DD STA $DD0D              STA D2ICR
.,F488 A9 06    LDA #$06               LDA #%00000110  ;DDRB
.,F48A 8D 03 DD STA $DD03              STA D2DDRB
.,F48D 8D 01 DD STA $DD01              STA D2PRB       ;DTR,RTS HIGH
.,F490 A9 04    LDA #$04               LDA #$04        ;OUTPUT HIGH PA2
.,F492 0D 00 DD ORA $DD00              ORA D2PRA
.,F495 8D 00 DD STA $DD00              STA D2PRA
.,F498 A0 00    LDY #$00               LDY #00
.,F49A 8C A1 02 STY $02A1              STY ENABL       ;CLEAR ENABLS
.,F49D 60       RTS                    RTS
                                .END
                                .LIB   LOAD
                                ;**********************************
                                ;* LOAD RAM FUNCTION              *
                                ;*                                *
                                ;* LOADS FROM CASSETTE 1 OR 2, OR *
                                ;* SERIAL BUS DEVICES >=4 TO 31   *
                                ;* AS DETERMINED BY CONTENTS OF   *
                                ;* VARIABLE FA. VERIFY FLAG IN .A *
                                ;*                                *
                                ;* ALT LOAD IF SA=0, NORMAL SA=1  *
                                ;* .X , .Y LOAD ADDRESS IF SA=0   *
                                ;* .A=0 PERFORMS LOAD,<> IS VERIFY*
                                ;*                                *
                                ;* HIGH LOAD RETURN IN X,Y.       *
                                ;*                                *
                                ;**********************************
.,F49E 86 C3    STX $C3         LOADSP STX MEMUSS      ;.X HAS LOW ALT START
.,F4A0 84 C4    STY $C4         STY    MEMUSS+1
.,F4A2 6C 30 03 JMP ($0330)     LOAD   JMP (ILOAD)     ;MONITOR LOAD ENTRY
                                ;
.,F4A5 85 93    STA $93         NLOAD  STA VERCK       ;STORE VERIFY FLAG
.,F4A7 A9 00    LDA #$00        LDA    #0
.,F4A9 85 90    STA $90         STA    STATUS
                                ;
.,F4AB A5 BA    LDA $BA         LDA    FA              ;CHECK DEVICE NUMBER
.,F4AD D0 03    BNE $F4B2       BNE    LD20
                                ;
.,F4AF 4C 13 F7 JMP $F713       LD10   JMP ERROR9      ;BAD DEVICE #-KEYBOARD
                                ;
.,F4B2 C9 03    CMP #$03        LD20   CMP #3
.,F4B4 F0 F9    BEQ $F4AF       BEQ    LD10            ;DISALLOW SCREEN LOAD
.,F4B6 90 7B    BCC $F533       BCC    LD100           ;HANDLE TAPES DIFFERENT
                                ;
                                ;LOAD FROM CBM IEEE DEVICE
                                ;
.,F4B8 A4 B7    LDY $B7         LDY    FNLEN           ;MUST HAVE FILE NAME
.,F4BA D0 03    BNE $F4BF       BNE    LD25            ;YES...OK
                                ;
.,F4BC 4C 10 F7 JMP $F710       JMP    ERROR8          ;MISSING FILE NAME
                                ;
.,F4BF A6 B9    LDX $B9         LD25   LDX SA          ;SAVE SA IN .X
.,F4C1 20 AF F5 JSR $F5AF       JSR    LUKING          ;TELL USER LOOKING
.,F4C4 A9 60    LDA #$60        LDA    #$60            ;SPECIAL LOAD COMMAND
.,F4C6 85 B9    STA $B9         STA    SA
.,F4C8 20 D5 F3 JSR $F3D5       JSR    OPENI           ;OPEN THE FILE
                                ;
.,F4CB A5 BA    LDA $BA         LDA    FA
.,F4CD 20 09 ED JSR $ED09       JSR    TALK            ;ESTABLISH THE CHANNEL
.,F4D0 A5 B9    LDA $B9         LDA    SA
.,F4D2 20 C7 ED JSR $EDC7       JSR    TKSA            ;TELL IT TO LOAD
                                ;
.,F4D5 20 13 EE JSR $EE13       JSR    ACPTR           ;GET FIRST BYTE
.,F4D8 85 AE    STA $AE         STA    EAL
                                ;
.,F4DA A5 90    LDA $90         LDA    STATUS          ;TEST STATUS FOR ERROR
.,F4DC 4A       LSR             LSR    A
.,F4DD 4A       LSR             LSR    A
.,F4DE B0 50    BCS $F530       BCS    LD90            ;FILE NOT FOUND...
.,F4E0 20 13 EE JSR $EE13       JSR    ACPTR
.,F4E3 85 AF    STA $AF         STA    EAH
                                ;
.,F4E5 8A       TXA             TXA                    ;FIND OUT OLD SA
.,F4E6 D0 08    BNE $F4F0       BNE    LD30            ;SA<>0 USE DISK ADDRESS
.,F4E8 A5 C3    LDA $C3         LDA    MEMUSS          ;ELSE LOAD WHERE USER WANTS
.,F4EA 85 AE    STA $AE         STA    EAL
.,F4EC A5 C4    LDA $C4         LDA    MEMUSS+1
.,F4EE 85 AF    STA $AF         STA    EAH
.,F4F0 20 D2 F5 JSR $F5D2       LD30   JSR LODING      ;TELL USER LOADING
                                ;
.,F4F3 A9 FD    LDA #$FD        LD40   LDA #$FD        ;MASK OFF TIMEOUT
.,F4F5 25 90    AND $90         AND    STATUS
.,F4F7 85 90    STA $90         STA    STATUS
                                ;
.,F4F9 20 E1 FF JSR $FFE1       JSR    STOP            ;STOP KEY?
.,F4FC D0 03    BNE $F501       BNE    LD45            ;NO...
                                ;
.,F4FE 4C 33 F6 JMP $F633       JMP    BREAK           ;STOP KEY PRESSED
                                ;
.,F501 20 13 EE JSR $EE13       LD45   JSR ACPTR       ;GET BYTE OFF IEEE
.,F504 AA       TAX             TAX
.,F505 A5 90    LDA $90         LDA    STATUS          ;WAS THERE A TIMEOUT?
.,F507 4A       LSR             LSR    A
.,F508 4A       LSR             LSR    A
.,F509 B0 E8    BCS $F4F3       BCS    LD40            ;YES...TRY AGAIN
.,F50B 8A       TXA             TXA
.,F50C A4 93    LDY $93         LDY    VERCK           ;PERFORMING VERIFY?
.,F50E F0 0C    BEQ $F51C       BEQ    LD50            ;NO...LOAD
.,F510 A0 00    LDY #$00        LDY    #0
.,F512 D1 AE    CMP ($AE),Y     CMP    (EAL)Y          ;VERIFY IT
.,F514 F0 08    BEQ $F51E       BEQ    LD60            ;O.K....
.,F516 A9 10    LDA #$10        LDA    #SPERR          ;NO GOOD...VERIFY ERROR
.,F518 20 1C FE JSR $FE1C       JSR    UDST            ;UPDATE STATUS
.:F51B 2C       .BYTE $2C       .BYT   $2C             ;SKIP NEXT STORE
                                ;
.,F51C 91 AE    STA ($AE),Y     LD50   STA (EAL)Y
.,F51E E6 AE    INC $AE         LD60   INC EAL         ;INCREMENT STORE ADDR
.,F520 D0 02    BNE $F524       BNE    LD64
.,F522 E6 AF    INC $AF         INC    EAH
.,F524 24 90    BIT $90         LD64   BIT STATUS      ;EOI?
.,F526 50 CB    BVC $F4F3       BVC    LD40            ;NO...CONTINUE LOAD
                                ;
.,F528 20 EF ED JSR $EDEF       JSR    UNTLK           ;CLOSE CHANNEL
.,F52B 20 42 F6 JSR $F642       JSR    CLSEI           ;CLOSE THE FILE
.,F52E 90 79    BCC $F5A9       BCC    LD180           ;BRANCH ALWAYS
                                ;
.,F530 4C 04 F7 JMP $F704       LD90   JMP ERROR4      ;FILE NOT FOUND
                                ;
                                ;LOAD FROM TAPE
                                ;
.,F533 4A       LSR             LD100  LSR A
.,F534 B0 03    BCS $F539       BCS    LD102           ;IF C-SET THEN IT'S CASSETTE
                                ;
.,F536 4C 13 F7 JMP $F713       JMP    ERROR9          ;BAD DEVICE #
                                ;
.,F539 20 D0 F7 JSR $F7D0       LD102  JSR ZZZ         ;SET POINTERS AT TAPE
.,F53C B0 03    BCS $F541       BCS    LD104
.,F53E 4C 13 F7 JMP $F713       JMP    ERROR9          ;DEALLOCATED...
.,F541 20 17 F8 JSR $F817       LD104  JSR CSTE1       ;TELL USER ABOUT BUTTONS
.,F544 B0 68    BCS $F5AE       BCS    LD190           ;STOP KEY PRESSED?
.,F546 20 AF F5 JSR $F5AF       JSR    LUKING          ;TELL USER SEARCHING
                                ;
.,F549 A5 B7    LDA $B7         LD112  LDA FNLEN       ;IS THERE A NAME?
.,F54B F0 09    BEQ $F556       BEQ    LD150           ;NONE...LOAD ANYTHING
.,F54D 20 EA F7 JSR $F7EA       JSR    FAF             ;FIND A FILE ON TAPE
.,F550 90 0B    BCC $F55D       BCC    LD170           ;GOT IT!
.,F552 F0 5A    BEQ $F5AE       BEQ    LD190           ;STOP KEY PRESSED
.,F554 B0 DA    BCS $F530       BCS    LD90            ;NOPE...END OF TAPE
                                ;
.,F556 20 2C F7 JSR $F72C       LD150  JSR FAH         ;FIND ANY HEADER
.,F559 F0 53    BEQ $F5AE       BEQ    LD190           ;STOP KEY PRESSED
.,F55B B0 D3    BCS $F530       BCS    LD90            ;NO HEADER
                                ;
.,F55D A5 90    LDA $90         LD170  LDA STATUS
.,F55F 29 10    AND #$10        AND    #SPERR          ;MUST GOT HEADER RIGHT
.,F561 38       SEC             SEC
.,F562 D0 4A    BNE $F5AE       BNE    LD190           ;IS BAD
                                ;
.,F564 E0 01    CPX #$01        CPX    #BLF            ;IS IT A MOVABLE PROGRAM...
.,F566 F0 11    BEQ $F579       BEQ    LD178           ;YES
                                ;
.,F568 E0 03    CPX #$03        CPX    #PLF            ;IS IT A PROGRAM
.,F56A D0 DD    BNE $F549       BNE    LD112           ;NO...ITS SOMETHING ELSE
                                ;
.,F56C A0 01    LDY #$01        LD177  LDY #1          ;FIXED LOAD...
.,F56E B1 B2    LDA ($B2),Y     LDA    (TAPE1)Y        ;...THE ADDRESS IN THE...
.,F570 85 C3    STA $C3         STA    MEMUSS          ;...BUFFER IS THE START ADDRESS
.,F572 C8       INY             INY
.,F573 B1 B2    LDA ($B2),Y     LDA    (TAPE1)Y
.,F575 85 C4    STA $C4         STA    MEMUSS+1
.,F577 B0 04    BCS $F57D       BCS    LD179           ;JMP ..CARRY SET BY CPX'S
                                ;
.,F579 A5 B9    LDA $B9         LD178  LDA SA          ;CHECK FOR MONITOR LOAD...
.,F57B D0 EF    BNE $F56C       BNE    LD177           ;...YES WE WANT FIXED TYPE
                                ;
.,F57D A0 03    LDY #$03        LD179  LDY #3          ;TAPEA - TAPESTA
                                ;CARRY SET BY CPX'S
.,F57F B1 B2    LDA ($B2),Y     LDA    (TAPE1)Y
.,F581 A0 01    LDY #$01        LDY    #1
.,F583 F1 B2    SBC ($B2),Y     SBC    (TAPE1)Y
.,F585 AA       TAX             TAX                    ;LOW TO .X
.,F586 A0 04    LDY #$04        LDY    #4
.,F588 B1 B2    LDA ($B2),Y     LDA    (TAPE1)Y
.,F58A A0 02    LDY #$02        LDY    #2
.,F58C F1 B2    SBC ($B2),Y     SBC    (TAPE1)Y
.,F58E A8       TAY             TAY                    ;HIGH TO .Y
                                ;
.,F58F 18       CLC             CLC                    ;EA = STA+(TAPEA-TAPESTA)
.,F590 8A       TXA             TXA
.,F591 65 C3    ADC $C3         ADC    MEMUSS          ;
.,F593 85 AE    STA $AE         STA    EAL
.,F595 98       TYA             TYA
.,F596 65 C4    ADC $C4         ADC    MEMUSS+1
.,F598 85 AF    STA $AF         STA    EAH
.,F59A A5 C3    LDA $C3         LDA    MEMUSS          ;SET UP STARTING ADDRESS
.,F59C 85 C1    STA $C1         STA    STAL
.,F59E A5 C4    LDA $C4         LDA    MEMUSS+1
.,F5A0 85 C2    STA $C2         STA    STAH
.,F5A2 20 D2 F5 JSR $F5D2       JSR    LODING          ;TELL USER LOADING
.,F5A5 20 4A F8 JSR $F84A       JSR    TRD             ;DO TAPE BLOCK LOAD
.:F5A8 24       .BYTE $24       .BYT   $24             ;CARRY FROM TRD
                                ;
.,F5A9 18       CLC             LD180  CLC             ;GOOD EXIT
                                ;
                                ; SET UP END LOAD ADDRESS
                                ;
.,F5AA A6 AE    LDX $AE         LDX    EAL
.,F5AC A4 AF    LDY $AF         LDY    EAH
                                ;
.,F5AE 60       RTS             LD190  RTS
                                ;SUBROUTINE TO PRINT TO CONSOLE:
                                ;
                                ;SEARCHING [FOR NAME]
                                ;
.,F5AF A5 9D    LDA $9D         LUKING LDA MSGFLG      ;SUPPOSED TO PRINT?
.,F5B1 10 1E    BPL $F5D1       BPL    LD115           ;...NO
.,F5B3 A0 0C    LDY #$0C        LDY    #MS5-MS1        ;"SEARCHING"
.,F5B5 20 2F F1 JSR $F12F       JSR    MSG
.,F5B8 A5 B7    LDA $B7         LDA    FNLEN
.,F5BA F0 15    BEQ $F5D1       BEQ    LD115
.,F5BC A0 17    LDY #$17        LDY    #MS6-MS1        ;"FOR"
.,F5BE 20 2F F1 JSR $F12F       JSR    MSG
                                ;SUBROUTINE TO OUTPUT FILE NAME
                                ;
.,F5C1 A4 B7    LDY $B7         OUTFN  LDY FNLEN       ;IS THERE A NAME?
.,F5C3 F0 0C    BEQ $F5D1       BEQ    LD115           ;NO...DONE
.,F5C5 A0 00    LDY #$00        LDY    #0
.,F5C7 B1 BB    LDA ($BB),Y     LD110  LDA (FNADR)Y
.,F5C9 20 D2 FF JSR $FFD2       JSR    BSOUT
.,F5CC C8       INY             INY
.,F5CD C4 B7    CPY $B7         CPY    FNLEN
.,F5CF D0 F6    BNE $F5C7       BNE    LD110
                                ;
.,F5D1 60       RTS             LD115  RTS
                                ;SUBROUTINE TO PRINT:
                                ;
                                ;LOADING/VERIFING
                                ;
.,F5D2 A0 49    LDY #$49        LODING LDY #MS10-MS1   ;ASSUME 'LOADING'
.,F5D4 A5 93    LDA $93         LDA    VERCK           ;CHECK FLAG
.,F5D6 F0 02    BEQ $F5DA       BEQ    LD410           ;ARE DOING LOAD
.,F5D8 A0 59    LDY #$59        LDY    #MS21-MS1       ;ARE 'VERIFYING'
.,F5DA 4C 2B F1 JMP $F12B       LD410  JMP SPMSG
                                .END
                                .LIB   SAVE
                                ;***********************************
                                ;* SAVE                            *
                                ;*                                 *
                                ;* SAVES TO CASSETTE 1 OR 2, OR    *
                                ;* IEEE DEVICES 4>=N>=31 AS SELECT-*
                                ;* ED BY VARIABLE FA.              *
                                ;*                                 *
                                ;*START OF SAVE IS INDIRECT AT .A  *
                                ;*END OF SAVE IS .X,.Y             *
                                ;***********************************
.,F5DD 86 AE    STX $AE         SAVESP STX EAL
.,F5DF 84 AF    STY $AF         STY    EAH
.,F5E1 AA       TAX             TAX                    ;SET UP START
.,F5E2 B5 00    LDA $00,X       LDA    $00,X
.,F5E4 85 C1    STA $C1         STA    STAL
.,F5E6 B5 01    LDA $01,X       LDA    $01,X
.,F5E8 85 C2    STA $C2         STA    STAH
                                ;
.,F5EA 6C 32 03 JMP ($0332)     SAVE   JMP (ISAVE)
.,F5ED A5 BA    LDA $BA         NSAVE  LDA FA  ***MONITOR ENTRY
.,F5EF D0 03    BNE $F5F4       BNE    SV20
                                ;
.,F5F1 4C 13 F7 JMP $F713       SV10   JMP ERROR9      ;BAD DEVICE #
                                ;
.,F5F4 C9 03    CMP #$03        SV20   CMP #3
.,F5F6 F0 F9    BEQ $F5F1       BEQ    SV10
.,F5F8 90 5F    BCC $F659       BCC    SV100
.,F5FA A9 61    LDA #$61        LDA    #$61
.,F5FC 85 B9    STA $B9         STA    SA
.,F5FE A4 B7    LDY $B7         LDY    FNLEN
.,F600 D0 03    BNE $F605       BNE    SV25
                                ;
.,F602 4C 10 F7 JMP $F710       JMP    ERROR8          ;MISSING FILE NAME
                                ;
.,F605 20 D5 F3 JSR $F3D5       SV25   JSR OPENI
.,F608 20 8F F6 JSR $F68F       JSR    SAVING
.,F60B A5 BA    LDA $BA         LDA    FA
.,F60D 20 0C ED JSR $ED0C       JSR    LISTN
.,F610 A5 B9    LDA $B9         LDA    SA
.,F612 20 B9 ED JSR $EDB9       JSR    SECND
.,F615 A0 00    LDY #$00        LDY    #0
.,F617 20 8E FB JSR $FB8E       JSR    RD300
.,F61A A5 AC    LDA $AC         LDA    SAL
.,F61C 20 DD ED JSR $EDDD       JSR    CIOUT
.,F61F A5 AD    LDA $AD         LDA    SAH
.,F621 20 DD ED JSR $EDDD       JSR    CIOUT
.,F624 20 D1 FC JSR $FCD1       SV30   JSR CMPSTE      ;COMPARE START TO END
.,F627 B0 16    BCS $F63F       BCS    SV50            ;HAVE REACHED END
.,F629 B1 AC    LDA ($AC),Y     LDA    (SAL)Y
.,F62B 20 DD ED JSR $EDDD       JSR    CIOUT
.,F62E 20 E1 FF JSR $FFE1       JSR    STOP
.,F631 D0 07    BNE $F63A       BNE    SV40
                                ;
.,F633 20 42 F6 JSR $F642       BREAK  JSR CLSEI
.,F636 A9 00    LDA #$00        LDA    #0
.,F638 38       SEC             SEC
.,F639 60       RTS             RTS
                                ;
.,F63A 20 DB FC JSR $FCDB       SV40   JSR INCSAL      ;INCREMENT CURRENT ADDR.
.,F63D D0 E5    BNE $F624       BNE    SV30
.,F63F 20 FE ED JSR $EDFE       SV50   JSR UNLSN
.,F642 24 B9    BIT $B9         CLSEI  BIT SA
.,F644 30 11    BMI $F657       BMI    CLSEI2
.,F646 A5 BA    LDA $BA         LDA    FA
.,F648 20 0C ED JSR $ED0C       JSR    LISTN
.,F64B A5 B9    LDA $B9         LDA    SA
.,F64D 29 EF    AND #$EF        AND    #$EF
.,F64F 09 E0    ORA #$E0        ORA    #$E0
.,F651 20 B9 ED JSR $EDB9       JSR    SECND
                                ;
.,F654 20 FE ED JSR $EDFE       CUNLSN JSR UNLSN       ;ENTRY FOR OPENI
                                ;
.,F657 18       CLC             CLSEI2 CLC
.,F658 60       RTS             RTS
.,F659 4A       LSR             SV100  LSR A
.,F65A B0 03    BCS $F65F       BCS    SV102           ;IF C-SET THEN IT'S CASSETTE
                                ;
.,F65C 4C 13 F7 JMP $F713       JMP    ERROR9          ;BAD DEVICE #
                                ;
.,F65F 20 D0 F7 JSR $F7D0       SV102  JSR ZZZ         ;GET ADDR OF TAPE
.,F662 90 8D    BCC $F5F1       BCC    SV10            ;BUFFER IS DEALLOCATED
.,F664 20 38 F8 JSR $F838       JSR    CSTE2
.,F667 B0 25    BCS $F68E       BCS    SV115           ;STOP KEY PRESSED
.,F669 20 8F F6 JSR $F68F       JSR    SAVING          ;TELL USER 'SAVING'
.,F66C A2 03    LDX #$03        SV105  LDX #PLF        ;DECIDE TYPE TO SAVE
.,F66E A5 B9    LDA $B9         LDA    SA              ;1-PLF 0-BLF
.,F670 29 01    AND #$01        AND    #01
.,F672 D0 02    BNE $F676       BNE    SV106
.,F674 A2 01    LDX #$01        LDX    #BLF
.,F676 8A       TXA             SV106  TXA
.,F677 20 6A F7 JSR $F76A       JSR    TAPEH
.,F67A B0 12    BCS $F68E       BCS    SV115           ;STOP KEY PRESSED
.,F67C 20 67 F8 JSR $F867       JSR    TWRT
.,F67F B0 0D    BCS $F68E       BCS    SV115           ;STOP KEY PRESSED
.,F681 A5 B9    LDA $B9         LDA    SA
.,F683 29 02    AND #$02        AND    #2              ;WRITE END OF TAPE?
.,F685 F0 06    BEQ $F68D       BEQ    SV110           ;NO...
                                ;
.,F687 A9 05    LDA #$05        LDA    #EOT
.,F689 20 6A F7 JSR $F76A       JSR    TAPEH
.:F68C 24       .BYTE $24       .BYT   $24             ;SKIP 1 BYTE
                                ;
.,F68D 18       CLC             SV110  CLC
.,F68E 60       RTS             SV115  RTS
                                ;SUBROUTINE TO OUTPUT:
                                ;'SAVING <FILE NAME>'
                                ;
.,F68F A5 9D    LDA $9D         SAVING LDA MSGFLG
.,F691 10 FB    BPL $F68E       BPL    SV115           ;NO PRINT
                                ;
.,F693 A0 51    LDY #$51        LDY    #MS11-MS1       ;'SAVING'
.,F695 20 2F F1 JSR $F12F       JSR    MSG
.,F698 4C C1 F5 JMP $F5C1       JMP    OUTFN           ;<FILE NAME>
                                .END
                                .LIB   TIME
                                ;***********************************
                                ;*                                 *
                                ;* TIME                            *
                                ;*                                 *
                                ;*CONSISTS OF THREE FUNCTIONS:     *
                                ;* (1) UDTIM-- UPDATE TIME. USUALLY*
                                ;*     CALLED EVERY 60TH SECOND.   *
                                ;* (2) SETTIM-- SET TIME. .Y=MSD,  *
                                ;*     .X=NEXT SIGNIFICANT,.A=LSD  *
                                ;* (3) RDTIM-- READ TIME. .Y=MSD,  *
                                ;*     .X=NEXT SIGNIFICANT,.A=LSD  *
                                ;*                                 *
                                ;***********************************
                                ;INTERRUPTS ARE COMING FROM THE 6526 TIMERS
                                ;
.,F69B A2 00    LDX #$00        UDTIM  LDX #0          ;PRE-LOAD FOR LATER
                                ;
                                ;HERE WE PROCEED WITH AN INCREMENT
                                ;OF THE TIME REGISTER.
                                ;
.,F69D E6 A2    INC $A2         UD20   INC TIME+2
.,F69F D0 06    BNE $F6A7       BNE    UD30
.,F6A1 E6 A1    INC $A1         INC    TIME+1
.,F6A3 D0 02    BNE $F6A7       BNE    UD30
.,F6A5 E6 A0    INC $A0         INC    TIME
                                ;
                                ;HERE WE CHECK FOR ROLL-OVER 23:59:59
                                ;AND RESET THE CLOCK TO ZERO IF TRUE
                                ;
.,F6A7 38       SEC             UD30   SEC
.,F6A8 A5 A2    LDA $A2         LDA    TIME+2
.,F6AA E9 01    SBC #$01        SBC    #$01
.,F6AC A5 A1    LDA $A1         LDA    TIME+1
.,F6AE E9 1A    SBC #$1A        SBC    #$1A
.,F6B0 A5 A0    LDA $A0         LDA    TIME
.,F6B2 E9 4F    SBC #$4F        SBC    #$4F
.,F6B4 90 06    BCC $F6BC       BCC    UD60
                                ;
                                ;TIME HAS ROLLED--ZERO REGISTER
                                ;
.,F6B6 86 A0    STX $A0         STX    TIME
.,F6B8 86 A1    STX $A1         STX    TIME+1
.,F6BA 86 A2    STX $A2         STX    TIME+2
                                ;
                                ;SET STOP KEY FLAG HERE
                                ;
.,F6BC AD 01 DC LDA $DC01       UD60   LDA ROWS        ;WAIT FOR IT TO SETTLE
.,F6BF CD 01 DC CMP $DC01       CMP    ROWS
.,F6C2 D0 F8    BNE $F6BC       BNE    UD60            ;STILL BOUNCING
.,F6C4 AA       TAX             TAX                    ;SET FLAGS...
.,F6C5 30 13    BMI $F6DA       BMI    UD80            ;NO STOP KEY...EXIT  STOP KEY=$7F
.,F6C7 A2 BD    LDX #$BD        LDX    #$FF-$42        ;CHECK FOR A SHIFT KEY (C64 KEYBOARD)
.,F6C9 8E 00 DC STX $DC00       STX    COLM
.,F6CC AE 01 DC LDX $DC01       UD70   LDX ROWS        ;WAIT TO SETTLE...
.,F6CF EC 01 DC CPX $DC01       CPX    ROWS
.,F6D2 D0 F8    BNE $F6CC       BNE    UD70
.,F6D4 8D 00 DC STA $DC00       STA    COLM            ;!!!!!WATCH OUT...STOP KEY .A=$7F...SAME AS COLMS WAS...
.,F6D7 E8       INX             INX                    ;ANY KEY DOWN ABORTS
.,F6D8 D0 02    BNE $F6DC       BNE    UD90            ;LEAVE SAME AS BEFORE...
.,F6DA 85 91    STA $91         UD80   STA STKEY       ;SAVE FOR OTHER ROUTINES
.,F6DC 60       RTS             UD90   RTS
.,F6DD 78       SEI             RDTIM  SEI             ;KEEP TIME FROM ROLLING
.,F6DE A5 A2    LDA $A2         LDA    TIME+2          ;GET LSD
.,F6E0 A6 A1    LDX $A1         LDX    TIME+1          ;GET NEXT MOST SIG.
.,F6E2 A4 A0    LDY $A0         LDY    TIME            ;GET MSD
.,F6E4 78       SEI             SETTIM SEI             ;KEEP TIME FROM CHANGING
.,F6E5 85 A2    STA $A2         STA    TIME+2          ;STORE LSD
.,F6E7 86 A1    STX $A1         STX    TIME+1          ;NEXT MOST SIGNIFICANT
.,F6E9 84 A0    STY $A0         STY    TIME            ;STORE MSD
.,F6EB 58       CLI             CLI
.,F6EC 60       RTS             RTS
                                .END
                                .LIB   ERRORHANDLER
                                ;***************************************
                                ;* STOP -- CHECK STOP KEY FLAG AND     *
                                ;* RETURN Z FLAG SET IF FLAG TRUE.     *
                                ;* ALSO CLOSES ACTIVE CHANNELS AND     *
                                ;* FLUSHES KEYBOARD QUEUE.             *
                                ;* ALSO RETURNS KEY DOWNS FROM LAST    *
                                ;* KEYBOARD ROW IN .A.                 *
                                ;***************************************
.,F6ED A5 91    LDA $91         NSTOP  LDA STKEY       ;VALUE OF LAST ROW
.,F6EF C9 7F    CMP #$7F        CMP    #$7F            ;CHECK STOP KEY POSITION
.,F6F1 D0 07    BNE $F6FA       BNE    STOP2           ;NOT DOWN
.,F6F3 08       PHP             PHP
.,F6F4 20 CC FF JSR $FFCC       JSR    CLRCH           ;CLEAR CHANNELS
.,F6F7 85 C6    STA $C6         STA    NDX             ;FLUSH QUEUE
.,F6F9 28       PLP             PLP
.,F6FA 60       RTS             STOP2  RTS
                                ;************************************
                                ;*                                  *
                                ;* ERROR HANDLER                    *
                                ;*                                  *
                                ;* PRINTS KERNAL ERROR MESSAGE IF   *
                                ;* BIT 6 OF MSGFLG SET.  RETURNS    *
                                ;* WITH ERROR # IN .A AND CARRY.    *
                                ;*                                  *
                                ;************************************
                                ;
.,F6FB A9 01    LDA #$01        ERROR1 LDA #1          ;TOO MANY FILES
.:F6FD 2C       .BYTE $2C       .BYT   $2C
.,F6FE A9 02    LDA #$02        ERROR2 LDA #2          ;FILE OPEN
.:F700 2C       .BYTE $2C       .BYT   $2C
.,F701 A9 03    LDA #$03        ERROR3 LDA #3          ;FILE NOT OPEN
.:F703 2C       .BYTE $2C       .BYT   $2C
.,F704 A9 04    LDA #$04        ERROR4 LDA #4          ;FILE NOT FOUND
.:F706 2C       .BYTE $2C       .BYT   $2C
.,F707 A9 05    LDA #$05        ERROR5 LDA #5          ;DEVICE NOT PRESENT
.:F709 2C       .BYTE $2C       .BYT   $2C
.,F70A A9 06    LDA #$06        ERROR6 LDA #6          ;NOT INPUT FILE
.:F70C 2C       .BYTE $2C       .BYT   $2C
.,F70D A9 07    LDA #$07        ERROR7 LDA #7          ;NOT OUTPUT FILE
.:F70F 2C       .BYTE $2C       .BYT   $2C
.,F710 A9 08    LDA #$08        ERROR8 LDA #8          ;MISSING FILE NAME
.:F712 2C       .BYTE $2C       .BYT   $2C
.,F713 A9 09    LDA #$09        ERROR9 LDA #9          ;BAD DEVICE #
                                ;
.,F715 48       PHA             PHA                    ;ERROR NUMBER ON STACK
.,F716 20 CC FF JSR $FFCC       JSR    CLRCH           ;RESTORE I/O CHANNELS
                                ;
.,F719 A0 00    LDY #$00        LDY    #MS1-MS1
.,F71B 24 9D    BIT $9D         BIT    MSGFLG          ;ARE WE PRINTING ERROR?
.,F71D 50 0A    BVC $F729       BVC    EREXIT          ;NO...
                                ;
.,F71F 20 2F F1 JSR $F12F       JSR    MSG             ;PRINT "CBM I/O ERROR #"
.,F722 68       PLA             PLA
.,F723 48       PHA             PHA
.,F724 09 30    ORA #$30        ORA    #$30            ;MAKE ERROR # ASCII
.,F726 20 D2 FF JSR $FFD2       JSR    BSOUT           ;PRINT IT
                                ;
.,F729 68       PLA             EREXIT PLA
.,F72A 38       SEC             SEC
.,F72B 60       RTS             RTS
                                .END
                                .LIB   TAPEFILE
                                ;FAH -- FIND ANY HEADER
                                ;
                                ;READS TAPE DEVICE UNTIL ONE OF FOLLOWING
                                ;BLOCK TYPES FOUND: BDFH--BASIC DATA
                                ;FILE HEADER, BLF--BASIC LOAD FILE
                                ;FOR SUCCESS CARRY IS CLEAR ON RETURN.
                                ;FOR FAILURE CARRY IS SET ON RETURN.
                                ;IN ADDITION ACCUMULATOR IS 0 IF STOP
                                ;KEY WAS PRESSED.
                                ;
.,F72C A5 93    LDA $93         FAH    LDA VERCK       ;SAVE OLD VERIFY
.,F72E 48       PHA             PHA
.,F72F 20 41 F8 JSR $F841       JSR    RBLK            ;READ TAPE BLOCK
.,F732 68       PLA             PLA
.,F733 85 93    STA $93         STA    VERCK           ;RESTORE VERIFY FLAG
.,F735 B0 32    BCS $F769       BCS    FAH40           ;READ TERMINATED
                                ;
.,F737 A0 00    LDY #$00        LDY    #0
.,F739 B1 B2    LDA ($B2),Y     LDA    (TAPE1)Y        ;GET HEADER TYPE
                                ;
.,F73B C9 05    CMP #$05        CMP    #EOT            ;CHECK END OF TAPE?
.,F73D F0 2A    BEQ $F769       BEQ    FAH40           ;YES...FAILURE
                                ;
.,F73F C9 01    CMP #$01        CMP    #BLF            ;BASIC LOAD FILE?
.,F741 F0 08    BEQ $F74B       BEQ    FAH50           ;YES...SUCCESS
                                ;
.,F743 C9 03    CMP #$03        CMP    #PLF            ;FIXED LOAD FILE?
.,F745 F0 04    BEQ $F74B       BEQ    FAH50           ;YES...SUCCESS
                                ;
.,F747 C9 04    CMP #$04        CMP    #BDFH           ;BASIC DATA FILE?
.,F749 D0 E1    BNE $F72C       BNE    FAH             ;NO...KEEP TRYING
                                ;
.,F74B AA       TAX             FAH50  TAX             ;RETURN FILE TYPE IN .X
.,F74C 24 9D    BIT $9D         BIT    MSGFLG          ;PRINTING MESSAGES?
.,F74E 10 17    BPL $F767       BPL    FAH45           ;NO...
                                ;
.,F750 A0 63    LDY #$63        LDY    #MS17-MS1       ;PRINT "FOUND"
.,F752 20 2F F1 JSR $F12F       JSR    MSG
                                ;
                                ;OUTPUT COMPLETE FILE NAME
                                ;
.,F755 A0 05    LDY #$05        LDY    #5
.,F757 B1 B2    LDA ($B2),Y     FAH55  LDA (TAPE1)Y
.,F759 20 D2 FF JSR $FFD2       JSR    BSOUT
.,F75C C8       INY             INY
.,F75D C0 15    CPY #$15        CPY    #21
.,F75F D0 F6    BNE $F757       BNE    FAH55
                                ;
.,F761 A5 A1    LDA $A1         FAH56  LDA STKEY       ;KEY  DOWN ON LAST ROW...
.,F763 20 E0 E4 JSR $E4E0              JSR FPATCH      ;GOTO PATCH...
.,F766 EA       NOP                    NOP
                                ;
.,F767 18       CLC             FAH45  CLC             ;SUCCESS FLAG
.,F768 88       DEY             DEY                    ;MAKE NONZERO FOR OKAY RETURN
                                ;
.,F769 60       RTS             FAH40  RTS
                                ;TAPEH--WRITE TAPE HEADER
                                ;ERROR IF TAPE BUFFER DE-ALLOCATED
                                ;CARRY CLEAR IF O.K.
                                ;
.,F76A 85 9E    STA $9E         TAPEH  STA T1
                                ;
                                ;DETERMINE ADDRESS OF BUFFER
                                ;
.,F76C 20 D0 F7 JSR $F7D0       JSR    ZZZ
.,F76F 90 5E    BCC $F7CF       BCC    TH40            ;BUFFER WAS DE-ALLOCATED
                                ;
                                ;PRESERVE START AND END ADDRESSES
                                ;FOR CASE OF HEADER FOR LOAD FILE
                                ;
.,F771 A5 C2    LDA $C2         LDA    STAH
.,F773 48       PHA             PHA
.,F774 A5 C1    LDA $C1         LDA    STAL
.,F776 48       PHA             PHA
.,F777 A5 AF    LDA $AF         LDA    EAH
.,F779 48       PHA             PHA
.,F77A A5 AE    LDA $AE         LDA    EAL
.,F77C 48       PHA             PHA
                                ;
                                ;PUT BLANKS IN TAPE BUFFER
                                ;
.,F77D A0 BF    LDY #$BF        LDY    #BUFSZ-1
.,F77F A9 20    LDA #$20        LDA    #'
.,F781 91 B2    STA ($B2),Y     BLNK2  STA (TAPE1)Y
.,F783 88       DEY             DEY
.,F784 D0 FB    BNE $F781       BNE    BLNK2
                                ;
                                ;PUT BLOCK TYPE IN HEADER
                                ;
.,F786 A5 9E    LDA $9E         LDA    T1
.,F788 91 B2    STA ($B2),Y     STA    (TAPE1)Y
                                ;
                                ;PUT START LOAD ADDRESS IN HEADER
                                ;
.,F78A C8       INY             INY
.,F78B A5 C1    LDA $C1         LDA    STAL
.,F78D 91 B2    STA ($B2),Y     STA    (TAPE1)Y
.,F78F C8       INY             INY
.,F790 A5 C2    LDA $C2         LDA    STAH
.,F792 91 B2    STA ($B2),Y     STA    (TAPE1)Y
                                ;
                                ;PUT END LOAD ADDRESS IN HEADER
                                ;
.,F794 C8       INY             INY
.,F795 A5 AE    LDA $AE         LDA    EAL
.,F797 91 B2    STA ($B2),Y     STA    (TAPE1)Y
.,F799 C8       INY             INY
.,F79A A5 AF    LDA $AF         LDA    EAH
.,F79C 91 B2    STA ($B2),Y     STA    (TAPE1)Y
                                ;
                                ;PUT FILE NAME IN HEADER
                                ;
.,F79E C8       INY             INY
.,F79F 84 9F    STY $9F         STY    T2
.,F7A1 A0 00    LDY #$00        LDY    #0
.,F7A3 84 9E    STY $9E         STY    T1
.,F7A5 A4 9E    LDY $9E         TH20   LDY T1
.,F7A7 C4 B7    CPY $B7         CPY    FNLEN
.,F7A9 F0 0C    BEQ $F7B7       BEQ    TH30
.,F7AB B1 BB    LDA ($BB),Y     LDA    (FNADR)Y
.,F7AD A4 9F    LDY $9F         LDY    T2
.,F7AF 91 B2    STA ($B2),Y     STA    (TAPE1)Y
.,F7B1 E6 9E    INC $9E         INC    T1
.,F7B3 E6 9F    INC $9F         INC    T2
.,F7B5 D0 EE    BNE $F7A5       BNE    TH20
                                ;
                                ;SET UP START AND END ADDRESS OF HEADER
                                ;
.,F7B7 20 D7 F7 JSR $F7D7       TH30   JSR LDAD1
                                ;
                                ;SET UP TIME FOR LEADER
                                ;
.,F7BA A9 69    LDA #$69        LDA    #$69
.,F7BC 85 AB    STA $AB         STA    SHCNH
                                ;
.,F7BE 20 6B F8 JSR $F86B       JSR    TWRT2           ;WRITE HEADER ON TAPE
                                ;
                                ;RESTORE START AND END ADDRESS OF
                                ;LOAD FILE.
                                ;
.,F7C1 A8       TAY             TAY                    ;SAVE ERROR CODE IN .Y
.,F7C2 68       PLA             PLA
.,F7C3 85 AE    STA $AE         STA    EAL
.,F7C5 68       PLA             PLA
.,F7C6 85 AF    STA $AF         STA    EAH
.,F7C8 68       PLA             PLA
.,F7C9 85 C1    STA $C1         STA    STAL
.,F7CB 68       PLA             PLA
.,F7CC 85 C2    STA $C2         STA    STAH
.,F7CE 98       TYA             TYA                    ;RESTORE ERROR CODE FOR RETURN
                                ;
.,F7CF 60       RTS             TH40   RTS
                                ;FUNCTION TO RETURN TAPE BUFFER
                                ;ADDRESS IN TAPE1
                                ;
.,F7D0 A6 B2    LDX $B2         ZZZ    LDX TAPE1       ;ASSUME TAPE1
.,F7D2 A4 B3    LDY $B3         LDY    TAPE1+1
.,F7D4 C0 02    CPY #$02        CPY    #>BUF           ;CHECK FOR ALLOCATION...
                                ;...[TAPE1+1]=0 OR 1 MEANS DEALLOCATED
                                ;...C CLR => DEALLOCATED
.,F7D6 60       RTS             RTS
.,F7D7 20 D0 F7 JSR $F7D0       LDAD1  JSR ZZZ         ;GET PTR TO CASSETTE
.,F7DA 8A       TXA             TXA
.,F7DB 85 C1    STA $C1         STA    STAL            ;SAVE START LOW
.,F7DD 18       CLC             CLC
.,F7DE 69 C0    ADC #$C0        ADC    #BUFSZ          ;COMPUTE POINTER TO END
.,F7E0 85 AE    STA $AE         STA    EAL             ;SAVE END LOW
.,F7E2 98       TYA             TYA
.,F7E3 85 C2    STA $C2         STA    STAH            ;SAVE START HIGH
.,F7E5 69 00    ADC #$00        ADC    #0              ;COMPUTE POINTER TO END
.,F7E7 85 AF    STA $AF         STA    EAH             ;SAVE END HIGH
.,F7E9 60       RTS             RTS
.,F7EA 20 2C F7 JSR $F72C       FAF    JSR FAH         ;FIND ANY HEADER
.,F7ED B0 1D    BCS $F80C       BCS    FAF40           ;FAILED
                                ;
                                ;SUCCESS...SEE IF RIGHT NAME
                                ;
.,F7EF A0 05    LDY #$05        LDY    #5              ;OFFSET INTO TAPE HEADER
.,F7F1 84 9F    STY $9F         STY    T2
.,F7F3 A0 00    LDY #$00        LDY    #0              ;OFFSET INTO FILE NAME
.,F7F5 84 9E    STY $9E         STY    T1
.,F7F7 C4 B7    CPY $B7         FAF20  CPY FNLEN       ;COMPARE THIS MANY
.,F7F9 F0 10    BEQ $F80B       BEQ    FAF30           ;DONE
                                ;
.,F7FB B1 BB    LDA ($BB),Y     LDA    (FNADR)Y
.,F7FD A4 9F    LDY $9F         LDY    T2
.,F7FF D1 B2    CMP ($B2),Y     CMP    (TAPE1)Y
.,F801 D0 E7    BNE $F7EA       BNE    FAF             ;MISMATCH--TRY NEXT HEADER
.,F803 E6 9E    INC $9E         INC    T1
.,F805 E6 9F    INC $9F         INC    T2
.,F807 A4 9E    LDY $9E         LDY    T1
.,F809 D0 EC    BNE $F7F7       BNE    FAF20           ;BRANCH ALWAYS
                                ;
.,F80B 18       CLC             FAF30  CLC             ;SUCCESS FLAG
.,F80C 60       RTS             FAF40  RTS
                                .END
                                .LIB   TAPECONTROL
.,F80D 20 D0 F7 JSR $F7D0       JTP20  JSR ZZZ
.,F810 E6 A6    INC $A6         INC    BUFPT
.,F812 A4 A6    LDY $A6         LDY    BUFPT
.,F814 C0 C0    CPY #$C0        CPY    #BUFSZ
.,F816 60       RTS             RTS
                                ;STAYS IN ROUTINE D2T1LL PLAY SWITCH
                                ;
.,F817 20 2E F8 JSR $F82E       CSTE1  JSR CS10
.,F81A F0 1A    BEQ $F836       BEQ    CS25
.,F81C A0 1B    LDY #$1B        LDY    #MS7-MS1        ;"PRESS PLAY..."
.,F81E 20 2F F1 JSR $F12F       CS30   JSR MSG
.,F821 20 D0 F8 JSR $F8D0       CS40   JSR TSTOP       ;WATCH FOR STOP KEY
.,F824 20 2E F8 JSR $F82E       JSR    CS10            ;WATCH CASSETTE SWITCHES
.,F827 D0 F8    BNE $F821       BNE    CS40
.,F829 A0 6A    LDY #$6A        LDY    #MS18-MS1       ;"OK"
.,F82B 4C 2F F1 JMP $F12F       JMP    MSG
                                ;SUBR RETURNS <> FOR CASSETTE SWITCH
                                ;
.,F82E A9 10    LDA #$10        CS10   LDA #$10        ;CHECK PORT
.,F830 24 01    BIT $01         BIT    R6510           ;CLOSED?...
.,F832 D0 02    BNE $F836       BNE    CS25            ;NO. . .
.,F834 24 01    BIT $01         BIT    R6510           ;CHECK AGAIN TO DEBOUNCE
.,F836 18       CLC             CS25   CLC             ;GOOD RETURN
.,F837 60       RTS             RTS
                                ;CHECKS FOR PLAY & RECORD
                                ;
.,F838 20 2E F8 JSR $F82E       CSTE2  JSR CS10
.,F83B F0 F9    BEQ $F836       BEQ    CS25
.,F83D A0 2E    LDY #$2E        LDY    #MS8-MS1        ;"RECORD"
.,F83F D0 DD    BNE $F81E       BNE    CS30
                                ;READ HEADER BLOCK ENTRY
                                ;
.,F841 A9 00    LDA #$00        RBLK   LDA #0
.,F843 85 90    STA $90         STA    STATUS
.,F845 85 93    STA $93         STA    VERCK
.,F847 20 D7 F7 JSR $F7D7       JSR    LDAD1
                                ;READ LOAD BLOCK ENTRY
                                ;
.,F84A 20 17 F8 JSR $F817       TRD    JSR CSTE1       ;SAY 'PRESS PLAY'
.,F84D B0 1F    BCS $F86E       BCS    TWRT3           ;STOP KEY PRESSED
.,F84F 78       SEI             SEI
.,F850 A9 00    LDA #$00        LDA    #0              ;CLEAR FLAGS...
.,F852 85 AA    STA $AA         STA    RDFLG
.,F854 85 B4    STA $B4         STA    SNSW1
.,F856 85 B0    STA $B0         STA    CMP0
.,F858 85 9E    STA $9E         STA    PTR1
.,F85A 85 9F    STA $9F         STA    PTR2
.,F85C 85 9C    STA $9C         STA    DPSW
.,F85E A9 90    LDA #$90        LDA    #$90            ;ENABLE FOR CA1 IRQ...READ LINE
.,F860 A2 0E    LDX #$0E        LDX    #14             ;POINT IRQ VECTOR TO READ
.,F862 D0 11    BNE $F875       BNE    TAPE            ;JMP
                                ;WRITE HEADER BLOCK ENTRY
                                ;
.,F864 20 D7 F7 JSR $F7D7       WBLK   JSR LDAD1
                                ;
                                ;WRITE LOAD BLOCK ENTRY
                                ;
.,F867 A9 14    LDA #$14        TWRT   LDA #20         ;BETWEEN BLOCK SHORTS
.,F869 85 AB    STA $AB         STA    SHCNH
.,F86B 20 38 F8 JSR $F838       TWRT2  JSR CSTE2       ;SAY 'PRESS PLAY & RECORD'
.,F86E B0 6C    BCS $F8DC       TWRT3  BCS STOP3       ;STOP KEY PRESSED
.,F870 78       SEI             SEI
.,F871 A9 82    LDA #$82        LDA    #$82            ;ENABLE T2 IRQS...WRITE TIME
.,F873 A2 08    LDX #$08        LDX    #8              ;VECTOR IRQ TO WRTZ
                                ;START TAPE OPERATION ENTRY POINT
                                ;
.,F875 A0 7F    LDY #$7F        TAPE   LDY #$7F        ;KILL UNWANTED IRQ'S
.,F877 8C 0D DC STY $DC0D              STY D1ICR
.,F87A 8D 0D DC STA $DC0D              STA D1ICR       ;TURN ON WANTED
.,F87D AD 0E DC LDA $DC0E              LDA D1CRA       ;CALC TIMER ENABLES
.,F880 09 19    ORA #$19               ORA #$19
.,F882 8D 0F DC STA $DC0F              STA D1CRB       ;TURN ON T2 IRQ'S FOR CASS WRITE(ONE SHOT)
.,F885 29 91    AND #$91               AND #$91        ;SAVE TOD 50/60 INDICATION
.,F887 8D A2 02 STA $02A2              STA CASTON      ;PLACE IN AUTO MODE FOR T1
                                ; WAIT FOR RS-232 TO FINISH
.,F88A 20 A4 F0 JSR $F0A4              JSR RSP232
                                ; DISABLE SCREEN DISPLAY
.,F88D AD 11 D0 LDA $D011              LDA VICREG+17
.,F890 29 EF    AND #$EF               AND #$FF-$10    ;DISABLE SCREEN
.,F892 8D 11 D0 STA $D011              STA VICREG+17
                                ; MOVE IRQ TO IRQTEMP FOR CASS OPS
.,F895 AD 14 03 LDA $0314       LDA    CINV
.,F898 8D 9F 02 STA $029F       STA    IRQTMP
.,F89B AD 15 03 LDA $0315       LDA    CINV+1
.,F89E 8D A0 02 STA $02A0       STA    IRQTMP+1
.,F8A1 20 BD FC JSR $FCBD       JSR    BSIV            ;GO CHANGE IRQ VECTOR
.,F8A4 A9 02    LDA #$02        LDA    #2              ;FSBLK STARTS AT 2
.,F8A6 85 BE    STA $BE         STA    FSBLK
.,F8A8 20 97 FB JSR $FB97       JSR    NEWCH           ;PREP LOCAL COUNTERS AND FLAGS
.,F8AB A5 01    LDA $01         LDA    R6510           ;TURN MOTOR ON
.,F8AD 29 1F    AND #$1F        AND    #%011111        ;LOW TURNS ON
.,F8AF 85 01    STA $01         STA    R6510
.,F8B1 85 C0    STA $C0         STA    CAS1            ;FLAG INTERNAL CONTROL OF CASS MOTOR
.,F8B3 A2 FF    LDX #$FF        LDX    #$FF            ;DELAY BETWEEN BLOCKS
.,F8B5 A0 FF    LDY #$FF        TP32   LDY #$FF
.,F8B7 88       DEY             TP35   DEY
.,F8B8 D0 FD    BNE $F8B7       BNE    TP35
.,F8BA CA       DEX             DEX
.,F8BB D0 F8    BNE $F8B5       BNE    TP32
.,F8BD 58       CLI             CLI
.,F8BE AD A0 02 LDA $02A0       TP40   LDA IRQTMP+1    ;CHECK FOR INTERRUPT VECTOR...
.,F8C1 CD 15 03 CMP $0315       CMP    CINV+1          ;...POINTING AT KEY ROUTINE
.,F8C4 18       CLC             CLC
.,F8C5 F0 15    BEQ $F8DC       BEQ    STOP3           ;...YES RETURN
.,F8C7 20 D0 F8 JSR $F8D0       JSR    TSTOP           ;...NO CHECK FOR STOP KEY
                                ;
                                ; 60 HZ KEYSCAN IGNORED
                                ;
.,F8CA 20 BC F6 JSR $F6BC       JSR    UD60            ; STOP KEY CHECK
.,F8CD 4C BE F8 JMP $F8BE       JMP    TP40            ;STAY IN LOOP UNTILL TAPES ARE DONE
.,F8D0 20 E1 FF JSR $FFE1       TSTOP  JSR STOP        ;STOP KEY DOWN?
.,F8D3 18       CLC             CLC                    ;ASSUME NO STOP
.,F8D4 D0 0B    BNE $F8E1       BNE    STOP4           ;WE WERE RIGHT
                                ;
                                ;STOP KEY DOWN...
                                ;
.,F8D6 20 93 FC JSR $FC93       JSR    TNIF            ;TURN OFF CASSETTES
.,F8D9 38       SEC             SEC                    ;FAILURE FLAG
.,F8DA 68       PLA             PLA                    ;BACK ONE SQUARE...
.,F8DB 68       PLA             PLA
                                ;
                                ; LDA #0 ;STOP KEY FLAG
                                ;
.,F8DC A9 00    LDA #$00        STOP3  LDA #0          ;DEALLOCATE IRQTMP
.,F8DE 8D A0 02 STA $02A0       STA    IRQTMP+1        ;IF C-SET THEN STOP KEY
.,F8E1 60       RTS             STOP4  RTS
                                ;
                                ; STT1 - SET UP TIMEOUT WATCH FOR NEXT DIPOLE
                                ;
.,F8E2 86 B1    STX $B1         STT1   STX TEMP        ;.X HAS CONSTANT FOR TIMEOUT
.,F8E4 A5 B0    LDA $B0         LDA    CMP0            ;CMP0*5
.,F8E6 0A       ASL             ASL    A
.,F8E7 0A       ASL             ASL    A
.,F8E8 18       CLC             CLC
.,F8E9 65 B0    ADC $B0         ADC    CMP0
.,F8EB 18       CLC             CLC
.,F8EC 65 B1    ADC $B1         ADC    TEMP            ;ADJUST LONG BYTE COUNT
.,F8EE 85 B1    STA $B1         STA    TEMP
.,F8F0 A9 00    LDA #$00        LDA    #0
.,F8F2 24 B0    BIT $B0         BIT    CMP0            ;CHECK CMP0 ...
.,F8F4 30 01    BMI $F8F7       BMI    STT2            ;...MINUS, NO ADJUST
.,F8F6 2A       ROL             ROL    A               ;...PLUS SO ADJUST POS
.,F8F7 06 B1    ASL $B1         STT2   ASL TEMP        ;MULTIPLY CORRECTED VALUE BY 4
.,F8F9 2A       ROL             ROL    A
.,F8FA 06 B1    ASL $B1         ASL    TEMP
.,F8FC 2A       ROL             ROL    A
.,F8FD AA       TAX             TAX
.,F8FE AD 06 DC LDA $DC06       STT3   LDA D1T2L       ;WATCH OUT FOR D1T2H ROLLOVER...
.,F901 C9 16    CMP #$16        CMP    #22             ;...TIME FOR ROUTINE...!!!...
.,F903 90 F9    BCC $F8FE       BCC    STT3            ;...TOO CLOSE SO WAIT UNTILL PAST
.,F905 65 B1    ADC $B1         ADC    TEMP            ;CALCULATE AND...
.,F907 8D 04 DC STA $DC04       STA    D1T1L           ;...STORE ADUSTED TIME COUNT
.,F90A 8A       TXA             TXA
.,F90B 6D 07 DC ADC $DC07       ADC    D1T2H           ;ADJUST FOR HIGH TIME COUNT
.,F90E 8D 05 DC STA $DC05       STA    D1T1H
.,F911 AD A2 02 LDA $02A2       LDA    CASTON          ;ENABLE TIMERS
.,F914 8D 0E DC STA $DC0E       STA    D1CRA
.,F917 8D A4 02 STA $02A4       STA    STUPID          ;NON-ZERO MEANS AN T1 IRQ HAS NOT OCCURED YET
.,F91A AD 0D DC LDA $DC0D       LDA    D1ICR           ;CLEAR OLD T1 INTERRUPT
.,F91D 29 10    AND #$10        AND    #$10            ;CHECK FOR OLD-FLAG IRQ
.,F91F F0 09    BEQ $F92A       BEQ    STT4            ;NO...NORMAL EXIT
.,F921 A9 F9    LDA #$F9        LDA    #>STT4          ;PUSH SIMULATED RETURN ADDRESS ON STACK
.,F923 48       PHA             PHA
.,F924 A9 2A    LDA #$2A        LDA    #<STT4
.,F926 48       PHA             PHA
.,F927 4C 43 FF JMP $FF43       JMP    SIMIRQ
.,F92A 58       CLI             STT4   CLI             ;ALLOW FOR RE-ENTRY CODE
.,F92B 60       RTS             RTS
                                .END
                                .LIB   READ
                                ; VARIABLES USED IN CASSETTE READ ROUTINES
                                ;
                                ;  REZ - COUNTS ZEROS (IF Z THEN CORRECT # OF DIPOLES)
                                ;  RER - FLAGS ERRORS (IF Z THEN NO ERROR)
                                ;  DIFF - USED TO PRESERVE SYNO (OUTSIDE OF BIT ROUTINES)
                                ;  SYNO - FLAGS IF WE HAVE BLOCK SYNC (16 ZERO DIPOLES)
                                ;  SNSW1 - FLAGS IF WE HAVE BYTE SYNC (A LONGLONG)
                                ;  DATA - HOLDS MOST RECENT DIPOLE BIT VALUE
                                ;  MYCH - HOLDS INPUT BYTE BEING BUILT
                                ;  FIRT - USED TO INDICATE WHICH HALF OF DIPOLE WE'RE IN
                                ;  SVXT - TEMP USED TO ADJUST SOFTWARE SERVO
                                ;  TEMP - USED TO HOLD DIPOLE TIME DURING TYPE CALCULATIONS
                                ;  PRTY - HOLDS CURRENT CALCULATED PARITY BIT
                                ;  PRP - HAS COMBINED ERROR VALUES FROM BIT ROUTINES
                                ;  FSBLK - INDICATE WHICH BLOCK WE'RE LOOKING AT (0 TO EXIT)
                                ;  SHCNL - HOLDS FSBLK, USED TO DIRECT ROUTINES, BECAUSE OF EXIT CASE
                                ;  RDFLG - HOLDS FUNCTION MODE
                                ;     MI - WAITING FOR BLOCK SYNC
                                ;     VS - IN DATA BLOCK READING DATA
                                ;     NE - WAITING FOR BYTE SYNC
                                ;  SAL - INDIRECT TO DATA STORAGE AREA
                                ;  SHCNH - LEFT OVER FROM DEBUGGING
                                ;  BAD - STORAGE SPACE FOR BAD READ LOCATIONS (BOTTOM OF STACK)
                                ;  PTR1 - COUNT OF READ LOCATIONS IN ERROR (POINTER INTO BAD, MAX 61)
                                ;  PTR2 - COUNT OF RE-READ LOCATIONS (POINTER INTO BAD, DURING RE-READ)
                                ;  VERCHK - VERIFY OR LOAD FLAG (Z - LOADING)
                                ;  CMP0 - SOFTWARE SERVO (+/- ADJUST TO TIME CALCS)
                                ;  DPSW - IF NZ THEN EXPECTING LL/L COMBINATION THAT ENDS A BYTE
                                ;  PCNTR - COUNTS DOWN FROM 8-0 FOR DATA THEN TO FF FOR PARITY
                                ;  STUPID - HOLD INDICATOR (NZ - NO T1IRQ YET) FOR T1IRQ
                                ;  KIKA26 - HOLDS OLD D1ICR AFTER CLEAR ON READ
                                ;
.,F92C AE 07 DC LDX $DC07       READ   LDX D1T2H       ;GET TIME SINCE LAST INTERRUPT
.,F92F A0 FF    LDY #$FF        LDY    #$FF            ;COMPUTE COUNTER DIFFERENCE
.,F931 98       TYA             TYA
.,F932 ED 06 DC SBC $DC06       SBC    D1T2L
.,F935 EC 07 DC CPX $DC07       CPX    D1T2H           ;CHECK FOR TIMER HIGH ROLLOVER...
.,F938 D0 F2    BNE $F92C       BNE    READ            ;...YES THEN RECOMPUTE
.,F93A 86 B1    STX $B1         STX    TEMP
.,F93C AA       TAX             TAX
.,F93D 8C 06 DC STY $DC06       STY    D1T2L           ;RELOAD TIMER2 (COUNT DOWN FROM $FFFF)
.,F940 8C 07 DC STY $DC07       STY    D1T2H
.,F943 A9 19    LDA #$19        LDA    #$19            ;ENABLE TIMER
.,F945 8D 0F DC STA $DC0F       STA    D1CRB
.,F948 AD 0D DC LDA $DC0D       LDA    D1ICR           ;CLEAR READ INTERRUPT
.,F94B 8D A3 02 STA $02A3       STA    KIKA26          ;SAVE FOR LATTER
.,F94E 98       TYA             TYA
.,F94F E5 B1    SBC $B1         SBC    TEMP            ;CALCULATE HIGH
.,F951 86 B1    STX $B1         STX    TEMP
.,F953 4A       LSR             LSR    A               ;MOVE TWO BITS FROM HIGH TO TEMP
.,F954 66 B1    ROR $B1         ROR    TEMP
.,F956 4A       LSR             LSR    A
.,F957 66 B1    ROR $B1         ROR    TEMP
.,F959 A5 B0    LDA $B0         LDA    CMP0            ;CALC MIN PULSE VALUE
.,F95B 18       CLC             CLC
.,F95C 69 3C    ADC #$3C        ADC    #60
.,F95E C5 B1    CMP $B1         CMP    TEMP            ;IF PULSE LESS THAN MIN...
.,F960 B0 4A    BCS $F9AC       BCS    RDBK            ;...THEN IGNORE AS NOISE
.,F962 A6 9C    LDX $9C         LDX    DPSW            ;CHECK IF LAST BIT...
.,F964 F0 03    BEQ $F969       BEQ    RJDJ            ;...NO THEN CONTINUE
.,F966 4C 60 FA JMP $FA60       JMP    RADJ            ;...YES THEN GO FINISH BYTE
.,F969 A6 A3    LDX $A3         RJDJ   LDX PCNTR       ;IF 9 BITS READ...
.,F96B 30 1B    BMI $F988       BMI    JRAD2           ;... THEN GOTO ENDING
.,F96D A2 00    LDX #$00        LDX    #0              ;SET BIT VALUE TO ZERO
.,F96F 69 30    ADC #$30        ADC    #48             ;ADD UP TO HALF WAY BETWEEN...
.,F971 65 B0    ADC $B0         ADC    CMP0            ;...SHORT PULSE AND SYNC PULSE
.,F973 C5 B1    CMP $B1         CMP    TEMP            ;CHECK FOR SHORT...
.,F975 B0 1C    BCS $F993       BCS    RADX2           ;...YES IT'S A SHORT
.,F977 E8       INX             INX                    ;SET BIT VALUE TO ONE
.,F978 69 26    ADC #$26        ADC    #38             ;MOVE TO MIDDLE OF HIGH
.,F97A 65 B0    ADC $B0         ADC    CMP0
.,F97C C5 B1    CMP $B1         CMP    TEMP            ;CHECK FOR ONE...
.,F97E B0 17    BCS $F997       BCS    RADL            ;...YES IT'S A ONE
.,F980 69 2C    ADC #$2C        ADC    #44             ;MOVE TO LONGLONG
.,F982 65 B0    ADC $B0         ADC    CMP0
.,F984 C5 B1    CMP $B1         CMP    TEMP            ;CHECK FOR LONGLONG...
.,F986 90 03    BCC $F98B       BCC    SRER            ;...GREATER THAN IS ERROR
.,F988 4C 10 FA JMP $FA10       JRAD2  JMP RAD2        ;...IT'S A LONGLONG
.,F98B A5 B4    LDA $B4         SRER   LDA SNSW1       ;IF NOT SYNCRONIZED...
.,F98D F0 1D    BEQ $F9AC       BEQ    RDBK            ;...THEN NO ERROR
.,F98F 85 A8    STA $A8         STA    RER             ;...ELSE FLAG RER
.,F991 D0 19    BNE $F9AC       BNE    RDBK            ;JMP
.,F993 E6 A9    INC $A9         RADX2  INC REZ         ;COUNT REZ UP ON ZEROS
.,F995 B0 02    BCS $F999       BCS    RAD5            ;JMP
.,F997 C6 A9    DEC $A9         RADL   DEC REZ         ;COUNT REZ DOWN ON ONES
.,F999 38       SEC             RAD5   SEC             ;CALC ACTUAL VALUE FOR COMPARE STORE
.,F99A E9 13    SBC #$13        SBC    #19
.,F99C E5 B1    SBC $B1         SBC    TEMP            ;SUBTRACT INPUT VALUE FROM CONSTANT...
.,F99E 65 92    ADC $92         ADC    SVXT            ;...ADD DIFFERENCE TO TEMP STORAGE...
.,F9A0 85 92    STA $92         STA    SVXT            ;...USED LATER TO ADJUST SOFT SERVO
.,F9A2 A5 A4    LDA $A4         LDA    FIRT            ;FLIP DIPOLE FLAG
.,F9A4 49 01    EOR #$01        EOR    #1
.,F9A6 85 A4    STA $A4         STA    FIRT
.,F9A8 F0 2B    BEQ $F9D5       BEQ    RAD3            ;SECOND HALF OF DIPOLE
.,F9AA 86 D7    STX $D7         STX    DATA            ;FIRST HALF SO STORE ITS VALUE
.,F9AC A5 B4    LDA $B4         RDBK   LDA SNSW1       ;IF NO BYTE START...
.,F9AE F0 22    BEQ $F9D2       BEQ    RADBK           ;...THEN RETURN
.,F9B0 AD A3 02 LDA $02A3       LDA    KIKA26          ;CHECK TO SEE IF TIMER1 IRQD US...
.,F9B3 29 01    AND #$01        AND    #$01
.,F9B5 D0 05    BNE $F9BC       BNE    RADKX           ;...YES
.,F9B7 AD A4 02 LDA $02A4       LDA    STUPID          ;CHECK FOR OLD T1IRQ
.,F9BA D0 16    BNE $F9D2       BNE    RADBK           ;NO...SO EXIT
                                ;
.,F9BC A9 00    LDA #$00        RADKX  LDA #0          ;...YES, SET DIPOLE FLAG FOR FIRST HALF
.,F9BE 85 A4    STA $A4         STA    FIRT
.,F9C0 8D A4 02 STA $02A4       STA    STUPID          ;SET T1IRQ FLAG
.,F9C3 A5 A3    LDA $A3         LDA    PCNTR           ;CHECK WHERE WE ARE IN BYTE...
.,F9C5 10 30    BPL $F9F7       BPL    RAD4            ;...DOING DATA
.,F9C7 30 BF    BMI $F988       BMI    JRAD2           ;...PROCESS PARITY
.,F9C9 A2 A6    LDX #$A6        RADP   LDX #166        ;SET UP FOR LONGLONG TIMEOUT
.,F9CB 20 E2 F8 JSR $F8E2       JSR    STT1
.,F9CE A5 9B    LDA $9B         LDA    PRTY            ;IF PARITY NOT EVEN...
.,F9D0 D0 B9    BNE $F98B       BNE    SRER            ;...THEN GO SET ERROR
.,F9D2 4C BC FE JMP $FEBC       RADBK  JMP PREND       ;GO RESTORE REGS AND RTI
.,F9D5 A5 92    LDA $92         RAD3   LDA SVXT        ;ADJUST THE SOFTWARE SERVO (CMP0)
.,F9D7 F0 07    BEQ $F9E0       BEQ    ROUT1           ;NO ADJUST
.,F9D9 30 03    BMI $F9DE       BMI    ROUT2           ;ADJUST FOR MORE BASE TIME
.,F9DB C6 B0    DEC $B0         DEC    CMP0            ;ADJUST FOR LESS BASE TIME
.:F9DD 2C       .BYTE $2C       .BYT   $2C             ;SKIP TWO BYTES
.,F9DE E6 B0    INC $B0         ROUT2  INC CMP0
.,F9E0 A9 00    LDA #$00        ROUT1  LDA #0          ;CLEAR DIFFERENCE VALUE
.,F9E2 85 92    STA $92         STA    SVXT
                                ;CHECK FOR CONSECUTIVE LIKE VALUES IN DIPOLE...
.,F9E4 E4 D7    CPX $D7         CPX    DATA
.,F9E6 D0 0F    BNE $F9F7       BNE    RAD4            ;...NO, GO PROCESS INFO
.,F9E8 8A       TXA             TXA                    ;...YES SO CHECK THE VALUES...
.,F9E9 D0 A0    BNE $F98B       BNE    SRER            ;IF THEY WERE ONES THEN  ERROR
                                ; CONSECUTIVE ZEROS
.,F9EB A5 A9    LDA $A9         LDA    REZ             ;...CHECK HOW MANY ZEROS HAVE HAPPENED
.,F9ED 30 BD    BMI $F9AC       BMI    RDBK            ;...IF MANY DON'T CHECK
.,F9EF C9 10    CMP #$10        CMP    #16             ;... DO WE HAVE 16 YET?...
.,F9F1 90 B9    BCC $F9AC       BCC    RDBK            ;....NO SO CONTINUE
.,F9F3 85 96    STA $96         STA    SYNO            ;....YES SO FLAG SYNO (BETWEEN BLOCKS)
.,F9F5 B0 B5    BCS $F9AC       BCS    RDBK            ;JMP
.,F9F7 8A       TXA             RAD4   TXA             ;MOVE READ DATA TO .A
.,F9F8 45 9B    EOR $9B         EOR    PRTY            ;CALCULATE PARITY
.,F9FA 85 9B    STA $9B         STA    PRTY
.,F9FC A5 B4    LDA $B4         LDA    SNSW1           ;REAL DATA?...
.,F9FE F0 D2    BEQ $F9D2       BEQ    RADBK           ;...NO SO FORGET BY EXITING
.,FA00 C6 A3    DEC $A3         DEC    PCNTR           ;DEC BIT COUNT
.,FA02 30 C5    BMI $F9C9       BMI    RADP            ;IF MINUS THEN  TIME FOR PARITY
.,FA04 46 D7    LSR $D7         LSR    DATA            ;SHIFT BIT FROM DATA...
.,FA06 66 BF    ROR $BF         ROR    MYCH            ;...INTO BYTE STORAGE (MYCH) BUFFER
.,FA08 A2 DA    LDX #$DA        LDX    #218            ;SET UP FOR NEXT DIPOLE
.,FA0A 20 E2 F8 JSR $F8E2       JSR    STT1
.,FA0D 4C BC FE JMP $FEBC       JMP    PREND           ;RESTORE REGS AND RTI
                                ; RAD2 - LONGLONG HANDLER (COULD BE A LONG ONE)
.,FA10 A5 96    LDA $96         RAD2   LDA SYNO        ;HAVE WE GOTTEN BLOCK SYNC...
.,FA12 F0 04    BEQ $FA18       BEQ    RAD2Y           ;...NO
.,FA14 A5 B4    LDA $B4         LDA    SNSW1           ;CHECK IF WE'VE HAD A REAL BYTE START...
.,FA16 F0 07    BEQ $FA1F       BEQ    RAD2X           ;...NO
.,FA18 A5 A3    LDA $A3         RAD2Y  LDA PCNTR       ;ARE WE AT END OF BYTE...
.,FA1A 30 03    BMI $FA1F       BMI    RAD2X           ;YES...GO ADJUST FOR LONGLONG
.,FA1C 4C 97 F9 JMP $F997       JMP    RADL            ;...NO SO TREAT IT AS A LONG ONE READ
.,FA1F 46 B1    LSR $B1         RAD2X  LSR TEMP        ;ADJUST TIMEOUT FOR...
.,FA21 A9 93    LDA #$93        LDA    #147            ;...LONGLONG PULSE VALUE
.,FA23 38       SEC             SEC
.,FA24 E5 B1    SBC $B1         SBC    TEMP
.,FA26 65 B0    ADC $B0         ADC    CMP0
.,FA28 0A       ASL             ASL    A
.,FA29 AA       TAX             TAX                    ;AND SET TIMEOUT FOR LAST BIT
.,FA2A 20 E2 F8 JSR $F8E2       JSR    STT1
.,FA2D E6 9C    INC $9C         INC    DPSW            ;SET BIT THROW AWAY FLAG
.,FA2F A5 B4    LDA $B4         LDA    SNSW1           ;IF BYTE SYNCRONIZED....
.,FA31 D0 11    BNE $FA44       BNE    RADQ2           ;...THEN SKIP TO PASS CHAR
.,FA33 A5 96    LDA $96         LDA    SYNO            ;THROWS OUT DATA UNTILL BLOCK SYNC...
.,FA35 F0 26    BEQ $FA5D       BEQ    RDBK2           ;...NO BLOCK SYNC
.,FA37 85 A8    STA $A8         STA    RER             ;FLAG DATA AS ERROR
.,FA39 A9 00    LDA #$00        LDA    #0              ;KILL 16 SYNC FLAG
.,FA3B 85 96    STA $96         STA    SYNO
.,FA3D A9 81    LDA #$81        LDA    #$81            ;SET UP FOR TIMER1 INTERRUPTS
.,FA3F 8D 0D DC STA $DC0D       STA    D1ICR
.,FA42 85 B4    STA $B4         STA    SNSW1           ;FLAG THAT WE HAVE BYTE SYNCRONIZED
                                ;
.,FA44 A5 96    LDA $96         RADQ2  LDA SYNO        ;SAVE SYNO STATUS
.,FA46 85 B5    STA $B5         STA    DIFF
.,FA48 F0 09    BEQ $FA53       BEQ    RADK            ;NO BLOCK SYNC, NO BYTE LOOKING
.,FA4A A9 00    LDA #$00        LDA    #0              ;TURN OFF BYTE SYNC SWITCH
.,FA4C 85 B4    STA $B4         STA    SNSW1
.,FA4E A9 01    LDA #$01        LDA    #$01            ;DISABLE TIMER1 INTERRUPTS
.,FA50 8D 0D DC STA $DC0D       STA    D1ICR
.,FA53 A5 BF    LDA $BF         RADK   LDA MYCH        ;PASS CHARACTER TO BYTE ROUTINE
.,FA55 85 BD    STA $BD         STA    OCHAR
.,FA57 A5 A8    LDA $A8         LDA    RER             ;COMBINE ERROR VALUES WITH ZERO COUNT...
.,FA59 05 A9    ORA $A9         ORA    REZ
.,FA5B 85 B6    STA $B6         STA    PRP             ;...AND SAVE IN PRP
.,FA5D 4C BC FE JMP $FEBC       RDBK2  JMP PREND       ;GO BACK AND GET LAST BYTE
.,FA60 20 97 FB JSR $FB97       RADJ   JSR NEWCH       ;FINISH BYTE, CLR FLAGS
.,FA63 85 9C    STA $9C         STA    DPSW            ;CLEAR BIT THROW AWAY FLAG
.,FA65 A2 DA    LDX #$DA        LDX    #218            ;INITILIZE FOR NEXT DIPOLE
.,FA67 20 E2 F8 JSR $F8E2       JSR    STT1
.,FA6A A5 BE    LDA $BE         LDA    FSBLK           ;CHECK FOR LAST VALUE
.,FA6C F0 02    BEQ $FA70       BEQ    RD15
.,FA6E 85 A7    STA $A7         STA    SHCNL
                                ;*************************************************
                                ;* BYTE HANDLER OF CASSETTE READ                 *
                                ;*                                               *
                                ;* THIS PORTION OF IN LINE CODE IS PASSED THE    *
                                ;* BYTE ASSEMBLED FROM READING TAPE IN OCHAR.    *
                                ;* RER IS SET IF THE BYTE READ IS IN ERROR.      *
                                ;* REZ IS SET IF THE INTERRUPT PROGRAM IS READING*
                                ;* ZEROS.  RDFLG TELLS US WHAT WE ARE DOING.     *
                                ;* BIT 7 SAYS TO IGNORE BYTES UNTIL REZ IS SET   *
                                ;* BIT 6 SAYS TO LOAD THE BYTE. OTHERWISE RDFLG  *
                                ;* IS A COUNTDOWN AFTER SYNC.  IF VERCK IS SET   *
                                ;* WE DO A COMPARE INSTEAD OF A STORE AND SET    *
                                ;* STATUS.  FSBLK COUNTS THE TWO BLOCKS. PTR1 IS *
                                ;* INDEX TO ERROR TABLE FOR PASS1.  PTR2 IS INDEX*
                                ;* TO CORRECTION TABLE FOR PASS2.                *
                                ;*************************************************
                                ;
                                SPERR=16
                                CKERR=32
                                SBERR=4
                                LBERR=8
                                ;
.,FA70 A9 0F    LDA #$0F        RD15   LDA #$F
                                ;
.,FA72 24 AA    BIT $AA         BIT    RDFLG           ;TEST FUNCTION MODE
.,FA74 10 17    BPL $FA8D       BPL    RD20            ;NOT WAITING FOR ZEROS
                                ;
.,FA76 A5 B5    LDA $B5         LDA    DIFF            ;ZEROS YET?
.,FA78 D0 0C    BNE $FA86       BNE    RD12            ;YES...WAIT FOR SYNC
.,FA7A A6 BE    LDX $BE         LDX    FSBLK           ;IS PASS OVER?
.,FA7C CA       DEX             DEX                    ;...IF FSBLK ZERO THEN NO ERROR (FIRST GOOD)
.,FA7D D0 0B    BNE $FA8A       BNE    RD10            ;NO...
                                ;
.,FA7F A9 08    LDA #$08        LDA    #LBERR
.,FA81 20 1C FE JSR $FE1C       JSR    UDST            ;YES...LONG BLOCK ERROR
.,FA84 D0 04    BNE $FA8A       BNE    RD10            ;BRANCH ALWAYS
                                ;
.,FA86 A9 00    LDA #$00        RD12   LDA #0
.,FA88 85 AA    STA $AA         STA    RDFLG           ;NEW MODE IS WAIT FOR SYNC
.,FA8A 4C BC FE JMP $FEBC       RD10   JMP PREND       ;EXIT...DONE
                                ;
.,FA8D 70 31    BVS $FAC0       RD20   BVS RD60        ;WE ARE LOADING
.,FA8F D0 18    BNE $FAA9       BNE    RD200           ;WE ARE SYNCING
                                ;
.,FA91 A5 B5    LDA $B5         LDA    DIFF            ;DO WE HAVE BLOCK SYNC...
.,FA93 D0 F5    BNE $FA8A       BNE    RD10            ;...YES, EXIT
.,FA95 A5 B6    LDA $B6         LDA    PRP             ;IF FIRST BYTE HAS ERROR...
.,FA97 D0 F1    BNE $FA8A       BNE    RD10            ;...THEN SKIP (EXIT)
.,FA99 A5 A7    LDA $A7         LDA    SHCNL           ;MOVE FSBLK TO CARRY...
.,FA9B 4A       LSR             LSR    A
.,FA9C A5 BD    LDA $BD         LDA    OCHAR           ; SHOULD BE A HEADER COUNT CHAR
.,FA9E 30 03    BMI $FAA3       BMI    RD22            ;IF NEG THEN FIRSTBLOCK DATA
.,FAA0 90 18    BCC $FABA       BCC    RD40            ;...EXPECTING FIRSTBLOCK DATA...YES
.,FAA2 18       CLC             CLC
.,FAA3 B0 15    BCS $FABA       RD22   BCS RD40        ;EXPECTING SECOND BLOCK?...YES
.,FAA5 29 0F    AND #$0F        AND    #$F             ;MASK OFF HIGH STORE HEADER COUNT...
.,FAA7 85 AA    STA $AA         STA    RDFLG           ;...IN MODE FLAG (HAVE CORRECT BLOCK)
.,FAA9 C6 AA    DEC $AA         RD200  DEC RDFLG       ;WAIT UNTILL WE GET REAL DATA...
.,FAAB D0 DD    BNE $FA8A       BNE    RD10            ;...9876543210 REAL
.,FAAD A9 40    LDA #$40        LDA    #$40            ;NEXT UP IS REAL DATA...
.,FAAF 85 AA    STA $AA         STA    RDFLG           ;...SET DATA MODE
.,FAB1 20 8E FB JSR $FB8E       JSR    RD300           ;GO SETUP ADDRESS POINTERS
.,FAB4 A9 00    LDA #$00        LDA    #0              ;DEBUG CODE##################################################
.,FAB6 85 AB    STA $AB         STA    SHCNH
.,FAB8 F0 D0    BEQ $FA8A       BEQ    RD10            ;JMP TO CONTINUE
.,FABA A9 80    LDA #$80        RD40   LDA #$80        ;WE WANT TO...
.,FABC 85 AA    STA $AA         STA    RDFLG           ;IGNORE BYTES MODE
.,FABE D0 CA    BNE $FA8A       BNE    RD10            ;JMP
.,FAC0 A5 B5    LDA $B5         RD60   LDA DIFF        ;CHECK FOR END OF BLOCK...
.,FAC2 F0 0A    BEQ $FACE       BEQ    RD70            ;...OKAY
                                ;
.,FAC4 A9 04    LDA #$04        LDA    #SBERR          ;SHORT BLOCK ERROR
.,FAC6 20 1C FE JSR $FE1C       JSR    UDST
.,FAC9 A9 00    LDA #$00        LDA    #0              ;FORCE RDFLG FOR AN END
.,FACB 4C 4A FB JMP $FB4A       JMP    RD161
.,FACE 20 D1 FC JSR $FCD1       RD70   JSR CMPSTE      ;CHECK FOR END OF STORAGE AREA
.,FAD1 90 03    BCC $FAD6       BCC    *+5             ;NOT DONE YET
.,FAD3 4C 48 FB JMP $FB48       JMP    RD160
.,FAD6 A6 A7    LDX $A7         LDX    SHCNL           ;CHECK WHICH PASS...
.,FAD8 CA       DEX             DEX
.,FAD9 F0 2D    BEQ $FB08       BEQ    RD58            ;...SECOND PASS
.,FADB A5 93    LDA $93         LDA    VERCK           ;CHECK IF LOAD OR VERIFY...
.,FADD F0 0C    BEQ $FAEB       BEQ    RD80            ;...LOADING
.,FADF A0 00    LDY #$00        LDY    #0              ;...JUST VERIFYING
.,FAE1 A5 BD    LDA $BD         LDA    OCHAR
.,FAE3 D1 AC    CMP ($AC),Y     CMP    (SAL)Y          ;COMPARE WITH DATA IN PET
.,FAE5 F0 04    BEQ $FAEB       BEQ    RD80            ;...GOOD SO CONTINUE
.,FAE7 A9 01    LDA #$01        LDA    #1              ;...BAD SO FLAG...
.,FAE9 85 B6    STA $B6         STA    PRP             ;...AS AN ERROR
                                ; STORE BAD LOCATIONS FOR SECOND PASS RE-TRY
.,FAEB A5 B6    LDA $B6         RD80   LDA PRP         ;CHK FOR ERRORS...
.,FAED F0 4B    BEQ $FB3A       BEQ    RD59            ;...NO ERRORS
.,FAEF A2 3D    LDX #$3D        LDX    #61             ;MAX ALLOWED IS 30
.,FAF1 E4 9E    CPX $9E         CPX    PTR1            ;ARE WE AT MAX?...
.,FAF3 90 3E    BCC $FB33       BCC    RD55            ;...YES, FLAG AS SECOND PASS ERROR
.,FAF5 A6 9E    LDX $9E         LDX    PTR1            ;GET INDEX INTO BAD...
.,FAF7 A5 AD    LDA $AD         LDA    SAH             ;...AND STORE THE BAD LOCATION
.,FAF9 9D 01 01 STA $0101,X     STA    BAD+1,X         ;...IN BAD TABLE
.,FAFC A5 AC    LDA $AC         LDA    SAL
.,FAFE 9D 00 01 STA $0100,X     STA    BAD,X
.,FB01 E8       INX             INX                    ;ADVANCE POINTER TO NEXT
.,FB02 E8       INX             INX
.,FB03 86 9E    STX $9E         STX    PTR1
.,FB05 4C 3A FB JMP $FB3A       JMP    RD59            ;GO STORE CHARACTER
                                ; CHECK BAD TABLE FOR RE-TRY (SECOND PASS)
.,FB08 A6 9F    LDX $9F         RD58   LDX PTR2        ;HAVE WE DONE ALL IN THE TABLE?...
.,FB0A E4 9E    CPX $9E         CPX    PTR1
.,FB0C F0 35    BEQ $FB43       BEQ    RD90            ;...YES
.,FB0E A5 AC    LDA $AC         LDA    SAL             ;SEE IF THIS IS NEXT IN THE TABLE...
.,FB10 DD 00 01 CMP $0100,X     CMP    BAD,X
.,FB13 D0 2E    BNE $FB43       BNE    RD90            ;...NO
.,FB15 A5 AD    LDA $AD         LDA    SAH
.,FB17 DD 01 01 CMP $0101,X     CMP    BAD+1,X
.,FB1A D0 27    BNE $FB43       BNE    RD90            ;...NO
.,FB1C E6 9F    INC $9F         INC    PTR2            ;WE FOUND NEXT ONE, SO ADVANCE POINTER
.,FB1E E6 9F    INC $9F         INC    PTR2
.,FB20 A5 93    LDA $93         LDA    VERCK           ;DOING A LOAD OR VERIFY?...
.,FB22 F0 0B    BEQ $FB2F       BEQ    RD52            ;...LOADING
.,FB24 A5 BD    LDA $BD         LDA    OCHAR           ;...VERIFYING, SO CHECK
.,FB26 A0 00    LDY #$00        LDY    #0
.,FB28 D1 AC    CMP ($AC),Y     CMP    (SAL)Y
.,FB2A F0 17    BEQ $FB43       BEQ    RD90            ;...OKAY
.,FB2C C8       INY             INY                    ;MAKE .Y= 1
.,FB2D 84 B6    STY $B6         STY    PRP             ;FLAG IT AS AN ERROR
.,FB2F A5 B6    LDA $B6         RD52   LDA PRP         ;A SECOND PASS ERROR?...
.,FB31 F0 07    BEQ $FB3A       BEQ    RD59            ;...NO
                                ;SECOND PASS ERR
.,FB33 A9 10    LDA #$10        RD55   LDA #SPERR
.,FB35 20 1C FE JSR $FE1C       JSR    UDST
.,FB38 D0 09    BNE $FB43       BNE    RD90            ;JMP
.,FB3A A5 93    LDA $93         RD59   LDA VERCK       ;LOAD OR VERIFY?...
.,FB3C D0 05    BNE $FB43       BNE    RD90            ;...VERIFY, DON'T STORE
.,FB3E A8       TAY             TAY                    ;MAKE Y ZERO
.,FB3F A5 BD    LDA $BD         LDA    OCHAR
.,FB41 91 AC    STA ($AC),Y     STA    (SAL)Y          ;STORE CHARACTER
.,FB43 20 DB FC JSR $FCDB       RD90   JSR INCSAL      ;INCREMENT ADDR.
.,FB46 D0 43    BNE $FB8B       BNE    RD180           ;BRANCH ALWAYS
.,FB48 A9 80    LDA #$80        RD160  LDA #$80        ;SET MODE SKIP NEXT DATA
.,FB4A 85 AA    STA $AA         RD161  STA RDFLG
                                ;
                                ; MODIFY FOR C64 6526'S
                                ;
.,FB4C 78       SEI             SEI                    ;PROTECT CLEARING OF T1 INFORMATION
.,FB4D A2 01    LDX #$01        LDX    #$01
.,FB4F 8E 0D DC STX $DC0D       STX    D1ICR           ;CLEAR T1 ENABLE...
.,FB52 AE 0D DC LDX $DC0D       LDX    D1ICR           ;CLEAR THE INTERRUPT
.,FB55 A6 BE    LDX $BE         LDX    FSBLK           ;DEC FSBLK FOR NEXT PASS...
.,FB57 CA       DEX             DEX
.,FB58 30 02    BMI $FB5C       BMI    RD167           ;WE ARE DONE...FSBLK=0
.,FB5A 86 BE    STX $BE         STX    FSBLK           ;...ELSE FSBLK=NEXT
.,FB5C C6 A7    DEC $A7         RD167  DEC SHCNL       ;DEC PASS CALC...
.,FB5E F0 08    BEQ $FB68       BEQ    RD175           ;...ALL DONE
.,FB60 A5 9E    LDA $9E         LDA    PTR1            ;CHECK FOR FIRST PASS ERRORS...
.,FB62 D0 27    BNE $FB8B       BNE    RD180           ;...YES SO CONTINUE
.,FB64 85 BE    STA $BE         STA    FSBLK           ;CLEAR FSBLK IF NO ERRORS...
.,FB66 F0 23    BEQ $FB8B       BEQ    RD180           ;JMP TO EXIT
.,FB68 20 93 FC JSR $FC93       RD175  JSR TNIF        ;READ IT ALL...EXIT
.,FB6B 20 8E FB JSR $FB8E       JSR    RD300           ;RESTORE SAL & SAH
.,FB6E A0 00    LDY #$00        LDY    #0              ;SET SHCNH TO ZERO...
.,FB70 84 AB    STY $AB         STY    SHCNH           ;...USED TO CALC PARITY BYTE
                                ;
                                ;COMPUTE PARITY OVER LOAD
                                ;
.,FB72 B1 AC    LDA ($AC),Y     VPRTY  LDA (SAL)Y      ;CALC BLOCK BCC
.,FB74 45 AB    EOR $AB         EOR    SHCNH
.,FB76 85 AB    STA $AB         STA    SHCNH
.,FB78 20 DB FC JSR $FCDB       JSR    INCSAL          ;INCREMENT ADDRESS
.,FB7B 20 D1 FC JSR $FCD1       JSR    CMPSTE          ;TEST AGAINST END
.,FB7E 90 F2    BCC $FB72       BCC    VPRTY           ;NOT DONE YET...
.,FB80 A5 AB    LDA $AB         LDA    SHCNH           ;CHECK FOR BCC CHAR MATCH...
.,FB82 45 BD    EOR $BD         EOR    OCHAR
.,FB84 F0 05    BEQ $FB8B       BEQ    RD180           ;...YES, EXIT
                                ;CHKSUM ERROR
.,FB86 A9 20    LDA #$20        LDA    #CKERR
.,FB88 20 1C FE JSR $FE1C       JSR    UDST
.,FB8B 4C BC FE JMP $FEBC       RD180  JMP PREND
.,FB8E A5 C2    LDA $C2         RD300  LDA STAH        ; RESTORE STARTING ADDRESS...
.,FB90 85 AD    STA $AD         STA    SAH             ;...POINTERS (SAH & SAL)
.,FB92 A5 C1    LDA $C1         LDA    STAL
.,FB94 85 AC    STA $AC         STA    SAL
.,FB96 60       RTS             RTS
.,FB97 A9 08    LDA #$08        NEWCH  LDA #8          ;SET UP FOR 8 BITS+PARITY
.,FB99 85 A3    STA $A3         STA    PCNTR
.,FB9B A9 00    LDA #$00        LDA    #0              ;INITILIZE...
.,FB9D 85 A4    STA $A4         STA    FIRT            ;..DIPOLE COUNTER
.,FB9F 85 A8    STA $A8         STA    RER             ;..ERROR FLAG
.,FBA1 85 9B    STA $9B         STA    PRTY            ;..PARITY BIT
.,FBA3 85 A9    STA $A9         STA    REZ             ;..ZERO COUNT
.,FBA5 60       RTS             RTS                    ;.A=0 ON RETURN
                                .END
                                .LIB   WRITE
                                ; CASSETTE INFO - FSBLK IS BLOCK COUNTER FOR RECORD
                                ;       FSBLK = 2 -FIRST HEADER
                                ;             = 1 -FIRST DATA
                                ;             = 0 -SECOND DATA
                                ;
                                ; WRITE - TOGGLE WRITE BIT ACCORDING TO LSB IN OCHAR
                                ;
.,FBA6 A5 BD    LDA $BD         WRITE  LDA OCHAR       ;SHIFT BIT TO WRITE INTO CARRY
.,FBA8 4A       LSR             LSR    A
.,FBA9 A9 60    LDA #$60        LDA    #96             ;...C CLR WRITE SHORT
.,FBAB 90 02    BCC $FBAF       BCC    WRT1
.,FBAD A9 B0    LDA #$B0        WRTW   LDA #176        ;...C SET WRITE LONG
.,FBAF A2 00    LDX #$00        WRT1   LDX #0          ;SET AND STORE TIME
.,FBB1 8D 06 DC STA $DC06       WRTX   STA D1T2L
.,FBB4 8E 07 DC STX $DC07       STX    D1T2H
.,FBB7 AD 0D DC LDA $DC0D       LDA    D1ICR           ;CLEAR IRQ
.,FBBA A9 19    LDA #$19        LDA    #$19            ;ENABLE TIMER (ONE-SHOT)
.,FBBC 8D 0F DC STA $DC0F       STA    D1CRB
.,FBBF A5 01    LDA $01         LDA    R6510           ;TOGGLE WRITE BIT
.,FBC1 49 08    EOR #$08        EOR    #$08
.,FBC3 85 01    STA $01         STA    R6510
.,FBC5 29 08    AND #$08        AND    #$08            ;LEAVE ONLY WRITE BIT
.,FBC7 60       RTS             RTS
                                ;
.,FBC8 38       SEC             WRTL3  SEC             ;FLAG PRP FOR END OF BLOCK
.,FBC9 66 B6    ROR $B6         ROR    PRP
.,FBCB 30 3C    BMI $FC09       BMI    WRT3            ; JMP
                                ;
                                ; WRTN - CALLED AT THE END OF EACH BYTE
                                ;   TO WRITE A LONG RER    REZ
                                ;              HHHHHHLLLLLLHHHLLL...
                                ;
.,FBCD A5 A8    LDA $A8         WRTN   LDA RER         ;CHECK FOR ONE LONG
.,FBCF D0 12    BNE $FBE3       BNE    WRTN1
.,FBD1 A9 10    LDA #$10        LDA    #16             ;WRITE A LONG BIT
.,FBD3 A2 01    LDX #$01        LDX    #1
.,FBD5 20 B1 FB JSR $FBB1       JSR    WRTX
.,FBD8 D0 2F    BNE $FC09       BNE    WRT3
.,FBDA E6 A8    INC $A8         INC    RER
.,FBDC A5 B6    LDA $B6         LDA    PRP             ;IF END OF BLOCK(BIT SET BY WRTL3)...
.,FBDE 10 29    BPL $FC09       BPL    WRT3            ;...NO END CONTINUE
.,FBE0 4C 57 FC JMP $FC57       JMP    WRNC            ;...END ...FINISH OFF
                                ;
.,FBE3 A5 A9    LDA $A9         WRTN1  LDA REZ         ;CHECK FOR A ONE BIT
.,FBE5 D0 09    BNE $FBF0       BNE    WRTN2
.,FBE7 20 AD FB JSR $FBAD       JSR    WRTW
.,FBEA D0 1D    BNE $FC09       BNE    WRT3
.,FBEC E6 A9    INC $A9         INC    REZ
.,FBEE D0 19    BNE $FC09       BNE    WRT3
                                ;
.,FBF0 20 A6 FB JSR $FBA6       WRTN2  JSR WRITE
.,FBF3 D0 14    BNE $FC09       BNE    WRT3            ;ON BIT LOW EXIT
.,FBF5 A5 A4    LDA $A4         LDA    FIRT            ;CHECK FOR FIRST OF DIPOLE
.,FBF7 49 01    EOR #$01        EOR    #1
.,FBF9 85 A4    STA $A4         STA    FIRT
.,FBFB F0 0F    BEQ $FC0C       BEQ    WRT2            ;DIPOLE DONE
.,FBFD A5 BD    LDA $BD         LDA    OCHAR           ;FLIPS BIT FOR COMPLEMENTARY RIGHT
.,FBFF 49 01    EOR #$01        EOR    #1
.,FC01 85 BD    STA $BD         STA    OCHAR
.,FC03 29 01    AND #$01        AND    #1              ;TOGGLE PARITY
.,FC05 45 9B    EOR $9B         EOR    PRTY
.,FC07 85 9B    STA $9B         STA    PRTY
.,FC09 4C BC FE JMP $FEBC       WRT3   JMP PREND       ;RESTORE REGS AND RTI EXIT
                                ;
.,FC0C 46 BD    LSR $BD         WRT2   LSR OCHAR       ;MOVE TO NEXT BIT
.,FC0E C6 A3    DEC $A3         DEC    PCNTR           ;DEC COUNTER FOR # OF BITS
.,FC10 A5 A3    LDA $A3         LDA    PCNTR           ;CHECK FOR 8 BITS SENT...
.,FC12 F0 3A    BEQ $FC4E       BEQ    WRT4            ;...IF YES MOVE IN PARITY
.,FC14 10 F3    BPL $FC09       BPL    WRT3            ;...ELSE SEND REST
                                ;
.,FC16 20 97 FB JSR $FB97       WRTS   JSR NEWCH       ;CLEAN UP COUNTERS
.,FC19 58       CLI             CLI                    ;ALLOW FOR INTERRUPTS TO NEST
.,FC1A A5 A5    LDA $A5         LDA    CNTDN           ;ARE WE WRITING HEADER COUNTERS?...
.,FC1C F0 12    BEQ $FC30       BEQ    WRT6            ;...NO
                                ; WRITE HEADER COUNTERS (9876543210 TO HELP WITH READ)
.,FC1E A2 00    LDX #$00        LDX    #0              ;CLEAR BCC
.,FC20 86 D7    STX $D7         STX    DATA
.,FC22 C6 A5    DEC $A5         WRTS1  DEC CNTDN
.,FC24 A6 BE    LDX $BE         LDX    FSBLK           ;CHECK FOR FIRST BLOCK HEADER
.,FC26 E0 02    CPX #$02        CPX    #2
.,FC28 D0 02    BNE $FC2C       BNE    WRT61           ;...NO
.,FC2A 09 80    ORA #$80        ORA    #$80            ;...YES MARK FIRST BLOCK HEADER
.,FC2C 85 BD    STA $BD         WRT61  STA OCHAR       ;WRITE CHARACTERS IN HEADER
.,FC2E D0 D9    BNE $FC09       BNE    WRT3
                                ;
.,FC30 20 D1 FC JSR $FCD1       WRT6   JSR CMPSTE      ;COMPARE START:END
.,FC33 90 0A    BCC $FC3F       BCC    WRT7            ;NOT DONE
.,FC35 D0 91    BNE $FBC8       BNE    WRTL3           ;GO MARK END
.,FC37 E6 AD    INC $AD         INC    SAH
.,FC39 A5 D7    LDA $D7         LDA    DATA            ;WRITE OUT BCC
.,FC3B 85 BD    STA $BD         STA    OCHAR
.,FC3D B0 CA    BCS $FC09       BCS    WRT3            ;JMP
                                ;
.,FC3F A0 00    LDY #$00        WRT7   LDY #0          ;GET NEXT CHARACTER
.,FC41 B1 AC    LDA ($AC),Y     LDA    (SAL)Y
.,FC43 85 BD    STA $BD         STA    OCHAR           ;STORE IN OUTPUT CHARACTER
.,FC45 45 D7    EOR $D7         EOR    DATA            ;UPDATE BCC
.,FC47 85 D7    STA $D7         STA    DATA
.,FC49 20 DB FC JSR $FCDB       JSR    INCSAL          ;INCREMENT FETCH ADDRESS
.,FC4C D0 BB    BNE $FC09       BNE    WRT3            ;BRANCH ALWAYS
                                ;
.,FC4E A5 9B    LDA $9B         WRT4   LDA PRTY        ;MOVE PARITY INTO OCHAR...
.,FC50 49 01    EOR #$01        EOR    #1
.,FC52 85 BD    STA $BD         STA    OCHAR           ;...TO BE WRITTEN AS NEXT BIT
.,FC54 4C BC FE JMP $FEBC       WRTBK  JMP PREND       ;RESTORE REGS AND RTI EXIT
                                ;
.,FC57 C6 BE    DEC $BE         WRNC   DEC FSBLK       ;CHECK FOR END
.,FC59 D0 03    BNE $FC5E       BNE    WREND           ;...BLOCK ONLY
.,FC5B 20 CA FC JSR $FCCA       JSR    TNOF            ;...WRITE, SO TURN OFF MOTOR
.,FC5E A9 50    LDA #$50        WREND  LDA #80         ;PUT 80 CASSETTE SYNCS AT END
.,FC60 85 A7    STA $A7         STA    SHCNL
.,FC62 A2 08    LDX #$08        LDX    #8
.,FC64 78       SEI             SEI
.,FC65 20 BD FC JSR $FCBD       JSR    BSIV            ;SET VECTOR TO WRITE ZEROS
.,FC68 D0 EA    BNE $FC54       BNE    WRTBK           ;JMP
                                ;
.,FC6A A9 78    LDA #$78        WRTZ   LDA #120        ;WRITE LEADING ZEROS FOR SYNC
.,FC6C 20 AF FB JSR $FBAF       JSR    WRT1
.,FC6F D0 E3    BNE $FC54       BNE    WRTBK
.,FC71 C6 A7    DEC $A7         DEC    SHCNL           ;CHECK IF DONE WITH LOW SYNC...
.,FC73 D0 DF    BNE $FC54       BNE    WRTBK           ;...NO
.,FC75 20 97 FB JSR $FB97       JSR    NEWCH           ;...YES CLEAR UP COUNTERS
.,FC78 C6 AB    DEC $AB         DEC    SHCNH           ;CHECK IF DONE WITH SYNC...
.,FC7A 10 D8    BPL $FC54       BPL    WRTBK           ;...NO
.,FC7C A2 0A    LDX #$0A        LDX    #10             ;...YES SO SET VECTOR FOR DATA
.,FC7E 20 BD FC JSR $FCBD       JSR    BSIV
.,FC81 58       CLI             CLI
.,FC82 E6 AB    INC $AB         INC    SHCNH           ;ZERO SHCNH
.,FC84 A5 BE    LDA $BE         LDA    FSBLK           ;IF DONE THEN...
.,FC86 F0 30    BEQ $FCB8       BEQ    STKY            ;...GOTO SYSTEM RESTORE
.,FC88 20 8E FB JSR $FB8E       JSR    RD300
.,FC8B A2 09    LDX #$09        LDX    #9              ;SET UP FOR HEADER COUNT
.,FC8D 86 A5    STX $A5         STX    CNTDN
.,FC8F 86 B6    STX $B6         STX    PRP             ;CLEAR ENDOF BLOCK FLAG
.,FC91 D0 83    BNE $FC16       BNE    WRTS            ;JMP
                                ;
.,FC93 08       PHP             TNIF   PHP             ;CLEAN UP INTERRUPTS AND RESTORE PIA'S
.,FC94 78       SEI             SEI
.,FC95 AD 11 D0 LDA $D011       LDA    VICREG+17       ;UNLOCK VIC
.,FC98 09 10    ORA #$10        ORA    #$10            ;ENABLE DISPLAY
.,FC9A 8D 11 D0 STA $D011       STA    VICREG+17
.,FC9D 20 CA FC JSR $FCCA       JSR    TNOF            ;TURN OFF MOTOR
.,FCA0 A9 7F    LDA #$7F        LDA    #$7F            ;CLEAR INTERRUPTS
.,FCA2 8D 0D DC STA $DC0D       STA    D1ICR
.,FCA5 20 DD FD JSR $FDDD       JSR    IOKEYS          ;RESTORE KEYBOARD IRQ FROM TIMMER1
.,FCA8 AD A0 02 LDA $02A0       LDA    IRQTMP+1        ;RESTORE KEYBOARD INTERRUPT VECTOR
.,FCAB F0 09    BEQ $FCB6       BEQ    TNIQ            ;NO IRQ (IRQ VECTOR CANNOT BE Z-PAGE)
.,FCAD 8D 15 03 STA $0315       STA    CINV+1
.,FCB0 AD 9F 02 LDA $029F       LDA    IRQTMP
.,FCB3 8D 14 03 STA $0314       STA    CINV
.,FCB6 28       PLP             TNIQ   PLP
.,FCB7 60       RTS             RTS
                                ;
.,FCB8 20 93 FC JSR $FC93       STKY   JSR TNIF        ;GO RESTORE SYSTEM INTERRUPTS
.,FCBB F0 97    BEQ $FC54       BEQ    WRTBK           ;CAME FOR CASSETTE IRQ SO RTI
                                ;
                                ; BSIV - SUBROUTINE TO CHANGE IRQ VECTORS
                                ;  ENTRYS - .X = 8 WRITE ZEROS TO TAPE
                                ;           .X = 10 WRITE DATA TO TAPE
                                ;           .X = 12 RESTORE TO KEYSCAN
                                ;           .X = 14 READ DATA FROM TAPE
                                ;
.,FCBD BD 93 FD LDA $FD93,X     BSIV   LDA BSIT-8,X    ;MOVE IRQ VECTORS, TABLE TO INDIRECT
.,FCC0 8D 14 03 STA $0314       STA    CINV
.,FCC3 BD 94 FD LDA $FD94,X     LDA    BSIT+1-8,X
.,FCC6 8D 15 03 STA $0315       STA    CINV+1
.,FCC9 60       RTS             RTS
                                ;
.,FCCA A5 01    LDA $01         TNOF   LDA R6510       ;TURN OFF CASSETTE MOTOR
.,FCCC 09 20    ORA #$20        ORA    #$20            ;
.,FCCE 85 01    STA $01         STA    R6510
.,FCD0 60       RTS             RTS
                                ;COMPARE START AND END LOAD/SAVE
                                ;ADDRESSES.  SUBROUTINE CALLED BY
                                ;TAPE READ, SAVE, TAPE WRITE
                                ;
.,FCD1 38       SEC             CMPSTE SEC
.,FCD2 A5 AC    LDA $AC         LDA    SAL
.,FCD4 E5 AE    SBC $AE         SBC    EAL
.,FCD6 A5 AD    LDA $AD         LDA    SAH
.,FCD8 E5 AF    SBC $AF         SBC    EAH
.,FCDA 60       RTS             RTS
                                ;INCREMENT ADDRESS POINTER SAL
                                ;
.,FCDB E6 AC    INC $AC         INCSAL INC SAL
.,FCDD D0 02    BNE $FCE1       BNE    INCR
.,FCDF E6 AD    INC $AD         INC    SAH
.,FCE1 60       RTS             INCR   RTS
                                .END
                                .LIB   INIT
                                ; START - SYSTEM RESET
                                ; WILL GOTO ROM AT $8000...
                                ; IF LOCS $8004-$8008
                                ; = 'CBM80'
                                ;    ^^^  > THESE HAVE MSB SET
                                ; KERNAL EXPECTS...
                                ; $8000- .WORD INITILIZE (HARD START)
                                ; $8002- .WORD PANIC (WARM START)
                                ; ... ELSE BASIC SYSTEM USED
                                ; ******************TESTING ONLY***************
                                ; USE AUTO DISK/CASSETTE LOAD WHEN DEVELOPED...
                                ;
.,FCE2 A2 FF    LDX #$FF        START  LDX #$FF
.,FCE4 78       SEI                    SEI
.,FCE5 9A       TXS                    TXS
.,FCE6 D8       CLD                    CLD
.,FCE7 20 02 FD JSR $FD02              JSR A0INT       ;TEST FOR $A0 ROM IN
.,FCEA D0 03    BNE $FCEF              BNE START1
.,FCEC 6C 00 80 JMP ($8000)            JMP ($8000)     ; GO INIT AS $A000 ROM WANTS
.,FCEF 8E 16 D0 STX $D016       START1 STX VICREG+22   ;SET UP REFRESH (.X=<5)
.,FCF2 20 A3 FD JSR $FDA3              JSR IOINIT      ;GO INITILIZE I/O DEVICES
.,FCF5 20 50 FD JSR $FD50              JSR RAMTAS      ;GO RAM TEST AND SET
.,FCF8 20 15 FD JSR $FD15              JSR RESTOR      ;GO SET UP OS VECTORS
                                ;
.,FCFB 20 5B FF JSR $FF5B              JSR CINT        ;GO INITILIZE SCREEN
.,FCFE 58       CLI                    CLI             ;INTERRUPTS OKAY NOW
.,FCFF 6C 00 A0 JMP ($A000)            JMP ($A000)     ;GO TO BASIC SYSTEM
                                ; A0INT - TEST FOR AN $8000 ROM
                                ;  RETURNS Z - $8000 IN
                                ;
.,FD02 A2 05    LDX #$05        A0INT  LDX #TBLA0E-TBLA0R ;CHECK FOR $8000
.,FD04 BD 0F FD LDA $FD0F,X     A0IN1  LDA TBLA0R-1,X
.,FD07 DD 03 80 CMP $8003,X            CMP $8004-1,X
.,FD0A D0 03    BNE $FD0F              BNE A0IN2
.,FD0C CA       DEX                    DEX
.,FD0D D0 F5    BNE $FD04              BNE A0IN1
.,FD0F 60       RTS             A0IN2  RTS
                                ;
.:FD10 C3 C2 CD 38 30           TBLA0R .BYT $C3,$C2,$CD,'80' ;..CBM80..
                                TBLA0E
                                ; RESTOR - SET KERNAL INDIRECTS AND VECTORS (SYSTEM)
                                ;
.,FD15 A2 30    LDX #$30        RESTOR LDX #<VECTSS
.,FD17 A0 FD    LDY #$FD               LDY #>VECTSS
.,FD19 18       CLC                    CLC
                                ;
                                ; VECTOR - SET KERNAL INDIRECT AND VECTORS (USER)
                                ;
.,FD1A 86 C3    STX $C3         VECTOR STX TMP2
.,FD1C 84 C4    STY $C4                STY TMP2+1
.,FD1E A0 1F    LDY #$1F               LDY #VECTSE-VECTSS-1
.,FD20 B9 14 03 LDA $0314,Y     MOVOS1 LDA CINV,Y      ;GET FROM STORAGE
.,FD23 B0 02    BCS $FD27              BCS MOVOS2      ;C...WANT STORAGE TO USER
.,FD25 B1 C3    LDA ($C3),Y            LDA (TMP2)Y     ;...WANT USER TO STORAGE
.,FD27 91 C3    STA ($C3),Y     MOVOS2 STA (TMP2)Y     ;PUT IN USER
.,FD29 99 14 03 STA $0314,Y            STA CINV,Y      ;PUT IN STORAGE
.,FD2C 88       DEY                    DEY
.,FD2D 10 F1    BPL $FD20              BPL MOVOS1
.,FD2F 60       RTS                    RTS
                                ;
                                VECTSS .WOR KEY,TIMB,NNMI
                                .WOR   NOPEN,NCLOSE,NCHKIN
                                .WOR   NCKOUT,NCLRCH,NBASIN
                                .WOR   NBSOUT,NSTOP,NGETIN
                                .WOR   NCLALL,TIMB     ;GOTO BREAK ON A USRCMD JMP
.:FD30 31 EA 66 FE 47 FE 4A F3  .WOR   NLOAD,NSAVE
                                VECTSE
                                ; RAMTAS - MEMORY SIZE CHECK AND SET
                                ;
.,FD50 A9 00    LDA #$00        RAMTAS LDA #0          ;ZERO LOW MEMORY
.,FD52 A8       TAY                    TAY             ;START AT 0002
.,FD53 99 02 00 STA $0002,Y     RAMTZ0 STA $0002,Y     ;ZERO PAGE
.,FD56 99 00 02 STA $0200,Y            STA $0200,Y     ;USER BUFFERS AND VARS
.,FD59 99 00 03 STA $0300,Y            STA $0300,Y     ;SYSTEM SPACE AND USER SPACE
.,FD5C C8       INY                    INY
.,FD5D D0 F4    BNE $FD53              BNE RAMTZ0
                                ;
                                ;ALLOCATE TAPE BUFFERS
                                ;
.,FD5F A2 3C    LDX #$3C               LDX #<TBUFFR
.,FD61 A0 03    LDY #$03               LDY #>TBUFFR
.,FD63 86 B2    STX $B2                STX TAPE1
.,FD65 84 B3    STY $B3                STY TAPE1+1
                                ;
                                ; SET TOP OF MEMORY
                                ;
                                RAMTBT
.,FD67 A8       TAY                    TAY             ;MOVE $00 TO .Y
.,FD68 A9 03    LDA #$03               LDA #3          ;SET HIGH INITAL INDEX
.,FD6A 85 C2    STA $C2                STA TMP0+1
                                ;
.,FD6C E6 C2    INC $C2         RAMTZ1 INC TMP0+1      ;MOVE INDEX THRU MEMORY
.,FD6E B1 C1    LDA ($C1),Y     RAMTZ2 LDA (TMP0)Y     ;GET PRESENT DATA
.,FD70 AA       TAX                    TAX             ;SAVE IN .X
.,FD71 A9 55    LDA #$55               LDA #$55        ;DO A $55,$AA TEST
.,FD73 91 C1    STA ($C1),Y            STA (TMP0)Y
.,FD75 D1 C1    CMP ($C1),Y            CMP (TMP0)Y
.,FD77 D0 0F    BNE $FD88              BNE SIZE
.,FD79 2A       ROL                    ROL A
.,FD7A 91 C1    STA ($C1),Y            STA (TMP0)Y
.,FD7C D1 C1    CMP ($C1),Y            CMP (TMP0)Y
.,FD7E D0 08    BNE $FD88              BNE SIZE
.,FD80 8A       TXA                    TXA             ;RESTORE OLD DATA
.,FD81 91 C1    STA ($C1),Y            STA (TMP0)Y
.,FD83 C8       INY                    INY
.,FD84 D0 E8    BNE $FD6E              BNE RAMTZ2
.,FD86 F0 E4    BEQ $FD6C              BEQ RAMTZ1
                                ;
.,FD88 98       TYA             SIZE   TYA             ;SET TOP OF MEMORY
.,FD89 AA       TAX                    TAX
.,FD8A A4 C2    LDY $C2                LDY TMP0+1
.,FD8C 18       CLC                    CLC
.,FD8D 20 2D FE JSR $FE2D              JSR SETTOP
.,FD90 A9 08    LDA #$08               LDA #$08        ;SET BOTTOM OF MEMORY
.,FD92 8D 82 02 STA $0282              STA MEMSTR+1    ;ALWAYS AT $0800
.,FD95 A9 04    LDA #$04               LDA #$04        ;SCREEN ALWAYS AT $400
.,FD97 8D 88 02 STA $0288              STA HIBASE      ;SET BASE OF SCREEN
.,FD9A 60       RTS                    RTS
.:FD9B 6A FC CD FB 31 EA 2C F9  BSIT   .WOR WRTZ,WRTN,KEY,READ ;TABLE OF INDIRECTS FOR CASSETTE IRQ'S
                                ; IOINIT - INITILIZE IO DEVICES
                                ;
.,FDA3 A9 7F    LDA #$7F        IOINIT LDA #$7F        ;KILL INTERRUPTS
.,FDA5 8D 0D DC STA $DC0D              STA D1ICR
.,FDA8 8D 0D DD STA $DD0D              STA D2ICR
.,FDAB 8D 00 DC STA $DC00              STA D1PRA       ;TURN ON STOP KEY
.,FDAE A9 08    LDA #$08               LDA #%00001000  ;SHUT OFF TIMERS
.,FDB0 8D 0E DC STA $DC0E              STA D1CRA
.,FDB3 8D 0E DD STA $DD0E              STA D2CRA
.,FDB6 8D 0F DC STA $DC0F              STA D1CRB
.,FDB9 8D 0F DD STA $DD0F              STA D2CRB
                                ; CONFIGURE PORTS
.,FDBC A2 00    LDX #$00               LDX #$00        ;SET UP KEYBOARD INPUTS
.,FDBE 8E 03 DC STX $DC03              STX D1DDRB      ;KEYBOARD INPUTS
.,FDC1 8E 03 DD STX $DD03              STX D2DDRB      ;USER PORT (NO RS-232)
.,FDC4 8E 18 D4 STX $D418              STX SIDREG+24   ;TURN OFF SID
.,FDC7 CA       DEX                    DEX
.,FDC8 8E 02 DC STX $DC02              STX D1DDRA      ;KEYBOARD OUTPUTS
.,FDCB A9 07    LDA #$07               LDA #%00000111  ;SET SERIAL/VA14/15 (CLKHI)
.,FDCD 8D 00 DD STA $DD00              STA D2PRA
.,FDD0 A9 3F    LDA #$3F               LDA #%00111111  ;SET SERIAL IN/OUT, VA14/15OUT
.,FDD2 8D 02 DD STA $DD02              STA D2DDRA
                                                       ;
                                                       ; SET UP THE 6510 LINES
                                                       ;
.,FDD5 A9 E7    LDA #$E7               LDA #%11100111  ;MOTOR ON, HIRAM LOWRAM CHAREN HIGH
.,FDD7 85 01    STA $01                STA R6510
.,FDD9 A9 2F    LDA #$2F               LDA #%00101111  ;MTR OUT,SW IN,WR OUT,CONTROL OUT
.,FDDB 85 00    STA $00                STA D6510
.,FDDD AD A6 02 LDA $02A6       IOKEYS LDA PALNTS      ;PAL OR NTSC
.,FDE0 F0 0A    BEQ $FDEC              BEQ I0010       ;NTSC
.,FDE2 A9 25    LDA #$25               LDA #<SIXTYP
.,FDE4 8D 04 DC STA $DC04              STA D1T1L
.,FDE7 A9 40    LDA #$40               LDA #>SIXTYP
.,FDE9 4C F3 FD JMP $FDF3              JMP I0020
.,FDEC A9 95    LDA #$95        I0010  LDA #<SIXTY     ;KEYBOARD SCAN IRQ'S
.,FDEE 8D 04 DC STA $DC04              STA D1T1L
.,FDF1 A9 42    LDA #$42               LDA #>SIXTY
.,FDF3 8D 05 DC STA $DC05       I0020  STA D1T1H
.,FDF6 4C 6E FF JMP $FF6E              JMP PIOKEY
                                ; LDA #$81 ;ENABLE T1 IRQ'S
                                ; STA D1ICR
                                ; LDA D1CRA
                                ; AND #$80 ;SAVE ONLY TOD BIT
                                ; ORA #%00010001 ;ENABLE TIMER1
                                ; STA D1CRA
                                ; JMP CLKLO ;RELEASE THE CLOCK LINE
                                ;
                                ; SIXTY HERTZ VALUE
                                ;
                                SIXTY  = 16667
.,FDF9 85 B7    STA $B7         SETNAM STA FNLEN
.,FDFB 86 BB    STX $BB         STX    FNADR
.,FDFD 84 BC    STY $BC         STY    FNADR+1
.,FDFF 60       RTS             RTS
.,FE00 85 B8    STA $B8         SETLFS STA LA
.,FE02 86 BA    STX $BA         STX    FA
.,FE04 84 B9    STY $B9         STY    SA
.,FE06 60       RTS             RTS
.,FE07 A5 BA    LDA $BA         READSS LDA FA          ;SEE WHICH DEVICES' TO READ
.,FE09 C9 02    CMP #$02               CMP #2          ;IS IT RS-232?
.,FE0B D0 0D    BNE $FE1A              BNE READST      ;NO...READ SERIAL/CASS
.,FE0D AD 97 02 LDA $0297              LDA RSSTAT      ;YES...GET RS-232 UP
.,FE10 48       PHA                    PHA
.,FE11 A9 00    LDA #$00               LDA #00         ;CLEAR RS232 STATUS WHEN READ
.,FE13 8D 97 02 STA $0297              STA RSSTAT
.,FE16 68       PLA                    PLA
.,FE17 60       RTS                    RTS
.,FE18 85 9D    STA $9D         SETMSG STA MSGFLG
.,FE1A A5 90    LDA $90         READST LDA STATUS
.,FE1C 05 90    ORA $90         UDST   ORA STATUS
.,FE1E 85 90    STA $90         STA    STATUS
.,FE20 60       RTS             RTS
.,FE21 8D 85 02 STA $0285       SETTMO STA TIMOUT
.,FE24 60       RTS             RTS
.,FE25 90 06    BCC $FE2D       MEMTOP BCC SETTOP
                                ;
                                ;CARRY SET--READ TOP OF MEMORY
                                ;
.,FE27 AE 83 02 LDX $0283       GETTOP LDX MEMSIZ
.,FE2A AC 84 02 LDY $0284       LDY    MEMSIZ+1
                                ;
                                ;CARRY CLEAR--SET TOP OF MEMORY
                                ;
.,FE2D 8E 83 02 STX $0283       SETTOP STX MEMSIZ
.,FE30 8C 84 02 STY $0284       STY    MEMSIZ+1
.,FE33 60       RTS             RTS
                                ;MANAGE BOTTOM OF MEMORY
                                ;
.,FE34 90 06    BCC $FE3C       MEMBOT BCC SETBOT
                                ;
                                ;CARRY SET--READ BOTTOM OF MEMORY
                                ;
.,FE36 AE 81 02 LDX $0281       LDX    MEMSTR
.,FE39 AC 82 02 LDY $0282       LDY    MEMSTR+1
                                ;
                                ;CARRY CLEAR--SET BOTTOM OF MEMORY
                                ;
.,FE3C 8E 81 02 STX $0281       SETBOT STX MEMSTR
.,FE3F 8C 82 02 STY $0282       STY    MEMSTR+1
.,FE42 60       RTS             RTS
                                .END
                                .LIB   RS232NMI
.,FE43 78       SEI             NMI    SEI             ;NO IRQ'S ALLOWED...
.,FE44 6C 18 03 JMP ($0318)            JMP (NMINV)     ;...COULD MESS UP CASSETTES
.,FE47 48       PHA             NNMI   PHA
.,FE48 8A       TXA                    TXA
.,FE49 48       PHA                    PHA
.,FE4A 98       TYA                    TYA
.,FE4B 48       PHA                    PHA
.,FE4C A9 7F    LDA #$7F        NNMI10 LDA #$7F        ;DISABLE ALL NMI'S
.,FE4E 8D 0D DD STA $DD0D              STA D2ICR
.,FE51 AC 0D DD LDY $DD0D              LDY D2ICR       ;CHECK IF REAL NMI...
.,FE54 30 1C    BMI $FE72              BMI NNMI20      ;NO...RS232/OTHER
                                ;
.,FE56 20 02 FD JSR $FD02       NNMI18 JSR A0INT       ;CHECK IF $A0 IN...NO .Y
.,FE59 D0 03    BNE $FE5E              BNE NNMI19      ;...NO
.,FE5B 6C 02 80 JMP ($8002)            JMP ($8002)     ;...YES
                                ;
                                ; CHECK FOR STOP KEY DOWN
                                ;
                                NNMI19
.,FE5E 20 BC F6 JSR $F6BC              JSR UD60        ;NO .Y
.,FE61 20 E1 FF JSR $FFE1              JSR STOP        ;NO .Y
.,FE64 D0 0C    BNE $FE72              BNE NNMI20      ;NO STOP KEY...TEST FOR RS232
                                ;
                                ; TIMB - WHERE SYSTEM GOES ON A BRK INSTRUCTION
                                ;
.,FE66 20 15 FD JSR $FD15       TIMB   JSR RESTOR      ;RESTORE SYSTEM INDIRECTS
.,FE69 20 A3 FD JSR $FDA3              JSR IOINIT      ;RESTORE I/O FOR BASIC
.,FE6C 20 18 E5 JSR $E518              JSR CINT        ;RESTORE SCREEN FOR BASIC
.,FE6F 6C 02 A0 JMP ($A002)            JMP ($A002)     ;...NO, SO BASIC WARM START
                                ; DISABLE NMI'S UNTILL READY
                                ;  SAVE ON STACK
                                ;
.,FE72 98       TYA             NNMI20 TYA             ;.Y SAVED THROUGH RESTORE
.,FE73 2D A1 02 AND $02A1              AND ENABL       ;SHOW ONLY ENABLES
.,FE76 AA       TAX                    TAX             ;SAVE IN .X FOR LATTER
                                ;
                                ; T1 NMI CHECK - TRANSMITT A BIT
                                ;
.,FE77 29 01    AND #$01               AND #$01        ;CHECK FOR T1
.,FE79 F0 28    BEQ $FEA3              BEQ NNMI30      ;NO...
                                ;
.,FE7B AD 00 DD LDA $DD00              LDA D2PRA
.,FE7E 29 FB    AND #$FB               AND #$FF-$04    ;FIX FOR CURRENT I/O
.,FE80 05 B5    ORA $B5                ORA NXTBIT      ;LOAD DATA AND...
.,FE82 8D 00 DD STA $DD00              STA D2PRA       ;...SEND IT
                                ;
.,FE85 AD A1 02 LDA $02A1              LDA ENABL       ;RESTORE NMI'S
.,FE88 8D 0D DD STA $DD0D              STA D2ICR       ;READY FOR NEXT...
                                ;
                                ; BECAUSE OF 6526 ICR STRUCTURE...
                                ;  HANDLE ANOTHER NMI AS A SUBROUTINE
                                ;
.,FE8B 8A       TXA                    TXA             ;TEST FOR ANOTHER NMI
.,FE8C 29 12    AND #$12               AND #$12        ;TEST FOR T2 OR FLAG
.,FE8E F0 0D    BEQ $FE9D              BEQ NNMI25
.,FE90 29 02    AND #$02               AND #$02        ;CHECK FOR T2
.,FE92 F0 06    BEQ $FE9A              BEQ NNMI22      ;MUST BE A FLAG
                                ;
.,FE94 20 D6 FE JSR $FED6              JSR T2NMI       ;HANDLE A NORMAL BIT IN...
.,FE97 4C 9D FE JMP $FE9D              JMP NNMI25      ;...THEN CONTINUE OUTPUT
                                ;
.,FE9A 20 07 FF JSR $FF07       NNMI22 JSR FLNMI       ;HANDLE A START BIT...
                                ;
.,FE9D 20 BB EE JSR $EEBB       NNMI25 JSR RSTRAB      ;GO CALC INFO (CODE COULD BE IN LINE)
.,FEA0 4C B6 FE JMP $FEB6              JMP NMIRTI
                                ;
                                ; T2 NMI CHECK - RECIEVE A BIT
                                ;
.,FEA3 8A       TXA             NNMI30 TXA
.,FEA4 29 02    AND #$02               AND #$02        ;MASK TO T2
.,FEA6 F0 06    BEQ $FEAE              BEQ NNMI40      ;NO...
                                ;
.,FEA8 20 D6 FE JSR $FED6              JSR T2NMI       ;HANDLE INTERRUPT
.,FEAB 4C B6 FE JMP $FEB6              JMP NMIRTI
                                ; FLAG NMI HANDLER - RECIEVE A START BIT
                                ;
.,FEAE 8A       TXA             NNMI40 TXA             ;CHECK FOR EDGE
.,FEAF 29 10    AND #$10               AND #$10        ;ON FLAG...
.,FEB1 F0 03    BEQ $FEB6              BEQ NMIRTI      ;NO...
                                ;
.,FEB3 20 07 FF JSR $FF07              JSR FLNMI       ;START BIT ROUTINE
.,FEB6 AD A1 02 LDA $02A1       NMIRTI LDA ENABL       ;RESTORE NMI'S
.,FEB9 8D 0D DD STA $DD0D              STA D2ICR
.,FEBC 68       PLA             PREND  PLA             ;BECAUSE OF MISSING SCREEN EDITOR
.,FEBD A8       TAY                    TAY
.,FEBE 68       PLA                    PLA
.,FEBF AA       TAX                    TAX
.,FEC0 68       PLA                    PLA
.,FEC1 40       RTI                    RTI
                                ; BAUDO TABLE CONTAINS VALUES
                                ;  FOR 1E6/BAUD RATE/2
                                ;
.:FEC2 C1 27                    BAUDO  .WOR 10000-CBIT ; 50 BAUD
.:FEC4 3E 1A                           .WOR 6667-CBIT  ;   75   BAUD
.:FEC6 C5 11                           .WOR 4545-CBIT  ;  110   BAUD
.:FEC8 74 0E                           .WOR 3715-CBIT  ;  134.6 BAUD
.:FECA ED 0C                           .WOR 3333-CBIT  ;  150   BAUD
.:FECC 45 06                           .WOR 1667-CBIT  ;  300   BAUD
.:FECE F0 02                           .WOR 833-CBIT   ;  600   BAUD
.:FED0 46 01                           .WOR 417-CBIT   ; 1200   BAUD
.:FED2 B8 00                           .WOR 278-CBIT   ; 1800   BAUD
.:FED4 71 00                           .WOR 208-CBIT   ; 2400   BAUD
                                ;
                                ; CBIT - AN ADJUSTMENT TO MAKE NEXT T2 HIT NEAR CENTER
                                ;   OF THE NEXT BIT.
                                ;   APROX THE TIME TO SERVICE A CB1 NMI
                                CBIT   =100            ;CYCLES
                                ; T2NMI - SUBROUTINE TO HANDLE AN RS232
                                ;  BIT INPUT.
                                ;
.,FED6 AD 01 DD LDA $DD01       T2NMI  LDA D2PRB       ;GET DATA IN
.,FED9 29 01    AND #$01               AND #01         ;MASK OFF...
.,FEDB 85 A7    STA $A7                STA INBIT       ;...SAVE FOR LATTER
                                ;
                                ; UPDATE T2 FOR MID BIT CHECK
                                ;   (WORST CASE <213 CYCLES TO HERE)
                                ;   (CALC 125 CYCLES+43-66 DEAD)
                                ;
.,FEDD AD 06 DD LDA $DD06              LDA D2T2L       ;CALC NEW TIME & CLR NMI
.,FEE0 E9 1C    SBC #$1C               SBC #22+6
.,FEE2 6D 99 02 ADC $0299              ADC BAUDOF
.,FEE5 8D 06 DD STA $DD06              STA D2T2L
.,FEE8 AD 07 DD LDA $DD07              LDA D2T2H
.,FEEB 6D 9A 02 ADC $029A              ADC BAUDOF+1
.,FEEE 8D 07 DD STA $DD07              STA D2T2H
                                ;
.,FEF1 A9 11    LDA #$11               LDA #$11        ;ENABLE TIMER
.,FEF3 8D 0F DD STA $DD0F              STA D2CRB
                                ;
.,FEF6 AD A1 02 LDA $02A1              LDA ENABL       ;RESTORE NMI'S EARLY...
.,FEF9 8D 0D DD STA $DD0D              STA D2ICR
                                ;
.,FEFC A9 FF    LDA #$FF               LDA #$FF        ;ENABLE COUNT FROM $FFFF
.,FEFE 8D 06 DD STA $DD06              STA D2T2L
.,FF01 8D 07 DD STA $DD07              STA D2T2H
                                ;
.,FF04 4C 59 EF JMP $EF59              JMP RSRCVR      ;GO SHIFT IN...
                                FLNMI
                                ;
                                ; GET HALF BIT RATE VALUE
                                ;
.,FF07 AD 95 02 LDA $0295              LDA M51AJB
.,FF0A 8D 06 DD STA $DD06              STA D2T2L
.,FF0D AD 96 02 LDA $0296              LDA M51AJB+1
.,FF10 8D 07 DD STA $DD07              STA D2T2H
                                ;
.,FF13 A9 11    LDA #$11               LDA #$11        ;ENABLE TIMER
.,FF15 8D 0F DD STA $DD0F              STA D2CRB
                                ;
.,FF18 A9 12    LDA #$12               LDA #$12        ;DISABLE FLAG, ENABLE T2
.,FF1A 4D A1 02 EOR $02A1              EOR ENABL
.,FF1D 8D A1 02 STA $02A1              STA ENABL
                                ;ORA #$82
                                ;STA D2ICR
                                ;
.,FF20 A9 FF    LDA #$FF               LDA #$FF        ;PRESET FOR COUNT DOWN
.,FF22 8D 06 DD STA $DD06              STA D2T2L
.,FF25 8D 07 DD STA $DD07              STA D2T2H
                                ;
.,FF28 AE 98 02 LDX $0298              LDX BITNUM      ;GET #OF BITS IN
.,FF2B 86 A8    STX $A8                STX BITCI       ;PUT IN RCVRCNT
.,FF2D 60       RTS                    RTS
                                ;
                                ; POPEN - PATCHES OPEN RS232 FOR UNIVERSAL KERNAL
                                ;
.,FF2E AA       TAX             POPEN  TAX             ;WE'RE CALCULATING BAUD RATE
.,FF2F AD 96 02 LDA $0296              LDA M51AJB+1    ; M51AJB=FREQ/BAUD/2-100
.,FF32 2A       ROL                    ROL A
.,FF33 A8       TAY                    TAY
.,FF34 8A       TXA                    TXA
.,FF35 69 C8    ADC #$C8               ADC #CBIT+CBIT
.,FF37 8D 99 02 STA $0299              STA BAUDOF
.,FF3A 98       TYA                    TYA
.,FF3B 69 00    ADC #$00               ADC #0
.,FF3D 8D 9A 02 STA $029A              STA BAUDOF+1
.,FF40 60       RTS                    RTS
.,FF41 EA       NOP                    NOP
.,FF42 EA       NOP                    NOP
                                .END
                                .LIB   IRQFILE
                                ; SIMIRQ - SIMULATE AN IRQ (FOR CASSETTE READ)
                                ;  ENTER BY A JSR SIMIRQ
                                ;
.,FF43 08       PHP             SIMIRQ PHP
.,FF44 68       PLA                    PLA             ;FIX THE BREAK FLAG
.,FF45 29 EF    AND #$EF               AND #$EF
.,FF47 48       PHA                    PHA
                                ; PULS - CHECKS FOR REAL IRQ'S OR BREAKS
                                ;
.,FF48 48       PHA             PULS   PHA
.,FF49 8A       TXA                    TXA
.,FF4A 48       PHA                    PHA
.,FF4B 98       TYA                    TYA
.,FF4C 48       PHA                    PHA
.,FF4D BA       TSX                    TSX
.,FF4E BD 04 01 LDA $0104,X            LDA $104,X      ;GET OLD P STATUS
.,FF51 29 10    AND #$10               AND #$10        ;BREAK FLAG?
.,FF53 F0 03    BEQ $FF58              BEQ PULS1       ;...NO
.,FF55 6C 16 03 JMP ($0316)            JMP (CBINV)     ;...YES...BREAK INSTR
.,FF58 6C 14 03 JMP ($0314)     PULS1  JMP (CINV)      ;...IRQ
                                .END
                                .LIB   VECTORS
.,FF5B 20 18 E5 JSR $E518       *=$FF8A-9
.,FF81 4C 5B FF JMP $FF5B       JMP    CINT
.,FF84 4C A3 FD JMP $FDA3       JMP    IOINIT
.,FF87 4C 50 FD JMP $FD50       JMP    RAMTAS
                                *=$FF8A                ;NEW VECTORS FOR BASIC
.,FF8A 4C 15 FD JMP $FD15       JMP    RESTOR          ;RESTORE VECTORS TO INITIAL SYSTEM
.,FF8D 4C 1A FD JMP $FD1A       JMP    VECTOR          ;CHANGE VECTORS FOR USER
                                *      =$FF90
.,FF90 4C 18 FE JMP $FE18       JMP    SETMSG          ;CONTROL O.S. MESSAGES
.,FF93 4C B9 ED JMP $EDB9       JMP    SECND           ;SEND SA AFTER LISTEN
.,FF96 4C C7 ED JMP $EDC7       JMP    TKSA            ;SEND SA AFTER TALK
.,FF99 4C 25 FE JMP $FE25       JMP    MEMTOP          ;SET/READ TOP OF MEMORY
.,FF9C 4C 34 FE JMP $FE34       JMP    MEMBOT          ;SET/READ BOTTOM OF MEMORY
.,FF9F 4C 87 EA JMP $EA87       JMP    SCNKEY          ;SCAN KEYBOARD
.,FFA2 4C 21 FE JMP $FE21       JMP    SETTMO          ;SET TIMEOUT IN IEEE
.,FFA5 4C 13 EE JMP $EE13       JMP    ACPTR           ;HANDSHAKE IEEE BYTE IN
.,FFA8 4C DD ED JMP $EDDD       JMP    CIOUT           ;HANDSHAKE IEEE BYTE OUT
.,FFAB 4C EF ED JMP $EDEF       JMP    UNTLK           ;SEND UNTALK OUT IEEE
.,FFAE 4C FE ED JMP $EDFE       JMP    UNLSN           ;SEND UNLISTEN OUT IEEE
.,FFB1 4C 0C ED JMP $ED0C       JMP    LISTN           ;SEND LISTEN OUT IEEE
.,FFB4 4C 09 ED JMP $ED09       JMP    TALK            ;SEND TALK OUT IEEE
.,FFB7 4C 07 FE JMP $FE07       JMP    READSS          ;RETURN I/O STATUS BYTE
.,FFBA 4C 00 FE JMP $FE00       JMP    SETLFS          ;SET LA, FA, SA
.,FFBD 4C F9 FD JMP $FDF9       JMP    SETNAM          ;SET LENGTH AND FN ADR
.,FFC0 6C 1A 03 JMP ($031A)     OPEN   JMP (IOPEN)     ;OPEN LOGICAL FILE
.,FFC3 6C 1C 03 JMP ($031C)     CLOSE  JMP (ICLOSE)    ;CLOSE LOGICAL FILE
.,FFC6 6C 1E 03 JMP ($031E)     CHKIN  JMP (ICHKIN)    ;OPEN CHANNEL IN
.,FFC9 6C 20 03 JMP ($0320)     CKOUT  JMP (ICKOUT)    ;OPEN CHANNEL OUT
.,FFCC 6C 22 03 JMP ($0322)     CLRCH  JMP (ICLRCH)    ;CLOSE I/O CHANNEL
.,FFCF 6C 24 03 JMP ($0324)     BASIN  JMP (IBASIN)    ;INPUT FROM CHANNEL
.,FFD2 6C 26 03 JMP ($0326)     BSOUT  JMP (IBSOUT)    ;OUTPUT TO CHANNEL
.,FFD5 4C 9E F4 JMP $F49E       JMP    LOADSP          ;LOAD FROM FILE
.,FFD8 4C DD F5 JMP $F5DD       JMP    SAVESP          ;SAVE TO FILE
.,FFDB 4C E4 F6 JMP $F6E4       JMP    SETTIM          ;SET INTERNAL CLOCK
.,FFDE 4C DD F6 JMP $F6DD       JMP    RDTIM           ;READ INTERNAL CLOCK
.,FFE1 6C 28 03 JMP ($0328)     STOP   JMP (ISTOP)     ;SCAN STOP KEY
.,FFE4 6C 2A 03 JMP ($032A)     GETIN  JMP (IGETIN)    ;GET CHAR FROM Q
.,FFE7 6C 2C 03 JMP ($032C)     CLALL  JMP (ICLALL)    ;CLOSE ALL FILES
.,FFEA 4C 9B F6 JMP $F69B       JMP    UDTIM           ;INCREMENT CLOCK
.,FFED 4C 05 E5 JMP $E505       JSCROG JMP SCRORG      ;SCREEN ORG
.,FFF0 4C 0A E5 JMP $E50A       JPLOT  JMP PLOT        ;READ/SET X,Y COORD
.,FFF3 4C 00 E5 JMP $E500       JIOBAS JMP IOBASE      ;RETURN I/O BASE
.:FFF6 52 52 42 59              *=$FFFA
.:FFFA 43 FE                    .WOR   NMI             ;PROGRAM DEFINEABLE
.:FFFC E2 FC                    .WOR   START           ;INITIALIZATION CODE
.:FFFE 48 FF                    .WOR   PULS            ;INTERRUPT HANDLER
