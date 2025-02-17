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
Gestion des litiges
Vérifier l'identité
Présentation
Démarrer
Vérifier des pièces d'identité
Gérer les résultats des vérifications
Accéder aux résultats de vérification
Réviser les résultats de vérification
Flux de vérification
Contrôles de vérification supplémentaires
Contrôles de vérification
Ajout de vérifications de selfie
À propos des API
Sessions de vérification
Passer en production
Avant de passer en mode production
Cas d'usage pris en charge
Identity en quelques mots


Canada
Français (France)
AccueilDémarrerVerify identities
# Identity
## La manière la plus simple de vérifier les identités.
Disponible pour les utilisateurs des pays suivants :
Utilisez Stripe Identity pour confirmer l’identité de vos utilisateurs à travers le monde. Vous pourrez ainsi prévenir la fraude, simplifier les opérations de gestion des risques et accroître la confiance et la sécurité. Stripe Identity vous permet de :
  * Vérifier l’authenticité de pièces d’identité de plus de 120 pays
  * Capturer des pièces d’identité grâce à un flux de vérification optimisé pour la conversion
  * Comparer des photos d’identité avec des selfies et valider le numéro de sécurité sociale
  * Accéder aux images collectées et aux données extraites des pièces d’identité


## Démarrer![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
S'inscrire
Activez Identity dans le Dashboard.
Vérifier les pièces d'identité de vos utilisateurs
Commencez par créer des sessions et recueillir des pièces d’identité.
Gérer les résultats des vérifications
Écoutez les résultats des vérifications pour que votre intégration puisse déclencher automatiquement des réactions.
Créer une configuration réutilisable
Utilisez les flux de vérification pour créer une configuration réutilisable et gérer la vérification de l’identité dans le Dashboard.
## Contrôles de vérification supplémentaires![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Contrôles de vérification
Découvrir les différents contrôles de vérification pris en charge par Stripe Identity.
Ajout de vérifications à l'aide de selfies
Ajoutez des contrôles de similarité des visages pour empêcher des personnes malveillantes d’utiliser des documents volés.
Vérifications supplémentaires pour Connect
Recueillez une vérification d’identité supplémentaire dans le cadre du processus d’inscription à Connect.
## Cloner un exemple de projet![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Essayer la démo
Aperçu d’une démo de Stripe Identity
Vérifier des pièces d'identité
Web · Mobile Web
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

