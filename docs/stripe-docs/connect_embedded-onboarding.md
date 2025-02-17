Accéder directement au contenu
Inscription des utilisateurs intégrée
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
AccueilPlateformes et places de marchéOnboard accountsChoose your onboarding configuration
#### Remarque
Cette page n'est pas encore disponible dans cette langue. Nous faisons tout notre possible pour proposer notre documentation dans davantage de langues et nous vous fournirons la version traduite dès qu'elle sera disponible.
# Embedded onboarding
## Show a localized onboarding form that validates data.
Embedded onboarding is a highly themeable onboarding UI with limited Stripe branding. You embed the Account onboarding component in your platform application, and your connected accounts interact with the embedded component without ever leaving your application.
The component supports Legal Entity Sharing, which allows owners of multiple Stripe accounts to share business information between them. When they onboard an account, they can reuse that information from an existing account instead of resubmitting it.
Embedded onboarding uses the Accounts API to read the requirements and generate an onboarding form with robust data validation, localized for all Stripe-supported countries. In addition, embedded onboarding handles all:
  * Business types
  * Configurations of company representatives
  * Verification document uploading
  * Identity verification and statuses
  * International bank accounts
  * Error states


Taille
Bureau
Paramètres régionaux
Français (France)
Cette démonstration est en lecture seule et ses fonctionnalités sont limitées. Pour bénéficier d'une démonstration complète, rendez-vous sur le site furever.dev.
## Create an account and prefill information
Server-side
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Create a connected account with the default controller properties. See design an integration to learn more about controller properties. Alternatively, you can create a connected account by specifying an account type.
With controller properties
With account type
Command Line
cURL
```

curl -X POST https://api.stripe.com/v1/accounts \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:"

```

If you know the country for your connected account, you can provide that information when you create the account. The country defaults to the same country as your platform if not provided.
To request capabilities for your connected account, you can provide that information when you create the account. Stripe’s onboarding UIs automatically collect the requirements for those capabilities. To reduce onboarding effort, request only the capabilities you need. If you omit capabilities, and your connected account has access to the full Stripe Dashboard or the Express Dashboard, capabilities are automatically requested. For accounts with access to the Express dashboard, Stripe-hosted onboarding uses the Configuration settings to request capabilities based on the account’s country.
If you have information about the account holder (like their name, address, or other details), you can proactively provide this when you create or update the account. Stripe-hosted onboarding asks the account holder to confirm the pre-filled information before accepting the Connect service agreement. Providing more information through the API reduces the number of prompts and enhances the onboarding flow for your connected account.
Additionally, if you onboard an account without its own website and your platform provides the account with a URL, prefill the account’s business_profile.url. If the account doesn’t have a URL, you can prefill its business_profile.product_description instead.
When testing your integration, use test data to simulate different outcomes including identity verification, business information verification, payout failures, and more.
## Determine the information to collect![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
As the platform, you must decide if you want to collect the required information from your connected accounts upfront or incrementally. Upfront onboarding collects the `eventually_due` requirements for the account, while incremental onboarding only collects the `currently_due` requirements.
Upfront onboarding | Incremental onboarding   
---|---  
**Advantages**| 
  * Entails a single request for information (normally)
  * Creates fewer problems in receiving payouts and maintaining processing ability
  * Exposes potential fraudsters or connected accounts who refuse to provide required information later

| 
  * Onboards connected accounts quickly
  * Results in higher onboarding rates

  
**Disadvantages**| 
  * Onboarding connected accounts can take longer
  * Some legitimate new connected accounts might turn away due to the amount of information required before they complete the onboarding process

| 
  * Creates a higher likelihood of disrupting business of an ongoing connected account

  
