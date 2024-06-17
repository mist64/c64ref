
# Building

*How to build this project locally*


## Generating

**Requirements:**

-   [Python]
-   [Markdown]

See also [requirements.txt].

The Python packages are installed into a virtual environment like this:

```sh
python3 -m venv .venv                       # create a virtual environment
source .venv/bin/activate                   # activate it
python3 -m pip install -r requirements.txt  # install the required packages
```

To generate the  `html`  files, simply execute  [`generate.py`][Generate]

This will build the different pages from the repos *reference material* with the help of `shell` and `python` scripts.

`./generate --wip` builds everything including `colors` and `c64io`.

`./generate.py --only 6502 colors c64mem` only builds the selected categories (using the category path names as keys).


The `6502` and the `color` reference are all Java Script and do not need to be generated while developing, but for release the umbrella `generate.py` adds navigation, matching titles and a link to the github project.


## Testing

For testing start Python's built-in webserver and navigate to the local url:
```sh
python3 -m http.server
```
[`http://localhost:8000/c64ref/6502/`][Localhost8000]


If the default port is already taken, choose your own port (eg. 6464):

```sh
python3 -m http.server 6464
```
[`http://localhost:6464/c64ref/6502/`][Localhost6464]


Navigate using the menu bar or by directly going to the specific pages:

*  `6502` for _6502 Family CPU Reference_
*  `c64disasm` for _C64 BASIC & KERNAL ROM Disassembly_ (**Slow**)
*  `c64io` for _C64 I/O Map_ (**WIP**)
*  `c64mem` for _C64 Memory Map_
*  `charset` for _Character Set · PETSCII · Keyboard_
*  `colors` for _C64 Colors_ (**WIP**)
*  `kernal` for _C64 KERNAL API_


## Upload

For uploading use

```
./generate upload
```

It checks for changes in the working copy and won't let you build if there are any.

---


<!----------------------------------------------------------------------------->

[Generate]: ../generate.py
[requirements.txt]: ../requirements.txt

[Markdown]: https://pypi.org/project/Markdown/
[Python]: https://www.python.org/

[Localhost8000]: http://localhost:8000/c64ref/6502/
[Localhost6464]: http://localhost:6464/c64ref/6502/
