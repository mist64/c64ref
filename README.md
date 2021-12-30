# Ultimate Commodore 64 Reference

An effort to collect `C64` reference material <br>
in machine readable form and maintain <br>
scripts to present this material to the web.

---

**⸢ [View Rendered] ⸥ ⸢ [Building] ⸥**

---

<br>

## Material

*Reference material collected in this repository.*

<br>

#### ROM Disassembly

| KERNEL | BASIC | Lang | By / From |
|:------:|:-----:|:----:|:---------:|
|  ◯                       | [⬤][Disassembly BASIC] | :us: | **Microsoft**
| [⬤][Disassembly KERNEL] |  ◯                      | :us: | **Commodore**
| [⬤][Disassembly Lee]    | [⬤][Disassembly Lee]   | :us: | `Lee Davison`
|  ◯                       | [⬤][Disassembly Bob]   | :us: | `Bob Sander-Cederlof`
| [⬤][Disassembly Buch]   | [⬤][Disassembly Buch]  | :de: | **Commodore-64-intern-Buch**
| [⬤][Disassembly Magnus] |  ◯                      | :us: | `Magnus Nyman`
| [⬤][Disassembly Marko]  | [⬤][Disassembly Marko] | :us: | `Marko Mäkelä`

<br>

#### Memory Map

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

#### KERNEL API

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

---

## Contributions

- `Extensions`
- `Corrections ( Typos & Content )`
- `Translations`
- `..` <br>
   <br>
  **Are Welcome !**

<br>

---

## Credits

The original effort of ***collecting***, ***converting***, ***formatting*** <br>
and ***editing*** the collected files was done by **[Michael Steil]**.

<!----------------------------------------------------------------------------->

[View Rendered]: http://pagetable.com/c64ref

[Building]: docs/Build.md

[Michael Steil]: mailto:mist64@mac.com

[Disassembly BASIC]: Source/c64disasm/c64disasm_ms.txt
[Disassembly KERNEL]: Source/c64disasm/c64disasm_cbm.txt
[Disassembly Lee]: Source/c64disasm/c64disasm_en.txt
[Disassembly Bob]: Source/c64disasm/c64disasm_sc.txt
[Disassembly Buch]: Source/c64disasm/c64disasm_de.txt
[Disassembly Magnus]: Source/c64disasm/c64disasm_mn.txt
[Disassembly Marko]: Source/c64disasm/c64disasm_mm.txt

[Memory Sheldon]: Source/c64mem/c64mem_mapc64.txt
[Memory Hauck]: Source/c64mem/c64mem_64er.txt
[Memory Buch]: Source/c64mem/c64mem_64intern.txt
[Memory Joe]: Source/c64mem/c64mem_sta.txt
[Memory Original]: Source/c64mem/c64mem_src.txt
[Memory Guide]: Source/c64mem/c64mem_prg.txt
[Memory Map]: Source/c64mem/c64mem_64map.txt
[Memory Jim]: Source/c64mem/c64mem_jb.txt

[API Guide]: Source/kernal/kernal_prg.txt
[API Dan]: Source/kernal/kernal_dh.txt
[API Todd]: Source/kernal/kernal_mlr.txt
[API Sheldon]: Source/kernal/kernal_mapc64.txt
[API 128]: Source/kernal/kernal_128intern.txt
[API Lee]: Source/kernal/kernal_ld.txt
[API Peter]: Source/kernal/kernal_pm.txt
[API Craig]: Source/kernal/kernal_ct.txt
[API Joe]: Source/kernal/kernal_sta.txt
[API Frank]: Source/kernal/kernal_fk.txt
[API Buch]: Source/kernal/kernal_64intern.txt
