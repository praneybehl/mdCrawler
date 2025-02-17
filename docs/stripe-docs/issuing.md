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
Présentation
Issuing dans le monde
Démarrer
Fonctionnement d'Issuing
Choisir votre offre de cartes
Personnaliser votre programme
Ajoutez des fonds à votre programme de cartes
Gérer la fraude
Cartes virtuelles
Présentation
Émettre des cartes
Cartes physiques
Présentation
Choisir votre lot physique
Commander un lot de cartes personnalisé
Créer un design
Émettre des cartes
Envoyer des cartes
Obtenir de l'aide pour les cartes en libre-service
Gérer des cartes bancaires
Portefeuilles électroniques
Cartes de remplacement
Contrôles
Contrôles des dépenses
Outils antifraude avancés
3DS
Étapes de détection de la fraude
Autorisations en temps réel
Gestion des PIN
Issuing et Elements
Gestion des tokens
L'obtention de financements
Solde
Achats
Autorisations
Transactions
Litiges
Tests
Catégories de marchands
Utilisation des distributeurs automatiques
Issuing avec Connect
Configurer une intégration pour Issuing et Connect
Mettre à jour les Conditions d'utilisation du service
Financement Connect
Comptes connectés, cartes et titulaires de carte
Intégrer l'interface utilisateur pour la gestion des cartes
Informations complémentaires
Choisir un type de titulaire de carte
Service de support dédié à Issuing et Treasury
Liste de surveillance Issuing
Recommandations pour le marketing (Europe/Royaume-Uni)
Recommandations pour la conformité des produits et du marketing (US)


Treasury
Financement d’entreprise
Financement Connect
Canada
Français (France)
AccueilServices bancairesIssuing cards
# Issuing
## Utilisez l'API Issuing de Stripe pour créer, gérer et distribuer des cartes de paiement pour votre entreprise.
Stripe Issuing vous permet de créer un programme de cartes commerciales pour vos utilisateurs sans frais d’installation. Vous pouvez créer vos propres designs de carte et approuver les transactions en temps réel. De nombreux utilisateurs utilisent Stripe Issuing conjointement à Stripe Treasury pour associer des cartes à des portefeuilles en boucle ouverte et offrir à leurs clients des options de transfert de fonds supplémentaires.
## Démarrer![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
S'inscrire
Créez un compte Stripe et accédez à Issuing.
Ajouter des fonds
Mettez des fonds à disposition dans votre solde Issuing pour vos futures dépenses par carte.
Créer des cartes
Créez des titulaires de carte et émettez des cartes virtuelles ou physiques.
Créer une plateforme
Créez des comptes connectés distincts, disposant chacun de son propre solde et ses propres cartes.
Ajouter un logo
Personnalisez vos cartes physiques avec le logo de votre entreprise.
Tester l'intégration
Simulez des achats en mode test avant de passer au mode production.
## Gérer des cartes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Définir des contrôles de dépenses
Contrôlez les dépenses en définissant des règles pour les cartes et les titulaires de cartes.
Effectuer des autorisations en temps réel
Approuvez ou refusez des demandes d’autorisation en temps réel.
Ajouter des cartes à des portefeuilles électroniques
Utilisez les cartes avec Apple Pay, Google Pay ou Samsung Pay.
Gérer des autorisations
Découvrez comment gérer les autorisations partielles et incrémentielles et les annulations d’autorisations.
Gérer des transactions
Découvrez comment gérer les remboursements et autres types de captures de transactions.
Contester des transactions
Découvrez le processus d’envoi et de suivi des litiges.
Obtenir de l'aide pour les cartes Issuing
Obtenez de l’aide pour les cartes en libre-service.
## Guides![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Comment générer des revenus en émettant des cartes
Découvrez les principes de base des revenus d’interchange, comment ils sont calculés et la manière dont Stripe peut vous aider à générer des revenus.
Introduction aux BaaS pour les plateformes SaaS
Découvrez pourquoi vous devriez intégrer des services financiers à votre produit, comment évaluer les solutions BaaS et comment Stripe peut vous y aider.
Présentation des cartes à débit différé
Découvrez les rouages de la création d’un programme de cartes à débit différé et comment Stripe peut vous y aider.
Bonnes pratiques pour la création d'une fintech
Apprenez à concevoir, fonder et développer une fintech prospère grâce aux conseils de quatre start-up.
Principes de base de la conformité des fintechs aux États-Unis
Comprendre les concepts de base de la conformité en matière de BaaS pour les fintechs aux États-Unis.
Partenariats bancaires pour l'offre de BaaS de Stripe
Gillian Wee vous explique ce que l’équipe responsable des partenariats financiers recherche chez les partenaires bancaires de Stripe.
Codes de catégorie de marchand (MCC)
Découvrez de quoi il s’agit et comment vous pouvez vous en servir pour améliorer votre programme de cartes.
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

