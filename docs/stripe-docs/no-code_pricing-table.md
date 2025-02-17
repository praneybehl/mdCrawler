Accéder directement au contenu
Créer une grille tarifaire
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
#### Remarque
Cette page n'est pas encore disponible dans cette langue. Nous faisons tout notre possible pour proposer notre documentation dans davantage de langues et nous vous fournirons la version traduite dès qu'elle sera disponible.
# Create an embeddable pricing table
## Display a pricing table on your website and take customers directly to Stripe Checkout.
You can use the Stripe Dashboard to create a table that displays different subscription pricing levels to your customers. You don’t need to write any custom code to create or embed a pricing table. This guide describes how to:
  * Use the Stripe Dashboard to configure the UI component
  * Copy the generated code from the Dashboard
  * Embed the code on your website to show your customers pricing information and take them to a checkout page


## Overview ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
![The pricing table is an embedded UI that displays pricing information and takes customers to checkout.](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table-embed.b27a06fcd84b57a8866a8b4b62323fdc.png)
Embed a pricing table on your website to display pricing details and convert customers to checkout.
A pricing table is an embeddable UI that:
  * Displays pricing information and takes customers to a prebuilt checkout flow. The checkout flow uses Stripe Checkout to complete the purchase.
  * Supports common subscription business models like flat-rate, per-seat, tiered pricing, and free trials.
  * Lets you configure, customize, and update product and pricing information directly in the Dashboard, without needing to write any code.
  * Embeds into your website with a `<script>` tag and web component. Stripe automatically generates the tag. You copy and paste it into your website’s code.


The diagram below summarizes how the customer goes from viewing a pricing table to completing checkout.
Customer
Your application
Stripe Checkout
Views pricing table
Clicks on “subscribe” button
Completes purchase
Returns to your website
checkout.session.completed
Pricing table
## Create pricing table![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  1. In the Dashboard, go to **More** > **Product catalog** > pricing tables.
  2. Click **+Create pricing table**.
  3. Add products relevant to your customers (up to four per pricing interval). Optionally, include a free trial.
  4. Adjust the look and feel in **Display settings**. Highlight a specific product and customize the language, colors, font, and button design, then click **Continue**.
  5. Configure **Payment settings** to select the customer information to collect, options to present to the customer, and whether to display a confirmation page or redirect customers back to your site after a successful purchase.
#### Confirm maximum quantity
If you have tiered pricing that supports quantities greater than the default maximum of 99, check the **Let customers adjust quantity** property and increase the **Max** value accordingly. Tiered pricing options for quantities above the maximum don’t appear in the selector.
  6. Configure the customer portal by clicking **Continue**.
  7. Click **Copy code** to copy the generated code and embed it into your website.


