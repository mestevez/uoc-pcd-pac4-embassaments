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

## Documentació

## Lint
S'utilitza `pylint` per a fer l'anàlisi estàtica del codi.
Aquest està inclòs a les dependències de desenvolupament, per tant, si has instal·lat les dependències de desenvolupament, ja el tens instal·lat.
L'execució de `pylint` es pot fer sobre un fitxer o directori concret. Per exemple:
```bash
pylint src
```