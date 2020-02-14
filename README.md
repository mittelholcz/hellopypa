# Hogyan készítsünk python csomagot?

## 1. Könyvtárszerkezet

```txt
hellopypa/
    hellopypa/
        __init__.py
        hellopypa.py
    test/
        test_hellopypa.py
    LICENCE.md
    MANIFEST.in
    README.md
    requirements.txt
    requirements-dev.txt
    setup.py
```

Fontosabb könyvtárak és fájlok:

- `hellopypa/`: a csomagunk fő könyvtára
- `test/`: A csomaghoz való tesztek könyvtára. A tesztek nem részei a csomagnak, csak a repónak.
- `MANIFEST.in`: Itt soroljuk fel a csomaghoz tartozó nem python fájlokat (binárisok, konfig fájlok, stb.)
- `requirements*.txt`: Ezekben vannak felsorolva azok a python csomagok, amelyeket használunk (függőségek). A `requirements.txt` tartalmazza magának a csomagnak a függőségeit, a `requirements-dev.txt` pedig a fejlesztéshez szükséges függőségeket (tesztelés, linter, stb).
- `setup.py`: Ez a fájl tartalmazza csomagoláshoz kellő metaadatokat.

## 2. Környezet

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
- `twine`: Ezzel lehet a [pypi.org](https://pypi.org/)-ra feltölteni az elkészült csomagot.
- `wheel`: Ez kell a 2012-ben bevezetett *wheel* csomagformátumhoz (l. [PEP 427](https://www.python.org/dev/peps/pep-0427/)).

# 3. Tesztelés

Mielőtt csomagolnánk, teszteljük le az alkalmazásunkat. A teszteléshez a [pytest](https://docs.pytest.org/en/latest/)-et használjunk. A `test/` könyvtárban vannak a tesztfájlok, ezeket a következő paranccsal futtathatjuk:

```sh
pytest --verbose test/
```

Megjegyzés: a `test/` könyvtár maga is csomag, kell benne lennie `__init__.py` fájlnak.

## TODO

- Bevezetés: modul, csomag, pypi
- [x] Könyvtárszerkezet
- [x] Környezet
- [x] Tesztelés
- [ ] Dokumentáció
- [ ] A `setup.py` fájl
- [ ] A `MANIFEST.in` fájl
- [ ] Verziózás
- [ ] Csomagolás
- [ ] Közzététel
- [ ] Automatizálás
- [ ] Telepítés
  - [ ] lokálisan
  - [ ] GH-ról
  - [ ] pypi

## Irodalom

- gyorstalpaló: <https://packaging.python.org/tutorials/packaging-projects/>
- sok részletes útmutató egyes témakörökhöz: <https://packaging.python.org/guides/>
- *Real Python* [tutorial](<https://realpython.com/pypi-publish-python-package/>)
