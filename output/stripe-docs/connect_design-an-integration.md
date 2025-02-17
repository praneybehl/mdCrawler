Accéder directement au contenu
Concevoir une intégration
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
# Guide d'intégration Connect
## Développez votre intégration en fonction de vos choix en matière d'inscription, de Dashboards et de types de paiement.
Utilisez ce guide pour explorer différentes intégrations Connect, faire des choix et accéder à un guide d’intégration personnalisé. Avant de démarrer votre intégration en mode test, vous devez :
  * Créer un compte Stripe
  * Commencer à compléter le profil de votre plateforme


## Sélectionner les propriétés![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
### Créer et inscrire des comptes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe vous permet de créer des comptes au nom des utilisateurs, appelés comptes connectés. Lorsque vous utilisez Connect, vous devez créer un compte connecté pour chaque utilisateur recevant des fonds sur votre plateforme.
Inscription des utilisateurs :
Inscription des utilisateurs :
Hébergé
Intégré
API
Envoyez vos comptes connectés vers un flux d’inscription hébergée par Stripe. L’inscription hébergée par Stripe vous permet de rediriger votre utilisateur vers Stripe pour terminer le processus d’inscription dans une interface co-marquée.
![Capture d'écran du formulaire Connect Onboarding](https://b.stripecdn.com/docs-statics-srv/assets/Kavholm-Seamless-Standard.78b64d90c0bf87130c8b6ba1ef53df7f.png)
Idéal pour un lancement rapide avec un minimum d’efforts d’intégration :
  * Les comptes connectés quittent votre site et sont redirigés vers Stripe pour terminer le flux.
  * Co-marquage avec Stripe et options de personnalisation limitées.
  * Stripe gère toute la logique du flux d’inscription.
  * Prend automatiquement en charge plus de 46 pays et 14 langues.


### Mise en place des flux du tableau de bord![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Les comptes connectés doivent avoir accès à un tableau de bord pour gérer leur compte. Fournissez aux comptes connectés un accès au Dashboard Stripe, au Dashboard Express ou à un tableau de bord créé à l’aide de l’API Stripe et de composants intégrés. 
Accès au Dashboard :
Accès au Dashboard :
Stripe
Express
Aucun
Donnez accès au Dashboard Stripe aux comptes connectés.
Le Dashboard Stripe offre aux comptes connectés un ensemble complet de fonctionnalités, y compris la consultation des paiements, la gestion des remboursements et des litiges, l’accès aux rapports et le traitement des paiements de manière autonome. Les utilisateurs peuvent se connecter à leur Dashboard Stripe à tout moment et y accéder directement depuis le site de Stripe. Les utilisateurs ont accès au service Support de Stripe, et Stripe peut les contacter et communiquer avec eux au sujet de leur compte.
Utilisez le Dashboard Stripe lorsque :
  * Vos utilisateurs doivent avoir accès à de puissants flux de paiements et à des fonctions avancées de gestion des utilisateurs.
  * Vous préférez que Stripe gère le risque de perte et prenne la responsabilité des soldes négatifs sur les comptes connectés.
  * Vous êtes à l’aise avec le marquage Stripe et le co-marquage limité de la plateforme.


You can always add embedded components to your own website in tandem with providing access to the Stripe Dashboard.
### Accepter un paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous créez un paiement pour accepter un paiement d’un client au nom de votre compte connecté. Le type de paiement que vous créez :
  * Détermine la répartition des fonds de paiement entre toutes les parties concernées
  * A une incidence sur la façon dont les frais apparaissent sur le relevé bancaire ou de facturation du client (avec les informations de votre plateforme ou celles de votre utilisateur)
  * Détermine le compte Stripe débité du coût des remboursements et des contestations de paiement


Type de paiement :
Type de paiement :
Paiements directs
Paiements indirects
Paiements et transferts distincts
Un paiement direct est un paiement effectué par un client directement sur un compte connecté. Les clients effectuent des transactions directement avec votre compte connecté, souvent sans connaître l’existence de votre plateforme.
Ce type de paiement est le mieux adapté aux plateformes SaaS. Par exemple, Shopify fournit des outils pour créer des vitrines en ligne et Thinkific permet aux enseignants de vendre des cours en ligne.
### Frais Stripe![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Modèle économique :
Modèle économique :
Vos comptes connectés
Votre plateforme
Stripe collecte les frais Stripe directement depuis vos comptes connectés. Vous pouvez prélever une commission de la plateforme facultative lorsque vous créez le paiement direct.
Client
Compte connecté
Paiement de 10 $
(1,23 $) Commission de la plateforme
Commission de la plateforme de 1,23 $
Plateforme
(0,59 $) Frais Stripe
8,18 $ net
Stripe
Paiement direct
### Envoyer des virements aux utilisateurs![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Lorsque les fonds issus du paiement sont versés et que le compte connecté de votre utilisateur a un solde Stripe positif, vous pouvez virer ces fonds sur son compte externe.
Par défaut, les fonds qui ont été versés sur les soldes de vos comptes connectés sont virés quotidiennement par Stripe. Si vous le souhaitez, vous pouvez configurer différentes fréquences de virement automatique, déclencher des virements manuellement plutôt qu’automatiquement, ou encore effectuer des virements instantanés.
### Responsabilité des soldes négatifs![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Responsabilité des soldes négatifs :
Responsabilité des soldes négatifs :
Stripe
Plateforme
Stripe surveille les signaux de risque sur vos comptes connectés, intervient en cas de risque et cherche à recouvrer les soldes négatifs de vos comptes connectés.
Pour la plupart des plateformes SaaS, il s’agit du meilleur choix par défaut, en particulier pour celles qui débutent dans l’intégration des paiements :
  * Stripe surveille les risques de crédit et de fraude sur vos comptes connectés et assure une protection contre les risques de perte en cas de soldes négatifs imputables à des risques commerciaux.
  * Stripe gère toutes les communications et mesures correctives de bout en bout directement avec vos comptes connectés via des flux hébergés ou des composants intégrés.


## Votre guide personnalisé![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Cette liste d’étapes est personnalisée en fonction de vos choix effectués ci-dessus. Utilisez-la pour démarrer votre intégration.
  * Utiliser le guide de démarrage rapide consacré à l'inscription des utilisateurs
Créez des comptes connectés et collectez les exigences en utilisant l'inscription des utilisateurs hébergée de Stripe. En savoir plus
  * Accepter des paiements
Créez des paiements directs. Vos comptes connectés paieront les frais Stripe. En savoir plus
  * Configurer le Dashboard Stripe
Découvrez le Dashboard Stripe et contrôlez les fonctionnalités offertes à vos comptes connectés.
  * Comprendre les responsabilités de Stripe en matière de risques pour les marchands
Comment Stripe gère les soldes négatifs sur vos comptes connectés. En savoir plus
  * Envoyer des virements aux utilisateurs
Découvrez comment contrôler les virements vers les comptes bancaires et les cartes de débit.


Propriétés
Réinitialiser
Inscription des utilisateurs
Inscription des utilisateurs :
Hébergé
Intégré
API
Accès au Dashboard
Accès au Dashboard :
Stripe
Express
Aucun
Type de paiement
Type de paiement :
Paiements directs
Paiements indirects
Paiements et transferts distincts
Qui paie les frais Stripe
Modèle économique :
Vos comptes connectés
Votre plateforme
Responsabilité des soldes négatifs
Responsabilité des soldes négatifs :
Stripe
Plateforme
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

