# protocole de communication graphique
Un outil de communication graphique, qui permet de coder une chaine de caractère sous forme d'un code graphique telle que chaque lettre de cette chaine est codée juste sur 6 bits au lieu de 8. 
On a utilisé le code de hamming pour que dans le cas ou quelqu'un veut bosser sur la lecture du code graphique (décodage), et au le cas où il y a une erreur de lecture d'un pixil au plus, tu récupere le code de base grâce à l'lagorithme de hamming.
Exécution du programme:
Après le clonage du projet avec la commande:
git clone https://github.com/elandaloussiayoub/qrcode
positionez vous dedans le dossier qrcode en tapant la commande:
cd qrcode
par la suite éxecutez le fichier code en tapant:
python3 qr_v2.py
et voilà vous aurez votre code graphique représentant la chaine de caractère que vous voulez :D
