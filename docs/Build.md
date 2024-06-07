
# Building

*How to build this project locally*


## Generating

<br>

**Requirements:** 

-   **[Python]**
-   **[Markdown]**

    ```sh
    pip3 install markdown
    ```
    
The Python package can also be installed into a virtual environment:
    
```sh
python3 -m venv .venv                       # create a virtual environment
source .venv/bin/activate                   # activate it 
python3 -m pip install -r requirements.txt  # install the required packages
```
    
To generate the  `html`  files, simply execute  [`generate.sh`][Generate]


This will build the different pages from the repos *reference material* with the help of `python` scripts.

The 6502 reference is all Java Script and does not need to be generated. 

## Testing

For testing start Python's built-in webserver and navigate to the local url:
```sh
python3 -m http.server 
```
[http://localhost:8000/6502/][Localhost8000]


If the default port is already taken, choose your own port (eg. 6502):

```sh
python3 -m http.server 6464
```
[http://localhost:6502/6502/][Localhost6464]


Navigate using the menu bar or directly going to the specific pages:

*  `6502` for _6502 Family CPU Reference_
*  `c64disasm` for _C64 BASIC & KERNAL ROM Disassembly_
<!-- *  `c64io` for _C64 I/O Map -->
*  `c64mem` for _C64 Memory Map_
*  `charset` for _Character Set · PETSCII · Keyboard_
*  `colors` for _C64 Colors_
*  `kernal` for _C64 KERNAL API_

---



<!----------------------------------------------------------------------------->

[Generate]: ../Source/generate.sh

[Markdown]: https://pypi.org/project/Markdown/
[Python]: https://www.python.org/

[Localhost8000]: http://localhost:8000/6502/
[Localhost6464]: http://localhost:6464/6502/
