Accéder directement au contenu
Types de comptes connectés
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
Principes de base de l'intégration
Exemples d'intégration
Inscrire des comptes
Configurer les dashboards des comptes
Accepter des paiements
Effectuer des virements vers des comptes
Gérer votre plateforme Connect
Formulaires fiscaux pour votre plateforme Connect
Utiliser les types de comptes connectés
Types de comptes connectés
Standard
Express
Personnalisé
Moyens de paiement dynamiques


Intégration avec Accounts v2
Canada
Français (France)
AccueilPlateformes et places de marchéWork with connected account types
# Types de comptes Connect
## En savoir plus sur les anciennes configurations de comptes connectés.
Lorsque vous utilisez Connect, vous créez un compte connecté pour chaque entreprise ou personne qui s’inscrit à votre plateforme afin d’accéder à ses services. Vous pouvez configurer votre plateforme et vos comptes connectés en fonction de votre modèle économique, et répartir différentes responsabilités entre votre plateforme, Stripe et vos comptes connectés.
Si vous configurez une nouvelle plateforme Connect, consultez la section Concevoir une intégration pour en savoir plus sur la configuration des comptes connectés. Les informations de cette page concernent uniquement les types de comptes connectés moins flexibles, qui sont principalement utilisés par les plateformes existantes.
#### Remarque
Si vos comptes connectés existants ont été configurés à l’aide d’un type de compte, vous pouvez toujours migrer votre plateforme afin de prendre en charge les nouveaux comptes connectés configurés sans type. Votre plateforme peut continuer à prendre en charge vos comptes connectés existants pendant et après la migration, sans interruption.
Connect prend en charge les types de comptes suivants :
  * Standard
  * Express
  * Custom


## Choisir un type de compte![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
De nombreux facteurs entrent en jeu lors du choix d’un type de compte. L’effort d’intégration et l’expérience utilisateur sont particulièrement importants, car ils peuvent influer sur l’ampleur des ressources techniques mobilisées et vos taux de conversion. Une fois créé, vous ne pouvez pas modifier le type d’un compte connecté.
Stripe vous recommande d’utiliser les propriétés du contrôleur plutôt que les types de compte. Si vous souhaitez utiliser des types de comptes, nous vous recommandons les comptes connectés Express ou Standard, car ils nécessitent moins d’efforts d’intégration. Pour mieux contrôler vos comptes connectés, envisagez d’utiliser des comptes connectés Custom. Pour savoir quel type de compte nous recommandons pour votre entreprise, consultez le profil de votre plateforme.
Les comptes connectés Express et Custom sont soumis à des frais supplémentaires.
Standard| Express| Custom  
---|---|---  
**Effort d’intégration**|  Très faible| Faible| Élevé  
**Méthode d’intégration**|  API ou OAuth| API| API  
**Responsabilité en matière de fraude et de litige**|  Compte connecté| Plateforme| Plateforme  
**La plateforme peut-elle définir le calendrier des virements ?**|  Oui, avec les contrôles de la plateforme| Oui| Oui  
**Inscription des utilisateurs**|  Stripe| Stripe| Plateforme ou Stripe  
**Recueil d’informations d’identité**|  Stripe| Stripe| Plateforme ou Stripe  
**Le compte connecté a-t-il accès au Dashboard ?**|  Oui, intégralité du Dashboard| Oui, Dashboard Express| Non  
**Service de support aux comptes connectés assuré par**|  Plateforme et Stripe| Plateforme et Stripe| Plateforme  
**Mises à jour automatiques pour répondre à l’évolution des exigences de conformité**|  Oui| Oui| Non  
**Prise en charge de nouveaux pays sans modification de l’intégration**|  Oui| Oui| Non  
**Idéal pour les plateformes**|  Dont les comptes connectés sont des entreprises en ligne expérimentées| Tout type| Avec d’importantes ressources techniques pouvant être dédiées à une personnalisation intégrale de l’expérience en marque blanche  
Les comptes connectés Standard sont responsables de la fraude et des litiges s’ils utilisent des paiements directs, mais pas nécessairement s’ils utilisent des paiements indirects.
## Comptes connectés Express![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe prend en charges les processus d’intégration et de vérification d’identité des comptes connectés _Express_. La plateforme peut spécifier des types de paiement et définir les paramètres de paiement du compte connecté de manière programmatique. La plateforme assume la gestion des litiges et des remboursements, comme pour un compte connecté Custom.
Vos comptes connectés ont quelques interactions avec Stripe, mais leur principal interlocuteur reste votre plateforme, en particulier pour ce qui a trait à la fonctionnalité centrale de traitement des paiements. Stripe met à la disposition des titulaires de comptes connectés Express le Dashboard Express, une version allégée du Dashboard, qui leur permet de gérer leurs informations personnelles et de consulter les virements réalisés vers leur banque.
Utilisez les comptes connectés Express dans les cas suivants :
  * Vous souhaitez démarrer rapidement (en laissant Stripe se charger de l’inscription des comptes, de leur gestion et de la vérification des identités).
  * Vous souhaitez utiliser des paiements indirects ou des paiements et transferts distincts.
  * Vous souhaitez exercer un contrôle important sur les interactions avec vos comptes connectés


