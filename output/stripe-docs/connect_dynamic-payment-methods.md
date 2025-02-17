Accéder directement au contenu
Moyens de paiement dynamiques
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
Configurer les dashboards des comptes
Accepter des paiements
Effectuer des virements vers des comptes
Gérer votre plateforme Connect
Formulaires fiscaux pour votre plateforme Connect
Utiliser les types de comptes connectés
Types de comptes connectés
Moyens de paiement dynamiques
API Payment Method Configurations


Intégration avec Accounts v2
Canada
Français (France)
AccueilPlateformes et places de marchéWork with connected account types
#### Remarque
Cette page n'est pas encore disponible dans cette langue. Nous faisons tout notre possible pour proposer notre documentation dans davantage de langues et nous vous fournirons la version traduite dès qu'elle sera disponible.
# Update to use dynamic payment methods
## Add dynamic payment methods to your existing platform.
This guide provides instructions for existing platforms to integrate dynamic payment methods. If you’re setting up a new platform, start with the Connect integration guide.
## Integration instructions for dynamic payment methods![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Use the following form to select your integration. If you need help determining your platform setup, including checkout solution, connected account types, and charge types, refer to Create a charge.
Confirmer votre intégration
Intégration de paiement :
Stripe CheckoutCheckout est un formulaire de paiement hébergé par Stripe.
Composant Element PaymentL'Element Payment (pour Web et mobile) est un composant d'interface utilisateur que vous pouvez intégrer à votre site Web ou votre application.
Type de paiement :
Paiements directsPaiements indirectsPaiements et transferts distincts
Accès au Dashboard :
StripeExpressAucun
## Enable payment methods for connected accounts
Recommended
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
If necessary, consult the following resources for payment method information:
  * A guide to payment methods for help in choosing the right payment methods for your platform.
  * Account capabilities to make sure your chosen payment methods work for your connected accounts.
  * Payment method and product support table to make sure your chosen payment methods work for your Stripe products and payments flows.


