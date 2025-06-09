# Programació per a la ciència de dades - PAC4
22.403 · Programació per a la ciència de dades
Grau en Ciència de Dades Aplicada
Estudis d'Informàtica, Multimèdia i Telecomunicació

## Descripció
Aquesta aplicació fa un estudi de les estadistiques de la quantita d'aigua als embassaments de les Conques internes de Catalunya.
Concretament, mostra l'evolució de la quantitat d'aigua a l'embassament de La Baells, i la seva comparació amb la mitjana dels darrers anys.

## Estructura del repositori
El repositori està estructurat de la següent manera:
```
.
├── data
├── doc
├── htmlcov
├── src
│   ├── main.py
│   ├── modules
├── tests
├── venv
```
A l'arrel del repositori es troben els fitxers de configuració i dependències del projecte, com ara `requirements.txt`, `dev-requirements.txt`, `README.md`, `LICENSE`, etc.

El directori `data` conté les dades utilitzades pel projecte, que s'han descarregat del [Portal de dades obertes de la Generalitat](https://analisi.transparenciacatalunya.cat/Medi-Ambient/Quantitat-d-aigua-als-embassaments-de-les-Conques-/gn9e-3qhr/about_data).

El directori `src` conté el codi font del projecte, incloent-hi el fitxer `main.py` que és el punt d'entrada de l'aplicació, i el directori `modules` que conté els mòduls del projecte.
En aquest cas, el projecte té un mòdul per a cada exercici de la PAC4, anomenat `exercici1`, `exercici2`, etc.

El directori `tests` conté els tests del projecte, organitzats per exercicis i amb una suite de tests per a cada exercici.

El directori `doc` conté la documentació generada del projecte, i el directori `htmlcov` conté els informes de cobertura dels tests. El contingut d'aquests directoris es genera automàticament quan s'executen les comandes de test i documentació, com es veurà més endevant.

## Requisits
Per executar aquest projecte, necessites tenir instal·lat Python 3.12 o superior.
Per altre banda, és recomanable tenir instal·lat pip en la versió 25.0 o superior.

## Instal·lació

### Creació de l'entorn virtual
És recomanable crear un entorn virtual per evitar conflictes amb altres projectes.
Per això necessites tenir instal·lat `virtualenv`. Si no el tens instal·lat, pots fer-ho amb pip:
```bash
pip install virtualenv
```
Després, crea un entorn virtual al directori del projecte:
```bash
virtualenv venv
```
I activa l'entorn virtual. En Linux o Mac podeu fer-ho amb:
```bash
source venv/bin/activate
```

En Windows, l'activació es fa amb:
```bash
venv\Scripts\activate.bat
```

A partir d'aquest moment, ens trobarem dins de l'entorn virtual (observeu que el cursor de la consola canvia per indicar que ens trobem dins de l'entorn venv).

> Es recomenable verificar la versió de python dins de l'entorn virtual amb `python --version`.

### Instal·lació de les dependències
Instal·la les dependències del projecte amb pip. 
És recomanable utilitzar un entorn virtual per evitar conflictes amb altres projectes.
```bash
pip install -r requirements.txt -r dev-requirements.txt
```

## Execució
Per executar el projecte cal executar el fitxer `main.py`:
```bash
python src/main.py
```

> L'execució sense parametres executarà tots els exercicis de la PAC4.

També es pot executar un exercici concret passant-li el número de l'exercici com a paràmetre:
```bash
python src/main.py -ex 2
```
> En cas d'indicar un número d'exercici, també s'executaran tots els exercicis previs.

## Test
### Execució dels tests
Els tests es troben al directori `tests`. 
Aquests es poden executar de manera individual, per una classe determinada:
```bash
PYTHONPATH=src python -m unittest tests/test_main.py
``` 

> En Windows es pot definir la variable d'entorn `PYTHONPATH`, i després executar les comandes sense indicar-la:
```bash
SET PYTHONPATH=src

python -m unittest tests/test_main.py
``` 

També es poden executar les suites de test disponibles: 
```bash
PYTHONPATH=src python -m unittest tests.suites.suite_exercici1
```

La llista de les suites de test es troba al fitxer `tests/suites.py`:
* suite_exercici1
* suite_exercici2
* suite_exercici3
* suite_exercici4
* suite_exercici5

Finalment, es poden executar tots els tests del directori `test`:
```bash
PYTHONPATH=src python -m unittest
```

> Per obtenir una informació més detallada sobre els tests, podeu consultar la documentació de Python.
> [Més informació](https://docs.python.org/3/library/unittest.html).

### Cobertura dels tests
Per comprovar la cobertura dels tests, s'utilitza `coverage.py`.
Aquesta llibreria està inclòsa a les dependències de desenvolupament, per tant, si has instal·lat les dependències de desenvolupament, ja la tens instal·lada.
Per executar-lo, es pot utilitzar qualsevol de les comandes de test mencionades anteriorment, 
però substituint `python` per `coverage run`. Per exemple:
```bash
PYTHONPATH=src coverage run -m unittest
```

Per veure el resultat de la cobertura, s'ha d'executar la següent comanda:
```bash
coverage report -m
```

També es pot generar un informe en format HTML per a una visualització més amigable:
```bash
coverage html
```

L'informe de la cobertura es generarà al directori `htmlcov`, i es pot visualitzar obrint el fitxer `index.html` al navegador.

## Documentació
Per generar la documentació del projecte, s'utilitza `pdoc`.
Aquesta llibreria està inclosa a les dependències de desenvolupament, per tant, si has instal·lat les dependències de desenvolupament, ja la tens instal·lada.

Per generar la documentació, executa la següent comanda:
```bash
PYTHONPATH=src pdoc src/** -o ./doc
```

La documentació es generarà al directori `docs`, i es pot visualitzar obrint el fitxer `index.html` al navegador.

## Lint
S'utilitza `pylint` per a fer l'anàlisi estàtica del codi.
Aquest està inclòs a les dependències de desenvolupament, per tant, si has instal·lat les dependències de desenvolupament, ja el tens instal·lat.
L'execució de `pylint` es pot fer sobre un fitxer o directori concret. Per exemple:
```bash
PYTHONPATH=src pylint src
```

## Generació del codi distribuïble
Gràcies a la definició del fitxer `setup.py`, es pot generar un paquet distribuïble del projecte.
Per fer-ho, cal executar la següent comanda:
```bash
python setup.py sdist bdist_wheel
```

Això generarà un paquet distribuïble al directori `dist`, que es pot instal·lar amb pip:
```bash
pip install dist/uoc_pcd_pac4_embassaments-0.1.0-py3-none-any.whl
```