Exemples de plateformes pouvant utiliser des comptes connectés Express (liste non exhaustive) : place de marché de location de biens immobiliers comme Airbnb, ou service de chauffeur privé comme Lyft.
Les exigences de conformité internationale évoluent avec le temps. Avec Express, Stripe collecte de manière proactive les informations nécessaires lorsque ces exigences changent. Pour prendre connaissance des bonnes pratiques en termes de communication avec les comptes connectés dans ce cas de figure, consultez le guide des comptes Express.
### Disponibilité des comptes connectés Express![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Lorsque vous créez un compte connecté Express, sélectionnez l’un des pays disponibles. Vous ne pourrez pas modifier ce pays par la suite.
Certains pays ne sont disponibles que pour les comptes utilisant les virements internationaux.
Pour savoir si les comptes connectés Express sont disponibles dans votre pays, contactez Stripe.
Afrique du Sud
Albanie
Allemagne
Antigua-et-Barbuda
Arabie saoudite
Argentine
Arménie
Australie
Autriche
Bahamas
Bahreïn
Belgique
Bénin
Bolivie
Bosnie-Herzégovine
Botswana
Brunéi Darussalam
Bulgarie
Cambodge
Canada
Chili
Chypre
Colombie
Corée du Sud
Costa Rica
Côte d’Ivoire
Danemark
Égypte
Émirats arabes unis
Équateur
Espagne
Estonie
États-Unis
Éthiopie
Finlande
France
Gambie
Ghana
Grèce
Guatemala
Guyana
Hong Kong
Hongrie
Irlande
Islande
Israël
Italie
Jamaïque
Japon
Jordanie
Kenya
Koweït
Lettonie
Lituanie
Luxembourg
Macédoine du Nord
Madagascar
Malte
Maroc
Maurice
Mexique
Moldavie
Monaco
Mongolie
Namibie
Nigéria
Norvège
Nouvelle-Zélande
Oman
Ouzbékistan
Pakistan
Panama
Paraguay
Pays-Bas
Pérou
Philippines
Pologne
Portugal
Qatar
R.A.S. chinoise de Macao
République dominicaine
République tchèque
Roumanie
Royaume-Uni
Rwanda
Sainte-Lucie
Salvador
Sénégal
Serbie
Singapour
Slovaquie
Slovénie
Sri Lanka
Suède
Suisse
Taïwan
Tanzanie
Thaïlande
Trinité-et-Tobago
Tunisie
Turquie
Uruguay
Vietnam
## Comptes connectés Standard![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Un compte connecté _standard_ est un compte Stripe classique, dont la relation à Stripe est directe, qui peut se connecter au Dashboard, et peut traiter ses paiements par lui-même.
Utilisez les comptes connectés Standard dans les cas suivants :
  * Vous souhaitez vous lancer rapidement et n’avez pas besoin d’exercer beaucoup de contrôle sur les interactions avec vos comptes connectés
  * Vous souhaitez utiliser des paiements directs.
  * Vos comptes connectés savent gérer des entreprises en ligne ou disposent déjà d’un compte Stripe
  * Vous préférez que Stripe gère la communication directe avec les comptes connectés pour les problèmes de compte (par exemple, pour demander davantage d’informations afin de procéder à la vérification d’identité)