Stripe enables certain payment methods for your connected accounts by default. Visit the Manage payment methods for your connected accounts page in your Dashboard to configure which payment methods your connected accounts accept. Changes to default settings apply to all new and existing connected accounts.
For each payment method, you can select one of the following dropdown options:
**On by default**|  Your connected accounts accept this payment method during checkout. Some payment methods can only be off or blocked, this is because the owners of your platform’s connected accounts must activate them in their Dashboard settings page.  
---|---  
**Off by default**|  Your connected accounts don’t accept this payment method during checkout. If you allow the owners of your platform’s connected accounts to manage their own payment methods in their Dashboard, however, they have the ability to turn it on.  
**Blocked**|  Your connected accounts don’t accept this payment method during checkout. If you allow the owners of your platform’s connected accounts to manage their own payment methods in their Dashboard, they don’t have the option to turn it on.  
![Dropdown options for payment methods, each showing an available option \(blocked, on by default, off by default\)](https://b.stripecdn.com/docs-statics-srv/assets/dropdowns.ef651d721d5939d81521dd34dde4577f.png)
Payment method options
If you make a change to a payment method, you must click **Review changes** in the bottom bar of your screen and **Save and apply** to update your connected accounts.
![Dialog that shows after clicking Save button with a list of what the user changed](https://b.stripecdn.com/docs-statics-srv/assets/dialog.a56ea7716f60db9778706790320d13be.png)
Save dialog
## Allow your connected accounts to manage their payment methods
Recommended
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe recommends that you allow the owners of your platform’s connected accounts to customize their own payment methods from the Dashboard. If you enable this option, then each connected account with Stripe Dashboard access can log in to their Dashboard and view their Payment methods page. The Dashboard displays the set of payment method defaults you applied to all new and existing connected accounts. The owners of your platform’s connected accounts can override these defaults, excluding payment methods you have blocked.
Check the **Account customization** checkbox to enable this option. You must click **Review changes** in the bottom bar of your screen and then select **Save and apply** to update this setting.
![Screenshot of the checkbox to select when allowing connected owners to customize payment methods](https://b.stripecdn.com/docs-statics-srv/assets/checkbox.275bd35d2a025272f03af029a144e577.png)
Account customization checkbox
## Integrate Checkout using dynamic payment methods
Required
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Previously, you might have used the `payment_method_types` parameter when defining your Checkout session to accept different payment methods. To begin managing your payment methods in the Dashboard, remove this parameter from your integration.
After you remove the `payment_method_types` parameter from your integration, some payment methods turn on automatically, including cards and wallets. The `currency` parameter restricts the payment methods that are shown to the customer during the checkout session.
Ruby
```

Stripe::Checkout::Session.create({
mode:'payment',# Remove the payment_method_types parameter# to manage payment methods in the Dashboard
payment_method_types:['card'],
line_items:[{
 price_data:{# The currency parameter determines which# payment methods are used in the Checkout Session.
  currency:'eur',
   product_data:{
    name:'T-shirt',},
   unit_amount:2000,},
  quantity:1,}],
 success_url:'https://example.com/success',
 cancel_url:'https://example.com/cancel',})

```

## Enable shipping address collection in Checkout
Recommended
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
If you collect shipping addresses, you need to define which countries you can ship to when you create the Checkout session. Specify the two-letter ISO country codes in the `shipping_address_collection.allowed_countries` parameter.
You can optionally add shipping rates with the `shipping_options` parameter.
If you use Afterpay or Clearpay, you must collect shipping addresses, but you don’t need to specify shipping rates for those payment methods.
#### Remarque
Shipping address collection is required to use Afterpay or Clearpay as a payment method in Checkout, but shipping rates aren’t.
## Handle delayed notification payment methods, if applicable
Recommended
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Follow the steps in our Manage payment methods in the Dashboard guide on how to handle delayed notification payment methods.
## Test your integration
Recommended
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Test your integration to ensure it performs as you expect. Log in to one of your test accounts and navigate to **Payment methods** settings to view your settings for your connected accounts. Test your checkout flow with your test API key and a test account. If a payment method you expect to be available is not available, check the payment method product support table to make sure your products and merchants are in a compatible currency and country.
## Have your connected accounts with Stripe Dashboard access enable any payment methods that require setup steps
Optional
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Your connected accounts with Stripe Dashboard access are able to use most payment methods by default; however, some payment methods (such as Alipay and WeChat Pay) require your users to manually activate the payment method in their Dashboard. Confirm which payment methods require manual activation using the payment method capabilities table. If the **Available by default** column reads **no** , the payment method requires manual activation.
If you allow the owners of your platform’s connected accounts to manage payment methods, then instruct them to enable these payment methods from their Dashboard.
![Screenshot of connected account payment method customization through Dashboard showing available payment methods as on and available.](https://b.stripecdn.com/docs-statics-srv/assets/turn-on-payments.afef26196ebae8f5564d328d6ba73b92.png)
Payment method customization
If you don’t allow the owners of your platform’s connected accounts to customize payment methods, then instruct them to visit their manual settings page.
![Screenshot of manual settings page with payment methods listed with the option to request access, request invite, or configure.](https://b.stripecdn.com/docs-statics-srv/assets/manual-settings.db0a0c2abebb94e197e1bef683ea7db9.png)
Manual settings for payment methods
#### Version bêta privée
The **embedded payment method settings component** allows connected accounts to configure the payment methods they offer at checkout without the need to access the Stripe Dashboard. Request access and learn how to integrate with Payment Method Configurations.
## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Connect integration guide
  * Payment method configurations API
  * Multiple payment method configurations
  * Add payment method capabilities


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
Integration instructions for dynamic payment methods
Enable payment methods for connected accounts
Allow your connected accounts to manage their payment methods
Integrate Checkout using dynamic payment methods
Enable shipping address collection in Checkout
Handle delayed notification payment methods, if applicable
Test your integration
Have your connected accounts with Stripe Dashboard access enable any payment methods that require setup steps
Voir aussi
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

