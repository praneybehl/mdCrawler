Accéder directement au contenu
Envoyer des factures
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
# Utiliser des factures
## Envoyez une facture que vos clients pourront payer en ligne.
Débitez automatiquement votre client sur le moyen de paiement enregistré ou envoyez-lui la facture par e-mail, avec ou sans lien vers une page de paiement. Vous pouvez également envoyer la facture ou le lien vers la page de paiement manuellement.
#### Remarque
Pour en savoir plus sur la gestion des abonnements et des revenus récurrents, consultez la documentation relative aux abonnements.
![Page de facture hébergée](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page-guide.df3cc5a1e4180c338269aacdfa792180.png)
Page de facture hébergée
![Facture au format PDF](https://b.stripecdn.com/docs-statics-srv/assets/invoice-pdf-guide.d79c407ca08ee4b14dc0519fb3772309.png)
Facture au format PDF
## Configurer la marque de votre entreprise
Facultatif
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Avant de commencer à utiliser Stripe Invoicing, aidez vos futurs clients à comprendre vos produits et vos conditions d’utilisation en ajoutant des informations concernant votre entreprise et en personnalisant l’apparence de votre marque.
Les clients voient les informations de l’entreprise et de la marque sur la page de facture hébergée lorsqu’ils paient une facture en ligne. Pour permettre aux clients de gérer leurs anciennes factures et leurs propres informations de facturation, configurez le portail client.
![Configurer la marque de votre entreprise](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page.79b4c18913fe9fb30f47ad8a5f062b6f.png)
Configurer la marque de votre entreprise
## Choisir vos modes de paiement
Facultatif
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Par défaut, vos clients peuvent régler leurs factures avec n’importe lequel des moyens de paiement activés dans votre modèle de facture. Si vous êtes un nouvel utilisateur, Stripe active automatiquement les cartes bancaires, Link, les virements bancaires, Cash App Pay et WeChat Pay. Pour autoriser d’autres moyens de paiement, vous devez les activer dans vos paramètres des moyens de paiement.
Dans certains cas, des restrictions peuvent empêcher l’utilisation de certains moyens de paiement pour une facture. Par exemple, un moyen de paiement peut ne fonctionner que dans une seule devise, ou ne pas prendre en charge les paiements supérieurs à un certain montant. Lorsque ces restrictions empêchent l’utilisation d’un moyen de paiement donné, Stripe ne le sélectionne pas automatiquement. Pour en savoir plus, consultez les informations sur les moyens de paiement pris en charge.
![Choisir des moyens de paiement supplémentaires](https://b.stripecdn.com/docs-statics-srv/assets/supported-payment-methods.194614192ca2c72656bc0587e8e21f46.png)
Choisir des moyens de paiement supplémentaires
## Comment se faire payer![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez créer et envoyer une facture à partir du Dashboard. Les factures fournissent une liste détaillée des biens et des services rendus, qui comprend le coût, la quantité et les taxes. Vous pouvez également les utiliser comme outil pour collecter des paiements. En savoir plus.
![Créer et envoyer une facture](https://b.stripecdn.com/docs-statics-srv/assets/create-send-invoices.985a3078348be3c2591f8d5e2d96e21c.png)
Créer et envoyer une facture
## Configurer un modèle personnalisé
Facultatif
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez utiliser le modèle de facture pour personnaliser le contenu de vos factures. Définissez un mémo par défaut, un pied de page et un système de numérotation, et déterminez vos conditions de paiement par défaut. Dans la mesure où vous en savez plus sur vos clients et votre entreprise que Stripe, vérifiez que vos factures incluent toutes les informations requises. Reportez-vous au guide complet sur la personnalisation des factures dans Personnaliser les factures.
![Configurer le modèle de facture](https://b.stripecdn.com/docs-statics-srv/assets/invoice-template.d50c4ba2210f06442b6adbb7279fe7a4.png)
Configurer le modèle de facture
![Gestion des informations fiscales](https://b.stripecdn.com/docs-statics-srv/assets/manage-tax-information.3bbd3b8425726dc4ac243bb5bfd707a3.png)
Gestion des informations fiscales
## Suivre une facture![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Entre le moment où elles sont créées et celui où elles sont réglées, les factures passent par différents états. Vous pouvez suivre l’état d’une facture sur la page Factures de votre Dashboard. Pour informer votre client que la date d’échéance d’une facture approche, envoyez-lui un rappel par e-mail. Pour en savoir plus, consultez notre documentation consacrée à la gestion des factures.
![Suivre et gérer vos factures](https://b.stripecdn.com/docs-statics-srv/assets/track-invoices.647ee840cc77e53c4d8537ec43ba9289.png)
Suivre et gérer vos factures
## Automatiser le rapprochement des factures et l'encaissement des paiements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Pour automatiser Stripe Invoicing et vous faire payer plus rapidement, choisissez de débiter automatiquement le moyen de paiement enregistré de votre client. Vous pouvez également laisser Stripe gérer les problèmes de recouvrement de factures.
![Automatiser la facturation](https://b.stripecdn.com/docs-statics-srv/assets/advanced-invoicing-features.70dfe42ac952e7924876201c06e5902d.png)
Automatiser la facturation
### Clôturez vos registres comptables et comptabilisez les recettes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Grâce au rapprochement automatique, vous n’avez pas besoin d’exposer vos coordonnées bancaires sensibles aux utilisateurs ou de rapprocher manuellement les factures en cours avec votre banque. Avec le rapprochement automatique des factures, Stripe peut :
  * Faire correspondre les paiements entrants avec les montants des factures.
  * Gérer les trop-perçus ou les paiements insuffisants, lorsque le montant payé ne correspond pas à la facture.
  * Réduire le nombre d’appels à l’API nécessaires pour transférer des fonds dans Stripe.
  * Gérer les tentatives de paiement sur les factures en cours.


![Clôturer vos registres comptables](https://b.stripecdn.com/docs-statics-srv/assets/invoicing-auto-reconciliation.2d4b2648e4b67e8b2a2c7225a22bec69.png)
Clôturer vos registres comptables
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
Configurer la marque de votre entreprise
Choisir vos modes de paiement
Comment se faire payer
Configurer un modèle personnalisé
Suivre une facture
Automatiser le rapprochement des factures et l'encaissement des paiements
Clôturez vos registres comptables et comptabilisez les recettes
Produits utilisés
Invoicing
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

