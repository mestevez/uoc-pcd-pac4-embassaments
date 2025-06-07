"""
Gestió com es mostra l'ajuda per executar l'aplicació.
"""

def show_help():
    """
    Mostra un missatge d'ajuda amb les opcions disponibles.
    :return:
    """
    print("""
usage: main.py [-h] [-ex EX]

Aquesta aplicació fa un estudi de les estadístiques de la quantitat d'aigua als embassaments de les Conques internes de Catalunya.
Concretament, mostra l'evolució de la quantitat d'aigua a l'embassament de La Baells, i la seva comparació amb la mitjana dels darrers anys.

En cas de no indicar cap paràmetre, s'executaran tots els exercicis de la pràctica.

optional arguments:
  -h, --help  Mostra aquest missatge d'ajuda i surt.
  -ex 1       Executa un exercici determinat, i tots els anteriors.
    """)
