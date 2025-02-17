Accéder directement au contenu
Configurer le portail client
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
# Configurer le portail client
## Offrez à vos clients la possibilité de gérer leurs propres comptes de facturation à l'aide d'un portail hébergé par Stripe.
Lorsque vous souhaitez proposer à vos clients un accès à leurs comptes de facturation en libre-service, vous pouvez configurer le portail client. Utilisez-le pour leur offrir la possibilité de gérer leurs informations de facturation, leurs abonnements et leurs factures au fil du développement de votre entreprise.
Stripe héberge le portail client, ce qui signifie que vous pouvez l’utiliser même si vous n’avez pas de site Web. Vous pouvez également y associer des utilisateurs à partir d’un site existant ou d’une intégration Stripe existante.
Pour commencer, vous devez créer un compte Stripe. M’inscrire.
## Créer un produit![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Pour créer un produit dans le Dashboard :
  1. Accédez à **Plus** > **Catalogue de produits**.
  2. Cliquez sur **+Ajouter un produit**.
  3. Indiquez le **Nom** de votre produit.
  4. _(Facultatif)_ Ajoutez une **Description**. La description apparaît lors du règlement, sur le portail client et dans les devis.
  5. _(Optional)_ Add an **Image** of your product. Use a JPEG, PNG, or WEBP file that’s smaller than 2MB. The image appears at checkout.
  6. _(Facultatif)_ Si vous utilisez Stripe Tax, sélectionnez un **Code de taxe** pour votre produit. Pour plus d’informations sur le code approprié pour votre produit, reportez-vous à notre description des catégories de taxe disponibles.
  7. _(Facultatif)_ Indiquez un **Libellé de relevé bancaire**. Ce libellé prévaudra sur tout libellé de compte pour les paiements récurrents. Choisissez un libellé que vos clients reconnaîtront facilement sur leur relevé bancaire.
  8. _(Facultatif)_ Indiquez un **Libellé d’unité** reflétant la façon dont vous facturez votre produit. Par exemple, si vous facturez par utilisateur, entrez « utilisateur » pour que le poste indique « par utilisateur » pour le tarif. Les libellés d’unité s’affichent lors du paiement, sur les factures, les reçus et sur le portail client.


Comment utiliser les produits et les tarifs.
## Configurer le portail client![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  1. **Activer un lien vers le portail client** Sur la page de configuration du portail client, cliquez sur **Activer le lien** dans la section **Méthodes pour démarrer**.
  2. **Configurer le portail** : accédez à la page de configuration du portail client et sélectionnez vos options de configuration. En savoir plus sur les options de configuration.
  3. **Partager le lien de connexion au portail** Ajoutez le lien activé à votre site ou envoyez-le directement à vos clients. Ils peuvent se connecter au portail à l’aide de leur adresse e-mail et d’un code à usage unique.
Assurez-vous que vos clients disposent d’une adresse e-mail définie. Si plusieurs clients utilisent la même adresse e-mail, Stripe sélectionne le client créé le plus récemment avec cette adresse e-mail et ayant un abonnement actif.
Pour des raisons de sécurité :
     * Les clients ne peuvent pas modifier leur adresse e-mail via ce lien.
     * Si un client ne reçoit pas de code à usage unique après avoir cliqué sur le lien de connexion, assurez-vous que son adresse e-mail correspond à celle d’un client existant. Pour vérifier, saisissez l’adresse e-mail dans la barre de recherche de votre Dashboard Stripe.


## FacultatifPersonnaliser l'image de marque![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## FacultatifRenseigner automatiquement l'e-mail du client![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
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
Créer un produit
Configurer le portail client
Produits utilisés
Payments
Billing
Tax
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

