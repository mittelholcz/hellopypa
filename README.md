# Hogyan készítsünk python csomagot?

## 1. Környezet

Feltételezett könyvtárszerkezet:

```txt
proba_package/
    proba_modul/
        __init__.py
        proba.py
    test/
        test_proba.py
    LICENCE.md
    MANIFEST.in
    README.md
    requirements.txt
    requirements-dev.txt
    setup.py
```

Hozzunk létre a csomagnak külön virtuális környezetet és aktiváljuk:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Telepítsük a csomaghoz (`requirements.txt`) és a csomagoláshoz (`requirements-dev.txt`) szükséges függőségeket:

```sh
pip install -r requirements-dev.txt
```

Megjegyzés: a `requirements-dev.txt` importálja sima `requirements.txt`-t is. A `requirements.txt` fájlok leírását l. [itt](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format) és [itt](https://pip.pypa.io/en/stable/user_guide/#requirements-files).

A csomagoláshoz szükséges csomagok:

- `setuptools`: Ez a `setup.py` függősége.
- `twine`: Ezzel lehet a <pypi.org>-ra feltölteni az elkészült csomagot.
- `wheel`: Ez kell a 2012-ben bevezetett *wheel* csomagformátumhoz (l. [PEP 427](https://www.python.org/dev/peps/pep-0427/)).

## 2. Tesztelés

TODO

## 3. A `setup.py` fájl

TODO

## 4. A 'MANIFEST.in' fájl

TODO

## 5. Csomagolás, közzététel

TODO

## Irodalom

- gyorstalpaló: <https://packaging.python.org/tutorials/packaging-projects/>
- sok részletes útmutató egyes témakörökhöz: <https://packaging.python.org/guides/>
- *Real Python* [tutorial](<https://realpython.com/pypi-publish-python-package/>)
