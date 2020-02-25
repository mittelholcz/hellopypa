# Hogyan készítsünk python csomagot

## 1. Bevezetés

A *modul* (*module*) egy python fájl, ami importálható, névteret alkot és tetszőleges további python objektumokat tartalmazhat.

A *csomag* (*package*) egy olyan könyvtár, ami tartalmaz egy `__init__.py`
fájlt, továbbá tartalmazhat további alcsomagokat (alkönyvtárakat) és
modulokat (python fájlokat). A *csomag* is importálható, névteret alkot és
további python objektumokat tartalmazhat.

*Megjegyzés*: A *modul~fájl* és a *csomag~könyvtár* csak analógia, nem minden
esetben igaz. Részletek [itt](https://docs.python.org/3/reference/import.html).

A csomagokat a Python csomagkezelőjével, a
[`pip`](https://pip.pypa.io/en/stable/)-pel lehet telepíteni, frissíteni,
eltávolítani. A `pip` képes verziókezelő repozitóriumokból is telepíteni, így
pl. a Github-ról is, de a python csomagok publikálásának szokott módja a
csomag feltöltése a [pypi.org](https://pypi.org/)-ra (*PyPI*: Python Package
Index). Ennek mikéntjéről lesz szó az alábbiakban.

A [pypi.org](https://pypi.org/)-ot és a csomagoláshoz szükséges eszközöket a
*PyPA* (*Python Packaging Authority*) fejleszti és tartja karban. Honlapjukon
([pypa.io](https://www.pypa.io/en/latest/)) sok hasznos anyag elérhető
csomagolás és terjesztés témakörben.

## 2. Könyvtárszerkezet

```txt
hellopypa/
    hellopypa/
        __init__.py
        __main__.py
        example.cfg
        hellopypa.py
        version.py
    test/
        __init__.py
        test_hello.py
    LICENSE
    MANIFEST.in
    README.md
    requirements.txt
    requirements-dev.txt
    setup.py
```

Fontosabb könyvtárak és fájlok:

- `hellopypa/`: A csomagunk fő könyvtára. Általában jó, ha ez megegyezik
  magának a repónak a nevével (külső `hellopypa/` könyvtár), de nem szükséges.
- `test/`: A csomaghoz való tesztek könyvtára. A tesztek nem részei a
  csomagnak, csak a repónak.
- `LICENSE`: Licenc, a lehetőségeket l. [itt](https://choosealicense.com/) és
  [itt](https://opensource.org/licenses), további tanácsok
  [itt](https://arstechnica.com/gadgets/2020/02/how-to-choose-an-open-source-license/).
- `MANIFEST.in`: Itt soroljuk fel a csomaghoz tartozó nem python fájlokat (binárisok, konfig fájlok, stb).
- `README.md`: Readme fájl, röviden leírja, hogy mire jó a csomag, hogyan kell telepíteni és hogyan lehet futtatni. A *markdown* formátumról bővebben [itt](https://guides.github.com/features/mastering-markdown/), a tartalmáról [itt](https://dbader.org/blog/write-a-great-readme-for-your-github-project) lehet olvasni.
- `requirements*.txt`: Ezekben vannak felsorolva azok a python csomagok, amelyeket használunk (függőségek). A `requirements.txt` tartalmazza magának a csomagnak a függőségeit, a `requirements-dev.txt` pedig a fejlesztéshez szükséges függőségeket (tesztelés, linter, stb).
- `setup.py`: Ez a fájl tartalmazza csomagoláshoz kellő metaadatokat.

## 3. Környezet

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

## 4. Az `__init__.py`

Az `__init__.py` lehet üres is, de ekkor is léteznie kell. Ha nem üres, akkor
a csomag importálásánál a tartalma végrehajtódik. Szokás metaadatok és az API
meghatározására használni.

*Metaadatok*: Kisebb projekteknél itt lehet felsorolni a csomag szerzőit,
verzióját, licencét, megadni email-címet, karbantartót, hálát kifejezni a
hozzájárulóknak, stb. Részletek [itt](https://stackoverflow.com/a/1523456). A
verziót érdemes külön fájlban tartani, l. alább a *Verzió* fejezetet.

*API*: Alapesetben ha használni szeretnénk egy importált csomag egy függvényét,
akkor azt így tudjuk hívni: `csomag.[alcsomag.]fájl.függvény()`. Ebből a
`csomag` és a `függvény` elhagyhatatlan, de az `alcsomag` és a `fájl`
általában felesleges. A felhasználónak csak azt kellene megjegyeznie, hogy melyik
függvény melyik csomagban van, azt nem, hogy melyik csomag melyik
fájljában van. Ráadásul a csomag írói is szeretik a kódot rugalmasan
átszervezni a háttérben, pl. egy nagyra nőtt fájl egy részét egy új fájlba
írni anélkül, hogy eltörnék az *API*-t.

Mivel az `__init__.py`-ban található kód importáláskor végrehajtódik,
ezért érdemes itt importálni a publikusnak szánt függvényeket, osztályokat, ezzel a csomag importálásakor ezek az objektumok is közvetlenül használhatók lesznek. Példa:

```py
# mypackage/__init__.py
from file1 import function1, function2
from file2 import function3
```

Ezután a használat egyszerű:

```py
import mypackage
mypackage.function1()
```

*Megjegyzés*: Ha az `__init__.py`-ban csillaggal importálunk (`from file import *`), akkor az alulvonással kezdődő objektumok nem kerülnek importálásra (a teljes elérési útjukon keresztül továbbra is elérhetőek lesznek). Példa:

```py
# file1
public_var = 10
_private_var = 20
```

```py
# mypackage/__init__.py
from file1 import *
```

```py
import mypackage
print(mypackage.public_var) # OK
print(mypackage._private_var) # NameError: "name '_public_var' is not defined"
print(mypackage.file1._private_var) # OK
```

## 5. A `setup.py` fájl

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
- `packages`: Itt adható meg, hol keresse a python fájlokat. Érdemes a *setuptools* `find_packages()` függvényére bízni a dolgot. Az `exclude=[dir1, dir2, ...]` paraméternek megadott könyvtárakban nem fog keresni.
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

## 6. További lehetőségek

### 6.1. Verzió

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

### 6.2. Fájlok hozzáadása

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

### 6.3. Parancssori futtatás

Ha csomagunkat a `pip install hellopypa` után nem csak importálva, de parancssori alkalmazásként is szeretnénk használni, akkor két dolgot tehetünk.

1. Egy python csomag futtatható az `-m` kapcsolóval, pl. `python -m hellopypa`. Ehhez az kell, hogy a csomagban legyen egy `__main__.py` fájl, a python ezt fogja keresni és ha létezik, akkor futtatni. Részletek (nem mintha nagyon lennének) [itt](https://docs.python.org/3/library/__main__.html).
2. Egy python csomag futtatható rendes, telepített parancsként is (`hellopypa`). Ekkor a *setup.py*-ban meg kell adni egy úgynevezett belépési pontot, konkrétan egy függvényt, amit meg fog hívni a python. Részletek [itt](https://setuptools.readthedocs.io/en/latest/pkg_resources.html#entry-points). Példa:

    ```py
    # ...
    setuptools.setup(
        # ...
        entry_points={
            "console_scripts": [
                "hellopypa=hellopypa.__main__:main",
            ]
        },
        # ...
    )
    # ...
    ```

## 4. Tesztelés

Mielőtt csomagolnánk, teszteljük le az alkalmazásunkat. A teszteléshez a [pytest](https://docs.pytest.org/en/latest/)-et használjunk. A `test/` könyvtárban vannak a tesztfájlok, ezeket a következő paranccsal futtathatjuk:

```sh
pytest --verbose test/
```

Megjegyzés: a `test/` könyvtár maga is csomag, kell benne lennie `__init__.py` fájlnak.

## TODO

- [x] Bevezetés: modul, csomag, pypi
- [x] Könyvtárszerkezet
- [x] Környezet
- [x] Tesztelés
- [ ] Dokumentáció
- [x] A `setup.py` fájl
- [x] A `MANIFEST.in` fájl
- [x] `__main__.py`, CLI
- [x] `__init__.py`, API
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
