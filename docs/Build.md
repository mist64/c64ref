# Building

<br>

---

<br>

## Generating

**Requires:** 
- [`Python`][Python]
- [`Markdown`][Markdown]

    ```sh
    pip install markdown
    ```

To generate the `html` files,<br>
simply execute [`generate.sh`][Generate].

This will build the different pages from the repos <br>
*reference material* with the help of `python` scripts.

<br>

---

<br>

## Testing

**Requires:** [`Deno`][Deno]

To test the generated pages you <br>
will need to start a local webserver.

```sh
Test/Webserver.sh
```

<br>

##### Permissions

*Make sure the file is executable, otherwise you* <br>
*will likely receive a `Permission Denied` error.*

```sh
sudo chmod ug+x Test/Webserver.sh # Linux Fix
```

<br>

##### Browser

After starting your webserver you will just need <br>
to navigate to [`http://localhost:6464/6502/`][Localhost]

<br>

##### Tips

Stop the **Webserver** with <kbd>Ctrl</kbd> <kbd>C</kbd>

Open the **Inspector** with either <kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>I</kbd> or <kbd>F12</kbd>.

Use <kbd>F5</kbd> to reload the page.


<!----------------------------------------------------------------------------->

[Generate]: ../Source/generate.sh

[Markdown]: https://pypi.org/project/Markdown/
[Python]: https://www.python.org/
[Deno]: https://deno.land/

[Localhost]: http://localhost:6464/6502/
