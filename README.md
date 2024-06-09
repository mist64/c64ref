
<div align = center>

# Ultimate Commodore <br> 64 Reference Guide

An effort to collect `C64` reference material <br>
in machine readable form and maintain <br>
scripts to present this material to the web.

<br>
<br>

[![Button Website]][Website]   
[![Button Building]][Building]

<br>
<br>

## Material

*Reference material collected in this repository.*

<br>

### ROM Disassembly

<br>

| KERNAL | BASIC | Lang | By / From |
|:------:|:-----:|:----:|:---------:|
|  ◯                       | [⬤][Disassembly BASIC] | :us: | **Microsoft**
| [⬤][Disassembly KERNAL] |  ◯                      | :us: | **Commodore**
| [⬤][Disassembly Lee]    | [⬤][Disassembly Lee]   | :us: | `Lee Davison`
|  ◯                       | [⬤][Disassembly Bob]   | :us: | `Bob Sander-Cederlof`
| [⬤][Disassembly Buch]   | [⬤][Disassembly Buch]  | :de: | **Commodore-64-intern-Buch**
| [⬤][Disassembly Magnus] |  ◯                      | :us: | `Magnus Nyman`
| [⬤][Disassembly Marko]  | [⬤][Disassembly Marko] | :us: | `Marko Mäkelä`

<br>

### Memory Map

<br>

| Title | Lang | By / From |
|:-----:|:----:|:---------:|
| [`Mapping the Commodore 64`][Memory Sheldon]         | :us: | `Sheldon Leemon`
| [`Memory Map mit Wandervorschlägen`][Memory Hauck]   | :de: | `Dr. H. Hauck`
| [`Commodore-64-intern-Buch`][Memory Buch]            | :de: | **Commodore**
| [`Reference`][Memory Joe]                            | :us: | `Joe Forster / STA`
| [`Comments in the original source`][Memory Original] | :us: | **Microsoft** / **Commodore** |
| [`C64 Programmer's Reference Guide`][Memory Guide]   | :us: |
| [`64map`][Memory Map]                                | :us: |
| [`Reference`][Memory Jim]                            | :us: | `Jim Butterfield`

<br>

### KERNAL API

<br>

| Title | Lang | By / From |
|:-----:|:----:|:---------:|
| [`Commodore 64 Programmer's Reference Guide`][API Guide] | :us: | **Commodore**
| [`COMPUTE!'s VIC-20 and Commodore 64 Tool Kit: Kernal`][API Dan] | :us: | `Dan Heeb`
| [`Machine Language Routines for the Commodore 64 and 128`][API Todd] | :us: | `Todd D Heimarck` <br> `Patrick Parrish`
| [`Mapping the Commodore 64`][API Sheldon] | :us: | `Sheldon Leemon`
| [`Commodore 128 intern`][API 128] | :us: | `Jörg Schieb` <br> `Frank Thrun` <br> `Heinz Wrobel`
| [`The almost completely commented C64 ROM disassembly`][API Lee] | :us: | `Lee Davison`
| [`Cracking The Kernal`][API Peter] | :us: | `Peter Marcotty`
| [`Kernal 64 / 128`][API Craig] | :us: | `Craig Taylor`
| [`Commodore 64 standard KERNAL functions`][API Joe] | :us: | `Joe Forster / STA`
| [`C64 KERNAL jump table`][API Frank] | :us: | `Frank Kontros`
| [`Das neue Commodore-64-intern-Buch`][API Sheldon] | :de: | `Baloui` <br> `Brückmann` <br> `Englisch` <br> `Felt` <br> `Gelfand` <br> `Gerits` <br> `Krsnik`

<br>
<br>

## Contributions

`Extensions` , `Translations` , `Corrections` <br>
of typos and content, .. **are welcome!**

<br>
<br>

## Credits

The original effort of ***collecting***, ***converting***, ***formatting*** <br>
and ***editing*** the collected files was done by **[Michael Steil]**.

</div>

<br>


<!----------------------------------------------------------------------------->

[Website]: http://pagetable.com/c64ref

[Building]: docs/Build.md

[Michael Steil]: mailto:mist64@mac.com

[Disassembly KERNAL]: src/c64disasm/c64disasm_cbm.txt
[Disassembly Magnus]: src/c64disasm/c64disasm_mn.txt
[Disassembly BASIC]: src/c64disasm/c64disasm_ms.txt
[Disassembly Marko]: src/c64disasm/c64disasm_mm.txt
[Disassembly Buch]: src/c64disasm/c64disasm_de.txt
[Disassembly Bob]: src/c64disasm/c64disasm_sc.txt
[Disassembly Lee]: src/c64disasm/c64disasm_en.txt

[Memory Original]: src/c64mem/c64mem_src.txt
[Memory Sheldon]: src/c64mem/c64mem_mapc64.txt
[Memory Hauck]: src/c64mem/c64mem_64er.txt
[Memory Guide]: src/c64mem/c64mem_prg.txt
[Memory Buch]: src/c64mem/c64mem_64intern.txt
[Memory Joe]: src/c64mem/c64mem_sta.txt
[Memory Map]: src/c64mem/c64mem_64map.txt
[Memory Jim]: src/c64mem/c64mem_jb.txt

[API Sheldon]: src/kernal/kernal_mapc64.txt
[API Guide]: src/kernal/kernal_prg.txt
[API Frank]: src/kernal/kernal_fk.txt
[API Peter]: src/kernal/kernal_pm.txt
[API Craig]: src/kernal/kernal_ct.txt
[API Buch]: src/kernal/kernal_64intern.txt
[API Todd]: src/kernal/kernal_mlr.txt
[API 128]: src/kernal/kernal_128intern.txt
[API Dan]: src/kernal/kernal_dh.txt
[API Lee]: src/kernal/kernal_ld.txt
[API Joe]: src/kernal/kernal_sta.txt


<!---------------------------------[ Buttons ]--------------------------------->

[Button Building]: https://img.shields.io/badge/Building-5A6AB1?style=for-the-badge&logoColor=white&logo=GitBook
[Button Website]: https://img.shields.io/badge/Website-6BA539?style=for-the-badge&logoColor=white&logo=OpenStreetMap
