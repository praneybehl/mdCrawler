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
Web Elements
Elements intégrés à l'application
Scénarios de paiement
Tunnels de paiement personnalisés
Acquisition flexible
Paiements par TPE
Terminal
Autres produits Stripe
Financial Connections
Présentation
Démarrer
Cas d'usage
Principes de base
Tests
Établissements pris en charge
Collecter des comptes pour obtenir des données
Paiements par prélèvement automatique ACH
Virements Connect
Autres produits reposant sur les données
Accéder aux données des comptes
Soldes
Propriété
Transactions
Gérer les comptes
Déconnexions
Webhooks


Cryptomonnaies
Climate
Payout Links
Canada
Français (France)
AccueilPaiementsFinancial Connections
# Stripe Financial Connections
## Accédez aux données autorisées des comptes financiers de vos utilisateurs.
Stripe Financial Connections permet aux utilisateurs de partager leurs données financières avec votre entreprise en toute sécurité. Une seule intégration vous permet de vérifier instantanément les comptes bancaires pour les paiements ACH, d’améliorer l’évaluation des risques grâce aux données relatives aux soldes, de réduire les risques en vérifiant les informations du titulaire d’un compte, et de créer de nouveaux produits fintech à partir des données de transactions.
Financial Connections enables your users to connect their accounts in fewer steps with Link, allowing them to save and quickly reuse their bank account details across Stripe businesses.
Demo loading...
## Disponibilité![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Financial Connections peut être utilisé par les entreprises établies dans les pays suivants avec des comptes bancaires américains.
Allemagne
Autriche
Belgique
Bulgarie
Chypre
Croatie
Danemark
Espagne
Estonie
États-Unis
Finlande
France
Gibraltar
Grèce
Hongrie
Irlande
Islande
Italie
Lettonie
Liechtenstein
Lituanie
Luxembourg
Malte
Monaco
Norvège
Pays-Bas
Pologne
Portugal
République tchèque
Roumanie
Royaume-Uni
Saint-Marin
Slovaquie
Slovénie
Suède
Suisse
## Cas d’usage![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Paiements ACH
Collectez un compte bancaire pour les paiements par prélèvement automatique ACH et exploitez les données du compte, dont les soldes.
Virements Connect
Collectez les coordonnées bancaires à utiliser pour les virements Connect et exploitez les données du compte, comme les informations relatives au titulaire du compte, avec votre intégration.
Produits alimentés par les données
Collectez les comptes des utilisateurs et accédez à leurs données pour créer des intégrations plus complexes, comme des applications de services financiers pour particuliers.
## Types de données pris en charge![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Soldes
Accédez au solde actuel et au solde disponible d’un compte.
Propriété
Accédez aux noms et adresses postales des titulaires de compte.
Transactions
Accédez à l’historique des transactions d’un compte.
## En savoir plus![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Principes de base
Découvrez le fonctionnement de Financial Connections.
Cas d'usage
Obtenez des informations plus détaillées sur les principaux cas d’usage de Financial Connections.
Tests
Testez votre intégration Financial Connections.
Webhooks
Recevez des notifications en cas d’activité.
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
Disponibilité
Cas d’usage
Types de données pris en charge
En savoir plus
Produits utilisés
Financial Connections
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

