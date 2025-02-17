Accéder directement au contenu
Présentation
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
Démarrer une intégration
Produits
Émission de cartes
Treasury
Présentation
Exigences propres à Treasury
Directives pour le marketing, la conception et la conformité des produits Treasury et Issuing
Démarrer avec l'accès à l'API
Guides et exemples
Utiliser Treasury pour configurer des comptes financiers et des cartes
Utilisation de Treasury pour le transfert de fonds
Application test Issuing et Treasury
Guide d'inscription des utilisateurs finaux de la plateforme Treasury
Guide Treasury contre la fraude
Webhooks pour Stripe Issuing et Stripe Treasury
Gestion de compte
Structure des comptes de Stripe Treasury
Fonctionnement des comptes connectés
Fonctionnement des comptes financiers
Fonctionnalités des comptes financiers
Comptes financiers de plateforme
Fonctionnement des cartes Stripe Issuing
Fonctionnement des soldes et des transactions
Transférer de l'argent
Virements et recharges depuis Stripe Payments
Utilisation des SetupIntents, PaymentMethods et BankAccounts
Transfert de fonds vers un compte financier
Transfert de fonds depuis un compte financier
Délais des mouvements de fonds
Informations sur Fifth Third Bank


Financement d’entreprise
Financement Connect
Canada
Français (France)
AccueilServices bancairesTreasury
# Présentation de Stripe Treasury
## En savoir plus sur l'API Stripe Treasury.
Stripe Treasury est une API de services bancaires (BaaS) destinée aux plateformes Connect qui vous permet d’intégrer des services financiers à votre produit. Stripe fournit l’infrastructure en partenariat avec des banques de confiance.
Avec Treasury, vous pouvez permettre à vos comptes connectés de détenir des fonds, de payer des factures, de percevoir des intérêts et de gérer leurs flux de trésorerie. De nombreuses plateformes utilisent également Stripe Issuing pour émettre des cartes permettant d’accéder aux comptes Treasury.
Pour demander un accès au mode test de Treasury, remplissez le formulaire Treasury.
Les entreprises qui offrent leurs services à des entreprises commerciales établies aux États-Unis ont immédiatement accès au mode test après avoir rempli le formulaire. Toutes les autres entreprises doivent être vérifiées par Stripe qui décidera ou non de les prendre en charge. Pour en savoir plus sur les entreprises qui peuvent utiliser Treasury, consultez notre guide sur les exigences propres à Treasury.
## Composants personnalisables des services financiers![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe Treasury vous fournit les composants modulaires permettant de concevoir un produit financier complet et évolutif.
Créer des comptes
Réserve de fonds
Transférer de l'argent
Associer des cartes de paiement
Configurez vos comptes connectés en tant que clients de Treasury, vérifiez leur identité et fournissez l’accès au service des comptes financiers Treasury auprès de l’un de nos partenaires bancaires.
  * Vérification d’identité
  * Vérifications KYC
  * Contrôle des sanctions


## Cas d’usage de Treasury![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Voici quelques exemples de cas d’usage courants de Stripe Treasury :
  * **Gestion des dépenses** : créez un produit de gestion des dépenses afin que vos clients puissent stocker des fonds sur votre plateforme et gérer les dépenses effectuées avec des cartes de marque.
  * **Compte de stockage et de dépenses** : créez des comptes pouvant être garantis par la FDIC et permettant aux entreprises de stocker des fonds, de percevoir des intérêts, de déposer un chèque, ainsi que de payer des entrepreneurs et des fournisseurs par ACH et les  virements bancaires.
  * **Transfert de fonds programmatique** : simplifiez les transferts de fonds entre les comptes connectés de votre plateforme et entre les comptes connectés et des comptes tiers.


## Architecture des comptes Treasury![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Avec Stripe Connect, vous inscrivez les clients à votre plateforme en tant que comptes connectés. Vous pouvez créer un compte Treasury pour chaque compte connecté pour lui permettre d’accéder à vos produits financiers. Le schéma suivant représente une vue d’ensemble d’une plateforme ayant intégré Stripe Treasury.
![Diagramme d'une plateforme ayant intégré Treasury, montrant des clients, la plateforme, des comptes connectés et comptes financiers, des comptes bancaires externes, des cartes de paiement et des mouvements de fonds.](https://b.stripecdn.com/docs-statics-srv/assets/architecture.59cac501261250e0ebe9785c6f9701ce.png)Architecture des comptes Treasury
### Comptes connectés![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Les comptes connectés sont des marchands ou fournisseurs de services utilisant une plateforme. Par exemple, si vous êtes propriétaire d’une plateforme d’e-commerce, vous fournissez aux entreprises un cadre permettant de créer des boutiques en ligne et d’encaisser des paiements. Chaque entreprise qui utilise la plateforme d’e-commerce est un compte connecté.
Treasury prend uniquement en charge les comptes connectés qui n’utilisent pas de Dashboard hébergé par Stripe, et dont votre plateforme est responsable de la collecte des exigences et des pertes, y compris les comptes connectés Custom. Découvrez comment créer des comptes connectés qui fonctionnent avec Treasury.
#### Bêta
Enabling Treasury on non-custom connected accounts is a new feature. Email treasury-support@stripe.com to request access.
En tant que plateforme disposant de comptes connectés, vous êtes tenu(e) de maintenir une version compatible de l’API, de communiquer à vos comptes connectés les mises à jour des conditions d’utilisation de votre service, de traiter leurs demandes d’information et de leur fournir une assistance. Étant donné que votre plateforme est responsable en dernier ressort des pertes subies par vos comptes connectés, vous devez contrôler vos comptes connectés pour prévenir la fraude. Pour en savoir plus, consultez le guide Treasury sur la fraude.
### Comptes financiers![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Grâce aux endpoints Treasury de l’API Stripe, vous pouvez créer des comptes financiers et les associer à des comptes connectés dans le cadre d’une relation directe (à moins que vous ne soyez inscrit à la version bêta de la fonctionnalité Comptes financiers multiples).
Vous pouvez alimenter les comptes financiers des comptes connectés de votre plateforme, et déplacer de l’argent entre eux. Vos comptes connectés peuvent également alimenter leurs comptes financiers Treasury en utilisant une banque externe à Stripe. Si votre plateforme utilise Stripe Issuing, vous pouvez fournir des cartes de paiement liées au solde des comptes financiers de vos comptes connectés.
Les comptes financiers Treasury ont des numéros de routage, car ils sont garantis par des banques partenaires des États-Unis, et les soldes peuvent bénéficier de l’assurance transfert de la FDIC.
## Exemple d’intégration![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Suivez notre exemple d’intégration en deux parties pour découvrir le fonctionnement de Treasury :
  1. Utiliser Treasury pour configurer des comptes financiers et créer des cartes bancaires avec Issuing.
  2. Utiliser Treasury avec des SetupIntents et des PaymentMethods pour transférer de l’argent.


Stripe Treasury est fourni aux États-Unis par Stripe Payments Company, transmetteur de fonds agréé, avec des fonds étant détenus par les banques partenaires de Stripe, membres de la FDIC. Les cartes bancaires et les autres produits de crédit sont fournis par la Celtic Bank, établissement membre de la FDIC géré par Stripe, Inc. ainsi que sa société affiliée Stripe Servicing, Inc.
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
Composants personnalisables des services financiers
Cas d’usage de Treasury
Architecture des comptes Treasury
Comptes connectés
Comptes financiers
Exemple d’intégration
Produits utilisés
Treasury
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

