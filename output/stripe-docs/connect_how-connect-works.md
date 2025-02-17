Accéder directement au contenu
Fonctionnement de Connect
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
Aperçu
Démarrer avec Connect
Fonctionnement de Connect
Concevoir une intégration
Migrer vers les propriétés du contrôleur de comptes
Prochaines modifications des exigences
Guide de démarrage rapide sur l'inscription des utilisateurs


Principes de base de l'intégration
Exemples d'intégration
Inscrire des comptes
Configurer les dashboards des comptes
Accepter des paiements
Effectuer des virements vers des comptes
Gérer votre plateforme Connect
Formulaires fiscaux pour votre plateforme Connect
Utiliser les types de comptes connectés
Intégration avec Accounts v2
Canada
Français (France)
AccueilPlateformes et places de marchéGet started with Connect
# Fonctionnement de Connect
## Découvrez comment les fonctionnalités de Connect prennent en charge les intégrations multipartites.
Les entreprises telles que les places de marché et les plateformes logicielles utilisent Connect pour gérer et acheminer les paiements et les virements entre les marchands, les clients, les fournisseurs de services et d’autres entités.
  * **Inscription des utilisateurs** : inscrivez et vérifiez des marchands en utilisant des comptes connectés avec des flux hébergés par Stripe, ou créez les vôtres avec nos API.
  * **Gestion de compte** : offrez aux marchands la possibilité de gérer leur compte avec des Dashboards hébergés par Stripe, des composants intégrés ou des interfaces personnalisées que vous pouvez créer avec nos API.
  * **Paiements** : intégrez les paiements et acheminez-les vers les marchands sur votre plateforme.
  * **Virements** : payez les marchands avec une variété d’options de paiement. Activez les virements transfrontaliers pour les marchands internationaux.
  * **Outils de plateforme** : gérez votre plateforme ou place de marché avec une suite sophistiquée d’outils de plateforme pour la monétisation, l’assistance aux marchands, la gestion des risques et les déclarations fiscales.


### Pays concernés![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## Éléments d’une intégration Connect![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Une intégration Connect inclut cinq éléments principaux :
  * L’application Web ou mobile de votre plateforme
  * Le compte Stripe de votre plateforme
  * Les comptes connectés
  * Les paiements Stripe
  * Les virements Stripe


Lors de l’inscription des utilisateurs à Connect, vous créez une application Connect sur le compte Stripe de votre plateforme. L’application Connect vous permet de créer et d’accéder aux données de vos comptes connectés. Vous utilisez vos clés API Stripe pour effectuer des demandes d’API au nom de vos comptes connectés.
![Une vue d'ensemble des interactions entre une plateforme Connect, les clients et les comptes connectés](https://b.stripecdn.com/docs-statics-srv/assets/connect-overview.c6c7d0fac01a655bc51523add1eecd21.png)
Connect offre un certain nombre d’options différentes pour l’inscription des comptes connectés et la création de paiements et de virements. En donnant à vos utilisateurs l’accès aux Dashboards hébergés par Stripe et aux composants intégrés, vous pouvez personnaliser leurs flux financiers tout en réduisant au maximum vos efforts de développement et les délais requis pour vous lancer.
Les types de paiements Connect offrent différentes façons d’orchestrer les paiements sur vos comptes connectés, qu’il s’agisse de leur permettre d’accepter directement les paiements ou de faciliter les paiements entre plusieurs marchands. Les virements Connect vous permettent de gérer les délais de paiement, les comptes de virements de destination et la monétisation des virements sur vos comptes connectés.
## Cas d’usage![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Connect est très flexible et est conçu pour prendre en charge de nombreux cas d’usage à destination de plusieurs bénéficiaires :
  * **Plateformes SaaS** : permettent aux comptes connectés d’accepter directement des paiements. Les plateformes telles que Squarespace permettent aux entreprises de créer leurs propres boutiques en ligne pour vendre directement aux clients.
  * **Places de marché** : collectent les paiements et effectuent des virement vers plusieurs marchands. Les plateformes telles qu’Airbnb mettent en relation les propriétaires et les hôtes potentiels.
  * **Recharge et virement** : faites des virements à des comptes sans accepter de paiements. Ajoutez des fonds au compte de votre plateforme, puis transférez des fonds à vos comptes connectés sans traiter les paiements sur Stripe.
  * **Paiements par TPE** : ajoutez Stripe Terminal à votre intégration à destination de plusieurs bénéficiaires. Offrez à vos comptes connectés la possibilité d’accepter des paiements par TPE en même temps que des paiements en ligne avec une seule intégration.


## Concevoir une intégration![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Afin de déterminer comment concevoir une intégration Connect pour votre cas d’usage :
  1. Complétez le processus d’inscription à la plateforme Connect ou consultez des exemples d’intégration.
  2. Après l’inscription des utilisateurs, consultez votre guide d’intégration. Ce guide est personnalisé en fonction des sélections que vous avez effectuées lors de l’inscription des utilisateurs à la plateforme.
  3. Suivez le guide d’inscription pour configurer et commencer à utiliser votre intégration.


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
Éléments d’une intégration Connect
Cas d’usage
Concevoir une intégration
Produits utilisés
Connect
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

Regardez le guide vidéo
Mini Player
