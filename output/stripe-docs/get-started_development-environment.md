Accéder directement au contenu
Configurer votre environnement de développement
Créez un compte
ou 
connecter-vous
Logo de la documentation Stripe
Rechercher dans la documentation
`/`
Créez un compte
Connectez-vous
Démarrer
Paiements
Automatisation des opérations financières
Plateformes et places de marché
Services bancaires
Outils de développement
Démarrer
Paiements
Automatisation des opérations financières
Démarrer
Paiements
Automatisation des opérations financières
Plateformes et places de marché
Services bancaires
API et SDK
Aide
AperçuDécouvrir tous les produitsPhases de publication
Planifier votre intégration
Configurer Stripe
Créer un compte
Accepter un paiement
Produits et tarifs
Utiliser Stripe sans coder
Aide en matière de réglementation
Dashboard Stripe
Dashboard Web
Dashboard mobile
Pour les développeurs
Commencer le développement
Configurer votre environnement de développement
Envoyer votre première requête à l'API
Créer et tester de nouvelles fonctionnalités
Liste de contrôle pour la mise en production


Exemples de projets
À propos des API
Migrer vers Stripe
Migrer les données client
Migrer des données de paiement
Migrer des abonnements
Gérer le risque de fraude
Comprendre la fraude
Radar pour la protection contre la fraude
Gestion des litiges
Vérifier l'identité
Canada
Français (France)
AccueilDémarrerStart developing
# Configurer votre environnement de développement
## Familiarisez-vous avec l'interface de ligne de commande Stripe et nos SDK côté serveur.
Les SDK côté serveur et l’interface de ligne de commande (CLI) de Stripe vous permettent de communiquer avec les API REST de Stripe. Commencez par l’interface de commande Stripe pour rationaliser votre environnement de développement et effectuer des appels à l’API.
Utilisez les SDK pour éviter d’avoir à rédiger du code standard. Si vous souhaitez commencer à envoyer des requêtes depuis votre environnement, choisissez un langage pour consulter un guide de démarrage rapide.
Ruby
Python
Go
Java
Node.js
PHP
.NET
Dans ce guide de démarrage rapide, vous allez installer l’interface de ligne de commande Stripe, un outil essentiel qui vous fournit un accès à votre intégration Stripe via une ligne de commande. Vous allez également installer le SDK Ruby côté serveur de Stripe pour accéder aux API Stripe depuis les applications rédigées en Ruby.
## Objectifs d’apprentissage![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Dans ce guide de démarrage rapide, vous apprendrez à :
  * Appeler les API Stripe sans avoir à écrire une ligne de code
  * Gérer les dépendances tierces à l’aide d’un bundler avec RubyGems
  * Installer le dernier SDK Ruby v13.0.0 de Stripe
  * Envoyer votre première requête SDK


## Configurer l'interface de ligne de commande Stripe![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Tout d’abord, créez un compte Stripe ou connectez-vous.
### Installer![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
À partir de la ligne de commande, utilisez un script d’installation ou téléchargez et extrayez un fichier d’archive versionné pour votre système d’exploitation afin d’installer la CLI.
homebrew
apt
yum
Scoop
macOS
Linux
Windows
Docker
Pour installer la CLI Stripe avec homebrew, exécutez la commande suivante :
Command Line
```

brew install stripe/stripe-cli/stripe

```

This command fails if you run it on the Linux version of homebrew, but you can use this alternative or follow the instructions on the Linux tab.
Command Line
```

brew install stripe-cli

```

### S’identifier![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Log in and authenticate your Stripe user Account to generate a set of _restricted keys_. To learn more, see Stripe CLI keys and permissions.
Command Line
```

stripe login

```

Appuyez sur la touche **Entrée** de votre clavier pour effectuer le processus d’authentification dans votre navigateur.
Output
```

Your pairing code is: enjoy-enough-outwit-win
This pairing code verifies your authentication with Stripe.
Press Enter to open the browser or visit https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1 (^C to quit)

```

### Confirmer la configuration![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Maintenant que l’interface de ligne de commande est installée, vous pouvez effectuer une requête unique à l’API afin de créer un produit.
Command Line
```

stripe products create \
--name="My First Product"\
--description="Created with the Stripe CLI"

```

Recherchez l’identifiant produit (dans `id`) dans l’objet réponse. Conservez-le pour la prochaine étape.
Si tout a bien fonctionné, la ligne de commande affiche la réponse suivante.
```

{"id":
"prod_LTenIrmp8Q67sa"
,"object":"product",

```

Afficher les 25 lignes
Ensuite, effectuez un appel de création de tarif pour associer un tarif de 30 USD. Remplacez le paramètre substituable contenu dans `product` par l’identifiant de votre produit (par exemple, `prod_LTenIrmp8Q67sa`).
Command Line
```

stripe prices create \ --unit-amount=3000\ --currency=usd \ --product=
{{PRODUCT_ID}}

```

