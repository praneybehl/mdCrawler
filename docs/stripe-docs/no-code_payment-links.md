Accéder directement au contenu
Créer des liens de paiement
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
Présentation
Trouver votre cas d'usage
Créer des liens de paiement
Créer un bouton d'achat
Envoyer des factures
Créer des abonnements
Envoyer des devis
Accepter les paiements par TPE
Effectuer des virements
Créer une grille tarifaire
Configurer le portail client


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
Gestion des litiges
Vérifier l'identité
Canada
Français (France)
AccueilDémarrerUse Stripe without code
# Créer des liens de paiement
## Acceptez rapidement des paiements pour des marchandises, des services, des abonnements, des pourboires ou des dons.
Si vous vendez vos produits et services en ligne, Payment Links offre à vos clients un moyen simple de vous payer. Créez un lien que vous pouvez partager avec tout le monde.
Type
Vendre un produit ou serviceVendre un abonnementCollecter des pourboires ou des dons
Nom
Tarif
$CA
AEDAFNALLAMDANGAOAARSAUDAWGAZNBAMBBDBDTBGNBHDBIFBMDBNDBOBBRLBSDBWPBYNBZDCADCDFCHFCLPCNYCOPCRCCVECZKDJFDKKDOPDZDEEKEGPETBEURFJDFKPGBPGELGIPGMDGNFGTQGYDHKDHNLHTGHUFIDRILSINRISKJMDJODJPYKESKGSKHRKMFKRWKWDKYDKZTLAKLBPLKRLRDLSLLTLLVLMADMDLMGAMKDMMKMNTMOPMROMURMVRMWKMXNMYRMZNNADNGNNIONOKNPRNZDOMRPABPENPGKPHPPKRPLNPYGQARRONRSDRUBRWFSARSBDSCRSEKSGDSHPSLLSOSSRDSTDSVCSZLTHBTJSTNDTOPTRYTTDTWDTZSUAHUGXUSDUYUUZSVEFVNDVUVWSTXAFXCDXOFXPFYERZARZMW
Créer votre lien de paiement
![](https://b.stripecdn.com/docs-statics-srv/assets/0bf124f94479ea72ead56c0aad4e7557.svg)
Nom de votre entreprise
Lunettes de soleil
# 0,00 $CA
![](https://b.stripecdn.com/docs-statics-srv/assets/2fc0a8c0d6698e8ecd951d3c8137aa89.svg)
![](https://b.stripecdn.com/docs-statics-srv/assets/c63e01cc65f29058b5709a0b8bcabf8b.svg)
Payment Links prend en charge plus de 30 langues et plus de 20 moyens de paiement.
## Créer un lien de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Avant de commencer, déterminez quel modèle de tarification vous convient le mieux :
  * **Produits ou abonnements** : recommandé pour les modèles e-commerce ou SaaS dans lesquels vous vendez des produits à un tarif fixe.
  * **Les clients définissent le montant à payer** : idéal pour les dons, les pourboires ou les prix libres. Ce modèle tarifaire ne prend actuellement pas en charge les paiements et dons récurrents. En savoir plus sur les conditions relatives à l’acceptation des pourboires ou des dons.


Produits ou abonnements
Les clients choisissent le montant à payer
Pour permettre à vos clients de définir le montant à payer, créez un lien de paiement en effectuant les étapes suivantes :
  1. Dans le Dashboard, ouvrez la page Liens de paiement et cliquez sur **Nouveau** (ou sur le signe plus () et sélectionnez **Lien de paiement**).
  2. Renseignez les détails de paiement.
  3. (Facultatif) Définissez un montant prédéfini.
  4. (Facultatif) Définissez les montants de paiement minimal et maximal. Par défaut, le montant de paiement maximal est de 10,000.00 CAD. Contactez le service Support pour augmenter cette limite.
  5. Cliquez sur **Créer un lien**.


## Payment Links sur mobile![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Si vous créez un produit ou un abonnement, utilisez l’application iOS Stripe Dashboard pour créer un lien de paiement sur votre appareil mobile. Dans l’application, accédez à **Paiements** > **Payment Links** afin de créer un lien de paiement (ou cliquez sur l’icône de création () et sélectionnez **Lien de paiement**). L’application iOS ne prend actuellement pas en charge la création de liens permettant à vos clients de choisir le montant à payer.
## Partager des liens de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Utilisez le Dashboard pour copier votre lien de paiement et le partager en ligne. Cliquez sur l’icône de copie située à côté d’un lien existant sur la page Payment Links, ou accédez à la page d’informations du lien de paiement. Vous pouvez partager votre lien de paiement plusieurs fois et n’importe où en ligne, notamment par les moyens suivants :
  * E-mails
  * SMS
  * Plateformes de réseaux sociaux


### Générer un code QR![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez créer un code QR pour un lien de paiement dans le Dashboard. Choisissez un lien existant sur la page **Payment Links** , ou créez un lien et cliquez sur **Code QR**. Copiez ou téléchargez une image au format PNG du code QR.
Le code QR n’expire pas. Si vous désactivez le lien de paiement associé, le code QR redirige vers une page d’expiration.
### Intégrer un bouton sur votre site![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Transformez votre lien de paiement en bouton d’achat intégrable afin de vendre un produit ou un abonnement à partir de votre site Web. Sélectionnez un lien existant sur la page **Payment Links** , ou créez un nouveau lien, puis cliquez sur le **bouton Acheter**. Copiez le code et collez-le sur votre site Web. Pour en savoir plus sur l’intégration et la personnalisation d’un bouton, consultez la page Créer un bouton Acheter.
### Désactiver un lien![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez désactiver un lien de paiement depuis le Dashboard. Cliquez sur le menu de débordement () à droite du lien de paiement souhaité, puis sur **Désactiver**. Une fois le lien désactivé, les clients ne pourront plus l’utiliser pour effectuer des achats. Vous pouvez choisir de réactiver le lien de paiement à tout moment. Vous pouvez également utiliser l’API pour désactiver un lien de paiement.
## Configurer des moyens de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Avec les moyens de paiement dynamiques, Stripe affiche les moyens de paiement les plus pertinents et les plus souvent compatibles pour vos clients, y compris Apple Pay et Google Pay. Stripe active pour vous certains moyens de paiement par défaut. Nous pouvons également activer d’autres moyens de paiement après vous en avoir informé. Utilisez le Dashboard à tout moment pour activer ou désactiver des moyens de paiement. En savoir plus sur les moyens de paiement pris en charge et les différents types de moyens de paiement.
Vous pouvez examiner les méthodes de paiement que vos clients voient dans le Dashboard en saisissant un ID de transaction ou en définissant le montant et la devise d’une commande.
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
Créer un lien de paiement
Payment Links sur mobile
Partager des liens de paiement
Générer un code QR
Intégrer un bouton sur votre site
Désactiver un lien
Configurer des moyens de paiement
Produits utilisés
Payment Links
Payments
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

Regardez le guide vidéo
Mini Player