To determine whether to use upfront or incremental onboarding, review the required information for the countries where your connected accounts are located to understand the requirements that are eventually due. While Stripe tries to minimize any impact to connected accounts, requirements might change over time.
For connected accounts where you’re responsible for requirement collection, you can customize the behavior of future requirements using the `collection_options` parameter. Set `collection_options.future_requirements` to `include` to collect the account’s future requirements.
For connected accounts where you’re responsible for requirement collection, you can customize the behavior of future requirements using the `collectionOptions` attribute when integrating the Account onboarding component. Set `collectionOptions.futureRequirements` to `include` which collects the account’s future requirements.
## Customize the policies shown to your users![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Connected accounts see Stripe’s service agreement and Privacy Policy during embedded onboarding. Connected account users who haven’t accepted Stripe’s services agreement must accept it on the final onboarding screen. Embedded onboarding also has a footer with links to Stripe’s service agreement and Privacy Policy.
For connected accounts where the platform is responsible for requirement collection, you have additional options to customize the onboarding flow, as outlined below.
### Handle service agreement acceptance on your own![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
If you’re a platform onboarding connected accounts where you’re responsible for requirement collection, you can collect Terms of Service acceptance using your own process instead of using the embedded account onboarding component. If using your own process, the final onboarding screen only asks your connected accounts to confirm the information they entered, and you must secure their acceptance of Stripe’s service agreement.
Embedded onboarding still has links to the terms of service (for example, in the footer) that you can replace by linking to your own agreements and privacy policy.
### Link to your agreements and privacy policy ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Connected accounts see the Stripe service agreement and Privacy Policy throughout embedded onboarding. For the connected accounts where you’re responsible for requirement collection, you can replace the links with your own agreements and policy. Follow the instructions to incorporate the Stripe services agreement and link to the Stripe Privacy Policy.
## Integrate the account onboarding component
Server-side
Client-side
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Create an Account Session by specifying the ID of the connected account and `account_onboarding` as the component to enable.
## Create an Account Session![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
When creating an Account Session, enable account onboarding by specifying `account_onboarding` in the `components` parameter.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/account_sessions \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -daccount=
{{CONNECTED_ACCOUNT_ID}}
 \
 -d"components[account_onboarding][enabled]"=true \
 -d"components[account_onboarding][features][external_account_collection]"=true

```

After creating the Account Session and initializing ConnectJS, you can render the Account onboarding component in the front end:
account-onboarding.js
JavaScript
```

// Include this element in your HTMLconst accountOnboarding = stripeConnectInstance.create('account-onboarding');
accountOnboarding.setOnExit(()=>{
 console.log('User exited the onboarding flow');});
container.appendChild(accountOnboarding);// Optional: make sure to follow our policy instructions above// accountOnboarding.setFullTermsOfServiceUrl('{{URL}}')// accountOnboarding.setRecipientTermsOfServiceUrl('{{URL}}')// accountOnboarding.setPrivacyPolicyUrl('{{URL}}')// accountOnboarding.setSkipTermsOfServiceCollection(false)// accountOnboarding.setCollectionOptions({//  fields: 'eventually_due',//  futureRequirements: 'include',// })// accountOnboarding.setOnStepChange((stepChange) => {//  console.log(`User entered: ${stepChange.step}`);// });

