
Sur Windows il faut installer python via windows store c'est la manière la plus simple de l'installer.

1) Il faut installer playwright :
python -m playwright install

2) Il faut installer les requirements :
pip install -r requirements.txt

3) Il faut lancer le script avec le URL et le nom de la docs :
python main.py https://docs.python.org/fr/3/ python-docs

Elle ira dans le dossier output/python-docs et créera un dossier pour chaque page HTML du site.