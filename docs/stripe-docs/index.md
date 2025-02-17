Accéder directement au contenu
Accueil
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
![](https://b.stripecdn.com/docs-statics-srv/assets/52d6e32f24e1d2872960ba1d0cb8aac5.webp)
# Documentation
Parcourez nos guides et exemples pour intégrer Stripe.
Démarrer avec les paiements
Découvrir tous les produits
Connectez-vous ou créez un compte pour charger vos clés API de test.
Cartes de test
4242 4242 4242 4242
## Sans code
  * Vendre et se faire payer en ligne
  * Facturer les clients
  * Configurer des paiements récurrents


## Hébergé par Stripe
  * Utiliser une page de paiement préconfigurée
  * Configurer le portail client
  * Créer une grille tarifaire


## Pour les développeurs
  * Documentation de l’API
  * QuickStart consacré au développement
  * Consulter nos exemples de projets


## Faire un essai
Démarrer un paiement
Vendre un produit
Émettre des bons de réduction
Obtenir votre solde
Gérer les taxes
`
$ stripe payment_intents create --amount 1099 --currency "usd"
```

Copier
{
```
"id"
```
```
: 
```
```
"xxxxxx"
```
```
,
```

```
"object"
```
```
: 
```
```
"payment_intent"
```
```
,
```

```
"amount"
```
```
: 
```
```
1099
```
```
,
```

```
"amount_capturable"
```
```
: 
```
```
0
```
```
,
```

```

"amount_details": {
```
"tip"
```
```
: 
```
```
{}
```
```
,
```

},
```

```
"amount_received"
```
```
: 
```
```
0
```
```
,
```

```
"amount_subtotal"
```
```
: 
```
```
1099
```
```
,
```

```
"application"
```
```
: 
```
```
null
```
```
,
```

```
"application_fee_amount"
```
```
: 
```
```
null
```
```
,
```

```
"automatic_payment_methods"
```
```
: 
```
```
null
```
```
,
```

```
"canceled_at"
```
```
: 
```
```
null
```
```
,
```

```
"cancellation_reason"
```
```
: 
```
```
null
```
```
,
```

```
"capture_method"
```
```
: 
```
```
"automatic"
```
```
,
```

```
"charges"
```
```
: 
```
```
{… 5 éléments}
```
```
,
```

```
"client_secret"
```
```
: 
```
```
"xxxxxx"
```
```
,
```

```
"confirmation_method"
```
```
: 
```
```
"automatic"
```
```
,
```

```
"created"
```
```
: 
```
```

1739804773

```
```
,
```

```
"currency"
```
```
: 
```
```
"usd"
```
```
,
```

```
"customer"
```
```
: 
```
```
null
```
```
,
```

```
"description"
```
```
: 
```
```
null
```
```
,
```

```
"invoice"
```
```
: 
```
```
null
```
```
,
```

```
"last_payment_error"
```
```
: 
```
```
null
```
```
,
```

```
"livemode"
```
```
: 
```
```
false
```
```
,
```

```
"metadata"
```
```
: 
```
```
{}
```
```
,
```

```
"next_action"
```
```
: 
```
```
null
```
```
,
```

```
"on_behalf_of"
```
```
: 
```
```
null
```
```
,
```

```
"payment_method"
```
```
: 
```
```
null
```
```
,
```

```

"payment_method_options": {
```
"card"
```
```
: 
```
```
{… 5 éléments}
```
```
,
```

},
```
```

"payment_method_types": [
```
"card"
```
```
,
```

],
```

```
"processing"
```
```
: 
```
```
null
```
```
,
```

```
"receipt_email"
```
```
: 
```
```
null
```
```
,
```

```
"review"
```
```
: 
```
```
null
```
```
,
```

```
"setup_future_usage"
```
```
: 
```
```
null
```
```
,
```

```
"shipping"
```
```
: 
```
```
null
```
```
,
```

```
"source"
```
```
: 
```
```
null
```
```
,
```

```
"statement_descriptor"
```
```
: 
```
```
null
```
```
,
```

```
"statement_descriptor_suffix"
```
```
: 
```
```
null
```
```
,
```

```
"status"
```
```
: 
```
```
"requires_payment_method"
```
```
,
```

```
"total_details"
```
```
: 
```
```
{… 3 éléments}
```
```
,
```

```
"transfer_data"
```
```
: 
```
```
null
```
```
,
```

```
"transfer_group"
```
```
: 
```
```
null
```
```
,
```

}
```

`
Connectez-vous pour modifier des requêtes réelles.
En savoir plus sur les Payment Intents
## Parcourir par produit![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Paiements
PaymentsPaiements en ligne
TerminalPaiements par TPE et omnicanaux
ConnectPaiements pour les plateformes
RadarGestion de la fraude et du risque
ClimateÉlimination du carbone
IdentityVérification de l'identité en ligne
Financial ConnectionsConnexion aux comptes financiers des utilisateurs
CryptoIntégrer une rampe d'accès à la cryptomonnaie ou effectuer des virements en cryptomonnaies
Automatisation des opérations financières
BillingAbonnements et paiements récurrents
TaxCalcul automatisé de la taxe sur les ventes et de la TVA
Revenue RecognitionAutomatisation de la comptabilité
SigmaRapports personnalisés
Data PipelineSynchronisation d'entrepôts de données
AtlasConstitution de start-up
Services bancaires
IssuingCréation de cartes
TreasuryModules destinés aux services financiers
CapitalFinancement d'entreprise
Composants préconfigurés
Payment LinksPaiements sans code
CheckoutPage de paiement préconfigurée hébergée par Stripe
ElementsComposants d'interface utilisateur front-end sécurisés
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