```

HTML + JS
React
Method| Type| Description| Default  
---|---|---|---  
`setFullTermsOfServiceUrl`| `string`| Absolute URL to your full terms of service agreement.| Stripe’s full service agreement  
`setRecipientTermsOfServiceUrl`| `string`| Absolute URL to your recipient terms of service agreement.| Stripe’s recipient service agreement  
`setPrivacyPolicyUrl`| `string`| Absolute URL to your privacy policy.| Stripe’s privacy policy  
`setSkipTermsOfServiceCollection`| `string`| If true, embedded onboarding skips terms of service collection and you must collect terms acceptance yourself.| false  
`setCollectionOptions`| `{ fields: 'currently_due' | 'eventually_due', future_requirements: 'omit' | 'include' }`| Customizes collecting `currently_due` or `eventually_due` requirements and controls whether to include future requirements. Specifying `eventually_due` collects both `eventually_due` and `currently_due` requirements.| `{fields: 'currently_due', futureRequirements: 'omit'}`  
`setOnExit`| `() => void`| The connected account has exited the onboarding process  
`setOnStepChange`| `({step}: StepChange) => void`| The connected account has navigated from one step to another within the onboarding process. See the step change object for a full reference and restrictions.  
To use this component to set up new accounts:
  1. Create a connected account. You can prefill information on the account object in this API call.
  2. Initialize Connect embedded components using the ID of the connected account.
  3. Include the `account-onboarding` element to show the onboarding flow to the connected account.
  4. Listen for the `exit` event emitted from this component. Stripe sends this event when the connected account exits the onboarding process.
  5. When `exit` triggers, retrieve account details to check the status of details_submitted, charges_enabled, payouts_enabled, and other capabilities. If all required capabilities are enabled, you can take the account to the next step of your flow.


#### The `stepchange` object![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Every time the connected account navigates from one step to another in the onboarding process, a `stepchange` object is passed to the step change handler with the following properties.
Name| Type| Example value  
---|---|---  
`step`| `string` See the possible step values| `business_type`  
The unique reference to an onboarding step.  
##### Restrictions![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * The `stepchange` object is only for analytics.
  * Steps can appear in any order and can be repeated.
  * Possible `step` values can change at any time.


#### Step Values![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Each page in onboarding has a unique step name. This `step` is an exhaustive list of pages the user could see in the onboarding process. These values can change at any time without notice.
Steps| Description  
---|---  
`stripe_user_authentication`| User authentication includes a popup to a Stripe-owned window. The connected account must authenticate before they can continue their workflow.  
`risk_intervention`| Guides the connected account to resolve risk-related requirements.  
`legal_entity_sharing`| Connected accounts can optionally reuse existing information when onboarding new accounts.  
`business_type`| Sets the business type of the connected account. In certain cases the connected account can also set their country.  
`business_details`| Collects information related to the connected account’s business.  
`business_verification`| Collects a proof of entity document establishing the business’ entity ID number, such as the company’s articles of incorporation. Or allows users to correct wrongly entered information related to the entity.  
`business_bank_account_ownership_verification`| Collects documents needed to verify that bank account information, such as the legal owner’s name and account number, match the information on the user’s Stripe account.  
`business_documents`| Collects other documents and verification requirements related to the business.  
`representative_details`| Collects information about the account representative.  
`representative_document`| Collects a government-issued ID verifying the existence of the account representative.  
`representative_additional_document`| Collects an additional document to verifying the details of the account representative.  
`legal_guardian_details`| Collects the legal guardians consent for accounts opened by minors.  
`owners`| Collects information about the beneficial owners of a company.  
`directors`| Collects information about the directors of a company.  
`executives`| Collects information about the executives of a company.  
`confirm_owners`| Allows connected accounts to attest that the beneficial owner information provided to Stripe is both current and correct.  
`risa_compliance_survey`| Answers questions concerning the Revised Installment Sales Act. (only for Japan)  
`treasury_and_card_issuing_terms_of_service`| Collects Treasury and Card Issuing terms of service when requesting those capabilities.  
`external_account`| Collects the external account of the connected account.  
`support_details`| Collects information that helps customers recognize the connected accounts business. This support information may be visible in payment statements, invoices, and receipts.  
`climate`| Allows a connected account to opt into Stripe Climate.  
`tax`| Allows a connected account to opt into Stripe Tax.  
`summary`| Final review step of onboarding. The connected account can update entered information from this step. The terms of service and privacy URL is displayed in this screen.  
`summary_risk`| From the summary step, a connected account can update information related to risk requirements.  
`summary_business_type`| From the summary step, a connected account can update information related to their business type.  
`summary_business`| From the summary step, a connected account can update information related to their business.  
`summary_support`| From the summary step, a connected account can update information related to their businesses public facing information.  
`summary_persons`| From the summary step, a connected account can update information about each person on their account.  
`summary_external_account`| From the summary step, a connected account can update information related to their external account.  
`summary_tax`| From the summary step, a connected account can update information related to their Stripe Tax integration.  
`summary_tax_identification_form`| From the summary step, a connected account can update information related to their W8/W9 certified tax information. This is shown when Stripe must collect W8/W9 information.  
`summary_climate`| From the summary step, a connected account can update information related to their Stripe Climate integration.  
## Handle new requirements becoming due
Server-side
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Set up your integration to listen for changes to account requirements. You can test handling new requirements (and how they might disable charges and payouts) with the test mode trigger cards.
Based on your application’s verification requirements, send the connected account back through onboarding when it has `currently_due` or `eventually_due` requirements. Use these signals to determine when it’s necessary to re-initiate onboarding for a connected account.
You don’t need to worry about determining which requirements are missing. Onboarding collects the necessary information. For example, if there’s a typo preventing verification, onboarding prompts the connected account to upload an identity document (such as a Driver’s License in the United States). If any information is missing, onboarding requests it.
Stripe notifies you about any upcoming requirements updates that affect your connected accounts. You can proactively collect this information by reviewing the future requirements for your accounts.
### Handle verification errors ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Listen to the account.updated event. If the account contains any `currently_due` fields when the `current_deadline` arrives, the corresponding functionality is disabled and those fields are added to `past_due`.
Let your accounts remediate their verification requirements by directing them to the Account onboarding component.
account.updated event
If `requirements.currently_due` contains fields
Direct account to onboarding in time to finish before current_deadline
No action required
If `requirements.past_due` contains fields
Account possibly disabled; direct it to onboarding
Render the Account onboarding component
YesYesNoNo
### Disable Stripe user authentication ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
When using embedded onboarding, Stripe user authentication is enabled by default. You can use `disable_stripe_user_authentication` to remove this behavior.
We recommend implementing two-factor authentication or equivalent security measures as a best practice. For account configurations that support this feature, such as Custom, you assume liability for connected accounts if they can’t pay back negative balances.
## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Get started with Connect embedded components
  * Customize embedded components


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
Create an account and prefill information
Determine the information to collect
Customize the policies shown to your users
Handle service agreement acceptance on your own
Link to your agreements and privacy policy
Integrate the account onboarding component
Create an Account Session
Handle new requirements becoming due
Handle verification errors
Disable Stripe user authentication
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

