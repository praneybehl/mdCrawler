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
Présentation


Checkout
Web Elements
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
AccueilPaiementsPayment Links
#### Remarque
Cette page n'est pas encore disponible dans cette langue. Nous faisons tout notre possible pour proposer notre documentation dans davantage de langues et nous vous fournirons la version traduite dès qu'elle sera disponible.
# Payment Links
## Sell online without building a digital storefront.
Accept a payment or sell subscriptions without building additional standalone websites or applications with Payment Links. Share the link as many times as you want on social media, in emails, or on your website.
Payment Links supports more than 20 payment methods—including credit and debit cards, Apple Pay, and Google Pay. The payment link automatically matches your customer’s preferred browser language for more than 30 languages.
If you don’t have a Stripe account and want to get started with Payment links, sign up for an account.
Create a payment link in the demo below, and learn more about the features.
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
## Get started ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Create a payment link
Create a payment link without using code.
Share a payment link
Share a payment link with your customers.
Track a payment link
Track a payment link and related campaigns.
## Explore advanced options ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Create and manage a payment link with the API
Create and manage a payment link with the API.
Create an embeddable buy button
Create an embeddable buy button to sell a product, subscription, or accept a payment on your website.
Customize your checkout experience
Choose the information you collect from customers at checkout.
## Features![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Quick setupWithout writing any code, create payment links that automatically match your customer’s browser language for over 30 languages.
  * Multiple payment methodsSupport over 20 payment methods—including credit and debit cards, digital wallets, and local payment methods.
  * Shareable linksDistribute payment links through email, social media, messaging apps, or embed them directly on your website.
  * Customize checkoutCustomize the payment page your customers see with your logo, colors, and branding.
  * Automatic receiptsSend branded receipts and invoices to customers after successful payments.
  * Refund capabilityProcess refunds directly from your Stripe Dashboard.


## Compare Invoicing and Payment Links ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Invoicing and Payment Links are two of the easiest ways to start using Stripe to accept payments without writing any code. Use the following table to compare the two products and to understand which works best for your use case.
**Invoicing** | **Payment Links**  
---|---  
**Description**|  Use invoices to collect one-time or recurring payments from a specific customer.| Use Payment Links to sell a product, a subscription, or accept a donation.  
**Customer**|  Specific individuals or businesses.| Anyone with the link.  
**Reusability**|  You can’t reuse invoices, but you can duplicate them and edit the details for another customer.| Reuse multiple times with multiple customers, or limit the number of purchases.  
**Integration effort**|  No coding| No coding  
**Sharing options**| 
  * Email from the Dashboard.
  * Copy the invoice link to share over email or SMS.
  * Send a PDF.
  * Auto-charge the payment method on file.

| 
  * Show a QR code.
  * Copy the link to share it over email, SMS, or social media.
  * Add a buy button to your website.

  
**UI customization**|  Editable template1| Limited customization2  
**Payment methods**|  Choose from over 40 payment methods, and manage them in the Dashboard without coding.| Dynamically display over 40 payment methods3, and manage them in the Dashboard without coding.  
**Preferred language support**|  Over 30 languages. Set the Dashboard language preference for each customer.| Over 30 languages. Match the browser language setting for each customer.  
**Recurring payments**|  Use Stripe Billing to send a subscription or recurring invoice. No-code subscriptions are available| Create a payment link for a subscription.  
**Collection tools**|  Automatic collection features, including Smart Retries and reminder emails are available.| Revenue recovery features, including Smart Retries and reminder emails are available for subscription payment links.  
**Reconciliation**|  Auto-reconciliation of bank payments| Simple reconciliation by using URL parameters  
**Stripe-hosted payment page**  
**Stripe Tax support**  
**Customers can choose what to pay**  
**Collect partial payments or set up payment plans**  
**Customers can edit quantities**  
**Coupons or discounts**  
**Send a quote or estimate and convert it to an invoice once finalized**  
**Upsells and cross-sells**  
**PCI compliance handling**|  4  
1 Use the editable template to incorporate your own icons, brand colors, payment terms, page sizes, as well as memo and footer fields.2 With limited customization, you can access 20 preset fonts, three predefined border radiuses, and options for adjusting your logo, background, product images, and the color of your own button.3 Dynamic payment methods filter for eligibility, displaying the most relevant payment methods to maximize conversion. Payment method availability varies by product.4 Learn how to customize invoices for global compliance.
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

