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

Ez *build-szkript* a [*setuptools*](https://setuptools.readthedocs.io/en/latest/) számára. A *setuptools* hozza létre a könyvtárunkból a terjeszthető és *pip*-pel telepíthető formátumot.

Minta:

```py
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='hellopypa',
    version='0.0.1',
    author='mittelholcz',
    description='A sample Python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mittelholcz/hellopypa',
    packages=setuptools.find_packages(exclude=['test']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
)
```

A *setuptools.setup* fontosabb mezői:

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

paranccsal tudjuk futtatni. A repónkban három új könyvtár fog létrejönni: egy `build/`, egy `dist/` és egy `hellopypa.egg-info/`. Ezek közül a `dist/` ami fontos, ebben található ugyanis a csomagunk terjeszthető és telepíthető változata.

A csomag közvetlenül telepíthető a `pip install .` paranccal, vagy regisztrációt követően feltölthető a pypi.org oldalra a következő paranccsal:

```sh
python3 -m twine upload dist/*
```

Ezután bármelyik gépen telepíthető a csomag a `pip install hellopypa` paranccsal.

A pypi.org oldalnak van egy teszt változata is, ha csak kísérletezni szeretnénk, javasolt ezt használni. A fenti parancsok ekkor így módosulnak:

```sh
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ hellopypa
```

## 5. Verzió

A csomag verzióját érdemes egy helyen tárolni csak és máshol erről az egy helyről beolvasni valahogy. A lehetőségeket l. [itt](https://packaging.python.org/guides/single-sourcing-package-version/). Az itt használt megoldás lényege, hogy a csomagon belül egy külön fájlt használunk erre (`hellopypa/version.py`). Ezt a fájlt importáljuk a `setup.py`-ban és a `hellopypa/__init__.py`-ban is. Ezzel elkerülhetők a `hellopypa/__init__.py` közvetlen importálásának problémái (l. az előbbi cikk 6. pontjához írt figyelmeztetést), de telepítés nélkül is hozzáférhető lesz a verzió, mintha az `__init__.py`-ban lenne közvetlenül.

`hellopypa/version.py`:

```py
__version__ = '0.0.3'
```

`hellopypa/__init__.py`:

```py
# ...
from hellopypa.version import __version__
# ...
```

`setup.py`:

```py
# ...
from hellopypa.version import __version__
# ...
setuptools.setup(
    # ...
    version=__version__,
    # ...
)
# ...
```

## 6. Fájlok hozzáadása

A *setuptools* csak a python fájlokat veszi figyelembe. Ha más fájlokat is a csomaghoz szeretnénk adni (konfigurációs fájlokat, binárisokat, adatot), akkor két dolgot kell csinálnunk.

1. Létre kell hoznunk egy *MANIFEST.in* fájlt, amiben felsoroljuk, hogy miket szeretnénk még a csomaghoz adni. Részletek [itt](https://packaging.python.org/guides/using-manifest-in/). Példa: adjuk a projekthez a *.cfg* kiterjesztésű fájlokat.

    ```txt
    include hellopypa/*.cfg
    ```

2. A *setup.py*-ba is bele kell írni, hogy további fájlok is lesznek.

    ```py
    # ...
    setuptools.setup(
        # ...
        include_package_data=True,
        # ...
    )
    # ...
    ```

## TODO

- [ ] Bevezetés: modul, csomag, pypi
- [x] Könyvtárszerkezet
- [x] Környezet
- [x] Tesztelés
- [ ] Dokumentáció
- [x] A `setup.py` fájl
- [x] A `MANIFEST.in` fájl
- [ ] `__main__.py`, CLI
- [ ] `__init__.py`, API
- [x] Verziózás
- [x] Csomagolás
- [x] Közzététel
- [ ] Automatizálás
- [x] Telepítés
  - [x] lokálisan
  - [x] pypi
- [ ] make

## Irodalom

- gyorstalpaló: <https://packaging.python.org/tutorials/packaging-projects/>
- sok részletes útmutató egyes témakörökhöz: <https://packaging.python.org/guides/>
- *Real Python* [tutorial](<https://realpython.com/pypi-publish-python-package/>)
