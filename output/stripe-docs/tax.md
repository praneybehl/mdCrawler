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
# Stripe Tax
## Automatisez votre conformité en matière de taxe sur les ventes, de TVA et de TPS sur toutes vos transactions, avec une intégration sans code ou nécessitant peu de code.
Vous pouvez intégrer Stripe Tax à Payment Links Payment Links ou l’API Checkout Sessions et l’utiliser pour vos abonnements et vos factures. Vous pouvez également créer des tunnels de paiement personnalisés ou intégrer Stripe Tax en tant que plateforme à Connect.
Si vous travaillez pour une plateforme qui vous paie via Stripe, vous avez besoin d’un formulaire 1099 pour effectuer vos déclarations fiscales. Consultez le site de support pour en savoir plus sur la vérification de vos informations fiscales et la réception de vos formulaires.
## Fonctionnement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Configurer Stripe Tax
Pour commencer, configurez vos paramètres fiscaux dans le Dashboard en quelques étapes.
Suivre vos obligations fiscales
Immatriculez-vous pour collecter des taxes gratuitement au moment de commencer à traiter des paiements.
Gérez votre conformité
Comment Tax s’intègre à vos objectifs de conformité.
Calculer les taxes automatiquement
Découvrez comment Stripe Tax calcule les taxes.
TAX
API Stripe Tax pour personnaliser vos tunnels de paiement
Calculez et déclarez les taxes sur tous les paiements, même ceux traités en dehors du réseau Stripe.
Fonctionnement
![](https://b.stripecdn.com/docs-statics-srv/assets/tax_api_transparent.958dd19b740d048f9e2b8b0d1986e671.png)
## Ajouter Stripe Tax à vos intégrations![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Configurer des Payment Links
Ajoutez Stripe Tax à vos Payment Links via un simple clic.
Configurer le paiement
Intégrez Stripe Tax avec vos paiements Checkout.
Configurer des abonnements
Avec des cycles de facturation, des périodes d’essai, des plans au prorata et la taxe.
Configurer des factures
Avec ou sans code, calculer la taxe et envoyer des factures à intervalles réguliers.
Configurer des paiements personnalisés
Calculez et collectez les taxes dues pour tous les paiements grâce à notre API flexible.
Intégrer avec Connect
Activez Stripe Tax pour votre plateforme et vos comptes connectés.
## En savoir plus sur la conformité fiscale![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Guides Stripe consacrés à la conformité des taxes indirectes
Consultez nos guides pour en savoir plus sur la conformité fiscale.
Déterminer la localisation des clients
Découvrez comment Stripe Tax détermine la localisation d’un client à partir de différentes informations saisies.
## Autres fonctionnalités fiscales![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Atlas
En savoir plus sur le traitement de l’impôt sur les bénéfices des sociétés et de l’impôt de franchise.
Formulaires 1099
Explorer la solution de Stripe relative à l’impôt sur les bénéfices de Stripe pour les plateformes aux États-Unis.
Taux de taxe
Créer et gérer vos propres taux de taxe et les appliquer aux produits.
## Fonctionnalités![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Calcul automatique des taxesCalculez instantanément la taxe de vente, la TVA et la TPS pour les transactions dans le monde entier, et déterminez les taux de taxe en fonction de la localisation des clients et de l’entreprise.
  * Codes de taxe sur les produitsClassez vos produits et services par catégorie pour assurer le bon traitement des taxes.
  * Prise en charge de plusieurs paysGérez le calcul des taxes pour les ventes internationales et les transactions transfrontalières.
  * Gérer les immatriculations fiscalesGérez vos immatriculations fiscales à partir d’un seul système dans le Dashboard Stripe.


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

