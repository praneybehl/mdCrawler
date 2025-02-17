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
Présentation
Address Element
Express Checkout Element
Payment Element
Link Authentication Element


Elements intégrés à l'application
Scénarios de paiement
Tunnels de paiement personnalisés
Acquisition flexible
Paiements par TPE
Terminal
Autres produits Stripe
Financial Connections
Cryptomonnaies
Climate
Payout Links
Canada
Français (France)
AccueilPaiementsWeb Elements
#### Remarque
Cette page n'est pas encore disponible dans cette langue. Nous faisons tout notre possible pour proposer notre documentation dans davantage de langues et nous vous fournirons la version traduite dès qu'elle sera disponible.
# Stripe Web Elements
## Create your own checkout flows with prebuilt UI components.
Stripe Elements is a set of prebuilt UI components for building your web checkout flow. It’s available as a feature of Stripe.js, our foundational JavaScript library for building payment flows. Stripe.js tokenizes sensitive payment details within an Element without ever having them touch your server. We recommend the Payment Element for most integrations.
## Get started![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
If you don’t see your Element below, find more in the Stripe.js API Reference.
![](https://b.stripecdn.com/docs-statics-srv/assets/payment-element.750bc8af6d17414b54dc09ae8acb8efb.svg)
Payment Element
Recommended
Accept a payment with one or multiple payment methods securely, including cards.
![](https://b.stripecdn.com/docs-statics-srv/assets/wallet-element.c96ed64cf20f79da4cd61d96699a3ff3.svg)
Express Checkout Element
Recommended
Display popular Wallets like Apple Pay, Google Pay, and PayPal.
![](https://b.stripecdn.com/docs-statics-srv/assets/link-element.9773d44cacda7df8846963ff92cdd4b6.svg)
Link Authentication Element
Link auto-fills your customers’ payment and shipping details to reduce friction and deliver an easy and secure checkout experience.
![](https://b.stripecdn.com/docs-statics-srv/assets/shipping-element.01362d4c55a5a5bfe5ce171e3cc6b953.svg)
Address Element
Collect address information and display Link saved addresses.
![](https://b.stripecdn.com/docs-statics-srv/assets/customize@2x.e4101cdeb47e80bca9181a73da5581cf.png)
Customize the appearance of Elements
Pick from prebuilt themes, add your own color and size variables, or adjust individual components for more advanced use cases.
## Features![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * **Customizable UI components** Choose pre-built, customizable elements for collecting customer and payment information that can match the branding of your business.
  * **Automatic user formatting** Format and structure customer input in real-time as they type payment information and match your customer’s preferred language.
  * **Real-time validation and error handling** Provide instant feedback such as error messages on card number, expiry date, CVC inputs, email addresses, and addresses during checkout.
  * **Accessibility** Provide a responsive design that fits on any screen size, also supporting screen readers and keyboard navigation.
  * **One-click checkout** Allow customers to pay using saved payment information with one-click checkout using Link.


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