Si tout a bien fonctionné, la ligne de commande affiche la réponse suivante.
```

{"id":
"price_1KzlAMJJDeE9fu01WMJJr79o"
,"object":"price",

```

Afficher les 20 lignes
## Gérer les dépendances tierces![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Nous vous recommandons de gérer les dépendances tierces avec l’outil de ligne de commande RubyGems, ce qui vous permet d’ajouter de nouvelles bibliothèques et de les inclure dans vos projets Ruby. Vérifiez que RubyGems est installé :
### Installation de RubyGems![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Command Line
```

gem --version

```

Si vous obtenez `gem: command not found`, téléchargez RubyGems depuis sa page de téléchargement.
## Installer le SDK de Ruby côté serveur![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
v13.0.0 est la dernière version du SDK Stripe Ruby côté serveur. Elle prend en charge les versions 2.3 et ultérieures de Ruby.
Vérifiez votre version Ruby :
Command Line
```

ruby -v

```

### Installer la bibliothèque![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Créez un fichier gem, puis installez-le à l’aide d’un bundler à partir de RubyGems.
Ajoutez la dernière version du gem Stripe à un projet :
Command Line
```

bundle add stripe

```

Installez les fichiers gem requis à partir des sources spécifiées :
Command Line
```

bundle install

```

### Autres méthodes d'installation![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## Exécuter votre première requête SDK![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Maintenant que le SDK de Ruby est installé, vous pouvez créer un abonnement Produit et associer un tarif avec deux requêtes API. Nous utilisons l’identifiant du produit renvoyé dans la réponse pour créer le tarif dans cet exemple.
#### Remarque
Cet exemple utilise les clés par défaut de votre compte utilisateur Stripe pour le mode test. Vous êtes la seule personne à pouvoir voir ces valeurs.
create_price.rb
```

require'rubygems'require'stripe'Stripe.api_key ="sk_test_Hrs6SAopgFPF0bZXSN3f6ELN"
starter_subscription =Stripe::Product.create(
 name:'Starter Subscription',
 description:'$12/Month subscription',)
starter_subscription_price =Stripe::Price.create(
 currency:'usd',
 unit_amount:1200,
 recurring:{interval:'month'},
 product: starter_subscription['id'],)
puts "Success! Here is your starter subscription product id: #{starter_subscription.id}"
puts "Success! Here is your starter subscription price id: #{starter_subscription_price.id}"

```

Enregistrez le fichier sous `create_price.rb`. Depuis la ligne de commande, utilisez la commande `cd` pour pointer vers le répertoire contenant le fichier que vous venez d’enregistrer, puis exécutez ce qui suit :
Command Line
```

ruby create_price.rb

```

Si tout a bien fonctionné, la ligne de commande affiche la réponse suivante. Enregistrez ces identifiants afin de pouvoir les utiliser lors de la création de votre intégration.
Command Line
```

Success! Here is your starter subscription product id: prod_0KxBDl589O8KAxCG1alJgiA6
Success! Here is your starter subscription price id: price_0KxBDm589O8KAxCGMgG7scjb

```

## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Cela marque la conclusion du QuickStart. Référez-vous aux liens ci-dessous pour découvrir différents moyens de traiter un paiement pour le produit que vous venez de créer.
  * Créer un lien de paiement
  * Stripe-hosted page
  * Advanced integration


Cette page vous a-t-elle été utile ?
OuiNon
Besoin d'aide ? Contactez le service Support.
Rejoignez notre programme d'accès anticipé.
Consultez notre journal des modifications des produits.
Des questions ? Contactez l'équipe commerciale.
Propulsé par Markdoc
Inscrivez-vous pour recevoir les mises à jour destinées aux développeurs :
S'inscrire
Vous pouvez vous désabonner à tout moment. Lisez notre politique de confidentialité.
Sur cette page
Objectifs d’apprentissage
Configurer l'interface de ligne de commande Stripe
Installer
S’identifier
Confirmer la configuration
Gérer les dépendances tierces
Installation de RubyGems
Installer le SDK de Ruby côté serveur
Installer la bibliothèque
Exécuter votre première requête SDK
Voir aussi
Produits utilisés
Payments
Checkout
Stripe Shell
Test mode
API Explorer
```


Welcome to the Stripe Shell!
Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.
- View supported Stripe commands: 
stripe help ▶️

- Find webhook events: 
stripe trigger ▶️ [event]

- Listen for webhook events: 
stripe listen ▶

- Call Stripe APIs: stripe [api resource] [operation] (e.g., 
stripe customers list ▶️
)


```

Le shell Stripe est plus optimisé sur la version bureau.
```
$
```

