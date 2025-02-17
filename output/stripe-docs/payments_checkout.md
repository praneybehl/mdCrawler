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
À propos des paiements Stripe
Mettre votre intégration à niveau
Analyses des paiements
Paiements en ligne
PrésentationTrouver votre cas d'usage
Use Payment Links
Créer une page de paiement
Développer une intégration avancée
Développer une intégration dans l'application
Moyens de paiement
Ajouter des moyens de paiement
Gérer les moyens de paiement
Paiement accéléré avec Link
Interfaces de paiement
Payment Links
Checkout
Présentation
Fonctionnement de Checkout


Web Elements
Elements intégrés à l'application
Scénarios de paiement
Tunnels de paiement personnalisés
Acquisition flexible
Paiements par TPE
Terminal
Autres produits Stripe
Financial Connections
Cryptomonnaies
Climate
Payout Links
Canada
Français (France)
AccueilPaiementsCheckout
# Stripe Checkout
## Créez un formulaire de paiement nécessitant peu d'écriture de code et intégrez-le à votre site ou hébergez-le sur Stripe.
Checkout est une intégration de paiement low-code qui permet de créer un formulaire personnalisable afin d’encaisser des paiements. Vous pouvez intégrer directement Checkout à votre site Web, rediriger les clients vers une page de paiement hébergée par Stripe ou créer une page de paiement personnalisée avec Stripe Elements. Cette solution prend en charge les paiements ponctuels et les abonnements, et accepte plus de 40 moyens de paiement locaux. Pour obtenir la liste complète des fonctionnalités offertes par Checkout, consultez la section Fonctionnalités intégrées et personnalisables.
En savoir plus sur Stripe Checkout
![Formulaire de paiement hébergé](https://b.stripecdn.com/docs-statics-srv/assets/checkout-hosted-hover.180c6ab2498a8c65daefb5bedae835bf.png)
Page hébergée par Stripe : le client est redirigé vers une page de paiement hébergée par Stripe lorsqu’il est prêt à effectuer l’achat. Une fois qu’il a saisi ses coordonnées bancaires sur la page de paiement et effectué la transaction, il peut être redirigé vers votre site.
![Formulaire de paiement à l’aide d’Elements avec l’API Checkout Sessions](https://b.stripecdn.com/docs-statics-srv/assets/checkout-embedded-hover.14466c835d9723cfe90b3549956c451a.png)
Formulaire intégré : le client reste sur votre site et voit s’afficher une page de paiement personnalisée lorsqu’il est prêt à effectuer l’achat. Il saisit ses informations de paiement et effectue la transaction sur la même page de votre site, sans aucune redirection requise.
![Formulaire de paiement à l’aide d’Elements avec l’API Checkout Sessions](https://b.stripecdn.com/docs-statics-srv/assets/checkout-elements-hover.bfd33fb56dc4ec8915e4ab4601799f49.png)
Embedded components: Customizable checkout page built with Stripe Elements. Customers stay on your site and are shown a customized checkout page when they’re ready to complete their purchase. The customer enters their payment details and completes the transaction on the same page in your site so they don’t need to be redirected back to your site.
## Démarrer![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Fonctionnement de Checkout
Découvrez comment ajouter une page Checkout à votre site Web et encaisser des paiements
Regarder un tutoriel vidéo
Découvrez comment implémenter les fonctionnalités de Stripe Checkout pour les entreprises d’e-commerce et proposant des abonnements.
QuickStart
Découvrez un exemple de code d’intégration avec Stripe Checkout.
Activer des moyens de paiement internationaux
Activez différents moyens de paiement Checkout via le Dashboard.
Traiter vos commandes
Découvrez comment traiter les commandes réglées par vos clients.
## Personnaliser Checkout![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Personnaliser votre intégration
Personnalisez votre image de marque, la prise en charge des langues, les polices, les politiques internes, etc.
Utiliser des domaines personnalisés
Découvrez comment connecter votre domaine personnalisé à Stripe Checkout.
Personnaliser votre page de confirmation de paiement
Affichez une page de confirmation personnalisée contenant les informations relatives à la commande de votre client.
Collecter des taxes
Collectez les taxes pour des paiements ponctuels.
Collecter des numéros fiscaux
Collectez les numéros de TVA et autres numéros fiscaux des clients avec Checkout.
Collecter des numéros de téléphone
Collectez les numéros de téléphone dans Checkout.
Factures post-paiement
Envoyez des factures à vos clients avec Stripe Checkout.
Configurer des paiements futurs
Enregistrez les données de paiement de vos clients et facturez-les ultérieurement.
## Booster vos revenus![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Mises à niveau d'abonnements
Proposez à vos clients de passer à un abonnement supérieur au moment du paiement.
Ventes croisées
Offrez à vos clients la possibilité d’acheter des produits complémentaires lors du paiement grâce aux ventes croisées.
Récupération des paniers abandonnés
Récupérez des pages Checkout abandonnées et augmentez vos revenus.
Conversion automatique des devises grâce à Adaptive Pricing
Convertissez automatiquement vos tarifs dans la devise locale de vos clients pour augmenter votre taux de conversion.
Définir des tarifs manuels pour chaque devise
Affichez les prix dans la devise locale de vos clients lors du paiement.
Analyser votre tunnel de conversion
Découvrez comment analyser le tunnel de conversion de votre page Stripe Checkout.
## Options sans code![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Grille tarifaire
Affichez une grille tarifaire sur votre site Web et redirigez directement vos clients vers Stripe Checkout.
Liens de paiement
Intégrez ou partagez un lien vers une page de paiement Stripe pour accepter des paiements sans site Web.
## Autres fonctionnalités![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajouter des réductions
Réduisez le montant facturé à un client en déduisant des bons de réduction ou des codes promotionnels du sous-total.
Facturer la livraison
Définissez des tarifs de livraison et recueillez les adresses de livraison de vos clients.
Gérer un inventaire limité avec Checkout
Découvrez comment gérer vos stocks avec des périodes d’achat limitées dans le temps.
## Essayer un exemple de projet![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Paiements ponctuels
Web · Mobile web
Abonnements
Web · Mobile web · Stripe Billing
Consulter nos exemples
## Fonctionnalités intégrées et personnalisables![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe Checkout propose les fonctionnalités suivantes :
### Fonctionnalités intégrées![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Prise en charge des portefeuilles électroniques et de Link
  * Design mobile adaptatif
  * Mise en conformité avec la SCA
  * Utilisation de CAPTCHA
  * Conformité PCI
  * Validation de carte
  * Messages d’erreur
  * Quantités ajustables
  * Collecte automatique des taxes
  * Prise en charge de nombreuses langues
  * Adaptive Pricing


### Fonctionnalités personnalisables![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Collecte des taxes
  * Adaptation à votre marque au niveau des couleurs, boutons et polices
  * Ventes croisées
  * Moyens de paiement internationaux
  * Mises à niveau d’abonnements
  * Domaines personnalisés (page hébergée par Stripe uniquement)
  * Reçus par e-mail
  * Application de réductions
  * Page de confirmation de paiement personnalisée
  * Récupération des paniers abandonnés
  * Remplissage automatique des informations de paiement avec Link
  * Collecter des numéros fiscaux
  * Collecte des informations de livraison
  * Collecter les numéros de téléphone
  * Définition de la date de début de facturation de l’abonnement


## Inscrivez-vous pour recevoir un e-mail en cas de nouvelle fonctionnalité ou mise à jour.
Indiquez votre e-mail pour recevoir des actualités sur les nouvelles fonctionnalités et la prise en charge d'un plus grand nombre de cas d'usage.
Collect Email
Recevoir les mises à jour
Consultez notre politique de confidentialité.
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

