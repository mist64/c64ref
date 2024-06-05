
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

**Testing is probably also possible with Python's built-in webserver.**

---


**Requires:** **[Deno]**


To test the generated pages you will need to start a local webserver.

```sh
Test/Webserver.sh
```

### Permissions

*Make sure the file is executable, otherwise you will likely receive a `Permission Denied` error.*

```sh
sudo chmod ug+x Test/Webserver.sh # Linux Fix
```

### Browser

After starting your webserver you will just need to navigate to [`http://localhost:6464/6502/`][Localhost]

### Shortcuts

* Stop the **Webserver**: <kbd>  Ctrl + C  </kbd> 

* Open the **Inspector**: <kbd>  Ctrl + Shift + I  </kbd>  or  <kbd>  F12  </kbd> 

* Reload the page: <kbd>  F5  </kbd>



<!----------------------------------------------------------------------------->

[Generate]: ../Source/generate.sh

[Markdown]: https://pypi.org/project/Markdown/
[Python]: https://www.python.org/
[Deno]: https://deno.land/

[Localhost]: http://localhost:6464/6502/
