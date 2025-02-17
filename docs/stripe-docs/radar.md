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
Exemples de projets
À propos des API
Migrer vers Stripe
Migrer les données client
Migrer des données de paiement
Migrer des abonnements
Gérer le risque de fraude
Comprendre la fraude
Radar pour la protection contre la fraude
Présentation
Intégration
Session Radar
Évaluation des risques
Scores Radar pour plusieurs prestataires de services de paiement
Paramètres de risque
Avis
Listes
Règles
Analyses Radar


Gestion des litiges
Vérifier l'identité
Canada
Français (France)
AccueilDémarrer
#### Remarque
Cette page n'est pas encore disponible dans cette langue. Nous faisons tout notre possible pour proposer notre documentation dans davantage de langues et nous vous fournirons la version traduite dès qu'elle sera disponible.
# Radar
## Use Stripe Radar to protect your business against fraud.
Stripe Radar provides real-time fraud protection and requires no additional development time. Radar for Fraud Teams adds customization capabilities and deeper insights and trend analysis for your business.
Radar evaluates transactions in real-time, using machine learning algorithms to assess the risk of fraud. Both pricing tiers of Radar charge a fee for each transaction it evaluates. Radar screens all types of payment attempts such as successful, declined, blocked, and flagged for review. Learn more about Radar’s features.
## Design your integration with your fraud strategy![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Set up your integration
Make sure your payment integration collects the transaction data needed for Stripe to assess fraud risk.
Radar Sessions
Use Radar Session to apply Radar protection to your non-Stripe tokenized payments.
Try out rules
Simulate fraudulent payments in test mode or perform what-if analyses for new rules.
## Use the Dashboard to understand how fraud affects your business![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
View risk evaluation results
See Radar’s risk ratings and actions.
Analyze Radar metrics
Understand fraud patterns and their impact on your business.
## Customize your fraud interventions with Radar for Fraud Teams![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Set risk score
Adjust the default threshold risk score that tells Radar to allow or block a payment.
Handle manual reviews
Review suspicious payments that need a human decision.
Create lists
Maintain lists of trusted customers to automatically allow or block charges accordingly.
Customize rules
Modify criteria that instructs Radar to allow, block, review, or request 3DS authentication.
## Features![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Machine learning-based fraud detectionAutomatically identify and block fraudulent transactions using advanced algorithms, and evaluate the risk score of each transaction.
  * Custom rules engineCreate and implement your own fraud prevention rules based on your business needs, and set up automatic responses to specific risk levels.
  * Risk insightsUnderstand the factors driving risk on every payment, and detect suspicious patterns in customer behavior across transactions and location data.
  * Direct 3D Secure integrationSeamlessly incorporate additional authentication for high-risk transactions.
  * Block lists and allow listsManage lists of high-risk or trusted users, email addresses, IP addresses, metadata, and cards.
  * Real-time monitoring View and respond to potentially fraudulent activity as it happens.


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