![Customizing a pricing table](https://b.stripecdn.com/docs-statics-srv/assets/create-pricing-table-step-1.45ac9351d8f043a0a63554b89b2cedfc.png)
Customize your pricing table
![Configure payment settings](https://b.stripecdn.com/docs-statics-srv/assets/create-pricing-table-step-2.07d5287026b797b9aa1905c6ad99958d.png)
Configure payment settings
## Embed pricing table![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
After creating a pricing table, Stripe automatically returns an embed code composed of a `<script>` tag and a `<stripe-pricing-table>` web component. Click the **Copy code** button to copy the code and paste it into your website.
![Pricing table detail page](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table-detail-page.dee9a93d69e802759dabd0e4ce62f1bd.png)
Copy the pricing table’s code and embed it on your website.
If you’re using HTML, paste the embed code into the HTML. If you’re using React, include the `script` tag in your `index.html` page to mount the `<stripe-pricing-table>` component.
#### Mise en garde
The pricing table uses your account’s publishable API key. If you revoke the API key, you need to update the embed code with your new publishable API key.
pricing-page.html
HTML
```

<body><h1>We offer plans that help any business!</h1><!-- Paste your embed code script here. --><scriptasyncsrc="https://js.stripe.com/v3/pricing-table.js"></script><stripe-pricing-tablepricing-table-id=
'{{PRICING_TABLE_ID}}'
publishable-key=
"pk_test_A7jK4iCYHL045qgjjfzAfPxu"
></stripe-pricing-table></body>

```

## Track subscriptions![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
When a customer purchases a subscription, you’ll see it on the subscriptions page in the Dashboard.
### Handle fulfillment with the Stripe API![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
The pricing table component uses Stripe Checkout to render a prebuilt, hosted payment page. When a payment is completed using Checkout, Stripe sends the checkout.session.completed event. Register an event destination to receive the event at your endpoint to process fulfillment and reconciliation. See the Checkout fulfillment guide for more details.
The `<stripe-pricing-table>` web component supports setting the `client-reference-id` property. When the property is set, the pricing table passes it to the Checkout Session’s client_reference_id attribute to help you reconcile the Checkout Session with your internal system. This can be an authenticated user ID or a similar string. `client-reference-id` can be composed of alphanumeric characters, dashes, or underscores, and be any value up to 200 characters. Invalid values are silently dropped and your pricing table will continue to work as expected.
#### Mise en garde
Since the pricing table is embedded on your website and is accessible to anyone, check that `client-reference-id` does not include sensitive information or secrets, such as passwords or API keys.
pricing-page.html
HTML
```

<body><h1>We offer plans that help any business!</h1><!-- Paste your embed code script here. --><scriptasyncsrc="https://js.stripe.com/v3/pricing-table.js"></script><stripe-pricing-tablepricing-table-id=
'{{PRICING_TABLE_ID}}'
publishable-key=
"pk_test_A7jK4iCYHL045qgjjfzAfPxu"
client-reference-id="{{CLIENT_REFERENCE_ID}}"></stripe-pricing-table></body>

```

## FacultatifAdd product marketing features![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## FacultatifAdd a custom call-to-action![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## FacultatifPass the customer email![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## FacultatifPass an existing customer![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## FacultatifCustomize the post-purchase experience![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## FacultatifUpdate pricing table![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## FacultatifConfigure free trials![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## FacultatifContent Security Policy![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## FacultatifLet customers manage their subscriptions
No code
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## FacultatifPresent local currencies![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## FacultatifAdd custom fields![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## Limitations ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * **Business models** —The pricing table supports common subscription business models like flat-rate, per-seat, tiered pricing, and trials. Other advanced pricing models aren’t supported.
  * **Product and price limits** —You can configure the pricing table to display a maximum of four products, with up to three prices per product. You can only configure three unique pricing intervals across all products.
  * **Account creation** —The pricing table call-to-action takes customers directly to checkout. It doesn’t currently support adding an intermediate step (for example, asking the customer to create an account on your website before checking out).
  * **Rate limit** —The pricing table has a rate limit of up to 50 read operations per second. If you have multiple pricing tables, the rate limit is shared.
  * **Checkout redirect** —The pricing table can’t redirect customers to checkout if your website provider sandboxes the embed code in an iframe without the `allow-top-navigation` attribute enabled. Contact your website provider to enable this setting.
  * **Testing the pricing table locally** —The pricing table requires a website domain to render. To test the pricing table locally, run a local HTTP server to host your website’s `index.html` file over the `localhost` domain. To run a local HTTP server, use Python’s SimpleHTTPServer or the http-server npm module.
  * **Connect** —The pricing table isn’t designed to work with Connect and doesn’t support features like a platform collecting fees.


## Limit customers to one subscription ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
You can redirect customers that already have a subscription to the customer portal or your website to manage their subscription. Learn more about limiting customers to one subscription.
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
Overview
Create pricing table
Embed pricing table
Track subscriptions
Handle fulfillment with the Stripe API
Limitations
Limit customers to one subscription
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