Exemples de plateformes qui utilisent des comptes connectés Standard : les plateformes de création de boutiques comme Shopify, et les plateformes de logiciels en tant que service (SaaS), comme les services de facturation et de paiement en ligne.
Les exigences de conformité internationale évoluent avec le temps. Avec les comptes connectés Standard, Stripe collecte de manière proactive les informations nécessaires lorsque ces exigences changent. Pour prendre connaissance des bonnes pratiques en termes de communication avec les comptes connectés dans ce cas de figure, consultez le guide des comptes Standard.
#### Le pays ne peut pas être modifié
Une fois créé, vous ne pouvez plus modifier le pays d’un compte connecté Standard.
## Comptes connectés Custom![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Un compte connecté _Custom_ est presque transparent pour son titulaire. Vous, la plateforme, êtes responsable de toutes les interactions avec votre compte connecté, y compris la collecte des informations dont Stripe peut avoir besoin. Vous pouvez modifier tous les paramètres du compte, y compris le compte bancaire ou la carte de débit utilisés par les virements, par voie programmatique.
Les titulaires de compte connecté Custom n’ont pas accès au Dashboard. Stripe ne les contacte jamais directement.
Utilisez les comptes connectés Custom dans les cas suivants :
  * Vous souhaitez exercer un contrôle total sur les interactions avec vos comptes connectés
  * Vous êtes en mesure de créer l’infrastructure nécessaire pour collecter des informations sur les comptes connectés, déployer un tableau de bord personnalisé, et gérer l’assistance
  * Vous souhaitez gérer toute la communication avec vos comptes connectés, sans contact direct entre eux et Stripe


La création et la gestion de comptes connectés Custom demandent un effort d’intégration supérieur à celui des autres types de comptes. Pour en savoir plus, consultez la section dédiée à l’utilisation de Connect avec des comptes Custom.
Les exigences de conformité internationale évoluent avec le temps. Pour prendre connaissance des bonnes pratiques de communication auprès de vos comptes connectés à suivre dans ce cas de figure, consultez le guide des comptes Custom.
Si vous optez pour des comptes connectés Custom, Stripe vous recommande d’utiliser Connect Onboarding pour les comptes Custom afin de collecter les informations d’inscription et de vérification de vos comptes connectés. Vous limiterez ainsi vos efforts d’intégration et vous n’aurez pas besoin de mettre à jour votre formulaire d’inscription lorsque les exigences évolueront.
### Disponibilité des comptes connectés Custom![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Lorsque vous créez un compte connecté Custom, sélectionnez l’un des pays disponibles. Vous ne pourrez pas modifier ce pays par la suite.
Certains pays ne sont disponibles que pour les comptes utilisant les virements internationaux.
Pour recevoir une notification quand les comptes connectés Custom seront disponibles dans votre pays, veuillez contacter Stripe.
Afrique du Sud
Albanie
Allemagne
Antigua-et-Barbuda
Arabie saoudite
Argentine
Arménie
Australie
Autriche
Bahamas
Bahreïn
Belgique
Bénin
Bolivie
Bosnie-Herzégovine
Botswana
Brunéi Darussalam
Bulgarie
Cambodge
Canada
Chili
Chypre
Colombie
Corée du Sud
Costa Rica
Côte d’Ivoire
Danemark
Égypte
Émirats arabes unis
Équateur
Espagne
Estonie
États-Unis
Éthiopie
Finlande
France
Gambie
Ghana
Grèce
Guatemala
Guyana
Hong Kong
Hongrie
Irlande
Islande
Israël
Italie
Jamaïque
Japon
Jordanie
Kenya
Koweït
Lettonie
Lituanie
Luxembourg
Macédoine du Nord
Madagascar
Malte
Maroc
Maurice
Mexique
Moldavie
Monaco
Mongolie
Namibie
Nigéria
Norvège
Nouvelle-Zélande
Oman
Ouzbékistan
Pakistan
Panama
Paraguay
Pays-Bas
Pérou
Philippines
Pologne
Portugal
Qatar
R.A.S. chinoise de Macao
République dominicaine
République tchèque
Roumanie
Royaume-Uni
Rwanda
Sainte-Lucie
Salvador
Sénégal
Serbie
Singapour
Slovaquie
Slovénie
Sri Lanka
Suède
Suisse
Taïwan
Tanzanie
Thaïlande
Trinité-et-Tobago
Tunisie
Turquie
Uruguay
Vietnam
## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Comptes connectés Express
  * Comptes connectés Standard
  * Comptes connectés Custom
  * Fonctionnalités du compte


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
Choisir un type de compte
Comptes connectés Express
Disponibilité des comptes connectés Express
Comptes connectés Standard
Comptes connectés Custom
Disponibilité des comptes connectés Custom
Voir aussi
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

