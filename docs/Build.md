
# Building

<br>

## Generating

<br>

**Requirements:** 

-   **[Python]**

-   **[Markdown]**

    ```sh
    pip install markdown
    ```

<br>

To generate the  `html`  files,<br>
simply execute  [`generate.sh`][Generate]

This will build the different pages from the repos <br>
*reference material* with the help of `python` scripts.

<br>
<br>

## Testing

**Requires:** **[Deno]**

To test the generated pages you <br>
will need to start a local webserver.

```sh
Test/Webserver.sh
```

<br>

### Permissions

*Make sure the file is executable, otherwise you* <br>
*will likely receive a `Permission Denied` error.*

```sh
sudo chmod ug+x Test/Webserver.sh # Linux Fix
```

<br>

### Browser

After starting your webserver you will just need <br>
to navigate to [`http://localhost:6464/6502/`][Localhost]

<br>

### Shortcuts

#### <kbd>  Ctrl + C  </kbd>

To stop the **Webserver**.

<br>

#### <kbd>  Ctrl + Shift + I  </kbd> or <kbd>  F12  </kbd>

To open the **Inspector**.

<br>

#### <kbd>  F5  </kbd>

To reload the page.

<br>


<!----------------------------------------------------------------------------->

[Generate]: ../Source/generate.sh

[Markdown]: https://pypi.org/project/Markdown/
[Python]: https://www.python.org/
[Deno]: https://deno.land/

[Localhost]: http://localhost:6464/6502/
