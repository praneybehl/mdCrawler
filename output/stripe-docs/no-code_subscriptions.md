Accéder directement au contenu
Créer des abonnements
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
# Create subscriptions
## Set up recurring payments by offering subscriptions to your service.
Subscriptions represent what your customer is paying for and how much and how often you’re charging them for the product. You can subscribe customers manually through the Dashboard. You can also let them sign up through your website or a Payment Link.
This page shows you how to manually create and edit a subscription in your Stripe Dashboard.
## Create a subscription ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
To create a subscription:
  1. In the Stripe Dashboard, go to the subscriptions page.
  2. Click **+Create subscription**.
  3. Find or add a customer.
  4. Enter the pricing and product information. You can add multiple products.
  5. Set the start and end date of the subscription.
  6. Set the starting date for the billing cycle. This defines when the next invoice is generated. Depending on your settings, the saved payment method on file might also be charged automatically on the billing cycle date. Learn more about the billing cycle date.
  7. (Optional) Add the default tax behavior, a coupon, a free trial, or metadata.
  8. (Optional) Enable revenue recovery features in the Dashboard, which can help you reduce and recover failed subscription payments. You can automatically retry failed payments, build custom automations, configure customer emails, and so on.


### Advanced options![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## Edit a subscription ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
To edit a subscription:
  1. Go to the subscriptions page.
  2. Find the subscription you want to modify, click the overflow menu (), then click **Update subscription**. You can also click the pencil icon () next to the subscription name. From this menu, you can also:
     * **Cancel the subscription**. In the modal that opens, select the date to cancel the subscription—immediately, at the end of the current period, or on a custom date. You can also select the option to refund the last payment for this subscription and create a credit note for your records.
     * **Pause payment collection**. In the modal that opens, select the duration of the pause—indefinite or ending on a custom date—and how invoices should behave during the pause.
     * **Share payment update link**. In the modal that opens, you can share a link with the customer to update their payment details. For more information, see Share payment update link.
  3. Make your changes to the subscription.
  4. Click **Update subscription**.


## Delete a subscription ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
You can’t delete a subscription. But you can cancel it or pause payment collection. See editing a subscription for those details.
## Subscriptions on mobile![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Use the Stripe Dashboard mobile app to create or manage subscriptions on your mobile device. (Currently only available on iOS only.)
  1. Go to the **Customers** tab.
  2. Select a customer.
  3. Tap the plus sign (**+**) in the subscription row. Alternatively, tap the overflow menu (), and select **Create subscription**.


You can only select existing products with a recurring price.
### Cancel a subscription from the mobile app ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  1. Go to **Payments > Subscriptions**.
  2. Select an active subscription.
  3. Tap **Cancel Subscription** in the action bar.


Currently, you can’t pause subscriptions using the app.
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
Create a subscription
Edit a subscription
Delete a subscription
Subscriptions on mobile
Cancel a subscription from the mobile app
Produits utilisés
Billing
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

