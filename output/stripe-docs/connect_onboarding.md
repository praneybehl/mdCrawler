Accéder directement au contenu
Choisir votre configuration d'inscription des utilisateurs
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
Choisir votre configuration d'inscription des utilisateurs
Stripe-hosted onboarding
Inscription des utilisateurs intégrée
Inscription via l'API
Fonctionnalités du compte
Informations de vérification requises
Types de contrat de services
Vérifications supplémentaires
Partage de l'entité juridique
Migrer vers Stripe


Configurer les dashboards des comptes
Accepter des paiements
Effectuer des virements vers des comptes
Gérer votre plateforme Connect
Formulaires fiscaux pour votre plateforme Connect
Utiliser les types de comptes connectés
Intégration avec Accounts v2
Canada
Français (France)
AccueilPlateformes et places de marchéOnboard accounts
# Choisissez votre configuration d'inscription des utilisateurs
## Découvrez les différentes options d'inscription pour vos comptes connectés.
Stripe propose plusieurs options d’inscription :
  * **Inscription hébergée par Stripe** : Vos comptes connectés passent par le flux d’inscription dans un formulaire Web hébergé par Stripe.
  * **Inscription intégrée des utilisateurs** : vous intégrez le composant Account onboarding directement dans votre application, et vos comptes connectés passent par le flux d’inscription sans quitter votre application.
  * **Inscription via l’API** : Vous utilisez les API de Stripe pour créer votre interface utilisateur d’inscription personnalisée.


Choisissez l’option d’inscription des utilisateurs qui convient le mieux à votre entreprise. Stripe recommande d’utiliser l’inscription hébergée par Stripe ou l’inscription intégrée. Ces options se mettent automatiquement à jour pour gérer l’évolution des exigences lorsqu’elles s’appliquent à un compte connecté.
**INSCRIPTION HÉBERGÉE PAR STRIPE**| **INSCRIPTION INTÉGRÉE**| **INSCRIPTION VIA L’API**  
---|---|---  
**TRAVAIL D’INTÉGRATION**|  Minimal, mise en production rapide| Plus d’efforts, mise en production rapide| Le maximum d’efforts, peut retarder la mise en production  
**PERSONNALISATION**|  Logo Stripe et marquage de la plateforme limité| Hautement personnalisable avec un marquage Stripe limité| Contrôle total sur votre propre interface utilisateur  
**MISES À JOUR AUTOMATIQUES POUR LES NOUVELLES EXIGENCES DE CONFORMITÉ**|  Immédiate| Immédiate| Nécessite des modifications de l’intégration  
**PRENEZ EN CHARGE DE NOUVEAUX PAYS SANS MODIFICATIONS DE L’INTÉGRATION**  
**PRISE EN CHARGE DU PARTAGE DE L’ENTITÉ JURIDIQUE**  
**LOGIQUE DE FLUX**|  Contrôle limité| Contrôle limité| Contrôle total  
**IDÉAL POUR**|  Plateformes qui souhaitent que Stripe s’occupe de l’inscription| Plateformes qui souhaitent un flux d’inscription aux couleurs de leur marque au sein de leur application| Plateformes qui exigent un contrôle total du flux d’inscription et qui disposent des ressources nécessaires pour le créer et le maintenir  
## Inscription hébergée par Stripe![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
L’inscription hébergée par Stripe est un formulaire Web hébergé par Stripe avec le nom, la couleur et l’icône de votre marque. L’Inscription hébergée par Stripe utilise l’API Accounts pour lire les exigences et générer un formulaire d’inscription hébergée avec une validation robuste des données. Elle est localisée pour tous les pays dans lesquels Stripe est disponible.
L’inscription hébergée par Stripe prend en charge le partage de l’entité juridique, qui permet aux propriétaires de plusieurs comptes Stripe de partager certaines informations sur leur entreprise entre ces comptes. Lors de l’inscription d’un compte, ils peuvent réutiliser les informations d’un compte existant au lieu de les envoyer à nouveau.
Utilisez l’Inscription hébergée par Stripe si vous souhaitez que Stripe s’occupe de l’inscription, avec peu d’efforts à fournir de la part de votre plateforme.
En savoir plus sur l’inscription hébergée par Stripe
## Inscription intégrée![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
L’inscription intégrée est une interface utilisateur hautement personnalisable avec une faible présence de l’image de marque Stripe. Votre plateforme intègre le composant d’inscription des comptes dans votre application, et vos comptes connectés interagissent avec le composant intégré sans jamais quitter votre application. L’inscription intégrée utilise l’API Accounts pour lire les exigences et générer un formulaire d’inscription avec une validation robuste des données. Elle est localisée pour tous les pays pris en charge par Stripe.
L’inscription intégrée prend en charge le partage de l’entité juridique, qui permet aux propriétaires de plusieurs comptes Stripe de partager certaines informations sur leur entreprise. Lors de l’inscription d’un compte, ils peuvent réutiliser les informations d’un compte existant au lieu de les envoyer à nouveau.
Avec l’inscription intégrée des utilisateurs, vous bénéficiez d’un flux d’inscription personnalisé sans la complexité et la maintenance associées à la mise à jour de votre intégration d’inscription au fur et à mesure de l’évolution des exigences de conformité.
En savoir plus sur l’inscription intégrée
## Inscription via l’API![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous utilisez l’API Accounts pour mettre en place un flux d’inscription et gérer la vérification d’identité, la localisation et la gestion des erreurs pour chaque pays dans lequel vos comptes connectés s’inscrivent. Stripe peut être complètement invisible pour le titulaire du compte. Votre plateforme est responsable de toutes les interactions avec vos comptes connectés et de la collecte de toutes les informations nécessaires à la vérification de chaque compte. Les exigences de vérification sont mises à jour au fur et à mesure que les lois et les réglementations changent dans le monde. Vous devez prévoir de revoir et de mettre à jour les exigences d’inscription des utilisateurs au moins tous les six mois.
Stripe ne recommande pas cette option à moins que vous ne soyez totalement engagé dans la complexité opérationnelle requise pour construire et maintenir un flux d’inscription des utilisateurs via l’API. Pour une inscription des utilisateurs personnalisée, Stripe recommande fortement l’inscription intégré.
En savoir plus sur l’inscription des utilisateurs via l’API
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
Inscription hébergée par Stripe
Inscription intégrée
Inscription via l’API
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

