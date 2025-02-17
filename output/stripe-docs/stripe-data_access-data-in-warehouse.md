Accéder directement au contenu
Accéder aux données de votre entrepôt de données avec Data Pipeline
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
Rapports
Données
Présentation
Démarrer
Access Stripe data using Sigma
Accéder aux données de votre entrepôt de données avec Data Pipeline
Exporter des données vers votre entrepôt de données
Exporter les données vers votre Cloud Storage
Actualisation des données
Importer et gérer des données
Interroger des données
Écrire des requêtes
Interroger des données transactionnelles
Faire une recherche dans les données de litige et de fraude
Interroger des données Billing
Interroger des données fiscales
Interroger toutes les données de frais
Interroger des données Connect
Interroger des données Issuing
Interroger plusieurs comptes
Planifier des requêtes
Migrer des requêtes


Constitution de start-up
Canada
Français (France)
AccueilAutomatisation des opérations financièresData
# Accéder aux données de votre entrepôt de données avec Data Pipeline
## Synchronisez votre compte Stripe avec Snowflake, Amazon Redshift, Google Cloud Storage et d'autres services de stockage de données.
Data Pipeline est un produit sans code qui envoie l’ensemble de vos données Stripe vers une multitude de destinations de stockage de données. Cela vous permet de centraliser vos données Stripe avec d’autres données commerciales pour clôturer vos comptes et bénéficier d’informations plus détaillées.
Grâce à Data Pipeline, vous pouvez :
  * Exporter automatiquement la totalité de vos données Stripe en toute sécurité et rapidité.
  * Cesser de vous appuyer sur des pipelines d’extraction, de transformation et de chargement (ETL) tiers ou sur des intégrations d’API préconfigurées.
  * Combiner les données de tous vos comptes Stripe dans un seul entrepôt de données.
  * Intégrer les données Stripe aux autres données de votre entreprise pour obtenir des analyses commerciales plus complètes.


#### Mise en garde
Stripe ne propose pas les services de Data Pipeline aux clients, entreprises et utilisateurs en Inde en raison des exigences de localisation des données.
#### Remarque
Si vous avez des questions concernant la prise en charge de votre destination de données, contactez-nous à l’adresse data-pipeline@stripe.com.
## Prise en charge des destinations![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe Data Pipeline prend en charge deux types de destinations.
  * Entrepôts de données (Snowflake, Amazon Redshift)
    * Pour les destinations d’entrepôt de données, Stripe envoie un partage de données à votre entrepôt de données.
    * Une fois que vous avez accepté le partage de données, vous pouvez accéder à vos données Stripe principales dans Snowflake ou Amazon Redshift sous 12 heures.
    * Après le chargement initial, vos données Stripe sont mises à jour régulièrement, et vous obtenez de nouvelles données toutes les 3 heures par le biais du chargement incrémentiel ou complet.
  * Cloud Storage (Google Cloud Storage, Azure Blob Storage)
    * Pour nos destinations de stockage dans le cloud, Stripe envoie les fichiers Parquet directement à l’un de vos emplacements de stockage dans le cloud.
    * Après le chargement initial, vos données Stripe sont mises à jour régulièrement, et vous obtenez de nouvelles données toutes les 6 heures.


## Schémas de base de données![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Les données de votre entrepôt sont divisées en deux schémas de base de données, en fonction du mode d’API utilisé pour créer les données.
Nom du schéma| Description  
---|---  
`STRIPE`| Données renseignées par le mode production  
`STRIPE_TESTMODE`| Données renseignées par le mode test  
## Entrepôt de données utilisé par plusieurs comptes Stripe![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Si vous partagez les données de plusieurs comptes Stripe avec un même entrepôt de données, vous pouvez les identifier séparément. Chaque tableau comporte une colonne `merchant_id`, qui vous permet de filtrer les données par compte.
## Exemple de cas d’usage![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Dans certains cas, vous pouvez souhaiter regrouper les informations issues de vos données propriétaires avec les données de Stripe. Le schéma qui suit expose une table `orders` qui liste les informations à propos d’une commande pour une entreprise :
date| order_no| stripe_txn_no| customer_name| tarif| articles  
---|---|---|---|---|---  
17/02/2025| 1| bt_xcVXgHcBfi83m94| Jean Durand| 5| 1 livre  
Le tableau ci-dessus ne contient pas les données relatives aux frais de transaction ou aux virements, car ces données sont uniquement disponibles dans Stripe. Dans Stripe, le tableau `balance_transactions` contient les informations suivantes, mais les données propriétaires concernant les noms des clients et les articles achetés n’y figurent pas :
id| montant| available_on| frais| net| automatic_transfer_id  
---|---|---|---|---|---  
bt_xcVXgHcBfi83m94| 500| 17/02/2025| 50| 450| po_rC4ocAkjGy8zl3j  
Pour accéder à vos données propriétaires en même temps qu’à vos données Stripe, associez le tableau `orders` au tableau `balance_transactions` de Stripe :
```

select
 orders.date,
 orders.order_no,
 orders.stripe_txn_no,
 bts.amount,
 bts.fee,
 bts.automatic_transfer_id
from mycompany.orders join stripe.balance_transactions bts
on orders.stripe_txn_no = bts.id;

```

Une fois l’opération terminée, les informations suivantes sont disponibles :
date| order_no| Stripe_txn_no| montant| frais| automatic_transfer_id  
---|---|---|---|---|---  
17/02/2025| 1| bt_xcVXgHcBfi83m94| 500| 50| po_rC4ocAkjGy8zl3j  
### Jeux de données![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez consulter la liste des ensembles de données disponibles dans la section **Ensembles de données ** de la documentation consacrée aux schémas du Dashboard. Les ensembles de données disponibles peuvent varier en fonction de la région, et dépendent de la disponibilité et des réglementations locales. Data Pipeline partage séparément chaque ensemble de données, qui contient une ou plusieurs tables d’entrepôt de données, chaque fois que de nouvelles données sont disponibles. Data Pipeline met à jour différentes tables à différentes fréquences, en fonction de la disponibilité des nouvelles données. Pour en savoir plus sur les ensembles de données disponibles et les fréquences d’actualisation, consultez la documentation consacrée à l’actualisation des données.
## Notifications par e-mail![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez également vous abonner pour recevoir des notifications par e-mail pour les mises à jour importantes dans le Dashboard.
## Désactiver Data Pipeline![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez désactiver Data Pipeline sur la page des paramètres du Dashboard en cliquant sur **Désactiver**. Après la déconnexion, vous perdrez immédiatement l’accès à vos données partagées.
## Vous souhaitez utiliser Data Pipeline pour un entrepôt de données que nous ne prenons pas encore en charge ?
Nous recherchons des utilisateurs susceptibles de participer à notre programme Alpha limité pour l'obtention d'entrepôts de données supplémentaires. Si vous souhaitez rejoindre la liste d'attente, veuillez saisir votre adresse e-mail ci-dessous. Notre équipe vous contactera sous peu.
Collect Email
S'inscrire
Consultez notre politique de confidentialité.
### Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Interroger des données de transaction
  * Interroger des données Billing
  * Sigma et Data Pipeline pour les plateformes Connect
  * Interroger des données Issuing
  * Interroger toutes les données de frais


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
Prise en charge des destinations
Schémas de base de données
Entrepôt de données utilisé par plusieurs comptes Stripe
Exemple de cas d’usage
Jeux de données
Notifications par e-mail
Désactiver Data Pipeline
Voir aussi
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

