# Programació per a la ciència de dades - PAC4
22.403 · Programació per a la ciència de dades
Grau en Ciència de Dades Aplicada
Estudis d'Informàtica, Multimèdia i Telecomunicació

## Descripció

## Estructura del repositori

## Instal·lació

### Creació de l'entorn virtual
És recomanable crear un entorn virtual per evitar conflictes amb altres projectes.
Per això necessites tenir instal·lat `virtualenv`. Si no el tens instal·lat, pots fer-ho amb pip:
```bash
sudo pip install virtualenv
```
Després, crea un entorn virtual al directori del projecte:
```bash
virtualenv venv
```
I activa l'entorn virtual:
```bash
source venv/bin/activate
```
A partir d'aquest moment, ens trobarem dins de l'entorn virtual (observeu que el cursor de la consola canvia per indicar que ens trobem dins de l'entorn venv).

### Instal·lació de les dependències
Instal·la les dependències del projecte amb pip. És recomanable crear un entorn virtual per evitar conflictes amb altres projectes.
```bash
pip install -r requirements.txt -r dev-requirements.txt
```

## Execució

## Execució dels tests
Els tests es troben al directori `test`. 
Aquests es poden executar de manera individual, per una classe determinada:
```bash
python -m unittest test/test_main.py

```
També es poden executar les suites de test. La llista de les suites de test es troba al fitxer `test/suites.py`:
* suite_exercici1
* suite_exercici2
* suite_exercici3
* suite_exercici4
* suite_exercici5

La comanda per executar una suite de test és la següent:
```bash
python -m unittest test.suites.suite_exercici1
```

O bé es poden executar tots els tests del directori `test`:
```bash
python -m unittest
```

> Per obtenir una informació més detallada sobre els tests, podeu consultar la documentació de Python.
> [Més informació](https://docs.python.org/3/library/unittest.html).

## Documentació

## Lint
S'utilitza `pylint` per a fer l'anàlisi estàtica del codi.
Aquest està inclòs a les dependències de desenvolupament, per tant, si has instal·lat les dependències de desenvolupament, ja el tens instal·lat.
L'execució de `pylint` es pot fer sobre un fitxer o directori concret. Per exemple:
```bash
pylint src
```