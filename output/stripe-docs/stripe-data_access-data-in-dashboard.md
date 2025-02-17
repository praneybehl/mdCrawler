Accéder directement au contenu
Access Stripe data using Sigma
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
Billing
Tax
Rapports
Données
Présentation
Démarrer
Access Stripe data using Sigma
Accéder aux données de votre entrepôt de données avec Data Pipeline
Actualisation des données
Importer et gérer des données
Interroger des données
Écrire des requêtes
Interroger des données transactionnelles
Faire une recherche dans les données de litige et de fraude
Interroger des données Billing
Interroger des données fiscales
Interroger toutes les données de frais
Interroger des données Connect
Interroger des données Issuing
Interroger plusieurs comptes
Planifier des requêtes
Migrer des requêtes


Constitution de start-up
Canada
Français (France)
AccueilAutomatisation des opérations financièresData
#### Remarque
Cette page n'est pas encore disponible dans cette langue. Nous faisons tout notre possible pour proposer notre documentation dans davantage de langues et nous vous fournirons la version traduite dès qu'elle sera disponible.
# Access Stripe data using Sigma
## Generate custom reports for charges, refunds, disputes, and more with Sigma.
Sigma makes all your transactional data available within an interactive SQL environment in the Stripe Dashboard. It lets you create fully customized reports using information about your payments, subscriptions, customers, payouts, and so on.
With Sigma, you can:
  * Get information that best reflects your business and Stripe integration.
  * Export in CSV format to import into your tools.
  * Fetch data on a schedule of your choosing.


## Create a custom report ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Reports give you the data required for your accounting and reconciliation workflows. To create a report, query the assistant or write your own report with SQL. The reports you generate can differ from those you generate on the Stripe Dashboard in the following ways:
  * **Data availability:** For financial reports, you can find the most recent day of available data by selecting **month to date** or opening the date picker calendar. In Sigma, the `data_load_time` parameter provides the timestamp that data is available through.
  * **Time zone:** Financial reports in the Stripe Dashboard filter reports by the local time zone by default, but you can switch them to use the UTC time zone. Sigma filters templates by the UTC time zone.
  * **Date range:** A selected date range for Stripe Dashboard financial reports, such as Jan. 13 to Jan. 14, filters reports from January 13 00:00:00 up to January 14 23:59:59. A chosen date range filter for Sigma templates for January 13 to January 14 filters reports from Jan 13 00:00:00 up to January 13 23:59:59.
  * **Currency:** Financial reports in the Stripe Dashboard always filter data to a single currency. By default, the Sigma report templates return all currencies. You can add a `WHERE` clause to your Sigma query to restrict your results to a single currency.
  * **Metadata:** Financial reports allow you to include metadata. Sigma templates don’t include it. You can add metadata to your reports by following the `Metadata to column` Sigma template.


Reports follow the same availability rules as the Stripe Dashboard. Payout Reconciliation reports are only available for users with the **Automatic payouts** setting enabled, and connect variants of reports are only available for users on Stripe Connect.
### Report templates ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
You can also create a report using a template. By default, these reports run on the last completed month that all data is available for. To change the dates, make a copy of the template and edit the report date intervals. Use the listed templates to generate their related reports and their connected variants:
Report group| Sigma template name| API report type  
---|---|---  
**Balance report** | Itemized balance change from activity| `balance_change_from_activity.itemized.3`  
Itemized payouts| `payouts.itemized.3`  
**Payout reconciliation report** | Itemized payout reconciliation| `payout_reconciliation.itemized.5`  
Itemized ending balance reconciliation| `ending_balance_reconciliation.itemized.4`  
## Unsubscribing from Sigma ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
If you currently have an active Sigma subscription and want to cancel it, go to your Sigma settings and click **Cancel Stripe Sigma subscription**. You can continue using Sigma until the end of the billing cycle, at which point the subscription ends.
## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Query transaction data
  * Query Billing data
  * Sigma and Data Pipeline for Connect platforms
  * Query Issuing data
  * Query all fees data
  * Schedule queries with Sigma
  * Migrate queries onto the new Sigma version


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
Create a custom report
Report templates
Unsubscribing from Sigma
Voir aussi
Produits utilisés
Sigma
Payments
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

