# Hogyan készítsünk python csomagot?

## 1. Könyvtárszerkezet

```txt
hellopypa/
    hellopypa/
        __init__.py
        hellopypa.py
    test/
        test_hellopypa.py
    LICENSE.md
    MANIFEST.in
    README.md
    requirements.txt
    requirements-dev.txt
    setup.py
```

Fontosabb könyvtárak és fájlok:

- `hellopypa/`: a csomagunk fő könyvtára
- `test/`: A csomaghoz való tesztek könyvtára. A tesztek nem részei a csomagnak, csak a repónak.
- `LICENSE`: Licenc, a lehetőségeket l. [itt](https://choosealicense.com/).
- `MANIFEST.in`: Itt soroljuk fel a csomaghoz tartozó nem python fájlokat (binárisok, konfig fájlok, stb).
- `README.md`: Readme fájl, röviden leírja, hogy mire jó a csomag, hogyan kell telepíteni és hogyan lehet futtatni. A *markdown* formátumról bővebben [itt](https://guides.github.com/features/mastering-markdown/), a tartalmáról [itt](https://dbader.org/blog/write-a-great-readme-for-your-github-project) lehet olvasni.
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

## 3. Tesztelés

Mielőtt csomagolnánk, teszteljük le az alkalmazásunkat. A teszteléshez a [pytest](https://docs.pytest.org/en/latest/)-et használjunk. A `test/` könyvtárban vannak a tesztfájlok, ezeket a következő paranccsal futtathatjuk:

```sh
pytest --verbose test/
```

Megjegyzés: a `test/` könyvtár maga is csomag, kell benne lennie `__init__.py` fájlnak.

## 4. A `setup.py` fájl

Ez a fájl a build-szkript a [setuptools](https://setuptools.readthedocs.io/en/latest/) számára. A setuptools egy python csomag, ami a csomagolást végzi.

Minta:

```py
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hellopypa",
    version="0.0.1",
    author="mittelholcz",
    description="Get string 'hello pypa!'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mittelholcz/hellopypa",
    packages=setuptools.find_packages(exclude=['test']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
```

- `name`: A csomag neve (kötelező).
- `verzion`: A csomag verziója (kötelező).
- `author`: A csomag szerzője.
- `description`: Rövid leírás.
- `long_description`: Hosszú leírás, jellemzően magát a README.md-t szokták megadni. A PyPI ezt fogja a csomag oldalán megjeleníteni. Ha *markdown* fájlt adunk meg, akkor meg kell adnunk a formátumot is.
- `url`: A projekt honlapja.
- `packages`: Itt adható meg, hol keresse a python fájlokat. Érdemes a *setuptools* `find_packages()` függvényére bizni a dolgot. Az `exclude=[dir1, dir2, ...]` paraméternek megadott könyvtárakban nem fog keresni.
- `classifiers`: A PyPI számára megadható címkék listája [itt](https://pypi.org/classifiers/).
- `python_requires`: Megadható a minimum python verzió.

Ha `setup.py` fájlt a

```sh
python3 setup.py sdist bdist_wheel
```

paranccsal tudjuk futtatni. Ez létrehoz egy `dist/` könyvtárat a repo-n belül, amiben a csomagunk található.

## TODO

- [ ] Bevezetés: modul, csomag, pypi
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
