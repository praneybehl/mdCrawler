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
Billing
Tax
Présentation
Démarrer
Fonctionnement de Stripe Tax
Configurer
Parcourir le Dashboard
Utilisation de l'API Settings
Tests
Intégrer par tunnel de paiement
Payment Links
Checkout
Invoicing
Abonnements
Intégration de paiement personnalisée
Réaliser une intégration avec Stripe Connect
Présentation
Stripe Tax pour les plateformes logicielles
Stripe Tax pour les places de marché
Gérez votre conformité
Surveiller vos obligations
S'inscrire
Calculer la taxe
Rapport
Déclarer et verser
Référence fiscale
Codes de taxe produit
Pays pris en charge
FAQ


Rapports
Données
Constitution de start-up
Canada
Français (France)
AccueilAutomatisation des opérations financièresTax
# Utiliser Stripe Tax avec Connect
## Découvrez comment Stripe Tax peut aider votre plateforme et vos comptes connectés à respecter leurs obligations fiscales.
Stripe Tax prend en charge Connect en vous aidant à calculer et à collecter les taxes. Il fournit des rapports sur les transactions pour vous aider dans les déclarations fiscales de votre plateforme ou de vos comptes connectés.
Pour utiliser Stripe Tax avec Connect, vous devez d’abord **déterminer quelle entité a l’obligation de collecter et de déclarer les taxes**. L’entité redevable de la taxe peut être votre compte connecté ou vous-même, selon votre modèle économique, les réglementations (par exemple, les lois sur les places de marché aux États-Unis et dans l’Union européenne), ou les détails de la transaction, tels que le montant de la commande ou le type de marchandises vendues.
## Cas d’usage![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe Tax est conçu pour prendre en charge différents cas d’usage à destination de plusieurs bénéficiaires :
Cas d’usage| Applications| Exemples  
---|---|---  
Tax pour les plateformes logicielles| 
  * Vous êtes une plateforme SaaS qui permet à d’autres entreprises proposant des services logiciels d’atteindre leurs clients.
  * Vos _comptes connectés_ sont en charge de la collecte et du versement des taxes.

| 
  * Une plateforme de commerce électronique comme Shopify ou Squarespace, qui permet aux entreprises de créer leurs propres boutiques en ligne pour vendre directement à leurs clients.

  
Tax pour les places de marché| 
  * Vous êtes une place de marché qui met en relation des acheteurs et des marchands sur une plateforme unique, généralement par le biais de sites Web ou d’applications où les produits sont référencés par divers vendeurs tiers.
  * Votre _plateforme_ est en charge de la collecte et du versement des taxes.

| 
  * Une place de marché en ligne comme Etsy ou Amazon, qui permet d’ajouter à un même panier des biens vendus par plusieurs entreprises.

  
La distinction faite par Stripe Connect entre les plateformes SaaS et les places de marché ne correspond pas strictement à la définition fiscale des places de marché qui sont responsables de la collecte des taxes. Consultez un conseiller fiscal maîtrisant votre modèle économique pour déterminer les obligations fiscales de votre plateforme et vos comptes connectés.
## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Tax pour les plateformes
  * Tax pour les places de marché


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
Cas d’usage
Voir aussi
Produits utilisés
Tax
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

