- Fully Commented Commodore 64 BASIC ROM Disassembly (English, "MS")
-
- The comments have been taken from
-    Microsoft's original BASIC for M6502 source
-    http://www.pagetable.com/?p=774
-
- The comments here are basically a complete copy of Microsoft's BASIC
- for 6502 source code, lined up with the version in the C64 ROM.
- This way, even all variable names are intact. The C64 ROM contains
- several fixes and extensions, so the comments do not always line
- up perfectly, so make sure the machine code matches the assembly
- code in the respective lines your looking at.
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
# * 32 leading spaces and "SUBTTL" indicate a heading.
# * Otherwise, 32 leading spaces indicate an overflow comment.
# The encoding is UTF-8.

                                TITLE   BASIC M6502 8K VER 1.1 BY MICRO-SOFT
                                SEARCH  M6502
                                SALL
                                RADIX 10                        ;THROUGHOUT ALL BUT MATH-PAK.
                                
                                $Z::                            ;STARTING POINT FOR M6502 SIMULATOR
                                        ORG     0               ;START OFF AT LOCATION ZERO.
                                SUBTTL  SWITCHES,MACROS.
                                
                                REALIO=4                        ;5=STM
                                                                ;4=APPLE.
                                                                ;3=COMMODORE.
                                                                ;2=OSI
                                                                ;1=MOS TECH,KIM
                                                                ;0=PDP-10 SIMULATING 6502
                                INTPRC==1                       ;INTEGER ARRAYS.
                                ADDPRC==1                       ;FOR ADDITIONAL PRECISION.
                                LNGERR==0                       ;LONG ERROR MESSAGES.
                                TIME==  0                       ;CAPABILITY TO SET AND READ A CLK.
                                EXTIO== 0                       ;EXTERNAL I/O.
                                DISKO== 0                       ;SAVE AND LOAD COMMANDS
                                NULCMD==1                       ;FOR THE "NULL" COMMAND
                                GETCMD==1
                                RORSW==1
                                ROMSW==1                        ;TELLS IF THIS IS ON ROM.
                                CLMWID==14
                                LONGI==1                        ;LONG INITIALIZATION SWITCH.
                                STKEND=511
                                BUFPAG==0
                                LINLEN==72                      ;TERMINAL LINE LENGTH.
                                BUFLEN==72                      ;INPUT BUFFER SIZE.
                                ROMLOC= ^O20000                 ;ADDRESS OF START OF PURE SEGMENT.
                                KIMROM=1
                                IFE     ROMSW,<KIMROM==0>
                                IFN     REALIO-1,<KIMROM==0>
                                IFN     ROMSW,<
                                RAMLOC= ^O40000                 ;USED ONLY IF ROMSW=1
                                IFE     REALIO,<ROMLOC= ^O20000 ;START AT 8K.
                                        RAMLOC=^O1400>>
                                IFE     REALIO-3,<
                                        DISKO==1
                                        RAMLOC==^O2000
                                        ROMLOC=^O140000
                                        NULCMD==0
                                        GETCMD==1
                                        linlen==40
                                        BUFLEN==81
                                        CQOPEN=^O177700
                                        CQCLOS=^O177703
                                        CQOIN= ^O177706         ;OPEN CHANNEL FOR INPUT
                                        CQOOUT=^O177711         ;FILL FOR COMMO.
                                        CQCCHN=^O177714
                                        CQINCH=^O177717         ;INCHR'S CALL TO GET A CHARACTER
                                        OUTCH= ^O177722
                                        CQLOAD=^O177725
                                        CQSAVE=^O177730
                                        CQVERF=^O177733
                                        CQSYS= ^O177736
                                        ISCNTC=^O177741
                                        CZGETL=^O177744         ;CALL POINT FOR "GET"
                                        CQCALL=^O177747         ;CLOSE ALL CHANNELS
                                        CQTIMR=^O215
                                        BUFPAG==2
                                        BUF==256*BUFPAG
                                        STKEND==507
                                        CQSTAT=^O226
                                        CQHTIM=^O164104
                                        EXTIO==1
                                        TIME==1
                                        GETCMD==1
                                        CLMWID==10
                                        PI=255                          ;VALUE OF PI CHARACTER FOR COMMODORE.
                                        ROMSW==1
                                        RORSW==1
                                        TRMPOS=^O306>
                                IFE     REALIO-1,<GETCMD==1
                                        DISKO==1
                                        OUTCH=^O17240                   ;1EA0
                                        ROMLOC==^O20000
                                        RORSW==0
                                        CZGETL=^O17132>
                                IFE     REALIO-2,<
                                        RORSW==0
                                        RAMLOC==^O1000
                                IFN     ROMSW,<
                                        RORSW==0
                                        RAMLOC==^O100000>
                                        OUTCH==^O177013>
                                IFE     REALIO-4,<
                                        RORSW==1
                                        NULCMD==0
                                        GETCMD==1
                                        CQINLN==^O176547
                                        CQPRMP==^O63
                                        CQINCH==^O176414
                                        CQCOUT==^O177315
                                        CQCSIN==^O177375
                                        BUFPAG==2
                                        BUF=BUFPAG*256
                                        ROMLOC=^O4000
                                        RAMLOC=^O25000                  ;PAGE 2A
                                        OUTCH=^O176755
                                        CZGETL=^O176414
                                        LINLEN==40
                                        BUFLEN==240
                                        RORSW==1
                                        STKEND=507>
                                IFE     RORSW,<
                                DEFINE  ROR (WD),<
                                        LDAI    0
                                        BCC     .+4
                                        LDAI    ^O200
                                        LSR     WD
                                        ORA     WD
                                        STA     WD>>
                                
                                DEFINE ACRLF,<
                                        13
                                        10>
                                DEFINE  SYNCHK  (Q),<
                                        LDAI    <Q>
                                        JSR     SYNCHR>
                                DEFINE  DT(Q),<
                                IRPC    Q,<IFDIF <Q><">,<EXP "Q">>>
                                DEFINE  LDWD    (WD),<
                                        LDA     WD
                                        LDY     <WD>+1>
                                DEFINE  LDWDI   (WD),<
                                        LDAI    <<WD>&^O377>
                                        LDYI    <<WD>/^O400>>
                                DEFINE  LDWX    (WD),<
                                        LDA     WD
                                        LDX     <WD>+1>
                                DEFINE  LDWXI   (WD),<
                                        LDAI    <<WD>&^O377>
                                        LDXI    <<WD>/^O400>>
                                DEFINE  LDXY    (WD),<
                                        LDX     WD
                                        LDY     <WD>+1>
                                DEFINE  LDXYI   (WD),<
                                        LDXI    <<WD>&^O377>
                                        LDYI    <<WD>/^O400>>
                                DEFINE  STWD    (WD),<
                                        STA     WD
                                        STY     <WD>+1>
                                DEFINE  STWX    (WD),<
                                        STA     WD
                                        STX     <WD>+1>
                                DEFINE  STXY    (WD),<
                                        STX     WD
                                        STY     <WD>+1>
                                DEFINE  CLR     (WD),<
                                        LDAI    0
                                        STA     WD>
                                DEFINE  COM     (WD),<
                                        LDA     WD
                                        EORI    ^O377
                                        STA     WD>
                                DEFINE  PULWD   (WD),<
                                        PLA
                                        STA     WD
                                        PLA
                                        STA     <WD>+1>
                                DEFINE  PSHWD   (WD),<
                                        LDA     <WD>+1
                                        PHA
                                        LDA     WD
                                        PHA>
                                DEFINE  JEQ     (WD),<
                                        BNE     .+5
                                        JMP     WD>
                                DEFINE  JNE     (WD),<
                                        BEQ     .+5
                                        JMP     WD>
                                DEFINE  BCCA(Q),<       BCC     Q>      ;BRANCHES THAT ALWAYS BRANCH
                                DEFINE  BCSA(Q),<       BCS     Q>      ;THESE ARE USED ON THE 6502 BECAUSE
                                DEFINE  BEQA(Q),<       BEQ     Q>      ;THERE IS NO UNCONDITIONAL BRANCH
                                DEFINE  BNEA(Q),<       BNE     Q>
                                DEFINE  BMIA(Q),<       BMI     Q>
                                DEFINE  BPLA(Q),<       BPL     Q>
                                DEFINE  BVCA(Q),<       BVC     Q>
                                DEFINE  BVSA(Q),<       BVS     Q>
                                DEFINE  INCW(R),<
                                        INC     R
                                        BNE     %Q
                                        INC     R+1
                                %Q:>
                                DEFINE  SKIP1,  <XWD ^O1000,^O044>      ;BIT ZERO PAGE TRICK.
                                DEFINE  SKIP2,  <XWD ^O1000,^O054>      ;BIT ABS TRICK.
                                IF1,<
                                IFE     REALIO,<PRINTX/SIMULATE/>
                                IFE     REALIO-1,<PRINTX KIM>
                                IFE     REALIO-2,<PRINTX OSI>
                                IFE     REALIO-3,<PRINTX COMMODORE>
                                IFE     REALIO-4,<PRINTX APPLE>
                                IFE     REALIO-5,<PRINTX STM>
                                IFN     ADDPRC,<PRINTX ADDITIONAL PRECISION>
                                IFN     INTPRC,<PRINTX INTEGER ARRAYS>
                                IFN     LNGERR,<PRINTX LONG ERRORS>
                                IFN     DISKO,<PRINTX SAVE AND LOAD>
                                IFE     ROMSW,<PRINTX RAM>
                                IFN     ROMSW,<PRINTX ROM>
                                IFE     RORSW,<PRINTX NO ROR>
                                IFN     RORSW,<PRINTX ROR ASSUMED>>
                                PAGE
                                SUBTTL  INTRODUCTION AND COMPILATION PARAMETERS.
                                COMMENT *
                                
                                --------- ---- -- ---------
                                COPYRIGHT 1976 BY MICROSOFT
                                --------- ---- -- ---------
                                7/27/78 FIXED BUG WHERE FOR VARIABLE AT BYTE FF MATCHED RETURN SEARCHING
                                        FOR GOSUB ENTRY ON STACK IN FNDFOR CALL BY CHANGING STA FORPNT
                                        TO STA FORPNT+1. THIS IS A SERIOUS BUG IN ALL VERSIONS.
                                7/27/78 FIXED BUG AT NEWSTT UNDER IFN BUFPAG WHEN CHECK OF CURLIN
                                        WAS DONE BEFORE CURLIN SET UP SO INPUT RETRIES OF FIRST STATEMENT
                                        WAS GIVING SYNTAX ERROR INSTEAD OF REDO FROM START (CODE WAS 12/1/77 FIX)
                                7/1/78  SAVED A FEW BYTES IN INIT FOR COMMODORE (14)
                                7/1/78 FIXED BUG WHERE REPLACING A LINE OVERFLOWING MEMORY LEFT LINKS
                                        IN A BAD STATE. (CODE AT NODEL AND FINI) BUG#4
                                7/1/78 FIXED BUG WHERE GARBAGE COLLECTION NEVER(!) COLLECTS TEMPS
                                        (STY GRBPNT  AT FNDVAR, LDA GRBPNT ORA GRBPNT+1 AT GRBPAS)
                                        THIS WAS COMMODORE BUG #2
                                7/1/78 FIXED BUG WHERE DELETE/INSERT OF LINE COULD CAUSE A GARBAGE COLLECTION WITH BAD VARTAB IF OUT OF MEMORY
                                         (LDWD MEMSIZ STWD FRETOP=JSR RUNC CLC ALSO AT NODEL)
                                3/9/78 EDIT TO FIX COMMO TRMPOS AND CHANGE LEFT$ AND RIGHT$ TO ALLOW A SECOND ARGUMENT OF 0 AND RETURN A NULL STRING
                                2/25/78 FIXED BUG THAT INPFLG WAS SET WRONG WHEN BUFPAG.NE.0
                                        INCREASED NUMLEV FROM 19 TO 23
                                2/11/78 DISALLOWED SPACES IN RESERVED WORDS. PUT IN SPECIAL CHECK FOR "GO TO"
                                2/11/78 FIXED BUG WHERE ROUNDING OF THE FAC BEFORE PUSHING COULD CAUSE A STRING POINTER
                                        IN THE FAC TO BE INCREMENTED
                                1/24/78 fixed problem where user defined function undefined check fix was smashing error number in [x]
                                12/1/77 FIXED PROBLEM WHERE PEEK WAS SMASHING (POKER) CAUSING POKE OF PEEK TO FAIL
                                12/1/77 FIXED PROBLEM WHERE PROBLEM WITH VARTXT=LINNUM=BUF-2 CAUSING BUF-1 COMMA TO DISAPPEAR
                                12/1/77 FIXED BUFPAG.NE.0 PROBLEM AT NEWSTT AND STOP : CODE WAS STILL
                                        ASSUMING TXTPTR+1.EQ.0 IFF STATEMENT WAS DIRECT
                                *
                                NUMLEV==23                      ;NUMBER OF STACK LEVELS RESERVED
                                                                ;BY AN EXPLICIT CALL TO "GETSTK".
                                STRSIZ==3                       ;# OF LOCS PER STRING DESCRIPTOR.
                                NUMTMP==3                       ;NUMBER OF STRING TEMPORARIES.
                                CONTW==15                       ;CHARACTER TO SUPPRESS OUTPUT.
                                
                                PAGE
                                SUBTTL  SOME EXPLANATION.
                                COMMENT *
                                
                                M6502 BASIC CONFIGURES BASIC AS FOLLOWS
                                
                                LOW LOCATIONS
                                        PAGE    ZERO
                                
                                                STARTUP:
                                                INITIALLY A JMP TO INITIALIZATION CODE BUT
                                                CHANGED TO A JMP TO "READY".
                                                RESTARTING THE MACHINE AT LOC 0 DURING PROGRAM
                                                EXECUTION CAN LEAVE THINGS MESSED UP.
                                
                                                LOC OF FAC TO INTEGER AND INTEGER TO FAC
                                                ROUTINES.
                                
                                                "DIRECT" MEMORY:
                                                THESE ARE THE MOST COMMONLY USED LOCATIONS.
                                                THEY HOLD BOOKKEEPING INFO AND ALL OTHER
                                                FREQUENTLY USED INFORMATION.
                                                ALL TEMPORARIES, FLAGS, POINTERS, THE BUFFER AREA,
                                                THE FLOATING ACCUMULATOR, AND ANYTHING ELSE THAT
                                                IS USED TO STORE A CHANGING VALUE SHOULD BE LOCATED
                                                IN THIS AREA. CARE MUST BE MADE IN MOVING LOCATIONS
                                                IN THIS AREA SINCE THE JUXTAPOSITION OF TWO LOCATIONS
                                                IS OFTEN DEPENDED UPON.
                                
                                                STILL IN RAM WE HAVE THE BEGINNING OF THE "CHRGET"
                                                SUBROUTINE. IT IS HERE SO [TXTPTR] CAN BE THE
                                                EXTENDED ADDRESS OF A LOAD INSTRUCTION.
                                                THIS SAVES HAVING TO BOTHER ANY REGISTERS.
                                
                                        PAGE    ONE
                                                THE STACK.
                                
                                        STORAGE PAGE TWO AND ON
                                                IN RAM VERSIONS THESE DATA STRUCTURES COME AT THE
                                                END OF BASIC. IN ROM VERSON THEY ARE AT RAMLOC WHICH
                                                CAN EITHER BE ABOVE OR BELOW ROMLOC, WHICH IS WHERE
                                                BASIC ITSELF RESIDES.
                                
                                                                A ZERO.
                                                [TXTTAB]        POINTER TO NEXT LINE'S POINTER.
                                                                LINE # OF THIS LINE (2 BYTES).
                                                                CHARACTERS ON THIS LINE.
                                                                ZERO.
                                                                POINTER AT NEXT LINE'S POINTER
                                                                        (POINTED TO BY THE ABOVE POINTER).
                                                                ... REPEATS ...
                                                LAST LINE:      POINTER AT ZERO POINTER.
                                                                LINE # OF THIS LINE.
                                                                CHARACTERS ON THIS LINE.
                                                                ZERO.
                                                                DOUBLE ZERO (POINTED TO BY THE ABOVE POINTER).
                                                [VARTAB]        SIMPLE VARIABLES. 6 BYTES PER VALUE.
                                                                2 BYTES GIVE THE NAME, 4 BYTES THE VALUE.
                                                                ... REPEATS ...
                                                [ARYTAB]        ARRAY VARIABLES. 2 BYTES NAME, 2 BYTE
                                                                LENGTH, NUMBER OF DIMENSIONS , EXTENT OF
                                                                EACH DIMENSION (2BYTES/), VALUES
                                                                ... REPEATS ...
                                                [STREND]        FREE SPACE.
                                                                ... REPEATS ...
                                                [FRETOP]        STRING SPACE IN USE.
                                                                ... REPEATS ...
                                                [MEMSIZ]        HIGHEST MACHINE LOCATION.
                                                                UNUSED EXCEPT BY THE VAL FUNCTION.
                                
                                                ROM -- CONSTANTS AND CODE.
                                
                                        FUNCTION DISPATCH ADDRESSES (AT ROMLOC)
                                                "FUNDSP" CONTAINS THE ADDRESSES OF THE
                                                FUNCTION ROUTINES IN THE ORDER OF THE
                                                FUNCTION NAMES IN THE CRUNCH LIST.
                                                THE FUNCTIONS THAT TAKE MORE THAN ONE ARGUMENT
                                                ARE AT THE END. SEE THE EXPLANATION AT "ISFUN".
                                
                                        THE OPERATOR LIST
                                                THE "OPTAB" LIST CONTAINS AN OPERATOR'S PRECEDENCE
                                                FOLLOWED BY THE ADDRESS OF THE ROUTINE TO PERFORM
                                                THE OPERATION. THE INDEX INTO THE
                                                OPERATOR LIST IS MADE BY SUBTRACTING OFF THE CRUNCH VALUE
                                                OF THE LOWEST NUMBERED OPERATOR. THE ORDER
                                                OF OPERATORS IN THE CRUNCH LIST AND IN "OPTAB" IS IDENTICAL.
                                                THE PRECEDENCES ARE ARBITRARY EXCEPT FOR THEIR
                                                COMPARATIVE SIZES. NOTE THAT THE PRECEDENCE FOR
                                                UNARY OPERATORS SUCH AS "NOT" AND NEGATION ARE
                                                SETUP SPECIALLY WITHOUT USING THE LIST.
                                
                                        THE RESERVED WORD OR CRUNCH LIST
                                                WHEN A COMMAND OR PROGRAM LINE IS TYPED IN
                                                IT IS STORED IN "BUF". AS SOON AS THE WHOLE LINE
                                                HAS BEEN TYPED IN ("INLIN" RETURNS) "CRUNCH" IS
                                                CALLED TO CONVERT ALL RESERVED WORDS TO THEIR
                                                CRUNCHED VALUES. THIS REDUCES THE SIZE OF THE
                                                PROGRAM AND SPEEDS UP EXECUTION BY ALLOWING
                                                LIST DISPATCHES TO PERFORM FUNCTIONS, STATEMENTS,
                                                AND OPERATIONS. THIS IS BECAUSE ALL THE STATEMENT
                                                NAMES ARE STORED CONSECUTIVELY IN THE CRUNCH LIST.
                                                WHEN A MATCH IS FOUND BETWEEN A STRING
                                                OF CHARACTERS AND A WORD IN THE CRUNCH LIST
                                                THE ENTIRE TEXT OF THE MATCHED WORD IS TAKEN OUT OF
                                                THE INPUT LINE AND A RESERVED WORD TOKEN IS PUT
                                                IN ITS PLACE. A RESERVED WORD TOKEN IS ALWAYS EQUAL
                                                TO OCTAL 200 PLUS THE POSITION OF THE MATCHED WORD
                                                IN THE CRUNCH LIST.
                                
                                        STATEMENT DISPATCH ADDRESSES
                                                WHEN A STATEMENT IS TO BE EXECUTED, THE FIRST
                                                CHARACTER OF THE STATEMENT IS EXAMINED
                                                TO SEE IF IT IS LESS THAN THE RESERVED
                                                WORD TOKEN FOR THE LOWEST NUMBERED STATEMENT NAME.
                                                IF SO, THE "LET" CODE IS CALLED TO
                                                TREAT THE STATEMENT AS AN ASSIGNMENT STATEMENT.
                                                OTHERWISE A CHECK IS MADE TO MAKE SURE THE
                                                RESERVED WORD NUMBER IS NOT TOO LARGE TO BE A
                                                STATEMENT TYPE NUMBER. IF NOT THE ADDRESS
                                                TO DISPATCH TO IS FETCHED FROM "STMDSP" (THE STATEMENT
                                                DISPATCH LIST) USING THE RESERVED WORD
                                                NUMBER FOR THE STATEMENT TO CALCULATE AN INDEX INTO
                                                THE LIST.
                                
                                        ERROR MESSAGES
                                                WHEN AN ERROR CONDITION IS DETECTED,
                                                [ACCX] MUST BE SET UP TO INDICATE WHICH ERROR
                                                MESSAGE IS APPROPRIATE AND A BRANCH MUST BE MADE
                                                TO "ERROR". THE STACK WILL BE RESET AND ALL
                                                PROGRAM CONTEXT WILL BE LOST. VARIABLES
                                                VALUES AND THE ACTUAL PROGRAM REMAIN INTACT.
                                                ONLY THE VALUE OF [ACCX] IS IMPORTANT WHEN
                                                THE BRANCH IS MADE TO ERROR. [ACCX] IS USED AS AN
                                                INDEX INTO "ERRTAB" WHICH GIVES THE TWO
                                                CHARACTER ERROR MESSAGE THAT WILL BE PRINTED ON THE
                                                USER'S TERMINAL.
                                
                                
                                        TEXTUAL MESSAGES
                                                CONSTANT MESSAGES ARE STORED HERE. UNLESS
                                                THE CODE TO CHECK IF A STRING MUST BE COPIED
                                                IS CHANGED THESE STRINGS MUST BE STORED ABOVE
                                                PAGE ZERO, OR ELSE THEY WILL BE COPIED BEFORE
                                                THEY ARE PRINTED.
                                
                                        FNDFOR
                                                MOST SMALL ROUTINES ARE FAIRLY SIMPLE
                                                AND ARE DOCUMENTED IN PLACE. "FNDFOR" IS
                                                USED FOR FINDING "FOR" ENTRIES ON
                                                THE STACK. WHENEVER A "FOR" IS EXECUTED, A
                                                16-BYTE ENTRY IS PUSHED ONTO THE STACK.
                                                BEFORE THIS IS DONE, HOWEVER, A CHECK
                                                MUST BE MADE TO SEE IF THERE
                                                ARE ANY "FOR" ENTRIES ALREADY ON THE STACK
                                                FOR THE SAME LOOP VARIABLE. IF SO, THAT "FOR" ENTRY
                                                AND ALL OTHER "FOR" ENTRIES THAT WERE MADE AFTER IT
                                                ARE ELIMINATED FROM THE STACK. THIS IS SO A
                                                PROGRAM THAT JUMPS OUT OF THE MIDDLE
                                                OF A "FOR" LOOP AND THEN RESTARTS THE LOOP AGAIN
                                                AND AGAIN WON'T USE UP 18 BYTES OF STACK
                                                SPACE EVERY TIME. THE "NEXT" CODE ALSO
                                                CALLS "FNDFOR" TO SEARCH FOR A "FOR" ENTRY WITH
                                                THE LOOP VARIABLE IN
                                                THE "NEXT". AT WHATEVER POINT A MATCH IS FOUND
                                                THE STACK IS RESET. IF NO MATCH IS FOUND A
                                                "NEXT WITHOUT FOR"  ERROR OCCURS. GOSUB EXECUTION
                                                ALSO PUTS A 5-BYTE ENTRY ON STACK.
                                                WHEN A RETURN IS EXECUTED "FNDFOR" IS
                                                CALLED WITH A VARIABLE POINTER THAT CAN'T
                                                BE MATCHED. WHEN "FNDFOR" HAS RUN
                                                THROUGH ALL THE "FOR" ENTRIES ON THE STACK
                                                IT RETURNS AND THE RETURN CODE MAKES
                                                SURE THE ENTRY THAT WAS STOPPED
                                                ON IS A GOSUB ENTRY. THIS ASSURES THAT
                                                IF YOU GOSUB TO A SECTION OF CODE
                                                IN WHICH A FOR LOOP IS ENTERED BUT NEVER
                                                EXITED THE RETURN WILL STILL BE
                                                ABLE TO FIND THE MOST RECENT
                                                GOSUB ENTRY. THE "RETURN" CODE ELIMINATES THE
                                                "GOSUB" ENTRY AND ALL "FOR" ENTRIES MADE AFTER
                                                THE GOSUB ENTRY.
                                
                                        NON-RUNTIME STUFF
                                                THE CODE TO INPUT A LINE, CRUNCH IT, GIVE ERRORS,
                                                FIND A SPECIFIC LINE IN THE PROGRAM,
                                                PERFORM A "NEW", "CLEAR", AND "LIST" ARE
                                                ALL IN THIS AREA. GIVEN THE EXPLANATION OF
                                                PROGRAM STORAGE SET FORTH ABOVE, THESE ARE
                                                ALL STRAIGHTFORWARD.
                                
                                        NEWSTT
                                                WHENEVER A STATEMENT FINISHES EXECUTION IT
                                                DOES A "RTS" WHICH TAKES
                                                EXECUTION BACK TO "NEWSTT". STATEMENTS THAT
                                                CREATE OR LOOK AT SEMI-PERMANENT STACK ENTRIES
                                                MUST GET RID OF THE RETURN ADDRESS OF "NEWSTT" AND
                                                JMP TO "NEWSTT" WHEN DONE. "NEWSTT" ALWAYS
                                                CHRGETS THE FIRST CHARACTER AFTER THE STATEMENT
                                                NAME BEFORE DISPATCHING. WHEN RETURNING
                                                BACK TO "NEWSTT" THE ONLY THING THAT
                                                MUST BE SET UP IS THE TEXT POINTER IN
                                                "TXTPTR". "NEWSTT" WILL CHECK TO MAKE SURE
                                                "TXTPTR" IS POINTING TO A STATEMENT TERMINATOR.
                                                IF A STATEMENT SHOULDN'T BE PERFORMED UNLESS
                                                IT IS PROPERLY FORMATTED (I.E. "NEW") IT CAN
                                                SIMPLY DO A RETURN AFTER READING ALL OF
                                                ITS ARGUMENTS. SINCE THE ZERO FLAG
                                                BEING OFF INDICATES THERE IS NOT
                                                A STATEMENT TERMINATOR "NEWSTT" WILL
                                                DO THE JMP TO THE "SYNTAX ERROR"
                                                ROUTINE. IF A STATEMENT SHOULD BE STARTED
                                                OVER IT CAN DO LDWD OLDTXT, STWD TXTPTR RTS SINCE THE TEXT PNTR
                                                AT "NEWSTT" IS ALWAYS STORED IN "OLDTXT".
                                                THE ^C CODE STORES [CURLIN] (THE
                                                CURRENT LINE NUMBER) IN "OLDLIN" SINCE THE ^C CHECK
                                                IS MADE BEFORE THE STATEMENT POINTED TO IS
                                                EXECUTED. "STOP" AND "END" STORE THE TEXT POINTER
                                                FROM "TXTPTR", WHICH POINTS AT THEIR TERMINATING
                                                CHARACTER, IN "OLDTXT".
                                
                                        STATEMENT CODE
                                                THE INDIVIDUAL STATEMENT CODE COMES
                                                NEXT. THE APPROACH USED IN EXECUTING EACH
                                                STATEMENT IS DOCUMENTED IN THE STATEMENT CODE
                                                ITSELF.
                                
                                        FRMEVL, THE FORMULA EVALUATOR
                                                GIVEN A TEXT POINTER POINTING TO THE STARTING
                                                CHARACTER OF A FORMULA, "FRMEVL"
                                                EVALUATES THE FORMULA AND LEAVES
                                                THE VALUE IN THE FLOATING ACCUMULATOR (FAC).
                                                "TXTPTR" IS RETURNED POINTING TO THE FIRST CHARACTER
                                                THAT COULD NOT BE INTERPRETED AS PART OF THE
                                                FORMULA. THE ALGORITHM USES THE STACK
                                                TO STORE TEMPORARY RESULTS:
                                
                                                        0. PUT A DUMMY PRECEDENCE OF ZERO ON
                                                                THE STACK.
                                                        1. READ LEXEME (CONSTANT,FUNCTION,
                                                                VARIABLE,FORMULA IN PARENS)
                                                                AND TAKE THE LAST PRECEDENCE VALUE
                                                                OFF THE STACK.
                                                        2. SEE IF THE NEXT CHARACTER IS AN OPERATOR.
                                                                IF NOT, CHECK PREVIOUS ONE. THIS MAY CAUSE
                                                                OPERATOR APPLICATION OR AN ACTUAL
                                                                RETURN FROM "FRMEVL".
                                                        3. IF IT IS, SEE WHAT PRECEDENCE IT HAS
                                                                AND COMPARE IT TO THE PRECEDENCE
                                                                OF THE LAST OPERATOR ON THE STACK.
                                                        4. IF = OR LESS REMEMBER THE OPERATOR
                                                                POINTER OF THIS OPERATOR
                                                                AND BRANCH TO "QCHNUM" TO CAUSE
                                                                APPLICATION OF THE LAST OPERATOR.
                                                                EVENTUALLY RETURN TO STEP 2
                                                                BY RETURNING TO JUST AFTER "DOPREC".
                                                        5. IF GREATER PUT THE LAST PRECEDENCE
                                                                BACK ON, SAVE THE OPERATOR ADDRESS,
                                                                CURRENT TEMPORARY RESULT,
                                                                AND PRECEDENCE AND RETURN TO STEP 1.
                                
                                                RELATIONAL OPERATORS ARE ALL HANDLED THROUGH
                                                A COMMON ROUTINE. SPECIAL
                                                CARE IS TAKEN TO DETECT TYPE MISMATCHES SUCH AS 3+"F".
                                
                                        EVAL -- THE ROUTINE TO READ A LEXEME
                                                "EVAL" CHECKS FOR THE DIFFERENT TYPES OF
                                                ENTITIES IT IS SUPPOSED TO DETECT.
                                                LEADING PLUSES ARE IGNORED,
                                                DIGITS AND "." CAUSE "FIN" (FLOATING INPUT)
                                                TO BE CALLED. FUNCTION NAMES CAUSE THE
                                                FORMULA INSIDE THE PARENTHESES TO BE EVALUATED
                                                AND THE FUNCTION ROUTINE TO BE CALLED. VARIABLE
                                                NAMES CAUSE "PTRGET" TO BE CALLED TO GET A POINTER
                                                TO THE VALUE, AND THEN THE VALUE IS PUT INTO
                                                THE FAC. AN OPEN PARENTHESIS CAUSES "FRMEVL"
                                                TO BE CALLED (RECURSIVELY), AND THE ")" TO
                                                BE CHECKED FOR. UNARY OPERATORS (NOT AND
                                                NEGATION)  PUT THEIR PRECEDENCE ON THE STACK
                                                AND ENTER FORMULA EVALUATION AT STEP 1, SO
                                                THAT EVERYTHING UP TO AN OPERATOR GREATER THAN
                                                THEIR PRECEDENCE OR THE END OF THE FORMULA
                                                WILL BE EVALUATED.
                                
                                        DIMENSION AND VARIABLE SEARCHING
                                                SPACE IS ALLOCATED FOR VARIABLES AS THEY ARE
                                                ENCOUNTERED. THUS "DIM" STATEMENTS MUST BE
                                                EXECUTED TO HAVE EFFECT. 6 BYTES ARE ALLOCATED
                                                FOR EACH SIMPLE VARIABLE, WHETHER IT IS A STRING,
                                                NUMBER OR USER DEFINED FUNCTION. THE FIRST TWO
                                                BYTES GIVE THE NAME OF THE VARIABLE AND THE LAST FOUR
                                                GIVE ITS VALUE. [VARTAB] GIVES THE FIRST LOCATION
                                                WHERE A SIMPLE VARIABLE NAME IS FOUND AND [ARYTAB]
                                                GIVES THE LOCATION TO STOP SEARCHING FOR SIMPLE
                                                VARIABLES. A "FOR" ENTRY HAS A TEXT POINTER
                                                AND A POINTER TO A VARIABLE VALUE SO NEITHER
                                                THE PROGRAM OR THE SIMPLE VARIABLES CAN BE
                                                MOVED WHILE THERE ARE ACTIVE "FOR" ENTRIES ON THE STACK.
                                                USER DEFINED FUNCTION VALUES ALSO CONTAIN
                                                POINTERS INTO SIMPLE VARIABLE SPACE SO NO USER-DEFINED
                                                FUNCTION VALUES CAN BE RETAINED IF SIMPLE VARIABLES
                                                ARE MOVED. ADDING A SIMPLE VARIABLE IS JUST
                                                ADDING SIX TO [ARYTAB] AND [STREND], BLOCK TRANSFERING
                                                THE ARRAY VARIABLES UP BY SIX AND MAKING SURE THE
                                                NEW [STREND] IS NOT TOO CLOSE TO THE STRINGS.
                                                THIS MOVEMENT OF ARRAY VARIABLES MEANS
                                                THAT NO POINTER TO AN ARRAY WILL STAY VALID WHEN
                                                NEW SIMPLE VARIABLES CAN BE ENCOUNTERED. THIS IS
                                                WHY ARRAY VARIABLES ARE NOT ALLOWED FOR "FOR"
                                                LOOP VARIABLES. SETTING UP A NEW ARRAY VARIABLE
                                                MERELY INVOLVES BUILDING THE DESCRIPTOR,
                                                UPDATING [STREND], AND MAKING SURE THERE IS
                                                STILL ENOUGH ROOM BETWEEN [STREND] AND STRING SPACE.
                                                "PTRGET", THE ROUTINE WHICH RETURNS A POINTER
                                                TO A VARIABLE VALUE, HAS TWO IMPORTANT FLAGS. ONE IS
                                                "DIMFLG" WHICH INDICATES WHETHER "DIM" CALLED "PTRGET"
                                                OR NOT. IF SO, NO PRIOR ENTRY FOR THE VARIABLE IN
                                                QUESTION SHOULD BE FOUND, AND THE INDEX INDICATES
                                                HOW MUCH SPACE TO SET ASIDE. SIMPLE VARIABLES CAN
                                                BE "DIMENSIONED", BUT THE ONLY EFFECT WILL BE TO
                                                SET ASIDE SPACE FOR THE VARIABLE IF IT HASN'T BEEN
                                                ENCOUNTERED YET. THE OTHER IMPORTANT FLAG IS "SUBFLG"
                                                WHICH INDICATES WHETHER A SUBSCRIPTED VARIABLE SHOULD BE
                                                ALLOWED IN THE CURRENT CONTEXT. IF [SUBFLG] IS NON-ZERO
                                                THE OPEN PARENTHESIS FOR A SUBSCRIPTED VARIABLE
                                                WILL NOT BE SCANNED BY "PTRGET", AND "PTRGET" WILL RETURN
                                                WITH A TEXT POINTER POINTING TO THE "(", IF
                                                THERE WAS ONE.
                                        STRINGS
                                                IN THE VARIABLE TABLES STRINGS ARE STORED JUST LIKE
                                                NUMERIC VARIABLES. SIMPLE STRINGS HAVE THREE VALUE
                                                BYTES WHICH ARE INITIALIZED TO ALL ZEROS (WHICH
                                                REPRESENTS THE NULL STRING). THE ONLY DIFFERENCE
                                                IN HANDLING IS THAT WHEN "PTRGET" SEES A "$" AFTER THE
                                                NAME OF A VARIABLE, "PTRGET" SETS [VALTYP]
                                                TO NEGATIVE ONE AND TURNS
                                                ON THE MSB (MOST-SIGNIFIGANT-BIT) OF THE VALUE OF
                                                THE FIRST CHARACTER OF THE VARIABLE NAME.
                                                HAVING THIS BIT ON IN THE NAME OF THE VARIABLE ENSURES
                                                THAT THE SEARCH ROUTINE WILL NOT MATCH
                                                'A' WITH 'A$' OR 'A$' WITH 'A'. THE MEANING OF
                                                THE THREE VALUE BYTES ARE:
                                                        LOW
                                                                LENGTH OF THE STRING
                                                                LOW 8 BITS
                                                                HIGH 8 BITS  OF THE ADDRESS
                                                                        OF THE CHARACTERS IN THE
                                                                        STRING IF LENGTH.NE.0.
                                                                        MEANINGLESS OTHERWISE.
                                                        HIGH
                                                THE VALUE OF A STRING VARIABLE (THESE 3 BYTES)
                                                IS CALLED THE STRING DESCRIPTOR TO DISTINGUISH
                                                IT FROM THE ACTUAL STRING DATA. WHENEVER A
                                                STRING CONSTANT IS ENCOUNTERED IN A FORMULA OR AS
                                                PART OF AN INPUT STRING, OR AS PART OF DATA, "STRLIT"
                                                IS CALLED, CAUSING A DESCRIPTOR TO BE BUILT FOR
                                                THE STRING. WHEN ASSIGNMENT IS MADE TO A STRING POINTING INTO
                                                "BUF" THE VALUE IS COPIED INTO STRING SPACE SINCE [BUF]
                                                IS ALWAYS CHANGING.
                                
                                                STRING FUNCTIONS AND THE ONE STRING OPERATOR "+"
                                                ALWAYS RETURN THEIR VALUES IN STRING SPACE.
                                                ASSIGNING A STRING A CONSTANT VALUE IN A PROGRAM
                                                THROUGH A "READ" OR ASSIGNMENT STATEMENT
                                                WILL NOT USE ANY STRING SPACE SINCE
                                                THE STRING DESCRIPTOR  WILL POINT INTO THE
                                                PROGRAM ITSELF. IN GENERAL, COPYING IS DONE
                                                WHEN A STRING VALUE IS IN "BUF", OR IT IS IN STRING
                                                SPACE AND THERE IS AN ACTIVE POINTER TO IT.
                                                THUS F$=G$ WILL CAUSE COPYING IF G$ HAS ITS
                                                STRING DATA IN STRING SPACE. F$=CHR$(7)
                                                WILL USE ONE BYTE OF STRING SPACE TO STORE THE
                                                NEW ONE CHARACTER STRING CREATED BY "CHR$", BUT
                                                THE ASSIGNMENT ITSELF WILL CAUSE NO COPYING SINCE
                                                THE ONLY POINTER AT THE NEW STRING IS A
                                                TEMPORARY DESCRIPTOR CREATED BY "FRMEVL" WHICH WILL
                                                GO AWAY AS SOON AS THE ASSIGNMENT IS DONE.
                                                IT IS THE NATURE OF GARBAGE COLLECTION THAT
                                                DISALLOWS HAVING TWO STRING DESCRIPTORS POINT TO THE SAME
                                                AREA IN STRING SPACE. STRING FUNCTIONS AND OPERATORS
                                                MUST PROCEED AS FOLLOWS:
                                                        1) FIGURE OUT THE LENGTH OF THEIR RESULT.
                                
                                                        2) CALL "GETSPA" TO FIND SPACE FOR THEIR
                                                        RESULT. THE ARGUMENTS TO THE FUNCTION
                                                        OR OPERATOR MAY CHANGE SINCE GARBAGE COLLECTION
                                                        MAY BE INVOKED. THE ONLY THING THAT CAN
                                                        BE SAVED DURING THE CALL TO "GETSPA" IS A POINTER
                                                        TO THE DESCRIPTORS OF THE ARGUMENTS.
                                                        3) CONSTRUCT THE RESULT DESCRIPTOR IN "DSCTMP".
                                                        "GETSPA" RETURNS THE LOCATION OF THE AVAILABLE
                                                        SPACE.
                                                        4) CREATE THE NEW VALUE BY COPYING PARTS
                                                        OF THE ARGUMENTS OR WHATEVER.
                                                        5) FREE UP THE ARGUMENTS BY CALLING "FRETMP".
                                                        6) JUMP TO "PUTNEW" TO GET THE DESCRIPTOR IN
                                                        "DSCTMP" TRANSFERRED INTO A NEW STRING TEMPORARY.
                                
                                                THE REASON FOR STRING TEMPORARIES IS THAT GARBAGE
                                                COLLECTION HAS TO KNOW ABOUT ALL ACTIVE STRING DESCRIPTORS
                                                SO IT KNOWS WHAT IS AND ISN'T IN USE. STRING TEMPORARIES ARE
                                                USED TO STORE THE DESCRIPTORS OF STRING EXPRESSIONS.
                                
                                                INSTEAD OF HAVING AN ACTUAL VALUE STORED IN THE
                                                FAC, AND HAVING THE VALUE OF A TEMPORARY RESULT
                                                BEING SAVED ON THE STACK, AS HAPPENS WITH NUMERIC
                                                VARIABLES, STRINGS HAVE THE POINTER TO A STRING DESCRIPTOR
                                                STORED IN THE FAC, AND IT IS THIS POINTER
                                                THAT GETS SAVED ON THE STACK BY FORMULA EVALUATION.
                                                STRING FUNCTIONS CANNOT FREE THEIR ARGUMENTS UP RIGHT
                                                AWAY SINCE "GETSPA" MAY FORCE
                                                GARBAGE COLLECTION AND THE ARGUMENT STRINGS
                                                MAY BE OVER-WRITTEN SINCE GARBAGE COLLECTION
                                                WILL NOT BE ABLE TO FIND AN ACTIVE POINTER TO
                                                THEM. FUNCTION AND OPERATOR RESULTS ARE BUILT IN
                                                "DSCTMP" SINCE STRING TEMPORARIES ARE ALLOCATED
                                                (PUTNEW) AND DEALLOCATED (FRETMP) IN A FIFO ORDERING
                                                (I.E. A STACK) SO THE NEW TEMPORARY CANNOT
                                                BE SET UP UNTIL THE OLD ONE(S) ARE FREED. TRYING
                                                TO BUILD A RESULT IN A TEMPORARY AFTER
                                                FREEING UP THE ARGUMENT TEMPORARIES COULD RESULT
                                                IN ONE OF THE ARGUMENT TEMPORARIES BEING OVERWRITTEN
                                                TOO SOON BY THE NEW RESULT.
                                
                                                STRING SPACE IS ALLOCATED AT THE VERY TOP
                                                OF MEMORY. "MEMSIZ" POINTS BEYOND THE LAST LOCATION OF
                                                STRING SPACE. STRINGS ARE STORED IN HIGH LOCATIONS
                                                FIRST. WHENEVER STRING SPACE IS ALLOCATED (GETSPA).
                                                [FRETOP], WHICH IS INITIALIZED TO [MEMSIZ], IS UPDATED
                                                TO GIVE THE HIGHEST LOCATION IN STRING SPACE
                                                THAT IS NOT IN USE. THE RESULT IS THAT
                                                [FRETOP] GETS SMALLER AND SMALLER, UNTIL SOME
                                                ALLOCATION WOULD MAKE [FRETOP] LESS THAN OR EQUAL TO
                                                [STREND]. THIS MEANS STRING SPACE HAS RUN INTO THE
                                                THE ARRAYS AND THAT GARBAGE COLLECTION MUST BE CALLED.
                                
                                                GARBAGE COLLECTION:
                                                        0. [MINPTR]=[STREND] [FRETOP]=[MEMSIZ]
                                                        1. [REMMIN]=0
                                                        2. FOR EACH STRING DESCRIPTOR
                                                        (TEMPORARIES, SIMPLE STRINGS, STRING ARRAYS)
                                                        IF THE STRING IS NOT NULL AND ITS POINTER IS
                                                        .GT.MINPTR AND .LT.FRETOP,
                                                        [MINPTR]=THIS STRING DESCRIPTOR'S POINTER,
                                                        [REMMIN]=POINTER AT THIS STRING DESCRIPTOR.
                                                        END.
                                                        3. IF REMMIN.NE.0 (WE FOUND AN UNCOLLECTED STRING),
                                                        BLOCK TRANSFER THE STRING DATA POINTED
                                                        TO IN THE STRING DESCRIPTOR POINTED TO BY "REMMIN"
                                                        SO THAT THE LAST BYTE OF STRING DATA IS AT
                                                        [FRETOP]. UPDATE [FRETOP] SO THAT IT
                                                        POINTS TO THE LOCATION JUST BELOW THE ONE
                                                        THE STRING DATA WAS MOVED INTO. UPDATE
                                                        THE POINTER IN THE DESCRIPTOR SO IT POINTS
                                                        TO THE NEW LOCATION OF THE STRING DATA.
                                                        GO TO STEP 1.
                                
                                                AFTER CALLING GARBAGE COLLECTION "GETSPA" AGAIN CHECKS
                                                TO SEE IF [ACCA] CHARACTERS ARE AVAILABLE BETWEEN
                                                [STREND] AND [FRETOP]; IF NOT, AN "OUT OF STRING"
                                                ERROR IS INVOKED.
                                
                                        MATH PACKAGE
                                                THE MATH PACKAGE CONTAINS FLOATING INPUT (FIN),
                                                FLOATING OUTPUT (FOUT), FLOATING COMPARE (FCOMP)
                                                ... AND ALL THE NUMERIC OPERATORS AND FUNCTIONS.
                                                THE FORMATS, CONVENTIONS AND ENTRY POINTS ARE ALL
                                                DESCRIBED IN THE MATH PACKAGE ITSELF.
                                
                                        INIT -- THE INITIALIZATION ROUTINE
                                                THE AMOUNT OF MEMORY,
                                                TERMINAL WIDTH, AND WHICH FUNCTIONS TO BE RETAINED
                                                ARE ASCERTAINED FROM THE USER. A ZERO IS PUT DOWN
                                                AT THE FIRST LOCATION NOT USED BY THE MATH-PACKAGE
                                                AND [TXTTAB] IS SET UP TO POINT AT THE NEXT LOCATION.
                                                THIS DETERMINES WHERE PROGRAM STORAGE WILL START.
                                                SPECIAL CHECKS ARE MADE TO MAKE SURE
                                                ALL QUESTIONS IN "INIT" ARE ANSWERED REASONABLY, SINCE
                                                ONCE "INIT" FINISHES, THE LOCATIONS IT USES ARE
                                                USED FOR PROGRAM STORAGE. THE LAST THING "INIT" DOES IS
                                                CHANGE LOCATION ZERO TO BE A JUMP TO "READY" INSTEAD
                                                OF "INIT". ONCE THIS IS DONE THERE IS NO WAY TO RESTART
                                                "INIT".
                                HIGH LOCATIONS
                                
                                *
                                PAGE
                                SUBTTL  PAGE ZERO.
                                IFN     REALIO-3,<
                                START:  JMP     INIT            ;INITIALIZE - SETUP CERTAIN LOCATIONS
                                                                ;AND DELETE FUNCTIONS IF NOT NEEDED,
                                                                ;AND CHANGE THIS TO "JMP READY"
                                                                ;IN CASE USER RESTARTS AT LOC ZERO.
                                RDYJSR: JMP     INIT            ;CHANGED TO "JMP STROUT" BY "INIT"
                                                                ;TO HANDLE ERRORS.
                                ADRAYI: ADR(AYINT)              ;STORE HERE THE ADDR OF THE
                                                                ;ROUTINE TO TURN THE FAC INTO A
                                                                ;TWO BYTE SIGNED INTEGER IN [Y,A]
                                ADRGAY: ADR(GIVAYF)>            ;STORE HERE THE ADDR OF THE
                                                                ;ROUTINE TO CONVERT [Y,A] TO A FLOATING
                                                                ;POINT NUMBER IN THE FAC.
                                IFN     ROMSW,<
                                USRPOK: JMP     FCERR>          ;SET UP ORIG BY INIT.
                                ;
                                ; THIS IS THE "VOLATILE" STORAGE AREA AND NONE OF IT
                                ; CAN BE KEPT IN ROM. ANY CONSTANTS IN THIS AREA CANNOT
                                ; BE KEPT IN A ROM, BUT MUST BE LOADED IN BY THE
                                ; PROGRAM INSTRUCTIONS IN ROM.
                                ;
                                ; --- GENERAL RAM ---:
                                CHARAC: BLOCK   1               ;A DELIMITING CHARACTER.
                                INTEGR= CHARAC                  ;A ONE-BYTE INTEGER FROM "QINT".
                                ENDCHR: BLOCK   1               ;THE OTHER DELIMITING CHARACTER.
                                COUNT:  BLOCK   1               ;A GENERAL COUNTER.
                                
                                ; --- FLAGS ---:
                                DIMFLG: BLOCK   1               ;IN GETTING A POINTER TO A VARIABLE
                                                                ;IT IS IMPORTANT TO REMEMBER WHETHER IT
                                                                ;IS BEING DONE FOR "DIM" OR NOT.
                                                                ;DIMFLG AND VALTYP MUST BE
                                                                ;CONSECUTIVE LOCATIONS.
                                KIMY=   DIMFLG                  ;PLACE TO PRESERVE Y DURING OUT.
                                VALTYP: BLOCK   1               ;THE TYPE INDICATOR.
                                                                ;0=NUMERIC 1=STRING.
                                IFN     INTPRC,<
                                INTFLG: BLOCK   1>              ;TELLS IF INTEGER.
                                DORES:  BLOCK   1               ;WHETHER CAN OR CAN'T CRUNCH RES'D WORDS.
                                                                ;TURNED ON WHEN "DATA"
                                                                ;BEING SCANNED BY CRUNCH SO UNQUOTED
                                                                ;STRINGS WON'T BE CRUNCHED.
                                GARBFL= DORES                   ;WHETHER TO DO GARBAGE COLLECTION.
                                SUBFLG: BLOCK   1               ;FLAG WHETHER SUB'D VARIABLE ALLOWED.
                                                                ;"FOR" AND USER-DEFINED FUNCTION
                                                                ;POINTER FETCHING TURN
                                                                ;THIS ON BEFORE CALLING "PTRGET"
                                                                ;SO ARRAYS WON'T BE DETECTED.
                                                                ;"STKINI" AND "PTRGET" CLEAR IT.
                                                                ;ALSO DISALLOWS INTEGERS THERE.
                                INPFLG: BLOCK   1               ;FLAGS WHETHER WE ARE DOING "INPUT"
                                                                ;OR "READ".
                                TANSGN: BLOCK   1               ;USED IN DETERMINING SIGN OF TANGENT.
                                IFN     REALIO,<
                                CNTWFL: BLOCK   1>              ;SUPPRESS OUTPUT FLAG.
                                                                ;NON-ZERO MEANS SUPPRESS.
                                                                ;RESET BY "INPUT", READY AND ERRORS.
                                                                ;COMPLEMENTED BY INPUT OF ^O.
                                
                                IFE     REALIO-4,<ORG   80>     ;ROOM FOR APPLE PAGE 0 STUFF.
                                ; --- RAM DEALING WITH TERMINAL HANDLING ---:
                                IFN     EXTIO,<
                                CHANNL: BLOCK   1>              ;HOLDS CHANNEL NUMBER.
                                IFN     NULCMD,<
                                NULCNT: 0>                      ;NUMBER OF NULLS TO PRINT.
                                IFN     REALIO-3,<
                                TRMPOS: BLOCK   1>              ;POSITION OF TERMINAL CARRIAGE.
                                LINWID: LINLEN                  ;LENGTH OF LINE (WIDTH).
                                NCMWID: NCMPOS                  ;POSITION BEYOND WHICH THERE ARE
                                                                ;NO MORE FIELDS.
                                LINNUM: 0                       ;LOCATION TO STORE LINE NUMBER BEFORE BUF
                                                                ;SO THAT "BLTUC" CAN STORE IT ALL AWAY AT ONCE.
                                        44                      ;A COMMA (PRELOAD OR FROM ROM)
                                                                ;USED BY INPUT STATEMENT SINCE THE
                                                                ;DATA POINTER ALWAYS STARTS ON A
                                                                ;COMMA OR TERMINATOR.
                                IFE     BUFPAG,<
                                BUF:    BLOCK   BUFLEN>         ;TYPE IN STORED HERE.
                                                                ;DIRECT STATEMENTS EXECUTE OUT OF
                                                                ;HERE. REMEMBER "INPUT" SMASHES BUF.
                                                                ;MUST BE ON PAGE ZERO
                                                                ;OR ASSIGNMENT OF STRING
                                                                ;VALUES IN DIRECT STATEMENTS WON'T COPY
                                                                ;INTO STRING SPACE -- WHICH IT MUST.
                                                                ;N.B. TWO NONZERO BYTES MUST PRECEDE "BUFLNM".
                                
                                ; --- STORAGE FOR TEMPORARY THINGS ---:
                                TEMPPT: BLOCK   1               ;POINTER AT FIRST FREE TEMP DESCRIPTOR.
                                                                ;INITIALIZED TO POINT TO TEMPST.
                                LASTPT: BLOCK   2               ;POINTER TO LAST-USED STRING TEMPORARY.
                                TEMPST: BLOCK   STRSIZ*NUMTMP   ;STORAGE FOR NUMTMP TEMP DESCRIPTORS.
                                INDEX1: BLOCK   2               ;INDEXES.
                                INDEX=  INDEX1
                                INDEX2: BLOCK   2
                                RESHO:  BLOCK   1               ;RESULT OF MULTIPLIER AND DIVIDER.
                                IFN     ADDPRC,<
                                RESMOH: BLOCK   1>              ;ONE MORE BYTE.
                                RESMO:  BLOCK   1
                                RESLO:  BLOCK   1
                                ADDEND= RESMO                   ;TEMPORARY USED BY "UMULT".
                                        0                       ;OVERFLOW FOR RES.
                                
                                ; --- POINTERS INTO DYNAMIC DATA STRUCTURES ---;
                                TXTTAB: BLOCK   2               ;POINTER TO BEGINNING OF TEXT.
                                                                ;DOESN'T CHANGE AFTER BEING
                                                                ;SETUP BY "INIT".
                                VARTAB: BLOCK   2               ;POINTER TO START OF SIMPLE
                                                                ;VARIABLE SPACE.
                                                                ;UPDATED WHENEVER THE SIZE OF THE
                                                                ;PROGRAM CHANGES, SET TO [TXTTAB]
                                                                ;BY "SCRATCH" ("NEW").
                                ARYTAB: BLOCK   2               ;POINTER TO BEGINNING OF ARRAY
                                                                ;TABLE.
                                                                ;INCREMENTED BY 6 WHENEVER
                                                                ;A NEW SIMPLE VARIABLE IS FOUND, AND
                                                                ;SET TO [VARTAB] BY "CLEARC".
                                STREND: BLOCK   2               ;END OF STORAGE IN USE.
                                                                ;INCREASED WHENEVER A NEW ARRAY
                                                                ;OR SIMPLE VARIABLE IS ENCOUNTERED.
                                                                ;SET TO [VARTAB] BY "CLEARC".
                                FRETOP: BLOCK   2               ;TOP OF STRING FREE SPACE.
                                FRESPC: BLOCK   2               ;POINTER TO NEW STRING.
                                MEMSIZ: BLOCK   2               ;HIGHEST LOCATION IN MEMORY.
                                
                                ; --- LINE NUMBERS AND TEXTUAL POINTERS ---:
                                CURLIN: BLOCK   2               ;CURRENT LINE #.
                                                                ;SET TO 0,255 FOR DIRECT STATEMENTS.
                                OLDLIN: BLOCK   2               ;OLD LINE NUMBER (SETUP BY ^C,"STOP"
                                                                ;OR "END" IN A PROGRAM).
                                POKER=  LINNUM                  ;SET UP LOCATION USED BY POKE.
                                                                ;TEMPORARY FOR INPUT AND READ CODE
                                OLDTXT: BLOCK   2               ;OLD TEXT POINTER.
                                                                ;POINTS AT STATEMENT TO BE EXEC'D NEXT.
                                DATLIN: BLOCK   2               ;DATA LINE # -- REMEMBER FOR ERRORS.
                                DATPTR: BLOCK   2               ;POINTER TO DATA. INITIALIZED TO POINT
                                                                ;AT THE ZERO IN FRONT OF [TXTTAB]
                                                                ;BY "RESTORE" WHICH IS CALLED BY "CLEARC".
                                                                ;UPDATED BY EXECUTION OF A "READ".
                                INPPTR: BLOCK   2               ;THIS REMEMBERS WHERE INPUT IS COMING FROM.
                                
                                ; --- STUFF USED IN EVALUATIONS ---:
                                VARNAM: BLOCK   2               ;VARIABLE'S NAME IS STORED HERE.
                                VARPNT: BLOCK   2               ;POINTER TO VARIABLE IN MEMORY.
                                FDECPT= VARPNT                  ;POINTER INTO POWER OF TENS OF "FOUT".
                                FORPNT: BLOCK   2               ;A VARIABLE'S POINTER FOR "FOR" LOOPS
                                                                ;AND "LET" STATEMENTS.
                                LSTPNT= FORPNT                  ;PNTR TO LIST STRING.
                                ANDMSK= FORPNT                  ;THE MASK USED BY WAIT FOR ANDING.
                                EORMSK= FORPNT+1                ;THE MASK FOR EORING IN WAIT.
                                OPPTR:  BLOCK   2               ;POINTER TO CURRENT OP'S ENTRY IN "OPTAB".
                                VARTXT= OPPTR                   ;POINTER INTO LIST OF VARIABLES.
                                OPMASK: BLOCK   1               ;MASK CREATED BY CURRENT OPERATOR.
                                DOMASK=TANSGN                   ;MASK IN USE BY RELATION OPERATIONS.
                                DEFPNT: BLOCK   2               ;POINTER USED IN FUNCTION DEFINITION.
                                GRBPNT= DEFPNT                  ;ANOTHER USED IN GARBAGE COLLECTION.
                                DSCPNT: BLOCK   2               ;POINTER TO A STRING DESCRIPTOR.
                                IFN     ADDPRC,<BLOCK   1>      ;FOR TEMPF3.
                                FOUR6:  EXP     STRSIZ          ;VARIABLE CONSTANT USED BY GARB COLLECT.
                                
                                ; --- ET CETERA ---:
                                JMPER:  JMP     60000
                                SIZE=   JMPER+1
                                OLDOV=  JMPER+2                 ;THE OLD OVERFLOW.
                                TEMPF3= DEFPNT                  ;A THIRD FAC TEMPORARY (4 BYTES).
                                TEMPF1:
                                IFN     ADDPRC,<0>              ;FOR TEMPF1S EXTRA BYTE.
                                HIGHDS: BLOCK   2               ;DESINATION OF HIGHEST ELEMENT IN BLT.
                                HIGHTR: BLOCK   2               ;SOURCE OF HIGHEST ELEMENT TO MOVE.
                                TEMPF2:
                                IFN     ADDPRC,<0>              ;FOR TEMPF2S EXTRA BYTE.
                                LOWDS:  BLOCK   2               ;LOCATION OF LAST BYTE TRANSFERRED INTO.
                                LOWTR:  BLOCK   2               ;LAST THING TO MOVE IN BLT.
                                ARYPNT= HIGHDS                  ;A POINTER USED IN ARRAY BUILDING.
                                GRBTOP= LOWTR                   ;A POINTER USED IN GARBAGE COLLECTION.
                                DECCNT= LOWDS                   ;NUMBER OF PLACES BEFORE DECIMAL POINT.
                                TENEXP= LOWDS+1                 ;HAS A DPT BEEN INPUT?
                                DPTFLG= LOWTR                   ;BASE TEN EXPONENT.
                                EXPSGN= LOWTR+1                 ;SIGN OF BASE TEN EXPONENT.
                                
                                ; --- THE FLOATING ACCUMULATOR ---:
                                FAC:
                                FACEXP: 0
                                FACHO:  0                       ;MOST SIGNIFICANT BYTE OF MANTISSA.
                                IFN     ADDPRC,<
                                FACMOH: 0>                      ;ONE MORE.
                                FACMO:  0                       ;MIDDLE ORDER OF MANTISSA.
                                FACLO:  0                       ;LEAST SIG BYTE OF MANTISSA.
                                FACSGN: 0                       ;SIGN OF FAC (0 OR -1) WHEN UNPACKED.
                                SGNFLG: 0                       ;SIGN OF FAC IS PRESERVED BERE BY "FIN".
                                DEGREE= SGNFLG                  ;A COUNT USED BY POLYNOMIALS.
                                DSCTMP= FAC                     ;THIS IS WHERE TEMP DESCS ARE BUILT.
                                INDICE= FACMO                   ;INDICE IS SET UP HERE BY "QINT".
                                BITS:   0                       ;SOMETHING FOR "SHIFTR" TO USE.
                                
                                ; --- THE FLOATING ARGUMENT (UNPACKED) ---:
                                ARGEXP: 0
                                ARGHO:  0
                                IFN     ADDPRC,<ARGMOH: 0>
                                ARGMO:  0
                                ARGLO:  0
                                ARGSGN: 0
                                
                                ARISGN: 0                       ;A SIGN REFLECTING THE RESULT.
                                FACOV:  0                       ;OVERFLOW BYTE OF THE FAC.
                                STRNG1= ARISGN                  ;POINTER TO A STRING OR DESCRIPTOR.
                                
                                FBUFPT: BLOCK   2               ;POINTER INTO FBUFFR USED BY FOUT.
                                BUFPTR= FBUFPT                  ;POINTER TO BUF USED BY "CRUNCH".
                                STRNG2= FBUFPT                  ;POINTER TO STRING OR DESC.
                                POLYPT= FBUFPT                  ;POINTER INTO POLYNOMIAL COEFFICIENTS.
                                CURTOL= FBUFPT                  ;ABSOLUTE LINEAR INDEX IS FORMED HERE.
                                PAGE
                                SUBTTL  RAM CODE.
                                ; THIS CODE GETS CHANGED THROUGHOUT EXECUTION.
                                ; IT IS MADE TO BE FAST THIS WAY.
                                ; ALSO, [X] AND [Y] ARE NOT DISTURBED
                                ;
                                ; "CHRGET" USING [TXTPTR] AS THE CURRENT TEXT PNTR
                                ; FETCHES A NEW CHARACTER INTO ACCA AFTER INCREMENTING [TXTPTR]
                                ; AND SETS CONDITION CODES ACCORDING TO WHAT'S IN ACCA.
                                ;       NOT C=  NUMERIC   ("0" THRU "9")
                                ;       Z=      ":" OR END-OF-LINE (A NULL)
                                ;
                                ; [ACCA] = NEW CHAR.
                                ; [TXTPTR]=[TXTPTR]+1
                                ;
                                ; THE FOLLOWING EXISTS IN ROM IF ROM EXISTS AND IS LOADED
                                ; DOWN HERE BY INIT. OTHERWISE IT IS JUST LOADED INTO THIS
                                ; RAM LIKE ALL THE REST OF RAM IS LOADED.
                                ;
                                CHRGET: INC     CHRGET+7        ;INCREMENT THE WHOLE TXTPTR.
                                        BNE     CHRGOT
                                        INC     CHRGET+8
                                CHRGOT: LDA     60000           ;A LOAD WITH AN EXT ADDR.
                                TXTPTR= CHRGOT+1
                                        CMPI    " "             ;SKIP SPACES.
                                        BEQ     CHRGET
                                QNUM:   CMPI    ":"             ;IS IT A ":"?
                                        BCS     CHRRTS          ;IT IS .GE. ":"
                                        SEC
                                        SBCI    "0"             ;ALL CHARS .GT. "9" HAVE RET'D SO
                                        SEC
                                        SBCI    256-"0"         ;SEE IF NUMERIC.
                                                                ;TURN CARRY ON IF NUMERIC.
                                                                ;ALSO, SETZ IF NULL.
                                CHRRTS: RTS                     ;RETURN TO CALLER.
                                
                                RNDX:   128                     ;LOADED OR FROM ROM.
                                        79                      ;THE INITIAL RANDOM NUMBER.
                                        199
                                        82
                                IFN     ADDPRC,<89>             ;ONE MORE BYTE.
                                
                                ORG     255                     ;PAGE 1 STUFF COMING UP.
                                LOFBUF: BLOCK   1               ;THE LOW FAC BUFFER. COPYABLE.
                                ;---  PAGE ZERO/ONE BOUNDARY ---.
                                                                ;MUST HAVE 13 CONTIGUOUS BYTES.
                                FBUFFR: BLOCK   3*ADDPRC+13     ;BUFFER FOR "FOUT".
                                                                ;ON PAGE 1 SO THAT STRING IS NOT COPIED.
                                
                                ;STACK IS LOCATED HERE. IE FROM THE END OF FBUFFR TO STKEND.
.:A000 94 E3                    
.:A002 7B E3                    
.:A004 43 42 4D 42 41 53 49 43  
                                PAGE
                                SUBTTL  DISPATCH TABLES, RESERVED WORDS, AND ERROR TEXTS.
                                
                                        ORG     ROMLOC
                                
.:A00C 30 A8                    STMDSP: ADR(END-1)
.:A00E 41 A7                            ADR(FOR-1)
.:A010 1D AD                            ADR(NEXT-1)
.:A012 F7 A8                            ADR(DATA-1)
                                IFN     EXTIO,<
.:A014 A4 AB                            ADR(INPUTN-1)>
.:A016 BE AB                            ADR(INPUT-1)
.:A018 80 B0                            ADR(DIM-1)
.:A01A 05 AC                            ADR(READ-1)
.:A01C A4 A9                            ADR(LET-1)
.:A01E 9F A8                            ADR(GOTO-1)
.:A020 70 A8                            ADR(RUN-1)
.:A022 27 A9                            ADR(IF-1)
.:A024 1C A8                            ADR(RESTORE-1)
.:A026 82 A8                            ADR(GOSUB-1)
.:A028 D1 A8                            ADR(RETURN-1)
.:A02A 3A A9                            ADR(REM-1)
.:A02C 2E A8                            ADR(STOP-1)
.:A02E 4A A9                            ADR(ONGOTO-1)
                                IFN     NULCMD,<
                                        ADR(NULL-1)>
.:A030 2C B8                            ADR(FNWAIT-1)
                                IFN     DISKO,<
                                IFE     REALIO-3,<
.:A032 67 E1                            ADR(CQLOAD-1)
.:A034 55 E1                            ADR(CQSAVE-1)
.:A036 64 E1                            ADR(CQVERF-1)>
                                IFN     REALIO,<
                                IFN     REALIO-2,<
                                IFN     REALIO-3,<
                                IFN     REALIO-5,<
                                        ADR(LOAD-1)
                                        ADR(SAVE-1)>>>>
                                IFN     REALIO-1,<
                                IFN     REALIO-3,<
                                IFN     REALIO-4,<
                                        ADR(511)                ;ADDRESS OF LOAD
                                        ADR(511)>>>>            ;ADDRESS OF SAVE
.:A038 B2 B3                            ADR(DEF-1)
.:A03A 23 B8                            ADR(POKE-1)
                                IFN     EXTIO,<
.:A03C 7F AA                            ADR(PRINTN-1)>
.:A03E 9F AA                            ADR(PRINT-1)
.:A040 56 A8                            ADR(CONT-1)
                                IFE     REALIO,<
                                        ADR(DDT-1)>
.:A042 9B A6                            ADR(LIST-1)
.:A044 5D A6                            ADR(CLEAR-1)
                                IFN     EXTIO,<
.:A046 85 AA                            ADR(CMD-1)
.:A048 29 E1                            ADR(CQSYS-1)
.:A04A BD E1                            ADR(CQOPEN-1)
.:A04C C6 E1                            ADR(CQCLOS-1)>
                                IFN     GETCMD,<
.:A04E 7A AB                            ADR(GET-1)>             ;FILL W/ GET ADDR.
.:A050 41 A6                            ADR(SCRATH-1)
                                
.:A052 39 BC                    FUNDSP: ADR(SGN)
.:A054 CC BC                            ADR(INT)
.:A056 58 BC                            ADR(ABS)
                                IFE     ROMSW,<
                                USRLOC: ADR(FCERR)>             ;INITIALLY NO USER ROUTINE.
                                IFN     ROMSW,<
.:A058 10 03                    USRLOC: ADR(USRPOK)>
.:A05A 7D B3                            ADR(FRE)
.:A05C 9E B3                            ADR(POS)
.:A05E 71 BF                            ADR(SQR)
.:A060 97 E0                            ADR(RND)
.:A062 EA B9                            ADR(LOG)
.:A064 ED BF                            ADR(EXP)
                                IFN     KIMROM,<
                                REPEAT  4,<
                                        ADR(FCERR)>>
                                IFE     KIMROM,<
.:A066 64 E2                    COSFIX: ADR(COS)
.:A068 6B E2                    SINFIX: ADR(SIN)
.:A06A B4 E2                    TANFIX: ADR(TAN)
.:A06C 0E E3                    ATNFIX: ADR(ATN)>
.:A06E 0D B8                            ADR(PEEK)
.:A070 7C B7                            ADR(LEN)
.:A072 65 B4                            ADR(STR)
.:A074 AD B7                            ADR(VAL)
.:A076 8B B7                            ADR(ASC)
.:A078 EC B6                            ADR(CHR)
.:A07A 00 B7                            ADR(LEFT)
.:A07C 2C B7                            ADR(RIGHT)
.:A07E 37 B7                            ADR(MID)
.:A080 79                       OPTAB:  121
.:A081 69 B8                            ADR(FADDT-1)
.:A083 79                               121
.:A084 52 B8                            ADR(FSUBT-1)
.:A086 7B                               123
.:A087 2A BA                            ADR(FMULTT-1)
.:A089 7B                               123
.:A08A 11 BB                            ADR(FDIVT-1)
.:A08C 7F                               127
.:A08D 7A BF                            ADR(FPWRT-1)
.:A08F 50                               80
.:A090  E8 AF                           ADR(ANDOP-1)
.:A092 46                               70
.:A093 E5 AF                            ADR(OROP-1)
.:A095 7D                       NEGTAB: 125
.:A096 B3 BF                            ADR(NEGOP-1)
.:A098 5A                       NOTTAB: 90
.:A099 D3 AE                            ADR(NOTOP-1)
.:A09B 64                       PTDORL: 100                     ;PRECEDENCE.
.:A09C 15 B0                            ADR     (DOREL-1)       ;OPERATOR ADDRESS.
                                ;
                                ; TOKENS FOR RESERVED WORDS ALWAYS HAVE THE MOST
                                ; SIGNIFICANT BIT ON.
                                ; THE LIST OF RESERVED WORDS:
                                ;
                                Q=128-1
                                DEFINE  DCI(A),<Q=Q+1
                                        DC(A)>
.:A09E 45 4E                    RESLST: DCI"END"
.:A0A0 C4 46 4F D2 4E 45 58 D4          ENDTK==Q
.:A0A8 44 41 54 C1 49 4E 50 55          DCI"FOR"
.:A0B0 54 A3 49 4E 50 55 D4 44          FORTK==Q
.:A0B8 49 CD 52 45 41 C4 4C 45          DCI"NEXT"
.:A0C0 D4 47 4F 54 CF 52 55 CE          DCI"DATA"
.:A0C8 49 C6 52 45 53 54 4F 52          DATATK==Q
.:A0D0 C5 47 4F 53 55 C2 52 45  IFN     EXTIO,<
.:A0D8 54 55 52 CE 52 45 CD 53          DCI"INPUT#">
.:A0E0 54 4F D0 4F CE 57 41 49          DCI"INPUT"
.:A0E8 D4 4C 4F 41 C4 53 41 56          DCI"DIM"
.:A0F0 C5 56 45 52 49 46 D9 44          DCI"READ"
.:A0F8 45 C6 50 4F 4B C5 50 52          DCI"LET"
.:A100 49 4E 54 A3 50 52 49 4E          DCI"GOTO"
.:A108 D4 43 4F 4E D4 4C 49 53          GOTOTK==Q
.:A110 D4 43 4C D2 43 4D C4 53          DCI"RUN"
.:A118 59 D3 4F 50 45 CE 43 4C          DCI"IF"
.:A120 4F 53 C5 47 45 D4 4E 45          DCI"RESTORE"
.:A128 D7 54 41 42 A8 54 CF 46          DCI"GOSUB"
.:A130 CE 53 50 43 A8 54 48 45          GOSUTK=Q
.:A138 CE 4E 4F D4 53 54 45 D0          DCI"RETURN"
.:A140 AB AD AA AF DE 41 4E C4          DCI"REM"
.:A148 4F D2 BE BD BC 53 47 CE          REMTK=Q
.:A150 49 4E D4 41 42 D3 55 53          DCI"STOP"
.:A158 D2 46 52 C5 50 4F D3 53          DCI"ON"
.:A160 51 D2 52 4E C4 4C 4F C7  IFN     NULCMD,<
.:A168 45 58 D0 43 4F D3 53 49          DCI"NULL">
.:A170 CE 54 41 CE 41 54 CE 50          DCI"WAIT"
.:A178 45 45 CB 4C 45 CE 53 54  IFN     DISKO,<
.:A180 52 A4 56 41 CC 41 53 C3          DCI"LOAD"
.:A188 43 48 52 A4 4C 45 46 54          DCI"SAVE"
.:A190 A4 52 49 47 48 54 A4 4D  IFE     REALIO-3,<
.:A198 49 44 A4 47 CF 00                DCI"VERIFY">>
.:A1A0 54 4F                            DCI"DEF"
                                        DCI"POKE"
                                IFN     EXTIO,<
                                        DCI"PRINT#">
                                        DCI"PRINT"
                                        PRINTK==Q
                                        DCI"CONT"
                                IFE     REALIO,<
                                        DCI"DDT">
                                        DCI"LIST"
                                IFN     REALIO-3,<
                                        DCI"CLEAR">
                                IFE     REALIO-3,<
                                        DCI"CLR">
                                IFN     EXTIO,<
                                        DCI"CMD"
                                        DCI"SYS"
                                        DCI"OPEN"
                                        DCI"CLOSE">
                                IFN     GETCMD,<
                                        DCI"GET">
                                        DCI"NEW"
                                        SCRATK=Q
                                ; END OF COMMAND LIST.
                                        "T"
                                        "A"
                                        "B"
                                        "("+128
                                        Q=Q+1
                                        TABTK=Q
                                        DCI"TO"
                                        TOTK==Q
                                        DCI"FN"
                                        FNTK==Q
                                        "S"
                                        "P"
                                        "C"
                                        "("+128                 ;MACRO DOESNT LIKE ('S IN ARGUMENTS.
                                        Q=Q+1
                                        SPCTK==Q
                                        DCI"THEN"
                                        THENTK=Q
                                        DCI"NOT"
                                        NOTTK==Q
                                        DCI"STEP"
                                        STEPTK=Q
                                        DCI"+"
                                        PLUSTK=Q
                                        DCI"-"
                                        MINUTK=Q
                                        DCI"*"
                                        DCI"/"
                                        DCI"^"
                                        DCI"AND"
                                        DCI"OR"
                                        190                     ;A GREATER THAN SIGN
                                        Q=Q+1
                                        GREATK=Q
                                        DCI"="
                                        EQULTK=Q
                                        188
                                        Q=Q+1                   ;A LESS THAN SIGN
                                        LESSTK=Q
                                ;
                                ; NOTE DANGER OF ONE RESERVED WORD BEING A PART
                                ; OF ANOTHER:
                                ; IE . . IF 2 GREATER THAN F OR T=5 THEN...
                                ; WILL NOT WORK!!! SINCE "FOR" WILL BE CRUNCHED!!
                                ; IN ANY CASE MAKE SURE THE SMALLER WORD APPEARS
                                ; SECOND IN THE RESERVED WORD TABLE ("INP" AND "INPUT")
                                ; ANOTHER EXAMPLE: IF T OR Q THEN ... "TO" IS CRUNCHED
                                ;
                                        DCI"SGN"
                                        ONEFUN=Q
                                        DCI"INT"
                                        DCI"ABS"
                                        DCI"USR"
                                        DCI"FRE"
                                        DCI"POS"
                                        DCI"SQR"
                                        DCI"RND"
                                        DCI"LOG"
                                        DCI"EXP"
                                        DCI"COS"
                                        DCI"SIN"
                                        DCI"TAN"
                                        DCI"ATN"
                                        DCI"PEEK"
                                        DCI"LEN"
                                        DCI"STR$"
                                        DCI"VAL"
                                        DCI"ASC"
                                        DCI"CHR$"
                                LASNUM==Q                       ;NUMBER OF LAST FUNCTION
                                                                ;THAT TAKES ONE ARG
                                        DCI"LEFT$"
                                        DCI"RIGHT$"
                                        DCI"MID$"
                                        DCI"GO"
                                GOTK==Q
                                        0                       ;MARKS END OF RESERVED WORD LIST
                                
                                IFE LNGERR,<
                                Q=0-2
                                DEFINE  DCE(X),<Q=Q+2
                                        DC(X)>
                                ERRTAB: DCE"NF"
                                        ERRNF==Q                ;NEXT WITHOUT FOR.
                                        DCE"SN"
                                        ERRSN==Q                ;SYNTAX
                                        DCE"RG"
                                        ERRRG==Q                ;RETURN WITHOUT GOSUB.
                                        DCE"OD"
                                        ERROD==Q                ;OUT OF DATA.
                                        DCE"FC"
                                        ERRFC==Q                ;ILLEGAL QUANTITY.
                                        DCE"OV"
                                        ERROV==Q                ;OVERFLOW.
                                        DCE"OM"
                                        ERROM==Q                ;OUT OF MEMORY.
                                        DCE"US"
                                        ERRUS==Q                ;UNDEFINED STATEMENT.
                                        DCE"BS"
                                        ERRBS==Q                ;BAD SUBSCRIPT.
                                        DCE"DD"
                                        ERRDD==Q                ;REDIMENSIONED ARRAY.
                                        DCE"/0"
                                        ERRDV0==Q               ;DIVISION BY ZERO.
                                        DCE"ID"
                                        ERRID==Q                ;ILLEGAL DIRECT.
                                        DCE"TM"
                                        ERRTM==Q                ;TYPE MISMATCH.
                                        DCE"LS"
                                        ERRLS==Q                ;STRING TOO LONG.
                                IFN     EXTIO,<
                                        DCE"FD"                 ;FILE DATA.
                                        ERRBD==Q>
                                        DCE"ST"
                                        ERRST==Q                ;STRING FORMULA TOO COMPLEX.
                                        DCE"CN"
                                        ERRCN==Q                ;CAN'T CONTINUE.
                                        DCE"UF"
                                        ERRUF==Q>               ;UNDEFINED FUNCTION.
                                
                                IFN LNGERR,<
                                Q=0
                                ; NOTE: THIS ERROR COUNT TECHNIQUE WILL NOT WORK IF THERE ARE MORE
                                ; THAN 256 CHARACTERS OF ERROR MESSAGES
.:A1A0 4F 20 4D 41 4E 59 20 46  ERRTAB: DC"NEXT WITHOUT FOR"
.:A1A8 49 4C 45 D3 46 49 4C 45          ERRNF==Q
.:A1B0 20 4F 50 45 CE 46 49 4C          Q=Q+16
.:A1B8 45 20 4E 4F 54 20 4F 50          DC"SYNTAX"
.:A1C0 45 CE 46 49 4C 45 20 4E          ERRSN==Q
.:A1C8 4F 54 20 46 4F 55 4E C4          Q=Q+6
.:A1D0 44 45 56 49 43 45 20 4E          DC"RETURN WITHOUT GOSUB"
.:A1D8 4F 54 20 50 52 45 53 45          ERRRG==Q
.:A1E0 4E D4 4E 4F 54 20 49 4E          Q=Q+20
.:A1E8 50 55 54 20 46 49 4C C5          DC"OUT OF DATA"
.:A1F0 4E 4F 54 20 4F 55 54 50          ERROD==Q
.:A1F8 55 54 20 46 49 4C C5 4D          Q=Q+11
.:A200 49 53 53 49 4E 47 20 46          DC"ILLEGAL QUANTITY"
.:A208 49 4C 45 20 4E 41 4D C5          ERRFC==Q
.:A210 49 4C 4C 45 47 41 4C 20          Q=Q+16
.:A218 44 45 56 49 43 45 20 4E          DC"OVERFLOW"
.:A220 55 4D 42 45 D2 4E 45 58          ERROV==Q
.:A228 54 20 57 49 54 48 4F 55          Q=Q+8
.:A230 54 20 46 4F D2 53 59 4E          DC"OUT OF MEMORY"
.:A238 54 41 D8 52 45 54 55 52          ERROM==Q
.:A240 4E 20 57 49 54 48 4F 55          Q=Q+13
.:A248 54 20 47 4F 53 55 C2 4F          DC"UNDEF'D STATEMENT"
.:A250 55 54 20 4F 46 20 44 41          ERRUS==Q
.:A258 54 C1 49 4C 4C 45 47 41          Q=Q+17
.:A260 4C 20 51 55 41 4E 54 49          DC"BAD SUBSCRIPT"
.:A268 54 D9 4F 56 45 52 46 4C          ERRBS==Q
.:A270 4F D7 4F 55 54 20 4F 46          Q=Q+13
.:A278 20 4D 45 4D 4F 52 D9 55          DC"REDIM'D ARRAY"
.:A280 4E 44 45 46 27 44 20 53          ERRDD==Q
.:A288 54 41 54 45 4D 45 4E D4          Q=Q+13
.:A290 42 41 44 20 53 55 42 53          DC"DIVISION BY ZERO"
.:A298 43 52 49 50 D4 52 45 44          ERRDV0==Q
.:A2A0 49 4D 27 44 20 41 52 52          Q=Q+16
.:A2A8 41 D9 44 49 56 49 53 49          DC"ILLEGAL DIRECT"
.:A2B0 4F 4E 20 42 59 20 5A 45          ERRID==Q
.:A2B8 52 CF 49 4C 4C 45 47 41          Q=Q+14
.:A2C0 4C 20 44 49 52 45 43 D4          DC"TYPE MISMATCH"
.:A2C8 54 59 50 45 20 4D 49 53          ERRTM==Q
.:A2D0 4D 41 54 43 C8 53 54 52          Q=Q+13
.:A2D8 49 4E 47 20 54 4F 4F 20          DC"STRING TOO LONG"
.:A2E0 4C 4F 4E C7 46 49 4C 45          ERRLS==Q
.:A2E8 20 44 41 54 C1 46 4F 52          Q=Q+15
.:A2F0 4D 55 4C 41 20 54 4F 4F  IFN     EXTIO,<
.:A2F8 20 43 4F 4D 50 4C 45 D8          DC"FILE DATA"
.:A300 43 41 4E 27 54 20 43 4F          ERRBD==Q
.:A308 4E 54 49 4E 55 C5 55 4E          Q=Q+9>
.:A310 44 45 46 27 44 20 46 55          DC"FORMULA TOO COMPLEX"
.:A318 4E 43 54 49 4F CE 56 45          ERRST==Q
.:A320 52 49 46 D9 4C 4F 41 C4          Q=Q+19
                                        DC"CAN'T CONTINUE"
                                        ERRCN==Q
                                        Q=Q+14
                                        DC"UNDEF'D FUNCTION"
                                        ERRUF==Q>
                                
.:A328 9E A1 AC A1 B5 A1 C2 A1  
.:A330 D0 A1 E2 A1 F0 A1 FF A1  
.:A338 10 A2 25 A2 35 A2 3B A2  
.:A340 4F A2 5A A2 6A A2 72 A2  
.:A348 7F A2 90 A2 9D A2 AA A2  
.:A350 BA A2 C8 A2 D5 A2 E4 A2  
.:A358 ED A2 00 A3 0E A3 1E A3  
.:A360 24 A3 83 A3              
                                
                                ;
                                ; NEEDED FOR MESSAGES IN ALL VERSIONS.
                                ;
.:A364 0D 4F 4B 0D              ERR:    DT" ERROR"
.:A368 00 20 20 45 52 52 4F 52          0
.:A370 00 20 49 4E 20 00 0D 0A  INTXT:  DT" IN "
.:A378 52 45 41 44 59 2E 0D 0A          0
.:A380 00 0D 0A 42 52 45 41 4B  REDDY:  ACRLF
.:A388 00 A0                    IFE REALIO-3,<
                                        DT"READY.">
                                IFN REALIO-3,<
                                        DT"OK">
                                        ACRLF
                                        0
                                BRKTXT: ACRLF
                                        DT"BREAK"
                                        0
                                PAGE
                                SUBTTL  GENERAL STORAGE MANAGEMENT ROUTINES.
                                ;
                                ; FIND A "FOR" ENTRY ON THE STACK VIA "VARPNT".
                                ;
                                FORSIZ==2*ADDPRC+16
.,A38A BA       TSX             FNDFOR: TSX                     ;LOAD XREG WITH STK PNTR.
.,A38B E8       INX                     REPEAT  4,<INX>         ;IGNORE ADR(NEWSTT) AND RTS ADDR.
.,A38C E8       INX             
.,A38D E8       INX             
.,A38E E8       INX             
.,A38F BD 01 01 LDA $0101,X     FFLOOP: LDA     257,X           ;GET STACK ENTRY.
.,A392 C9 81    CMP #$81                CMPI    FORTK           ;IS IT A "FOR" TOKEN?
.,A394 D0 21    BNE $A3B7               BNE     FFRTS           ;NO, NO "FOR" LOOPS WITH THIS PNTR.
.,A396 A5 4A    LDA $4A                 LDA     FORPNT+1        ;GET HIGH.
.,A398 D0 0A    BNE $A3A4               BNE     CMPFOR
.,A39A BD 02 01 LDA $0102,X             LDA     258,X           ;PNTR IS ZERO, SO ASSUME THIS ONE.
.,A39D 85 49    STA $49                 STA     FORPNT
.,A39F BD 03 01 LDA $0103,X             LDA     259,X
.,A3A2 85 4A    STA $4A                 STA     FORPNT+1
.,A3A4 DD 03 01 CMP $0103,X     CMPFOR: CMP     259,X
.,A3A7 D0 07    BNE $A3B0               BNE     ADDFRS          ;NOT THIS ONE.
.,A3A9 A5 49    LDA $49                 LDA     FORPNT          ;GET DOWN.
.,A3AB DD 02 01 CMP $0102,X             CMP     258,X
.,A3AE F0 07    BEQ $A3B7               BEQ     FFRTS           ;WE GOT IT! WE GOT IT!
.,A3B0 8A       TXA             ADDFRS: TXA
.,A3B1 18       CLC                     CLC                     ;ADD 16 TO X.
.,A3B2 69 12    ADC #$12                ADCI    FORSIZ
.,A3B4 AA       TAX                     TAX                     ;RESULT BACK INTO X.
.,A3B5 D0 D8    BNE $A38F               BNE     FFLOOP
.,A3B7 60       RTS             FFRTS:  RTS                     ;RETURN TO CALLER.
                                
                                ;
                                ; THIS IS THE BLOCK TRANSFER ROUTINE.
                                ; IT MAKES SPACE BY SHOVING EVERYTHING FORWARD.
                                ;
                                ; ON ENTRY:
                                ; [Y,A]=[HIGHDS]    (FOR REASON).
                                ; [HIGHDS]= DESTINATION OF [HIGH ADDRESS].
                                ; [LOWTR]= LOWEST ADDR TO BE TRANSFERRED.
                                ; [HIGHTR]= HIGHEST ADDR TO BE TRANSFERRED.
                                ;
                                ; A CHECK IS MADE TO ASCERTAIN THAT A REASONABLE
                                ; AMOUNT OF SPACE REMAINS BETWEEN THE BOTTOM
                                ; OF THE STRINGS AND THE HIGHEST LOCATION TRANSFERRED INTO.
                                ;
                                ; ON EXIT:
                                ; [LOWTR] ARE UNCHANGED.
                                ; [HIGHTR]=[LOWTR]-200 OCTAL.
                                ; [HIGHDS]=LOWEST ADDR TRANSFERRED INTO MINUS 200 OCTAL.
                                ;
.,A3B8 20 08 A4 JSR $A408       BLTU:   JSR     REASON          ;ASCERTAIN THAT STRING SPACE WON'T
                                                                ;BE OVERRUN.
.,A3BB 85 31    STA $31                 STWD    STREND
.,A3BD 84 32    STY $32         
.,A3BF 38       SEC             BLTUC:  SEC                     ;PREPARE TO SUBTRACT.
.,A3C0 A5 5A    LDA $5A                 LDA     HIGHTR
.,A3C2 E5 5F    SBC $5F                 SBC     LOWTR           ;COMPUTE NUMBER OF THINGS TO MOVE.
.,A3C4 85 22    STA $22                 STA     INDEX           ;SAVE FOR LATER.
.,A3C6 A8       TAY                     TAY
.,A3C7 A5 5B    LDA $5B                 LDA     HIGHTR+1
.,A3C9 E5 60    SBC $60                 SBC     LOWTR+1
.,A3CB AA       TAX                     TAX                     ;PUT IT IN A COUNTER REGISTER.
.,A3CC E8       INX                     INX                     ;SO THAT COUNTER ALGORITHM WORKS.
.,A3CD 98       TYA                     TYA                     ;SEE IF LOW PART OF COUNT IS ZERO.
.,A3CE F0 23    BEQ $A3F3               BEQ     DECBLT          ;YES, GO START MOVING BLOCKS.
.,A3D0 A5 5A    LDA $5A                 LDA     HIGHTR          ;NO, MUST MODIFY BASE ADDR.
.,A3D2 38       SEC                     SEC
.,A3D3 E5 22    SBC $22                 SBC     INDEX           ;BORROW IS OFF SINCE [HIGHTR].GT.[LOWTR].
.,A3D5 85 5A    STA $5A                 STA     HIGHTR          ;SAVE MODIFIED BASE ADDR.
.,A3D7 B0 03    BCS $A3DC               BCS     BLT1            ;IF NO BORROW, GO SHOVE IT.
.,A3D9 C6 5B    DEC $5B                 DEC     HIGHTR+1        ;BORROW IMPLIES SUB 1 FROM HIGH ORDER.
.,A3DB 38       SEC                     SEC
.,A3DC A5 58    LDA $58         BLT1:   LDA     HIGHDS          ;MOD BASE OF DEST ADDR.
.,A3DE E5 22    SBC $22                 SBC     INDEX
.,A3E0 85 58    STA $58                 STA     HIGHDS
.,A3E2 B0 08    BCS $A3EC               BCS     MOREN1          ;NO BORROW.
.,A3E4 C6 59    DEC $59                 DEC     HIGHDS+1        ;DECREMENT HIGH ORDER BYTE.
.,A3E6 90 04    BCC $A3EC               BCC     MOREN1          ;ALWAYS SKIP.
.,A3E8 B1 5A    LDA ($5A),Y     BLTLP:  LDADY   HIGHTR          ;FETCH BYTE TO MOVE
.,A3EA 91 58    STA ($58),Y             STADY   HIGHDS          ;MOVE IT IN, MOVE IT OUT.
.,A3EC 88       DEY             MOREN1: DEY
.,A3ED D0 F9    BNE $A3E8               BNE     BLTLP
.,A3EF B1 5A    LDA ($5A),Y             LDADY   HIGHTR          ;MOVE LAST OF THE BLOCK.
.,A3F1 91 58    STA ($58),Y             STADY   HIGHDS
.,A3F3 C6 5B    DEC $5B         DECBLT: DEC     HIGHTR+1
.,A3F5 C6 59    DEC $59                 DEC     HIGHDS+1        ;START ON NEW BLOCKS.
.,A3F7 CA       DEX                     DEX
.,A3F8 D0 F2    BNE $A3EC               BNE     MOREN1
.,A3FA 60       RTS                     RTS                     ;RETURN TO CALLER.
                                
                                ;
                                ; THIS ROUTINE IS USED TO ASCERTAIN THAT A GIVEN
                                ; NUMBER OF LOCS REMAIN AVAILABLE FOR THE STACK.
                                ;    THE CALL IS:
                                ;       LDAI    NUMBER OF 2-BYTE ENTRIES NEEDED.
                                ;       JSR     GETSTK
                                ;
                                ; THIS ROUTINE MUST BE CALLED BY ANY ROUTINE WHICH PUTS
                                ; AN ARBITRARY AMOUNT OF STUFF ON THE STACK,
                                ; I.E., ANY RECURSIVE ROUTINE LIKE "FRMEVL".
                                ; IT IS ALSO CALLED BY ROUTINES SUCH AS "GOSUB" AND "FOR"
                                ; WHICH MAKE PERMANENT ENTRIES ON THE STACK.
                                ;
                                ; ROUTINES WHICH MERELY USE AND FREE UP THE GUARANTEED
                                ; NUMLEV LOCATIONS NEED NOT CALL THIS.
                                ;
                                ;
                                ; ON EXIT:
                                ;    [A] AND [X] HAVE BEEN MODIFIED.
                                ;
.,A3FB 0A       ASL             GETSTK: ASL     A,              ;MULT [A] BY 2. NB, CLEARS C BIT.
.,A3FC 69 3E    ADC #$3E                ADCI    2*NUMLEV+<3*ADDPRC>+13  ;MAKE SURE 2*NUMLEV+13 LOCS
                                                                ;(13 BECAUSE OF FBUFFR)
.,A3FE B0 35    BCS $A435               BCS     OMERR           ;WILL REMAIN IN STACK.
.,A400 85 22    STA $22                 STA     INDEX
.,A402 BA       TSX                     TSX                     ;GET STACKED.
.,A403 E4 22    CPX $22                 CPX     INDEX           ;COMPARE.
.,A405 90 2E    BCC $A435               BCC     OMERR           ;IF STACK.LE.INDEX1, OM.
.,A407 60       RTS                     RTS
                                
                                ;
                                ; [Y,A] IS A CERTAIN ADDRESS. "REASON" MAKES SURE
                                ; IT IS LESS THAN [FRETOP].
                                ;
.,A408 C4 34    CPY $34         REASON: CPY     FRETOP+1
.,A40A 90 28    BCC $A434               BCC     REARTS
.,A40C D0 04    BNE $A412               BNE     TRYMOR          ;GO GARB COLLECT.
.,A40E C5 33    CMP $33                 CMP     FRETOP
.,A410 90 22    BCC $A434               BCC     REARTS
.,A412 48       PHA             TRYMOR: PHA
.,A413 A2 09    LDX #$09                LDXI    8+ADDPRC        ;IF TEMPF2 HAS ZERO IN BETWEEN.
.,A415 98       TYA                     TYA
.,A416 48       PHA             REASAV: PHA
.,A417 B5 57    LDA $57,X               LDA     HIGHDS-1,X      ;SAVE HIGHDS ON STACK.
.,A419 CA       DEX                     DEX
.,A41A 10 FA    BPL $A416               BPL     REASAV          ;PUT 8 OF THEM ON STK.
.,A41C 20 26 B5 JSR $B526               JSR     GARBA2          ;GO GARB COLLECT.
.,A41F A2 F7    LDX #$F7                LDXI    256-8-ADDPRC
.,A421 68       PLA             REASTO: PLA
.,A422 95 61    STA $61,X               STA     HIGHDS+8+ADDPRC,X       ;RESTORE AFTER GARB COLLECT.
.,A424 E8       INX                     INX
.,A425 30 FA    BMI $A421               BMI     REASTO
.,A427 68       PLA                     PLA
.,A428 A8       TAY                     TAY
.,A429 68       PLA                     PLA                     ;RESTORE A AND Y.
.,A42A C4 34    CPY $34                 CPY     FRETOP+1        ;COMPARE HIGHS
.,A42C 90 06    BCC $A434               BCC     REARTS
.,A42E D0 05    BNE $A435               BNE     OMERR           ;HIGHER IS BAD.
.,A430 C5 33    CMP $33                 CMP     FRETOP          ;AND THE LOWS.
.,A432 B0 01    BCS $A435               BCS     OMERR
.,A434 60       RTS             REARTS: RTS
                                
                                PAGE
                                SUBTTL  ERROR HANDLER, READY, TERMINAL INPUT, COMPACTIFY, NEW, REINIT.
.,A435 A2 10    LDX #$10        OMERR:  LDXI    ERROM
.,A437 6C 00 03 JMP ($0300)     ERROR:
.,A43A 8A       TXA             IFN     REALIO,<
.,A43B 0A       ASL                     LSR     CNTWFL>         ;FORCE OUTPUT.
.,A43C AA       TAX             IFN     EXTIO,<
.,A43D BD 26 A3 LDA $A326,X             LDA     CHANNL          ;CLOSE NON-TERMINAL CHANNEL.
.,A440 85 22    STA $22                 BEQ     ERRCRD
.,A442 BD 27 A3 LDA $A327,X             JSR     CQCCHN          ;CLOSE IT.
.,A445 85 23    STA $23                 LDAI    0
.,A447 20 CC FF JSR $FFCC               STA     CHANNL>
.,A44A A9 00    LDA #$00        
.,A44C 85 13    STA $13         
.,A44E 20 D7 AA JSR $AAD7       ERRCRD: JSR     CRDO            ;OUTPUT CRLF.
.,A451 20 45 AB JSR $AB45               JSR     OUTQST          ;PRINT A QUESTION MARK
                                IFE LNGERR,<
                                        LDA     ERRTAB,X,       ;GET FIRST CHR OF ERR MSG.
                                        JSR     OUTDO           ;OUTPUT IT.
                                        LDA     ERRTAB+1,X,     ;GET SECOND CHR.
                                        JSR     OUTDO>          ;OUTPUT IT.
.,A454 A0 00    LDY #$00        IFN LNGERR,<
.,A456 B1 22    LDA ($22),Y     GETERR: LDA     ERRTAB,X
.,A458 48       PHA                     PHA
.,A459 29 7F    AND #$7F                ANDI    127             ;GET RID OF HIGH BIT.
.,A45B 20 47 AB JSR $AB47               JSR     OUTDO           ;OUTPUT IT.
.,A45E C8       INY                     INX
.,A45F 68       PLA                     PLA                     ;LAST CHAR OF MESSAGE?
.,A460 10 F4    BPL $A456               BPL     GETERR>         ;NO. GO GET NEXT AND OUTPUT IT.
.,A462 20 7A A6 JSR $A67A       TYPERR: JSR     STKINI          ;RESET THE STACK AND FLAGS.
.,A465 A9 69    LDA #$69                LDWDI   ERR             ;GET PNTR TO " ERROR".
.,A467 A0 A3    LDY #$A3        
.,A469 20 1E AB JSR $AB1E       ERRFIN: JSR     STROUT          ;OUTPUT IT.
.,A46C A4 3A    LDY $3A                 LDY     CURLIN+1
.,A46E C8       INY                     INY                     ;WAS NUMBER 64000?
.,A46F F0 03    BEQ $A474               BEQ     READY           ;YES, DON'T TYPE LINE NUMBER.
.,A471 20 C2 BD JSR $BDC2               JSR     INPRT
                                READY:
                                IFN     REALIO,<
                                        LSR     CNTWFL>         ;TURN OUTPUT BACK ON IF SUPRESSED
.,A474 A9 76    LDA #$76                LDWDI   REDDY           ;SAY "OK".
.,A476 A0 A3    LDY #$A3        
                                IFN     REALIO-3,<
                                        JSR     RDYJSR>         ;OR GO TO INIT IF INIT ERROR.
                                IFE     REALIO-3,<
.,A478 20 1E AB JSR $AB1E               JSR     STROUT>         ;NO INIT ERRORS POSSIBLE.
.,A47B A9 80    LDA #$80        
.,A47D 20 90 FF JSR $FF90       
.,A480 6C 02 03 JMP ($0302)     
.,A483 20 60 A5 JSR $A560       MAIN:   JSR     INLIN           ;GET A LINE FROM TERMINAL.
.,A486 86 7A    STX $7A                 STXY    TXTPTR
.,A488 84 7B    STY $7B         
.,A48A 20 73 00 JSR $0073               JSR     CHRGET
.,A48D AA       TAX                     TAX                     ;SET ZERO FLAG BASED ON [A]
                                                                ;THIS DISTINGUISHES ":" AND 0
.,A48E F0 F0    BEQ $A480               BEQ     MAIN            ;IF BLANK LINE, GET ANOTHER.
.,A490 A2 FF    LDX #$FF                LDXI    255             ;SET DIRECT LINE NUMBER.
.,A492 86 3A    STX $3A                 STX     CURLIN+1
.,A494 90 06    BCC $A49C               BCC     MAIN1           ;IS A LINE NUMBER. NOT DIRECT.
.,A496 20 79 A5 JSR $A579               JSR     CRUNCH          ;COMPACTIFY.
.,A499 4C E1 A7 JMP $A7E1               JMP     GONE            ;EXECUTE IT.
.,A49C 20 6B A9 JSR $A96B       MAIN1:  JSR     LINGET          ;READ LINE NUMBER INTO "LINNUM".
.,A49F 20 79 A5 JSR $A579               JSR     CRUNCH
.,A4A2 84 0B    STY $0B                 STY     COUNT           ;RETAIN CHARACTER COUNT.
.,A4A4 20 13 A6 JSR $A613               JSR     FNDLIN
.,A4A7 90 44    BCC $A4ED               BCC     NODEL           ;NO MATCH, SO DON'T DELETE.
.,A4A9 A0 01    LDY #$01                LDYI    1
.,A4AB B1 5F    LDA ($5F),Y             LDADY   LOWTR
.,A4AD 85 23    STA $23                 STA     INDEX1+1
.,A4AF A5 2D    LDA $2D                 LDA     VARTAB
.,A4B1 85 22    STA $22                 STA     INDEX1
.,A4B3 A5 60    LDA $60                 LDA     LOWTR+1         ;SET TRANSFER TO.
.,A4B5 85 25    STA $25                 STA     INDEX2+1
.,A4B7 A5 5F    LDA $5F                 LDA     LOWTR
.,A4B9 88       DEY                     DEY
.,A4BA F1 5F    SBC ($5F),Y             SBCDY   LOWTR           ;COMPUTE NEGATIVE LENGTH.
.,A4BC 18       CLC                     CLC
.,A4BD 65 2D    ADC $2D                 ADC     VARTAB          ;COMPUTE NEW VARTAB.
.,A4BF 85 2D    STA $2D                 STA     VARTAB
.,A4C1 85 24    STA $24                 STA     INDEX2          ;SET LOW OF TRANS TO.
.,A4C3 A5 2E    LDA $2E                 LDA     VARTAB+1
.,A4C5 69 FF    ADC #$FF                ADCI    255
.,A4C7 85 2E    STA $2E                 STA     VARTAB+1        ;COMPUTE HIGH OF VARTAB.
.,A4C9 E5 60    SBC $60                 SBC     LOWTR+1         ;COMPUTE NUMBER OF BLOCKS TO MOVE.
.,A4CB AA       TAX                     TAX
.,A4CC 38       SEC                     SEC
.,A4CD A5 5F    LDA $5F                 LDA     LOWTR
.,A4CF E5 2D    SBC $2D                 SBC     VARTAB          ;COMPUTE OFFSET.
.,A4D1 A8       TAY                     TAY
.,A4D2 B0 03    BCS $A4D7               BCS     QDECT1          ;IF VARTAB.LE.LOWTR,
.,A4D4 E8       INX                     INX                     ;DECR DUE TO CARRY, AND
.,A4D5 C6 25    DEC $25                 DEC     INDEX2+1        ;DECREMENT STORE SO CARRY WORKS.
.,A4D7 18       CLC             QDECT1: CLC
.,A4D8 65 22    ADC $22                 ADC     INDEX1
.,A4DA 90 03    BCC $A4DF               BCC     MLOOP
.,A4DC C6 23    DEC $23                 DEC     INDEX1+1
.,A4DE 18       CLC                     CLC                     ;FOR LATER ADCQ
.,A4DF B1 22    LDA ($22),Y     MLOOP:  LDADY   INDEX1
.,A4E1 91 24    STA ($24),Y             STADY   INDEX2
.,A4E3 C8       INY                     INY
.,A4E4 D0 F9    BNE $A4DF               BNE     MLOOP           ;BLOCK DONE?
.,A4E6 E6 23    INC $23                 INC     INDEX1+1
.,A4E8 E6 25    INC $25                 INC     INDEX2+1
.,A4EA CA       DEX                     DEX
.,A4EB D0 F2    BNE $A4DF               BNE     MLOOP           ;DO ANOTHER BLOCK. ALWAYS.
.,A4ED 20 59 A6 JSR $A659       NODEL:  JSR     RUNC            ;RESET ALL VARIABLE INFO SO GARBAGE
                                                                ;COLLECTION CAUSED BY REASON WILL WORK
.,A4F0 20 33 A5 JSR $A533               JSR     LNKPRG          ;FIX UP THE LINKS
.,A4F3 AD 00 02 LDA $0200               LDA     BUF             ;SEE IF ANYTHNG THERE
.,A4F6 F0 88    BEQ $A480               BEQ     MAIN
.,A4F8 18       CLC                     CLC
.,A4F9 A5 2D    LDA $2D                 LDA     VARTAB
.,A4FB 85 5A    STA $5A                 STA     HIGHTR          ;SETUP HIGHTR.
.,A4FD 65 0B    ADC $0B                 ADC     COUNT           ;ADD LENGTH OF LINE TO INSERT.
.,A4FF 85 58    STA $58                 STA     HIGHDS          ;THIS GIVES DEST ADDR.
.,A501 A4 2E    LDY $2E                 LDY     VARTAB+1
.,A503 84 5B    STY $5B                 STY     HIGHTR+1        ;SAME FOR HIGH ORDERS.
.,A505 90 01    BCC $A508               BCC     NODELC
.,A507 C8       INY                     INY
.,A508 84 59    STY $59         NODELC: STY     HIGHDS+1
.,A50A 20 B8 A3 JSR $A3B8               JSR     BLTU
                                IFN     BUFPAG,<
.,A50D A5 14    LDA $14                 LDWD    LINNUM          ;POSITION THE BINARY LINE NUMBER
.,A50F A4 15    LDY $15         
.,A511 8D FE 01 STA $01FE               STWD    BUF-2>          ;IN FRONT OF BUF
.,A514 8C FF 01 STY $01FF       
.,A517 A5 31    LDA $31                 LDWD    STREND
.,A519 A4 32    LDY $32         
.,A51B 85 2D    STA $2D                 STWD    VARTAB
.,A51D 84 2E    STY $2E         
.,A51F A4 0B    LDY $0B                 LDY     COUNT
.,A521 88       DEY                     DEY
.,A522 B9 FC 01 LDA $01FC,Y     STOLOP: LDA     BUF-4,Y
.,A525 91 5F    STA ($5F),Y             STADY   LOWTR
.,A527 88       DEY                     DEY
.,A528 10 F8    BPL $A522               BPL     STOLOP
.,A52A 20 59 A6 JSR $A659       FINI:   JSR     RUNC            ;DO CLEAR & SET UP STACK.
                                                                ;AND SET [TXTPTR] TO [TXTTAB]-1.
.,A52D 20 33 A5 JSR $A533               JSR     LNKPRG          ;FIX UP PROGRAM LINKS
.,A530 4C 80 A4 JMP $A480               JMP     MAIN
.,A533 A5 2B    LDA $2B         LNKPRG: LDWD    TXTTAB          ;SET [INDEX] TO [TXTTAB].
.,A535 A4 2C    LDY $2C         
.,A537 85 22    STA $22                 STWD    INDEX
.,A539 84 23    STY $23         
.,A53B 18       CLC                     CLC
                                ;
                                ; CHEAD GOES THROUGH PROGRAM STORAGE AND FIXES
                                ; UP ALL THE LINKS. THE END OF EACH LINE IS FOUND
                                ; BY SEARCHING FOR THE ZERO AT THE END.
                                ; THE DOUBLE ZERO LINK IS USED TO DETECT THE END OF THE PROGRAM.
                                ;
.,A53C A0 01    LDY #$01        CHEAD:  LDYI    1
.,A53E B1 22    LDA ($22),Y             LDADY   INDEX           ;ARRIVED AT DOUBLE ZEROES?
.,A540 F0 1D    BEQ $A55F               BEQ     LNKRTS
.,A542 A0 04    LDY #$04                LDYI    4
.,A544 C8       INY             CZLOOP: INY                     ;THERE IS AT LEAST ONE BYTE.
.,A545 B1 22    LDA ($22),Y             LDADY   INDEX
.,A547 D0 FB    BNE $A544               BNE     CZLOOP          ;NO, CONTINUE SEARCHING.
.,A549 C8       INY                     INY                     ;GO ONE BEYOND.
.,A54A 98       TYA                     TYA
.,A54B 65 22    ADC $22                 ADC     INDEX
.,A54D AA       TAX                     TAX
.,A54E A0 00    LDY #$00                LDYI    0
.,A550 91 22    STA ($22),Y             STADY   INDEX
.,A552 A5 23    LDA $23                 LDA     INDEX+1
.,A554 69 00    ADC #$00                ADCI    0
.,A556 C8       INY                     INY
.,A557 91 22    STA ($22),Y             STADY   INDEX
.,A559 86 22    STX $22                 STX     INDEX
.,A55B 85 23    STA $23                 STA     INDEX+1
.,A55D 90 DD    BCC $A53C               BCCA    CHEAD           ;ALWAYS BRANCHES.
.,A55F 60       RTS             LNKRTS: RTS
                                ;
                                ; THIS IS THE LINE INPUT ROUTINE.
                                ; IT READS CHARACTERS INTO BUF USING BACKARROW (UNDERSCORE, OR
                                ; SHIFT O) AS THE DELETE CHARACTER AND @ AS THE
                                ; LINE DELETE CHARACTER. IF MORE THAN BUFLEN CHARACTERS
                                ; ARE TYPED, NO ECHOING IS DONE UNTIL A BACKARROW OR @ OR CR
                                ; IS TYPED. CONTROL-G WILL BE TYPED FOR EACH EXTRA CHARACTER.
                                ; THE ROUTINE IS ENTERED AT INLIN.
                                ;
                                IFE     REALIO-4,<
                                INLIN:  LDXI    128             ;NO PROMPT CHARACTER
                                        STX     CQPRMP
                                        JSR     CQINLN          ;GET A LINE ONTO PAGE 2
                                        CPXI    BUFLEN-1
                                        BCS     GDBUFS          ;NOT TOO MANY CHARACTERS
                                        LDXI    BUFLEN-1
                                GDBUFS: LDAI    0               ;PUT A ZERO AT THE END
                                        STA     BUF,X
                                        TXA
                                        BEQ     NOCHR
                                LOPBHT: LDA     BUF-1,X
                                        ANDI    127
                                        STA     BUF-1,X
                                        DEX
                                        BNE     LOPBHT
                                NOCHR:  LDAI    0
                                        LDXYI   <BUF-1>         ;POINT AT THE BEGINNING
                                        RTS>
                                IFN     REALIO-4,<
                                IFN     REALIO-3,<
                                LINLIN: IFE     REALIO-2,<
                                        JSR     OUTDO>          ;ECHO IT.
                                        DEX                     ;BACKARROW SO BACKUP PNTR AND
                                        BPL     INLINC          ;GET ANOTHER IF COUNT IS POSITIVE.
                                INLINN: IFE     REALIO-2,<
                                        JSR     OUTDO>          ;PRINT THE @ OR A SECOND BACKARROW
                                                                ;IF THERE WERE TOO MANY.
                                        JSR     CRDO>
.,A560 A2 00    LDX #$00        INLIN:  LDXI    0
.,A562 20 12 E1 JSR $E112       INLINC: JSR     INCHR           ;GET A CHARACTER.
                                IFN REALIO-3,<
                                        CMPI    7               ;IS IT BOB ALBRECHT RINGING THE BELL
                                                                ;FOR SCHOOL KIDS?
                                        BEQ     GOODCH>
.,A565 C9 0D    CMP #$0D                CMPI    13              ;CARRIAGE RETURN?
.,A567 F0 0D    BEQ $A576               BEQ     FININ1          ;YES, FINISH UP.
                                IFN     REALIO-3,<
                                        CMPI    32              ;CHECK FOR FUNNY CHARACTERS.
                                        BCC     INLINC
                                        CMPI    125             ;IS IT TILDA OR DELETE?
                                        BCS     INLINC          ;BIG BAD ONES TOO.
                                        CMPI    "@"             ;LINE DELETE?
                                        BEQ     INLINN          ;YES.
                                        CMPI    "_"             ;CHARACTER DELETE?
                                        BEQ     LINLIN>         ;YES.
                                GOODCH:
                                IFN     REALIO-3,<
                                        CPXI    BUFLEN-1        ;LEAVE ROOM FOR NULL.
                                                        ;COMMO ASSURES US NEVER MORE THAN BUFLEN.
                                        BCS     OUTBEL>
.,A569 9D 00 02 STA $0200,X             STA     BUF,X
.,A56C E8       INX                     INX
.,A56D E0 59    CPX #$59        IFE     REALIO-2,<SKIP2>
.,A56F 90 F1    BCC $A562       IFN     REALIO-2,<BNE INLINC>
.,A571 A2 17    LDX #$17        IFN REALIO-3,<
.,A573 4C 37 A4 JMP $A437       OUTBEL: LDAI    7
.,A576 4C CA AA JMP $AACA       IFN     REALIO,<
.,A579 6C 04 03 JMP ($0304)             JSR     OUTDO>          ;ECHO IT.
                                        BNE     INLINC>         ;CYCLE ALWAYS.
                                FININ1: JMP     FININL>         ;GO TO FININL FAR, FAR AWAY.
                                INCHR:
                                IFE     REALIO-3,<
                                        JSR     CQINCH>         ;FOR COMMODORE.
                                IFE     REALIO-2,<
                                INCHRL: LDA     ^O176000
                                        REPEAT  4,<NOP>
                                        LSR     A,
                                        BCC     INCHRL
                                        LDA     ^O176001        ;GET THE CHARACTER.
                                        REPEAT  4,<NOP>
                                        ANDI    127>
                                IFE     REALIO-1,<
                                        JSR     ^O17132>        ;1E5A FOR MOS TECH.
                                IFE     REALIO-4,<
                                        JSR     CQINCH          ;FD0C FOR APPLE COMPUTER.
                                        ANDI    127>
                                IFE     REALIO,<
                                        TJSR    INSIM##>        ;GET A CHARACTER FROM SIMULATOR
                                
                                IFN     REALIO,<
                                IFN     EXTIO,<
                                        LDY     CHANNL          ;CNT-O HAS NO EFFECT IF NOT FROM TERM.
                                        BNE     INCRTS>
                                        CMPI    CONTW           ;SUPPRESS OUTPUT CHARACTER (^W).
                                        BNE     INCRTS          ;NO, RETURN.
                                        PHA
                                        COM     CNTWFL          ;COMPLEMENT ITS STATE.
                                        PLA>
                                INCRTS: RTS                     ;END OF INCHR.
                                
                                ;
                                ; ALL "RESERVED" WORDS ARE TRANSLATED INTO SINGLE
                                ; BYTES WITH THE MSB ON. THIS SAVES SPACE AND TIME
                                ; BY ALLOWING FOR TABLE DISPATCH DURING EXECUTION.
                                ; THEREFORE ALL STATEMENTS APPEAR TOGETHER IN THE
                                ; RESERVED WORD LIST IN THE SAME ORDER THEY
                                ; APPEAR IN STMDSP.
                                ;
                                BUFOFS=0                        ;THE AMOUNT TO OFFSET THE LOW BYTE
                                                                ;OF THE TEXT POINTER TO GET TO BUF
                                                                ;AFTER TXTPTR HAS BEEN SETUP TO POINT INTO BUF
                                IFN     BUFPAG,<
                                BUFOFS=<BUF/256>*256>
.,A57C A6 7A    LDX $7A         CRUNCH: LDX     TXTPTR          ;SET SOURCE POINTER.
.,A57E A0 04    LDY #$04                LDYI    4               ;SET DESTINATION OFFSET.
.,A580 84 0F    STY $0F                 STY     DORES           ;ALLOW CRUNCHING.
.,A582 BD 00 02 LDA $0200,X     KLOOP:  LDA     BUFOFS,X
                                IFE     REALIO-3,<
.,A585 10 07    BPL $A58E               BPL     CMPSPC          ;GO LOOK AT SPACES.
.,A587 C9 FF    CMP #$FF                CMPI    PI              ;PI??
.,A589 F0 3E    BEQ $A5C9               BEQ     STUFFH          ;GO SAVE IT.
.,A58B E8       INX                     INX                     ;SKIP NO PRINTING.
.,A58C D0 F4    BNE $A582               BNE     KLOOP>          ;ALWAYS GOES.
.,A58E C9 20    CMP #$20        CMPSPC: CMPI    " "             ;IS IT A SPACE TO SAVE?
.,A590 F0 37    BEQ $A5C9               BEQ     STUFFH          ;YES, GO SAVE IT.
.,A592 85 08    STA $08                 STA     ENDCHR          ;IF IT'S A QUOTE, THIS WILL
                                                                ;STOP LOOP WHEN OTHER QUOTE APPEARS.
.,A594 C9 22    CMP #$22                CMPI    34              ;QUOTE SIGN?
.,A596 F0 56    BEQ $A5EE               BEQ     STRNG           ;YES, DO SPECIAL STRING HANDLING.
.,A598 24 0F    BIT $0F                 BIT     DORES           ;TEST FLAG.
.,A59A 70 2D    BVS $A5C9               BVS     STUFFH          ;NO CRUNCH, JUST STORE.
.,A59C C9 3F    CMP #$3F                CMPI    "?"             ;A QMARK?
.,A59E D0 04    BNE $A5A4               BNE     KLOOP1
.,A5A0 A9 99    LDA #$99                LDAI    PRINTK          ;YES, STUFF A "PRINT" TOKEN.
.,A5A2 D0 25    BNE $A5C9               BNE     STUFFH          ;ALWAYS GO TO STUFFH.
.,A5A4 C9 30    CMP #$30        KLOOP1: CMPI    "0"             ;SKIP NUMERICS.
.,A5A6 90 04    BCC $A5AC               BCC     MUSTCR
.,A5A8 C9 3C    CMP #$3C                CMPI    60              ;":" AND ";" ARE ENTERED STRAIGHTAWAY.
.,A5AA 90 1D    BCC $A5C9               BCC     STUFFH
.,A5AC 84 71    STY $71         MUSTCR: STY     BUFPTR          ;SAVE BUFFER POINTER.
.,A5AE A0 00    LDY #$00                LDYI    0               ;LOAD RESLST POINTER.
.,A5B0 84 0B    STY $0B                 STY     COUNT           ;ALSO CLEAR COUNT.
.,A5B2 88       DEY                     DEY
.,A5B3 86 7A    STX $7A                 STX     TXTPTR          ;SAVE TEXT POINTER FOR LATER USE.
.,A5B5 CA       DEX                     DEX
.,A5B6 C8       INY             RESER:  INY
.,A5B7 E8       INX             RESPUL: INX
.,A5B8 BD 00 02 LDA $0200,X     RESCON: LDA     BUFOFS,X
.,A5BB 38       SEC                     SEC                     ;PREPARE TO SUBSTARCT.
.,A5BC F9 9E A0 SBC $A09E,Y             SBC     RESLST,Y        ;CHARACTERS EQUAL?
.,A5BF F0 F5    BEQ $A5B6               BEQ     RESER           ;YES, CONTINUE SEARCH.
.,A5C1 C9 80    CMP #$80                CMPI    128             ;NO BUT MAYBE THE END IS HERE.
.,A5C3 D0 30    BNE $A5F5               BNE     NTHIS           ;NO, TRULY UNEQUAL.
.,A5C5 05 0B    ORA $0B                 ORA     COUNT
.,A5C7 A4 71    LDY $71         GETBPT: LDY     BUFPTR          ;GET BUFFER PNTR.
.,A5C9 E8       INX             STUFFH: INX
.,A5CA C8       INY                     INY
.,A5CB 99 FB 01 STA $01FB,Y             STA     BUF-5,Y
.,A5CE B9 FB 01 LDA $01FB,Y             LDA     BUF-5,Y
.,A5D1 F0 36    BEQ $A609               BEQ     CRDONE          ;NULL IMPLIES END OF LINE.
.,A5D3 38       SEC                     SEC                     ;PREPARE TO SUBSTARCT.
.,A5D4 E9 3A    SBC #$3A                SBCI    ":"             ;IS IT A ":"?
.,A5D6 F0 04    BEQ $A5DC               BEQ     COLIS           ;YES, ALLOW CRUNCHING AGAIN.
.,A5D8 C9 49    CMP #$49                CMPI    DATATK-":"      ;IS IT A DATATK?
.,A5DA D0 02    BNE $A5DE               BNE     NODATT          ;NO, SEE IF IT IS REM TOKEN.
.,A5DC 85 0F    STA $0F         COLIS:  STA     DORES           ;SETUP FLAG.
.,A5DE 38       SEC             NODATT: SEC                     ;PREP TO SBCQ
.,A5DF E9 55    SBC #$55                SBCI    REMTK-":"       ;REM ONLY STOPS ON NULL.
.,A5E1 D0 9F    BNE $A582               BNE     KLOOP           ;NO, CONTINUE CRUNCHING.
.,A5E3 85 08    STA $08                 STA     ENDCHR          ;REM STOPS ONLY ON NULL, NOT : OR ".
.,A5E5 BD 00 02 LDA $0200,X     STR1:   LDA     BUFOFS,X
.,A5E8 F0 DF    BEQ $A5C9               BEQ     STUFFH          ;YES, END OF LINE, SO DONE.
.,A5EA C5 08    CMP $08                 CMP     ENDCHR          ;END OF GOBBLE?
.,A5EC F0 DB    BEQ $A5C9               BEQ     STUFFH          ;YES, DONE WITH STRING.
.,A5EE C8       INY             STRNG:  INY                     ;INCREMENT BUFFER POINTER.
.,A5EF 99 FB 01 STA $01FB,Y             STA     BUF-5,Y
.,A5F2 E8       INX                     INX
.,A5F3 D0 F0    BNE $A5E5               BNE     STR1            ;PROCESS NEXT CHARACTER.
.,A5F5 A6 7A    LDX $7A         NTHIS:  LDX     TXTPTR          ;RESTORE TEXT POINTER.
.,A5F7 E6 0B    INC $0B                 INC     COUNT           ;INCREMENT RES WORD COUNT.
.,A5F9 C8       INY             NTHIS1: INY
.,A5FA B9 9D A0 LDA $A09D,Y             LDA     RESLST-1,Y,     ;GET RES CHARACTER.
.,A5FD 10 FA    BPL $A5F9               BPL     NTHIS1          ;END OF ENTRY?
.,A5FF B9 9E A0 LDA $A09E,Y             LDA     RESLST,Y,       ;YES. IS IT THE END?
.,A602 D0 B4    BNE $A5B8               BNE     RESCON          ;NO, TRY THE NEXT WORD.
.,A604 BD 00 02 LDA $0200,X             LDA     BUFOFS,X        ;YES, END OF TABLE. GET 1ST CHR.
.,A607 10 BE    BPL $A5C7               BPL     GETBPT          ;STORE IT AWAY (ALWAYS BRANCHES).
.,A609 99 FD 01 STA $01FD,Y     CRDONE: STA     BUF-3,Y,        ;SO THAT IF THIS IS A DIR STATEMENT
                                                                ;ITS END WILL LOOK LIKE END OF PROGRAM.
                                IFN     <<BUF+BUFLEN>/256>-<<BUF-1>/256>,<
.,A60C C6 7B    DEC $7B                 DEC     TXTPTR+1>
.,A60E A9 FF    LDA #$FF                LDAI    <BUF&255>-1     ;MAKE TXTPTR POINT TO
.,A610 85 7A    STA $7A                 STA     TXTPTR          ;CRUNCHED LINE.
.,A612 60       RTS             LISTRT: RTS                     ;RETURN TO CALLER.
                                ;
                                ; FNDLIN SEARCHES THE PROGRAM TEXT FOR THE LINE
                                ; WHOSE NUMBER IS PASSED IN "LINNUM".
                                ; THERE ARE TWO POSSIBLE RETURNS:
                                ;
                                ;       1) CARRY SET.
                                ;          LOWTR POINTS TO THE LINK FIELD IN THE LINE
                                ;          WHICH IS THE ONE SEARCHED FOR.
                                ;
                                ;       2) CARRY NOT SET.
                                ;          LINE NOT FOUND. [LOWTR] POINTS TO THE LINE IN THE
                                ;          PROGRAM GREATER THAN THE ONE SOUGHT AFTER.
                                ;
.,A613 A5 2B    LDA $2B         FNDLIN: LDWX    TXTTAB          ;LOAD [X,A] WITH [TXTTAB]
.,A615 A6 2C    LDX $2C         
.,A617 A0 01    LDY #$01        FNDLNC: LDYI    1
.,A619 85 5F    STA $5F                 STWX    LOWTR           ;STORE [X,A] INTO LOWTR
.,A61B 86 60    STX $60         
.,A61D B1 5F    LDA ($5F),Y             LDADY   LOWTR           ;SEE IF LINK IS 0
.,A61F F0 1F    BEQ $A640               BEQ     FLINRT
.,A621 C8       INY                     INY
.,A622 C8       INY                     INY
.,A623 A5 15    LDA $15                 LDA     LINNUM+1        ;COMP HIGH ORDERS OF LINE NUMBERS.
.,A625 D1 5F    CMP ($5F),Y             CMPDY   LOWTR
.,A627 90 18    BCC $A641               BCC     FLNRTS          ;NO SUCH LINE NUMBER.
.,A629 F0 03    BEQ $A62E               BEQ     FNDLO1
.,A62B 88       DEY                     DEY
.,A62C D0 09    BNE $A637               BNE     AFFRTS          ;ALWAYS BRANCH.
.,A62E A5 14    LDA $14         FNDLO1: LDA     LINNUM
.,A630 88       DEY                     DEY
.,A631 D1 5F    CMP ($5F),Y             CMPDY   LOWTR           ;COMPARE LOW ORDERS.
.,A633 90 0C    BCC $A641               BCC     FLNRTS          ;NO SUCH NUMBER.
.,A635 F0 0A    BEQ $A641               BEQ     FLNRTS          ;GO TIT.
.,A637 88       DEY             AFFRTS: DEY
.,A638 B1 5F    LDA ($5F),Y             LDADY   LOWTR           ;FETCH LINK.
.,A63A AA       TAX                     TAX
.,A63B 88       DEY                     DEY
.,A63C B1 5F    LDA ($5F),Y             LDADY   LOWTR
.,A63E B0 D7    BCS $A617               BCS     FNDLNC          ;ALWAYS BRANCHES.
.,A640 18       CLC             FLINRT: CLC                     ;C MAY BE HIGH.
.,A641 60       RTS             FLNRTS: RTS                     ;RETURN TO CALLER.
                                ;
                                ; THE "NEW" COMMAND CLEARS THE PROGRAM TEXT AS WELL
                                ; AS VARIABLE SPACE.
                                ;
.,A642 D0 FD    BNE $A641       SCRATH: BNE     FLNRTS          ;MAKE SURE THERE IS A TERMINATOR.
.,A644 A9 00    LDA #$00        SCRTCH: LDAI    0               ;GET A CLEARER.
.,A646 A8       TAY                     TAY                     ;SET UP INDEX.
.,A647 91 2B    STA ($2B),Y             STADY   TXTTAB          ;CLEAR  FIRST LINK.
.,A649 C8       INY                     INY
.,A64A 91 2B    STA ($2B),Y             STADY   TXTTAB
.,A64C A5 2B    LDA $2B                 LDA     TXTTAB
.,A64E 18       CLC                     CLC
.,A64F 69 02    ADC #$02                ADCI    2
.,A651 85 2D    STA $2D                 STA     VARTAB          ;SETUP [VARTAB].
.,A653 A5 2C    LDA $2C                 LDA     TXTTAB+1
.,A655 69 00    ADC #$00                ADCI    0
.,A657 85 2E    STA $2E                 STA     VARTAB+1
.,A659 20 8E A6 JSR $A68E       RUNC:   JSR     STXTPT
.,A65C A9 00    LDA #$00                LDAI    0               ;SET ZERO FLAG
                                ;
                                ; THIS CODE IS FOR THE CLEAR COMMAND.
                                ;
.,A65E D0 2D    BNE $A68D       CLEAR:  BNE     STKRTS          ;SYNTAX ERROR IF NO TERMINATOR.
                                ;
                                ; CLEAR INITIALIZES THE VARIABLE AND
                                ; ARRAY SPACE BY RESETING ARYTAB (THE END OF SIMPLE VARIABLE SPACE)
                                ; AND STREND (THE END OF ARRAY STORAGE). IT FALLS INTO "STKINI"
                                ; WHICH RESETS THE STACK.
.,A660 20 E7 FF JSR $FFE7       ;
.,A663 A5 37    LDA $37         CLEARC: LDWD    MEMSIZ          ;FREE UP STRING SPACE.
.,A665 A4 38    LDY $38         
.,A667 85 33    STA $33                 STWD    FRETOP
.,A669 84 34    STY $34         IFN     EXTIO,<
                                        JSR     CQCALL>         ;CLOSE ALL OPEN FILES.
.,A66B A5 2D    LDA $2D                 LDWD    VARTAB          ;LIBERATE THE
.,A66D A4 2E    LDY $2E         
.,A66F 85 2F    STA $2F                 STWD    ARYTAB          ;VARIABLES AND
.,A671 84 30    STY $30         
.,A673 85 31    STA $31                 STWD    STREND          ;ARRAYS.
.,A675 84 32    STY $32         
.,A677 20 1D A8 JSR $A81D       FLOAD:  JSR     RESTOR          ;RESTORE DATA.
                                ;
                                ; STKINI RESETS THE STACK POINTER ELIMINATING
                                ; GOSUB AND FOR CONTEXT. STRING TEMPORARIES ARE FREED
                                ; UP, SUBFLG IS RESET. CONTINUING IS PROHIBITED.
                                ; AND A DUMMY ENTRY IS LEFT AT THE BOTTOM OF THE STACK SO "FNDFOR" WILL ALWAYS
                                ; FIND A NON-"FOR" ENTRY AT THE BOTTOM OF THE STACK.
                                ;
.,A67A A2 19    LDX #$19        STKINI: LDXI    TEMPST          ;INITIALIZE STRING TEMPORARIES.
.,A67C 86 16    STX $16                 STX     TEMPPT
.,A67E 68       PLA                     PLA                     ;SETUP RETURN ADDRESS.
.,A67F A8       TAY                     TAY
.,A680 68       PLA                     PLA
.,A681 A2 FA    LDX #$FA                LDXI    STKEND-257
.,A683 9A       TXS                     TXS
.,A684 48       PHA                     PHA
.,A685 98       TYA                     TYA
.,A686 48       PHA                     PHA
.,A687 A9 00    LDA #$00                LDAI    0
.,A689 85 3E    STA $3E                 STA     OLDTXT+1        ;DISALLOWING CONTINUING
.,A68B 85 10    STA $10                 STA     SUBFLG          ;ALLOW SUBSCRIPTS.
.,A68D 60       RTS             STKRTS: RTS
                                
.,A68E 18       CLC             STXTPT: CLC
.,A68F A5 2B    LDA $2B                 LDA     TXTTAB
.,A691 69 FF    ADC #$FF                ADCI    255
.,A693 85 7A    STA $7A                 STA     TXTPTR
.,A695 A5 2C    LDA $2C                 LDA     TXTTAB+1
.,A697 69 FF    ADC #$FF                ADCI    255
.,A699 85 7B    STA $7B                 STA     TXTPTR+1        ;SETUP TEXT POINTER.
.,A69B 60       RTS                     RTS
                                PAGE
                                SUBTTL  THE "LIST" COMMAND.
                                
.,A69C 90 06    BCC $A6A4       LIST:   BCC     GOLST           ;IT IS A DIGIT.
.,A69E F0 04    BEQ $A6A4               BEQ     GOLST           ;IT IS A TERMINATOR.
.,A6A0 C9 AB    CMP #$AB                CMPI    MINUTK          ;DASH PRECEDING?
.,A6A2 D0 E9    BNE $A68D               BNE     STKRTS          ;NO, SO SYNTAX ERROR.
.,A6A4 20 6B A9 JSR $A96B       GOLST:  JSR     LINGET          ;GET LINE NUMBER INTO NUMLIN.
.,A6A7 20 13 A6 JSR $A613               JSR     FNDLIN          ;FIND LINE .GE. [NUMLIN].
.,A6AA 20 79 00 JSR $0079               JSR     CHRGOT          ;GET LAST CHARACTER.
.,A6AD F0 0C    BEQ $A6BB               BEQ     LSTEND          ;IF END OF LINE, # IS THE END.
.,A6AF C9 AB    CMP #$AB                CMPI    MINUTK          ;DASH?
.,A6B1 D0 8E    BNE $A641               BNE     FLNRTS          ;IF NOT, SYNTAX ERROR.
.,A6B3 20 73 00 JSR $0073               JSR     CHRGET          ;GET NEXT CHAR.
.,A6B6 20 6B A9 JSR $A96B               JSR     LINGET          ;GET END #.
.,A6B9 D0 86    BNE $A641               BNE     FLNRTS          ;IF NOT TERMINATOR, ERROR.
.,A6BB 68       PLA             LSTEND: PLA
.,A6BC 68       PLA                     PLA                     ;GET RID OF "NEWSTT" RTS ADDR.
.,A6BD A5 14    LDA $14                 LDA     LINNUM          ;SEE IF IT WAS EXISTENT.
.,A6BF 05 15    ORA $15                 ORA     LINNUM+1
.,A6C1 D0 06    BNE $A6C9               BNE     LIST4           ;IT WAS TYPED.
.,A6C3 A9 FF    LDA #$FF                LDAI    255
.,A6C5 85 14    STA $14                 STA     LINNUM
.,A6C7 85 15    STA $15                 STA     LINNUM+1        ;MAKE IT HUGE.
.,A6C9 A0 01    LDY #$01        LIST4:  LDYI    1
                                IFE     REALIO-3,<
.,A6CB 84 0F    STY $0F                 STY     DORES>
.,A6CD B1 5F    LDA ($5F),Y             LDADY   LOWTR           ;IS LINK ZERO?
.,A6CF F0 43    BEQ $A714               BEQ     GRODY           ;YES, GO TO READY.
                                IFN     REALIO,<
.,A6D1 20 2C A8 JSR $A82C               JSR     ISCNTC>         ;LISTEN FOR CONT-C.
.,A6D4 20 D7 AA JSR $AAD7               JSR     CRDO            ;PRINT CRLF TO START WITH.
.,A6D7 C8       INY                     INY
.,A6D8 B1 5F    LDA ($5F),Y             LDADY   LOWTR
.,A6DA AA       TAX                     TAX
.,A6DB C8       INY                     INY
.,A6DC B1 5F    LDA ($5F),Y             LDADY   LOWTR           ;GET LINE NUMBER.
.,A6DE C5 15    CMP $15                 CMP     LINNUM+1        ;SEE IF BEYOND LAST.
.,A6E0 D0 04    BNE $A6E6               BNE     TSTDUN          ;GO DETERMINE RELATION.
.,A6E2 E4 14    CPX $14                 CPX     LINNUM          ;WAS EQUAL SO TEST LOW ORDER.
.,A6E4 F0 02    BEQ $A6E8               BEQ     TYPLIN          ;EQUAL, SO LIST IT.
.,A6E6 B0 2C    BCS $A714       TSTDUN: BCS     GRODY           ;IF LINE IS GR THAN LAST, THEN DUNE.
.,A6E8 84 49    STY $49         TYPLIN: STY     LSTPNT
.,A6EA 20 CD BD JSR $BDCD               JSR     LINPRT          ;PRINT AS INT WITHOUT LEADING SPACE.
.,A6ED A9 20    LDA #$20                LDAI    " "             ;ALWAYS PRINT SPACE AFTER NUMBER.
.,A6EF A4 49    LDY $49         PRIT4:  LDY     LSTPNT          ;GET POINTER TO LINE BACK.
.,A6F1 29 7F    AND #$7F                ANDI    127
.,A6F3 20 47 AB JSR $AB47       PLOOP:  JSR     OUTDO           ;PRINT CHAR.
                                IFE     REALIO-3,<
.,A6F6 C9 22    CMP #$22                CMPI    34
.,A6F8 D0 06    BNE $A700               BNE     PLOOP1
.,A6FA A5 0F    LDA $0F                 COM     DORES>          ;IF QUOTE, COMPLEMENT FLAG.
.,A6FC 49 FF    EOR #$FF        
.,A6FE 85 0F    STA $0F         
.,A700 C8       INY             PLOOP1: INY
.,A701 F0 11    BEQ $A714               BEQ     GRODY           ;IF WE HAVE PRINTED 256 CHARACTERS
                                                                ;THE PROGRAM MUST BE MISFORMATED IN
                                                                ;MEMORY DUE TO A BAD LOAD OR BAD
                                                                ;HARDWARE. LET THE GUY RECOVER
.,A703 B1 5F    LDA ($5F),Y             LDADY   LOWTR           ;GET NEXT CHAR. IS IT ZERO?
.,A705 D0 10    BNE $A717               BNE     QPLOP           ;YES. END OF LINE.
.,A707 A8       TAY                     TAY
.,A708 B1 5F    LDA ($5F),Y             LDADY   LOWTR
.,A70A AA       TAX                     TAX
.,A70B C8       INY                     INY
.,A70C B1 5F    LDA ($5F),Y             LDADY   LOWTR
.,A70E 86 5F    STX $5F                 STX     LOWTR
.,A710 85 60    STA $60                 STA     LOWTR+1
.,A712 D0 B5    BNE $A6C9               BNE     LIST4           ;BRANCH IF SOMETHING TO LIST.
.,A714 4C 86 E3 JMP $E386       GRODY:  JMP     READY
.,A717 6C 06 03 JMP ($0306)                                     ;IS IT A TOKEN?
.,A71A 10 D7    BPL $A6F3       QPLOP:  BPL     PLOOP           ;NO, HEAD FOR PRINTER.
                                IFE     REALIO-3,<
.,A71C C9 FF    CMP #$FF                CMPI    PI
.,A71E F0 D3    BEQ $A6F3               BEQ     PLOOP
.,A720 24 0F    BIT $0F                 BIT     DORES           ;INSIDE QUOTE MARKS?
.,A722 30 CF    BMI $A6F3               BMI     PLOOP>          ;YES, JUST TYPE THE CHARACTER.
.,A724 38       SEC                     SEC
.,A725 E9 7F    SBC #$7F                SBCI    127             ;GET RID OF SIGN BIT AND ADD 1.
.,A727 AA       TAX                     TAX                     ;MAKE IT A COUNTER.
.,A728 84 49    STY $49                 STY     LSTPNT          ;SAVE POINTER TO LINE.
.,A72A A0 FF    LDY #$FF                LDYI    255             ;LOOK AT RES'D WORD LIST.
.,A72C CA       DEX             RESRCH: DEX                     ;IS THIS THE RES'D WORD?
.,A72D F0 08    BEQ $A737               BEQ     PRIT3           ;YES, GO TOSS IT UP..
.,A72F C8       INY             RESCR1: INY
.,A730 B9 9E A0 LDA $A09E,Y             LDA     RESLST,Y,       ;END OF ENTRY?
.,A733 10 FA    BPL $A72F               BPL     RESCR1          ;NO, CONTINUE PASSING.
.,A735 30 F5    BMI $A72C               BMI     RESRCH
.,A737 C8       INY             PRIT3:  INY
.,A738 B9 9E A0 LDA $A09E,Y             LDA     RESLST,Y
.,A73B 30 B2    BMI $A6EF               BMI     PRIT4           ;END OF RESERVED WORD.
.,A73D 20 47 AB JSR $AB47               JSR     OUTDO           ;PRINT IT.
.,A740 D0 F5    BNE $A737               BNE     PRIT3           ;END OF ENTRY? NO, TYPE REST.
                                PAGE
                                SUBTTL THE "FOR" STATEMENT.
                                ;
                                ; A "FOR" ENTRY ON THE STACK HAS THE FOLLOWING FORMAT:
                                ;
                                ; LOW ADDRESS
                                ;       TOKEN (FORTK) 1 BYTE
                                ;       A POINTER TO THE LOOP VARIABLE 2 BYTES
                                ;       THE STEP 4+ADDPRC BYTES
                                ;       A BYTE REFLECTING THE SIGN OF THE INCREMENT 1 BYTE
                                ;       THE UPPER VALUE 4+ADDPRC BYTES
                                ;       THE LINE NUMBER OF THE "FOR" STATEMENT 2 BYTES
                                ;       A TEXT POINTER INTO THE "FOR" STATEMENT 2 BYTES
                                ; HIGH ADDRESS
                                ;
                                ; TOTAL 16+2*ADDPRC BYTES.
                                ;
                                
.,A742 A9 80    LDA #$80        FOR:    LDAI    128             ;DON'T RECOGNIZE
.,A744 85 10    STA $10                 STA     SUBFLG          ;SUBSCRIPTED VARIABLES.
.,A746 20 A5 A9 JSR $A9A5               JSR     LET             ;READ THE VARIABLE AND ASSIGN IT
                                                                ;THE CORRECT INITIAL VALUE AND STORE
                                                                ;A POINTER TO THE VARIABLE IN VARPNT.
.,A749 20 8A A3 JSR $A38A               JSR     FNDFOR          ;PNTR IS IN VARPNT, AND FORPNT.
.,A74C D0 05    BNE $A753               BNE     NOTOL           ;IF NO MATCH, DON'T ELIMINATE ANYTHING.
.,A74E 8A       TXA                     TXA                     ;MAKE IT ARITHMETICAL.
.,A74F 69 0F    ADC #$0F                ADCI    FORSIZ-3        ;ELIMINATE ALMOST ALL.
.,A751 AA       TAX                     TAX                     ;NOTE C=1, THEN PLA, PLA.
.,A752 9A       TXS                     TXS                     ;MANIFEST.
.,A753 68       PLA             NOTOL:  PLA                     ;GET RID OF NEWSTT RETURN ADDRESS
.,A754 68       PLA                     PLA                     ;IN CASE THIS IS A TOTALLY NEW ENTRY.
.,A755 A9 09    LDA #$09                LDAI    8+ADDPRC
.,A757 20 FB A3 JSR $A3FB               JSR     GETSTK          ;MAKE SURE 16 BYTES ARE AVAILABLE.
.,A75A 20 06 A9 JSR $A906               JSR     DATAN           ;GET A COUNT IN [Y] OF THE NUMBER OF
                                                                ;CHACRACTERS LEFT IN THE "FOR" STATEMENT
                                                                ;[TXTPTR] IS UNAFFECTED.
.,A75D 18       CLC                     CLC                     ;PREP TO ADD.
.,A75E 98       TYA                     TYA                     ;SAVE IT FOR PUSHING.
.,A75F 65 7A    ADC $7A                 ADC     TXTPTR
.,A761 48       PHA                     PHA
.,A762 A5 7B    LDA $7B                 LDA     TXTPTR+1
.,A764 69 00    ADC #$00                ADCI    0
.,A766 48       PHA                     PHA
.,A767 A5 3A    LDA $3A                 PSHWD   CURLIN          ;PUT LINE NUMBER ON STACK.
.,A769 48       PHA             
.,A76A A5 39    LDA $39         
.,A76C 48       PHA             
.,A76D A9 A4    LDA #$A4                SYNCHK  TOTK            ;"TO" IS NECESSARY.
.,A76F 20 FF AE JSR $AEFF       
.,A772 20 8D AD JSR $AD8D               JSR     CHKNUM          ;VALUE MUST BE A NUMBER.
.,A775 20 8A AD JSR $AD8A               JSR     FRMNUM          ;GET UPPER VALUE INTO FAC.
.,A778 A5 66    LDA $66                 LDA     FACSGN          ;PACK FAC.
.,A77A 09 7F    ORA #$7F                ORAI    127
.,A77C 25 62    AND $62                 AND     FACHO
.,A77E 85 62    STA $62                 STA     FACHO           ;SET PACKED SIGN BIT.
.,A780 A9 8B    LDA #$8B                LDWDI   LDFONE
.,A782 A0 A7    LDY #$A7        
.,A784 85 22    STA $22                 STWD    INDEX1
.,A786 84 23    STY $23         
.,A788 4C 43 AE JMP $AE43               JMP     FORPSH          ;PUT FAC ONTO STACK, PACKED.
.,A78B A9 BC    LDA #$BC        LDFONE: LDWDI   FONE            ;PUT 1.0 INTO FAC.
.,A78D A0 B9    LDY #$B9        
.,A78F 20 A2 BB JSR $BBA2               JSR     MOVFM
.,A792 20 79 00 JSR $0079               JSR     CHRGOT
.,A795 C9 A9    CMP #$A9                CMPI    STEPTK          ;A STEP IS GIVEN?
.,A797 D0 06    BNE $A79F               BNE     ONEON           ;NO. ASSUME 1.0.
.,A799 20 73 00 JSR $0073               JSR     CHRGET          ;YES. ADVANCE POINTER.
.,A79C 20 8A AD JSR $AD8A               JSR     FRMNUM          ;READ THE STEP.
.,A79F 20 2B BC JSR $BC2B       ONEON:  JSR     SIGN            ;GET SIGN IN ACCA.
.,A7A2 20 38 AE JSR $AE38               JSR     PUSHF           ;PUSH FAC ONTO STACK (THRU A).
.,A7A5 A5 4A    LDA $4A                 PSHWD   FORPNT          ;PUT PNTR TO VARIABLE ON STACK.
.,A7A7 48       PHA             
.,A7A8 A5 49    LDA $49         
.,A7AA 48       PHA             
.,A7AB A9 81    LDA #$81        NXTCON: LDAI    FORTK           ;PUT A FORTK ONTO STACK.
.,A7AD 48       PHA                     PHA
                                ;       BNEA    NEWSTT          ;SIMULATE BNE TO NEWSTT. JUST FALL IN.
                                PAGE
                                SUBTTL  NEW STATEMENT FETCHER.
                                ;
                                ; BACK HERE FOR NEW STATEMENT. CHARACTER POINTED TO BY TXTPTR
                                ; IS ":" OR END-OF-LINE. THE ADDRESS OF THIS LOC IS LEFT
                                ; ON THE STACK WHEN A STATEMENT IS EXECUTED SO THAT
                                ; IT CAN MERELY DO A RTS WHEN IT IS DONE.
                                ;
                                NEWSTT: IFN     REALIO,<
.,A7AE 20 2C A8 JSR $A82C               JSR     ISCNTC>         ;LISTEN FOR CONTROL-C.
.,A7B1 A5 7A    LDA $7A                 LDWD    TXTPTR          ;LOOK AT CURRENT CHARACTER.
.,A7B3 A4 7B    LDY $7B         
                                IFN     BUFPAG,<
.,A7B5 C0 02    CPY #$02                CPYI    BUFPAG>         ;SEE IF IT WAS DIRECT BY CHECK FOR BUF'S PAGE NUMBER
.,A7B7 EA       NOP             
.,A7B8 F0 04    BEQ $A7BE               BEQ     DIRCON
.,A7BA 85 3D    STA $3D                 STWD    OLDTXT          ;SAVE IN CASE OF RESTART BY INPUT.
.,A7BC 84 3E    STY $3E         
                                IFN     BUFPAG,<DIRCON:>
.,A7BE A0 00    LDY #$00                LDYI    0
                                IFE     BUFPAG,<DIRCON:>
.,A7C0 B1 7A    LDA ($7A),Y             LDADY   TXTPTR
.,A7C2 D0 43    BNE $A807               BNE     MORSTS          ;NOT NULL -- CHECK WHAT IT IS
.,A7C4 A0 02    LDY #$02                LDYI    2               ;LOOK AT LINK.
.,A7C6 B1 7A    LDA ($7A),Y             LDADY   TXTPTR          ;IS LINK 0?
.,A7C8 18       CLC                     CLC             ;CLEAR CARRY FOR ENDCON AND MATH THAT FOLLOWS
.,A7C9 D0 03    BNE $A7CE               JEQ     ENDCON          ;YES - RAN OFF THE END.
.,A7CB 4C 4B A8 JMP $A84B       
.,A7CE C8       INY                     INY                     ;PUT LINE NUMBER IN CURLIN.
.,A7CF B1 7A    LDA ($7A),Y             LDADY   TXTPTR
.,A7D1 85 39    STA $39                 STA     CURLIN
.,A7D3 C8       INY                     INY
.,A7D4 B1 7A    LDA ($7A),Y             LDADY   TXTPTR
.,A7D6 85 3A    STA $3A                 STA     CURLIN+1
.,A7D8 98       TYA                     TYA
.,A7D9 65 7A    ADC $7A                 ADC     TXTPTR
.,A7DB 85 7A    STA $7A                 STA     TXTPTR
.,A7DD 90 02    BCC $A7E1               BCC     GONE
.,A7DF E6 7B    INC $7B                 INC     TXTPTR+1
.,A7E1 6C 08 03 JMP ($0308)     
.,A7E4 20 73 00 JSR $0073       GONE:   JSR     CHRGET          ;GET THE STATEMENT TYPE.
.,A7E7 20 ED A7 JSR $A7ED               JSR     GONE3
.,A7EA 4C AE A7 JMP $A7AE               JMP     NEWSTT
.,A7ED F0 3C    BEQ $A82B       GONE3:  BEQ     ISCRTS          ;IF TERMINATOR, TRY AGAIN.
                                                                ;NO NEED TO SET UP CARRY SINCE IT WILL
                                                                ;BE ON IF NON-NUMERIC AND NUMERICS
                                                                ;WILL CAUSE A SYNTAX ERROR LIKE THEY SHOULD
.,A7EF E9 80    SBC #$80        GONE2:  SBCI    ENDTK           ;" ON ... GOTO AND GOSUB" COME HERE.
.,A7F1 90 11    BCC $A804               BCC     GLET
.,A7F3 C9 23    CMP #$23                CMPI    SCRATK-ENDTK+1
.,A7F5 B0 17    BCS $A80E               BCS     SNERRX          ;SOME RES'D WORD BUT NOT
                                                                ;A STATEMENT RES'D WORD.
.,A7F7 0A       ASL                     ASL     A,              ;MULTIPLY BY TWO.
.,A7F8 A8       TAY                     TAY                     ;MAKE AN INDEX.
.,A7F9 B9 0D A0 LDA $A00D,Y             LDA     STMDSP+1,Y
.,A7FC 48       PHA                     PHA
.,A7FD B9 0C A0 LDA $A00C,Y             LDA     STMDSP,Y
.,A800 48       PHA                     PHA                     ;PUT DISP ADDR ONTO STACK.
.,A801 4C 73 00 JMP $0073               JMP     CHRGET
.,A804 4C A5 A9 JMP $A9A5       GLET:   JMP     LET             ;MUST BE A LET
.,A807 C9 3A    CMP #$3A        MORSTS: CMPI    ":"
.,A809 F0 D6    BEQ $A7E1               BEQ     GONE            ;IF A ":" CONTINUE STATEMENT
.,A80B 4C 08 AF JMP $AF08       SNERR1: JMP     SNERR           ;NEITHER 0 OR ":" SO SYNTAX ERROR
.,A80E C9 4B    CMP #$4B        SNERRX: CMPI    GOTK-ENDTK
.,A810 D0 F9    BNE $A80B               BNE     SNERR1
.,A812 20 73 00 JSR $0073               JSR     CHRGET          ;READ IN THE CHARACTER AFTER "GO "
.,A815 A9 A4    LDA #$A4                SYNCHK  TOTK
.,A817 20 FF AE JSR $AEFF       
.,A81A 4C A0 A8 JMP $A8A0               JMP     GOTO
                                PAGE
                                SUBTTL  RESTORE,STOP,END,CONTINUE,NULL,CLEAR.
                                
.,A81D 38       SEC             RESTOR: SEC
.,A81E A5 2B    LDA $2B                 LDA     TXTTAB
.,A820 E9 01    SBC #$01                SBCI    1
.,A822 A4 2C    LDY $2C                 LDY     TXTTAB+1
.,A824 B0 01    BCS $A827               BCS     RESFIN
.,A826 88       DEY                     DEY
.,A827 85 41    STA $41         RESFIN: STWD    DATPTR          ;READ FINISHES COME TO "RESFIN".
.,A829 84 42    STY $42         
.,A82B 60       RTS             ISCRTS: RTS
                                
                                IFE     REALIO-1,<
                                ISCNTC: LDAI    1
                                        BIT     ^O13500
                                        BMI     ISCRTS
                                        LDXI    8
                                        LDAI    3
                                        CMPI    3>
                                IFE     REALIO-2,<
                                ISCNTC: LDA     ^O176000
                                        REPEAT  4,<NOP>
                                        LSR     A,
                                        BCC     ISCRTS
                                        JSR     INCHR           ;EAT CHAR THAT WAS TYPED
                                        CMPI    3>              ;WAS IT A CONTROL-C??
                                
                                IFE     REALIO-4,<
                                ISCNTC: LDA     ^O140000        ;CHECK THE CHARACTER
                                        CMPI    ^O203
                                        BEQ     ISCCAP
                                        RTS
                                ISCCAP: JSR     INCHR
.,A82C 20 E1 FF JSR $FFE1               CMPI    ^O203>
.,A82F B0 01    BCS $A832       STOP:   BCS     STOPC           ;MAKE [C] NONZERO AS A FLAG.
.,A831 18       CLC             END:    CLC
.,A832 D0 3C    BNE $A870       STOPC:  BNE     CONTRT          ;RETURN IF NOT CONT-C OR
                                                                ;IF NO TERMINATOR FOR STOP OR END.
                                                                ;[C]=0 SO WILL NOT PRINT "BREAK".
.,A834 A5 7A    LDA $7A                 LDWD    TXTPTR
.,A836 A4 7B    LDY $7B         IFN     BUFPAG,<
.,A838 A6 3A    LDX $3A                 LDX     CURLIN+1
.,A83A E8       INX                     INX>
.,A83B F0 0C    BEQ $A849               BEQ     DIRIS
.,A83D 85 3D    STA $3D                 STWD    OLDTXT
.,A83F 84 3E    STY $3E         
.,A841 A5 39    LDA $39         STPEND: LDWD    CURLIN
.,A843 A4 3A    LDY $3A         
.,A845 85 3B    STA $3B                 STWD    OLDLIN
.,A847 84 3C    STY $3C         
.,A849 68       PLA             DIRIS:  PLA                     ;POP OFF NEWSTT ADDR.
.,A84A 68       PLA                     PLA
.,A84B A9 81    LDA #$81        ENDCON: LDWDI   BRKTXT
.,A84D A0 A3    LDY #$A3        IFN     REALIO,<
                                        LDXI    0
                                        STX     CNTWFL>
.,A84F 90 03    BCC $A854               BCC     GORDY           ;CARRY CLEAR SO DON'T PRINT "BREAK".
.,A851 4C 69 A4 JMP $A469               JMP     ERRFIN
.,A854 4C 86 E3 JMP $E386       GORDY:  JMP     READY           ;TYPE "READY".
                                
                                IFE     REALIO,<
                                DDT:    PLA                     ;GET RID OF NEWSTT RETURN.
                                        PLA
                                        HRRZ    14,.JBDDT##
                                        JRST    0(14)>
.,A857 D0 17    BNE $A870       CONT:   BNE     CONTRT          ;MAKE SURE THERE IS A TERMINATOR.
.,A859 A2 1A    LDX #$1A                LDXI    ERRCN           ;CONTINUE ERROR.
.,A85B A4 3E    LDY $3E                 LDY     OLDTXT+1        ;A STORED TXTPTR OF ZERO IS SETUP
                                                                ;BY STKINI AND INDICATES THERE IS
                                                                ;NOTHING TO CONTINUE.
.,A85D D0 03    BNE $A862               JEQ     ERROR           ;"STOP", "END", TYPING CRLF TO
.,A85F 4C 37 A4 JMP $A437                                       ;"INPUT" AND  ^C SETUP OLDTXT.
.,A862 A5 3D    LDA $3D                 LDA     OLDTXT
.,A864 85 7A    STA $7A                 STWD    TXTPTR
.,A866 84 7B    STY $7B         
.,A868 A5 3B    LDA $3B                 LDWD    OLDLIN
.,A86A A4 3C    LDY $3C         
.,A86C 85 39    STA $39                 STWD    CURLIN
.,A86E 84 3A    STY $3A         
.,A870 60       RTS             CONTRT: RTS                     ;RETURN TO CALLER.
                                
                                IFN     NULCMD,<
                                NULL:   JSR     GETBYT
                                        BNE     CONTRT          ;MAKE SURE THERE IS TERMINATOR.
                                        INX
                                        CPXI    240             ;IS THE NUMBER REASONABLE?
                                        BCS     FCERR1          ;"FUNCTION CALL" ERROR.
                                        DEX                     ;BACK -1
                                        STX     NULCNT
                                        RTS
                                FCERR1: JMP     FCERR>
                                PAGE
                                SUBTTL  LOAD AND SAVE SUBROUTINES.
                                
                                IFE     REALIO-1,<              ;KIM CASSETTE I/O
                                SAVE:   TSX                     ;SAVE STACK POINTER
                                        STX     INPFLG
                                        LDAI    STKEND-256-200
                                        STA     ^O362           ;SETUP DUMMY STACK FOR KIM MONITOR
                                        LDAI    254             ;MAKE ID BYTE EQUAL TO FF HEX
                                        STA     ^O13771         ;STORE INTO KIM ID
                                        LDWD    TXTTAB          ;START DUMPING FROM TXTTAB
                                        STWD    ^O13765         ;SETUP SAL,SAH
                                        LDWD    VARTAB          ;STOP AT VARTAB
                                        STWD    ^O13767         ;SETUP EAL,EAH
                                        JMP     ^O14000
                                RETSAV: LDX     INPFLG          ;RESORE THE REAL STACK POINTER
                                        TXS
                                        LDWDI   TAPMES          ;SAY IT WAS DONE
                                        JMP     STROUT
                                GLOAD:  DT"LOADED"
                                        0
                                TAPMES: DT"SAVED"
                                        ACRLF
                                        0
                                PATSAV: BLOCK 20
                                LOAD:   LDWD    TXTTAB          ;START DUMPING IN AT TXTTAB
                                        STWD    ^O13765         ;SETUP SAL,SAH
                                        LDAI    255
                                        STA     ^O13771
                                        LDWDI   RTLOAD
                                        STWD    ^O1             ;SET UP RETURN ADDRESS FOR LOAD
                                        JMP     ^O14163         ;GO READ THE DATA IN
                                RTLOAD: LDXI    STKEND-256              ;RESET THE STACK
                                        TXS
                                        LDWDI   READY
                                        STWD    ^O1
                                        LDWDI   GLOAD           ;TELL HIM IT WORKED
                                        JSR     STROUT
                                        LDXY    ^O13755         ;GET LAST LOCATION
                                        TXA                     ;ITS ONE TOO BIG
                                        BNE     DECVRT          ;DECREMENT [X,Y]
                                        NOP
                                DECVRT: NOP
                                        STXY    VARTAB          ;SETUP NEW VARIABLE LOCATION
                                        JMP     FINI>           ;RELINK THE PROGRAM
                                IFE     REALIO-4,<
                                SAVE:   SEC                     ;CALCLUATE PROGRAM SIZE IN POKER
                                        LDA     VARTAB
                                        SBC     TXTTAB
                                        STA     POKER
                                        LDA     VARTAB+1
                                        SBC     TXTTAB+1
                                        STA     POKER+1
                                        JSR     VARTIO
                                        JSR     CQCOUT          ;WRITE PROGRAM SIZE [POKER]
                                        JSR     PROGIO
                                        JMP     CQCOUT          ;WRITE PROGRAM.
                                
                                LOAD:   JSR     VARTIO
                                        JSR     CQCSIN          ;READ SIZE OF PROGRAM INTO POKER
                                        CLC
                                        LDA     TXTTAB          ;CALCULATE VARTAB FROM SIZE AND
                                        ADC     POKER           ;TXTTAB
                                        STA     VARTAB
                                        LDA     TXTTAB+1
                                        ADC     POKER+1
                                        STA     VARTAB+1
                                        JSR     PROGIO
                                        JSR     CQCSIN          ;READ PROGRAM.
                                        LDWDI   TPDONE
                                        JSR     STROUT
                                        JMP     FINI
                                
                                TPDONE: DT"LOADED"
                                        0
                                
                                VARTIO: LDWDI   POKER
                                        STWD    ^O74
                                        LDAI    POKER+2
                                        STWD    ^O76
                                        RTS
                                PROGIO: LDWD    TXTTAB
                                        STWD    ^O74
                                        LDWD    VARTAB
                                        STWD    ^O76
                                        RTS>
                                
                                PAGE
                                SUBTTL  RUN,GOTO,GOSUB,RETURN.
.,A871 08       PHP             
.,A872 A9 00    LDA #$00        
.,A874 20 90 FF JSR $FF90       
.,A877 28       PLP             
.,A878 D0 03    BNE $A87D       RUN:    JEQ     RUNC            ;IF NO LINE # ARGUMENT.
.,A87A 4C 59 A6 JMP $A659       
.,A87D 20 60 A6 JSR $A660               JSR     CLEARC          ;CLEAN UP -- RESET THE STACK.
.,A880 4C 97 A8 JMP $A897               JMP     RUNC2           ;MUST REPLACE RTS ADDR.
                                ;
                                ; A GOSUB ENTRY ON THE STACK HAS THE FOLLOWING FORMAT:
                                ;
                                ; LOW ADDRESS:
                                ;       THE GOSUTK ONE BYTE
                                ;       THE LINE NUMBER OF THE GOSUB STATEMENT TWO BYTES
                                ;       A POINTER INTO THE TEXT OF THE GOSUB TWO BYTES
                                ;
                                ; HIGH ADDRESS.
                                ;
                                ; TOTAL FIVE BYTES.
                                ;
.,A883 A9 03    LDA #$03        GOSUB:  LDAI    3
.,A885 20 FB A3 JSR $A3FB               JSR     GETSTK          ;MAKE SURE THERE IS ROOM.
.,A888 A5 7B    LDA $7B                 PSHWD   TXTPTR          ;PUSH ON THE TEXT POINTER.
.,A88A 48       PHA             
.,A88B A5 7A    LDA $7A         
.,A88D 48       PHA             
.,A88E A5 3A    LDA $3A                 PSHWD   CURLIN          ;PUSH ON THE CURRENT LINE NUMBER.
.,A890 48       PHA             
.,A891 A5 39    LDA $39         
.,A893 48       PHA             
.,A894 A9 8D    LDA #$8D                LDAI    GOSUTK
.,A896 48       PHA                     PHA                     ;PUSH ON A GOSUB TOKEN.
.,A897 20 79 00 JSR $0079       RUNC2:  JSR     CHRGOT          ;GET CHARACTER AND SET CODES FOR LINGET.
.,A89A 20 A0 A8 JSR $A8A0               JSR     GOTO            ;USE RTS SCHEME TO "NEWSTT".
.,A89D 4C AE A7 JMP $A7AE               JMP     NEWSTT
                                
.,A8A0 20 6B A9 JSR $A96B       GOTO:   JSR     LINGET          ;PICK UP THE LINE NUMBER IN "LINNUM".
.,A8A3 20 09 A9 JSR $A909               JSR     REMN            ;SKIP TO END OF LINE.
.,A8A6 38       SEC             
.,A8A7 A5 39    LDA $39         
.,A8A9 E5 14    SBC $14         
.,A8AB A5 3A    LDA $3A                 LDA     CURLIN+1
.,A8AD E5 15    SBC $15                 CMP     LINNUM+1
.,A8AF B0 0B    BCS $A8BC               BCS     LUK4IT
.,A8B1 98       TYA                     TYA
.,A8B2 38       SEC                     SEC
.,A8B3 65 7A    ADC $7A                 ADC     TXTPTR
.,A8B5 A6 7B    LDX $7B                 LDX     TXTPTR+1
.,A8B7 90 07    BCC $A8C0               BCC     LUKALL
.,A8B9 E8       INX                     INX
.,A8BA B0 04    BCS $A8C0               BCSA    LUKALL          ;ALWAYS GOES.
.,A8BC A5 2B    LDA $2B         LUK4IT: LDWX    TXTTAB
.,A8BE A6 2C    LDX $2C         
.,A8C0 20 17 A6 JSR $A617       LUKALL: JSR     FNDLNC          ;[X,A] ARE ALL SET UP.
.,A8C3 90 1E    BCC $A8E3       QFOUND: BCC     USERR           ;GOTO LINE IS NONEXISTANT.
.,A8C5 A5 5F    LDA $5F                 LDA     LOWTR
.,A8C7 E9 01    SBC #$01                SBCI    1
.,A8C9 85 7A    STA $7A                 STA     TXTPTR
.,A8CB A5 60    LDA $60                 LDA     LOWTR+1
.,A8CD E9 00    SBC #$00                SBCI    0
.,A8CF 85 7B    STA $7B                 STA     TXTPTR+1
.,A8D1 60       RTS             GORTS:  RTS                     ;PROCESS THE STATEMENT.
                                ;
                                ; "RETURN" RESTORES THE LINE NUMBER AND TEXT PNTR FROM THE STACK
                                ; AND ELIMINATES ALL THE "FOR" ENTRIES IN FRONT OF THE "GOSUB" ENTRY.
                                ;
.,A8D2 D0 FD    BNE $A8D1       RETURN: BNE     GORTS           ;NO TERMINATOR=BLOW HIM UP.
.,A8D4 A9 FF    LDA #$FF                LDAI    255
.,A8D6 85 4A    STA $4A                 STA     FORPNT+1        ;MAKE SURE THE VARIABLE'S PNTR
                                                                ;NEVER GETS MATCHED.
.,A8D8 20 8A A3 JSR $A38A               JSR     FNDFOR          ;GO PAST ALL THE "FOR" ENTRIES.
.,A8DB 9A       TXS                     TXS
.,A8DC C9 8D    CMP #$8D                CMPI    GOSUTK          ;RETURN WITHOUT GOSUB?
.,A8DE F0 0B    BEQ $A8EB               BEQ     RETU1
.,A8E0 A2 0C    LDX #$0C                LDXI    ERRRG
.:A8E2 2C       .BYTE $2C               SKIP2
.,A8E3 A2 11    LDX #$02        USERR:  LDXI    ERRUS           ;NO MATCH SO "US" ERROR.
.,A8E5 4C 37 A4 JMP $A437               JMP     ERROR           ;YES.
.,A8E8 4C 08 AF JMP $AF08       SNERR2: JMP     SNERR
.,A8EB 68       PLA             RETU1:  PLA                     ;REMOVE GOSUTK.
.,A8EC 68       PLA                     PULWD   CURLIN          ;GET LINE NUMBER "GOSUB" WAS FROM.
.,A8ED 85 39    STA $39         
.,A8EF 68       PLA             
.,A8F0 85 3A    STA $3A         
.,A8F2 68       PLA                     PULWD   TXTPTR          ;GET TEXT PNTR FROM "GOSUB".
.,A8F3 85 7A    STA $7A         
.,A8F5 68       PLA             
.,A8F6 85 7B    STA $7B         
.,A8F8 20 06 A9 JSR $A906       DATA:   JSR     DATAN           ;SKIP TO END OF STATEMENT,
                                                                ;SINCE WHEN "GOSUB" STUCK THE TEXT  PNTR
                                                                ;ONTO THE STACK, THE LINE NUMBER ARG
                                                                ;HADN'T BEEN READ YET.
.,A8FB 98       TYA             ADDON:  TYA
.,A8FC 18       CLC                     CLC
.,A8FD 65 7A    ADC $7A                 ADC     TXTPTR
.,A8FF 85 7A    STA $7A                 STA     TXTPTR
.,A901 90 02    BCC $A905               BCC     REMRTS
.,A903 E6 7B    INC $7B                 INC     TXTPTR+1
.,A905 60       RTS             REMRTS: RTS                     ;"NEWSTT" RTS ADDR IS STILL THERE.
                                
.,A906 A2 3A    LDX #$3A        DATAN:  LDXI    ":"             ;"DATA" TERMINATES ON ":" AND NULL.
.:A908 2C       .BYTE $2C               SKIP2
.,A909 A2 00    LDX #$00        REMN:   LDXI    0               ;THE ONLY TERMINATOR IS NULL.
.,A90B 86 07    STX $07                 STX     CHARAC          ;PRESERVE IT.
.,A90D A0 00    LDY #$00                LDYI    0               ;THIS MAKES CHARAC=0 AFTER SWAP.
.,A90F 84 08    STY $08                 STY     ENDCHR
.,A911 A5 08    LDA $08         EXCHQT: LDA     ENDCHR
.,A913 A6 07    LDX $07                 LDX     CHARAC
.,A915 85 07    STA $07                 STA     CHARAC
.,A917 86 08    STX $08                 STX     ENDCHR
.,A919 B1 7A    LDA ($7A),Y     REMER:  LDADY   TXTPTR
.,A91B F0 E8    BEQ $A905               BEQ     REMRTS          ;NULL ALWAYS TERMINATES.
.,A91D C5 08    CMP $08                 CMP     ENDCHR          ;IS IT THE OTHER TERMINATOR?
.,A91F F0 E4    BEQ $A905               BEQ     REMRTS          ;YES, IT'S FINISHED.
.,A921 C8       INY                     INY                     ;PROGRESS TO NEXT CHARACTER.
.,A922 C9 22    CMP #$22                CMPI    34              ;IS IT A QUOTE?
.,A924 D0 F3    BNE $A919               BNE     REMER           ;NO, JUST CONTINUE.
.,A926 F0 E9    BEQ $A911               BEQA    EXCHQT          ;YES, TIME TO TRADE.
                                PAGE
                                SUBTTL  "IF ... THEN" CODE.
.,A928 20 9E AD JSR $AD9E       IF:     JSR     FRMEVL          ;EVALUATE A FORMULA.
.,A92B 20 79 00 JSR $0079               JSR     CHRGOT          ;GET CURRENT CHARACTER.
.,A92E C9 89    CMP #$89                CMPI    GOTOTK          ;IS TERMINATING CHARACTER A GOTOTK?
.,A930 F0 05    BEQ $A937               BEQ     OKGOTO          ;YES.
.,A932 A9 A7    LDA #$A7                SYNCHK  THENTK          ;NO, IT MUST BE "THEN".
.,A934 20 FF AE JSR $AEFF       
.,A937 A5 61    LDA $61         OKGOTO: LDA     FACEXP          ;0=FALSE. ALL OTHERS TRUE.
.,A939 D0 05    BNE $A940               BNE     DOCOND          ;TRUE !
.,A93B 20 09 A9 JSR $A909       REM:    JSR     REMN            ;SKIP REST OF STATEMENT.
.,A93E F0 BB    BEQ $A8FB               BEQA    ADDON           ;WILL ALWAYS BRANCH.
.,A940 20 79 00 JSR $0079       DOCOND: JSR     CHRGOT          ;TEST CURRENT CHARACTER.
.,A943 B0 03    BCS $A948               BCS     DOCO            ;IF A NUMBER, GOTO IT.
.,A945 4C A0 A8 JMP $A8A0               JMP     GOTO
.,A948 4C ED A7 JMP $A7ED       DOCO:   JMP     GONE3           ;INTERPRET NEW STATEMENT.
                                PAGE
                                SUBTTL  "ON ... GO TO ..." CODE.
.,A94B 20 9E B7 JSR $B79E       ONGOTO: JSR     GETBYT          ;GET VALUE IN FACLO.
.,A94E 48       PHA                     PHA                     ;SAVE FOR LATER.
.,A94F C9 8D    CMP #$8D                CMPI    GOSUTK          ;AN "ON ... GOSUB" PERHAPS?
.,A951 F0 04    BEQ $A957               BEQ     ONGLOP          ;YES.
.,A953 C9 89    CMP #$89        SNERR3: CMPI    GOTOTK          ;MUST BE "GOTOTK".
.,A955 D0 91    BNE $A8E8               BNE     SNERR2
.,A957 C6 65    DEC $65         ONGLOP: DEC     FACLO
.,A959 D0 04    BNE $A95F               BNE     ONGLP1          ;SKIP ANOTHER LINE NUMBER.
.,A95B 68       PLA                     PLA                     ;GET DISPATCH CHARACTER.
.,A95C 4C EF A7 JMP $A7EF               JMP     GONE2
.,A95F 20 73 00 JSR $0073       ONGLP1: JSR     CHRGET          ;ADVANCE AND SET CODES.
.,A962 20 6B A9 JSR $A96B               JSR     LINGET
.,A965 C9 2C    CMP #$2C                CMPI    44              ;IS IT A COMMA?
.,A967 F0 EE    BEQ $A957               BEQ     ONGLOP
.,A969 68       PLA                     PLA                     ;REMOVE STACK ENTRY (TOKEN).
.,A96A 60       RTS             ONGRTS: RTS                     ;EITHER END-OF-LINE OR SYNTAX ERROR.
                                PAGE
                                SUBTTL  LINGET -- READ A LINE NUMBER INTO LINNUM
                                ;
                                ; "LINGET" READS A LINE NUMBER FROM THE CURRENT TEXT POSITION.
                                ;
                                ; LINE NUMBERS RANGE FROM 0 TO 64000-1.
                                ;
                                ; THE ANSWER IS RETURNED IN "LINNUM".
                                ; "TXTPTR" IS UPDATED TO POINT TO THE TERMINATING CHARCTER
                                ; AND [A] = THE TERMINATING CHARACTER WITH CONDITION
                                ; CODES SET UP TO REFLECT ITS VALUE.
                                ;
.,A96B A2 00    LDX #$00        LINGET: LDXI    0
.,A96D 86 14    STX $14                 STX     LINNUM          ;INITIALIZE LINE NUMBER TO ZERO.
.,A96F 86 15    STX $15                 STX     LINNUM+1
.,A971 B0 F7    BCS $A96A       MORLIN: BCS     ONGRTS          ;IT IS NOT A DIGIT.
.,A973 E9 2F    SBC #$2F                SBCI    "0"-1           ;-1 SINCE C=0.
.,A975 85 07    STA $07                 STA     CHARAC          ;SAVE CHARACTER.
.,A977 A5 15    LDA $15                 LDA     LINNUM+1
.,A979 85 22    STA $22                 STA     INDEX
.,A97B C9 19    CMP #$19                CMPI    25              ;LINE NUMBER WILL BE .LT. 64000?
.,A97D B0 D4    BCS $A953               BCS     SNERR3
.,A97F A5 14    LDA $14                 LDA     LINNUM
.,A981 0A       ASL                     ASL     A,              ;MULTIPLY BY 10.
.,A982 26 22    ROL $22                 ROL     INDEX
.,A984 0A       ASL                     ASL     A
.,A985 26 22    ROL $22                 ROL     INDEX
.,A987 65 14    ADC $14                 ADC     LINNUM
.,A989 85 14    STA $14                 STA     LINNUM
.,A98B A5 22    LDA $22                 LDA     INDEX
.,A98D 65 15    ADC $15                 ADC     LINNUM+1
.,A98F 85 15    STA $15                 STA     LINNUM+1
.,A991 06 14    ASL $14                 ASL     LINNUM
.,A993 26 15    ROL $15                 ROL     LINNUM+1
.,A995 A5 14    LDA $14                 LDA     LINNUM
.,A997 65 07    ADC $07                 ADC     CHARAC          ;ADD IN DIGIT.
.,A999 85 14    STA $14                 STA     LINNUM
.,A99B 90 02    BCC $A99F               BCC     NXTLGC
.,A99D E6 15    INC $15                 INC     LINNUM+1
.,A99F 20 73 00 JSR $0073       NXTLGC: JSR     CHRGET
.,A9A2 4C 71 A9 JMP $A971               JMP     MORLIN
                                
                                PAGE
                                SUBTTL  "LET" CODE.
.,A9A5 20 8B B0 JSR $B08B       LET:    JSR     PTRGET          ;GET PNTR TO VARIABLE INTO "VARPNT".
.,A9A8 85 49    STA $49                 STWD    FORPNT          ;PRESERVE POINTER.
.,A9AA 84 4A    STY $4A         
.,A9AC A9 B2    LDA #$B2                SYNCHK  EQULTK          ;"=" IS NECESSARY.
.,A9AE 20 FF AE JSR $AEFF       IFN     INTPRC,<
.,A9B1 A5 0E    LDA $0E                 LDA     INTFLG          ;SAVE FOR LATER.
.,A9B3 48       PHA                     PHA>
.,A9B4 A5 0D    LDA $0D                 LDA     VALTYP          ;RETAIN THE VARIABLE'S VALUE TYPE.
.,A9B6 48       PHA                     PHA
.,A9B7 20 9E AD JSR $AD9E               JSR     FRMEVL          ;GET VALUE OF FORMULA INTO "FAC".
.,A9BA 68       PLA                     PLA
.,A9BB 2A       ROL                     ROL     A,              ;CARRY SET FOR STRING, OFF FOR
                                                                ;NUMERIC.
.,A9BC 20 90 AD JSR $AD90               JSR     CHKVAL          ;MAKE SURE "VALTYP" MATCHES CARRY.
                                                                ;AND SET ZERO FLAG FOR NUMERIC.
.,A9BF D0 18    BNE $A9D9               BNE     COPSTR          ;IF NUMERIC, COPY IT.
                                COPNUM:
                                IFN     INTPRC,<
.,A9C1 68       PLA                     PLA                     ;GET NUMBER TYPE.
.,A9C2 10 12    BPL $A9D6       QINTGR: BPL     COPFLT          ;STORE A FLTING NUMBER.
.,A9C4 20 1B BC JSR $BC1B               JSR     ROUND           ;ROUND INTEGER.
.,A9C7 20 BF B1 JSR $B1BF               JSR     AYINT           ;MAKE 2-BYTE NUMBER.
.,A9CA A0 00    LDY #$00                LDYI    0
.,A9CC A5 64    LDA $64                 LDA     FACMO           ;GET HIGH.
.,A9CE 91 49    STA ($49),Y             STADY   FORPNT          ;STORE IT.
.,A9D0 C8       INY                     INY
.,A9D1 A5 65    LDA $65                 LDA     FACLO           ;GET LOW.
.,A9D3 91 49    STA ($49),Y             STADY   FORPNT
.,A9D5 60       RTS                     RTS>
.,A9D6 4C D0 BB JMP $BBD0       COPFLT: JMP     MOVVF           ;PUT NUMBER @FORPNT.
                                
                                COPSTR:
.,A9D9 68       PLA             IFN     INTPRC,<PLA>            ;IF STRING, NO INTFLG.
                                INPCOM:
                                IFN     TIME,<
.,A9DA A4 4A    LDY $4A                 LDY     FORPNT+1        ;TI$?
.,A9DC C0 BF    CPY #$BF                CPYI    ZERO/256        ;ONLY TI$ CAN BE THIS ON ASSIG.
.,A9DE D0 4C    BNE $AA2C               BNE     GETSPT          ; WAS NOT TI$.
.,A9E0 20 A6 B6 JSR $B6A6               JSR     FREFAC          ;WE WONT NEEDIT.
.,A9E3 C9 06    CMP #$06                CMPI    6               ;LENGTH CORRECT?
.,A9E5 D0 3D    BNE $AA24               BNE     FCERR2
.,A9E7 A0 00    LDY #$00                LDYI    0               ;YES. DO SETUP.
.,A9E9 84 61    STY $61                 STY     FACEXP          ;ZERO FAC TO START WITH.
.,A9EB 84 66    STY $66                 STY     FACSGN
.,A9ED 84 71    STY $71         TIMELP: STY     FBUFPT          ;SAVE POSOTION.
.,A9EF 20 1D AA JSR $AA1D               JSR     TIMNUM          ;GET A DIGIT.
.,A9F2 20 E2 BA JSR $BAE2               JSR     MUL10           ;WHOLE QTY BY 10.
.,A9F5 E6 71    INC $71                 INC     FBUFPT
.,A9F7 A4 71    LDY $71                 LDY     FBUFPT
.,A9F9 20 1D AA JSR $AA1D               JSR     TIMNUM
.,A9FC 20 0C BC JSR $BC0C               JSR     MOVAF
.,A9FF AA       TAX                     TAX                     ;IF NUM=0 THEN NO MULT.
.,AA00 F0 05    BEQ $AA07               BEQ     NOML6           ;IF =0, GO TIT.
.,AA02 E8       INX                     INX                     ;MULT BY TWO.
.,AA03 8A       TXA                     TXA
.,AA04 20 ED BA JSR $BAED               JSR     FINML6          ;ADD IN AND MULT BY 2 GIVES *6.
.,AA07 A4 71    LDY $71         NOML6:  LDY     FBUFPT
.,AA09 C8       INY                     INY
.,AA0A C0 06    CPY #$06                CPYI    6               ;DONE ALL SIX?
.,AA0C D0 DF    BNE $A9ED               BNE     TIMELP
.,AA0E 20 E2 BA JSR $BAE2               JSR     MUL10           ;ONE LAST TIME.
.,AA11 20 9B BC JSR $BC9B               JSR     QINT            ;SHIFT IT OVER TO THE RIGHT.
.,AA14 A6 64    LDX $64                 LDXI    2
.,AA16 A4 63    LDY $63                 SEI                     ;DISALLOW INTERRUPTS.
.,AA18 A5 65    LDA $65         TIMEST: LDA     FACMOH,X
.,AA1A 4C DB FF JMP $FFDB               STA     CQTIMR,X
                                        DEX
                                        BPL     TIMEST          ;LOOP 3 TIMES.
                                        CLI                     ;TURN ON INTS AGAIN.
                                        RTS
.,AA1D B1 22    LDA ($22),Y     TIMNUM: LDADY   INDEX           ;INDEX SET UP BY FREFAC.
.,AA1F 20 80 00 JSR $0080               JSR     QNUM
.,AA22 90 03    BCC $AA27               BCC     GOTNUM
.,AA24 4C 48 B2 JMP $B248       FCERR2: JMP     FCERR           ;MUST BE NUMERIC STRING.
.,AA27 E9 2F    SBC #$2F        GOTNUM: SBCI    "0"-1           ;C IS OFF.
.,AA29 4C 7E BD JMP $BD7E               JMP     FINLOG>         ;ADD IN DIGIT TO FAC.
                                
.,AA2C A0 02    LDY #$02        GETSPT: LDYI    2               ;GET PNTR TO DESCRIPTOR.
.,AA2E B1 64    LDA ($64),Y             LDADY   FACMO
.,AA30 C5 34    CMP $34                 CMP     FRETOP+1        ;SEE IF IT POINTS INTO STRING SPACE.
.,AA32 90 17    BCC $AA4B               BCC     DNTCPY          ;IF [FRETOP],GT.[2&3,FACMO], DON'T COPY.
.,AA34 D0 07    BNE $AA3D               BNE     QVARIA          ;IT IS LESS.
.,AA36 88       DEY                     DEY
.,AA37 B1 64    LDA ($64),Y             LDADY   FACMO
.,AA39 C5 33    CMP $33                 CMP     FRETOP          ;COMPARE LOW ORDERS.
.,AA3B 90 0E    BCC $AA4B               BCC     DNTCPY
.,AA3D A4 65    LDY $65         QVARIA: LDY     FACLO
.,AA3F C4 2E    CPY $2E                 CPY     VARTAB+1        ;IF [VARTAB].GT.[FACMO], DON'T COPY.
.,AA41 90 08    BCC $AA4B               BCC     DNTCPY
.,AA43 D0 0D    BNE $AA52               BNE     COPY            ;IT IS LESS.
.,AA45 A5 64    LDA $64                 LDA     FACMO
.,AA47 C5 2D    CMP $2D                 CMP     VARTAB          ;COMPARE LOW ORDERS.
.,AA49 B0 07    BCS $AA52               BCS     COPY
.,AA4B A5 64    LDA $64         DNTCPY: LDWD    FACMO
.,AA4D A4 65    LDY $65         
.,AA4F 4C 68 AA JMP $AA68               JMP     COPYZC
.,AA52 A0 00    LDY #$00        COPY:   LDYI    0
.,AA54 B1 64    LDA ($64),Y             LDADY   FACMO
.,AA56 20 75 B4 JSR $B475               JSR     STRINI          ;GET ROOM TO COPY STRING INTO.
.,AA59 A5 50    LDA $50                 LDWD    DSCPNT          ;GET POINTER TO OLD DESCRIPTOR, SO
.,AA5B A4 51    LDY $51         
.,AA5D 85 6F    STA $6F                 STWD    STRNG1          ;MOVINS CAN FIND STRING.
.,AA5F 84 70    STY $70         
.,AA61 20 7A B6 JSR $B67A               JSR     MOVINS          ;COPY IT.
.,AA64 A9 61    LDA #$61                LDWDI   DSCTMP          ;GET POINTER TO OLD DESCRIPTOR.
.,AA66 A0 00    LDY #$00        
.,AA68 85 50    STA $50         COPYZC: STWD    DSCPNT          ;REMEMBER POINTER TO DESCRIPTOR.
.,AA6A 84 51    STY $51         
.,AA6C 20 DB B6 JSR $B6DB               JSR     FRETMS          ;FREE UP THE TEMPORARY WITHOUT
                                                                ;FREEING UP ANY STRING SPACE.
.,AA6F A0 00    LDY #$00                LDYI    0
.,AA71 B1 50    LDA ($50),Y             LDADY   DSCPNT
.,AA73 91 49    STA ($49),Y             STADY   FORPNT
.,AA75 C8       INY                     INY                     ;POINT TO STRING PNTR.
.,AA76 B1 50    LDA ($50),Y             LDADY   DSCPNT
.,AA78 91 49    STA ($49),Y             STADY   FORPNT
.,AA7A C8       INY                     INY
.,AA7B B1 50    LDA ($50),Y             LDADY   DSCPNT
.,AA7D 91 49    STA ($49),Y             STADY   FORPNT
.,AA7F 60       RTS                     RTS
                                PAGE
                                SUBTTL  PRINT CODE.
                                IFN     EXTIO,<
.,AA80 20 86 AA JSR $AA86       PRINTN: JSR     CMD             ;DOCMD
.,AA83 4C B5 AB JMP $ABB5               JMP     IODONE          ;RELEASE CHANNEL.
.,AA86 20 9E B7 JSR $B79E       CMD:    JSR     GETBYT
.,AA89 F0 05    BEQ $AA90               BEQ     SAVEIT
.,AA8B A9 2C    LDA #$2C                SYNCHK  44              ;COMMA?
.,AA8D 20 FF AE JSR $AEFF       
.,AA90 08       PHP             SAVEIT: PHP
.,AA91 86 13    STX $13                 JSR     CQOOUT          ;CHECK AND OPEN OUTPUT CHANNL.
.,AA93 20 18 E1 JSR $E118               STX     CHANNL          ;CHANNL TO OUTPUT ON.
.,AA96 28       PLP                     PLP                     ;GET STATUS BACK.
.,AA97 4C A0 AA JMP $AAA0               JMP     PRINT>
.,AA9A 20 21 AB JSR $AB21       STRDON: JSR     STRPRT
.,AA9D 20 79 00 JSR $0079       NEWCHR: JSR     CHRGOT          ;REGET LAST CHARACTER.
.,AAA0 F0 35    BEQ $AAD7       PRINT:  BEQ     CRDO            ;TERMINATOR SO TYPE CRLF.
.,AAA2 F0 43    BEQ $AAE7       PRINTC: BEQ     PRTRTS          ;HERE AFTER SEEING TAB(X) OR , OR ;
                                                                ;IN WHICH CASE A TERMINATOR DOES NOT
                                                                ;MEAN TYPE A CRLF BUT JUST RTS.
.,AAA4 C9 A3    CMP #$A3                CMPI    TABTK           ;TAB FUNCTION?
.,AAA6 F0 50    BEQ $AAF8               BEQ     TABER           ;YES.
.,AAA8 C9 A6    CMP #$A6                CMPI    SPCTK           ;SPACE FUNCTION?
.,AAAA 18       CLC                     CLC
.,AAAB F0 4B    BEQ $AAF8               BEQ     TABER
.,AAAD C9 2C    CMP #$2C                CMPI    44              ;A COMMA?
.,AAAF F0 37    BEQ $AAE8               BEQ     COMPRT          ;YES.
.,AAB1 C9 3B    CMP #$3B                CMPI    59              ;A SEMICOLON?
.,AAB3 F0 5E    BEQ $AB13               BEQ     NOTABR          ;YES.
.,AAB5 20 9E AD JSR $AD9E               JSR     FRMEVL          ;EVALUATE THE FORMULA.
.,AAB8 24 0D    BIT $0D                 BIT     VALTYP          ;A STRING?
.,AABA 30 DE    BMI $AA9A               BMI     STRDON          ;YES.
.,AABC 20 DD BD JSR $BDDD               JSR     FOUT
.,AABF 20 87 B4 JSR $B487               JSR     STRLIT          ;BUILD DESCRIPTOR.
                                IFN     REALIO-3,<
                                        LDYI    0               ;GET THE POINTER.
                                        LDADY   FACMO
                                        CLC
                                        ADC     TRMPOS          ;MAKE SURE LEN+POS.LT.WIDTH.
                                        CMP     LINWID          ;GREATER THAN LINE LENGTH?
                                                                ;REMEMBER SPACE PRINTED AFTER NUMBER.
                                        BCC     LINCHK          ;GO TYPE.
                                        JSR     CRDO>           ;YES, TYPE CRLF FIRST.
.,AAC2 20 21 AB JSR $AB21       LINCHK: JSR     STRPRT          ;PRINT THE NUMBER.
.,AAC5 20 3B AB JSR $AB3B               JSR     OUTSPC          ;PRINT A SPACE
.,AAC8 D0 D3    BNE $AA9D               BNEA    NEWCHR          ;ALWAYS GOES.
                                IFN     REALIO-4,<
                                IFN     BUFPAG,<
.,AACA A9 00    LDA #$00        FININL: LDAI    0
.,AACC 9D 00 02 STA $0200,X             STA     BUF,X
.,AACF A2 FF    LDX #$FF                LDXYI   BUF-1>
.,AAD1 A0 01    LDY #$01        IFE     BUFPAG,<
                                FININL: LDYI    0               ;PUT A ZERO AT END OF BUF.
                                        STY     BUF,X
                                        LDXI    BUF-1>          ;SETUP POINTER.
                                IFN     EXTIO,<
.,AAD3 A5 13    LDA $13                 LDA     CHANNL          ;NO CRDO IF NOT TERMINAL.
.,AAD5 D0 10    BNE $AAE7               BNE     PRTRTS>>
                                CRDO:
                                IFE     EXTIO,<
                                        LDAI    13              ;MAKE TRMPOS LESS THAN LINE LENGTH.
                                        STA     TRMPOS>
                                IFN     EXTIO,<
                                IFN     REALIO-3,<
                                        LDA     CHANNL
                                        BNE     GOCR
                                        STA     TRMPOS>
.,AAD7 A9 0D    LDA #$0D        GOCR:   LDAI    13>             ;X AND Y MUST BE PRESERVED.
.,AAD9 20 47 AB JSR $AB47               JSR     OUTDO
.,AADC 24 13    BIT $13                 LDAI    10
.,AADE 10 05    BPL $AAE5               JSR     OUTDO
.,AAE0 A9 0A    LDA #$0A        CRFIN:
.,AAE2 20 47 AB JSR $AB47       IFN     EXTIO,<
.,AAE5 49 FF    EOR #$FF        IFN     REALIO-3,<
.,AAE7 60       RTS                     LDA     CHANNL
                                        BNE     PRTRTS>>
                                IFE     NULCMD,<
                                IFN     REALIO-3,<
                                        LDAI    0
                                        STA     TRMPOS>
                                        EORI    255>
                                IFN     NULCMD,<
                                        TXA                     ;PRESERVE [ACCX]. SOME NEED IT.
                                        PHA
                                        LDX     NULCNT          ;GET NUMBER OF NULLS.
                                        BEQ     CLRPOS
                                        LDAI    0
                                PRTNUL: JSR     OUTDO
                                        DEX                     ;DONE WITH NULLS?
                                        BNE     PRTNUL
                                CLRPOS: STX     TRMPOS
                                        PLA
                                        TAX>
                                PRTRTS: RTS
                                
                                COMPRT: LDA     TRMPOS
                                NCMPOS==<<<LINLEN/CLMWID>-1>*CLMWID>    ;CLMWID BEYOND WHICH THERE ARE
                                IFN     REALIO-3,<
                                                                ;NO MORE COMMA FIELDS.
                                        CMP     NCMWID          ;SO ALL COMMA DOES IS "CRDO".
                                
.,AAE8 38       SEC                     BCC     MORCOM
.,AAE9 20 F0 FF JSR $FFF0               JSR     CRDO            ;TYPE CRLF.
.,AAEC 98       TYA                     JMP     NOTABR>         ;AND QUIT IF BEYOND LAST FIELD.
.,AAED 38       SEC             MORCOM: SEC
.,AAEE E9 0A    SBC #$0A        MORCO1: SBCI    CLMWID          ;GET [A] MODULUS CLMWID.
.,AAF0 B0 FC    BCS $AAEE               BCS     MORCO1
.,AAF2 49 FF    EOR #$FF                EORI    255             ;FILL PRINT POS OUT TO EVEN CLMWID SO
.,AAF4 69 01    ADC #$01                ADCI    1
.,AAF6 D0 16    BNE $AB0E               BNE     ASPAC           ;PRINT [A] SPACES.
                                
.,AAF8 08       PHP             TABER:  PHP                     ;REMEMBER IF SPC OR TAB FUNCTION.
.,AAF9 38       SEC                     JSR     GTBYTC          ;GET VALUE INTO ACCX.
.,AAFA 20 F0 FF JSR $FFF0       
.,AAFD 84 09    STY $09         
.,AAFF 20 9B B7 JSR $B79B       
.,AB02 C9 29    CMP #$29                CMPI    41
.,AB04 D0 59    BNE $AB5F               BNE     SNERR4
.,AB06 28       PLP                     PLP
.,AB07 90 06    BCC $AB0F               BCC     XSPAC           ;PRINT [X] SPACES.
.,AB09 8A       TXA                     TXA
.,AB0A E5 09    SBC $09                 SBC     TRMPOS
.,AB0C 90 05    BCC $AB13               BCC     NOTABR          ;NEGATIVE, DON'T PRINT ANY.
.,AB0E AA       TAX             ASPAC:  TAX
.,AB0F E8       INX             XSPAC:  INX
.,AB10 CA       DEX             XSPAC2: DEX                     ;DECREMENT THE COUNT.
.,AB11 D0 06    BNE $AB19               BNE     XSPAC1
.,AB13 20 73 00 JSR $0073       NOTABR: JSR     CHRGET          ;REGET LAST CHARACTER.
.,AB16 4C A2 AA JMP $AAA2               JMP     PRINTC          ;DON'T CALL CRDO.
.,AB19 20 3B AB JSR $AB3B       XSPAC1: JSR     OUTSPC
.,AB1C D0 F2    BNE $AB10               BNEA    XSPAC2
                                ;
                                ; PRINT THE STRING POINTED TO BY [Y,A] WHICH ENDS WITH A ZERO.
                                ; IF THE STRING IS BELOW DSCTMP IT WILL BE COPIED INTO STRING SPACE.
                                ;
.,AB1E 20 87 B4 JSR $B487       STROUT: JSR     STRLIT          ;GET A STRING LITERAL.
                                ;
                                ; PRINT THE STRING WHOSE DESCRIPTOR IS POINTED TO BY FACMO.
                                ;
.,AB21 20 A6 B6 JSR $B6A6       STRPRT: JSR     FREFAC          ;RETURN TEMP POINTER.
.,AB24 AA       TAX                     TAX                     ;PUT COUNT INTO COUNTER.
.,AB25 A0 00    LDY #$00                LDYI    0
.,AB27 E8       INX                     INX                     ;MOVE ONE AHEAD.
.,AB28 CA       DEX             STRPR2: DEX
.,AB29 F0 BC    BEQ $AAE7               BEQ     PRTRTS          ;ALL DONE.
.,AB2B B1 22    LDA ($22),Y             LDADY   INDEX           ;PNTR TO ACT STRNG SET BY FREFAC.
.,AB2D 20 47 AB JSR $AB47               JSR     OUTDO
.,AB30 C8       INY                     INY
.,AB31 C9 0D    CMP #$0D                CMPI    13
.,AB33 D0 F3    BNE $AB28               BNE     STRPR2
.,AB35 20 E5 AA JSR $AAE5               JSR     CRFIN           ;TYPE REST OF CARRIAGE RETURN.
.,AB38 4C 28 AB JMP $AB28               JMP     STRPR2          ;AND ON AND ON.
                                ;
                                ; OUTDO OUTPUTS THE CHARACTER IN ACCA, USING CNTWFL
                                ; (SUPPRESS OR NOT), TRMPOS (PRINT HEAD POSITION),
                                ; TIMING, ETCQ. NO REGISTERS ARE CHANGED.
                                ;
                                OUTSPC:
                                IFN     REALIO-3,<
                                        LDAI    " ">
                                IFE     REALIO-3,<
.,AB3B A5 13    LDA $13                 LDA     CHANNL
.,AB3D F0 03    BEQ $AB42               BEQ     CRTSKP
.,AB3F A9 20    LDA #$20                LDAI    " "
.:AB41 2C       .BYTE $2C               SKIP2
.,AB42 A9 1D    LDA #$1D        CRTSKP: LDAI    29>             ;COMMODORE'S SKIP CHARACTER.
.:AB44 2C       .BYTE $2C               SKIP2
.,AB45 A9 3F    LDA #$3F        OUTQST: LDAI    "?"
                                OUTDO:  IFN     REALIO,<
                                        BIT     CNTWFL          ;SHOULDN'T AFFECT CHANNEL I/O!
                                        BMI     OUTRTS>
                                IFN     REALIO-3,<
                                        PHA
                                        CMPI    32              ;IS THIS A PRINTING CHAR?
                                        BCC     TRYOUT          ;NO, DON'T INCLUDE IT IN TRMPOS.
                                        LDA     TRMPOS
                                        CMP     LINWID          ;LENGTH = TERMINAL WIDTH?
                                        BNE     OUTDO1
                                        JSR     CRDO            ;YES, TYPE CRLF
                                OUTDO1:
                                IFN EXTIO,<
                                        LDA     CHANNL
                                        BNE     TRYOUT>
                                INCTRM: INC     TRMPOS          ;INCREMENT COUNT.
                                TRYOUT: PLA>                    ;RESTORE THE A REGISTER
                                
                                IFE     REALIO-1,<
                                        STY     KIMY>           ;PRESERVE Y.
                                IFE     REALIO-4,<ORAI  ^O200>  ;TURN ON B7 FOR APPLE.
                                IFN     REALIO,<
.,AB47 20 0C E1 JSR $E10C       OUTLOC: JSR     OUTCH>          ;OUTPUT THE CHARACTER.
                                IFE     REALIO-1,<
                                        LDY     KIMY>           ;GET Y BACK.
                                IFE     REALIO-2,<REPEAT        4,<NOP>>
                                IFE     REALIO-4,<ANDI  ^O177>  ;GET [A] BACK FROM APPLE.
                                
                                IFE     REALIO,<
                                        TJSR    OUTSIM##>       ;CALL SIMULATOR OUTPUT ROUTINE
.,AB4A 29 FF    AND #$FF        OUTRTS: ANDI    255             ;SET Z=0.
.,AB4C 60       RTS             GETRTS: RTS
                                
                                PAGE
                                SUBTTL  INPUT AND READ CODE.
                                ;
                                ; HERE WHEN THE DATA THAT WAS TYPED IN OR IN "DATA" STATEMENTS
                                ; IS IMPROPERLY FORMATTED. FOR "INPUT" WE START AGAIN.
                                ; FOR "READ" WE GIVE A SYNTAX ERROR AT THE DATA LINE.
                                ;
.,AB4D A5 11    LDA $11         TRMNOK: LDA     INPFLG
.,AB4F F0 11    BEQ $AB62               BEQ     TRMNO1          ;IF INPUT TRY AGAIN.
                                IFN     GETCMD,<
.,AB51 30 04    BMI $AB57               BMI     GETDTL
.,AB53 A0 FF    LDY #$FF                LDYI    255             ;MAKE IT LOOK DIRECT.
.,AB55 D0 04    BNE $AB5B               BNEA    STCURL          ;ALWAYS GOES.
                                GETDTL:>
.,AB57 A5 3F    LDA $3F                 LDWD    DATLIN          ;GET DATA LINE NUMBER.
.,AB59 A4 40    LDY $40         
.,AB5B 85 39    STA $39         STCURL: STWD    CURLIN          ;MAKE IT CURRENT LINE.
.,AB5D 84 3A    STY $3A         
.,AB5F 4C 08 AF JMP $AF08       SNERR4: JMP     SNERR
                                TRMNO1:
                                IFN     EXTIO,<
.,AB62 A5 13    LDA $13                 LDA     CHANNL          ;IF NOT TERMINAL, GIVE BAD DATA.
.,AB64 F0 05    BEQ $AB6B               BEQ     DOAGIN
.,AB66 A2 18    LDX #$18                LDXI    ERRBD
.,AB68 4C 37 A4 JMP $A437               JMP     ERROR>
.,AB6B A9 0C    LDA #$0C        DOAGIN: LDWDI   TRYAGN
.,AB6D A0 AD    LDY #$AD        
.,AB6F 20 1E AB JSR $AB1E               JSR     STROUT          ;PRINT "?REDO FROM START".
.,AB72 A5 3D    LDA $3D                 LDWD    OLDTXT          ;POINT AT START
.,AB74 A4 3E    LDY $3E         
.,AB76 85 7A    STA $7A                 STWD    TXTPTR          ;OF THIS CURRENT LINE.
.,AB78 84 7B    STY $7B         
.,AB7A 60       RTS                     RTS                     ;GO TO "NEWSTT".
                                IFN     GETCMD,<
.,AB7B 20 A6 B3 JSR $B3A6       GET:    JSR     ERRDIR          ;DIRECT IS NOT OK.
                                IFN     EXTIO,<
.,AB7E C9 23    CMP #$23                CMPI    "#"             ;SEE IF "GET#".
.,AB80 D0 10    BNE $AB92               BNE     GETTTY          ;NO, JUST GET TTY INPUT.
.,AB82 20 73 00 JSR $0073               JSR     CHRGET          ;MOVE UP TO NEXT BYTE.
.,AB85 20 9E B7 JSR $B79E               JSR     GETBYT          ;GET CHANNEL INTO X
.,AB88 A9 2C    LDA #$2C                SYNCHK  44              ;COMMA?
.,AB8A 20 FF AE JSR $AEFF       
.,AB8D 86 13    STX $13                 JSR     CQOIN           ;GET CHANNEL OPEN FOR INPUT.
.,AB8F 20 1E E1 JSR $E11E               STX     CHANNL>
.,AB92 A2 01    LDX #$01        GETTTY: LDXYI   BUF+1           ;POINT TO 0.
.,AB94 A0 02    LDY #$02        IFN     BUFPAG,<
.,AB96 A9 00    LDA #$00                LDAI    0               ;TO STUFF AND TO POINT.
.,AB98 8D 01 02 STA $0201               STA     BUF+1>
                                IFE     BUFPAG,<
                                        STY     BUF+1>          ;ZERO IT.
.,AB9B A9 40    LDA #$40                LDAI    64              ;TURN ON V-BIT.
.,AB9D 20 0F AC JSR $AC0F               JSR     INPCO1          ;DO THE GET.
                                IFN     EXTIO,<
.,ABA0 A6 13    LDX $13                 LDX     CHANNL
.,ABA2 D0 13    BNE $ABB7               BNE     IORELE>         ;RELEASE.
.,ABA4 60       RTS                     RTS>
                                
                                IFN     EXTIO,<
.,ABA5 20 9E B7 JSR $B79E       INPUTN: JSR     GETBYT          ;GET CHANNEL NUMBER.
.,ABA8 A9 2C    LDA #$2C                SYNCHK  44              ;A COMMA?
.,ABAA 20 FF AE JSR $AEFF       
.,ABAD 86 13    STX $13                 JSR     CQOIN           ;GO WHERE COMMODORE CHECKS IN OPEN.
.,ABAF 20 1E E1 JSR $E11E               STX     CHANNL
.,ABB2 20 CE AB JSR $ABCE               JSR     NOTQTI          ;DO INPUT TO VARIABLES.
.,ABB5 A5 13    LDA $13         IODONE: LDA     CHANNL          ;RELEASE CHANNEL.
.,ABB7 20 CC FF JSR $FFCC       IORELE: JSR     CQCCHN
.,ABBA A2 00    LDX #$00                LDXI    0               ;RESET CHANNEL TO TERMINAL.
.,ABBC 86 13    STX $13                 STX     CHANNL
.,ABBE 60       RTS                     RTS>
                                INPUT:  IFN     REALIO,<
                                        LSR     CNTWFL>         ;BE TALKATIVE.
.,ABBF C9 22    CMP #$22                CMPI    34              ;A QUOTE?
.,ABC1 D0 0B    BNE $ABCE               BNE     NOTQTI          ;NO MESSAGE.
.,ABC3 20 BD AE JSR $AEBD               JSR     STRTXT          ;LITERALIZE THE STRING IN TEXT
.,ABC6 A9 3B    LDA #$3B                SYNCHK  59              ;MUST END WITH SEMICOLON.
.,ABC8 20 FF AE JSR $AEFF       
.,ABCB 20 21 AB JSR $AB21               JSR     STRPRT          ;PRINT IT OUT.
.,ABCE 20 A6 B3 JSR $B3A6       NOTQTI: JSR     ERRDIR          ;USE COMMON ROUTINE SINCE DEF DIRECT
.,ABD1 A9 2C    LDA #$2C                LDAI    44              ;GET COMMA.
.,ABD3 8D FF 01 STA $01FF               STA     BUF-1
                                                                ;IS ALSO ILLEGAL.
.,ABD6 20 F9 AB JSR $ABF9       GETAGN: JSR     QINLIN          ;TYPE "?" AND INPUT A LINE OF TEXT.
                                IFN     EXTIO,<
.,ABD9 A5 13    LDA $13                 LDA     CHANNL
.,ABDB F0 0D    BEQ $ABEA               BEQ     BUFFUL
.,ABDD 20 B7 FF JSR $FFB7               LDA     CQSTAT          ;GET STATUS BYTE.
.,ABE0 29 02    AND #$02                ANDI    2
.,ABE2 F0 06    BEQ $ABEA               BEQ     BUFFUL          ;A-OK.
.,ABE4 20 B5 AB JSR $ABB5               JSR     IODONE          ;BAD. CLOSE CHANNEL.
.,ABE7 4C F8 A8 JMP $A8F8               JMP     DATA            ;SKIP REST OF INPUT.
                                BUFFUL:>
.,ABEA AD 00 02 LDA $0200               LDA     BUF             ;ANYTHING INPUT?
.,ABED D0 1E    BNE $AC0D               BNE     INPCON          ;YES, CONTINUE.
                                IFN     EXTIO,<
.,ABEF A5 13    LDA $13                 LDA     CHANNL          ;BLANK LINE MEANS GET ANOTHER.
.,ABF1 D0 E3    BNE $ABD6               BNE     GETAGN>         ;IF NOT TERMINAL.
.,ABF3 20 06 A9 JSR $A906               CLC                     ;MAKE SURE DONT PRINT BREAK
.,ABF6 4C FB A8 JMP $A8FB               JMP     STPEND          ;NO, STOP.
                                QINLIN:
                                IFN     EXTIO,<
.,ABF9 A5 13    LDA $13                 LDA     CHANNL
.,ABFB D0 06    BNE $AC03               BNE     GINLIN>
.,ABFD 20 45 AB JSR $AB45               JSR     OUTQST
.,AC00 20 3B AB JSR $AB3B               JSR     OUTSPC
.,AC03 4C 60 A5 JMP $A560       GINLIN: JMP     INLIN
.,AC06 A6 41    LDX $41         READ:   LDXY    DATPTR          ;GET LAST DATA LOCATION.
.,AC08 A4 42    LDY $42         
.,AC0A A9 98    LDA #$98                XWD     ^O1000,^O251    ;LDAI TYA TO MAKE IT NONZERO.
                                IFE     BUFPAG,<
                                INPCON: >
                                        TYA
                                IFN     BUFPAG,<
.:AC0C 2C       .BYTE $2C               SKIP2
.,AC0D A9 00    LDA #$00        INPCON: LDAI    0>              ;SET FLAG THAT THIS IS INPUT
.,AC0F 85 11    STA $11         INPCO1: STA     INPFLG          ;STORE THE FLAG.
                                ;
                                ; IN THE PROCESSING OF DATA AND READ STATEMENTS:
                                ; ONE POINTER POINTS TO THE DATA (IE, THE NUMBERS BEING FETCHED)
                                ; AND ANOTHER POINTS TO THE LIST OF VARIABLES.
                                ;
                                ; THE POINTER INTO THE DATA ALWAYS STARTS POINTING TO A
                                ; TERMINATOR -- A , : OR END-OF-LINE.
                                ;
                                ; AT THIS POINT TXTPTR POINTS TO LIST OF VARIABLES AND
                                ; [Y,X] POINTS TO DATA OR INPUT LINE.
                                ;
.,AC11 86 43    STX $43                 STXY    INPPTR
.,AC13 84 44    STY $44         
.,AC15 20 8B B0 JSR $B08B       INLOOP: JSR     PTRGET          ;READ VARIABLE LIST.
.,AC18 85 49    STA $49                 STWD    FORPNT          ;SAVE POINTER FOR "LET" STRING STUFFING.
.,AC1A 84 4A    STY $4A                                         ;RETURNS PNTR TOP VAR IN VARPNT.
.,AC1C A5 7A    LDA $7A                 LDWD    TXTPTR          ;SAVE TEXT PNTR.
.,AC1E A4 7B    LDY $7B         
.,AC20 85 4B    STA $4B                 STWD    VARTXT
.,AC22 84 4C    STY $4C         
.,AC24 A6 43    LDX $43                 LDXY    INPPTR
.,AC26 A4 44    LDY $44         
.,AC28 86 7A    STX $7A                 STXY    TXTPTR
.,AC2A 84 7B    STY $7B         
.,AC2C 20 79 00 JSR $0079               JSR     CHRGOT          ;GET IT AND SET Z IF TERM.
.,AC2F D0 20    BNE $AC51               BNE     DATBK1
.,AC31 24 11    BIT $11                 BIT     INPFLG
                                IFN     GETCMD,<
.,AC33 50 0C    BVC $AC41               BVC     QDATA
.,AC35 20 24 E1 JSR $E124               JSR     CZGETL          ;DON'T WANT INCHR. JUST ONE.
                                IFE     REALIO-4,<
                                        ANDI    127>
.,AC38 8D 00 02 STA $0200               STA     BUF             ;MAKE IT FIRST CHARACTER.
.,AC3B A2 FF    LDX #$FF                LDXYI   <BUF-1>         ;POINT JUST BEFORE IT.
.,AC3D A0 01    LDY #$01        IFE     BUFPAG,<
.,AC3F D0 0C    BNE $AC4D               BEQA    DATBK>
.,AC41 30 75    BMI $ACB8       
                                IFN     BUFPAG,<
                                        BNEA    DATBK>>         ;GO PROCESS.
                                QDATA:  BMI     DATLOP          ;SEARCH FOR ANOTHER DATA STATEMENT.
                                IFN     EXTIO,<
.,AC43 A5 13    LDA $13                 LDA     CHANNL
.,AC45 D0 03    BNE $AC4A               BNE     GETNTH>
.,AC47 20 45 AB JSR $AB45               JSR     OUTQST
.,AC4A 20 F9 AB JSR $ABF9       GETNTH: JSR     QINLIN          ;GET ANOTHER LINE.
.,AC4D 86 7A    STX $7A         DATBK:  STXY    TXTPTR          ;SET FOR "CHRGET".
.,AC4F 84 7B    STY $7B         
.,AC51 20 73 00 JSR $0073       DATBK1: JSR     CHRGET
.,AC54 24 0D    BIT $0D                 BIT     VALTYP          ;GET VALUE TYPE.
.,AC56 10 31    BPL $AC89               BPL     NUMINS          ;INPUT A NUMBER IF NUMERIC.
                                IFN     GETCMD,<
.,AC58 24 11    BIT $11                 BIT     INPFLG          ;GET?
.,AC5A 50 09    BVC $AC65               BVC     SETQUT          ;NO, GO SET QUOTE.
.,AC5C E8       INX                     INX
.,AC5D 86 7A    STX $7A                 STX     TXTPTR
.,AC5F A9 00    LDA #$00                LDAI    0               ;ZERO TERMINATORS.
.,AC61 85 07    STA $07                 STA     CHARAC
.,AC63 F0 0C    BEQ $AC71               BEQA    RESETC>
.,AC65 85 07    STA $07         SETQUT: STA     CHARAC          ;ASSUME QUOTED STRING.
.,AC67 C9 22    CMP #$22                CMPI    34              ;TERMINATORS OK?
.,AC69 F0 07    BEQ $AC72               BEQ     NOWGET          ;YES.
.,AC6B A9 3A    LDA #$3A                LDAI    ":"             ;SET TERMINATORS TO ":" AND
.,AC6D 85 07    STA $07                 STA     CHARAC
.,AC6F A9 2C    LDA #$2C                LDAI    44              ;COMMA.
.,AC71 18       CLC             RESETC: CLC
.,AC72 85 08    STA $08         NOWGET: STA     ENDCHR
.,AC74 A5 7A    LDA $7A                 LDWD    TXTPTR
.,AC76 A4 7B    LDY $7B         
.,AC78 69 00    ADC #$00                ADCI    0               ;C IS SET PROPERLY ABOVE.
.,AC7A 90 01    BCC $AC7D               BCC     NOWGE1
.,AC7C C8       INY                     INY
.,AC7D 20 8D B4 JSR $B48D       NOWGE1: JSR     STRLT2          ;MAKE A STRING DESCRIPTOR FOR THE VALUE
                                                                ;AND COPY IF NECESSARY.
.,AC80 20 E2 B7 JSR $B7E2               JSR     ST2TXT          ;SET TEXT POINTER.
.,AC83 20 DA A9 JSR $A9DA               JSR     INPCOM          ;DO ASSIGNMENT.
.,AC86 4C 91 AC JMP $AC91               JMP     STRDN2
.,AC89 20 F3 BC JSR $BCF3       NUMINS: JSR     FIN
                                IFE     INTPRC,<
                                        JSR     MOVVF>
                                IFN     INTPRC,<
.,AC8C A5 0E    LDA $0E                 LDA     INTFLG          ;SET CODES ON FLAG.
.,AC8E 20 C2 A9 JSR $A9C2               JSR     QINTGR>         ;GO DECIDE ON FLOAT.
.,AC91 20 79 00 JSR $0079       STRDN2: JSR     CHRGOT          ;READ LAST CHARACTER.
.,AC94 F0 07    BEQ $AC9D               BEQ     TRMOK           ;":" OR EOL IS OK.
.,AC96 C9 2C    CMP #$2C                CMPI    44              ;A COMMA?
.,AC98 F0 03    BEQ $AC9D               JNE     TRMNOK
.,AC9A 4C 4D AB JMP $AB4D       
.,AC9D A5 7A    LDA $7A         TRMOK:  LDWD    TXTPTR
.,AC9F A4 7B    LDY $7B         
.,ACA1 85 43    STA $43                 STWD    INPPTR          ;SAVE FOR MORE READS.
.,ACA3 84 44    STY $44         
.,ACA5 A5 4B    LDA $4B                 LDWD    VARTXT
.,ACA7 A4 4C    LDY $4C         
.,ACA9 85 7A    STA $7A                 STWD    TXTPTR          ;POINT TO VARIABLE LIST.
.,ACAB 84 7B    STY $7B         
.,ACAD 20 79 00 JSR $0079               JSR     CHRGOT          ;LOOK AT LAST VARIABLE LIST CHARACTER.
.,ACB0 F0 2D    BEQ $ACDF               BEQ     VAREND          ;THAT'S THE END OF THE LIST.
.,ACB2 20 FD AE JSR $AEFD               JSR     CHKCOM          ;NOT END. CHECK FOR COMMA.
.,ACB5 4C 15 AC JMP $AC15               JMP     INLOOP
                                ;
                                ; SUBROUTINE TO FIND DATA
                                ; THE SEARCH IS MADE BY USING THE EXECUTION CODE FOR DATA TO
                                ; SKIP OVER STATEMENTS. THE START WORD OF EACH STATEMENT
                                ; IS COMPARED WITH "DATATK". EACH NEW LINE NUMBER
                                ; IS STORED IN "DATLIN" SO THAT IF AN ERROR OCCURS
                                ; WHILE READING DATA THE ERROR MESSAGE CAN GIVE THE LINE
                                ; NUMBER OF THE ILL-FORMATTED DATA.
                                ;
.,ACB8 20 06 A9 JSR $A906       DATLOP: JSR     DATAN           ;SKIP SOME TEXT.
.,ACBB C8       INY                     INY
.,ACBC AA       TAX                     TAX                     ;END OF LINE?
.,ACBD D0 12    BNE $ACD1               BNE     NOWLIN          ;SHO AIN'T.
.,ACBF A2 0D    LDX #$0D                LDXI    ERROD           ;YES = "NO DATA" ERROR.
.,ACC1 C8       INY                     INY
.,ACC2 B1 7A    LDA ($7A),Y             LDADY   TXTPTR
.,ACC4 F0 6C    BEQ $AD32               BEQ     ERRGO5
.,ACC6 C8       INY                     INY
.,ACC7 B1 7A    LDA ($7A),Y             LDADY   TXTPTR          ;GET HIGH BYTE OF LINE NUMBER.
.,ACC9 85 3F    STA $3F                 STA     DATLIN
.,ACCB C8       INY                     INY
.,ACCC B1 7A    LDA ($7A),Y             LDADY   TXTPTR          ;GET LOW BYTE.
.,ACCE C8       INY                     INY
.,ACCF 85 40    STA $40                 STA     DATLIN+1
.,ACD1 20 FB A8 JSR $A8FB       NOWLIN: LDADY   TXTPTR          ;HOW IS IT?
.,ACD4 20 79 00 JSR $0079               TAX
.,ACD7 AA       TAX                     JSR     ADDON           ;ADD [Y] TO [TXTPTR].
.,ACD8 E0 83    CPX #$83                CPXI    DATATK          ;IS IT A "DATA" STATEMENT.
.,ACDA D0 DC    BNE $ACB8               BNE     DATLOP          ;NOT QUITE RIGHT. KEEP LOOKING.
.,ACDC 4C 51 AC JMP $AC51               JMP     DATBK1          ;THIS IS THE ONE !
.,ACDF A5 43    LDA $43         VAREND: LDWD    INPPTR          ;PUT AWAY A NEW DATA PNTR MAYBE.
.,ACE1 A4 44    LDY $44         
.,ACE3 A6 11    LDX $11                 LDX     INPFLG
.,ACE5 10 03    BPL $ACEA               BPL     VARY0
.,ACE7 4C 27 A8 JMP $A827               JMP     RESFIN
.,ACEA A0 00    LDY #$00        VARY0:  LDYI    0
.,ACEC B1 43    LDA ($43),Y             LDADY   INPPTR          ;LAST DATA CHR COULD HAVE BEEN
                                                                ;COMMA OR COLON BUT SHOULD BE NULL.
.,ACEE F0 0B    BEQ $ACFB               BEQ     INPRTS          ;IT IS NULL.
                                IFN     EXTIO,<
.,ACF0 A5 13    LDA $13                 LDA     CHANNL          ;IF NOT TERMINAL, NO TYPE.
.,ACF2 D0 07    BNE $ACFB               BNE     INPRTS>
.,ACF4 A9 FC    LDA #$FC                LDWDI   EXIGNT
.,ACF6 A0 AC    LDY #$AC        
.,ACF8 4C 1E AB JMP $AB1E               JMP     STROUT          ;TYPE "?EXTRA IGNORED"
.,ACFB 60       RTS             INPRTS: RTS                     ;DO NEXT STATEMENT.
.:ACFC 3F 45 58 54 52 41 20 49  EXIGNT: DT"?EXTRA IGNORED"
.:AD04 47 4E 4F 52 45 44 0D 00          ACRLF
.:AD0C 3F 52 45 44 4F 20 46 52          0
.:AD14 4F 4D 20 53 54 41 52 54  TRYAGN: DT"?REDO FROM START"
.:AD1C 0D 00                            ACRLF
                                        0
                                PAGE
                                SUBTTL  THE NEXT CODE IS THE "NEXT CODE"
                                ;
                                ; A "FOR" ENTRY ON THE STACK HAS THE FOLLOWING FORMAT:
                                ;
                                ; LOW ADDRESS
                                ;       TOKEN (FORTK) 1 BYTE
                                ;       A POINTER TO THE LOOP VARIABLE 2 BYTES
                                ;       THE STEP 4+ADDPRC BYTES
                                ;       A BYTE REFLECTING THE SIGN OF THE INCREMENT 1 BYTE
                                ;       THE UPPER VALUE (PACKED) 4+ADDPRC BYTES
                                ;       THE LINE NUMBER OF THE "FOR" STATEMENT 2 BYTES
                                ;       A TEXT POINTER INTO THE "FOR" STATEMENT 2 BYTES
                                ; HIGH ADDRESS
                                ;
                                ; TOTAL 16+2*ADDPRC BYTES.
                                ;
.,AD1E D0 04    BNE $AD24       NEXT:   BNE     GETFOR
.,AD20 A0 00    LDY #$00                LDYI    0               ;WITHOUT ARG CALL "FNDFOR" WITH
.,AD22 F0 03    BEQ $AD27               BEQA    STXFOR          ;[FORPNT]=0.
.,AD24 20 8B B0 JSR $B08B       GETFOR: JSR     PTRGET          ;GET A POINTER TO LOOP VARIABLE
.,AD27 85 49    STA $49         STXFOR: STWD    FORPNT          ;INTO "FORPNT".
.,AD29 84 4A    STY $4A         
.,AD2B 20 8A A3 JSR $A38A               JSR     FNDFOR          ;FIND THE MATCHING ENTRY IF ANY.
.,AD2E F0 05    BEQ $AD35               BEQ     HAVFOR
.,AD30 A2 0A    LDX #$0A                LDXI    ERRNF           ;"NEXT WITHOUT FOR".
.,AD32 4C 37 A4 JMP $A437       ERRGO5: BEQ     ERRGO4
.,AD35 9A       TXS             HAVFOR: TXS                     ;SETUP STACK. CHOP FIRST.
.,AD36 8A       TXA                     TXA
.,AD37 18       CLC                     CLC
.,AD38 69 04    ADC #$04                ADCI    4               ;POINT TO INCREMENT
.,AD3A 48       PHA                     PHA                     ;SAVE THIS POINTER TO RESTORE TO [A]
.,AD3B 69 06    ADC #$06                ADCI    5+ADDPRC        ;POINT TO UPPER LIMIT
.,AD3D 85 24    STA $24                 STA     INDEX2          ;SAVE AS INDEX
.,AD3F 68       PLA                     PLA                     ;RESTORE POINTER TO INCREMENT
.,AD40 A0 01    LDY #$01                LDYI    1               ;SET HI ADDR OF THING TO MOVE.
.,AD42 20 A2 BB JSR $BBA2               JSR     MOVFM           ;GET QUANTITY INTO THE FAC.
.,AD45 BA       TSX                     TSX
.,AD46 BD 09 01 LDA $0109,X             LDA     257+7+ADDPRC,X, ;SET SIGN CORRECTLY.
.,AD49 85 66    STA $66                 STA     FACSGN
.,AD4B A5 49    LDA $49                 LDWD    FORPNT
.,AD4D A4 4A    LDY $4A         
.,AD4F 20 67 B8 JSR $B867               JSR     FADD            ;ADD INC TO LOOP VARIABLE.
.,AD52 20 D0 BB JSR $BBD0               JSR     MOVVF           ;PACK THE FAC INTO MEMORY.
.,AD55 A0 01    LDY #$01                LDYI    1
.,AD57 20 5D BC JSR $BC5D               JSR     FCOMPN          ;COMPARE FAC WITH UPPER VALUE.
.,AD5A BA       TSX                     TSX
.,AD5B 38       SEC                     SEC
.,AD5C FD 09 01 SBC $0109,X             SBC     257+7+ADDPRC,X, ;SUBTRACT SIGN OF INC FROM SIGN OF
                                                                ;OF (CURRENT VALUE-FINAL VALUE).
.,AD5F F0 17    BEQ $AD78               BEQ     LOOPDN          ;IF SIGN (FINAL-CURRENT)-SIGN STEP=0
                                                                ;THEN LOOP IS DONE.
.,AD61 BD 0F 01 LDA $010F,X             LDA     2*ADDPRC+12+257,X
.,AD64 85 39    STA $39                 STA     CURLIN          ;STORE LINE NUMBER OF "FOR" STATEMENT.
.,AD66 BD 10 01 LDA $0110,X             LDA     257+13+<2*ADDPRC>,X
.,AD69 85 3A    STA $3A                 STA     CURLIN+1
.,AD6B BD 12 01 LDA $0112,X             LDA     2*ADDPRC+15+257,X
.,AD6E 85 7A    STA $7A                 STA     TXTPTR          ;STORE TEXT PNTR INTO "FOR" STATEMENT.
.,AD70 BD 11 01 LDA $0111,X             LDA     2*ADDPRC+14+257,X
.,AD73 85 7B    STA $7B                 STA     TXTPTR+1
.,AD75 4C AE A7 JMP $A7AE       NEWSGO: JMP     NEWSTT          ;PROCESS NEXT STATEMENT.
.,AD78 8A       TXA             LOOPDN: TXA
.,AD79 69 11    ADC #$11                ADCI    2*ADDPRC+15             ;ADDS 16 WITH CARRY.
.,AD7B AA       TAX                     TAX
.,AD7C 9A       TXS                     TXS                     ;NEW STACK PNTR.
.,AD7D 20 79 00 JSR $0079               JSR     CHRGOT
.,AD80 C9 2C    CMP #$2C                CMPI    44              ;COMMA AT END?
.,AD82 D0 F1    BNE $AD75               BNE     NEWSGO
.,AD84 20 73 00 JSR $0073               JSR     CHRGET
.,AD87 20 24 AD JSR $AD24               JSR     GETFOR          ;DO NEXT BUT DON'T ALLOW BLANK VARIABLE
                                                                ;PNTR. [VARPNT] IS THE STK PNTR WHICH
                                                                ;NEVER MATCHES ANY POINTER.
                                                                ;JSR TO PUT ON DUMMY NEWSTT ADDR.
                                SUBTTL FORMULA EVALUATION CODE.
                                ;
                                ; THESE ROUTINES CHECK FOR CERTAIN "VALTYP".
                                ; [C] IS NOT PRESERVED.
                                ;
.,AD8A 20 9E AD JSR $AD9E       FRMNUM: JSR     FRMEVL
.,AD8D 18       CLC             CHKNUM: CLC
.:AD8E 24       .BYTE $24               SKIP1
.,AD8F 38       SEC             CHKSTR: SEC                     ;SET CARRY.
.,AD90 24 0D    BIT $0D         CHKVAL: BIT     VALTYP          ;WILL NOT F UP "VALTYP".
.,AD92 30 03    BMI $AD97               BMI     DOCSTR
.,AD94 B0 03    BCS $AD99               BCS     CHKERR
.,AD96 60       RTS             CHKOK:  RTS
.,AD97 B0 FD    BCS $AD96       DOCSTR: BCS     CHKOK
.,AD99 A2 16    LDX #$16        CHKERR: LDXI    ERRTM
.,AD9B 4C 37 A4 JMP $A437       ERRGO4: JMP     ERROR
                                ;
                                ; THE FORMULA EVALUATOR STARTS WITH
                                ; [TXTPTR] POINTING TO THE FIRST CHARACTER OF THE FORMULA.
                                ; AT THE END [TXTPTR] POINTS TO THE TERMINATOR.
                                ; THE RESULT IS LEFT IN THE FAC.
                                ; ON RETURN [A] DOES NOT REFLECT THE TERMINATOR.
                                ;
                                ; THE FORMULA EVALUATOR USES THE OPERATOR LIST (OPTAB)
                                ; TO DETERMINE PRECEDENCE AND DISPATCH ADDRESSES FOR
                                ; EACH OPERATOR.
                                ; A TEMPORARY RESULT ON THE STACK HAS THE FOLLOWING FORMAT.
                                ;       THE ADDRESS OF THE OPERATOR ROUTINE.
                                ;       THE FLOATING POINT TEMPORARY RESULT.
                                ;       THE PRECEDENCE OF THE OPERATOR.
                                ;
.,AD9E A6 7A    LDX $7A         FRMEVL: LDX     TXTPTR
.,ADA0 D0 02    BNE $ADA4               BNE     FRMEV1
.,ADA2 C6 7B    DEC $7B                 DEC     TXTPTR+1
.,ADA4 C6 7A    DEC $7A         FRMEV1: DEC     TXTPTR
.,ADA6 A2 00    LDX #$00                LDXI    0               ;INITIAL DUMMY PRECEDENCE IS 0.
.:ADA8 24       .BYTE $24               SKIP1
.,ADA9 48       PHA             LPOPER: PHA                     ;SAVE LOW PRECEDENCE. (MASK.)
.,ADAA 8A       TXA                     TXA
.,ADAB 48       PHA                     PHA                     ;SAVE HIGH PRECEDENCE.
.,ADAC A9 01    LDA #$01                LDAI    1
.,ADAE 20 FB A3 JSR $A3FB               JSR     GETSTK          ;MAKE SURE THERE IS ROOM FOR
                                                                ;RECURSIVE CALLS.
.,ADB1 20 83 AE JSR $AE83               JSR     EVAL            ;EVALUATE SOMETHING.
.,ADB4 A9 00    LDA #$00                CLR     OPMASK          ;PREPARE TO BUILD MASK MAYBE.
.,ADB6 85 4D    STA $4D         
.,ADB8 20 79 00 JSR $0079       TSTOP:  JSR     CHRGOT          ;REGET LAST CHARACTER.
.,ADBB 38       SEC             LOPREL: SEC                     ;PREP TO SUBTRACT.
.,ADBC E9 B1    SBC #$B1                SBCI    GREATK          ;IS CURRENT CHARACTER A RELATION?
.,ADBE 90 17    BCC $ADD7               BCC     ENDREL          ;NO. RELATIONS ALL THROUGH.
.,ADC0 C9 03    CMP #$03                CMPI    LESSTK-GREATK+1 ;REALLY RELATIONAL?
.,ADC2 B0 13    BCS $ADD7               BCS     ENDREL          ;NO -- JUST BIG.
.,ADC4 C9 01    CMP #$01                CMPI    1               ;RESET CARRY FOR ZERO ONLY.
.,ADC6 2A       ROL                     ROL     A,              ;0 TO 1, 1 TO 2, 2 TO 4.
.,ADC7 49 01    EOR #$01                EORI    1
.,ADC9 45 4D    EOR $4D                 EOR     OPMASK          ;BRING IN THE OLD BITS.
.,ADCB C5 4D    CMP $4D                 CMP     OPMASK          ;MAKE SURE THE NEW MASK IS BIGGER.
.,ADCD 90 61    BCC $AE30               BCC     SNERR5          ;SYNTAX ERROR. BECAUSE TWO OF THE SAME.
.,ADCF 85 4D    STA $4D                 STA     OPMASK          ;SAVE MASK.
.,ADD1 20 73 00 JSR $0073               JSR     CHRGET
.,ADD4 4C BB AD JMP $ADBB               JMP     LOPREL          ;GET THE NEXT CANDIDATE.
.,ADD7 A6 4D    LDX $4D         ENDREL: LDX     OPMASK          ;WERE THERE ANY?
.,ADD9 D0 2C    BNE $AE07               BNE     FINREL          ;YES, HANDLE AS SPECIAL OP.
.,ADDB B0 7B    BCS $AE58               BCS     QOP             ;NOT AN OPERATOR.
.,ADDD 69 07    ADC #$07                ADCI    GREATK-PLUSTK
.,ADDF 90 77    BCC $AE58               BCC     QOP             ;NOT AN OPERATOR.
.,ADE1 65 0D    ADC $0D                 ADC     VALTYP          ;[C]=1.
.,ADE3 D0 03    BNE $ADE8               JEQ     CAT             ;ONLY IF [A]=0 AND [VALTYP]=-1 (A STR).
.,ADE5 4C 3D B6 JMP $B63D       
.,ADE8 69 FF    ADC #$FF                ADCI    ^O377           ;GET BACK ORIGINAL [A].
.,ADEA 85 22    STA $22                 STA     INDEX1
.,ADEC 0A       ASL                     ASL     A,              ;MULTIPLY BY 2.
.,ADED 65 22    ADC $22                 ADC     INDEX1          ;BY THREE.
.,ADEF A8       TAY                     TAY                     ;SET UP FOR LATER.
.,ADF0 68       PLA             QPREC:  PLA                     ;GET PREVIOUS PRECEDENCE.
.,ADF1 D9 80 A0 CMP $A080,Y             CMP     OPTAB,Y         ;IS OLD PRECEDENCE GREATER OR EQUAL?
.,ADF4 B0 67    BCS $AE5D               BCS     QCHNUM          ;YES, GO OPERATE.
.,ADF6 20 8D AD JSR $AD8D               JSR     CHKNUM          ;CAN'T BE STRING HERE.
.,ADF9 48       PHA             DOPREC: PHA                     ;SAVE OLD PRECEDENCE.
.,ADFA 20 20 AE JSR $AE20       NEGPRC: JSR     DOPRE1          ;SET A RETURN ADDRESS FOR OP.
.,ADFD 68       PLA                     PLA                     ;PULL OFF PREVIOUS PRECEDENCE.
.,ADFE A4 4B    LDY $4B                 LDY     OPPTR           ;GET POINTER TO OP.
.,AE00 10 17    BPL $AE19               BPL     QPREC1          ;THAT'S A REAL OPERATOR.
.,AE02 AA       TAX                     TAX                     ;DONE ?
.,AE03 F0 56    BEQ $AE5B               BEQ     QOPGO           ;DONE !
.,AE05 D0 5F    BNE $AE66               BNE     PULSTK
.,AE07 46 0D    LSR $0D         FINREL: LSR     VALTYP          ;GET VALUE TYPE INTO "C".
.,AE09 8A       TXA                     TXA
.,AE0A 2A       ROL                     ROL     A,              ;PUT VALTYP INTO LOW ORDER BIT OF MASK.
.,AE0B A6 7A    LDX $7A                 LDX     TXTPTR          ;DECREMENT TEXT POINTER.
.,AE0D D0 02    BNE $AE11               BNE     FINRE2
.,AE0F C6 7B    DEC $7B                 DEC     TXTPTR+1
.,AE11 C6 7A    DEC $7A         FINRE2: DEC     TXTPTR
.,AE13 A0 1B    LDY #$1B                LDYI    PTDORL-OPTAB    ;MAKE [YREG] POINT AT OPERATOR ENTRY.
.,AE15 85 4D    STA $4D                 STA     OPMASK          ;SAVE THE OPERATION MASK.
.,AE17 D0 D7    BNE $ADF0               BNE     QPREC           ;SAVE IT ALL. BR ALWAYS.
                                                                ;NOTE B7(VALTYP)=0 SO CHKNUM CALL IS OK.
.,AE19 D9 80 A0 CMP $A080,Y     QPREC1: CMP     OPTAB,Y         ;LAST PRECEDENCE IS GREATER?
.,AE1C B0 48    BCS $AE66               BCS     PULSTK          ;YES, GO OPERATE.
.,AE1E 90 D9    BCC $ADF9               BCC     DOPREC          ;NO SAVE ARGUMENT AND GET OTHER OPERAND.
.,AE20 B9 82 A0 LDA $A082,Y     DOPRE1: LDA     OPTAB+2,Y
.,AE23 48       PHA                     PHA                     ;DISP ADDR GOES ONTO STACK.
.,AE24 B9 81 A0 LDA $A081,Y             LDA     OPTAB+1,Y
.,AE27 48       PHA                     PHA
.,AE28 20 33 AE JSR $AE33               JSR     PUSHF1          ;SAVE FAC ON STACK UNPACKED.
.,AE2B A5 4D    LDA $4D                 LDA     OPMASK          ;[ACCA] MAY BE MASK FOR REL.
.,AE2D 4C A9 AD JMP $ADA9               JMP     LPOPER
.,AE30 4C 08 AF JMP $AF08       SNERR5: JMP     SNERR           ;GO TO AN ERROR.
.,AE33 A5 66    LDA $66         PUSHF1: LDA     FACSGN
.,AE35 BE 80 A0 LDX $A080,Y             LDX     OPTAB,Y,        ;GET HIGH PRECEDENCE.
.,AE38 A8       TAY             PUSHF:  TAY                     ;GET POINTER INTO STACK.
.,AE39 68       PLA                     PLA
.,AE3A 85 22    STA $22                 STA     INDEX1
.,AE3C E6 22    INC $22                 INC     INDEX1
.,AE3E 68       PLA                     PLA
.,AE3F 85 23    STA $23                 STA     INDEX1+1
.,AE41 98       TYA                     TYA
                                                                ;STORE FAC ON STACK UNPACKED.
.,AE42 48       PHA                     PHA                     ;START WITH SIGN SET UP.
.,AE43 20 1B BC JSR $BC1B       FORPSH: JSR     ROUND           ;PUT ROUNDED FAC ON STACK.
.,AE46 A5 65    LDA $65                 LDA     FACLO           ;ENTRY POINT TO SKIP STORING SIGN.
.,AE48 48       PHA                     PHA
.,AE49 A5 64    LDA $64                 LDA     FACMO
.,AE4B 48       PHA                     PHA
                                IFN     ADDPRC,<
.,AE4C A5 63    LDA $63                 LDA     FACMOH
.,AE4E 48       PHA                     PHA>
.,AE4F A5 62    LDA $62                 LDA     FACHO
.,AE51 48       PHA                     PHA
.,AE52 A5 61    LDA $61                 LDA     FACEXP
.,AE54 48       PHA                     PHA
.,AE55 6C 22 00 JMP ($0022)             JMPD    INDEX1          ;RETURN.
.,AE58 A0 FF    LDY #$FF        QOP:    LDYI    255
.,AE5A 68       PLA                     PLA                     ;GET HIGH PRECEDENCE OF LAST OP.
.,AE5B F0 23    BEQ $AE80       QOPGO:  BEQ     QOPRTS          ;DONE !
.,AE5D C9 64    CMP #$64        QCHNUM: CMPI    100             ;RELATIONAL OPERATOR?
.,AE5F F0 03    BEQ $AE64               BEQ     UNPSTK          ;YES, DON'T CHECK OPERAND.
.,AE61 20 8D AD JSR $AD8D               JSR     CHKNUM          ;MUST BE NUMBER.
.,AE64 84 4B    STY $4B         UNPSTK: STY     OPPTR           ;SAVE OPERATOR'S POINTER FOR NEXT TIME.
.,AE66 68       PLA             PULSTK: PLA                     ;GET MASK FOR REL OP IF IT IS ONE.
.,AE67 4A       LSR                     LSR     A,              ;SETUP [C] FOR DOREL'S "CHKVAL".
.,AE68 85 12    STA $12                 STA     DOMASK          ;SAVE FOR "DOCMP".
.,AE6A 68       PLA                     PLA                     ;UNPACK STACK INTO ARG.
.,AE6B 85 69    STA $69                 STA     ARGEXP
.,AE6D 68       PLA                     PLA
.,AE6E 85 6A    STA $6A                 STA     ARGHO
                                IFN     ADDPRC,<
.,AE70 68       PLA                     PLA
.,AE71 85 6B    STA $6B                 STA     ARGMOH>
.,AE73 68       PLA                     PLA
.,AE74 85 6C    STA $6C                 STA     ARGMO
.,AE76 68       PLA                     PLA
.,AE77 85 6D    STA $6D                 STA     ARGLO
.,AE79 68       PLA                     PLA
.,AE7A 85 6E    STA $6E                 STA     ARGSGN
.,AE7C 45 66    EOR $66                 EOR     FACSGN          ;GET PROBABLE RESULT SIGN.
.,AE7E 85 6F    STA $6F                 STA     ARISGN          ;ARITHMETIC SIGN. USED BY
                                                                ;ADD, SUB, MULT, DIV.
.,AE80 A5 61    LDA $61         QOPRTS: LDA     FACEXP          ;GET IT AND SET CODES.
.,AE82 60       RTS             UNPRTS: RTS                     ;RETURN.
.,AE83 6C 0A 03 JMP ($030A)     
.,AE86 A9 00    LDA #$00        EVAL:   CLR     VALTYP          ;ASSUME VALUE WILL BE NUMERIC.
.,AE88 85 0D    STA $0D         
.,AE8A 20 73 00 JSR $0073       EVAL0:  JSR     CHRGET          ;GET A CHARACTER.
.,AE8D B0 03    BCS $AE92               BCS     EVAL2
.,AE8F 4C F3 BC JMP $BCF3       EVAL1:  JMP     FIN             ;IT IS A NUMBER.
.,AE92 20 13 B1 JSR $B113       EVAL2:  JSR     ISLETC          ;VARIABLE NAME?
.,AE95 90 03    BCC $AE9A               BCS     ISVAR           ;YES.
.,AE97 4C 28 AF JMP $AF28       IFE     REALIO-3,<
.,AE9A C9 FF    CMP #$FF                CMPI    PI
.,AE9C D0 0F    BNE $AEAD               BNE     QDOT
.,AE9E A9 A8    LDA #$A8                LDWDI   PIVAL
.,AEA0 A0 AE    LDY #$AE        
.,AEA2 20 A2 BB JSR $BBA2               JSR     MOVFM           ;PUT VALUE IN FOR PI.
.,AEA5 4C 73 00 JMP $0073               JMP     CHRGET
.:AEA8 82 49 0F DA A1           PIVAL:  ^O202
                                        ^O111
                                        ^O017
                                        ^O332
                                        ^O241>
.,AEAD C9 2E    CMP #$2E        QDOT:   CMPI    "."             ;LEADING CHARACTER OF CONSTANT?
.,AEAF F0 DE    BEQ $AE8F               BEQ     EVAL1
.,AEB1 C9 AB    CMP #$AB                CMPI    MINUTK          ;NEGATION?
.,AEB3 F0 58    BEQ $AF0D               BEQ     DOMIN           ;SHO IS.
.,AEB5 C9 AA    CMP #$AA                CMPI    PLUSTK
.,AEB7 F0 D1    BEQ $AE8A               BEQ     EVAL0
.,AEB9 C9 22    CMP #$22                CMPI    34              ;A QUOTE? A STRING?
.,AEBB D0 0F    BNE $AECC               BNE     EVAL3
.,AEBD A5 7A    LDA $7A         STRTXT: LDWD    TXTPTR
.,AEBF A4 7B    LDY $7B         
.,AEC1 69 00    ADC #$00                ADCI    0               ;TO INC, ADD C=1.
.,AEC3 90 01    BCC $AEC6               BCC     STRTX2
.,AEC5 C8       INY                     INY
.,AEC6 20 87 B4 JSR $B487       STRTX2: JSR     STRLIT          ;YES. GO PROCESS IT.
.,AEC9 4C E2 B7 JMP $B7E2               JMP     ST2TXT
.,AECC C9 A8    CMP #$A8        EVAL3:  CMPI    NOTTK           ;CHECK FOR "NOT" OPERATOR.
.,AECE D0 13    BNE $AEE3               BNE     EVAL4
.,AED0 A0 18    LDY #$18                LDYI    NOTTAB-OPTAB            ;"NOT" HAS PRECEDENCE 90.
.,AED2 D0 3B    BNE $AF0F               BNE     GONPRC          ;GO DO ITS EVALUATION.
.,AED4 20 BF B1 JSR $B1BF       NOTOP:  JSR     AYINT           ;INTEGERIZE.
.,AED7 A5 65    LDA $65                 LDA     FACLO           ;GET THE ARGUMENT.
.,AED9 49 FF    EOR #$FF                EORI    255
.,AEDB A8       TAY                     TAY
.,AEDC A5 64    LDA $64                 LDA     FACMO
.,AEDE 49 FF    EOR #$FF                EORI    255
.,AEE0 4C 91 B3 JMP $B391               JMP     GIVAYF          ;FLOAT [Y,A] AS RESULT IN FAC.
                                                                ;AND RETURN.
.,AEE3 C9 A5    CMP #$A5        EVAL4:  CMPI    FNTK            ;USER-DEFINED FUNCTION?
.,AEE5 D0 03    BNE $AEEA               JEQ     FNDOER
.,AEE7 4C F4 B3 JMP $B3F4       
.,AEEA C9 B4    CMP #$B4                CMPI    ONEFUN          ;A FUNCTION NAME?
.,AEEC 90 03    BCC $AEF1               BCC     PARCHK          ;FUNCTIONS ARE THE HIGHEST NUMBERED
.,AEEE 4C A7 AF JMP $AFA7               JMP     ISFUN           ;CHARACTERS SO NO NEED TO CHECK
                                                                ;AN UPPER-BOUND.
.,AEF1 20 FA AE JSR $AEFA       PARCHK: JSR     CHKOPN          ;ONLY POSSIBILITY LEFT IS
.,AEF4 20 9E AD JSR $AD9E               JSR     FRMEVL          ;A FORMULA IN PARENTHESIS.
                                                                ;RECURSIVELY EVALUATE THE FORMULA.
.,AEF7 A9 29    LDA #$29        CHKCLS: LDAI    41              ;CHECK FOR A RIGHT PARENTHESE
.:AEF9 2C       .BYTE $2C               SKIP2
.,AEFA A9 28    LDA #$28        CHKOPN: LDAI    40
.:AEFC 2C       .BYTE $2C               SKIP2
.,AEFD A9 2C    LDA #$2C        CHKCOM: LDAI    44
                                ;
                                ; "SYNCHK" LOOKS AT THE CURRENT CHARACTER TO MAKE SURE IT
                                ; IS THE SPECIFIC THING LOADED INTO ACCA JUST BEFORE THE CALL TO
                                ; "SYNCHK". IF NOT, IT CALLS THE "SYNTAX ERROR" ROUTINE.
                                ; OTHERWISE IT GOBBLES THE NEXT CHAR AND RETURNS,
                                ;
                                ; [A]=NEW CHAR AND TXTPTR IS ADVANCED BY "CHRGET".
                                ;
.,AEFF A0 00    LDY #$00        SYNCHR: LDYI    0
.,AF01 D1 7A    CMP ($7A),Y             CMPDY   TXTPTR          ;CHARACTERS EQUAL?
.,AF03 D0 03    BNE $AF08               BNE     SNERR
.,AF05 4C 73 00 JMP $0073       CHRGO5: JMP     CHRGET
.,AF08 A2 0B    LDX #$0B        SNERR:  LDXI    ERRSN           ;"SYNTAX ERROR"
.,AF0A 4C 37 A4 JMP $A437               JMP     ERROR
.,AF0D A0 15    LDY #$15        DOMIN:  LDYI    NEGTAB-OPTAB    ;A PRECEDENCE BELOW "^".
.,AF0F 68       PLA             GONPRC: PLA                     ;GET RID OF RTS ADDR.
.,AF10 68       PLA                     PLA
.,AF11 4C FA AD JMP $ADFA               JMP     NEGPRC          ;EVALUTE FOR NEGATION.
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
.,AF28 20 8B B0 JSR $B08B       ISVAR:  JSR     PTRGET          ;GET A PNTR TO VARIABLE.
.,AF2B 85 64    STA $64         ISVRET: STWD    FACMO
.,AF2D 84 65    STY $65         IFN     TIME!EXTIO,<
.,AF2F A6 45    LDX $45                 LDWD    VARNAM>         ;CHECK TIME,TIME$,STATUS.
.,AF31 A4 46    LDY $46                 LDX     VALTYP
.,AF33 A5 0D    LDA $0D         
.,AF35 F0 26    BEQ $AF5D               BEQ     GOOO            ;THE STRING IS SET UP.
.,AF37 A9 00    LDA #$00                LDXI    0
.,AF39 85 70    STA $70                 STX     FACOV
                                IFN     TIME,<
.,AF3B 20 14 AF JSR $AF14               BIT     FACLO           ;AN ARRAY?
.,AF3E 90 1C    BCC $AF5C               BPL     STRRTS          ;YES.
.,AF40 E0 54    CPX #$54                CMPI    "T"             ;TI$?
.,AF42 D0 18    BNE $AF5C               BNE     STRRTS
.,AF44 C0 C9    CPY #$C9                CPYI    "I"+128
.,AF46 D0 14    BNE $AF5C               BNE     STRRTS
.,AF48 20 84 AF JSR $AF84               JSR     GETTIM          ;YES. PUT TIME IN FACMOH-LO.
.,AF4B 84 5E    STY $5E                 STY     TENEXP          ;Y=0.
.,AF4D 88       DEY                     DEY
.,AF4E 84 71    STY $71                 STY     FBUFPT
.,AF50 A0 06    LDY #$06                LDYI    6               ;SIX    DIGITS TO PRINT.
.,AF52 84 5D    STY $5D                 STY     DECCNT
.,AF54 A0 24    LDY #$24                LDYI    FDCEND-FOUTBL
.,AF56 20 68 BE JSR $BE68               JSR     FOUTIM          ;CONVERT TO ASCII.
.,AF59 4C 6F B4 JMP $B46F               JMP     TIMSTR>
.,AF5C 60       RTS             STRRTS: RTS
                                GOOO:
                                IFN     INTPRC,<
.,AF5D 24 0E    BIT $0E                 LDX     INTFLG
.,AF5F 10 0D    BPL $AF6E               BPL     GOOOOO
.,AF61 A0 00    LDY #$00                LDYI    0
.,AF63 B1 64    LDA ($64),Y             LDADY   FACMO           ;FETCH HIGH.
.,AF65 AA       TAX                     TAX
.,AF66 C8       INY                     INY
.,AF67 B1 64    LDA ($64),Y             LDADY   FACMO
.,AF69 A8       TAY                     TAY                     ;PUT LOW IN Y.
.,AF6A 8A       TXA                     TXA                     ;GET HIGH IN A.
.,AF6B 4C 91 B3 JMP $B391               JMP     GIVAYF>         ;FLOAT AND RETURN.
                                GOOOOO:
                                IFN     TIME,<
.,AF6E 20 14 AF JSR $AF14               BIT     FACLO           ;AN ARRAY?
.,AF71 90 2D    BCC $AFA0               BPL     GOMOVF          ;YES.
.,AF73 E0 54    CPX #$54                CMPI    "T"
.,AF75 D0 1B    BNE $AF92               BNE     QSTATV
.,AF77 C0 49    CPY #$49                CPYI    "I"
.,AF79 D0 25    BNE $AFA0               BNE     GOMOVF
.,AF7B 20 84 AF JSR $AF84               JSR     GETTIM
.,AF7E 98       TYA                     TYA                     ;FOR FLOATB.
.,AF7F A2 A0    LDX #$A0                LDXI    160             ;SET EXPONNENT.
.,AF81 4C 4F BC JMP $BC4F               JMP     FLOATB
.,AF84 20 DE FF JSR $FFDE       GETTIM: LDWDI   <CQTIMR-2>
.,AF87 86 64    STX $64                 SEI                     ;TURN OF INT SYS.
.,AF89 84 63    STY $63                 JSR     MOVFM
.,AF8B 85 65    STA $65                 CLI                     ;BACK ON.
.,AF8D A0 00    LDY #$00        
.,AF8F 84 62    STY $62                 STY     FACHO           ;ZERO HIGHEST.
.,AF91 60       RTS                     RTS>
                                QSTATV:
                                IFN     EXTIO,<
.,AF92 E0 53    CPX #$53                CMPI    "S"
.,AF94 D0 0A    BNE $AFA0               BNE     GOMOVF
.,AF96 C0 54    CPY #$54                CPYI    "T"
.,AF98 D0 06    BNE $AFA0               BNE     GOMOVF
.,AF9A 20 B7 FF JSR $FFB7               LDA     CQSTAT
.,AF9D 4C 3C BC JMP $BC3C               JMP     FLOAT
                                GOMOVF:>
                                IFN     TIME!EXTIO,<
.,AFA0 A5 64    LDA $64                 LDWD    FACMO>
.,AFA2 A4 65    LDY $65         
.,AFA4 4C A2 BB JMP $BBA2               JMP     MOVFM           ;MOVE ACTUAL VALUE IN.
                                                                ;AND RETURN.
                                
.,AFA7 0A       ASL             ISFUN:  ASL     A,              ;MULTIPLY BY TWO.
.,AFA8 48       PHA                     PHA
.,AFA9 AA       TAX                     TAX
.,AFAA 20 73 00 JSR $0073               JSR     CHRGET          ;SET UP FOR SYNCHK.
.,AFAD E0 8F    CPX #$8F                CPXI    2*LASNUM-256+1  ;IS IT PAST "LASNUM"?
.,AFAF 90 20    BCC $AFD1               BCC     OKNORM          ;NO, MUST BE NORMAL FUNCTION.
                                ;
                                ; MOST FUNCTIONS TAKE A SINGLE ARGUMENT.
                                ; THE RETURN ADDRESS OF THESE FUNCTIONS IS "CHKNUM"
                                ; WHICH ASCERTAINS THAT [VALTYP]=0  (NUMERIC).
                                ; NORMAL FUNCTIONS THAT RETURN STRING RESULTS
                                ; (E.G., CHR$) MUST POP OFF THAT RETURN ADDR AND
                                ; RETURN DIRECTLY TO "FRMEVL".
                                ;
                                ; THE SO-CALLED "FUNNY" FUNCTIONS CAN TAKE MORE THAN ONE ARGUMENT,
                                ; THE FIRST OF WHICH MUST BE STRING AND THE SECOND OF WHICH
                                ; MUST BE A NUMBER BETWEEN 0 AND 255.
                                ; THE CLOSED PARENTHESIS MUST BE CHECKED AND RETURN IS DIRECTLY
                                ; TO "FRMEVL" WITH THE TEXT PNTR POINTING BEYOND THE ")".
                                ; THE POINTER TO THE DESCRIPTOR OF THE STRING ARGUMENT
                                ; IS STORED ON THE STACK UNDERNEATH THE VALUE OF THE
                                ; INTEGER ARGUMENT.
                                ;
.,AFB1 20 FA AE JSR $AEFA               JSR     CHKOPN          ;CHECK FOR AN OPEN PARENTHESE
.,AFB4 20 9E AD JSR $AD9E               JSR     FRMEVL          ;EAT OPEN PAREN AND FIRST ARG.
.,AFB7 20 FD AE JSR $AEFD               JSR     CHKCOM          ;TWO ARGS SO COMMA MUST DELIMIT.
.,AFBA 20 8F AD JSR $AD8F               JSR     CHKSTR          ;MAKE SURE FIRST WAS STRING.
.,AFBD 68       PLA                     PLA                     ;GET FUNCTION NUMBER.
.,AFBE AA       TAX                     TAX
.,AFBF A5 65    LDA $65                 PSHWD   FACMO           ;SAVE POINTER AT STRING DESCRIPTOR
.,AFC1 48       PHA             
.,AFC2 A5 64    LDA $64         
.,AFC4 48       PHA             
.,AFC5 8A       TXA                     TXA
.,AFC6 48       PHA                     PHA                     ;RESAVE FUNCTION NUMBER.
                                                                ;THIS MUST BE ON STACK SINCE RECURSIVE.
.,AFC7 20 9E B7 JSR $B79E               JSR     GETBYT          ;[X]=VALUE OF FORMULA.
.,AFCA 68       PLA                     PLA                     ;GET FUNCTION NUMBER.
.,AFCB A8       TAY                     TAY
.,AFCC 8A       TXA                     TXA
.,AFCD 48       PHA                     PHA
.,AFCE 4C D6 AF JMP $AFD6               JMP     FINGO           ;DISPATCH TO FUNCTION.
.,AFD1 20 F1 AE JSR $AEF1       OKNORM: JSR     PARCHK          ;READ A FORMULA SURROUNDED BY PARENS.
.,AFD4 68       PLA                     PLA                     ;GET DISPATCH FUNCTION.
.,AFD5 A8       TAY                     TAY
.,AFD6 B9 EA 9F LDA $9FEA,Y     FINGO:  LDA     FUNDSP-2*ONEFUN+256,Y,  ;MODIFY DISPATCH ADDRESS.
.,AFD9 85 55    STA $55                 STA     JMPER+1
.,AFDB B9 EB 9F LDA $9FEB,Y             LDA     FUNDSP-2*ONEFUN+257,Y
.,AFDE 85 56    STA $56                 STA     JMPER+2
.,AFE0 20 54 00 JSR $0054               JSR     JMPER           ;DISPATCH!
                                                                ;STRING FUNCTIONS REMOVE THIS RET ADDR.
.,AFE3 4C 8D AD JMP $AD8D               JMP     CHKNUM          ;CHECK IT FOR NUMERICNESS AND RETURN.
                                
.,AFE6 A0 FF    LDY #$FF        OROP:   LDYI    255             ;MUST ALWAYS COMPLEMENT..
.:AFE8 2C       .BYTE $2C               SKIP2
.,AFE9 A0 00    LDY #$00        ANDOP:  LDYI    0
.,AFEB 84 0B    STY $0B                 STY     COUNT           ;OPERATOR.
.,AFED 20 BF B1 JSR $B1BF               JSR     AYINT           ;[FACMO&LO]=INT VALUE AND CHECK SIZE.
.,AFF0 A5 64    LDA $64                 LDA     FACMO           ;USE DEMORGAN'S LAW ON HIGH
.,AFF2 45 0B    EOR $0B                 EOR     COUNT
.,AFF4 85 07    STA $07                 STA     INTEGR
.,AFF6 A5 65    LDA $65                 LDA     FACLO           ;AND LOW.
.,AFF8 45 0B    EOR $0B                 EOR     COUNT
.,AFFA 85 08    STA $08                 STA     INTEGR+1
.,AFFC 20 FC BB JSR $BBFC               JSR     MOVFA
.,AFFF 20 BF B1 JSR $B1BF               JSR     AYINT           ;[FACMO&LO]=INT OF ARG.
.,B002 A5 65    LDA $65                 LDA     FACLO
.,B004 45 0B    EOR $0B                 EOR     COUNT
.,B006 25 08    AND $08                 AND     INTEGR+1
.,B008 45 0B    EOR $0B                 EOR     COUNT           ;FINISH OUT DEMORGAN.
.,B00A A8       TAY                     TAY                     ;SAVE HIGH.
.,B00B A5 64    LDA $64                 LDA     FACMO
.,B00D 45 0B    EOR $0B                 EOR     COUNT
.,B00F 25 07    AND $07                 AND     INTEGR
.,B011 45 0B    EOR $0B                 EOR     COUNT
.,B013 4C 91 B3 JMP $B391               JMP     GIVAYF          ;FLOAT [A.Y] AND RET TO USER.
                                
                                ;
                                ; TIME TO PERFORM A RELATIONAL OPERATOR.
                                ; [DOMASK] CONTAINS THE BITS AS TO WHICH RELATIONAL
                                ; OPERATOR IT WAS. CARRY BIT ON=STRING COMPARE.
                                ;
.,B016 20 90 AD JSR $AD90       DOREL:  JSR     CHKVAL          ;CHECK FOR MATCH.
.,B019 B0 13    BCS $B02E               BCS     STRCMP          ;IT IS A STRING.
.,B01B A5 6E    LDA $6E                 LDA     ARGSGN          ;PACK ARG FOR FCOMP.
.,B01D 09 7F    ORA #$7F                ORAI    127
.,B01F 25 6A    AND $6A                 AND     ARGHO
.,B021 85 6A    STA $6A                 STA     ARGHO
.,B023 A9 69    LDA #$69                LDWDI   ARGEXP
.,B025 A0 00    LDY #$00        
.,B027 20 5B BC JSR $BC5B               JSR     FCOMP
.,B02A AA       TAX                     TAX
.,B02B 4C 61 B0 JMP $B061               JMP     QCOMP
.,B02E A9 00    LDA #$00        STRCMP: CLR     VALTYP          ;RESULT WILL BE NUMERIC.
.,B030 85 0D    STA $0D         
.,B032 C6 4D    DEC $4D                 DEC     OPMASK          ;TURN OFF VALTYP WHICH WAS STRING.
.,B034 20 A6 B6 JSR $B6A6               JSR     FREFAC          ;FREE THE FACLO STRING.
.,B037 85 61    STA $61                 STA     DSCTMP          ;SAVE FOR LATER.
.,B039 86 62    STX $62                 STXY    DSCTMP+1
.,B03B 84 63    STY $63         
.,B03D A5 6C    LDA $6C                 LDWD    ARGMO           ;GET POINTER TO OTHER STRING.
.,B03F A4 6D    LDY $6D         
.,B041 20 AA B6 JSR $B6AA               JSR     FRETMP          ;FREES FIRST DESC POINTER.
.,B044 86 6C    STX $6C                 STXY    ARGMO
.,B046 84 6D    STY $6D         
.,B048 AA       TAX                     TAX                     ;COPY COUNT INTO X.
.,B049 38       SEC                     SEC
.,B04A E5 61    SBC $61                 SBC     DSCTMP          ;WHICH IS GREATER. IF 0, ALL SET UP.
.,B04C F0 08    BEQ $B056               BEQ     STASGN          ;JUST PUT SIGN OF DIFFERENCE AWAY.
.,B04E A9 01    LDA #$01                LDAI    1
.,B050 90 04    BCC $B056               BCC     STASGN          ;SIGN IS POSITIVE.
.,B052 A6 61    LDX $61                 LDX     DSCTMP          ;LENGTH OF FAC IS SHORTER.
.,B054 A9 FF    LDA #$FF                LDAI    ^O377           ;GET A MINUS 1 FOR NEGATIVES.
.,B056 85 66    STA $66         STASGN: STA     FACSGN          ;KEEP FOR LATER.
.,B058 A0 FF    LDY #$FF                LDYI    255             ;SET POINTER TO FIRST STRING. (ARG.)
.,B05A E8       INX                     INX                     ;TO LOOP PROPERLY.
.,B05B C8       INY             NXTCMP: INY
.,B05C CA       DEX                     DEX                     ;ANY CHARACTERS LEFT TO COMPARE?
.,B05D D0 07    BNE $B066               BNE     GETCMP          ;NOT DONE YET.
.,B05F A6 66    LDX $66                 LDX     FACSGN          ;USE SIGN OF LENGTH DIFFERENCE
                                                                ;SINCE ALL CHARACTERS ARE THE SAME.
.,B061 30 0F    BMI $B072       QCOMP:  BMI     DOCMP           ;C IS ALWAYS SET THEN.
.,B063 18       CLC                     CLC
.,B064 90 0C    BCC $B072               BCC     DOCMP           ;ALWAYS BRANCH.
.,B066 B1 6C    LDA ($6C),Y     GETCMP: LDADY   ARGMO           ;GET NEXT CHAR TO COMPARE.
.,B068 D1 62    CMP ($62),Y             CMPDY   DSCTMP+1        ;SAME?
.,B06A F0 EF    BEQ $B05B               BEQ     NXTCMP          ;YEP. TRY FURTHER.
.,B06C A2 FF    LDX #$FF                LDXI    ^O377           ;SET A POSITIVE DIFFERENCE.
.,B06E B0 02    BCS $B072               BCS     DOCMP           ;PUT STACK BACK TOGETHER.
.,B070 A2 01    LDX #$01                LDXI    1               ;SET A NEGATIVE DIFFERENCE.
.,B072 E8       INX             DOCMP:  INX                     ;-1 TO 1, 0 TO 2, 1 TO 4.
.,B073 8A       TXA                     TXA
.,B074 2A       ROL                     ROL     A
.,B075 25 12    AND $12                 AND     DOMASK
.,B077 F0 02    BEQ $B07B               BEQ     GOFLOT
.,B079 A9 FF    LDA #$FF                LDAI    ^O377           ;MAP 0 TO 0. ALL OTHERS TO -1.
.,B07B 4C 3C BC JMP $BC3C       GOFLOT: JMP     FLOAT           ;FLOAT THE ONE-BYTE RESULT INTO FAC.
                                
                                PAGE
                                SUBTTL  DIMENSION AND VARIABLE SEARCHING.
                                ;
                                ; THE "DIM" CODE SETS [DIMFLG] AND THEN FALLS INTO THE VARIABLE SEARCH
                                ; ROUTINE, WHICH LOOKS AT DIMFLG AT THREE DIFFERENT POINTS.
                                ;       1) IF AN ENTRY IS FOUND, "DIMFLG" BEING ON INDICATES
                                ;               A "DOUBLY" DIMENSIONED VARIABLE.
                                ;       2) WHEN A NEW ENTRY IS BEING BUILT "DIMFLG" BEING ON
                                ;               INDICTAES THE INDICES SHOULD BE USED FOR THE
                                ;               SIZE OF EACH INDEX. OTHERWISE THE DEFAULT OF TEN
                                ;               IS USED.
                                ;       3) WHEN THE BUILD ENTRY CODE FINISHES, ONLY IF "DIMFLG" IS OFF
                                ;               WILL INDEXING BE DONE.
                                ;
.,B07E 20 FD AE JSR $AEFD       DIM3:   JSR     CHKCOM          ;MUST BE A COMMA
.,B081 AA       TAX             DIM:    TAX                     ;SET [ACCX] NONZERO.
                                                                ;[ACCA] MUST BE NONZERO TO WORK RIGHT.
.,B082 20 90 B0 JSR $B090       DIM1:   JSR     PTRGT1
.,B085 20 79 00 JSR $0079       DIMCON: JSR     CHRGOT          ;GET LAST CHARACTER.
.,B088 D0 F4    BNE $B07E               BNE     DIM3
.,B08A 60       RTS                     RTS
                                ;
                                ; ROUTINE TO READ THE VARIABLE NAME AT THE CURRENT TEXT POSITION
                                ; AND  PUT A POINTER TO ITS VALUE IN VARPNT. [TXTPTR]
                                ; POINTS TO THE TERMINATING CHARCTER.. NOT THAT EVALUATING SUBSCRIPTS
                                ; IN A VARIABLE NAME CAN CAUSE RECURSIVE CALLS TO "PTRGET" SO AT
                                ; THAT POINT ALL VALUES MUST BE STORED ON THE STACK.
                                ;
.,B08B A2 00    LDX #$00        PTRGET: LDXI    0               ;MAKE [ACCX]=0.
.,B08D 20 79 00 JSR $0079               JSR     CHRGOT          ;RETRIEVE LAST CHARACTER.
.,B090 86 0C    STX $0C         PTRGT1: STX     DIMFLG          ;STORE FLAG AWAY.
.,B092 85 45    STA $45         PTRGT2: STA     VARNAM
.,B094 20 79 00 JSR $0079               JSR     CHRGOT          ;GET CURRENT CHARACTER
                                                                ;MAYBE WITH FUNCTION BIT OFF.
.,B097 20 13 B1 JSR $B113               JSR     ISLETC          ;CHECK FOR LETTER.
.,B09A B0 03    BCS $B09F               BCS     PTRGT3          ;MUST HAVE A LETTER.
.,B09C 4C 08 AF JMP $AF08       INTERR: JMP     SNERR
.,B09F A2 00    LDX #$00        PTRGT3: LDXI    0               ;ASSUME NO SECOND CHARACTER.
.,B0A1 86 0D    STX $0D                 STX     VALTYP          ;DEFAULT IS NUMERIC.
                                IFN     INTPRC,<
.,B0A3 86 0E    STX $0E                 STX     INTFLG>         ;ASSUME FLOATING.
.,B0A5 20 73 00 JSR $0073               JSR     CHRGET          ;GET FOLLOWING CHARACTER.
.,B0A8 90 05    BCC $B0AF               BCC     ISSEC           ;CARRY RESET BY CHRGET IF NUMERIC.
.,B0AA 20 13 B1 JSR $B113               JSR     ISLETC          ;SET CARRY IF NOT ALPHABETIC.
.,B0AD 90 0B    BCC $B0BA               BCC     NOSEC           ;ALLOW ALPHABETICS.
.,B0AF AA       TAX             ISSEC:  TAX                     ;IT IS A NUMBER -- SAVE IN ACCX.
.,B0B0 20 73 00 JSR $0073       EATEM:  JSR     CHRGET          ;LOOK AT NEXT CHARACTER.
.,B0B3 90 FB    BCC $B0B0               BCC     EATEM           ;SKIP NUMERICS.
.,B0B5 20 13 B1 JSR $B113               JSR     ISLETC
.,B0B8 B0 F6    BCS $B0B0               BCS     EATEM           ;SKIP ALPHABETICS.
.,B0BA C9 24    CMP #$24        NOSEC:  CMPI    "$"             ;IS IT A STRING?
.,B0BC D0 06    BNE $B0C4               BNE     NOTSTR          ;IF NOT, [VALTYP]=0.
.,B0BE A9 FF    LDA #$FF                LDAI    ^O377           ;SET [VALTYP]=255 (STRING !).
.,B0C0 85 0D    STA $0D                 STA     VALTYP
                                IFN     INTPRC,<
.,B0C2 D0 10    BNE $B0D4               BNEA    TURNON          ;ALWAYS GOES.
.,B0C4 C9 25    CMP #$25        NOTSTR: CMPI    "%"             ;INTEGER VARIABLE?
.,B0C6 D0 13    BNE $B0DB               BNE     STRNAM          ;NO.
.,B0C8 A5 10    LDA $10                 LDA     SUBFLG
.,B0CA D0 D0    BNE $B09C               BNE     INTERR
.,B0CC A9 80    LDA #$80                LDAI    128
.,B0CE 85 0E    STA $0E                 STA     INTFLG          ;SET FLAG.
.,B0D0 05 45    ORA $45                 ORA     VARNAM          ;TURN ON BOTH HIGH BITS.
.,B0D2 85 45    STA $45                 STA     VARNAM>
.,B0D4 8A       TXA             TURNON: TXA
.,B0D5 09 80    ORA #$80                ORAI    128             ;TURN ON MSB OF SECOND CHARACTER.
.,B0D7 AA       TAX                     TAX
.,B0D8 20 73 00 JSR $0073               JSR     CHRGET          ;GET CHARACTER AFTER $.
                                IFE     INTPRC,<
                                NOTSTR:>
.,B0DB 86 46    STX $46         STRNAM: STX     VARNAM+1        ;STORE AWAY SECOND CHARACTER.
.,B0DD 38       SEC                     SEC
.,B0DE 05 10    ORA $10                 ORA     SUBFLG          ;ADD FLAG WHETHER TO ALLOW ARRAYS.
.,B0E0 E9 28    SBC #$28                SBCI    40              ;(CHECK FOR "(") WON'T MATCH IF SUBFLG SET.
.,B0E2 D0 03    BNE $B0E7               JEQ     ISARY           ;IT IS!
.,B0E4 4C D1 B1 JMP $B1D1       
.,B0E7 A0 00    LDY #$00                CLR     SUBFLG          ;ALLOW SUBSCRIPTS AGAIN.
.,B0E9 84 10    STY $10         
.,B0EB A5 2D    LDA $2D                 LDA     VARTAB          ;PLACE TO START SEARCH.
.,B0ED A6 2E    LDX $2E                 LDX     VARTAB+1
                                        LDYI    0
.,B0EF 86 60    STX $60         STXFND: STX     LOWTR+1
.,B0F1 85 5F    STA $5F         LOPFND: STA     LOWTR
.,B0F3 E4 30    CPX $30                 CPX     ARYTAB+1        ;AT END OF TABLE YET?
.,B0F5 D0 04    BNE $B0FB               BNE     LOPFN
.,B0F7 C5 2F    CMP $2F                 CMP     ARYTAB
.,B0F9 F0 22    BEQ $B11D               BEQ     NOTFNS          ;YES. WE COULDN'T FIND IT.
.,B0FB A5 45    LDA $45         LOPFN:  LDA     VARNAM
.,B0FD D1 5F    CMP ($5F),Y             CMPDY   LOWTR           ;COMPARE HIGH ORDERS.
.,B0FF D0 08    BNE $B109               BNE     NOTIT           ;NO COMPARISON.
.,B101 A5 46    LDA $46                 LDA     VARNAM+1
.,B103 C8       INY                     INY
.,B104 D1 5F    CMP ($5F),Y             CMPDY   LOWTR           ;AND THE LOW PART?
.,B106 F0 7D    BEQ $B185               BEQ     FINPTR          ;THAT'S IT ! THAT'S IT !
.,B108 88       DEY                     DEY
.,B109 18       CLC             NOTIT:  CLC
.,B10A A5 5F    LDA $5F                 LDA     LOWTR
.,B10C 69 07    ADC #$07                ADCI    6+ADDPRC        ;MAKES NO DIF AMONG TYPES.
.,B10E 90 E1    BCC $B0F1               BCC     LOPFND
.,B110 E8       INX                     INX
.,B111 D0 DC    BNE $B0EF               BNEA    STXFND          ;ALWAYS BRANCHES.
                                
                                ;
                                ; TEST FOR A LETTER.    / CARRY OFF= NOT A LETTER.
                                ;                         CARRY ON= A LETTER.
                                ;
.,B113 C9 41    CMP #$41        ISLETC: CMPI    "A"
.,B115 90 05    BCC $B11C               BCC     ISLRTS          ;IF LESS THAN "A", RET.
.,B117 E9 5B    SBC #$5B                SBCI    "Z"+1
.,B119 38       SEC                     SEC
.,B11A E9 A5    SBC #$A5                SBCI    256-"Z"-1       ;RESET CARRY IF [A] .GT. "Z".
.,B11C 60       RTS             ISLRTS: RTS                     ;RETURN TO CALLER.
                                
.,B11D 68       PLA             NOTFNS: PLA                     ;CHECK WHO'S CALLING.
.,B11E 48       PHA                     PHA                     ;RESTORE IT.
.,B11F C9 2A    CMP #$2A                CMPI    ISVRET-1-<ISVRET-1>/256*256     ;IS EVAL CALLING?
.,B121 D0 05    BNE $B128               BNE     NOTEVL          ;NO, CARRY ON.
                                IFN     REALIO-3,<
                                        TSX
                                        LDA     258,X
                                        CMPI    <<ISVRET-1>/256>
                                        BNE     NOTEVL>
.,B123 A9 13    LDA #$13        LDZR:   LDWDI   ZERO            ;SET UP PNTR TO SIMULATED ZERO.
.,B125 A0 BF    LDY #$BF        
.,B127 60       RTS                     RTS                     ;FOR STRINGS OR NUMERIC.
                                                                ;AND FOR INTEGERS TOO.
                                NOTEVL:
                                IFN     TIME!EXTIO,<
.,B128 A5 45    LDA $45                 LDWD    VARNAM>
.,B12A A4 46    LDY $46         IFN     TIME,<
.,B12C C9 54    CMP #$54                CMPI    "T"
.,B12E D0 0B    BNE $B13B               BNE     QSTAVR
.,B130 C0 C9    CPY #$C9                CPYI    "I"+128
.,B132 F0 EF    BEQ $B123               BEQ     LDZR
.,B134 C0 49    CPY #$49                CPYI    "I"
.,B136 D0 03    BNE $B13B               BNE     QSTAVR>
                                IFN     EXTIO!TIME,<
.,B138 4C 08 AF JMP $AF08       GOBADV: JMP     SNERR>
                                QSTAVR:
                                IFN     EXTIO,<
.,B13B C9 53    CMP #$53                CMPI    "S"
.,B13D D0 04    BNE $B143               BNE     VAROK
.,B13F C0 54    CPY #$54                CPYI    "T"
.,B141 F0 F5    BEQ $B138               BEQ     GOBADV>
.,B143 A5 2F    LDA $2F         VAROK:  LDWD    ARYTAB
.,B145 A4 30    LDY $30         
.,B147 85 5F    STA $5F                 STWD    LOWTR           ;LOWEST THING TO MOVE.
.,B149 84 60    STY $60         
.,B14B A5 31    LDA $31                 LDWD    STREND          ;GET HIGHEST ADDR TO MOVE.
.,B14D A4 32    LDY $32         
.,B14F 85 5A    STA $5A                 STWD    HIGHTR
.,B151 84 5B    STY $5B         
.,B153 18       CLC                     CLC
.,B154 69 07    ADC #$07                ADCI    6+ADDPRC
.,B156 90 01    BCC $B159               BCC     NOTEVE
.,B158 C8       INY                     INY
.,B159 85 58    STA $58         NOTEVE: STWD    HIGHDS          ;PLACE TO STUFF IT.
.,B15B 84 59    STY $59         
.,B15D 20 B8 A3 JSR $A3B8               JSR     BLTU            ;MOVE IT ALL.
                                                                ;NOTE [Y,A] HAS [HIGHDS] FOR REASON.
.,B160 A5 58    LDA $58                 LDWD    HIGHDS          ;AND SET UP
.,B162 A4 59    LDY $59         
.,B164 C8       INY                     INY
.,B165 85 2F    STA $2F                 STWD    ARYTAB          ;NEW START OF ARRAY TABLE.
.,B167 84 30    STY $30         
.,B169 A0 00    LDY #$00                LDYI    0               ;GET ADDR OF VARIABLE ENTRY.
.,B16B A5 45    LDA $45                 LDA     VARNAM
.,B16D 91 5F    STA ($5F),Y             STADY   LOWTR
.,B16F C8       INY                     INY
.,B170 A5 46    LDA $46                 LDA     VARNAM+1
.,B172 91 5F    STA ($5F),Y             STADY   LOWTR           ;STORE NAME OF VARIABLE.
.,B174 A9 00    LDA #$00                LDAI    0
.,B176 C8       INY                     INY
.,B177 91 5F    STA ($5F),Y             STADY   LOWTR
.,B179 C8       INY                     INY
.,B17A 91 5F    STA ($5F),Y             STADY   LOWTR
.,B17C C8       INY                     INY
.,B17D 91 5F    STA ($5F),Y             STADY   LOWTR
.,B17F C8       INY                     INY
.,B180 91 5F    STA ($5F),Y             STADY   LOWTR           ;FOURTH ZERO FOR DEF FUNC.
                                IFN     ADDPRC,<
.,B182 C8       INY                     INY
.,B183 91 5F    STA ($5F),Y             STADY   LOWTR>
.,B185 A5 5F    LDA $5F         FINPTR: LDA     LOWTR
.,B187 18       CLC                     CLC
.,B188 69 02    ADC #$02                ADCI    2
.,B18A A4 60    LDY $60                 LDY     LOWTR+1
.,B18C 90 01    BCC $B18F               BCC     FINNOW
.,B18E C8       INY                     INY
.,B18F 85 47    STA $47         FINNOW: STWD    VARPNT          ;THIS IS IT.
.,B191 84 48    STY $48         
.,B193 60       RTS                     RTS
                                PAGE
                                SUBTTL  MULTIPLE DIMENSION CODE.
.,B194 A5 0B    LDA $0B         FMAPTR: LDA     COUNT
.,B196 0A       ASL                     ASL     A,
.,B197 69 05    ADC #$05                ADCI    5               ;POINT TO ENTRIES. C CLR'D BY ASL.
.,B199 65 5F    ADC $5F                 ADC     LOWTR
.,B19B A4 60    LDY $60                 LDY     LOWTR+1
.,B19D 90 01    BCC $B1A0               BCC     JSRGM
.,B19F C8       INY                     INY
.,B1A0 85 58    STA $58         JSRGM:  STWD    ARYPNT
.,B1A2 84 59    STY $59         
.,B1A4 60       RTS                     RTS
                                
.:B1A5 90 80 00 00 00           N32768: EXP     144,128,0,0     ;-32768.
                                
.,B1AA 20 BF B1 JSR $B1BF       
.,B1AD A5 64    LDA $64         
.,B1AF A4 65    LDY $65         
.,B1B1 60       RTS             
                                
                                ;
                                ; INTIDX READS A FORMULA FROM THE CURRENT POSITION AND
                                ; TURNS IT INTO A POSITIVE INTEGER
                                ; LEAVING THE RESULT IN FACMO&LO. NEGATIVE ARGUMENTS
                                ; ARE NOT ALLOWED.
                                ;
.,B1B2 20 73 00 JSR $0073       INTIDX: JSR     CHRGET
.,B1B5 20 9E AD JSR $AD9E               JSR     FRMEVL          ;GET A NUMBER
.,B1B8 20 8D AD JSR $AD8D       POSINT: JSR     CHKNUM
.,B1BB A5 66    LDA $66                 LDA     FACSGN
.,B1BD 30 0D    BMI $B1CC               BMI     NONONO          ;IF NEGATIVE, BLOW HIM OUT.
.,B1BF A5 61    LDA $61         AYINT:  LDA     FACEXP
.,B1C1 C9 90    CMP #$90                CMPI    144             ;FAC .GT. 32767?
.,B1C3 90 09    BCC $B1CE               BCC     QINTGO
.,B1C5 A9 A5    LDA #$A5                LDWDI   N32768          ;GET ADDR OF -32768.
.,B1C7 A0 B1    LDY #$B1        
.,B1C9 20 5B BC JSR $BC5B               JSR     FCOMP           ;SEE IF FAC=[[Y,A]].
.,B1CC D0 7A    BNE $B248       NONONO: BNE     FCERR           ;NO, FAC IS TOO BIG.
.,B1CE 4C 9B BC JMP $BC9B       QINTGO: JMP     QINT            ;GO TO QINT AND SHOVE IT.
                                ;
                                ; FORMAT OF ARRAYS IN CORE.
                                ;
                                ; DESCRIPTOR:
                                ;       LOWBYTE = FIRST CHARACTER.
                                ;       HIGHBYTE = SECOND CHARACTER (200 BIT IS STRING FLAG).
                                ; LENGTH OF ARRAY IN CORE IN BYTES (INCLUDES EVERYTHING).
                                ; NUMBER OF DIMENSIONS.
                                ; FOR EACH DIMENSION STARTING WITH THE FIRST A LIST
                                ; (2 BYTES EACH) OF THE MAX INDICE+1
                                ; THE VALUES
                                ;
.,B1D1 A5 0C    LDA $0C         ISARY:  LDA     DIMFLG
                                IFN     INTPRC,<
.,B1D3 05 0E    ORA $0E                 ORA     INTFLG>
.,B1D5 48       PHA                     PHA                     ;SAVE [DIMFLG] FOR RECURSION.
.,B1D6 A5 0D    LDA $0D                 LDA     VALTYP
.,B1D8 48       PHA                     PHA                     ;SAVE [VALTYP] FOR RECURSION.
.,B1D9 A0 00    LDY #$00                LDYI    0               ;SET NUMBER OF DIMENSIONS TO ZERO.
.,B1DB 98       TYA             INDLOP: TYA                     ;SAVE NUMBER OF DIMS.
.,B1DC 48       PHA                     PHA
.,B1DD A5 46    LDA $46                 PSHWD   VARNAM          ;SAVE LOOKS.
.,B1DF 48       PHA             
.,B1E0 A5 45    LDA $45         
.,B1E2 48       PHA             
.,B1E3 20 B2 B1 JSR $B1B2               JSR     INTIDX          ;EVALUATE INDICE INTO FACMO&LO.
.,B1E6 68       PLA                     PULWD   VARNAM          ;GET BACK ALL... WE'RE HOME.
.,B1E7 85 45    STA $45         
.,B1E9 68       PLA             
.,B1EA 85 46    STA $46         
.,B1EC 68       PLA                     PLA                     ;(# OF DIMS).
.,B1ED A8       TAY                     TAY
.,B1EE BA       TSX                     TSX
.,B1EF BD 02 01 LDA $0102,X             LDA     258,X
.,B1F2 48       PHA                     PHA                     ;PUSH DIMFLG AND VALTYP FURTHER.
.,B1F3 BD 01 01 LDA $0101,X             LDA     257,X
.,B1F6 48       PHA                     PHA
.,B1F7 A5 64    LDA $64                 LDA     INDICE          ;PUT INDICE ONTO STACK.
.,B1F9 9D 02 01 STA $0102,X             STA     258,X,          ;UNDER DIMFLG AND VALTYP.
.,B1FC A5 65    LDA $65                 LDA     INDICE+1
.,B1FE 9D 01 01 STA $0101,X             STA     257,X
.,B201 C8       INY                     INY                     ;INCREMENT # OF DIMS.
.,B202 20 79 00 JSR $0079               JSR     CHRGOT          ;GET TERMINATING CHARACTER.
.,B205 C9 2C    CMP #$2C                CMPI    44              ;A COMMA?
.,B207 F0 D2    BEQ $B1DB               BEQ     INDLOP          ;YES.
.,B209 84 0B    STY $0B                 STY     COUNT           ;SAVE COUNT OF DIMS.
.,B20B 20 F7 AE JSR $AEF7               JSR     CHKCLS          ;MUST BE CLOSED PAREN.
.,B20E 68       PLA                     PLA
.,B20F 85 0D    STA $0D                 STA     VALTYP          ;GET VALTYP AND
.,B211 68       PLA                     PLA
                                IFN     INTPRC,<
.,B212 85 0E    STA $0E                 STA     INTFLG
.,B214 29 7F    AND #$7F                ANDI    127>
.,B216 85 0C    STA $0C                 STA     DIMFLG          ;DIMFLG OFF STACK.
.,B218 A6 2F    LDX $2F                 LDX     ARYTAB          ;PLACE TO START SEARCH.
.,B21A A5 30    LDA $30                 LDA     ARYTAB+1
.,B21C 86 5F    STX $5F         LOPFDA: STX     LOWTR
.,B21E 85 60    STA $60                 STA     LOWTR+1
.,B220 C5 32    CMP $32                 CMP     STREND+1        ;END OF ARRAYS?
.,B222 D0 04    BNE $B228               BNE     LOPFDV
.,B224 E4 31    CPX $31                 CPX     STREND
.,B226 F0 39    BEQ $B261               BEQ     NOTFDD          ;A FINE THING! NO ARRAY!.
.,B228 A0 00    LDY #$00        LOPFDV: LDYI    0
.,B22A B1 5F    LDA ($5F),Y             LDADY   LOWTR
.,B22C C8       INY                     INY
.,B22D C5 45    CMP $45                 CMP     VARNAM          ;COMPARE HIGH ORDERS.
.,B22F D0 06    BNE $B237               BNE     NMARY1          ;NO WAY IS IT THIS. GET OUT OF HERE.
.,B231 A5 46    LDA $46                 LDA     VARNAM+1
.,B233 D1 5F    CMP ($5F),Y             CMPDY   LOWTR           ;LOW ORDERS?
.,B235 F0 16    BEQ $B24D               BEQ     GOTARY          ;WELL, HERE IT IS !!
.,B237 C8       INY             NMARY1: INY
.,B238 B1 5F    LDA ($5F),Y             LDADY   LOWTR           ;GET LENGTH.
.,B23A 18       CLC                     CLC
.,B23B 65 5F    ADC $5F                 ADC     LOWTR
.,B23D AA       TAX                     TAX
.,B23E C8       INY                     INY
.,B23F B1 5F    LDA ($5F),Y             LDADY   LOWTR
.,B241 65 60    ADC $60                 ADC     LOWTR+1
.,B243 90 D7    BCC $B21C               BCC     LOPFDA          ;ALWAYS BRANCHES.
.,B245 A2 12    LDX #$12        BSERR:  LDXI    ERRBS           ;GET BAD SUB ERROR NUMBER.
.:B247 2C       .BYTE $2C               SKIP2
.,B248 A2 0E    LDX #$0E        FCERR:  LDXI    ERRFC           ;TOO BIG. "FUNCTION CALL" ERROR.
.,B24A 4C 37 A4 JMP $A437       ERRGO3: JMP     ERROR
.,B24D A2 13    LDX #$13        GOTARY: LDXI    ERRDD           ;PERHAPS A "RE-DIMENSION" ERROR
.,B24F A5 0C    LDA $0C                 LDA     DIMFLG          ;TEST THE DIMFLG
.,B251 D0 F7    BNE $B24A               BNE     ERRGO3
.,B253 20 94 B1 JSR $B194               JSR     FMAPTR
.,B256 A5 0B    LDA $0B                 LDA     COUNT           ;GET NUMBER OF DIMS INPUT.
.,B258 A0 04    LDY #$04                LDYI    4
.,B25A D1 5F    CMP ($5F),Y             CMPDY   LOWTR           ;# OF DIMS THE SAME?
.,B25C D0 E7    BNE $B245               BNE     BSERR           ;SAME SO GO GET DEFINITION.
.,B25E 4C EA B2 JMP $B2EA               JMP     GETDEF
                                
                                ;
                                ; HERE WHEN VARIABLE IS NOT FOUND IN THE ARRAY TABLE.
                                ;
                                ; BUILDING AN ENTRY.
                                ;
                                ;       PUT DOWN THE DESCRIPTOR.
                                ;       SETUP NUMBER OF DIMENSIONS.
                                ;       MAKE SURE THERE IS ROOM FOR THE NEW ENTRY.
                                ;       REMEMBER "VARPNT".
                                ;       TALLY=4.
                                ;       SKIP 2 LOCS FOR LATER FILL IN OF SIZE.
                                ; LOOP: GET AN INDICE
                                ;       PUT DOWN NUMBER+1 AND INCREMENT VARPTR.
                                ;       TALLY=TALLY*NUMBER+1.
                                ;       DECREMENT NUMBER-DIMS.
                                ;       BNE LOOP
                                ;       CALL "REASON" WITH [Y,A] REFLECTING LAST LOC OF VARIABLE.
                                ;       UPDATE STREND.
                                ;       ZERO ALL.
                                ;       MAKE TALLY INCLUDE MAXDIMS AND DESCRIPTOR.
                                ;       PUT DOWN TALLY.
                                ;       IF CALLED BY DIMENSION, RETURN.
                                ;       OTHERWISE INDEX INTO THE VARIABLE AS IF IT
                                ;        WERE FOUND ON THE INITIAL SEARCH.
                                ;
.,B261 20 94 B1 JSR $B194       NOTFDD: JSR     FMAPTR          ;FORM ARYPNT.
.,B264 20 08 A4 JSR $A408               JSR     REASON
.,B267 A0 00    LDY #$00                LDAI    0
                                        TAY
.,B269 84 72    STY $72                 STA     CURTOL+1
                                IFE     ADDPRC,<
                                        LDXI    4>
                                IFN     ADDPRC,<
.,B26B A2 05    LDX #$05                LDXI    5>
.,B26D A5 45    LDA $45                 LDA     VARNAM          ;THIS CODE ONLY WORKS FOR INTPRC=1
.,B26F 91 5F    STA ($5F),Y             STADY   LOWTR           ;IF ADDPRC=1.
                                IFN     ADDPRC,<
.,B271 10 01    BPL $B274               BPL     NOTFLT
.,B273 CA       DEX                     DEX>
.,B274 C8       INY             NOTFLT: INY
.,B275 A5 46    LDA $46                 LDA     VARNAM+1
.,B277 91 5F    STA ($5F),Y             STADY   LOWTR
.,B279 10 02    BPL $B27D               BPL     STOMLT
.,B27B CA       DEX                     DEX
                                IFN     ADDPRC,<
.,B27C CA       DEX                     DEX>
.,B27D 86 71    STX $71         STOMLT: STX     CURTOL
.,B27F A5 0B    LDA $0B                 LDA     COUNT
.,B281 C8       INY                     REPEAT  3,<INY>
.,B282 C8       INY             
.,B283 C8       INY             
.,B284 91 5F    STA ($5F),Y             STADY   LOWTR           ;SAVE NUMBER OF DIMENSIONS.
.,B286 A2 0B    LDX #$0B        LOPPTA: LDXI    11              ;DEFAULT SIZE.
.,B288 A9 00    LDA #$00                LDAI    0
.,B28A 24 0C    BIT $0C                 BIT     DIMFLG
.,B28C 50 08    BVC $B296               BVC     NOTDIM          ;NOT IN A DIM STATEMENT.
.,B28E 68       PLA                     PLA                     ;GET LOW ORDER OF INDICE.
.,B28F 18       CLC                     CLC
.,B290 69 01    ADC #$01                ADCI    1
.,B292 AA       TAX                     TAX
.,B293 68       PLA                     PLA                     ;GET HIGH PART OF INDICE.
.,B294 69 00    ADC #$00                ADCI    0
.,B296 C8       INY             NOTDIM: INY
.,B297 91 5F    STA ($5F),Y             STADY   LOWTR           ;STORE HIGH PART OF INDICE.
.,B299 C8       INY                     INY
.,B29A 8A       TXA                     TXA
.,B29B 91 5F    STA ($5F),Y             STADY   LOWTR           ;STORE LOW ORDER OF INDICE.
.,B29D 20 4C B3 JSR $B34C               JSR     UMULT           ;[X,A]=[CURTOL]*[LOWTR,Y]
.,B2A0 86 71    STX $71                 STX     CURTOL          ;SAVE NEW TALLY.
.,B2A2 85 72    STA $72                 STA     CURTOL+1
.,B2A4 A4 22    LDY $22                 LDY     INDEX
.,B2A6 C6 0B    DEC $0B                 DEC     COUNT           ;ANY MORE INDICES LEFT?
.,B2A8 D0 DC    BNE $B286               BNE     LOPPTA          ;YES.
.,B2AA 65 59    ADC $59                 ADC     ARYPNT+1
.,B2AC B0 5D    BCS $B30B               BCS     OMERR1          ;OVERFLOW.
.,B2AE 85 59    STA $59                 STA     ARYPNT+1        ;COMPUTE WHERE TO ZERO.
.,B2B0 A8       TAY                     TAY
.,B2B1 8A       TXA                     TXA
.,B2B2 65 58    ADC $58                 ADC     ARYPNT
.,B2B4 90 03    BCC $B2B9               BCC     GREASE
.,B2B6 C8       INY                     INY
.,B2B7 F0 52    BEQ $B30B               BEQ     OMERR1
.,B2B9 20 08 A4 JSR $A408       GREASE: JSR     REASON          ;GET ROOM.
.,B2BC 85 31    STA $31                 STWD    STREND          ;NEW END OF STORAGE.
.,B2BE 84 32    STY $32         
.,B2C0 A9 00    LDA #$00                LDAI    0               ;STORING [ACCA] IS FASTER THAN CLEAR.
.,B2C2 E6 72    INC $72                 INC     CURTOL+1
.,B2C4 A4 71    LDY $71                 LDY     CURTOL
.,B2C6 F0 05    BEQ $B2CD               BEQ     DECCUR
.,B2C8 88       DEY             ZERITA: DEY
.,B2C9 91 58    STA ($58),Y             STADY   ARYPNT
.,B2CB D0 FB    BNE $B2C8               BNE     ZERITA          ;NO. CONTINUE.
.,B2CD C6 59    DEC $59         DECCUR: DEC     ARYPNT+1
.,B2CF C6 72    DEC $72                 DEC     CURTOL+1
.,B2D1 D0 F5    BNE $B2C8               BNE     ZERITA          ;DO ANOTHER BLOCK.
.,B2D3 E6 59    INC $59                 INC     ARYPNT+1        ;BUMP BACK UP. WILL USE LATER.
.,B2D5 38       SEC                     SEC
.,B2D6 A5 31    LDA $31                 LDA     STREND          ;RESTORE [ACCA].
.,B2D8 E5 5F    SBC $5F                 SBC     LOWTR           ;DETERMINE LENGTH.
.,B2DA A0 02    LDY #$02                LDYI    2
.,B2DC 91 5F    STA ($5F),Y             STADY   LOWTR           ;LOW.
.,B2DE A5 32    LDA $32                 LDA     STREND+1
.,B2E0 C8       INY                     INY
.,B2E1 E5 60    SBC $60                 SBC     LOWTR+1
.,B2E3 91 5F    STA ($5F),Y             STADY   LOWTR           ;HIGH.
.,B2E5 A5 0C    LDA $0C                 LDA     DIMFLG
.,B2E7 D0 62    BNE $B34B               BNE     DIMRTS          ;BYE.
.,B2E9 C8       INY                     INY
                                ;
                                ; AT THIS POINT [LOWTR,Y] POINTS BEYOND THE SIZE TO THE NUMBER OF
                                ; DIMENSIONS. STRATEGY:
                                ;       NUMDIM=NUMBER OF DIMENSIONS.
                                ;       CURTOL=0.
                                ; INLPNM:GET A NEW INDICE.
                                ;       MAKE SURE INDICE IS NOT TOO BIG.
                                ;       MULTIPLY CURTOL BY CURMAX.
                                ;       ADD INDICE TO CURTOL.
                                ;       NUMDIM=NUMDIM-1.
                                ;       BNE     INLPNM.
                                ;       USE [CURTOL]*4 AS OFFSET.
                                ;
.,B2EA B1 5F    LDA ($5F),Y     GETDEF: LDADY   LOWTR
.,B2EC 85 0B    STA $0B                 STA     COUNT           ;SAVE A COUNTER.
.,B2EE A9 00    LDA #$00                LDAI    0               ;ZERO [CURTOL].
.,B2F0 85 71    STA $71                 STA     CURTOL
.,B2F2 85 72    STA $72         INLPNM: STA     CURTOL+1
.,B2F4 C8       INY                     INY
.,B2F5 68       PLA                     PLA                     ;GET LOW INDICE.
.,B2F6 AA       TAX                     TAX
.,B2F7 85 64    STA $64                 STA     INDICE
.,B2F9 68       PLA                     PLA                     ;AND THE HIGH PART
.,B2FA 85 65    STA $65                 STA     INDICE+1
.,B2FC D1 5F    CMP ($5F),Y             CMPDY   LOWTR           ;COMPARE WITH MAX INDICE.
.,B2FE 90 0E    BCC $B30E               BCC     INLPN2
.,B300 D0 06    BNE $B308               BNE     BSERR7          ;IF GREATER, "BAD SUBSCRIPT" ERROR.
.,B302 C8       INY                     INY
.,B303 8A       TXA                     TXA
.,B304 D1 5F    CMP ($5F),Y             CMPDY   LOWTR
.,B306 90 07    BCC $B30F               BCC     INLPN1
.,B308 4C 45 B2 JMP $B245       BSERR7: JMP     BSERR
.,B30B 4C 35 A4 JMP $A435       OMERR1: JMP     OMERR
.,B30E C8       INY             INLPN2: INY
.,B30F A5 72    LDA $72         INLPN1: LDA     CURTOL+1        ;DON'T MULTIPLY IF CURTOL=0.
.,B311 05 71    ORA $71                 ORA     CURTOL
.,B313 18       CLC                     CLC                     ;PREPARE TO GET INDICE BACK.
.,B314 F0 0A    BEQ $B320               BEQ     ADDIND          ;GET HIGH PART OF INDICE BACK.
.,B316 20 4C B3 JSR $B34C               JSR     UMULT           ;MULTIPLY [CURTOL] BY [LOWTR,Y,Y+1].
.,B319 8A       TXA                     TXA
.,B31A 65 64    ADC $64                 ADC     INDICE          ;ADD IN [INDICE].
.,B31C AA       TAX                     TAX
.,B31D 98       TYA                     TYA
.,B31E A4 22    LDY $22                 LDY     INDEX1
.,B320 65 65    ADC $65         ADDIND: ADC     INDICE+1
.,B322 86 71    STX $71                 STX     CURTOL
.,B324 C6 0B    DEC $0B                 DEC     COUNT           ;ANY MORE?
.,B326 D0 CA    BNE $B2F2               BNE     INLPNM          ;YES.
.,B328 85 72    STA $72                 STA     CURTOL+1        ;FIX ARRAY BUG ****
                                IFE     ADDPRC,<
                                        LDXI    4>
                                IFN     ADDPRC,<
.,B32A A2 05    LDX #$05                LDXI    5               ;THIS CODE ONLY WORKS FOR INTPRC=1
.,B32C A5 45    LDA $45                 LDA     VARNAM          ;IF ADDPRC=1.
.,B32E 10 01    BPL $B331               BPL     NOTFL1
.,B330 CA       DEX                     DEX>
.,B331 A5 46    LDA $46         NOTFL1: LDA     VARNAM+1
.,B333 10 02    BPL $B337               BPL     STOML1
.,B335 CA       DEX                     DEX
                                IFN     ADDPRC,<
.,B336 CA       DEX                     DEX>
.,B337 86 28    STX $28         STOML1: STX     ADDEND
.,B339 A9 00    LDA #$00                LDAI    0
.,B33B 20 55 B3 JSR $B355               JSR     UMULTD          ;ON RTS, A&Y=HI . X=LO.
.,B33E 8A       TXA                     TXA
.,B33F 65 58    ADC $58                 ADC     ARYPNT
.,B341 85 47    STA $47                 STA     VARPNT
.,B343 98       TYA                     TYA
.,B344 65 59    ADC $59                 ADC     ARYPNT+1
.,B346 85 48    STA $48                 STA     VARPNT+1
.,B348 A8       TAY                     TAY
.,B349 A5 47    LDA $47                 LDA     VARPNT
.,B34B 60       RTS             DIMRTS: RTS                     ;RETURN TO CALLER.
                                SUBTTL  INTEGER ARITHMETIC ROUTINES.
                                        ;TWO BYTE UNSIGNED INTEGER MULTIPLY.
                                        ;THIS IS FOR MULTIPLY DIMENSIONED ARRAYS.
                                        ; [X,Y]=[X,A]=[CURTOL]*[LOWTR,Y,Y+1].
.,B34C 84 22    STY $22         UMULT:  STY     INDEX
.,B34E B1 5F    LDA ($5F),Y             LDADY   LOWTR
.,B350 85 28    STA $28                 STA     ADDEND          ;LOW, THEN HIGH.
.,B352 88       DEY                     DEY
.,B353 B1 5F    LDA ($5F),Y             LDADY   LOWTR           ;PUT [LOWTR,Y,Y+1] IN FASTER MEMORY.
.,B355 85 29    STA $29         UMULTD: STA     ADDEND+1
.,B357 A9 10    LDA #$10                LDAI    16
.,B359 85 5D    STA $5D                 STA     DECCNT
.,B35B A2 00    LDX #$00                LDXI    0               ;CLR THE ACCS.
.,B35D A0 00    LDY #$00                LDYI    0               ;RESULT INITIALLY ZERO.
.,B35F 8A       TXA             UMULTC: TXA
.,B360 0A       ASL                     ASL     A,              ;MULTIPLY BY TWO.
.,B361 AA       TAX                     TAX
.,B362 98       TYA                     TYA
.,B363 2A       ROL                     ROL     A,
.,B364 A8       TAY                     TAY
.,B365 B0 A4    BCS $B30B               BCS     OMERR1          ;TWO MUCH !
.,B367 06 71    ASL $71                 ASL     CURTOL
.,B369 26 72    ROL $72                 ROL     CURTOL+1
.,B36B 90 0B    BCC $B378               BCC     UMLCNT          ;NOTHING IN THIS POSITION TO MULTIPLY.
.,B36D 18       CLC                     CLC
.,B36E 8A       TXA                     TXA
.,B36F 65 28    ADC $28                 ADC     ADDEND
.,B371 AA       TAX                     TAX
.,B372 98       TYA                     TYA
.,B373 65 29    ADC $29                 ADC     ADDEND+1
.,B375 A8       TAY                     TAY
.,B376 B0 93    BCS $B30B               BCS     OMERR1          ;MAN, JUST TOO MUCH !
.,B378 C6 5D    DEC $5D         UMLCNT: DEC     DECCNT          ;DONE?
.,B37A D0 E3    BNE $B35F               BNE     UMULTC          ;KEEP IT UP.
.,B37C 60       RTS             UMLRTS: RTS                     ;YES, ALL DONE.
                                PAGE
                                SUBTTL  FRE FUNCTION AND INTEGER TO FLOATING ROUTINES.
.,B37D A5 0D    LDA $0D         FRE:    LDA     VALTYP
.,B37F F0 03    BEQ $B384               BEQ     NOFREF
.,B381 20 A6 B6 JSR $B6A6               JSR     FREFAC
.,B384 20 26 B5 JSR $B526       NOFREF: JSR     GARBA2
.,B387 38       SEC                     SEC
.,B388 A5 33    LDA $33                 LDA     FRETOP          ;WE WANT
.,B38A E5 31    SBC $31                 SBC     STREND          ;[FRETOP]-[STREND].
.,B38C A8       TAY                     TAY
.,B38D A5 34    LDA $34                 LDA     FRETOP+1
.,B38F E5 32    SBC $32                 SBC     STREND+1
                                
.,B391 A2 00    LDX #$00        GIVAYF: LDXI    0
.,B393 86 0D    STX $0D                 STX     VALTYP
.,B395 85 62    STA $62                 STWD    FACHO
.,B397 84 63    STY $63         
.,B399 A2 90    LDX #$90                LDXI    144             ;SET EXPONENT TO 2^16.
.,B39B 4C 44 BC JMP $BC44               JMP     FLOATS          ;TURN IT TO A FLOATING PNT #.
                                
.,B39E 38       SEC             POS:    LDY     TRMPOS          ;GET POSITION.
.,B39F 20 F0 FF JSR $FFF0       
.,B3A2 A9 00    LDA #$00        SNGFLT: LDAI    0
.,B3A4 F0 EB    BEQ $B391               BEQA    GIVAYF          ;FLOAT IT.
                                PAGE
                                SUBTTL  SIMPLE-USER-DEFINED-FUNCTION CODE.
                                ;
                                ; NOTE ONLY SINGLE ARGUMENTS ARE ALLOWED TO FUNCTIONS
                                ; AND FUNCTIONS MUST BE OF THE SINGLE LINE FORM:
                                ;       DEF FNA(X)=X^2+X-2
                                ; NO STRINGS CAN BE INVOLVED WITH THESE FUNCTIONS.
                                ;
                                ; IDEA: CREATE A SIMPLE VARIABLE ENTRY
                                ; WHOSE FIRST CHARACTER HAS THE 200 BIT SET.
                                ; THE VALUE WILL BE:
                                ;
                                ;       A TEXT PNTR TO THE FORMULA.
                                ;       A PNTR TO THE ARGUMENT VARIABLE.
                                ;
                                ; FUNCTION NAMES CAN BE LIKE "FNA4".
                                ;
                                ;
                                ; SUBROUTINE TO SEE IF WE ARE IN DIRECT MODE.
                                ; AND COMPLAIN IF SO.
                                ;
.,B3A6 A6 3A    LDX $3A         ERRDIR: LDX     CURLIN+1        ;DIR MODE HAS [CURLIN]=0,255
.,B3A8 E8       INX                     INX                     ;SO NOW, IS RESULT ZERO?
.,B3A9 D0 A0    BNE $B34B               BNE     DIMRTS          ;YES.
.,B3AB A2 15    LDX #$15                LDXI    ERRID           ;INPUT DIRECT ERROR CODE.
.:B3AD 2C       .BYTE $2C               SKIP2
.,B3AE A2 1B    LDX #$1B        ERRGUF: LDXI    ERRUF           ;USER DEFINED FUNCTION NEVER DEFINED
.,B3B0 4C 37 A4 JMP $A437       ERRGO1: JMP     ERROR
                                
.,B3B3 20 E1 B3 JSR $B3E1       DEF:    JSR     GETFNM          ;GET A PNTR TO THE FUNCTION.
.,B3B6 20 A6 B3 JSR $B3A6               JSR     ERRDIR
.,B3B9 20 FA AE JSR $AEFA               JSR     CHKOPN          ;MUST HAVE "(".
.,B3BC A9 80    LDA #$80                LDAI    128
.,B3BE 85 10    STA $10                 STA     SUBFLG          ;PROHIBIT SUBSCRIPTED VARIABLES.
.,B3C0 20 8B B0 JSR $B08B               JSR     PTRGET          ;GET PNTR TO ARGUMENT.
.,B3C3 20 8D AD JSR $AD8D               JSR     CHKNUM          ;IS IT A NUMBER?
.,B3C6 20 F7 AE JSR $AEF7               JSR     CHKCLS          ;MUST HAVE ")"
.,B3C9 A9 B2    LDA #$B2                SYNCHK  EQULTK          ;MUST HAVE "=".
.,B3CB 20 FF AE JSR $AEFF       
.,B3CE 48       PHA             IFN     ADDPRC,<PHA>            ;PUT CRAZY BYTE ON.
.,B3CF A5 48    LDA $48                 PSHWD   VARPNT
.,B3D1 48       PHA             
.,B3D2 A5 47    LDA $47         
.,B3D4 48       PHA             
.,B3D5 A5 7B    LDA $7B                 PSHWD   TXTPTR
.,B3D7 48       PHA             
.,B3D8 A5 7A    LDA $7A         
.,B3DA 48       PHA             
.,B3DB 20 F8 A8 JSR $A8F8               JSR     DATA
.,B3DE 4C 4F B4 JMP $B44F               JMP     DEFFIN
                                ;
                                ; SUBROUTINE TO GET A PNTR TO A FUNCTION NAME.
                                ;
.,B3E1 A9 A5    LDA #$A5        GETFNM: SYNCHK  FNTK            ;MUST START WITH FN.
.,B3E3 20 FF AE JSR $AEFF       
.,B3E6 09 80    ORA #$80                ORAI    128             ;PUT FUNCTION BIT ON.
.,B3E8 85 10    STA $10                 STA     SUBFLG
.,B3EA 20 92 B0 JSR $B092               JSR     PTRGT2          ;GET POINTER TO FUNCTION OR CREATE ANEW.
.,B3ED 85 4E    STA $4E                 STWD    DEFPNT
.,B3EF 84 4F    STY $4F         
.,B3F1 4C 8D AD JMP $AD8D               JMP     CHKNUM          ;MAKE SURE IT'S NOT A STRING AND RETURN.
                                
.,B3F4 20 E1 B3 JSR $B3E1       FNDOER: JSR     GETFNM          ;GET THE FUNCTION'S NAME.
.,B3F7 A5 4F    LDA $4F                 PSHWD   DEFPNT
.,B3F9 48       PHA             
.,B3FA A5 4E    LDA $4E         
.,B3FC 48       PHA             
.,B3FD 20 F1 AE JSR $AEF1               JSR     PARCHK          ;EVALUATE PARAMETER.
.,B400 20 8D AD JSR $AD8D               JSR     CHKNUM
.,B403 68       PLA                     PULWD   DEFPNT
.,B404 85 4E    STA $4E         
.,B406 68       PLA             
.,B407 85 4F    STA $4F         
.,B409 A0 02    LDY #$02                LDYI    2
.,B40B B1 4E    LDA ($4E),Y             LDADY   DEFPNT          ;GET POINTER TO VARIABLE.
.,B40D 85 47    STA $47                 STA     VARPNT          ;SAVE VARIABLE POINTER.
.,B40F AA       TAX                     TAX
.,B410 C8       INY                     INY
.,B411 B1 4E    LDA ($4E),Y             LDADY   DEFPNT
.,B413 F0 99    BEQ $B3AE               BEQ     ERRGUF
.,B415 85 48    STA $48                 STA     VARPNT+1
.,B417 C8       INY             IFN     ADDPRC,<INY>            ;SINCE DEF USES ONLY 4.
.,B418 B1 47    LDA ($47),Y     DEFSTF: LDADY   VARPNT
.,B41A 48       PHA                     PHA                     ;PUSH IT ALL ON STACK.
.,B41B 88       DEY                     DEY                     ;SINCE WE ARE RECURSING MAYBE.
.,B41C 10 FA    BPL $B418               BPL     DEFSTF
.,B41E A4 48    LDY $48                 LDY     VARPNT+1
.,B420 20 D4 BB JSR $BBD4               JSR     MOVMF           ;PUT CURRENT FAC INTO OUR ARG VARIABLE.
.,B423 A5 7B    LDA $7B                 PSHWD   TXTPTR          ;SAVE TEXT POINTER.
.,B425 48       PHA             
.,B426 A5 7A    LDA $7A         
.,B428 48       PHA             
.,B429 B1 4E    LDA ($4E),Y             LDADY   DEFPNT          ;PNTR TO FUNCTION.
.,B42B 85 7A    STA $7A                 STA     TXTPTR
.,B42D C8       INY                     INY
.,B42E B1 4E    LDA ($4E),Y             LDADY   DEFPNT
.,B430 85 7B    STA $7B                 STA     TXTPTR+1
.,B432 A5 48    LDA $48                 PSHWD   VARPNT          ;SAVE VARIABLE POINTER.
.,B434 48       PHA             
.,B435 A5 47    LDA $47         
.,B437 48       PHA             
.,B438 20 8A AD JSR $AD8A               JSR     FRMNUM          ;EVALUATE FORMULA AND CHECK NUMERIC.
.,B43B 68       PLA                     PULWD   DEFPNT
.,B43C 85 4E    STA $4E         
.,B43E 68       PLA             
.,B43F 85 4F    STA $4F         
.,B441 20 79 00 JSR $0079               JSR     CHRGOT
.,B444 F0 03    BEQ $B449               JNE     SNERR           ;IT DIDN'T TERMINATE. HUH?
.,B446 4C 08 AF JMP $AF08       
.,B449 68       PLA                     PULWD   TXTPTR          ;RESTORE TEXT PNTR.
.,B44A 85 7A    STA $7A         
.,B44C 68       PLA             
.,B44D 85 7B    STA $7B         
.,B44F A0 00    LDY #$00        DEFFIN: LDYI    0
.,B451 68       PLA                     PLA                     ;GET OLD ARG VALUE OFF STACK
.,B452 91 4E    STA ($4E),Y             STADY   DEFPNT          ;AND PUT IT BACK IN VARIABLE.
.,B454 68       PLA                     PLA
.,B455 C8       INY                     INY
.,B456 91 4E    STA ($4E),Y             STADY   DEFPNT
.,B458 68       PLA                     PLA
.,B459 C8       INY                     INY
.,B45A 91 4E    STA ($4E),Y             STADY   DEFPNT
.,B45C 68       PLA                     PLA
.,B45D C8       INY                     INY
.,B45E 91 4E    STA ($4E),Y             STADY   DEFPNT
                                IFN     ADDPRC,<
.,B460 68       PLA                     PLA
.,B461 C8       INY                     INY
.,B462 91 4E    STA ($4E),Y             STADY   DEFPNT>
.,B464 60       RTS             DEFRTS: RTS
                                        PAGE
                                SUBTTL  STRING FUNCTIONS.
                                ;
                                ; THE STR$ FUNCTION TAKES A NUMBER AND GIVES A STRING
                                ; WITH THE CHARACTERS THE OUTPUT OF THE NUMBER
                                ; WOULD HAVE GIVEN.
                                ;
.,B465 20 8D AD JSR $AD8D       STR:    JSR     CHKNUM          ;ARG HAS TO BE NUMERIC.
.,B468 A0 00    LDY #$00                LDYI    0
.,B46A 20 DF BD JSR $BDDF               JSR     FOUTC           ;DO ITS OUTPUT.
.,B46D 68       PLA                     PLA
.,B46E 68       PLA                     PLA
.,B46F A9 FF    LDA #$FF        TIMSTR: LDWDI   LOFBUF
.,B471 A0 00    LDY #$00        
.,B473 F0 12    BEQ $B487               BEQA    STRLIT          ;SCAN IT AND TURN IT INTO A STRING.
                                ;
                                ; "STRINI" GET STRING SPACE FOR THE CREATION OF A STRING AND
                                ; CREATES A DESCRIPTOR FOR IT IN "DSCTMP".
                                ;
.,B475 A6 64    LDX $64         STRINI: LDXY    FACMO           ;GET FACMO TO STORE IN DSCPNT.
.,B477 A4 65    LDY $65         
.,B479 86 50    STX $50                 STXY    DSCPNT          ;RETAIN THE DESCRIPTOR POINTER.
.,B47B 84 51    STY $51         
.,B47D 20 F4 B4 JSR $B4F4       STRSPA: JSR     GETSPA          ;GET STRING SPACE.
.,B480 86 62    STX $62                 STXY    DSCTMP+1        ;SAVE LOCATION.
.,B482 84 63    STY $63         
.,B484 85 61    STA $61                 STA     DSCTMP          ;SAVE LENGTH.
.,B486 60       RTS             
                                        RTS                     ;ALL DONE.
                                ;
                                ; "STRLT2" TAKES THE STRING LITERAL WHOSE FIRST CHARACTER
                                ; IS POINTED TO BY [Y,A] AND BUILDS A DESCRIPTOR FOR IT.
                                ; THE DESCRIPTOR IS INITIALLY BUILT IN "DSCTMP", BUT "PUTNEW"
                                ; TRANSFERS IT INTO A TEMPORARY AND LEAVES A POINTER
                                ; AT THE TEMPORARY IN FACMO&LO. THE CHARACTERS OTHER THAN
                                ; ZERO THAT TERMINATE THE STRING SHOULD BE SET UP IN "CHARAC"
                                ; AND "ENDCHR". IF THE TERMINATOR IS A QUOTE, THE QUOTE IS SKIPPED
                                ; OVER. LEADING QUOTES SHOULD BE SKIPPED BEFORE JSR. ON RETURN
                                ; THE CHARACTER AFTER THE STRING LITERAL IS POINTED TO
                                ; BY [STRNG2].
                                ;
.,B487 A2 22    LDX #$22        STRLIT: LDXI    34              ;ASSUME STRING ENDS ON QUOTE.
.,B489 86 07    STX $07                 STX     CHARAC
.,B48B 86 08    STX $08                 STX     ENDCHR
.,B48D 85 6F    STA $6F         STRLT2: STWD    STRNG1          ;SAVE POINTER TO STRING.
.,B48F 84 70    STY $70         
.,B491 85 62    STA $62                 STWD    DSCTMP+1        ;IN CASE NO STRCPY.
.,B493 84 63    STY $63         
.,B495 A0 FF    LDY #$FF                LDYI    255             ;INITIALIZE CHARACTER COUNT.
.,B497 C8       INY             STRGET: INY
.,B498 B1 6F    LDA ($6F),Y             LDADY   STRNG1          ;GET CHARACTER.
.,B49A F0 0C    BEQ $B4A8               BEQ     STRFI1          ;IF ZERO.
.,B49C C5 07    CMP $07                 CMP     CHARAC          ;THIS TERMINATOR?
.,B49E F0 04    BEQ $B4A4               BEQ     STRFIN          ;YES.
.,B4A0 C5 08    CMP $08                 CMP     ENDCHR
.,B4A2 D0 F3    BNE $B497               BNE     STRGET          ;LOOK FURTHER.
.,B4A4 C9 22    CMP #$22        STRFIN: CMPI    34              ;QUOTE?
.,B4A6 F0 01    BEQ $B4A9               BEQ     STRFI2
.,B4A8 18       CLC             STRFI1: CLC                     ;NO, BACK UP.
.,B4A9 84 61    STY $61         STRFI2: STY     DSCTMP          ;RETAIN COUNT.
.,B4AB 98       TYA                     TYA
.,B4AC 65 6F    ADC $6F                 ADC     STRNG1          ;WISHING TO SET [TXTPTR].
.,B4AE 85 71    STA $71                 STA     STRNG2
.,B4B0 A6 70    LDX $70                 LDX     STRNG1+1
.,B4B2 90 01    BCC $B4B5               BCC     STRST2
.,B4B4 E8       INX                     INX
.,B4B5 86 72    STX $72         STRST2: STX     STRNG2+1
.,B4B7 A5 70    LDA $70                 LDA     STRNG1+1        ;IF PAGE 0, COPY SINCE IT IS EITHER
                                                                ;A STRING CONSTANT IN BUF OR A STR$
                                                                ;RESULT IN LOFBUF
                                IFN     BUFPAG,<
.,B4B9 F0 04    BEQ $B4BF               BEQ     STRCP
.,B4BB C9 02    CMP #$02                CMPI    BUFPAG>
.,B4BD D0 0B    BNE $B4CA               BNE     PUTNEW
.,B4BF 98       TYA             STRCP:  TYA
.,B4C0 20 75 B4 JSR $B475               JSR     STRINI
.,B4C3 A6 6F    LDX $6F                 LDXY    STRNG1
.,B4C5 A4 70    LDY $70         
.,B4C7 20 88 B6 JSR $B688               JSR     MOVSTR          ;MOVE STRING.
                                ;
                                ; SOME STRING FUNCTION IS RETURNING A RESULT IN DSCTMP.
                                ; SETUP A TEMP DESCRIPTOR WITH DSCTMP IN IT.
                                ; PUT A POINTER TO THE DESCRIPTOR IN FACMO&LO AND FLAG THE
                                ; RESULT AS TYPE STRING.
                                ;
.,B4CA A6 16    LDX $16         PUTNEW: LDX     TEMPPT          ;POINTER TO FIRST FREE TEMP.
.,B4CC E0 22    CPX #$22                CPXI    TEMPST+STRSIZ*NUMTMP
.,B4CE D0 05    BNE $B4D5               BNE     PUTNW1
.,B4D0 A2 19    LDX #$19                LDXI    ERRST           ;STRING TEMPORARY ERROR.
.,B4D2 4C 37 A4 JMP $A437       ERRGO2: JMP     ERROR           ;GO TELL HIM.
.,B4D5 A5 61    LDA $61         PUTNW1: LDA     DSCTMP
.,B4D7 95 00    STA $00,X               STA     0,X
.,B4D9 A5 62    LDA $62                 LDA     DSCTMP+1
.,B4DB 95 01    STA $01,X               STA     1,X
.,B4DD A5 63    LDA $63                 LDA     DSCTMP+2
.,B4DF 95 02    STA $02,X               STA     2,X
.,B4E1 A0 00    LDY #$00                LDYI    0
.,B4E3 86 64    STX $64                 STXY    FACMO
.,B4E5 84 65    STY $65         
.,B4E7 84 70    STY $70                 STY     FACOV
.,B4E9 88       DEY                     DEY
.,B4EA 84 0D    STY $0D                 STY     VALTYP          ;TYPE IS "STRING".
.,B4EC 86 17    STX $17                 STX     LASTPT          ;SET POINTER TO LAST-USED TEMP.
.,B4EE E8       INX                     INX
.,B4EF E8       INX                     INX
.,B4F0 E8       INX                     INX                     ;POINT FURTHER.
.,B4F1 86 16    STX $16                 STX     TEMPPT          ;SAVE POINTER TO NEXT TEMP IF ANY.
.,B4F3 60       RTS                     RTS                     ;ALL DONE.
                                
                                ;
                                ; GETSPA - GET SPACE FOR CHARACTER STRING.
                                ; MAY FORCE GARBAGE COLLECTION.
                                ;
                                ; # OF CHARACTERS (BYTES) IN ACCA.
                                ; RETURNS WITH POINTER IN [Y,X]. OTHERWISE (IF CAN'T GET
                                ; SPACE) BLOWS OFF TO "OUT OF STRING SPACE" TYPE ERROR.
                                ; ALSO PRESERVES [ACCA] AND SETS [FRESPC]=[Y,X]=PNTR AT SPACE.
                                ;
.,B4F4 46 0F    LSR $0F         GETSPA: LSR     GARBFL          ;SIGNAL NO GARBAGE COLLECTION YET.
.,B4F6 48       PHA             TRYAG2: PHA                     ;SAVE FOR LATER.
.,B4F7 49 FF    EOR #$FF                EORI    255
.,B4F9 38       SEC                     SEC                     ;ADD ONE TO COMPLETE NEGATION.
.,B4FA 65 33    ADC $33                 ADC     FRETOP
.,B4FC A4 34    LDY $34                 LDY     FRETOP+1
.,B4FE B0 01    BCS $B501               BCS     TRYAG3
.,B500 88       DEY                     DEY
.,B501 C4 32    CPY $32         TRYAG3: CPY     STREND+1        ;COMPARE HIGH ORDERS.
.,B503 90 11    BCC $B516               BCC     GARBAG          ;MAKE ROOM FOR MORE.
.,B505 D0 04    BNE $B50B               BNE     STRFRE          ;SAVE NEW FRETOP.
.,B507 C5 31    CMP $31                 CMP     STREND          ;COMPARE LOW ORDERS.
.,B509 90 0B    BCC $B516               BCC     GARBAG          ;CLEAN UP.
.,B50B 85 33    STA $33         STRFRE: STWD    FRETOP          ;SAVE NEW [FRETOP].
.,B50D 84 34    STY $34         
.,B50F 85 35    STA $35                 STWD    FRESPC          ;PUT IT THERE OLD MAN.
.,B511 84 36    STY $36         
.,B513 AA       TAX                     TAX                     ;PRESERVE A IN X.
.,B514 68       PLA                     PLA                     ;GET COUNT BACK IN ACCA.
.,B515 60       RTS                     RTS                     ;ALL DONE.
.,B516 A2 10    LDX #$10        GARBAG: LDXI    ERROM           ;"OUT OF STRING SPACE"
.,B518 A5 0F    LDA $0F                 LDA     GARBFL
.,B51A 30 B6    BMI $B4D2               BMI     ERRGO2
.,B51C 20 26 B5 JSR $B526               JSR     GARBA2
.,B51F A9 80    LDA #$80                LDAI    128
.,B521 85 0F    STA $0F                 STA     GARBFL
.,B523 68       PLA                     PLA                     ;GET BACK STRING LENGTH.
.,B524 D0 D0    BNE $B4F6               BNE     TRYAG2          ;ALWAYS BRANCHES.
                                GARBA2:                         ;START FROM TOP DOWN.
                                IFE     REALIO!DISKO,<
                                        LDAI    7               ;TYPE "BELL".
                                        JSR     OUTDO>
.,B526 A6 37    LDX $37                 LDX     MEMSIZ
.,B528 A5 38    LDA $38                 LDA     MEMSIZ+1
.,B52A 86 33    STX $33         FNDVAR: STX     FRETOP          ;LIKE SO.
.,B52C 85 34    STA $34                 STA     FRETOP+1
.,B52E A0 00    LDY #$00                LDYI    0
.,B530 84 4F    STY $4F                 STY     GRBPNT+1
.,B532 84 4E    STY $4E                 STY     GRBPNT          ;BOTH BYTES SET TO ZERO (FIX BUG)
.,B534 A5 31    LDA $31                 LDWX    STREND
.,B536 A6 32    LDX $32         
.,B538 85 5F    STA $5F                 STWX    GRBTOP
.,B53A 86 60    STX $60         
.,B53C A9 19    LDA #$19                LDWXI   TEMPST
.,B53E A2 00    LDX #$00        
.,B540 85 22    STA $22                 STWX    INDEX1
.,B542 86 23    STX $23         
.,B544 C5 16    CMP $16         TVAR:   CMP     TEMPPT          ;DONE WITH TEMPS?
.,B546 F0 05    BEQ $B54D               BEQ     SVARS           ;YEP.
.,B548 20 C7 B5 JSR $B5C7               JSR     DVAR
.,B54B F0 F7    BEQ $B544               BEQ     TVAR            ;LOOP.
.,B54D A9 07    LDA #$07        SVARS:  LDAI    6+ADDPRC
.,B54F 85 53    STA $53                 STA     FOUR6
.,B551 A5 2D    LDA $2D                 LDWX    VARTAB          ;GET START OF SIMPLE VARIABLES.
.,B553 A6 2E    LDX $2E         
.,B555 85 22    STA $22                 STWX    INDEX1
.,B557 86 23    STX $23         
.,B559 E4 30    CPX $30         SVAR:   CPX     ARYTAB+1        ;DONE WITH SIMPLE VARIABLES?
.,B55B D0 04    BNE $B561               BNE     SVARGO          ;NO.
.,B55D C5 2F    CMP $2F                 CMP     ARYTAB
.,B55F F0 05    BEQ $B566               BEQ     ARYVAR          ;YEP.
.,B561 20 BD B5 JSR $B5BD       SVARGO: JSR     DVARS           ;DO IT , AGAIN.
.,B564 F0 F3    BEQ $B559               BEQ     SVAR            ;LOOP.
.,B566 85 58    STA $58         ARYVAR: STWX    ARYPNT          ;SAVE FOR ADDITION.
.,B568 86 59    STX $59         
.,B56A A9 03    LDA #$03                LDAI    STRSIZ
.,B56C 85 53    STA $53                 STA     FOUR6
.,B56E A5 58    LDA $58         ARYVA2: LDWX    ARYPNT          ;GET THE POINTER TO VARIABLE.
.,B570 A6 59    LDX $59         
.,B572 E4 32    CPX $32         ARYVA3: CPX     STREND+1        ;DONE WITH ARRAYS?
.,B574 D0 07    BNE $B57D               BNE     ARYVGO          ;NO.
.,B576 C5 31    CMP $31                 CMP     STREND
.,B578 D0 03    BNE $B57D               JEQ     GRBPAS          ;YES, GO FINISH UP.
.,B57A 4C 06 B6 JMP $B606       
.,B57D 85 22    STA $22         ARYVGO: STWX    INDEX1
.,B57F 86 23    STX $23         
.,B581 A0 00    LDY #$00                LDYI    1-ADDPRC
                                IFN     ADDPRC,<
.,B583 B1 22    LDA ($22),Y             LDADY   INDEX1
.,B585 AA       TAX                     TAX
.,B586 C8       INY                     INY>
.,B587 B1 22    LDA ($22),Y             LDADY   INDEX1
.,B589 08       PHP                     PHP
.,B58A C8       INY                     INY
.,B58B B1 22    LDA ($22),Y             LDADY   INDEX1
.,B58D 65 58    ADC $58                 ADC     ARYPNT
.,B58F 85 58    STA $58                 STA     ARYPNT          ;FORM POINTER TO NEXT ARRAY VAR.
.,B591 C8       INY                     INY
.,B592 B1 22    LDA ($22),Y             LDADY   INDEX1
.,B594 65 59    ADC $59                 ADC     ARYPNT+1
.,B596 85 59    STA $59                 STA     ARYPNT+1
.,B598 28       PLP                     PLP
.,B599 10 D3    BPL $B56E               BPL     ARYVA2
                                IFN     ADDPRC,<
.,B59B 8A       TXA                     TXA
.,B59C 30 D0    BMI $B56E               BMI     ARYVA2>
.,B59E C8       INY                     INY
.,B59F B1 22    LDA ($22),Y             LDADY   INDEX1
.,B5A1 A0 00    LDY #$00                LDYI    0               ;RESET INDEX Y.
.,B5A3 0A       ASL                     ASL     A,
.,B5A4 69 05    ADC #$05                ADCI    5               ;CARRY IS OFF AND OFF AFTER ADD.
.,B5A6 65 22    ADC $22                 ADC     INDEX1
.,B5A8 85 22    STA $22                 STA     INDEX1
.,B5AA 90 02    BCC $B5AE               BCC     ARYGET
.,B5AC E6 23    INC $23                 INC     INDEX1+1
.,B5AE A6 23    LDX $23         ARYGET: LDX     INDEX1+1
.,B5B0 E4 59    CPX $59         ARYSTR: CPX     ARYPNT+1        ;END OF THE ARRAY?
.,B5B2 D0 04    BNE $B5B8               BNE     GOGO
.,B5B4 C5 58    CMP $58                 CMP     ARYPNT
.,B5B6 F0 BA    BEQ $B572               BEQ     ARYVA3          ;YES.
.,B5B8 20 C7 B5 JSR $B5C7       GOGO:   JSR     DVAR
.,B5BB F0 F3    BEQ $B5B0               BEQ     ARYSTR          ;CYCLE.
                                DVARS:
                                IFN     INTPRC,<
.,B5BD B1 22    LDA ($22),Y             LDADY   INDEX1
.,B5BF 30 35    BMI $B5F6               BMI     DVARTS>
.,B5C1 C8       INY                     INY
.,B5C2 B1 22    LDA ($22),Y             LDADY   INDEX1
.,B5C4 10 30    BPL $B5F6               BPL     DVARTS
.,B5C6 C8       INY                     INY
.,B5C7 B1 22    LDA ($22),Y     DVAR:   LDADY   INDEX1          ;IS LENGTH=0?
.,B5C9 F0 2B    BEQ $B5F6               BEQ     DVARTS          ;YES, RETURN.
.,B5CB C8       INY                     INY
.,B5CC B1 22    LDA ($22),Y             LDADY   INDEX1          ;GET LOW(ADR).
.,B5CE AA       TAX                     TAX
.,B5CF C8       INY                     INY
.,B5D0 B1 22    LDA ($22),Y             LDADY   INDEX1
.,B5D2 C5 34    CMP $34                 CMP     FRETOP+1        ;COMPARE HIGHS.
.,B5D4 90 06    BCC $B5DC               BCC     DVAR2           ;IF THIS STRING'S PNTR .GE. [FRETOP]
.,B5D6 D0 1E    BNE $B5F6               BNE     DVARTS          ;NO NEED TO MESS WITH IT FURTHER.
.,B5D8 E4 33    CPX $33                 CPX     FRETOP          ;COMPARE LOWS.
.,B5DA B0 1A    BCS $B5F6               BCS     DVARTS
.,B5DC C5 60    CMP $60         DVAR2:  CMP     GRBTOP+1
.,B5DE 90 16    BCC $B5F6               BCC     DVARTS          ;IF THIS STRING IS BELOW PREVIOUS,
                                                                ;FORGET IT.
.,B5E0 D0 04    BNE $B5E6               BNE     DVAR3
.,B5E2 E4 5F    CPX $5F                 CPX     GRBTOP          ;COMPARE LOW ORDERS.
.,B5E4 90 10    BCC $B5F6               BCC     DVARTS          ;[X,A] .LE. [GRBTOP].
.,B5E6 86 5F    STX $5F         DVAR3:  STX     GRBTOP
.,B5E8 85 60    STA $60                 STA     GRBTOP+1
.,B5EA A5 22    LDA $22                 LDWX    INDEX1
.,B5EC A6 23    LDX $23         
.,B5EE 85 4E    STA $4E         
.,B5F0 86 4F    STX $4F                 STWX    GRBPNT
.,B5F2 A5 53    LDA $53                 LDA     FOUR6
.,B5F4 85 55    STA $55                 STA     SIZE
.,B5F6 A5 53    LDA $53         DVARTS: LDA     FOUR6
.,B5F8 18       CLC                     CLC
.,B5F9 65 22    ADC $22                 ADC     INDEX1
.,B5FB 85 22    STA $22                 STA     INDEX1
.,B5FD 90 02    BCC $B601               BCC     GRBRTS
.,B5FF E6 23    INC $23                 INC     INDEX1+1
.,B601 A6 23    LDX $23         GRBRTS: LDX     INDEX1+1
.,B603 A0 00    LDY #$00                LDYI    0
.,B605 60       RTS                     RTS                     ;DONE.
                                ;
                                ; HERE WHEN MADE ONE COMPLETE PASS THROUGH STRING VARIABLES.
                                ;
.,B606 A5 4F    LDA $4F         GRBPAS: LDA     GRBPNT+1        ;VARIABLE POINTER.
.,B608 05 4E    ORA $4E                 ORA     GRBPNT
.,B60A F0 F5    BEQ $B601               BEQ     GRBRTS          ;ALL DONE.
.,B60C A5 55    LDA $55                 LDA     SIZE
.,B60E 29 04    AND #$04                ANDI    4               ;LEAVES C OFF.
.,B610 4A       LSR                     LSR     A,
.,B611 A8       TAY                     TAY
.,B612 85 55    STA $55                 STA     SIZE
.,B614 B1 4E    LDA ($4E),Y             LDADY   GRBPNT
                                                                ;NOTE: GRBTOP=LOWTR SO NO NEED TO SET LOWTR.
.,B616 65 5F    ADC $5F                 ADC     LOWTR
.,B618 85 5A    STA $5A                 STA     HIGHTR
.,B61A A5 60    LDA $60                 LDA     LOWTR+1
.,B61C 69 00    ADC #$00                ADCI    0
.,B61E 85 5B    STA $5B                 STA     HIGHTR+1
.,B620 A5 33    LDA $33                 LDWX    FRETOP
.,B622 A6 34    LDX $34         
.,B624 85 58    STA $58                 STWX    HIGHDS          ;WHERE IT ALL GOES.
.,B626 86 59    STX $59         
.,B628 20 BF A3 JSR $A3BF               JSR     BLTUC
.,B62B A4 55    LDY $55                 LDY     SIZE
.,B62D C8       INY                     INY
.,B62E A5 58    LDA $58                 LDA     HIGHDS          ;GET POSITION OF START OF RESULT.
.,B630 91 4E    STA ($4E),Y             STADY   GRBPNT
.,B632 AA       TAX                     TAX
.,B633 E6 59    INC $59                 INC     HIGHDS+1
.,B635 A5 59    LDA $59                 LDA     HIGHDS+1
.,B637 C8       INY                     INY
.,B638 91 4E    STA ($4E),Y             STADY   GRBPNT          ;CHANGE ADDR OF STRING IN VAR.
.,B63A 4C 2A B5 JMP $B52A               JMP     FNDVAR          ;GO TO FNDVAR WITH SOMETHING FOR
                                                                ;[FRETOP].
                                ;
                                ; THE FOLLOWING ROUTINE CONCATENATES TWO STRINGS.
                                ; THE FAC CONTAINS THE FIRST ONE AT THIS POINT.
                                ; [TXTPTR] POINTS TO THE + SIGN.
                                ;
.,B63D A5 65    LDA $65         CAT:    LDA     FACLO           ;PSH HIGH ORDER ONTO STACK.
.,B63F 48       PHA                     PHA
.,B640 A5 64    LDA $64                 LDA     FACMO           ;AND THE LOW.
.,B642 48       PHA                     PHA
.,B643 20 83 AE JSR $AE83               JSR     EVAL            ;CAN COME BACK HERE SINCE
                                                                ;OPERATOR IS KNOWN.
.,B646 20 8F AD JSR $AD8F               JSR     CHKSTR          ;RESULT MUST BE STRING.
.,B649 68       PLA                     PLA
.,B64A 85 6F    STA $6F                 STA     STRNG1          ;GET HIGH ORDER OF OLD DESC.
.,B64C 68       PLA                     PLA
.,B64D 85 70    STA $70                 STA     STRNG1+1
.,B64F A0 00    LDY #$00                LDYI    0
.,B651 B1 6F    LDA ($6F),Y             LDADY   STRNG1          ;GET LENGTH OF OLD STRING.
.,B653 18       CLC                     CLC
.,B654 71 64    ADC ($64),Y             ADCDY   FACMO
.,B656 90 05    BCC $B65D               BCC     SIZEOK          ;RESULT IS LESS THAN 256.
.,B658 A2 17    LDX #$17                LDXI    ERRLS           ;ERROR "LONG STRING".
.,B65A 4C 37 A4 JMP $A437               JMP     ERROR
.,B65D 20 75 B4 JSR $B475       SIZEOK: JSR     STRINI          ;INITIALIZE STRING.
.,B660 20 7A B6 JSR $B67A               JSR     MOVINS          ;MOVE IT.
.,B663 A5 50    LDA $50                 LDWD    DSCPNT          ;GET POINTER TO SECOND.
.,B665 A4 51    LDY $51         
.,B667 20 AA B6 JSR $B6AA               JSR     FRETMP          ;FREE IT.
.,B66A 20 8C B6 JSR $B68C               JSR     MOVDO
.,B66D A5 6F    LDA $6F                 LDWD    STRNG1
.,B66F A4 70    LDY $70         
.,B671 20 AA B6 JSR $B6AA               JSR     FRETMP
.,B674 20 CA B4 JSR $B4CA               JSR     PUTNEW
.,B677 4C B8 AD JMP $ADB8               JMP     TSTOP           ;"CAT" REENTERS FORM EVAL AT TSTOP.
                                
.,B67A A0 00    LDY #$00        MOVINS: LDYI    0               ;GET ADDR OF STRING.
.,B67C B1 6F    LDA ($6F),Y             LDADY   STRNG1
.,B67E 48       PHA                     PHA
.,B67F C8       INY                     INY
.,B680 B1 6F    LDA ($6F),Y             LDADY   STRNG1
.,B682 AA       TAX                     TAX
.,B683 C8       INY                     INY
.,B684 B1 6F    LDA ($6F),Y             LDADY   STRNG1
.,B686 A8       TAY                     TAY
.,B687 68       PLA                     PLA
.,B688 86 22    STX $22         MOVSTR: STXY    INDEX
.,B68A 84 23    STY $23         
.,B68C A8       TAY             MOVDO:  TAY
.,B68D F0 0A    BEQ $B699               BEQ     MVDONE
.,B68F 48       PHA                     PHA
.,B690 88       DEY             MOVLP:  DEY
.,B691 B1 22    LDA ($22),Y             LDADY   INDEX
.,B693 91 35    STA ($35),Y             STADY   FRESPC
.,B695 98       TYA             QMOVE:  TYA
.,B696 D0 F8    BNE $B690               BNE     MOVLP
.,B698 68       PLA                     PLA
.,B699 18       CLC             MVDONE: CLC
.,B69A 65 35    ADC $35                 ADC     FRESPC
.,B69C 85 35    STA $35                 STA     FRESPC
.,B69E 90 02    BCC $B6A2               BCC     MVSTRT
.,B6A0 E6 36    INC $36                 INC     FRESPC+1
.,B6A2 60       RTS             MVSTRT: RTS
                                ;
                                ; "FRETMP" IS PASSED A STRING DESCRIPTOR PNTR IN [Y,A].
                                ; A CHECK IS MADE TO SEE IF THE STRING DESCRIPTOR POINTS TO THE LAST
                                ; TEMPORARY DESCRIPTOR ALLOCATED BY PUTNEW.
                                ; IF SO, THE TEMPORARY IS FREED UP BY THE UPDATING OF [TEMPPT].
                                ; IF A TEMP IS FREED UP, A FURTHER CHECK SEES IF THE STRING DATA THAT
                                ; THAT STRING TEMP PNT'D TO IS THE LOWEST PART OF STRING SPACE IN USE.
                                ; IF SO, [FRETOP] IS UPDATED TO REFLECT THE FACT THE FACT THAT THE SPACE
                                ; IS NO LONGER IN USE.
                                ; THE ADDR OF THE ACTUAL STRING IS RETURNED IN [Y,X] AND
                                ; ITS LENGTH IN ACCA.
                                ;
.,B6A3 20 8F AD JSR $AD8F       FRESTR: JSR     CHKSTR          ;MAKE SURE ITS A STRING.
.,B6A6 A5 64    LDA $64         FREFAC: LDWD    FACMO           ;FREE UP STR PNT'D TO BY FAC.
.,B6A8 A4 65    LDY $65         
.,B6AA 85 22    STA $22         FRETMP: STWD    INDEX           ;GET LENGTH FOR LATER.
.,B6AC 84 23    STY $23         
.,B6AE 20 DB B6 JSR $B6DB               JSR     FRETMS          ;FREE UP THE TEMPORARY DESC.
.,B6B1 08       PHP                     PHP                     ;SAVE CODES.
.,B6B2 A0 00    LDY #$00                LDYI    0               ;PREP TO GET STUFF.
.,B6B4 B1 22    LDA ($22),Y             LDADY   INDEX           ;GET COUNT AND
.,B6B6 48       PHA                     PHA                     ;SAVE IT.
.,B6B7 C8       INY                     INY
.,B6B8 B1 22    LDA ($22),Y             LDADY   INDEX
.,B6BA AA       TAX                     TAX                     ;SAVE LOW ORDER.
.,B6BB C8       INY                     INY
.,B6BC B1 22    LDA ($22),Y             LDADY   INDEX
.,B6BE A8       TAY                     TAY                     ;SAVE HIGH ORDER.
.,B6BF 68       PLA                     PLA
.,B6C0 28       PLP                     PLP                     ;RETURN STATUS.
.,B6C1 D0 13    BNE $B6D6               BNE     FRETRT
.,B6C3 C4 34    CPY $34                 CPY     FRETOP+1        ;STRING IS LAST ONE IN?
.,B6C5 D0 0F    BNE $B6D6               BNE     FRETRT
.,B6C7 E4 33    CPX $33                 CPX     FRETOP
.,B6C9 D0 0B    BNE $B6D6               BNE     FRETRT
.,B6CB 48       PHA                     PHA
.,B6CC 18       CLC                     CLC
.,B6CD 65 33    ADC $33                 ADC     FRETOP
.,B6CF 85 33    STA $33                 STA     FRETOP
.,B6D1 90 02    BCC $B6D5               BCC     FREPLA
.,B6D3 E6 34    INC $34                 INC     FRETOP+1
.,B6D5 68       PLA             FREPLA: PLA                     ;GET COUNT BACK.
.,B6D6 86 22    STX $22         FRETRT: STXY    INDEX           ;SAVE FOR LATER USE.
.,B6D8 84 23    STY $23         
.,B6DA 60       RTS                     RTS
.,B6DB C4 18    CPY $18         FRETMS: CPY     LASTPT+1        ;LAST ENTRY TO TEMP?
.,B6DD D0 0C    BNE $B6EB               BNE     FRERTS
.,B6DF C5 17    CMP $17                 CMP     LASTPT
.,B6E1 D0 08    BNE $B6EB               BNE     FRERTS
.,B6E3 85 16    STA $16                 STA     TEMPPT
.,B6E5 E9 03    SBC #$03                SBCI    STRSIZ          ;POINT TO LAST ONE.
.,B6E7 85 17    STA $17                 STA     LASTPT          ;UPDATE TEMP PNTR.
.,B6E9 A0 00    LDY #$00                LDYI    0               ;ALSO CLEARS ZFLG SO WE DO REST OF FRETMP.
.,B6EB 60       RTS             FRERTS: RTS                     ;ALL DONE.
                                ;
                                ; CHR$(#) CREATES A STRING WHICH CONTAINS AS ITS ONLY
                                ; CHARACTER THE ASCII EQUIVALENT OF THE INTEGER ARGUMENT (#)
                                ; WHICH MUST BE .LT. 255.
                                ;
.,B6EC 20 A1 B7 JSR $B7A1       CHR:    JSR     CONINT          ;GET INTEGER IN RANGE.
.,B6EF 8A       TXA                     TXA
.,B6F0 48       PHA                     PHA
.,B6F1 A9 01    LDA #$01                LDAI    1               ;ONE-CHARACTER STRING.
.,B6F3 20 7D B4 JSR $B47D               JSR     STRSPA          ;GET SPACE FOR STRING.
.,B6F6 68       PLA                     PLA
.,B6F7 A0 00    LDY #$00                LDYI    0
.,B6F9 91 62    STA ($62),Y             STADY   DSCTMP+1
.,B6FB 68       PLA                     PLA                     ;GET RID OF "CHKNUM" RETURN ADDR.
.,B6FC 68       PLA                     PLA
.,B6FD 4C CA B4 JMP $B4CA       RLZRET: JMP     PUTNEW          ;SETUP FAC TO POINT TO DESC.
                                ;
                                ; THE FOLLOWING IS THE LEFT$($,#) FUNCTION.
                                ; IT TAKES THE LEFTMOST # CHARACTERS OF THE STRING.
                                ; IF # .GT. THE LEN OF THE STRING, IT RETURNS THE WHOLE STRING.
                                ;
.,B700 20 61 B7 JSR $B761       LEFT:   JSR     PREAM           ;TEST PARAMETERS.
.,B703 D1 50    CMP ($50),Y             CMPDY   DSCPNT
.,B705 98       TYA                     TYA
.,B706 90 04    BCC $B70C       RLEFT:  BCC     RLEFT1
.,B708 B1 50    LDA ($50),Y             LDADY   DSCPNT
.,B70A AA       TAX                     TAX                     ;PUT LENGTH INTO X.
.,B70B 98       TYA                     TYA                     ;ZERO A, THE OFFSET.
.,B70C 48       PHA             RLEFT1: PHA                     ;SAVE OFFSET.
.,B70D 8A       TXA             RLEFT2: TXA
.,B70E 48       PHA             RLEFT3: PHA                     ;SAVE LENGTH.
.,B70F 20 7D B4 JSR $B47D               JSR     STRSPA          ;GET SPACE.
.,B712 A5 50    LDA $50                 LDWD    DSCPNT
.,B714 A4 51    LDY $51         
.,B716 20 AA B6 JSR $B6AA               JSR     FRETMP
.,B719 68       PLA                     PLA
.,B71A A8       TAY                     TAY
.,B71B 68       PLA                     PLA
.,B71C 18       CLC                     CLC
.,B71D 65 22    ADC $22                 ADC     INDEX           ;COMPUTE WHERE TO COPY.
.,B71F 85 22    STA $22                 STA     INDEX
.,B721 90 02    BCC $B725               BCC     PULMOR
.,B723 E6 23    INC $23                 INC     INDEX+1
.,B725 98       TYA             PULMOR: TYA
.,B726 20 8C B6 JSR $B68C               JSR     MOVDO           ;GO MOVE IT.
.,B729 4C CA B4 JMP $B4CA               JMP     PUTNEW
.,B72C 20 61 B7 JSR $B761       RIGHT:  JSR     PREAM
.,B72F 18       CLC                     CLC                     ;[LENGTH DES'D]-[LENGTH]-1.
.,B730 F1 50    SBC ($50),Y             SBCDY   DSCPNT
.,B732 49 FF    EOR #$FF                EORI    255             ;NEGATE.
.,B734 4C 06 B7 JMP $B706               JMP     RLEFT
                                ;
                                ; MID ($,#) RETURNS STRING WITH CHARS FROM # POSITION
                                ; ONWARD. IF # .GT. LEN ($) THEN RETURN NULL STRING.
                                ; MID ($,#,#) RETURNS STRING WITH CHARACTERS FROM
                                ; # POSITION FOR #2 CHARACTERS. IF #2 GOES PAST END OF STRING
                                ; RETURN AS MUCH AS POSSIBLE.
                                ;
.,B737 A9 FF    LDA #$FF        MID:    LDAI    255             ;DEFAULT.
.,B739 85 65    STA $65                 STA     FACLO           ;SAVE FOR LATER COMPARE.
.,B73B 20 79 00 JSR $0079               JSR     CHRGOT          ;GET CURRENT CHARACTER.
.,B73E C9 29    CMP #$29                CMPI    41              ;IS IT A RIGHT PAREN )?
.,B740 F0 06    BEQ $B748               BEQ     MID2            ;NO THIRD PARAM.
.,B742 20 FD AE JSR $AEFD               JSR     CHKCOM          ;MUST HAVE COMMA.
.,B745 20 9E B7 JSR $B79E               JSR     GETBYT          ;GET THE LENGTH INTO "FACLO".
.,B748 20 61 B7 JSR $B761       MID2:   JSR     PREAM           ;CHECK IT OUT.
.,B74B F0 4B    BEQ $B798               BEQ     GOFUC           ;THERE IS NO POSTION 0
.,B74D CA       DEX                     DEX                     ;COMPUTE OFFSET.
.,B74E 8A       TXA                     TXA
.,B74F 48       PHA                     PHA                     ;PRSERVE AWHILE.
.,B750 18       CLC                     CLC
.,B751 A2 00    LDX #$00                LDXI    0
.,B753 F1 50    SBC ($50),Y             SBCDY   DSCPNT          ;GET LENGTH OF WHAT'S LEFT.
.,B755 B0 B6    BCS $B70D               BCS     RLEFT2          ;GIVE NULL STRING.
.,B757 49 FF    EOR #$FF                EORI    255             ;IN SUB C WAS 0 SO JUST COMPLEMENT.
.,B759 C5 65    CMP $65                 CMP     FACLO           ;GREATER THAN WHAT'S DESIRED?
.,B75B 90 B1    BCC $B70E               BCC     RLEFT3          ;NO, COPY THAT MUCH.
.,B75D A5 65    LDA $65                 LDA     FACLO           ;GET LENGTH OF WHAT'S DESIRED.
.,B75F B0 AD    BCS $B70E               BCS     RLEFT3          ;COPY IT.
                                
                                ;
                                ; USED BY RIGHT$, LEFT$, MID$ FOR PARAMETER CHECKING AND SETUP.
                                ;
.,B761 20 F7 AE JSR $AEF7       PREAM:  JSR     CHKCLS          ;PARAM LIST SHOULD END.
.,B764 68       PLA                     PLA                     ;GET THE RETURN ADDRESS INTO
.,B765 A8       TAY                     TAY                     ;[JMPER+1,Y]
.,B766 68       PLA                     PLA
.,B767 85 55    STA $55                 STA     JMPER+1
.,B769 68       PLA                     PLA                     ;GET RID OF FINGO'S JSR RET ADDR.
.,B76A 68       PLA                     PLA
.,B76B 68       PLA                     PLA                     ;GET LENGTH.
.,B76C AA       TAX                     TAX
.,B76D 68       PLA                     PULWD   DSCPNT
.,B76E 85 50    STA $50         
.,B770 68       PLA             
.,B771 85 51    STA $51         
.,B773 A5 55    LDA $55                 LDA     JMPER+1         ;PUT RETURN ADDRESS BACK ON
.,B775 48       PHA                     PHA
.,B776 98       TYA                     TYA
.,B777 48       PHA                     PHA
.,B778 A0 00    LDY #$00                LDYI    0
.,B77A 8A       TXA                     TXA
.,B77B 60       RTS                     RTS
                                ;
                                ; THE FUNCTION LEN($) RETURNS THE LENGTH OF THE STRING
                                ; PASSED AS AN ARGUMENT.
                                ;
.,B77C 20 82 B7 JSR $B782       LEN:    JSR     LEN1
.,B77F 4C A2 B3 JMP $B3A2               JMP     SNGFLT
.,B782 20 A3 B6 JSR $B6A3       LEN1:   JSR     FRESTR          ;FREE UP STRING.
.,B785 A2 00    LDX #$00                LDXI    0
.,B787 86 0D    STX $0D                 STX     VALTYP          ;FORCE NUMERIC.
.,B789 A8       TAY                     TAY                     ;SET CODES ON LENGTH.
.,B78A 60       RTS                     RTS                     ;DONE.
                                ;
                                ; THE FOLLOWING IS THE ASC($) FUNCTION. IT RETURNS
                                ; AN INTEGER WHICH IS THE DECIMAL ASCII EQUIVALENT.
                                ;
.,B78B 20 82 B7 JSR $B782       ASC:    JSR     LEN1
.,B78E F0 08    BEQ $B798               BEQ     GOFUC           ;NULL STRING, BAD ARG.
.,B790 A0 00    LDY #$00                LDYI    0
.,B792 B1 22    LDA ($22),Y             LDADY   INDEX1          ;GET CHARACTER.
.,B794 A8       TAY                     TAY
.,B795 4C A2 B3 JMP $B3A2               JMP     SNGFLT
.,B798 4C 48 B2 JMP $B248       GOFUC:  JMP     FCERR           ;YES.
                                
.,B79B 20 73 00 JSR $0073       GTBYTC: JSR     CHRGET
.,B79E 20 8A AD JSR $AD8A       GETBYT: JSR     FRMNUM          ;READ FORMULA INTO FAC.
.,B7A1 20 B8 B1 JSR $B1B8       CONINT: JSR     POSINT          ;CONVERT THE FAC TO A SINGLE BYTE INT.
.,B7A4 A6 64    LDX $64                 LDX     FACMO
.,B7A6 D0 F0    BNE $B798               BNE     GOFUC           ;RESULT MUST BE .LE. 255.
.,B7A8 A6 65    LDX $65                 LDX     FACLO
.,B7AA 4C 79 00 JMP $0079       CHRGO2: JMP     CHRGOT          ;SET CONDITION CODES ON TERMINATOR.
                                ;
                                ; THE "VAL" FUNCTION TAKES A STRING AND TURNS IT INTO
                                ; A NUMBER BY INTERPRETING THE ASCII DIGITS ETCQ
                                ; EXCEPT FOR THE PROBLEM THAT A TERMINATOR MUST BE SUPPLIED
                                ; BY REPLACING THE CHARACTER BEYOND THE STRING, VAL IS MERELY
                                ; A CALL TO FLOATING POINT INPUT ("FIN").
                                ;
.,B7AD 20 82 B7 JSR $B782       VAL:    JSR     LEN1            ;DO SETUP. SET RESULT=NUMERIC.
.,B7B0 D0 03    BNE $B7B5               JEQ     ZEROFC          ;ZERO THE FAC ON A NULL STRING
.,B7B2 4C F7 B8 JMP $B8F7       
.,B7B5 A6 7A    LDX $7A                 LDXY    TXTPTR
.,B7B7 A4 7B    LDY $7B         
.,B7B9 86 71    STX $71                 STXY    STRNG2          ;SAVE FOR LATER.
.,B7BB 84 72    STY $72         
.,B7BD A6 22    LDX $22                 LDX     INDEX1
.,B7BF 86 7A    STX $7A                 STX     TXTPTR
.,B7C1 18       CLC                     CLC
.,B7C2 65 22    ADC $22                 ADC     INDEX1
.,B7C4 85 24    STA $24                 STA     INDEX2
.,B7C6 A6 23    LDX $23                 LDX     INDEX1+1
.,B7C8 86 7B    STX $7B                 STX     TXTPTR+1
.,B7CA 90 01    BCC $B7CD               BCC     VAL2            ;NO CARRY, NO INC.
.,B7CC E8       INX                     INX
.,B7CD 86 25    STX $25         VAL2:   STX     INDEX2+1
.,B7CF A0 00    LDY #$00                LDYI    0
.,B7D1 B1 24    LDA ($24),Y             LDADY   INDEX2          ;PRESERVE CHARACTER.
.,B7D3 48       PHA                     PHA
.,B7D4 98       TYA                     LDAI    0               ;SET A TERMINATOR.
.,B7D5 91 24    STA ($24),Y             STADY   INDEX2
.,B7D7 20 79 00 JSR $0079               JSR     CHRGOT          ;GET CHARACTER PNT'D TO AND SET FLAGS.
.,B7DA 20 F3 BC JSR $BCF3               JSR     FIN
.,B7DD 68       PLA                     PLA                     ;GET PRES'D CHARACTER.
.,B7DE A0 00    LDY #$00                LDYI    0
.,B7E0 91 24    STA ($24),Y             STADY   INDEX2          ;STUFF IT BACK.
.,B7E2 A6 71    LDX $71         ST2TXT: LDXY    STRNG2
.,B7E4 A4 72    LDY $72         
.,B7E6 86 7A    STX $7A                 STXY    TXTPTR
.,B7E8 84 7B    STY $7B         
.,B7EA 60       RTS             VALRTS: RTS                     ;ALL DONE WITH STRINGS.
                                PAGE
                                SUBTTL  PEEK, POKE, AND FNWAIT.
                                
.,B7EB 20 8A AD JSR $AD8A       GETNUM: JSR     FRMNUM          ;GET ADDRESS.
.,B7EE 20 F7 B7 JSR $B7F7               JSR     GETADR          ;GET THAT LOCATION.
.,B7F1 20 FD AE JSR $AEFD       COMBYT: JSR     CHKCOM          ;CHECK FOR A COMMA.
.,B7F4 4C 9E B7 JMP $B79E               JMP     GETBYT          ;GET SOMETHING TO STORE AND RETURN.
.,B7F7 A5 66    LDA $66         GETADR: LDA     FACSGN          ;EXAMINE SIGN.
.,B7F9 30 9D    BMI $B798               BMI     GOFUC           ;FUNCTION CALL ERROR.
.,B7FB A5 61    LDA $61                 LDA     FACEXP          ;EXAMINE EXPONENT.
.,B7FD C9 91    CMP #$91                CMPI    145
.,B7FF B0 97    BCS $B798               BCS     GOFUC           ;FUNCTION CALL ERROR.
.,B801 20 9B BC JSR $BC9B               JSR     QINT            ;INTEGERIZE IT.
.,B804 A5 64    LDA $64                 LDWD    FACMO
.,B806 A4 65    LDY $65         
.,B808 84 14    STY $14                 STY     POKER
.,B80A 85 15    STA $15                 STA     POKER+1
.,B80C 60       RTS                     RTS                     ;IT'S DONE !.
                                
.,B80D A5 15    LDA $15         PEEK:   PSHWD   POKER
.,B80F 48       PHA             
.,B810 A5 14    LDA $14         
.,B812 48       PHA             
.,B813 20 F7 B7 JSR $B7F7               JSR     GETADR
.,B816 A0 00    LDY #$00                LDYI    0
                                IFE     REALIO-3,<
                                        CMPI    ROMLOC/256      ;IF WITHIN BASIC,
                                        BCC     GETCON
                                        CMPI    LASTWR/256
                                        BCC     DOSGFL>         ;GIVE HIM ZERO FOR AN ANSWER.
.,B818 B1 14    LDA ($14),Y     GETCON: LDADY   POKER           ;GET THAT BYTE.
.,B81A A8       TAY                     TAY
.,B81B 68       PLA             DOSGFL: PULWD   POKER
.,B81C 85 14    STA $14         
.,B81E 68       PLA             
.,B81F 85 15    STA $15         
.,B821 4C A2 B3 JMP $B3A2               JMP     SNGFLT          ;FLOAT IT.
                                
.,B824 20 EB B7 JSR $B7EB       POKE:   JSR     GETNUM
.,B827 8A       TXA                     TXA
.,B828 A0 00    LDY #$00                LDYI    0
.,B82A 91 14    STA ($14),Y             STADY   POKER           ;STORE VALUE AWAY.
.,B82C 60       RTS                     RTS                     ;SCANNED  EVERYTHING.
                                
                                ; THE WAIT LOCATION,MASK1,MASK2 STATEMENT WAITS UNTIL THE CONTENTS
                                ; OF LOCATION IS NONZERO WHEN XORED WITH MASK2
                                ; AND THEN ANDED WITH MASK1. IF MASK2 IS NOT PRESENT, IT
                                ; IS ASSUMED TO BE ZERO.
                                
.,B82D 20 EB B7 JSR $B7EB       FNWAIT: JSR     GETNUM
.,B830 86 49    STX $49                 STX     ANDMSK
.,B832 A2 00    LDX #$00                LDXI    0
.,B834 20 79 00 JSR $0079               JSR     CHRGOT
.,B837 F0 03    BEQ $B83C               BEQ     ZSTORDO
.,B839 20 F1 B7 JSR $B7F1               JSR     COMBYT          ;GET MASK2.
.,B83C 86 4A    STX $4A         STORDO: STX     EORMSK
.,B83E A0 00    LDY #$00                LDYI    0
.,B840 B1 14    LDA ($14),Y     WAITER: LDADY   POKER
.,B842 45 4A    EOR $4A                 EOR     EORMSK
.,B844 25 49    AND $49                 AND     ANDMSK
.,B846 F0 F8    BEQ $B840               BEQ     WAITER
.,B848 60       RTS             ZERRTS: RTS                     ;GOT A NONZERO.
                                SUBTTL FLOATING POINT MATH PACKAGE CONFIGURATION.
                                
                                RADIX   8                       ;!!!! ALERT !!!!
                                                                ;THROUGHOUT THE MATH PACKAGE.
                                COMMENT %
                                THE FLOATING POINT FORMAT IS AS FOLLOWS:
                                
                                THE SIGN IS THE FIRST BIT OF THE MANTISSA.
                                THE MANTISSA IS 24 BITS LONG.
                                THE BINARY POINT IS TO THE LEFT OF THE MSB.
                                NUMBER = MANTISSA * 2 ^ EXPONENT.
                                THE MANTISSA IS POSITIVE WITH A ONE ASSUMED TO BE WHERE THE SIGN BIT IS.
                                THE SIGN OF THE EXPONENT IS THE FIRST BIT OF THE EXPONENT.
                                THE EXPONENT IS STORED IN EXCESS 200, I.E. WITH A BIAS OF +200.
                                SO, THE EXPONENT IS A SIGNED 8-BIT NUMBER WITH 200 ADDED TO IT.
                                AN EXPONENT OF ZERO MEANS THE NUMBER IS ZERO.
                                THE OTHER BYTES MAY NOT BE ASSUMED TO BE ZERO.
                                TO KEEP THE SAME NUMBER IN THE FAC WHILE SHIFTING,
                                        TO SHIFT RIGHT, EXP:=EXP+1
                                        TO SHIFT LEFT,  EXP:=EXP-1
                                
                                IN MEMORY THE NUMBER LOOKS LIKE THIS:
                                        [THE EXPONENT AS A SIGNED NUMBER +200]
                                        [THE SIGN BIT IN 7, BITS 2-8 OF MANTISSA ARE IN BITS 6-0].
                                                (REMEMBER BIT 1 OF MANTISSA IS ALWAYS A ONE.)
                                        [BITS 9-16 OF THE MANTISSA]
                                        [BITS 17-24] OF THE MANTISSA]
                                
                                ARITHMETIC ROUTINE CALLING CONVENTIONS:
                                
                                FOR ONE ARGUMENT FUNCTIONS:
                                        THE ARGUMENT IS IN THE FAC.
                                        THE RESULT IS LEFT IN THE FAC.
                                FOR TWO ARGUMENT OPERATIONS:
                                        THE FIRST ARGUMENT IS IN ARG (ARGEXP,HO,MO,LO AND ARGSGN).
                                        THE SECOND ARGUMENT IS IN THE FAC.
                                        THE RESULT IS LEFT IN THE FAC.
                                
                                THE "T" ENTRY POINTS TO THE TWO-ARGUMENT OPERATIONS HAVE BOTH ARGUMENTS
                                SETUP IN THE RESPECTIVE REGISTERS. BEFORE CALLING ARG MAY HAVE BEEN
                                POPPED OFF THE STACK AND INTO ARG, FOR EXAMPLE.
                                THE OTHER ENTRY POINT ASSUMES [Y,A] POINTS TO THE ARGUMENT
                                SOMEWHERE IN MEMORY. IT IS UNPACKED INTO ARG BY "CONUPK".
                                
                                ON THE STACK, THE SGN IS PUSHED ON FIRST, THE LO,MO,HO AND FINALLY EXP.
                                NOTE ALL THINGS ARE KEPT UNPACKED IN ARG, FAC AND ON THE STACK.
                                
                                IT IS ONLY WHEN SOMETHING IS STORED AWAY THAT IT IS PACKED TO FOUR
                                BYTES. THE UNPACKED FORMAT HAS A SGN BYTE REFLECTING THE SIGN OF THE
                                NUMBER (POSITIVE=0, NEGATIVE=-1) A HO,MO AND LO WITH THE HIGH BIT
                                OF THE HO TURNED ON. THE EXP IS THE SAME AS STORED FORMAT.
                                THIS IS DONE FOR SPEED OF OPERATION.
                                %
                                PAGE
                                SUBTTL  FLOATING POINT ADDITION AND SUBTRACTION.
.,B849 A9 11    LDA #$11        FADDH:  LDWDI   FHALF           ;ENTRY TO ADD 1/2.
.,B84B A0 BF    LDY #$BF        
.,B84D 4C 67 B8 JMP $B867               JMP     FADD            ;UNPACK AND GO ADD IT.
.,B850 20 8C BA JSR $BA8C       FSUB:   JSR     CONUPK          ;UNPACK ARGUMENT INTO ARG.
.,B853 A5 66    LDA $66         FSUBT:  LDA     FACSGN
.,B855 49 FF    EOR #$FF                EORI    377             ;COMPLEMENT IT.
.,B857 85 66    STA $66                 STA     FACSGN
.,B859 45 6E    EOR $6E                 EOR     ARGSGN          ;COMPLEMENT ARISGN.
.,B85B 85 6F    STA $6F                 STA     ARISGN
.,B85D A5 61    LDA $61                 LDA     FACEXP          ;SET CODES ON FACEXP.
.,B85F 4C 6A B8 JMP $B86A               JMP     FADDT           ;[Y]=ARGEXP..
                                        XLIST
                                .XCREF
                                IFN     REALIO-3,<ZSTORDO=STORDO>
                                IFE     REALIO-3,<
                                ZSTORD:!        LDA     POKER
                                        CMPI    146
                                        BNE     STORDO
                                        LDA     POKER+1
                                        SBCI    31
                                        BNE     STORDO
                                        STA     POKER
                                        TAY
                                        LDAI    200
                                        STA     POKER+1
                                MRCHKR: LDXI    12
                                IF1,<
                                MRCHR:  LDA     60000,X,>
                                IF2,<
                                MRCHR:  LDA     SINCON+36,X,>
                                        ANDI    77
                                        STADY   POKER
                                        INY
                                        BNE     PKINC
                                        INC     POKER+1
                                PKINC:  DEX
                                        BNE     MRCHR
                                        DEC     ANDMSK
                                        BNE     MRCHKR
                                        RTS
                                IF2,<PURGE ZSTORD>>
                                .CREF
                                        LIST
.,B862 20 99 B9 JSR $B999       FADD5:  JSR     SHIFTR          ;DO A LONG SHIFT.
.,B865 90 3C    BCC $B8A3               BCC     FADD4           ;CONTINUE WITH ADDITION.
.,B867 20 8C BA JSR $BA8C       FADD:   JSR     CONUPK
.,B86A D0 03    BNE $B86F       FADDT:  JEQ     MOVFA           ;IF FAC=0, RESULT IS IN ARG.
.,B86C 4C FC BB JMP $BBFC       
.,B86F A6 70    LDX $70                 LDX     FACOV
.,B871 86 56    STX $56                 STX     OLDOV
.,B873 A2 69    LDX #$69                LDXI    ARGEXP          ;DEFAULT IS SHIFT ARGUMENT.
.,B875 A5 69    LDA $69                 LDA     ARGEXP          ;IF ARG=0, FAC IS RESULT.
.,B877 A8       TAY             FADDC:  TAY                     ;ALSO COPY ACCA INTO ACCY.
.,B878 F0 CE    BEQ $B848               BEQ     ZERRTS          ;RETURN.
.,B87A 38       SEC                     SEC
.,B87B E5 61    SBC $61                 SBC     FACEXP
.,B87D F0 24    BEQ $B8A3               BEQ     FADD4           ;NO SHIFTING.
.,B87F 90 12    BCC $B893               BCC     FADDA           ;BR IF ARGEXP.LT.FACEXP.
.,B881 84 61    STY $61                 STY     FACEXP          ;RESULTING EXPONENT.
.,B883 A4 6E    LDY $6E                 LDY     ARGSGN          ;SINCE ARG IS BIGGER, IT'S
.,B885 84 66    STY $66                 STY     FACSGN          ;SIGN IS SIGN OF RESULT.
.,B887 49 FF    EOR #$FF                EORI    377             ;SHIFT A NEGATIVE NUMBER OF PLACES.
.,B889 69 00    ADC #$00                ADCI    0               ;COMPLETE NEGATION. W/ C=1.
.,B88B A0 00    LDY #$00                LDYI    0               ;ZERO OLDOV.
.,B88D 84 56    STY $56                 STY     OLDOV
.,B88F A2 61    LDX #$61                LDXI    FAC             ;SHIFT THE FAC INSTEAD.
.,B891 D0 04    BNE $B897               BNE     FADD1
.,B893 A0 00    LDY #$00        FADDA:  LDYI    0
.,B895 84 70    STY $70                 STY     FACOV
.,B897 C9 F9    CMP #$F9        FADD1:  CMPI    ^D256-7         ;FOR SPEED AND NECESSITY.  GETS
                                                                ;MOST LIKELY CASE TO SHIFTR FASTEST
                                                                ;AND ALLOWS SHIFTING OF NEG NUMS
                                                                ;BY "QINT".
.,B899 30 C7    BMI $B862               BMI     FADD5           ;SHIFT BIG.
.,B89B A8       TAY                     TAY
.,B89C A5 70    LDA $70                 LDA     FACOV           ;SET FACOV.
.,B89E 56 01    LSR $01,X               LSR     1,X,            ;GETS 0 IN MOST SIG BIT.
.,B8A0 20 B0 B9 JSR $B9B0               JSR     ROLSHF          ;DO THE ROLLING.
.,B8A3 24 6F    BIT $6F         FADD4:  BIT     ARISGN          ;GET RESULTING SIGN.
.,B8A5 10 57    BPL $B8FE               BPL     FADD2           ;IF POSITIVE, ADD.
                                                                ;CARRY IS CLEAR.
.,B8A7 A0 61    LDY #$61        FADD3:  LDYI    FACEXP
.,B8A9 E0 69    CPX #$69                CPXI    ARGEXP          ;FAC IS BIGGER.
.,B8AB F0 02    BEQ $B8AF               BEQ     SUBIT
.,B8AD A0 69    LDY #$69                LDYI    ARGEXP          ;ARG IS BIGGER.
.,B8AF 38       SEC             SUBIT:  SEC
.,B8B0 49 FF    EOR #$FF                EORI    377
.,B8B2 65 56    ADC $56                 ADC     OLDOV
.,B8B4 85 70    STA $70                 STA     FACOV
.,B8B6 B9 04 00 LDA $0004,Y             LDA     3+ADDPRC,Y
.,B8B9 F5 04    SBC $04,X               SBC     3+ADDPRC,X
.,B8BB 85 65    STA $65                 STA     FACLO
.,B8BD B9 03 00 LDA $0003,Y             LDA     2+ADDPRC,Y
.,B8C0 F5 03    SBC $03,X               SBC     2+ADDPRC,X
.,B8C2 85 64    STA $64                 STA     FACMO
                                IFN     ADDPRC,<
.,B8C4 B9 02 00 LDA $0002,Y             LDA     2,Y
.,B8C7 F5 02    SBC $02,X               SBC     2,X
.,B8C9 85 63    STA $63                 STA     FACMOH>
.,B8CB B9 01 00 LDA $0001,Y             LDA     1,Y
.,B8CE F5 01    SBC $01,X               SBC     1,X
.,B8D0 85 62    STA $62                 STA     FACHO
.,B8D2 B0 03    BCS $B8D7       FADFLT: BCS     NORMAL          ;HERE IF SIGNS DIFFER. IF CARRY,
                                                                ;FAC IS SET OK.
.,B8D4 20 47 B9 JSR $B947               JSR     NEGFAC          ;NEGATE [FAC].
.,B8D7 A0 00    LDY #$00        NORMAL: LDYI    0
.,B8D9 98       TYA                     TYA
.,B8DA 18       CLC                     CLC
.,B8DB A6 62    LDX $62         NORM3:  LDX     FACHO
.,B8DD D0 4A    BNE $B929               BNE     NORM1
.,B8DF A6 63    LDX $63                 LDX     FACHO+1         ;SHIFT 8 BITS AT A TIME FOR SPEED.
.,B8E1 86 62    STX $62                 STX     FACHO
                                IFN     ADDPRC,<
.,B8E3 A6 64    LDX $64                 LDX     FACMOH+1
.,B8E5 86 63    STX $63                 STX     FACMOH>
.,B8E7 A6 65    LDX $65                 LDX     FACMO+1
.,B8E9 86 64    STX $64                 STX     FACMO
.,B8EB A6 70    LDX $70                 LDX     FACOV
.,B8ED 86 65    STX $65                 STX     FACLO
.,B8EF 84 70    STY $70                 STY     FACOV
.,B8F1 69 08    ADC #$08                ADCI    10
.,B8F3 C9 20    CMP #$20                CMPI    10*ADDPRC+30
.,B8F5 D0 E4    BNE $B8DB               BNE     NORM3
.,B8F7 A9 00    LDA #$00        ZEROFC: LDAI    0               ;NOT NEED BY NORMAL BUT BY OTHERS.
.,B8F9 85 61    STA $61         ZEROF1: STA     FACEXP          ;NUMBER MUST BE ZERO.
.,B8FB 85 66    STA $66         ZEROML: STA     FACSGN          ;MAKE SIGN POSITIVE.
.,B8FD 60       RTS                     RTS                     ;ALL DONE.
.,B8FE 65 56    ADC $56         FADD2:  ADC     OLDOV
.,B900 85 70    STA $70                 STA     FACOV
.,B902 A5 65    LDA $65                 LDA     FACLO
.,B904 65 6D    ADC $6D                 ADC     ARGLO
.,B906 85 65    STA $65                 STA     FACLO
.,B908 A5 64    LDA $64                 LDA     FACMO
.,B90A 65 6C    ADC $6C                 ADC     ARGMO
.,B90C 85 64    STA $64                 STA     FACMO
                                IFN     ADDPRC,<
.,B90E A5 63    LDA $63                 LDA     FACMOH
.,B910 65 6B    ADC $6B                 ADC     ARGMOH
.,B912 85 63    STA $63                 STA     FACMOH>
.,B914 A5 62    LDA $62                 LDA     FACHO
.,B916 65 6A    ADC $6A                 ADC     ARGHO
.,B918 85 62    STA $62                 STA     FACHO
.,B91A 4C 36 B9 JMP $B936               JMP     SQUEEZ          ;GO ROUND IF SIGNS SAME.
                                
.,B91D 69 01    ADC #$01        NORM2:  ADCI    1               ;DECREMENT SHIFT COUNT.
.,B91F 06 70    ASL $70                 ASL     FACOV           ;SHIFT ALL LEFT ONE BIT.
.,B921 26 65    ROL $65                 ROL     FACLO
.,B923 26 64    ROL $64                 ROL     FACMO
                                IFN     ADDPRC,<
.,B925 26 63    ROL $63                 ROL     FACMOH>
.,B927 26 62    ROL $62                 ROL     FACHO
.,B929 10 F2    BPL $B91D       NORM1:  BPL     NORM2           ;IF MSB=0 SHIFT AGAIN.
.,B92B 38       SEC                     SEC
.,B92C E5 61    SBC $61                 SBC     FACEXP
.,B92E B0 C7    BCS $B8F7               BCS     ZEROFC
.,B930 49 FF    EOR #$FF                EORI    377
.,B932 69 01    ADC #$01                ADCI    1               ;COMPLEMENT.
.,B934 85 61    STA $61                 STA     FACEXP
.,B936 90 0E    BCC $B946       SQUEEZ: BCC     RNDRTS          ;BITS TO SHIFT?
.,B938 E6 61    INC $61         RNDSHF: INC     FACEXP
.,B93A F0 42    BEQ $B97E               BEQ     OVERR
.,B93C 66 62    ROR $62                 ROR     FACHO
                                IFN     ADDPRC,<
.,B93E 66 63    ROR $63                 ROR     FACMOH>
.,B940 66 64    ROR $64                 ROR     FACMO
.,B942 66 65    ROR $65                 ROR     FACLO
.,B944 66 70    ROR $70                 ROR     FACOV
.,B946 60       RTS             RNDRTS: RTS                     ;ALL DONE ADDING.
                                
.,B947 A5 66    LDA $66         NEGFAC: COM     FACSGN          ;COMPLEMENT FAC  ENTIRELY.
.,B949 49 FF    EOR #$FF        
.,B94B 85 66    STA $66         
.,B94D A5 62    LDA $62         NEGFCH: COM     FACHO           ;COMPLEMENT JUST THE NUMBER.
.,B94F 49 FF    EOR #$FF        
.,B951 85 62    STA $62         
                                IFN     ADDPRC,<
.,B953 A5 63    LDA $63                 COM     FACMOH>
.,B955 49 FF    EOR #$FF        
.,B957 85 63    STA $63         
.,B959 A5 64    LDA $64                 COM     FACMO
.,B95B 49 FF    EOR #$FF        
.,B95D 85 64    STA $64         
.,B95F A5 65    LDA $65                 COM     FACLO
.,B961 49 FF    EOR #$FF        
.,B963 85 65    STA $65         
.,B965 A5 70    LDA $70                 COM     FACOV
.,B967 49 FF    EOR #$FF        
.,B969 85 70    STA $70         
.,B96B E6 70    INC $70                 INC     FACOV
.,B96D D0 0E    BNE $B97D               BNE     INCFRT
.,B96F E6 65    INC $65         INCFAC: INC     FACLO
.,B971 D0 0A    BNE $B97D               BNE     INCFRT
.,B973 E6 64    INC $64                 INC     FACMO
.,B975 D0 06    BNE $B97D               BNE     INCFRT          ;IF NO CARRY, RETURN.
                                IFN     ADDPRC,<
.,B977 E6 63    INC $63                 INC     FACMOH
.,B979 D0 02    BNE $B97D               BNE     INCFRT>
.,B97B E6 62    INC $62                 INC     FACHO           ;CARRY INCREMENT.
.,B97D 60       RTS             INCFRT: RTS
                                
.,B97E A2 0F    LDX #$0F        OVERR:  LDXI    ERROV
.,B980 4C 37 A4 JMP $A437               JMP     ERROR           ;TELL USER.
                                ;
                                ; "SHIFTR" SHIFTS [X+1:X+3] [-ACCA]  BITS RIGHT.
                                ; SHIFTS BYTES TO START WITH IF POSSIBLE.
                                ;
.,B983 A2 25    LDX #$25        MULSHF: LDXI    RESHO-1         ;ENTRY POINT FOR MULTIPLIER.
.,B985 B4 04    LDY $04,X       SHFTR2: LDY     3+ADDPRC,X,     ;SHIFT BYTES FIRST.
.,B987 84 70    STY $70                 STY     FACOV
                                IFN     ADDPRC,<
.,B989 B4 03    LDY $03,X               LDY     3,X
.,B98B 94 04    STY $04,X               STY     4,X>
.,B98D B4 02    LDY $02,X               LDY     2,X,            ;GET MO.
.,B98F 94 03    STY $03,X               STY     3,X,            ;STORE LO.
.,B991 B4 01    LDY $01,X               LDY     1,X,            ;GET HO.
.,B993 94 02    STY $02,X               STY     2,X,            ;STORE MO.
.,B995 A4 68    LDY $68                 LDY     BITS
.,B997 94 01    STY $01,X               STY     1,X,            ;STORE HO.
.,B999 69 08    ADC #$08        SHIFTR: ADCI    10
.,B99B 30 E8    BMI $B985               BMI     SHFTR2
.,B99D F0 E6    BEQ $B985               BEQ     SHFTR2
.,B99F E9 08    SBC #$08                SBCI    10              ;C CAN BE EITHER 1,0 AND IT WORKS.
.,B9A1 A8       TAY                     TAY
.,B9A2 A5 70    LDA $70                 LDA     FACOV
.,B9A4 B0 14    BCS $B9BA               BCS     SHFTRT          ;EQUIV TO BEQ HERE.
                                IFN     RORSW,<
.,B9A6 16 01    ASL $01,X       SHFTR3: ASL     1,X
.,B9A8 90 02    BCC $B9AC               BCC     SHFTR4
.,B9AA F6 01    INC $01,X               INC     1,X
.,B9AC 76 01    ROR $01,X       SHFTR4: ROR     1,X
.,B9AE 76 01    ROR $01,X               ROR     1,X>            ;YES, TWO OF THEM.
                                IFE     RORSW,<
                                SHFTR3: PHA
                                        LDA     1,X
                                        ANDI    200
                                        LSR     1,X
                                        ORA     1,X
                                        STA     1,X
                                        SKIP1>
                                ROLSHF:
                                IFN     RORSW,<
.,B9B0 76 02    ROR $02,X               ROR     2,X
.,B9B2 76 03    ROR $03,X               ROR     3,X
.,B9B4 76 04    ROR $04,X       IFN     ADDPRC,<        ROR     4,X>    ;ONE MO TIME.
                                >
                                IFE     RORSW,<
                                        PHA
                                        LDAI    0
                                        BCC     SHFTR5
                                        LDAI    200
                                SHFTR5: LSR     2,X
                                        ORA     2,X
                                        STA     2,X
                                        LDAI    0
                                        BCC     SHFTR6
                                        LDAI    200
                                SHFTR6: LSR     3,X
                                        ORA     3,X
                                        STA     3,X
                                IFN     ADDPRC,<
                                        LDAI    0
                                        BCC     SHFT6A
                                        LDAI    200
                                SHFT6A: LSR     4,X
                                        ORA     4,X
                                        STA     4,X>>
.,B9B6 6A       ROR             IFN     RORSW,<ROR      A,>     ;ROTATE ARGUMENT 1 BIT RIGHT.
                                IFE     RORSW,<
                                        PLA
                                        PHP
                                        LSR     A,
                                        PLP
                                        BCC     SHFTR7
                                        ORAI    200>
.,B9B7 C8       INY             SHFTR7: INY
.,B9B8 D0 EC    BNE $B9A6               BNE     SHFTR3          ;$$$ ( MOST EXPENSIVE ! )
.,B9BA 18       CLC             SHFTRT: CLC                     ;CLEAR OUTPUT OF FACOV.
.,B9BB 60       RTS                     RTS
                                PAGE
                                SUBTTL  NATURAL LOG FUNCTION.
                                ;
                                ; CALCULATION IS BY:
                                ; LN(F*2^N)=(N+LOG2(F))*LN(2)
                                ; AN APPROXIMATION POLYNOMIAL IS USED TO CALCULATE LOG2(F).
                                ;  CONSTANTS USED BY LOG:
.:B9BC 81 00 00 00 00           FONE:   201     ; 1.0
                                        000
                                        000
                                        000
                                IFN     ADDPRC,<0>
                                IFE     ADDPRC,<
                                LOGCN2: 2       ; DEGREE-1
                                        200     ; 0.59897437
                                        031
                                        126
                                        142
                                        200     ; 0.96147080
                                        166
                                        042
                                        363
                                        202     ; 2.88539129
                                        070
                                        252
                                        100>
                                
                                IFN     ADDPRC,<
.:B9C1 03                       LOGCN2: 3       ;DEGREE-1
.:B9C2 7F 5E 56 CB 79                   177     ;.43425594188
                                        136
                                        126
                                        313
                                        171
.:B9C7 80 13 9B 0B 64                   200     ; .57658454134
                                        023
                                        233
                                        013
                                        144
.:B9CC 80 76 38 93 16                   200     ; .96180075921
                                        166
                                        070
                                        223
                                        026
.:B9D1 82 38 AA 3B 20                   202     ; 2.8853900728
                                        070
                                        252
                                        073
                                        040>
.:B9D6 80 35 04 F3 34           SQRHLF: 200     ; SQR(0.5)
                                        065
                                        004
                                        363
                                IFN     ADDPRC,<064>
.:B9DB 81 35 04 F3 34           SQRTWO: 201     ; SQR(2.0)
                                        065
                                        004
                                        363
                                IFN     ADDPRC,<064>
.:B9E0 80 80 00 00 00           NEGHLF: 200     ; -1/2
                                        200
                                        000
                                        000
                                IFN     ADDPRC,<0>
.:B9E5 80 31 72 17 F8           LOG2:   200     ; LN(2)
                                        061
                                        162
                                IFE     ADDPRC,<030>
                                IFN     ADDPRC,<027
                                        370>
                                
.,B9EA 20 2B BC JSR $BC2B       LOG:    JSR     SIGN            ;IS IT POSITIVE?
.,B9ED F0 02    BEQ $B9F1               BEQ     LOGERR
.,B9EF 10 03    BPL $B9F4               BPL     LOG1
.,B9F1 4C 48 B2 JMP $B248       LOGERR: JMP     FCERR           ;CAN'T TOLERATE NEG OR ZERO.
.,B9F4 A5 61    LDA $61         LOG1:   LDA     FACEXP          ;GET EXPONENT INTO ACCA.
.,B9F6 E9 7F    SBC #$7F                SBCI    177             ;REMOVE BIAS. (CARRY IS OFF)
.,B9F8 48       PHA                     PHA                     ;SAVE AWHILE.
.,B9F9 A9 80    LDA #$80                LDAI    200
.,B9FB 85 61    STA $61                 STA     FACEXP          ;RESULT IS FAC IN RANGE [0.5,1].
.,B9FD A9 D6    LDA #$D6                LDWDI   SQRHLF          ;GET POINTER TO SQR(0.5).
.,B9FF A0 B9    LDY #$B9        
                                ; CALCULATE (F-SQR(.5))/(F+SQR(.5))
                                
.,BA01 20 67 B8 JSR $B867               JSR     FADD            ;ADD TO FAC.
.,BA04 A9 DB    LDA #$DB                LDWDI   SQRTWO          ;GET SQR(2.).
.,BA06 A0 B9    LDY #$B9        
.,BA08 20 0F BB JSR $BB0F               JSR     FDIV
.,BA0B A9 BC    LDA #$BC                LDWDI   FONE
.,BA0D A0 B9    LDY #$B9        
.,BA0F 20 50 B8 JSR $B850               JSR     FSUB
.,BA12 A9 C1    LDA #$C1                LDWDI   LOGCN2
.,BA14 A0 B9    LDY #$B9        
.,BA16 20 43 E0 JSR $E043               JSR     POLYX           ;EVALUATE APPROXIMATION POLYNOMIAL.
.,BA19 A9 E0    LDA #$E0                LDWDI   NEGHLF          ;ADD IN LAST CONSTANT.
.,BA1B A0 B9    LDY #$B9        
.,BA1D 20 67 B8 JSR $B867               JSR     FADD
.,BA20 68       PLA                     PLA                     ;GET EXPONENT BACK.
.,BA21 20 7E BD JSR $BD7E               JSR     FINLOG          ;ADD IT IN.
.,BA24 A9 E5    LDA #$E5        MULLN2: LDWDI   LOG2            ;MULTIPLY RESULT BY LOG(2.0).
.,BA26 A0 B9    LDY #$B9        ;       JMP     FMULT           ;MULTIPLY TOGETHER.
                                PAGE
                                SUBTTL  FLOATING MULTIPLICATION AND DIVISION.
                                        ;MULTIPLICATION         FAC:=ARG*FAC.
.,BA28 20 8C BA JSR $BA8C       FMULT:  JSR     CONUPK          ;UNPACK THE CONSTANT INTO ARG FOR USE.
.,BA2B D0 03    BNE $BA30       FMULTT: JEQ     MULTRT          ;IF FAC=0, RETURN. FAC IS SET.
.,BA2D 4C 8B BA JMP $BA8B       
.,BA30 20 B7 BA JSR $BAB7               JSR     MULDIV          ;FIX UP THE EXPONENTS.
.,BA33 A9 00    LDA #$00                LDAI    0               ;TO CLEAR RESULT.
.,BA35 85 26    STA $26                 STA     RESHO
                                IFN     ADDPRC,<
.,BA37 85 27    STA $27                 STA     RESMOH>
.,BA39 85 28    STA $28                 STA     RESMO
.,BA3B 85 29    STA $29                 STA     RESLO
.,BA3D A5 70    LDA $70                 LDA     FACOV
.,BA3F 20 59 BA JSR $BA59               JSR     MLTPLY
.,BA42 A5 65    LDA $65                 LDA     FACLO           ;MLTPLY ARG BY FACLO.
.,BA44 20 59 BA JSR $BA59               JSR     MLTPLY
.,BA47 A5 64    LDA $64                 LDA     FACMO           ;MLTPLY ARG BY FACMO.
.,BA49 20 59 BA JSR $BA59               JSR     MLTPLY
                                IFN     ADDPRC,<
.,BA4C A5 63    LDA $63                 LDA     FACMOH
.,BA4E 20 59 BA JSR $BA59               JSR     MLTPLY>
.,BA51 A5 62    LDA $62                 LDA     FACHO           ;MLTPLY ARG BY FACHO.
.,BA53 20 5E BA JSR $BA5E               JSR     MLTPL1
.,BA56 4C 8F BB JMP $BB8F               JMP     MOVFR           ;MOVE RESULT INTO FAC,
                                                                ;NORMALIZE RESULT, AND RETURN.
.,BA59 D0 03    BNE $BA5E       MLTPLY: JEQ     MULSHF          ;SHIFT RESULT RIGHT 1 BYTE.
.,BA5B 4C 83 B9 JMP $B983       
.,BA5E 4A       LSR             MLTPL1: LSR     A,
.,BA5F 09 80    ORA #$80                ORAI    200
.,BA61 A8       TAY             MLTPL2: TAY
.,BA62 90 19    BCC $BA7D               BCC     MLTPL3          ;IT MULT BIT=0, JUST SHIFT.
.,BA64 18       CLC                     CLC
.,BA65 A5 29    LDA $29                 LDA     RESLO
.,BA67 65 6D    ADC $6D                 ADC     ARGLO
.,BA69 85 29    STA $29                 STA     RESLO
.,BA6B A5 28    LDA $28                 LDA     RESMO
.,BA6D 65 6C    ADC $6C                 ADC     ARGMO
.,BA6F 85 28    STA $28                 STA     RESMO
                                IFN     ADDPRC,<
.,BA71 A5 27    LDA $27                 LDA     RESMOH
.,BA73 65 6B    ADC $6B                 ADC     ARGMOH
.,BA75 85 27    STA $27                 STA     RESMOH>
.,BA77 A5 26    LDA $26                 LDA     RESHO
.,BA79 65 6A    ADC $6A                 ADC     ARGHO
.,BA7B 85 26    STA $26                 STA     RESHO
.,BA7D 66 26    ROR $26         MLTPL3: ROR     RESHO
                                IFN     ADDPRC,<
.,BA7F 66 27    ROR $27                 ROR     RESMOH>
.,BA81 66 28    ROR $28                 ROR     RESMO
.,BA83 66 29    ROR $29                 ROR     RESLO
.,BA85 66 70    ROR $70                 ROR     FACOV           ;SAVE FOR ROUNDING.
.,BA87 98       TYA                     TYA
.,BA88 4A       LSR                     LSR     A,              ;CLEAR MSB SO WE GET A CLOSER TO 0.
.,BA89 D0 D6    BNE $BA61               BNE     MLTPL2          ;SLOW AS A TURTLE !
.,BA8B 60       RTS             MULTRT: RTS
                                
                                        ;ROUTINE TO UNPACK MEMORY INTO ARG.
.,BA8C 85 22    STA $22         CONUPK: STWD    INDEX1
.,BA8E 84 23    STY $23         
.,BA90 A0 04    LDY #$04                LDYI    3+ADDPRC
.,BA92 B1 22    LDA ($22),Y             LDADY   INDEX1
.,BA94 85 6D    STA $6D                 STA     ARGLO
.,BA96 88       DEY                     DEY
.,BA97 B1 22    LDA ($22),Y             LDADY   INDEX1
.,BA99 85 6C    STA $6C                 STA     ARGMO
.,BA9B 88       DEY                     DEY
                                IFN     ADDPRC,<
.,BA9C B1 22    LDA ($22),Y             LDADY   INDEX1
.,BA9E 85 6B    STA $6B                 STA     ARGMOH
.,BAA0 88       DEY                     DEY>
.,BAA1 B1 22    LDA ($22),Y             LDADY   INDEX1
.,BAA3 85 6E    STA $6E                 STA     ARGSGN
.,BAA5 45 66    EOR $66                 EOR     FACSGN
.,BAA7 85 6F    STA $6F                 STA     ARISGN
.,BAA9 A5 6E    LDA $6E                 LDA     ARGSGN
.,BAAB 09 80    ORA #$80                ORAI    200
.,BAAD 85 6A    STA $6A                 STA     ARGHO
.,BAAF 88       DEY                     DEY
.,BAB0 B1 22    LDA ($22),Y             LDADY   INDEX1
.,BAB2 85 69    STA $69                 STA     ARGEXP
.,BAB4 A5 61    LDA $61                 LDA     FACEXP          ;SET CODES OF FACEXP.
.,BAB6 60       RTS                     RTS
                                
                                        ;CHECK SPECIAL CASES AND ADD EXPONENTS FOR FMULT, FDIV.
.,BAB7 A5 69    LDA $69         MULDIV: LDA     ARGEXP          ;EXP OF ARG=0?
.,BAB9 F0 1F    BEQ $BADA       MLDEXP: BEQ     ZEREMV          ;SO WE GET ZERO EXPONENT.
.,BABB 18       CLC                     CLC
.,BABC 65 61    ADC $61                 ADC     FACEXP          ;RESULT IS IN ACCA.
.,BABE 90 04    BCC $BAC4               BCC     TRYOFF          ;FIND [C] XOR [N].
.,BAC0 30 1D    BMI $BADF               BMI     GOOVER          ;OVERFLOW IF BITS MATCH.
.,BAC2 18       CLC                     CLC
.:BAC3 2C       .BYTE $2C               SKIP2
.,BAC4 10 14    BPL $BADA       TRYOFF: BPL     ZEREMV          ;UNDERFLOW.
.,BAC6 69 80    ADC #$80                ADCI    200             ;ADD BIAS.
.,BAC8 85 61    STA $61                 STA     FACEXP
.,BACA D0 03    BNE $BACF               JEQ     ZEROML          ;ZERO THE REST OF IT.
.,BACC 4C FB B8 JMP $B8FB       
.,BACF A5 6F    LDA $6F                 LDA     ARISGN
.,BAD1 85 66    STA $66                 STA     FACSGN          ;ARISGN IS RESULT'S SIGN.
.,BAD3 60       RTS                     RTS                     ;DONE.
.,BAD4 A5 66    LDA $66         MLDVEX: LDA     FACSGN          ;GET SIGN.
.,BAD6 49 FF    EOR #$FF                EORI    377             ;COMPLEMENT IT.
.,BAD8 30 05    BMI $BADF               BMI     GOOVER
.,BADA 68       PLA             ZEREMV: PLA                     ;GET ADDR OFF STACK.
.,BADB 68       PLA                     PLA
.,BADC 4C F7 B8 JMP $B8F7               JMP     ZEROFC          ;UNDERFLOW.
.,BADF 4C 7E B9 JMP $B97E       GOOVER: JMP     OVERR           ;OVERFLOW.
                                
                                        ;MULTIPLY FAC BY 10.
.,BAE2 20 0C BC JSR $BC0C       MUL10:  JSR     MOVAF           ;COPY FAC INTO ARG.
.,BAE5 AA       TAX                     TAX
.,BAE6 F0 10    BEQ $BAF8               BEQ     MUL10R          ;IF [FAC]=0, GOT ANSWER.
.,BAE8 18       CLC                     CLC
.,BAE9 69 02    ADC #$02                ADCI    2               ;AUGMENT EXP BY 2.
.,BAEB B0 F2    BCS $BADF               BCS     GOOVER          ;OVERFLOW.
.,BAED A2 00    LDX #$00        FINML6: LDXI    0
.,BAEF 86 6F    STX $6F                 STX     ARISGN          ;SIGNS ARE SAME.
.,BAF1 20 77 B8 JSR $B877               JSR     FADDC           ;ADD TOGETHER.
.,BAF4 E6 61    INC $61                 INC     FACEXP          ;MULTIPLY BY TWO.
.,BAF6 F0 E7    BEQ $BADF               BEQ     GOOVER          ;OVERFLOW.
.,BAF8 60       RTS             MUL10R: RTS
                                
                                        ; DIVIDE FAC BY 10.
.:BAF9 84 20 00 00 00           TENZC:  204
                                        040
                                        000
                                        000
                                IFN     ADDPRC,<0>
.,BAFE 20 0C BC JSR $BC0C       DIV10:  JSR     MOVAF           ;MOVE FAC TO ARG.
.,BB01 A9 F9    LDA #$F9                LDWDI   TENZC           ;POINT TO CONSTANT OF 10.0
.,BB03 A0 BA    LDY #$BA        
.,BB05 A2 00    LDX #$00                LDXI    0               ;SIGNS ARE BOTH POSITIVE.
.,BB07 86 6F    STX $6F         FDIVF:  STX     ARISGN
.,BB09 20 A2 BB JSR $BBA2               JSR     MOVFM           ;PUT IT INTO FAC.
.,BB0C 4C 12 BB JMP $BB12               JMP     FDIVT           ;SKIP OVER NEXT TWO BYTES.
.,BB0F 20 8C BA JSR $BA8C       FDIV:   JSR     CONUPK          ;UNPACK CONSTANT.
.,BB12 F0 76    BEQ $BB8A       FDIVT:  BEQ     DV0ERR          ;CAN'T DIVIDE BY ZERO !
                                                                ;(NOT ENOUGH ROOM TO STORE RESULT.)
.,BB14 20 1B BC JSR $BC1B               JSR     ROUND           ;TAKE FACOV INTO ACCT IN FAC.
.,BB17 A9 00    LDA #$00                LDAI    0               ;NEGATE FACEXP.
.,BB19 38       SEC                     SEC
.,BB1A E5 61    SBC $61                 SBC     FACEXP
.,BB1C 85 61    STA $61                 STA     FACEXP
.,BB1E 20 B7 BA JSR $BAB7               JSR     MULDIV          ;FIX UP EXPONENTS.
.,BB21 E6 61    INC $61                 INC     FACEXP          ;SCALE IT RIGHT.
.,BB23 F0 BA    BEQ $BADF               BEQ     GOOVER          ;OVERFLOW.
.,BB25 A2 FC    LDX #$FC                LDXI    ^D256-3-ADDPRC  ;SETUP PROCEDURE.
.,BB27 A9 01    LDA #$01                LDAI    1
                                DIVIDE:                         ;THIS IS THE BEST CODE IN THE WHOLE PILE.
.,BB29 A4 6A    LDY $6A                 LDY     ARGHO           ;SEE WHAT RELATION HOLDS.
.,BB2B C4 62    CPY $62                 CPY     FACHO
.,BB2D D0 10    BNE $BB3F               BNE     SAVQUO          ;[C]=0,1. N(C=0)=0.
                                IFN     ADDPRC,<
.,BB2F A4 6B    LDY $6B                 LDY     ARGMOH
.,BB31 C4 63    CPY $63                 CPY     FACMOH
.,BB33 D0 0A    BNE $BB3F               BNE     SAVQUO>
.,BB35 A4 6C    LDY $6C                 LDY     ARGMO
.,BB37 C4 64    CPY $64                 CPY     FACMO
.,BB39 D0 04    BNE $BB3F               BNE     SAVQUO
.,BB3B A4 6D    LDY $6D                 LDY     ARGLO
.,BB3D C4 65    CPY $65                 CPY     FACLO
.,BB3F 08       PHP             SAVQUO: PHP
.,BB40 2A       ROL                     ROL     A,              ;SAVE RESULT.
.,BB41 90 09    BCC $BB4C               BCC     QSHFT           ;IF NOT DONE, CONTINUE.
.,BB43 E8       INX                     INX
.,BB44 95 29    STA $29,X               STA     RESLO,X
.,BB46 F0 32    BEQ $BB7A               BEQ     LD100
.,BB48 10 34    BPL $BB7E               BPL     DIVNRM          ;NOTE THIS REQ 1 MO RAM THEN NECESS.
.,BB4A A9 01    LDA #$01                LDAI    1
.,BB4C 28       PLP             QSHFT:  PLP                     ;RETURN CONDITION CODES.
.,BB4D B0 0E    BCS $BB5D               BCS     DIVSUB          ;FAC .LE. ARG.
.,BB4F 06 6D    ASL $6D         SHFARG: ASL     ARGLO           ;SHIFT ARG ONE PLACE LEFT.
.,BB51 26 6C    ROL $6C                 ROL     ARGMO
                                IFN     ADDPRC,<
.,BB53 26 6B    ROL $6B                 ROL     ARGMOH>
.,BB55 26 6A    ROL $6A                 ROL     ARGHO
.,BB57 B0 E6    BCS $BB3F               BCS     SAVQUO          ;SAVE A RESULT OF ONE FOR THIS POSITION
                                                                ;AND DIVIDE.
.,BB59 30 CE    BMI $BB29               BMI     DIVIDE          ;IF MSB ON, GO DECIDE WHETHER TO SUB.
.,BB5B 10 E2    BPL $BB3F               BPL     SAVQUO
.,BB5D A8       TAY             DIVSUB: TAY                     ;NOTICE C MUST BE ON HERE.
.,BB5E A5 6D    LDA $6D                 LDA     ARGLO
.,BB60 E5 65    SBC $65                 SBC     FACLO
.,BB62 85 6D    STA $6D                 STA     ARGLO
.,BB64 A5 6C    LDA $6C                 LDA     ARGMO
.,BB66 E5 64    SBC $64                 SBC     FACMO
.,BB68 85 6C    STA $6C                 STA     ARGMO
                                IFN     ADDPRC,<
.,BB6A A5 6B    LDA $6B                 LDA     ARGMOH
.,BB6C E5 63    SBC $63                 SBC     FACMOH
.,BB6E 85 6B    STA $6B                 STA     ARGMOH>
.,BB70 A5 6A    LDA $6A                 LDA     ARGHO
.,BB72 E5 62    SBC $62                 SBC     FACHO
.,BB74 85 6A    STA $6A                 STA     ARGHO
.,BB76 98       TYA                     TYA
.,BB77 4C 4F BB JMP $BB4F               JMP     SHFARG
.,BB7A A9 40    LDA #$40        LD100:  LDAI    100             ;ONLY WANT TWO MORE BITS.
.,BB7C D0 CE    BNE $BB4C               BNE     QSHFT           ;ALWAYS BRANCHES.
.,BB7E 0A       ASL             DIVNRM: REPEAT  6,<ASL  A>      ;GET LAST TWO BITS INTO MSB AND B6.
.,BB7F 0A       ASL             
.,BB80 0A       ASL             
.,BB81 0A       ASL             
.,BB82 0A       ASL             
.,BB83 0A       ASL             
.,BB84 85 70    STA $70                 STA     FACOV
.,BB86 28       PLP                     PLP                     ;TO GET GARBAGE OFF STACK.
.,BB87 4C 8F BB JMP $BB8F               JMP     MOVFR           ;MOVE RESULT INTO FAC, THEN
                                                                ;NORMALIZE RESULT AND RETURN.
.,BB8A A2 14    LDX #$14        DV0ERR: LDXI    ERRDV0
.,BB8C 4C 37 A4 JMP $A437               JMP     ERROR
                                PAGE
                                SUBTTL  FLOATING POINT MOVEMENT ROUTINES.
                                        ;MOVE RESULT TO FAC.
.,BB8F A5 26    LDA $26         MOVFR:  LDA     RESHO
.,BB91 85 62    STA $62                 STA     FACHO
                                IFN     ADDPRC,<
.,BB93 A5 27    LDA $27                 LDA     RESMOH
.,BB95 85 63    STA $63                 STA     FACMOH>
.,BB97 A5 28    LDA $28                 LDA     RESMO
.,BB99 85 64    STA $64                 STA     FACMO
.,BB9B A5 29    LDA $29                 LDA     RESLO           ;MOVE LO AND SGN.
.,BB9D 85 65    STA $65                 STA     FACLO
.,BB9F 4C D7 B8 JMP $B8D7               JMP     NORMAL          ;ALL DONE.
                                
                                        ;MOVE MEMORY INTO FAC (UNPACKED).
.,BBA2 85 22    STA $22         MOVFM:  STWD    INDEX1
.,BBA4 84 23    STY $23         
.,BBA6 A0 04    LDY #$04                LDYI    3+ADDPRC
.,BBA8 B1 22    LDA ($22),Y             LDADY   INDEX1
.,BBAA 85 65    STA $65                 STA     FACLO
.,BBAC 88       DEY                     DEY
.,BBAD B1 22    LDA ($22),Y             LDADY   INDEX1
.,BBAF 85 64    STA $64                 STA     FACMO
.,BBB1 88       DEY                     DEY
                                IFN     ADDPRC,<
.,BBB2 B1 22    LDA ($22),Y             LDADY   INDEX1
.,BBB4 85 63    STA $63                 STA     FACMOH
.,BBB6 88       DEY                     DEY>
.,BBB7 B1 22    LDA ($22),Y             LDADY   INDEX1
.,BBB9 85 66    STA $66                 STA     FACSGN
.,BBBB 09 80    ORA #$80                ORAI    200
.,BBBD 85 62    STA $62                 STA     FACHO
.,BBBF 88       DEY                     DEY
.,BBC0 B1 22    LDA ($22),Y             LDADY   INDEX1
.,BBC2 85 61    STA $61                 STA     FACEXP          ;LEAVE SWITCHES SET ON EXP.
.,BBC4 84 70    STY $70                 STY     FACOV
.,BBC6 60       RTS                     RTS
                                
                                        ;MOVE NUMBER FROM FAC TO MEMORY.
.,BBC7 A2 5C    LDX #$5C        MOV2F:  LDXI    TEMPF2
.:BBC9 2C       .BYTE $2C               SKIP2
.,BBCA A2 57    LDX #$57        MOV1F:  LDXI    TEMPF1
.,BBCC A0 00    LDY #$00        MOVML:  LDYI    0
.,BBCE F0 04    BEQ $BBD4               BEQ     MOVMF           ;ALWAYS BRANCHES.
.,BBD0 A6 49    LDX $49         MOVVF:  LDXY    FORPNT
.,BBD2 A4 4A    LDY $4A         
.,BBD4 20 1B BC JSR $BC1B       MOVMF:  JSR     ROUND
.,BBD7 86 22    STX $22                 STXY    INDEX1
.,BBD9 84 23    STY $23         
.,BBDB A0 04    LDY #$04                LDYI    3+ADDPRC
.,BBDD A5 65    LDA $65                 LDA     FACLO
.,BBDF 91 22    STA ($22),Y             STADY   INDEX
.,BBE1 88       DEY                     DEY
.,BBE2 A5 64    LDA $64                 LDA     FACMO
.,BBE4 91 22    STA ($22),Y             STADY   INDEX
.,BBE6 88       DEY                     DEY
                                IFN     ADDPRC,<
.,BBE7 A5 63    LDA $63                 LDA     FACMOH
.,BBE9 91 22    STA ($22),Y             STADY   INDEX
.,BBEB 88       DEY                     DEY>
.,BBEC A5 66    LDA $66                 LDA     FACSGN          ;INCLUDE SIGN IN HO.
.,BBEE 09 7F    ORA #$7F                ORAI    177
.,BBF0 25 62    AND $62                 AND     FACHO
.,BBF2 91 22    STA ($22),Y             STADY   INDEX
.,BBF4 88       DEY                     DEY
.,BBF5 A5 61    LDA $61                 LDA     FACEXP
.,BBF7 91 22    STA ($22),Y             STADY   INDEX
.,BBF9 84 70    STY $70                 STY     FACOV           ;ZERO IT SINCE ROUNDED.
.,BBFB 60       RTS                     RTS                     ;[Y]=0.
                                
                                        ;MOVE ARG INTO FAC.
.,BBFC A5 6E    LDA $6E         MOVFA:  LDA     ARGSGN
.,BBFE 85 66    STA $66         MOVFA1: STA     FACSGN
.,BC00 A2 05    LDX #$05                LDXI    4+ADDPRC
.,BC02 B5 68    LDA $68,X       MOVFAL: LDA     ARGEXP-1,X
.,BC04 95 60    STA $60,X               STA     FACEXP-1,X
.,BC06 CA       DEX                     DEX
.,BC07 D0 F9    BNE $BC02               BNE     MOVFAL
.,BC09 86 70    STX $70                 STX     FACOV
.,BC0B 60       RTS                     RTS
                                
                                        ;MOVE FAC INTO ARG.
.,BC0C 20 1B BC JSR $BC1B       MOVAF:  JSR     ROUND
.,BC0F A2 06    LDX #$06        MOVEF:  LDXI    5+ADDPRC
.,BC11 B5 60    LDA $60,X       MOVAFL: LDA     FACEXP-1,X
.,BC13 95 68    STA $68,X               STA     ARGEXP-1,X
.,BC15 CA       DEX                     DEX
.,BC16 D0 F9    BNE $BC11               BNE     MOVAFL
.,BC18 86 70    STX $70                 STX     FACOV           ;ZERO IT SINCE ROUNDED.
.,BC1A 60       RTS             MOVRTS: RTS
                                
.,BC1B A5 61    LDA $61         ROUND:  LDA     FACEXP          ;ZERO?
.,BC1D F0 FB    BEQ $BC1A               BEQ     MOVRTS          ;YES. DONE ROUNDING.
.,BC1F 06 70    ASL $70                 ASL     FACOV           ;ROUND?
.,BC21 90 F7    BCC $BC1A               BCC     MOVRTS          ;NO. MSB OFF.
.,BC23 20 6F B9 JSR $B96F       INCRND: JSR     INCFAC          ;YES, ADD ONE TO LSB(FAC).
.,BC26 D0 F2    BNE $BC1A               BNE     MOVRTS          ;NO CARRY MEANS DONE.
.,BC28 4C 38 B9 JMP $B938               JMP     RNDSHF          ;SQUEEZ MSB IN AND RTS.
                                                                ;NOTE [C]=1 SINCE INCFAC DOESNT TOUCH C.
                                PAGE
                                SUBTTL  SIGN, SGN, FLOAT, NEG, ABS.
                                
                                        ;PUT SIGN OF FAC IN ACCA.
.,BC2B A5 61    LDA $61         SIGN:   LDA     FACEXP
.,BC2D F0 09    BEQ $BC38               BEQ     SIGNRT          ;IF NUMBER IS ZERO, SO IS RESULT.
.,BC2F A5 66    LDA $66         FCSIGN: LDA     FACSGN
.,BC31 2A       ROL             FCOMPS: ROL     A
.,BC32 A9 FF    LDA #$FF                LDAI    ^O377           ;ASSUME NEGATIVE.
.,BC34 B0 02    BCS $BC38               BCS     SIGNRT
.,BC36 A9 01    LDA #$01                LDAI    1               ;GET +1.
.,BC38 60       RTS             SIGNRT: RTS
                                
                                        ;SGN FUNCTION.
.,BC39 20 2B BC JSR $BC2B       SGN:    JSR     SIGN
                                
                                        ;FLOAT THE SIGNED INTEGER IN ACCA.
.,BC3C 85 62    STA $62         FLOAT:  STA     FACHO           ;PUT [ACCA] IN HIGH ORDER.
.,BC3E A9 00    LDA #$00                LDAI    0
.,BC40 85 63    STA $63                 STA     FACHO+1
.,BC42 A2 88    LDX #$88                LDXI    210             ;GET THE EXPONENT.
                                
                                        ;FLOAT THE SIGNED NUMBER IN FAC.
.,BC44 A5 62    LDA $62         FLOATS: LDA     FACHO
.,BC46 49 FF    EOR #$FF                EORI    377
.,BC48 2A       ROL                     ROL     A,              ;GET COMP OF SIGN IN CARRY.
.,BC49 A9 00    LDA #$00        FLOATC: LDAI    0               ;ZERO [ACCA] BUT NOT CARRY.
.,BC4B 85 65    STA $65                 STA     FACLO
                                IFN     ADDPRC,<
.,BC4D 85 64    STA $64                 STA     FACMO>
.,BC4F 86 61    STX $61         FLOATB: STX     FACEXP
.,BC51 85 70    STA $70                 STA     FACOV
.,BC53 85 66    STA $66                 STA     FACSGN
.,BC55 4C D2 B8 JMP $B8D2               JMP     FADFLT
                                
                                        ;ABSOLUTE VALUE OF FAC.
.,BC58 46 66    LSR $66         ABS:    LSR     FACSGN
.,BC5A 60       RTS                     RTS
                                
                                PAGE
                                SUBTTL  COMPARE TWO NUMBERS.
                                        ;A=1 IF ARG .LT. FAC.
                                        ;A=0 IF ARG=FAC.
                                        ;A=-1 IF ARG .GT. FAC.
.,BC5B 85 24    STA $24         FCOMP:  STA     INDEX2
.,BC5D 84 25    STY $25         FCOMPN: STY     INDEX2+1
.,BC5F A0 00    LDY #$00                LDYI    0
.,BC61 B1 24    LDA ($24),Y             LDADY   INDEX2          ;HAS ARGEXP.
.,BC63 C8       INY                     INY                     ;BUMP PNTR UP.
.,BC64 AA       TAX                     TAX                     ;SAVE A IN X AND RESET CODES.
.,BC65 F0 C4    BEQ $BC2B               BEQ     SIGN
.,BC67 B1 24    LDA ($24),Y             LDADY   INDEX2
.,BC69 45 66    EOR $66                 EOR     FACSGN          ;SIGNS THE SAME.
.,BC6B 30 C2    BMI $BC2F               BMI     FCSIGN          ;SIGNS DIFFER SO RESULT IS
                                                                ;SIGN OF FAC AGAIN.
.,BC6D E4 61    CPX $61         FOUTCP: CPX     FACEXP
.,BC6F D0 21    BNE $BC92               BNE     FCOMPC
.,BC71 B1 24    LDA ($24),Y             LDADY   INDEX2
.,BC73 09 80    ORA #$80                ORAI    200
.,BC75 C5 62    CMP $62                 CMP     FACHO
.,BC77 D0 19    BNE $BC92               BNE     FCOMPC
.,BC79 C8       INY                     INY
                                IFN     ADDPRC,<
.,BC7A B1 24    LDA ($24),Y             LDADY   INDEX2
.,BC7C C5 63    CMP $63                 CMP     FACMOH
.,BC7E D0 12    BNE $BC92               BNE     FCOMPC
.,BC80 C8       INY                     INY>
.,BC81 B1 24    LDA ($24),Y             LDADY   INDEX2
.,BC83 C5 64    CMP $64                 CMP     FACMO
.,BC85 D0 0B    BNE $BC92               BNE     FCOMPC
.,BC87 C8       INY                     INY
.,BC88 A9 7F    LDA #$7F                LDAI    177
.,BC8A C5 70    CMP $70                 CMP     FACOV
.,BC8C B1 24    LDA ($24),Y             LDADY   INDEX2
.,BC8E E5 65    SBC $65                 SBC     FACLO           ;GET ZERO IF EQUAL.
.,BC90 F0 28    BEQ $BCBA               BEQ     QINTRT
.,BC92 A5 66    LDA $66         FCOMPC: LDA     FACSGN
.,BC94 90 02    BCC $BC98               BCC     FCOMPD
.,BC96 49 FF    EOR #$FF                EORI    377
.,BC98 4C 31 BC JMP $BC31       FCOMPD: JMP     FCOMPS          ;A PART OF SIGN SETS ACCA UP.
                                
                                PAGE
                                SUBTTL  GREATEST INTEGER FUNCTION.
                                        ;QUICK GREATEST INTEGER FUNCTION.
                                        ;LEAVES INT(FAC) IN FACHO&MO&LO SIGNED.
                                        ;ASSUMES FAC .LT. 2^23 = 8388608
.,BC9B A5 61    LDA $61         QINT:   LDA     FACEXP
.,BC9D F0 4A    BEQ $BCE9               BEQ     CLRFAC          ;IF ZERO, GOT IT.
.,BC9F 38       SEC                     SEC
.,BCA0 E9 A0    SBC #$A0                SBCI    8*ADDPRC+230    ;GET NUMBER OF PLACES TO SHIFT.
.,BCA2 24 66    BIT $66                 BIT     FACSGN
.,BCA4 10 09    BPL $BCAF               BPL     QISHFT
.,BCA6 AA       TAX                     TAX
.,BCA7 A9 FF    LDA #$FF                LDAI    377
.,BCA9 85 68    STA $68                 STA     BITS            ;PUT 377 IN WHEN SHFTR SHIFTS BYTES.
.,BCAB 20 4D B9 JSR $B94D               JSR     NEGFCH          ;TRULY NEGATE QUANTITY IN FAC.
.,BCAE 8A       TXA                     TXA
.,BCAF A2 61    LDX #$61        QISHFT: LDXI    FAC
.,BCB1 C9 F9    CMP #$F9                CMPI    ^D256-7
.,BCB3 10 06    BPL $BCBB               BPL     QINT1           ;IF NUMBER OF PLACES .GE. 7
                                                                ;SHIFT 1 PLACE AT A TIME.
.,BCB5 20 99 B9 JSR $B999               JSR     SHIFTR          ;START SHIFTING BYTES, THEN BITS.
.,BCB8 84 68    STY $68                 STY     BITS            ;ZERO BITS SINCE ADDER WANTS ZERO.
.,BCBA 60       RTS             QINTRT: RTS
.,BCBB A8       TAY             QINT1:  TAY                     ;PUT COUNT IN COUNTER.
.,BCBC A5 66    LDA $66                 LDA     FACSGN
.,BCBE 29 80    AND #$80                ANDI    200             ;GET SIGN BIT.
.,BCC0 46 62    LSR $62                 LSR     FACHO           ;SAVE FIRST SHIFTED BYTE.
.,BCC2 05 62    ORA $62                 ORA     FACHO
.,BCC4 85 62    STA $62                 STA     FACHO
.,BCC6 20 B0 B9 JSR $B9B0               JSR     ROLSHF          ;SHIFT THE REST.
.,BCC9 84 68    STY $68                 STY     BITS            ;ZERO [BITS].
.,BCCB 60       RTS                     RTS
                                
                                        ;GREATEST INTEGER FUNCTION.
.,BCCC A5 61    LDA $61         INT:    LDA     FACEXP
.,BCCE C9 A0    CMP #$A0                CMPI    8*ADDPRC+230
.,BCD0 B0 20    BCS $BCF2               BCS     INTRTS          ;FORGET IT.
.,BCD2 20 9B BC JSR $BC9B               JSR     QINT
.,BCD5 84 70    STY $70                 STY     FACOV           ;CLR OVERFLOW BYTE.
.,BCD7 A5 66    LDA $66                 LDA     FACSGN
.,BCD9 84 66    STY $66                 STY     FACSGN          ;MAKE FAC LOOK POSITIVE.
.,BCDB 49 80    EOR #$80                EORI    200             ;GET COMPLEMENT OF SIGN IN CARRY.
.,BCDD 2A       ROL                     ROL     A,
.,BCDE A9 A0    LDA #$A0                LDAI    8*ADDPRC+230
.,BCE0 85 61    STA $61                 STA     FACEXP
.,BCE2 A5 65    LDA $65                 LDA     FACLO
.,BCE4 85 07    STA $07                 STA     INTEGR
.,BCE6 4C D2 B8 JMP $B8D2               JMP     FADFLT
.,BCE9 85 62    STA $62         CLRFAC: STA     FACHO           ;MAKE IT REALLY ZERO.
.,BCEB 85 63    STA $63         IFN     ADDPRC,<STA FACMOH>
.,BCED 85 64    STA $64                 STA     FACMO
.,BCEF 85 65    STA $65                 STA     FACLO
.,BCF1 A8       TAY                     TAY
.,BCF2 60       RTS             INTRTS: RTS
                                PAGE
                                SUBTTL  FLOATING POINT INPUT ROUTINE.
                                        ;NUMBER INPUT IS LEFT IN FAC.
                                        ;AT ENTRY [TXTPTR] POINTS TO THE FIRST CHARACTER IN A TEXT BUFFER.
                                        ;THE FIRST CHARACTER IS ALSO IN ACCA. FIN PACKS THE DIGITS
                                        ;INTO THE FAC AS AN INTEGER AND KEEPS TRACK OF WHERE THE
                                        ;DECIMAL POINT IS. [DPTFLG] TELL WHETHER A DP HAS BEEN
                                        ;SEEN. [DECCNT] IS THE NUMBER OF DIGITS AFTER THE DP.
                                        ;AT THE END [DECCNT] AND THE EXPONENT ARE USED TO
                                        ;DETERMINE HOW MANY TIMES TO MULTIPLY OR DIVIDE BY TEN
                                        ;TO GET THE CORRECT NUMBER.
.,BCF3 A0 00    LDY #$00        FIN:    LDYI    0               ;ZERO FACSGN&SGNFLG.
.,BCF5 A2 0A    LDX #$0A                LDXI    11+ADDPRC       ;ZERO EXP AND HO (AND MOH).
.,BCF7 94 5D    STY $5D,X       FINZLP: STY     DECCNT,X        ;ZERO MO AND LO.
.,BCF9 CA       DEX                     DEX                     ;ZERO TENEXP AND EXPSGN
.,BCFA 10 FB    BPL $BCF7               BPL     FINZLP          ;ZERO DECCNT, DPTFLG.
.,BCFC 90 0F    BCC $BD0D               BCC     FINDGQ          ;FLAGS STILL SET FROM CHRGET.
.,BCFE C9 2D    CMP #$2D                CMPI    "-"             ;A NEGATIVE SIGN?
.,BD00 D0 04    BNE $BD06               BNE     QPLUS           ;NO, TRY PLUS SIGN.
.,BD02 86 67    STX $67                 STX     SGNFLG          ;IT'S NEGATIVE. (X=377).
.,BD04 F0 04    BEQ $BD0A               BEQ     FINC            ;ALWAYS BRANCHES.
.,BD06 C9 2B    CMP #$2B        QPLUS:  CMPI    "+"             ;PLUS SIGN?
.,BD08 D0 05    BNE $BD0F               BNE     FIN1            ;YES, SKIP IT.
.,BD0A 20 73 00 JSR $0073       FINC:   JSR     CHRGET
.,BD0D 90 5B    BCC $BD6A       FINDGQ: BCC     FINDIG
.,BD0F C9 2E    CMP #$2E        FIN1:   CMPI    "."             ;THE DP?
.,BD11 F0 2E    BEQ $BD41               BEQ     FINDP           ;NO KIDDING.
.,BD13 C9 45    CMP #$45                CMPI    "E"             ;EXPONENT FOLLOWS.
.,BD15 D0 30    BNE $BD47               BNE     FINE            ;NO.
                                        ;HERE TO CHECK FOR SIGN OF EXP.
.,BD17 20 73 00 JSR $0073               JSR     CHRGET          ;YES. GET ANOTHER.
.,BD1A 90 17    BCC $BD33               BCC     FNEDG1          ;IT IS A DIGIT. (EASIER THAN
                                                                ;BACKING UP POINTER.)
.,BD1C C9 AB    CMP #$AB                CMPI    MINUTK          ;MINUS?
.,BD1E F0 0E    BEQ $BD2E               BEQ     FINEC1          ;NEGATE.
.,BD20 C9 2D    CMP #$2D                CMPI    "-"             ;MINUS SIGN?
.,BD22 F0 0A    BEQ $BD2E               BEQ     FINEC1
.,BD24 C9 AA    CMP #$AA                CMPI    PLUSTK          ;PLUS?
.,BD26 F0 08    BEQ $BD30               BEQ     FINEC
.,BD28 C9 2B    CMP #$2B                CMPI    "+"             ;PLUS SIGN?
.,BD2A F0 04    BEQ $BD30               BEQ     FINEC
.,BD2C D0 07    BNE $BD35               BNE     FINEC2
.,BD2E 66 60    ROR $60         FINEC1: ROR     EXPSGN          ;TURN IT ON.
.,BD30 20 73 00 JSR $0073       FINEC:  JSR     CHRGET          ;GET ANOTHER.
.,BD33 90 5C    BCC $BD91       FNEDG1: BCC     FINEDG          ;IT IS A DIGIT.
.,BD35 24 60    BIT $60         FINEC2: BIT     EXPSGN
.,BD37 10 0E    BPL $BD47               BPL     FINE
.,BD39 A9 00    LDA #$00                LDAI    0
.,BD3B 38       SEC                     SEC
.,BD3C E5 5E    SBC $5E                 SBC     TENEXP
.,BD3E 4C 49 BD JMP $BD49               JMP     FINE1
.,BD41 66 5F    ROR $5F         FINDP:  ROR     DPTFLG
.,BD43 24 5F    BIT $5F                 BIT     DPTFLG
.,BD45 50 C3    BVC $BD0A               BVC     FINC
.,BD47 A5 5E    LDA $5E         FINE:   LDA     TENEXP
.,BD49 38       SEC             FINE1:  SEC
.,BD4A E5 5D    SBC $5D                 SBC     DECCNT          ;GET NUMBER OF PLACES TO SHIFT.
.,BD4C 85 5E    STA $5E                 STA     TENEXP
.,BD4E F0 12    BEQ $BD62               BEQ     FINQNG          ;NEGATE?
.,BD50 10 09    BPL $BD5B               BPL     FINMUL          ;POSITIVE SO MULTIPLY.
.,BD52 20 FE BA JSR $BAFE       FINDIV: JSR     DIV10
.,BD55 E6 5E    INC $5E                 INC     TENEXP          ;DONE?
.,BD57 D0 F9    BNE $BD52               BNE     FINDIV          ;NO.
.,BD59 F0 07    BEQ $BD62               BEQ     FINQNG          ;YES.
.,BD5B 20 E2 BA JSR $BAE2       FINMUL: JSR     MUL10
.,BD5E C6 5E    DEC $5E                 DEC     TENEXP          ;DONE?
.,BD60 D0 F9    BNE $BD5B               BNE     FINMUL          ;NO
.,BD62 A5 67    LDA $67         FINQNG: LDA     SGNFLG
.,BD64 30 01    BMI $BD67               BMI     NEGXQS          ;IF POSITIVE, RETURN.
.,BD66 60       RTS                     RTS
.,BD67 4C B4 BF JMP $BFB4       NEGXQS: JMP     NEGOP           ;OTHERWISE, NEGATE AND RETURN.
                                
.,BD6A 48       PHA             FINDIG: PHA
.,BD6B 24 5F    BIT $5F                 BIT     DPTFLG
.,BD6D 10 02    BPL $BD71               BPL     FINDG1
.,BD6F E6 5D    INC $5D                 INC     DECCNT
.,BD71 20 E2 BA JSR $BAE2       FINDG1: JSR     MUL10
.,BD74 68       PLA                     PLA                     ;GET IT BACK.
.,BD75 38       SEC                     SEC
.,BD76 E9 30    SBC #$30                SBCI    "0"
.,BD78 20 7E BD JSR $BD7E               JSR     FINLOG          ;ADD IT IN.
.,BD7B 4C 0A BD JMP $BD0A               JMP     FINC
                                
.,BD7E 48       PHA             FINLOG: PHA
.,BD7F 20 0C BC JSR $BC0C               JSR     MOVAF           ;SAVE FAC FOR LATER.
.,BD82 68       PLA                     PLA
.,BD83 20 3C BC JSR $BC3C               JSR     FLOAT           ;FLOAT THE VALUE IN ACCA.
.,BD86 A5 6E    LDA $6E                 LDA     ARGSGN
.,BD88 45 66    EOR $66                 EOR     FACSGN
.,BD8A 85 6F    STA $6F                 STA     ARISGN          ;RESULTANT SIGN.
.,BD8C A6 61    LDX $61                 LDX     FACEXP          ;SET SIGNS ON THING TO ADD.
.,BD8E 4C 6A B8 JMP $B86A               JMP     FADDT           ;ADD TOGETHER AND RETURN.
                                
                                        ;HERE PACK IN THE NEXT DIGIT OF THE EXPONENT.
                                        ;MULTIPLY THE OLD EXP BY 10 AND ADD IN THE NEXT
                                        ;DIGIT. NOTE: EXP OVERFLOW IS NOT CHECKED FOR.
.,BD91 A5 5E    LDA $5E         FINEDG: LDA     TENEXP          ;GET EXP SO FAR.
.,BD93 C9 0A    CMP #$0A                CMPI    12              ;WILL RESULT BE .GE. 100?
.,BD95 90 09    BCC $BDA0               BCC     MLEX10
.,BD97 A9 64    LDA #$64                LDAI    144             ;GET 100.
.,BD99 24 60    BIT $60                 BIT     EXPSGN
.,BD9B 30 11    BMI $BDAE               BMI     MLEXMI          ;IF NEG EXP, NO CHK FOR OVERR.
.,BD9D 4C 7E B9 JMP $B97E               JMP     OVERR
.,BDA0 0A       ASL             MLEX10: ASL     A,              ;MULT BY 2 TWICE
.,BDA1 0A       ASL                     ASL     A
.,BDA2 18       CLC                     CLC                     ;POSSIBLE SHIFT OUT OF HIGH.
.,BDA3 65 5E    ADC $5E                 ADC     TENEXP          ;LIKE MULTIPLYING BY FIVE.
.,BDA5 0A       ASL                     ASL     A,              ;AND NOW BY TEN.
.,BDA6 18       CLC                     CLC
.,BDA7 A0 00    LDY #$00                LDYI    0
.,BDA9 71 7A    ADC ($7A),Y             ADCDY   TXTPTR
.,BDAB 38       SEC                     SEC
.,BDAC E9 30    SBC #$30                SBCI    "0"
.,BDAE 85 5E    STA $5E         MLEXMI: STA     TENEXP          ;SAVE RESULT.
.,BDB0 4C 30 BD JMP $BD30               JMP     FINEC
                                PAGE
                                SUBTTL  FLOATING POINT OUTPUT ROUTINE.
                                
                                IFE     ADDPRC,<
                                NZ0999: 221     ; 99999.9499
                                        103
                                        117
                                        370
                                NZ9999: 224     ; 999999.499
                                        164
                                        043
                                        367
                                NZMIL:  224     ; 10^6.
                                        164
                                        044
                                        000>
                                IFN     ADDPRC,<
.:BDB3 9B 3E BC 1F FD           NZ0999: 233     ; 99999999.9499
                                        076
                                        274
                                        037
                                        375
.:BDB8 9E 6E 6B 27 FD           NZ9999: 236     ; 999999999.499
                                        156
                                        153
                                        047
                                        375
.:BDBD 9E 6E 6B 28 00           NZMIL:  236     ; 10^9
                                        156
                                        153
                                        050
                                        000>
                                        ;ENTRY TO LINPRT.
.,BDC2 A9 71    LDA #$71        INPRT:  LDWDI   INTXT
.,BDC4 A0 A3    LDY #$A3        
.,BDC6 20 DA BD JSR $BDDA               JSR     STROU2
.,BDC9 A5 3A    LDA $3A                 LDA     CURLIN+1
.,BDCB A6 39    LDX $39                 LDX     CURLIN
.,BDCD 85 62    STA $62         LINPRT: STWX    FACHO
.,BDCF 86 63    STX $63         
.,BDD1 A2 90    LDX #$90                LDXI    220             ;EXPONENT OF 16.
.,BDD3 38       SEC                     SEC                     ;NUMBER IS POSITIVE.
.,BDD4 20 49 BC JSR $BC49               JSR     FLOATC
.,BDD7 20 DF BD JSR $BDDF               JSR     FOUT
.,BDDA 4C 1E AB JMP $AB1E       STROU2: JMP     STROUT          ;PRINT AND RETURN.
                                
.,BDDD A0 01    LDY #$01        FOUT:   LDYI    1
.,BDDF A9 20    LDA #$20        FOUTC:  LDAI    " "             ;PRINT SPACE IF POSITIVE.
.,BDE1 24 66    BIT $66                 BIT     FACSGN
.,BDE3 10 02    BPL $BDE7               BPL     FOUT1
.,BDE5 A9 2D    LDA #$2D                LDAI    "-"
.,BDE7 99 FF 00 STA $00FF,Y     FOUT1:  STA     FBUFFR-1,Y,     ;STORE THE CHARACTER.
.,BDEA 85 66    STA $66                 STA     FACSGN          ;MAKE FAC POS FOR QINT.
.,BDEC 84 71    STY $71                 STY     FBUFPT          ;SAVE FOR LATER.
.,BDEE C8       INY                     INY
.,BDEF A9 30    LDA #$30                LDAI    "0"             ;GET ZERO TO TYPE IF FAC=0.
.,BDF1 A6 61    LDX $61                 LDX     FACEXP
.,BDF3 D0 03    BNE $BDF8               JEQ     FOUT19
.,BDF5 4C 04 BF JMP $BF04       
.,BDF8 A9 00    LDA #$00                LDAI     0
.,BDFA E0 80    CPX #$80                CPXI    200             ;IS NUMBER .LT. 1.0 ?
.,BDFC F0 02    BEQ $BE00               BEQ     FOUT37          ;NO.
.,BDFE B0 09    BCS $BE09               BCS     FOUT7
.,BE00 A9 BD    LDA #$BD        FOUT37: LDWDI   NZMIL           ;MULTIPLY BY 10^6.
.,BE02 A0 BD    LDY #$BD        
.,BE04 20 28 BA JSR $BA28               JSR     FMULT
.,BE07 A9 F7    LDA #$F7                LDAI    ^D256-3*ADDPRC-6
.,BE09 85 5D    STA $5D         FOUT7:  STA     DECCNT          ;SAVE COUNT OR ZERO IT.
.,BE0B A9 B8    LDA #$B8        FOUT4:  LDWDI   NZ9999
.,BE0D A0 BD    LDY #$BD        
.,BE0F 20 5B BC JSR $BC5B               JSR     FCOMP           ;IS NUMBER .GT. 999999.499 ?
                                                                ;OR 999999999.499?
.,BE12 F0 1E    BEQ $BE32               BEQ     BIGGES
.,BE14 10 12    BPL $BE28               BPL     FOUT9           ;YES. MAKE IT SMALLER.
.,BE16 A9 B3    LDA #$B3        FOUT3:  LDWDI   NZ0999
.,BE18 A0 BD    LDY #$BD        
.,BE1A 20 5B BC JSR $BC5B               JSR     FCOMP           ;IS NUMBER .GT. 99999.9499 ?
                                                                ; OR 99999999.9499?
.,BE1D F0 02    BEQ $BE21               BEQ     FOUT38
.,BE1F 10 0E    BPL $BE2F               BPL     FOUT5           ;YES. DONE MULTIPLYING.
.,BE21 20 E2 BA JSR $BAE2       FOUT38: JSR     MUL10           ;MAKE IT BIGGER.
.,BE24 C6 5D    DEC $5D                 DEC     DECCNT
.,BE26 D0 EE    BNE $BE16               BNE     FOUT3           ;SEE IF THAT DOES IT.
                                                                ;THIS ALWAYS GOES.
.,BE28 20 FE BA JSR $BAFE       FOUT9:  JSR     DIV10           ;MAKE IT SMALLER.
.,BE2B E6 5D    INC $5D                 INC     DECCNT
.,BE2D D0 DC    BNE $BE0B               BNE     FOUT4           ;SEE IF THAT DOES IT.
                                                                ;THIS ALWAYS GOES.
                                
.,BE2F 20 49 B8 JSR $B849       FOUT5:  JSR     FADDH           ;ADD A HALF TO ROUND UP.
.,BE32 20 9B BC JSR $BC9B       BIGGES: JSR     QINT
.,BE35 A2 01    LDX #$01                LDXI    1               ;DECIMAL POINT COUNT.
.,BE37 A5 5D    LDA $5D                 LDA     DECCNT
.,BE39 18       CLC                     CLC
.,BE3A 69 0A    ADC #$0A                ADCI    3*ADDPRC+7      ;SHOULD NUMBER BE PRINTED IN E NOTATION?
                                                                ;IE, IS NUMBER .LT. .01 ?
.,BE3C 30 09    BMI $BE47               BMI     FOUTPI          ;YES.
.,BE3E C9 0B    CMP #$0B                CMPI    3*ADDPRC+10     ;IS IT .GT. 999999 (999999999)?
.,BE40 B0 06    BCS $BE48               BCS     FOUT6           ;YES. USE E NOTATION.
.,BE42 69 FF    ADC #$FF                ADCI    ^O377           ;NUMBER OF PLACES BEFORE DECIMAL POINT.
.,BE44 AA       TAX                     TAX                     ;PUT INTO ACCX.
.,BE45 A9 02    LDA #$02                LDAI    2               ;NO E NOTATION.
.,BE47 38       SEC             FOUTPI: SEC
.,BE48 E9 02    SBC #$02        FOUT6:  SBCI    2               ;EFFECTIVELY ADD 5 TO ORIG EXP.
.,BE4A 85 5E    STA $5E                 STA     TENEXP          ;THAT IS THE EXPONENT TO PRINT.
.,BE4C 86 5D    STX $5D                 STX     DECCNT          ;NUMBER OF DECIMAL PLACES.
.,BE4E 8A       TXA                     TXA
.,BE4F F0 02    BEQ $BE53               BEQ     FOUT39
.,BE51 10 13    BPL $BE66               BPL     FOUT8           ;SOME PLACES BEFORE DEC PNT.
.,BE53 A4 71    LDY $71         FOUT39: LDY     FBUFPT          ;GET POINTER TO OUTPUT.
.,BE55 A9 2E    LDA #$2E                LDAI    "."             ;PUT IN "."
.,BE57 C8       INY                     INY
.,BE58 99 FF 00 STA $00FF,Y             STA     FBUFFR-1,Y
.,BE5B 8A       TXA                     TXA
.,BE5C F0 06    BEQ $BE64               BEQ     FOUT16
.,BE5E A9 30    LDA #$30                LDAI    "0"             ;GET THE ENSUING ZERO.
.,BE60 C8       INY                     INY
.,BE61 99 FF 00 STA $00FF,Y             STA     FBUFFR-1,Y
.,BE64 84 71    STY $71         FOUT16: STY     FBUFPT          ;SAVE FOR LATER.
.,BE66 A0 00    LDY #$00        FOUT8:  LDYI    0
.,BE68 A2 80    LDX #$80        FOUTIM: LDXI    200             ;FIRST PASS THRU, ACCX HAS MSB SET.
.,BE6A A5 65    LDA $65         FOUT2:  LDA     FACLO
.,BE6C 18       CLC                     CLC
.,BE6D 79 19 BF ADC $BF19,Y             ADC     FOUTBL+2+ADDPRC,Y
.,BE70 85 65    STA $65                 STA     FACLO
.,BE72 A5 64    LDA $64                 LDA     FACMO
.,BE74 79 18 BF ADC $BF18,Y             ADC     FOUTBL+1+ADDPRC,Y
.,BE77 85 64    STA $64                 STA     FACMO
                                IFN     ADDPRC,<
.,BE79 A5 63    LDA $63                 LDA     FACMOH
.,BE7B 79 17 BF ADC $BF17,Y             ADC     FOUTBL+1,Y
.,BE7E 85 63    STA $63                 STA     FACMOH>
.,BE80 A5 62    LDA $62                 LDA     FACHO
.,BE82 79 16 BF ADC $BF16,Y             ADC     FOUTBL,Y
.,BE85 85 62    STA $62                 STA     FACHO
.,BE87 E8       INX                     INX                     ;IT WAS DONE YET ANOTHER TIME.
.,BE88 B0 04    BCS $BE8E               BCS     FOUT41
.,BE8A 10 DE    BPL $BE6A               BPL     FOUT2
.,BE8C 30 02    BMI $BE90               BMI     FOUT40
.,BE8E 30 DA    BMI $BE6A       FOUT41: BMI     FOUT2
.,BE90 8A       TXA             FOUT40: TXA
.,BE91 90 04    BCC $BE97               BCC     FOUTYP          ;CAN USE ACCA AS IS.
.,BE93 49 FF    EOR #$FF                EORI    377             ;FIND 11.-[A].
.,BE95 69 0A    ADC #$0A                ADCI    12              ;C IS STILL ON TO COMPLETE NEGATION.
                                                                ;AND WILL ALWAYS BE ON AFTER.
.,BE97 69 2F    ADC #$2F        FOUTYP: ADCI    "0"-1           ;GET A CHARACTER TO PRINT.
.,BE99 C8       INY                     REPEAT  3+ADDPRC,<INY>  ;BUMP POINTER UP.
.,BE9A C8       INY             
.,BE9B C8       INY             
.,BE9C C8       INY             
.,BE9D 84 47    STY $47                 STY     FDECPT
.,BE9F A4 71    LDY $71                 LDY     FBUFPT
.,BEA1 C8       INY                     INY                     ;POINT TO PLACE TO STORE OUTPUT.
.,BEA2 AA       TAX                     TAX
.,BEA3 29 7F    AND #$7F                ANDI    177             ;GET RID OF MSB.
.,BEA5 99 FF 00 STA $00FF,Y             STA     FBUFFR-1,Y
.,BEA8 C6 5D    DEC $5D                 DEC     DECCNT
.,BEAA D0 06    BNE $BEB2               BNE     STXBUF          ;NOT TIME FOR DP YET.
.,BEAC A9 2E    LDA #$2E                LDAI    "."
.,BEAE C8       INY                     INY
.,BEAF 99 FF 00 STA $00FF,Y             STA     FBUFFR-1,Y,     ;STORE DP.
.,BEB2 84 71    STY $71         STXBUF: STY     FBUFPT          ;STORE PNTR FOR LATER.
.,BEB4 A4 47    LDY $47                 LDY     FDECPT
.,BEB6 8A       TXA             FOUTCM: TXA                     ;COMPLEMENT ACCX
.,BEB7 49 FF    EOR #$FF                EORI    377             ;COMPLEMENT ACCA.
.,BEB9 29 80    AND #$80                ANDI    200             ;SAVE ONLY MSB.
.,BEBB AA       TAX                     TAX
.,BEBC C0 24    CPY #$24                CPYI    FDCEND-FOUTBL
                                IFN     TIME,<
.,BEBE F0 04    BEQ $BEC4               BEQ     FOULDY
.,BEC0 C0 3C    CPY #$3C                CPYI    TIMEND-FOUTBL>
.,BEC2 D0 A6    BNE $BE6A               BNE     FOUT2           ;CONTINUE WITH OUTPUT.
.,BEC4 A4 71    LDY $71         FOULDY: LDY     FBUFPT          ;GET BACK OUTPUT PNTR.
.,BEC6 B9 FF 00 LDA $00FF,Y     FOUT11: LDA     FBUFFR-1,Y,     ;REMOVE TRAILING ZEROES.
.,BEC9 88       DEY                     DEY
.,BECA C9 30    CMP #$30                CMPI    "0"
.,BECC F0 F8    BEQ $BEC6               BEQ     FOUT11
.,BECE C9 2E    CMP #$2E                CMPI    "."
.,BED0 F0 01    BEQ $BED3               BEQ     FOUT12          ;RUN INTO DP. STOP.
.,BED2 C8       INY                     INY                     ;SOMETHING ELSE. SAVE IT.
.,BED3 A9 2B    LDA #$2B        FOUT12: LDAI    "+"
.,BED5 A6 5E    LDX $5E                 LDX     TENEXP
.,BED7 F0 2E    BEQ $BF07               BEQ     FOUT17          ;NO EXPONENT TO OUTPUT.
.,BED9 10 08    BPL $BEE3               BPL     FOUT14
.,BEDB A9 00    LDA #$00                LDAI    0
.,BEDD 38       SEC                     SEC
.,BEDE E5 5E    SBC $5E                 SBC     TENEXP
.,BEE0 AA       TAX                     TAX
.,BEE1 A9 2D    LDA #$2D                LDAI    "-"             ;EXPONENT IS NEGATIVE.
.,BEE3 99 01 01 STA $0101,Y     FOUT14: STA     FBUFFR-1+2,Y,   ;STORE SIGN OF EXP
.,BEE6 A9 45    LDA #$45                LDAI    "E"
.,BEE8 99 00 01 STA $0100,Y             STA     FBUFFR-1+1,Y,   ;STORE THE "E" CHARACTER.
.,BEEB 8A       TXA                     TXA
.,BEEC A2 2F    LDX #$2F                LDXI    "0"-1
.,BEEE 38       SEC                     SEC
.,BEEF E8       INX             FOUT15: INX                     ;MOVE CLOSER TO OUTPUT VALUE.
.,BEF0 E9 0A    SBC #$0A                SBCI    12              ;SUBTRACT 10.
.,BEF2 B0 FB    BCS $BEEF               BCS     FOUT15          ;NOT NEGATIVE YET.
.,BEF4 69 3A    ADC #$3A                ADCI    "0"+12          ;GET SECOND OUTPUT CHARACTER.
.,BEF6 99 03 01 STA $0103,Y             STA     FBUFFR-1+4,Y,   ;STORE HIGH DIGIT.
.,BEF9 8A       TXA                     TXA
.,BEFA 99 02 01 STA $0102,Y             STA     FBUFFR-1+3,Y,   ;STORE  LOW DIGIT.
.,BEFD A9 00    LDA #$00                LDAI    0               ;PUT IN TERMINATOR.
.,BEFF 99 04 01 STA $0104,Y             STA     FBUFFR-1+5,Y,
.,BF02 F0 08    BEQ $BF0C               BEQA    FOUT20          ;RETURN. (ALWAYS BRANCHES).
.,BF04 99 FF 00 STA $00FF,Y     FOUT19: STA     FBUFFR-1,Y,     ;STORE THE CHARACTER.
.,BF07 A9 00    LDA #$00        FOUT17: LDAI    0               ;A TERMINATOR.
.,BF09 99 00 01 STA $0100,Y             STA     FBUFFR-1+1,Y
.,BF0C A9 00    LDA #$00        FOUT20: LDWDI   FBUFFR
.,BF0E A0 01    LDY #$01        
.,BF10 60       RTS             FPWRRT: RTS                     ;ALL DONE.
.:BF11 80 00 00 00 00           FHALF:  200     ;1/2
                                        000
                                ZERO:   000
                                        000
                                IFN     ADDPRC,<0>
                                
                                ;POWER OF TEN TABLE
                                IFE     ADDPRC,<
                                FOUTBL: 376     ;-100000
                                        171
                                        140
                                        000     ;10000
                                        047
                                        020
                                        377     ;-1000
                                        374
                                        030
                                        000     ;100
                                        000
                                        144
                                        377     ;-10
                                        377
                                        366
                                        000     ;1
                                        000
                                        001>
                                
                                IFN     ADDPRC,<
.:BF16 FA 0A 1F 00              FOUTBL: 372     ;-100,000,000
                                        012
                                        037
                                        000
.:BF1A 00 98 96 80                      000     ;10,000,000
                                        230
                                        226
                                        200
.:BF1E FF F0 BD C0                      377     ;-1,000,000
                                        360
                                        275
                                        300
.:BF22 00 01 86 A0                      000     ;100,000
                                        001
                                        206
                                        240
.:BF26 FF FF D8 F0                      377     ;-10,000
                                        377
                                        330
                                        360
.:BF2A 00 00 03 E8                      000     ;1000
                                        000
                                        003
                                        350
.:BF2E FF FF FF 9C                      377     ;-100
                                        377
                                        377
                                        234
.:BF32 00 00 00 0A                      000     ;10
                                        000
                                        000
                                        012
.:BF36 FF FF FF FF                      377     ;-1
                                        377
                                        377
                                        377>
                                FDCEND:
                                IFN     TIME,<
.:BF3A FF DF 0A 80                      377     ; -2160000 FOR TIME CONVERTER.
                                        337
                                        012
                                        200
.:BF3E 00 03 4B C0                      000     ; 216000
                                        003
                                        113
                                        300
.:BF42 FF FF 73 60                      377     ; -36000
                                        377
                                        163
                                        140
.:BF46 00 00 0E 10                      000     ; 3600
                                        000
                                        016
                                        020
.:BF4A FF FF FD A8                      377     ; -600
                                        377
                                        375
                                        250
.:BF4E 00 00 00 3C                      000     ; 60
                                        000
                                        000
                                        074
                                TIMEND:>
.:BF52 EC                       
.:BF53 AA AA AA AA AA           
.:BF58 AA AA AA AA AA AA AA AA  
.:BF60 AA AA AA AA AA AA AA AA  
.:BF68 AA AA AA AA AA AA AA AA  
.:BF70 AA                       
                                PAGE
                                SUBTTL  EXPONENTIATION AND SQUARE ROOT FUNCTION.
                                        ;SQUARE ROOT FUNCTION --- SQR(A)
                                        ;USE SQR(X)=X^.5
.,BF71 20 0C BC JSR $BC0C       SQR:    JSR     MOVAF           ;MOVE FAC INTO ARG.
.,BF74 A9 11    LDA #$11                LDWDI   FHALF
.,BF76 A0 BF    LDY #$BF        
.,BF78 20 A2 BB JSR $BBA2               JSR     MOVFM           ;PUT MEMORY INTO FAC.
                                                                ;LAST THING FETCHED IS FACEXP. INTO ACCX.
                                ;       JMP     FPWRT           ;FALL INTO FPWRT.
                                
                                        ;EXPONENTIATION ---  X^Y.
                                        ;N.B.  0^0=1
                                        ;FIRST CHECK IF Y=0. IF SO, THE RESULT IS 1.
                                        ;NEXT CHECK IF X=0. IF SO THE RESULT IS 0.
                                        ;THEN CHECK IF X.GT.0. IF NOT CHECK THAT Y IS AN INTEGER.
                                        ;IF SO, NEGATE X, SO THAT LOG DOESN'T GIVE FCERR.
                                        ;IF X IS NEGATIVE AND Y IS ODD, NEGATE THE RESULT
                                        ;RETURNED BY EXP.
                                        ;TO COMPUTE THE RESULT USE X^Y=EXP((Y*LOG(X)).
.,BF7B F0 70    BEQ $BFED       FPWRT:  BEQ     EXP             ;IF FAC=0, JUST EXPONENTIATE THAT.
.,BF7D A5 69    LDA $69                 LDA     ARGEXP          ;IS X=0?
.,BF7F D0 03    BNE $BF84               BNE     FPWRT1
.,BF81 4C F9 B8 JMP $B8F9               JMP     ZEROF1          ;ZERO FAC.
.,BF84 A2 4E    LDX #$4E        FPWRT1: LDXYI   TEMPF3          ;SAVE FOR LATER IN A TEMP.
.,BF86 A0 00    LDY #$00        
.,BF88 20 D4 BB JSR $BBD4               JSR     MOVMF
                                        ;Y=0 ALREADY. GOOD IN CASE NO ONE CALLS INT.
.,BF8B A5 6E    LDA $6E                 LDA     ARGSGN
.,BF8D 10 0F    BPL $BF9E               BPL     FPWR1           ;NO PROBLEMS IF X.GT.0.
.,BF8F 20 CC BC JSR $BCCC               JSR     INT             ;INTEGERIZE THE FAC.
.,BF92 A9 4E    LDA #$4E                LDWDI   TEMPF3          ;GET ADDR OF COMPERAND.
.,BF94 A0 00    LDY #$00        
.,BF96 20 5B BC JSR $BC5B               JSR     FCOMP           ;EQUAL?
.,BF99 D0 03    BNE $BF9E               BNE     FPWR1           ;LEAVE X NEG. LOG WILL BLOW HIM OUT.
                                                                ;A=-1 AND Y IS IRRELEVANT.
.,BF9B 98       TYA                     TYA                     ;NEGATE X. MAKE POSITIVE.
.,BF9C A4 07    LDY $07                 LDY     INTEGR          ;GET EVENNESS.
.,BF9E 20 FE BB JSR $BBFE       FPWR1:  JSR     MOVFA1          ;ALTERNATE ENTRY POINT.
.,BFA1 98       TYA                     TYA
.,BFA2 48       PHA                     PHA                     ;SAVE EVENNESS FOR LATER.
.,BFA3 20 EA B9 JSR $B9EA               JSR     LOG             ;FIND LOG.
.,BFA6 A9 4E    LDA #$4E                LDWDI   TEMPF3          ;MULTIPLY FAC TIMES LOG(X).
.,BFA8 A0 00    LDY #$00        
.,BFAA 20 28 BA JSR $BA28               JSR     FMULT
.,BFAD 20 ED BF JSR $BFED               JSR     EXP             ;EXPONENTIATE THE FAC.
.,BFB0 68       PLA                     PLA
.,BFB1 4A       LSR                     LSR     A,              ;IS IT EVEN?
.,BFB2 90 0A    BCC $BFBE               BCC     NEGRTS          ;YES. OR X.GT.0.
                                        ;NEGATE THE NUMBER IN FAC.
.,BFB4 A5 61    LDA $61         NEGOP:  LDA     FACEXP
.,BFB6 F0 06    BEQ $BFBE               BEQ     NEGRTS
.,BFB8 A5 66    LDA $66                 COM     FACSGN
.,BFBA 49 FF    EOR #$FF        
.,BFBC 85 66    STA $66         
.,BFBE 60       RTS             NEGRTS: RTS
                                
                                PAGE
                                SUBTTL  EXPONENTIATION FUNCTION.
                                        ;FIRST SAVE THE ORIGINAL ARGUMENT AND MULTIPLY THE FAC BY
                                        ;LOG2(E). THE RESULT IS USED TO DETERMINE IF OVERFLOW
                                        ;WILL OCCUR SINCE EXP(X)=2^(X*LOG2(E)) WHERE
                                        ;LOG2(E)=LOG(E) BASE 2. THEN SAVE THE INTEGER PART OF
                                        ;THIS TO SCALE THE ANSWER AT THE END. SINCE
                                        ;2^Y=2^INT(Y)*2^(Y-INT(Y)) AND 2^INT(Y) IS EASY TO COMPUTE.
                                        ;NOW COMPUTE 2^(X*LOG2(E)-INT(X*LOG2(E)) BY
                                        ;P(LN(2)*(INT(X*LOG2(E))+1)-X) WHERE P IS AN APPROXIMATION
                                        ;POLYNOMIAL. THE RESULT IS THEN SCALED BY THE POWER OF 2
                                        ;PREVIOUSLY SAVED.
                                
.:BFBF 81 38 AA 3B 29           LOGEB2: 201                     ;LOG(E) BASE 2.
                                        070
                                        252
                                        073
                                IFN     ADDPRC,<051>
                                
                                ife     addprc,<
                                expcon: 6       ; degree -1.
                                        164     ; .00021702255
                                        143
                                        220
                                        214
                                        167     ; .0012439688
                                        043
                                        014
                                        253
                                        172     ; .0096788410
                                        036
                                        224
                                        000
                                        174     ; .055483342
                                        143
                                        102
                                        200
                                        176     ; .24022984
                                        165
                                        376
                                        320
                                        200     ; .69314698
                                        061
                                        162
                                        025
                                        201     ; 1.0
                                        000
                                        000
                                        000>
                                
                                
                                IFN     ADDPRC,<
.:BFC4 07                       EXPCON: 7       ;DEGREE-1
.:BFC5 71 34 58 3E 56                   161     ; .000021498763697
                                        064
                                        130
                                        076
                                        126
.:BFCA 74 16 7E B3 1B                   164     ; .00014352314036
                                        026
                                        176
                                        263
                                        033
.:BFCF 77 2F EE E3 85                   167     ; .0013422634824
                                        057
                                        356
                                        343
                                        205
.:BFD4 7A 1D 84 1C 2A                   172     ; .0096140170119
                                        035
                                        204
                                        034
                                        052
.:BFD9 7C 63 59 58 0A                   174     ; .055505126860
                                        143
                                        131
                                        130
                                        012
.:BFDE 7E 75 FD E7 C6                   176     ; .24022638462
                                        165
                                        375
                                        347
                                        306
.:BFE3 80 31 72 18 10                   200     ; .69314718608
                                        061
                                        162
                                        030
                                        020
.:BFE8 81 00 00 00 00                   201     ; 1.0
                                        000
                                        000
                                        000
                                        000>
                                
                                EXP:
.,BFED A9 BF    LDA #$BF                LDWDI   LOGEB2          ;MULTIPLY BY LOG(E) BASE 2.
.,BFEF A0 BF    LDY #$BF        
.,BFF1 20 28 BA JSR $BA28               JSR     FMULT
.,BFF4 A5 70    LDA $70                 LDA     FACOV
.,BFF6 69 50    ADC #$50                ADCI    120
.,BFF8 90 03    BCC $BFFD               BCC     STOLD
.,BFFA 20 23 BC JSR $BC23               JSR     INCRND
.,BFFD 4C 00 E0 JMP $E000       
.,E000 85 56    STA $56         STOLD:  STA     OLDOV
.,E002 20 0F BC JSR $BC0F               JSR     MOVEF           ;TO SAVE IN ARG WITHOUT ROUND.
.,E005 A5 61    LDA $61                 LDA     FACEXP
.,E007 C9 88    CMP #$88                CMPI    210             ;IF ABS(FAC) .GE. 128, TOO BIG.
.,E009 90 03    BCC $E00E               BCC     EXP1
.,E00B 20 D4 BA JSR $BAD4       GOMLDV: JSR     MLDVEX          ;OVERFLOW OR OVERFLOW.
.,E00E 20 CC BC JSR $BCCC       EXP1:   JSR     INT
.,E011 A5 07    LDA $07                 LDA     INTEGR  ;GET LOW PART.
.,E013 18       CLC                     CLC
.,E014 69 81    ADC #$81                ADCI    201
.,E016 F0 F3    BEQ $E00B               BEQ     GOMLDV          ;OVERFLOW OR OVERFLOW !!
.,E018 38       SEC                     SEC
.,E019 E9 01    SBC #$01                SBCI    1               ;SUBTRACT 1.
.,E01B 48       PHA                     PHA                     ;SAVE A WHILE.
.,E01C A2 05    LDX #$05                LDXI    4+ADDPRC        ;PREP TO SWAP FAC AND ARG.
.,E01E B5 69    LDA $69,X       SWAPLP: LDA     ARGEXP,X
.,E020 B4 61    LDY $61,X               LDY     FACEXP,X
.,E022 95 61    STA $61,X               STA     FACEXP,X
.,E024 94 69    STY $69,X               STY     ARGEXP,X
.,E026 CA       DEX                     DEX
.,E027 10 F5    BPL $E01E               BPL     SWAPLP
.,E029 A5 56    LDA $56                 LDA     OLDOV
.,E02B 85 70    STA $70                 STA     FACOV
.,E02D 20 53 B8 JSR $B853               JSR     FSUBT
.,E030 20 B4 BF JSR $BFB4               JSR     NEGOP           ;NEGATE FAC.
.,E033 A9 C4    LDA #$C4                LDWDI   EXPCON
.,E035 A0 BF    LDY #$BF        
.,E037 20 59 E0 JSR $E059               JSR     POLY
.,E03A A9 00    LDA #$00                CLR     ARISGN          ;MULTIPLY BY POSITIVE 1.0.
.,E03C 85 6F    STA $6F         
.,E03E 68       PLA                     PLA                     ;GET SCALE FACTOR.
.,E03F 20 B9 BA JSR $BAB9               JSR     MLDEXP          ;MODIFY FACEXP AND CHECK FOR OVERFLOW.
.,E042 60       RTS                     RTS                     ;HAS TO DO JSR DUE TO PULAS IN MULDIV.
                                
                                
                                PAGE
                                SUBTTL  POLYNOMIAL EVALUATOR AND THE RANDOM NUMBER GENERATOR.
                                        ;EVALUATE P(X^2)*X
                                        ;POINTER TO DEGREE IS IN [Y,A].
                                        ;THE CONSTANTS FOLLOW THE DEGREE.
                                        ;FOR X=FAC, COMPUTE:
                                        ; C0*X+C1*X^3+C2*X^5+C3*X^7+...+C(N)*X^(2*N+1)
.,E043 85 71    STA $71         POLYX:  STWD    POLYPT          ;RETAIN POLYNOMIAL POINTER FOR LATER.
.,E045 84 72    STY $72         
.,E047 20 CA BB JSR $BBCA               JSR     MOV1F           ;SAVE FAC IN FACTMP.
.,E04A A9 57    LDA #$57                LDAI    TEMPF1
.,E04C 20 28 BA JSR $BA28               JSR     FMULT           ;COMPUTE X^2.
.,E04F 20 5D E0 JSR $E05D               JSR     POLY1           ;COMPUTE P(X^2).
.,E052 A9 57    LDA #$57                LDWDI   TEMPF1
.,E054 A0 00    LDY #$00        
.,E056 4C 28 BA JMP $BA28               JMP     FMULT           ;MULTIPLY BY FAC AGAIN.
                                
                                        ;POLYNOMIAL EVALUATOR.
                                        ;POINTER TO DEGREE IS IN [Y,A].
                                        ;COMPUTE:
                                        ; C0+C1*X+C2*X^2+C3*X^3+C4*X^4+...+C(N-1)*X^(N-1)+C(N)*X^N.
.,E059 85 71    STA $71         POLY:   STWD    POLYPT
.,E05B 84 72    STY $72         
.,E05D 20 C7 BB JSR $BBC7       POLY1:  JSR     MOV2F           ;SAVE FAC.
.,E060 B1 71    LDA ($71),Y             LDADY   POLYPT
.,E062 85 67    STA $67                 STA     DEGREE
.,E064 A4 71    LDY $71                 LDY     POLYPT
.,E066 C8       INY                     INY
.,E067 98       TYA                     TYA
.,E068 D0 02    BNE $E06C               BNE     POLY3
.,E06A E6 72    INC $72                 INC     POLYPT+1
.,E06C 85 71    STA $71         POLY3:  STA     POLYPT
.,E06E A4 72    LDY $72                 LDY     POLYPT+1
.,E070 20 28 BA JSR $BA28       POLY2:  JSR     FMULT
.,E073 A5 71    LDA $71                 LDWD    POLYPT          ;GET CURRENT POINTER.
.,E075 A4 72    LDY $72         
.,E077 18       CLC                     CLC
.,E078 69 05    ADC #$05                ADCI    4+ADDPRC
.,E07A 90 01    BCC $E07D               BCC     POLY4
.,E07C C8       INY                     INY
.,E07D 85 71    STA $71         POLY4:  STWD    POLYPT
.,E07F 84 72    STY $72         
.,E081 20 67 B8 JSR $B867               JSR     FADD            ;ADD IN CONSTANT.
.,E084 A9 5C    LDA #$5C                LDWDI   TEMPF2          ;MULTIPLY THE ORIGINAL FAC.
.,E086 A0 00    LDY #$00        
.,E088 C6 67    DEC $67                 DEC     DEGREE          ;DONE?
.,E08A D0 E4    BNE $E070               BNE     POLY2
.,E08C 60       RTS             RANDRT: RTS                     ;YES.
                                
                                        ;PSUEDO-RANDOM NUMBER GENERATOR.
                                        ;IF ARG=0, THE LAST RANDOM NUMBER GENERATED IS RETURNED.
                                        ;IF ARG .LT. 0, A NEW SEQUENCE OF RANDOM NUMBERS IS
                                        ;STARTED USING THE ARGUMENT.
                                        ;   TO FORM THE NEXT RANDOM NUMBER IN THE SEQUENCE,
                                        ;MULTIPLY THE PREVIOUS RANDOM NUMBER BY A RANDOM CONSTANT
                                        ;AND ADD IN ANOTHER RANDOM CONSTANT. THE THEN HO
                                        ;AND LO BYTES ARE SWITCHED, THE EXPONENT IS PUT WHERE
                                        ;IT WILL BE SHIFTED IN BY NORMAL, AND THE EXPONENT IN THE FAC
                                        ;IS SET TO 200 SO THE RESULT WILL BE LESS THAN 1. THIS
                                        ;IS THEN NORMALIZED AND SAVED FOR THE NEXT TIME.
                                        ;THE HO AND LOW BYTES WERE SWITCHED SO THERE WILL BE A
                                        ;RANDOM CHANCE OF GETTING A NUMBER LESS THAN OR GREATER
                                        ;THAN .5 .
                                
.:E08D 98 35 44 7A 00           RMULZC: 230
                                        065
                                        104
                                        172
.:E092 68 28 B1 46 00           RADDZC: 150
                                        050
                                        261
                                        106
                                
.,E097 20 2B BC JSR $BC2B       RND:    JSR     SIGN            ;GET SIGN INTO ACCX.
                                IFN     REALIO-3,<
                                        TAX>                    ;GET INTO ACCX, SINCE "MOVFM" USES ACCX.
.,E09A 30 37    BMI $E0D3               BMI     RND1            ;START NEW SEQUENCE IF NEGATIVE.
                                IFE     REALIO-3,<
.,E09C D0 20    BNE $E0BE               BNE     QSETNR
                                                ;TIMERS ARE AT 9044(L0),45(HI),48(LO),49(HI) HEX.
                                                ;FIRST TWO ARE ALWAYS FREE RUNNING.
                                                ;SECOND PAIR IS NOT. LO IS FREER THAN HI THEN.
                                                ;SO ORDER IN FAC IS 44,48,45,49.
.,E09E 20 F3 FF JSR $FFF3               LDA     CQHTIM
.,E0A1 86 22    STX $22                 STA     FACHO
.,E0A3 84 23    STY $23                 LDA     CQHTIM+4
.,E0A5 A0 04    LDY #$04                STA     FACMOH
.,E0A7 B1 22    LDA ($22),Y             LDA     CQHTIM+1
.,E0A9 85 62    STA $62                 STA     FACMO
.,E0AB C8       INY                     LDA     CQHTIM+5
.,E0AC B1 22    LDA ($22),Y             STA     FACLO
.,E0AE 85 64    STA $64                 JMP     STRNEX>
.,E0B0 A0 08    LDY #$08        QSETNR: LDWDI   RNDX            ;GET LAST ONE INTO FAC.
.,E0B2 B1 22    LDA ($22),Y             JSR     MOVFM
.,E0B4 85 63    STA $63         IFN     REALIO-3,<
.,E0B6 C8       INY                     TXA                     ;FAC WAS ZERO?
.,E0B7 B1 22    LDA ($22),Y             BEQ     RANDRT>         ;RESTORE LAST ONE.
.,E0B9 85 65    STA $65         
.,E0BB 4C E3 E0 JMP $E0E3       
.,E0BE A9 8B    LDA #$8B        
.,E0C0 A0 00    LDY #$00        
.,E0C2 20 A2 BB JSR $BBA2       
.,E0C5 A9 8D    LDA #$8D                LDWDI   RMULZC          ;MULTIPLY BY RANDOM CONSTANT.
.,E0C7 A0 E0    LDY #$E0        
.,E0C9 20 28 BA JSR $BA28               JSR     FMULT
.,E0CC A9 92    LDA #$92                LDWDI   RADDZC
.,E0CE A0 E0    LDY #$E0        
.,E0D0 20 67 B8 JSR $B867               JSR     FADD            ;ADD RANDOM CONSTANT.
.,E0D3 A6 65    LDX $65         RND1:   LDX     FACLO
.,E0D5 A5 62    LDA $62                 LDA     FACHO
.,E0D7 85 65    STA $65                 STA     FACLO
.,E0D9 86 62    STX $62                 STX     FACHO           ;REVERSE HO AND LO.
                                IFE     REALIO-3,<
.,E0DB A6 63    LDX $63                 LDX     FACMOH
.,E0DD A5 64    LDA $64                 LDA     FACMO
.,E0DF 85 63    STA $63                 STA     FACMOH
.,E0E1 86 64    STX $64                 STX     FACMO>
.,E0E3 A9 00    LDA #$00        STRNEX: CLR     FACSGN          ;MAKE NUMBER POSITIVE.
.,E0E5 85 66    STA $66         
.,E0E7 A5 61    LDA $61                 LDA     FACEXP          ;PUT EXP WHERE IT WILL
.,E0E9 85 70    STA $70                 STA     FACOV           ;BE SHIFTED IN BY NORMAL.
.,E0EB A9 80    LDA #$80                LDAI    200
.,E0ED 85 61    STA $61                 STA     FACEXP          ;MAKE RESULT BETWEEN 0 AND 1.
.,E0EF 20 D7 B8 JSR $B8D7               JSR     NORMAL          ;NORMALIZE.
.,E0F2 A2 8B    LDX #$8B                LDXYI   RNDX
.,E0F4 A0 00    LDY #$00        
.,E0F6 4C D4 BB JMP $BBD4       GMOVMF: JMP     MOVMF           ;PUT NEW ONE INTO MEMORY.
                                
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
                                
                                PAGE
                                SUBTTL  SINE, COSINE AND TANGENT FUNCTIONS.
                                IFE     KIMROM,<
                                        ;COSINE FUNCTION.
                                        ;USE COS(X)=SIN(X+PI/2)
.,E264 A9 E0    LDA #$E0        COS:    LDWDI   PI2             ;PNTR TO PI/2.
.,E266 A0 E2    LDY #$E2        
.,E268 20 67 B8 JSR $B867               JSR     FADD            ;ADD IT IN.
                                                                ;FALL INTO SIN.
                                
                                
                                        ;SINE FUNCTION.
                                        ;USE IDENTITIES TO GET FAC IN QUADRANTS I OR IV.
                                        ;THE FAC IS DIVIDED BY 2*PI AND THE INTEGER PART IS IGNORED
                                        ;BECAUSE SIN(X+2*PI)=SIN(X). THEN THE ARGUMENT CAN BE COMPARED
                                        ;WITH PI/2 BY COMPARING THE RESULT OF THE DIVISION
                                        ;WITH PI/2/(2*PI)=1/4.
                                        ;IDENTITIES ARE THEN USED TO GET THE RESULT IN QUADRANTS
                                        ;I OR IV. AN APPROXIMATION POLYNOMIAL IS THEN USED TO
                                        ;COMPUTE SIN(X).
.,E26B 20 0C BC JSR $BC0C       SIN:    JSR     MOVAF
.,E26E A9 E5    LDA #$E5                LDWDI   TWOPI           ;GET PNTR TO DIVISOR.
.,E270 A0 E2    LDY #$E2        
.,E272 A6 6E    LDX $6E                 LDX     ARGSGN          ;GET SIGN OF RESULT.
.,E274 20 07 BB JSR $BB07               JSR     FDIVF
.,E277 20 0C BC JSR $BC0C               JSR     MOVAF           ;GET RESULT INTO ARG.
.,E27A 20 CC BC JSR $BCCC               JSR     INT             ;INTEGERIZE FAC.
.,E27D A9 00    LDA #$00                CLR     ARISGN          ;ALWAYS HAVE THE SAME SIGN.
.,E27F 85 6F    STA $6F         
.,E281 20 53 B8 JSR $B853               JSR     FSUBT           ;KEEP ONLY THE FRACTIONAL PART.
.,E284 A9 EA    LDA #$EA                LDWDI   FR4             ;GET PNTR TO 1/4.
.,E286 A0 E2    LDY #$E2        
.,E288 20 50 B8 JSR $B850               JSR     FSUB            ;COMPUTE 1/4-FAC.
.,E28B A5 66    LDA $66                 LDA     FACSGN          ;SAVE SIGN FOR LATER.
.,E28D 48       PHA                     PHA
.,E28E 10 0D    BPL $E29D               BPL     SIN1            ;FIRST QUADRANT.
.,E290 20 49 B8 JSR $B849               JSR     FADDH           ;ADD 1/2 TO FAC.
.,E293 A5 66    LDA $66                 LDA     FACSGN          ;SIGN IS NEGATIVE?
.,E295 30 09    BMI $E2A0               BMI     SIN2
.,E297 A5 12    LDA $12                 COM     TANSGN          ;QUADRANTS II AND III COME HERE.
.,E299 49 FF    EOR #$FF        
.,E29B 85 12    STA $12         
.,E29D 20 B4 BF JSR $BFB4       SIN1:   JSR     NEGOP           ;IF POSITIVE, NEGATE IT.
.,E2A0 A9 EA    LDA #$EA        SIN2:   LDWDI   FR4             ;POINTER TO 1/4.
.,E2A2 A0 E2    LDY #$E2        
.,E2A4 20 67 B8 JSR $B867               JSR     FADD            ;ADD IT IN.
.,E2A7 68       PLA                     PLA                     ;GET ORIGINAL QUADRANT.
.,E2A8 10 03    BPL $E2AD               BPL     SIN3
.,E2AA 20 B4 BF JSR $BFB4               JSR     NEGOP           ;IF NEGATIVE, NEGATE RESULT.
.,E2AD A9 EF    LDA #$EF        SIN3:   LDWDI   SINCON
.,E2AF A0 E2    LDY #$E2        
.,E2B1 4C 43 E0 JMP $E043       GPOLYX: JMP     POLYX           ;DO APPROXIMATION POLYNOMIAL.
                                
                                
                                        ;TANGENT FUNCTION.
.,E2B4 20 CA BB JSR $BBCA       TAN:    JSR     MOV1F           ;MOVE FAC INTO TEMPORARY.
.,E2B7 A9 00    LDA #$00                CLR     TANSGN          ;REMEMBER WHETHER TO NEGATE.
.,E2B9 85 12    STA $12         
.,E2BB 20 6B E2 JSR $E26B               JSR     SIN             ;COMPUTE THE SIN.
.,E2BE A2 4E    LDX #$4E                LDXYI   TEMPF3
.,E2C0 A0 00    LDY #$00        
.,E2C2 20 F6 E0 JSR $E0F6               JSR     GMOVMF          ;PUT SIGN INTO OTHER TEMP.
.,E2C5 A9 57    LDA #$57                LDWDI   TEMPF1
.,E2C7 A0 00    LDY #$00        
.,E2C9 20 A2 BB JSR $BBA2               JSR     MOVFM           ;PUT THIS MEMORY LOC INTO FAC.
.,E2CC A9 00    LDA #$00                CLR     FACSGN          ;START OFF POSITIVE.
.,E2CE 85 66    STA $66         
.,E2D0 A5 12    LDA $12                 LDA     TANSGN
.,E2D2 20 DC E2 JSR $E2DC               JSR     COSC            ;COMPUTE COSINE.
.,E2D5 A9 4E    LDA #$4E                LDWDI   TEMPF3          ;ADDRESS OF SINE VALUE.
.,E2D7 A0 00    LDY #$00        
.,E2D9 4C 0F BB JMP $BB0F       GFDIV:  JMP     FDIV            ;DIVIDE SINE BY COSINE AND RETURN.
.,E2DC 48       PHA             COSC:   PHA
.,E2DD 4C 9D E2 JMP $E29D               JMP     SIN1
                                
.:E2E0 81 49 0F DA A2           PI2:    201     ;PI/2
                                        111
                                        017
                                        333-ADDPRC
                                IFN     ADDPRC,<242>
.:E2E5 83 49 0F DA A2           TWOPI:  203     ;2*PI.
                                        111
                                        017
                                        333-ADDPRC
                                IFN     ADDPRC,<242>
.:E2EA 7F 00 00 00 00           FR4:    177     ;1/4
                                        000
                                        000
                                        0000
                                IFN     ADDPRC,<0>
                                IFE ADDPRC,<SINCON:     4       ;DEGREE-1.
                                        206     ;39.710899
                                        036
                                        327
                                        373
                                        207     ;-76.574956
                                        231
                                        046
                                        145
                                        207     ;81.602231
                                        043
                                        064
                                        130
                                        206     ;-41.341677
                                        245
                                        135
                                        341
                                        203     ;6.2831853
                                        111
                                        017
                                        333>
                                
                                IFN     ADDPRC,<
.:E2EF 05                       SINCON: 5               ;DEGREE-1.
.:E2F0 84 E6 1A 2D 1B                   204     ; -14.381383816
                                        346
                                        032
                                        055
                                        033
.:E2F5 86 28 07 FB F8                   206     ; 42.07777095
                                        050
                                        007
                                        373
                                        370
.:E2FA 87 99 68 89 01                   207     ; -76.704133676
                                        231
                                        150
                                        211
                                        001
.:E2FF 87 23 35 DF E1                   207     ; 81.605223690
                                        043
                                        065
                                        337
                                        341
.:E304 86 A5 5D E7 28                   206     ; -41.34170209
                                        245
                                        135
                                        347
                                        050
.:E309 83 49 0F DA A2                   203     ; 6.2831853070
                                        111
                                        017
                                        332
                                        242
                                        241     ; 7.2362932E7
                                        124
                                        106
                                        217
                                        23
                                        217     ; 73276.2515
                                        122
                                        103
                                        211
                                        315>
                                PAGE
                                SUBTTL  ARCTANGENT FUNCTION.
                                        ;USE IDENTITIES TO GET ARG BETWEEN 0 AND 1 AND THEN USE AN
                                        ;APPROXIMATION POLYNOMIAL TO COMPUTE ARCTAN(X).
.,E30E A5 66    LDA $66         ATN:    LDA     FACSGN          ;WHAT IS SIGN?
.,E310 48       PHA                     PHA                     ;(MEANWHILE SAVE FOR LATER.)
.,E311 10 03    BPL $E316               BPL     ATN1
.,E313 20 B4 BF JSR $BFB4               JSR     NEGOP           ;IF NEGATIVE, NEGATE FAC.
                                                                ;USE ARCTAN(X)=-ARCTAN(-X) .
.,E316 A5 61    LDA $61         ATN1:   LDA     FACEXP
.,E318 48       PHA                     PHA                     ;SAVE THIS TOO FOR LATER.
.,E319 C9 81    CMP #$81                CMPI    201             ;SEE IF FAC .GE. 1.0 .
.,E31B 90 07    BCC $E324               BCC     ATN2            ;IT IS LESS THAN 1.
.,E31D A9 BC    LDA #$BC                LDWDI   FONE            ;GET PNTR TO 1.0 .
.,E31F A0 B9    LDY #$B9        
.,E321 20 0F BB JSR $BB0F               JSR     FDIV            ;COMPUTE RECIPROCAL.
                                                                ;USE ARCTAN(X)=PI/2-ARCTAN(1/X) .
.,E324 A9 3E    LDA #$3E        ATN2:   LDWDI   ATNCON          ;PNTR TO ARCTAN CONSTANTS.
.,E326 A0 E3    LDY #$E3        
.,E328 20 43 E0 JSR $E043               JSR     POLYX
.,E32B 68       PLA                     PLA
.,E32C C9 81    CMP #$81                CMPI    201             ;WAS ORIGINAL ARGUMENT .LT. 1 ?
.,E32E 90 07    BCC $E337               BCC     ATN3            ;YES.
.,E330 A9 E0    LDA #$E0                LDWDI   PI2
.,E332 A0 E2    LDY #$E2        
.,E334 20 50 B8 JSR $B850               JSR     FSUB            ;SUBTRACT ARCTAGN FROM PI/2.
.,E337 68       PLA             ATN3:   PLA                     ;WAS ORIGINAL ARGUMENT POSITIVE?
.,E338 10 03    BPL $E33D               BPL     ATN4            ;YES.
.,E33A 4C B4 BF JMP $BFB4               JMP     NEGOP           ;IF NEGATIVE, NEGATE RESULT.
.,E33D 60       RTS             ATN4:   RTS                     ;ALL DONE.
                                
                                IFE     ADDPRC,<
                                ATNCON:  10     ;DEGREE-1.
                                        170     ;.0028498896
                                        072
                                        305
                                        067
                                        173     ;-.016068629
                                        203
                                        242
                                        134
                                        174     ;.042691519
                                        056
                                        335
                                        115
                                        175     ;-.075042945
                                        231
                                        260
                                        036
                                        175     ;.10640934
                                        131
                                        355
                                        044
                                        176     ;-.14203644
                                        221
                                        162
                                        000
                                        176     ;.19992619
                                        114
                                        271
                                        163
                                        177     ;.-33333073
                                        252
                                        252
                                        123
                                        201     ;1.0
                                        000
                                        000
                                        000>
                                
                                IFN     ADDPRC,<
.:E33E 0B                       ATNCON: 13      ;DEGREE-1.
.:E33F 76 B3 83 BD D3                   166     ; -.0006847939119
                                        263
                                        203
                                        275
                                        323
.:E344 79 1E F4 A6 F5                   171     ; .004850942156
                                        036
                                        364
                                        246
                                        365
.:E349 7B 83 FC B0 10                   173     ; -.01611170184
                                        203
                                        374
                                        260
                                        020
.:E34E 7C 0C 1F 67 CA                   174     ; .03420963805
                                        014
                                        037
                                        147
                                        312
.:E353 7C DE 53 CB C1                   174     ; -.05427913276
                                        336
                                        123
                                        313
                                        301
.:E358 7D 14 64 70 4C                   175     ; .07245719654
                                        024
                                        144
                                        160
                                        114
.:E35D 7D B7 EA 51 7A                   175     ; -.08980239538
                                        267
                                        352
                                        121
                                        172
.:E362 7D 63 30 88 7E                   175     ; .1109324134
                                        143
                                        060
                                        210
                                        176
.:E367 7E 92 44 99 3A                   176     ; -.1428398077
                                        222
                                        104
                                        231
                                        072
.:E36C 7E 4C CC 91 C7                   176     ; .1999991205
                                        114
                                        314
                                        221
                                        307
.:E371 7F AA AA AA 13                   177     ; -.3333333157
                                        252
                                        252
                                        252
                                        023
.:E376 81 00 00 00 00                   201     ; 1.0
                                        000
                                        000
                                        000
                                        000>>
                                
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
                                
                                PAGE
                                SUBTTL  SYSTEM INITIALIZATION CODE.
                                RADIX   10              ;IN ALL NON-MATH-PACKAGE CODE.
                                ; THIS INITIALIZES THE BASIC INTERPRETER FOR THE M6502 AND SHOULD BE
                                ; LOCATED WHERE IT WILL BE WIPED OUT IN RAM IF CODE IS ALL IN RAM.
                                
                                IFE     ROMSW,<
                                        BLOCK   1>              ;SO ZEROING AT TXTTAB DOESN'T PREVENT
                                                                ;RESTARTING INIT
.,E3A2 E6 7A    INC $7A         INITAT: INC     CHRGET+7        ;INCREMENT THE WHOLE TXTPTR.
.,E3A4 D0 02    BNE $E3A8               BNE     CHZGOT
.,E3A6 E6 7B    INC $7B                 INC     CHRGET+8
.,E3A8 AD 60 EA LDA $EA60       CHZGOT: LDA     60000           ;A LOAD WITH AN EXT ADDR.
.,E3AB C9 3A    CMP #$3A                CMPI    ":"             ;IS IT A ":"?
.,E3AD B0 0A    BCS $E3B9               BCS     CHZRTS          ;IT IS .GE. ":"
.,E3AF C9 20    CMP #$20                CMPI    " "             ;SKIP SPACES.
.,E3B1 F0 EF    BEQ $E3A2               BEQ     INITAT
.,E3B3 38       SEC                     SEC
.,E3B4 E9 30    SBC #$30                SBCI    "0"             ;ALL CHARS .GT. "9" HAVE RET'D SO
.,E3B6 38       SEC                     SEC
.,E3B7 E9 D0    SBC #$D0                SBCI    ^D256-"0"               ;SEE IF NUMERIC.
                                                                ;TURN CARRY ON IF NUMERIC.
                                                                ;ALSO, SETZ IF NULL.
.,E3B9 60       RTS             CHZRTS: RTS                     ;RETURN TO CALLER.
                                
.:E3BA 80 4F C7 52 58                   128                     ;LOADED OR FROM ROM.
                                        79                      ;THE INITIAL RANDOM NUMBER.
                                        199
                                        82
                                IFN     ADDPRC,<88>
                                IFN REALIO-3,<
                                IFE     KIMROM,<
                                TYPAUT: LDWDI   AUTTXT
                                        JSR     STROUT>>
                                INIT:
                                IFN     REALIO-3,<
.,E3BF A9 4C    LDA #$4C                LDXI    255             ;MAKE IT LOOK DIRECT IN CASE OF
.,E3C1 85 54    STA $54                 STX     CURLIN+1>       ;ERROR MESSAGE.
.,E3C3 8D 10 03 STA $0310       IFN     STKEND-511,<
.,E3C6 A9 48    LDA #$48                LDXI    STKEND-256>
.,E3C8 A0 B2    LDY #$B2                TXS
.,E3CA 8D 11 03 STA $0311       IFN     REALIO-3,<
.,E3CD 8C 12 03 STY $0312               LDWDI   INIT            ;ALLOW RESTART.
.,E3D0 A9 91    LDA #$91                STWD    START+1
.,E3D2 A0 B3    LDY #$B3                STWD    RDYJSR+1        ;RTS HERE ON ERRORS.
.,E3D4 85 05    STA $05                 LDWDI   AYINT
.,E3D6 84 06    STY $06                 STWD    ADRAYI
.,E3D8 A9 AA    LDA #$AA                LDWDI   GIVAYF
.,E3DA A0 B1    LDY #$B1                STWD    ADRGAY>
.,E3DC 85 03    STA $03                 LDAI    76              ;JMP INSTRUCTION.
.,E3DE 84 04    STY $04         IFE     REALIO,<HRLI 1,^O1000>  ;MAKE AN INST.
                                IFN     REALIO-3,<
                                        STA     START
                                        STA     RDYJSR>
                                        STA     JMPER
                                IFN     ROMSW,<
                                        STA     USRPOK
                                        LDWDI   FCERR
                                        STWD    USRPOK+1>
                                        LDAI    LINLEN          ;THESE MUST BE NON-ZERO SO CHEAD WILL
                                        STA     LINWID          ;WORK AFTER MOVING A NEW LINE IN BUF
                                                                ;INTO THE PROGRAM
                                        LDAI    NCMPOS
                                        STA     NCMWID
.,E3E0 A2 1C    LDX #$1C                LDXI    RNDX+4-CHRGET
.,E3E2 BD A2 E3 LDA $E3A2,X     MOVCHG: LDA     INITAT-1,X,
.,E3E5 95 73    STA $73,X               STA     CHRGET-1,X,     ;MOVE TO RAM.
.,E3E7 CA       DEX                     DEX
.,E3E8 10 F8    BPL $E3E2               BNE     MOVCHG
.,E3EA A9 03    LDA #$03                LDAI    STRSIZ
.,E3EC 85 53    STA $53                 STA     FOUR6
.,E3EE A9 00    LDA #$00                TXA                     ;SET CONST IN RAM.
.,E3F0 85 68    STA $68                 STA     BITS
.,E3F2 85 13    STA $13         IFN EXTIO,<
.,E3F4 85 18    STA $18                 STA     CHANNL>
.,E3F6 A2 01    LDX #$01                STA     LASTPT+1
.,E3F8 8E FD 01 STX $01FD       IFN     NULCMD,<
.,E3FB 8E FC 01 STX $01FC               STA     NULCNT>
.,E3FE A2 19    LDX #$19                PHA                     ;PUT ZERO AT THE END OF THE STACK
.,E400 86 16    STX $16                                         ;SO FNDFOR WILL STOP
.,E402 38       SEC             IFN     REALIO,<
.,E403 20 9C FF JSR $FF9C               STA     CNTWFL>         ;BE TALKATIVE.
.,E406 86 2B    STX $2B         IFN     BUFPAG,<
.,E408 84 2C    STY $2C                 INX                     ;MAKE [X]=1
.,E40A 38       SEC                     STX     BUF-3           ;SET PRE-BUF BYTES NON-ZERO FOR CHEAD
.,E40B 20 99 FF JSR $FF99               STX     BUF-4>
.,E40E 86 37    STX $37         IFN     REALIO-3,<
.,E410 84 38    STY $38                 JSR     CRDO>           ;TYPE A CR.
.,E412 86 33    STX $33                 LDXI    TEMPST
.,E414 84 34    STY $34                 STX     TEMPPT          ;SET UP STRING TEMPORARIES.
.,E416 A0 00    LDY #$00        IFN     REALIO!LONGI,<
.,E418 98       TYA             IFN     REALIO-3,<
.,E419 91 2B    STA ($2B),Y             LDWDI   MEMORY
.,E41B E6 2B    INC $2B                 JSR     STROUT
.,E41D D0 02    BNE $E421               JSR     QINLIN          ;GET A LINE OF INPUT.
.,E41F E6 2C    INC $2C                 STXY    TXTPTR          ;READ THIS !
.,E421 60       RTS                     JSR     CHRGET          ;GET THE FIRST CHARACTER.
.,E422 A5 2B    LDA $2B         IFE     KIMROM,<
.,E424 A4 2C    LDY $2C                 CMPI    "A"             ;IS IT AN "A"?
.,E426 20 08 A4 JSR $A408               BEQ     TYPAUT>         ;YES TYPE AUTHOR'S NAME.
.,E429 A9 73    LDA #$73                TAY                     ;NULL INPUT?
.,E42B A0 E4    LDY #$E4                BNE     USEDE9>         ;NO.
.,E42D 20 1E AB JSR $AB1E       IFE     REALIO-3,<
.,E430 A5 37    LDA $37                 LDYI    RAMLOC/^D256>
.,E432 38       SEC             IFN     REALIO-3,<
.,E433 E5 2B    SBC $2B         IFE     ROMSW,<
.,E435 AA       TAX                     LDWDI   LASTWR>         ;YES GET PNTR TO LAST WORD.
.,E436 A5 38    LDA $38         IFN     ROMSW,<
.,E438 E5 2C    SBC $2C                 LDWDI   RAMLOC>>
.,E43A 20 CD BD JSR $BDCD       IFN     ROMSW,<
.,E43D A9 60    LDA #$60                STWD    TXTTAB>         ;SET UP START OF PROGRAM LOCATION
.,E43F A0 E4    LDY #$E4                STWD    LINNUM
.,E441 20 1E AB JSR $AB1E       IFE     REALIO-3,<
.,E444 4C 44 A6 JMP $A644               TAY>
.:E447 8B E3 83 A4 7C A5 1A A7  IFN     REALIO-3,<
.:E44F E4 A7 86 AE                      LDYI    0>
.,E453 A2 0B    LDX #$0B        LOOPMM: INC     LINNUM
.,E455 BD 47 E4 LDA $E447,X             BNE     LOOPM1
.,E458 9D 00 03 STA $0300,X             INC     LINNUM+1
.,E45B CA       DEX             IFE     REALIO-3,<
.,E45C 10 F7    BPL $E455               BMI     USEDEC>
.,E45E 60       RTS             LOOPM1: LDAI    85              ;PUT RANDOM INFO INTO MEM.
                                        STADY   LINNUM
                                        CMPDY   LINNUM          ;WAS IT SAVED?
                                        BNE     USEDEC          ;NO. THAT IS END OF MEMORY.
                                        ASL     A,              ;LOOKS LIKE IT. TRY ANOTHER.
                                        STADY   LINNUM
                                        CMPDY   LINNUM          ;WAS IT SAVED?
                                IFN     REALIO-3,<
                                        BNE     USEDEC>         ;NO. THIS IS THE END.
                                IFN     REALIO-2,<
                                        BEQ     LOOPMM>
                                IFE     REALIO-2,<
                                        BNE     USEDEC
                                        CMP     0               ;SEE IF HITTING PAGE 0
                                        BNE     LOOPMM
                                        LDAI    76
                                        STA     0
                                        BNEA    USEDEC>
                                IFN     REALIO-3,<
                                USEDE9: JSR     CHRGOT          ;GET CURRENT CHARACTER.
                                        JSR     LINGET          ;GET DECIMAL ARGUMENT.
                                        TAY                     ;MAKE SURE A TERMINATOR EXISTS.
                                        BEQ     USEDEC          ;IT DOES.
                                        JMP     SNERR>          ;IT DOESN'T.
                                USEDEC: LDWD    LINNUM          ;GET SIZE OF MEMORY INPUT.
                                USEDEF: >                       ;HIGHEST ADDRESS.
                                IFE     REALIO!LONGI,<
                                        LDWDI   16190>          ;A STRANGE NUMBER.
                                        STWD    MEMSIZ          ;THIS IS THE SIZE OF MEMORY.
                                        STWD    FRETOP          ;TOP OF STRINGS TOO.
                                TTYW:
                                IFN     REALIO-3,<
                                IFN     REALIO!LONGI,<
                                        LDWDI   TTYWID
                                        JSR     STROUT
                                        JSR     QINLIN          ;GET LINE OF INPUT.
                                        STXY    TXTPTR          ;READ THIS !
                                        JSR     CHRGET          ;GET FIRST CHARACTER.
                                        TAY                     ;TEST ACCA BUT DON'T AFFECT CARRY.
                                        BEQ     ASKAGN
                                        JSR     LINGET          ;GET ARGUMENT.
                                        LDA     LINNUM+1
                                        BNE     TTYW            ;WIDTH MUST BE .LT. 256.
                                        LDA     LINNUM
                                        CMPI    16              ;WIDTH MUST BE GREATER THAN 16.
                                        BCC     TTYW
                                        STA     LINWID          ;THAT IS THE LINE WIDTH.
                                MORCPS: SBCI    CLMWID          ;COMPUTE POSITION BEYOND WHICH
                                        BCS     MORCPS          ;THERE ARE NO MORE FIELDS.
                                        EORI    255
                                        SBCI    CLMWID-2
                                        CLC
                                        ADC     LINWID
                                        STA     NCMWID>
                                ASKAGN:
                                IFE     ROMSW,<
                                IFN     REALIO!LONGI,<
                                        LDWDI   FNS
                                        JSR     STROUT
                                        JSR     QINLIN
                                        STXY    TXTPTR          ;READ THIS !
                                        JSR     CHRGET
                                        LDXYI   INITAT          ;DEFAULT.
                                        CMPI    "Y"
                                        BEQ     HAVFNS          ;SAVE ALL FUNCTIONS.
                                        CMPI    "A"
                                        BEQ     OKCHAR          ;SAVE ALL BUT ATN.
                                        CMPI    "N"
                                        BNE     ASKAGN          ;BAD INPUT.
                                                                ;SAVE NOTHING.
                                OKCHAR: LDXYI   FCERR
                                        STXY    ATNFIX          ;GET RID OF ATN FUNCTION.
                                        LDXYI   ATN             ;UNTIL WE KNOW THAT WE SHOULD DEL MORE.
                                        CMPI    "A"
                                        BEQ     HAVFNS          ;JUST GET RID OF ATN.
                                        LDXYI   FCERR
                                        STXY    COSFIX          ;GET RID OF THE REST.
                                        STXY    TANFIX
                                        STXY    SINFIX
                                        LDXYI   COS             ;AND GET RID OF ALL BACK TO "COS".
                                HAVFNS:>
                                IFE     REALIO!LONGI,<
                                        LDXYI   INITAT-1>>>     ;GET RID OF ALL UP TO "INITAT".
                                IFN     ROMSW,<
                                        LDXYI   RAMLOC
                                        STXY    TXTTAB>
                                        LDYI    0
                                        TYA
                                        STADY   TXTTAB          ;SET UP TEXT TABLE.
                                        INC     TXTTAB
                                IFN     REALIO-3,<
                                        BNE     QROOM
                                        INC     TXTTAB+1>
                                QROOM:  LDWD    TXTTAB          ;PREPARE TO USE "REASON".
                                        JSR     REASON
                                IFE     REALIO-3,<
                                        LDWDI   FREMES
                                        JSR     STROUT>
                                IFN     REALIO-3,<
                                        JSR     CRDO>
                                        LDA     MEMSIZ          ;COMPUTE [MEMSIZ]-[VARTAB].
                                        SEC
                                        SBC     TXTTAB
                                        TAX
                                        LDA     MEMSIZ+1
                                        SBC     TXTTAB+1
                                        JSR     LINPRT          ;TYPE THIS VALUE.
                                        LDWDI   WORDS           ;MORE BULLSHIT.
                                        JSR     STROUT
                                        JSR     SCRTCH          ;SET UP EVERYTHING ELSE.
                                IFE     REALIO-3,<
                                        JMP     READY>
                                IFN     REALIO-3,<
                                        LDWDI   STROUT
                                        STWD    RDYJSR+1
                                        LDWDI   READY
                                        STWD    START+1
                                        JMPD    START+1
                                
                                IFE     ROMSW,<
                                FNS:    DT"WANT SIN-COS-TAN-ATN"
                                        0>
                                IFE     KIMROM,<
                                AUTTXT: ACRLF
                                        12                      ;ANOTHER LINE FEED.
                                        DT"WRITTEN "
                                        DT"BY WEILAND & GATES"
                                        ACRLF
                                        0>
                                MEMORY: DT"MEMORY SIZE"
                                        0
                                TTYWID:
                                IFE     KIMROM,<
                                        DT"TERMINAL ">
                                        DT"WIDTH"
                                        0>
                                WORDS:  DT" BYTES FREE"
                                IFN     REALIO-3,<
                                        ACRLF
                                        ACRLF>
                                IFE     REALIO-3,<
                                        EXP     ^O15
                                        0
                                FREMES: >
                                IFE REALIO,<    DT"SIMULATED BASIC FOR THE 6502 V1.1">
                                IFE REALIO-1,<  DT"KIM BASIC V1.1">
                                IFE REALIO-2,<  DT"OSI 6502 BASIC VERSION 1.1">
                                IFE REALIO-3,<  DT"### COMMODORE BASIC ###"
                                        EXP     ^O15
                                        EXP     ^O15>
                                IFE     REALIO-4,<DT"APPLE BASIC V1.1">
                                IFE     REALIO-5,<DT"STM BASIC V1.1">
                                IFN     REALIO-3,<
                                        ACRLF
                                        DT"COPYRIGHT 1978 MICROSOFT"
                                        ACRLF>
                                        0
                                LASTWR::
                                        BLOCK   100             ;SPACE FOR TEMP STACK.
                                IFE REALIO,<
                                TSTACK::BLOCK   13600>
                                
                                IF2,<
                                        PURGE   A,X,Y>
                                IFNDEF  START,<START==0>
                                        END     $Z+START
