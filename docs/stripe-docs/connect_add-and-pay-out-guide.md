Accéder directement au contenu
Effectuer des virements
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
Encaisser des paiements et effectuer des virements
Permettre à d'autres entreprises d'accepter directement des paiements
Effectuer des virements
Développez une intégration Connect complète


Inscrire des comptes
Configurer les dashboards des comptes
Accepter des paiements
Effectuer des virements vers des comptes
Gérer votre plateforme Connect
Formulaires fiscaux pour votre plateforme Connect
Utiliser les types de comptes connectés
Intégration avec Accounts v2
Canada
Français (France)
AccueilPlateformes et places de marchéExample integrations
# Effectuer un virement
## Ajoutez de l'argent à votre solde Stripe et effectuez des virements à vos marchands ou prestataires de services.
#### Remarque
La plupart des plateformes peuvent uniquement virer des fonds vers les comptes connectés de la même région et dans des devises locales. Les plateformes établies aux États-Unis peuvent effectuer des virements internationaux vers des comptes situés dans d’autres régions, avec certaines restrictions.
API
Sans code
Utilisez ce guide pour découvrir comment ajouter des fonds au solde de votre compte et transférer des fonds vers les comptes bancaires de vos utilisateurs, sans traiter les paiements avec Stripe. Ce guide s’appuie sur l’exemple d’un produit de questions/réponses qui verse à ses auteurs une partie des revenus publicitaires générés par leurs réponses. La plateforme et les comptes connectés se situent tous les deux aux États-Unis.
Lorsque vous ajoutez des fonds à votre solde, la bonne pratique consiste à utiliser une fréquence de virements manuelle. Si vous activez les virements automatiques, vous ne pouvez pas vérifier si le système utilise des fonds supplémentaires dans le cadre de ces virements. Vous pouvez configurer votre fréquence de virements dans vos paramètres de virements.
#### Remarque
Seuls les membres de l’équipe disposant d’un accès d’administrateur au compte Stripe de la plateforme et ayant activé l’authentification à deux facteurs peuvent ajouter des fonds.
## Prérequis![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  1. Register your platform.
  2. Ajoutez des informations sur l’entreprise pour activer votre compte.
  3. Complétez votre profil de plateforme.
  4. Personnalisez vos paramètres de marque. Connect Onboarding nécessite l’ajout d’un nom d’entreprise, d’une icône et d’une couleur de marque.


## Créer un compte connecté![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Lorsqu’un utilisateur (marchand ou fournisseur de services) s’inscrit sur votre plateforme, créez un compte d’utilisateur (appelé _compte connecté_) afin de pouvoir accepter des paiements de sa part et transférer des fonds vers son compte bancaire. Les comptes connectés représentent vos utilisateurs dans l’API de Stripe et permettent de collecter plus facilement les informations dont Stripe a besoin pour vérifier l’identité de l’utilisateur. Dans le cadre du produit de questions/réponses qui rémunère les réponses fournies, le compte connecté représente l’auteur.
#### Remarque
Ce guide utilise des comptes Express, auxquels certaines restrictions s’appliquent. Vous avez également la possibilité d’évaluer des comptes Custom.
### Personnaliser votre formulaire d’inscription![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Dans les paramètres de votre plateforme, personnalisez votre formulaire d’inscription Express en modifiant la couleur et les logos présentés aux utilisateurs lorsqu’ils cliquent sur votre lien Connect.
![](https://b.stripecdn.com/docs-statics-srv/assets/oauth-form.4b13fc5edc56abd16004b4ccdff27fb6.png)
Formulaire d’inscription Express par défaut
![](https://b.stripecdn.com/docs-statics-srv/assets/branding-settings-payouts.20c99c810389a4e7f5c55238e80a9fc8.png)
Adaptation à votre marque
### Créer un lien de compte connecté![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez créer un lien d’inscription de compte connecté en cliquant sur **+Créer** sur la page d’aperçu des comptes, puis en sélectionnant le type de compte **Express** et la fonctionnalité **Transferts**. Cliquez sur **Continuer** pour générer un lien à envoyer à l’utilisateur que vous souhaitez inscrire.
![Create an account in the Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/create-account-unified.450b8fb21ed13bcc165baa7db225e157.png)
Créer un compte connecté
![](https://b.stripecdn.com/docs-statics-srv/assets/no-code-connect-express-link-unified.64f67a6c708c26fa52ec9b1ac1327b40.png)
Créer un lien d’inscription des utilisateurs
Ce lien redirige les utilisateurs vers un formulaire dans lequel ils peuvent fournir des informations pour se connecter à votre plateforme. Par exemple, si vous avez une plateforme de questions/réponses, vous pouvez fournir un lien permettant aux auteurs de se connecter à la plateforme. Ce lien est réservé uniquement au compte connecté que vous avez créé. Une fois que l’utilisateur a terminé le processus d’inscription, il apparaît dans la liste de vos comptes.
![](https://b.stripecdn.com/docs-statics-srv/assets/dashboard-account-payout.94e15f1be4a11a54d18fc305433e50f4.png)
## Ajouter des fonds à votre solde![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Pour ajouter des fonds, accédez à la section Solde du Dashboard. Cliquez sur **Ajouter des fonds à mon solde** et sélectionnez la raison pour laquelle vous ajoutez des fonds à votre compte.
![](https://b.stripecdn.com/docs-statics-srv/assets/add_funds_modal_with_issuing.f3dc58497698fb2a62b6461b7ed4fba6.png)
Sélectionnez l’option **Effectuer des virements vers des comptes connectés** pour ajouter des fonds à vos comptes connectés. Si vous ajoutez des fonds à votre solde en vue de futurs remboursements et litiges ou pour régulariser le solde négatif de votre plateforme, sélectionnez **Couvrir les soldes négatifs** et consultez la page Ajouter des fonds à votre solde Stripe.
### Vérifier votre compte bancaire![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Effectuez le processus de vérification dans le Dashboard la première fois que vous tentez d’ajouter des fonds depuis un compte non vérifié. Si votre compte bancaire n’est pas vérifié, vous devrez confirmer deux microversements venant de Stripe. Ces versements apparaîtront sur votre relevé bancaire en ligne sous la description `ACCTVERIFY` dans un délai de 1 à 2 jours ouvrables.
Stripe vous informe via le Dashboard et par e-mail lorsque les micro-versements devraient être arrivés dans votre compte. Pour terminer le processus de vérification, cliquez sur la notification du Dashboard dans la section Solde, saisissez les montants des deux micro-versements et cliquez sur **Vérifier le compte**.
![](https://b.stripecdn.com/docs-statics-srv/assets/top-ups4.85d1f2d8440f525714d0f2d20775e2d1.png)
### Ajouter des fonds![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Une fois vérifié, vous pouvez utiliser le Dashboard pour ajouter des fonds au solde de votre compte.
  1. Dans le Dashboard, accédez à la section Solde.
  2. Dans la fenêtre **Ajouter au solde** , saisissez un montant en USD, puis cliquez sur Virements Connect.
  3. Dans la fenêtre modale qui s’affiche (illustrée ci-dessous), saisissez un montant en USD.
  4. Vérifiez le montant et cliquez sur **Ajouter des fonds.**
  5. L’objet qui en résulte est une recharge qui est visible dans la section Recharges du Dashboard.


![](https://b.stripecdn.com/docs-statics-srv/assets/topup_modal.5523d356678b312020e4e063e7de8eb4.png)
### Consulter vos fonds![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez voir les fonds ajoutés dans le Dashboard sous l’onglet Recharges de la page Solde. Chaque fois que vous ajoutez des fonds, un objet recharge est créé avec un identifiant unique au format **tu_XXXXXX** , que vous pouvez consulter dans la vue détaillée de la recharge.
### Délai de règlement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Les plateformes basées aux États-Unis ajoutent des fonds via un prélèvement ACH. Les fonds sont disponibles dans votre solde Stripe sous 5 à 6 jours ouvrables. Si vous souhaitez bénéficier d’un délai de règlement plus rapide, contactez le service Support de Stripe pour demander l’examen de votre compte.
Lorsque votre compte sera un peu plus ancien, Stripe pourra peut-être réduire automatiquement le délai de règlement.
Vous pouvez ajouter des fonds pour de futurs remboursements ou litiges, ou bien pour régulariser un solde négatif en effectuant des virements bancaires. Ces fonds sont disponibles sous 1 à 2 jours ouvrables.
## Payer vos utilisateurs![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Une fois que votre utilisateur a terminé le processus d’inscription et que vous avez ajouté des fonds à votre solde, vous pouvez transférer une partie de votre solde vers vos comptes connectés. Dans cet exemple, des fonds sont transférés du solde de la plateforme de questions/réponses à l’auteur.
Pour payer votre utilisateur, rendez-vous dans la section **Solde** de la page des détails du compte, et cliquez sur **Ajouter des fonds**. Par défaut, tous les fonds que vous transférez vers un compte connecté s’ajoutent au solde Stripe de ce compte et sont versés quotidiennement. Vous pouvez modifier la fréquence des virements en cliquant sur le bouton tout à droite de la section **Solde** et en sélectionnant **Modifier la fréquence des virements**.
![](https://b.stripecdn.com/docs-statics-srv/assets/send-funds.5c34a4e2e038c3a5343c7aa165eb3787.png)
Envoyer des fonds aux utilisateurs
![](https://b.stripecdn.com/docs-statics-srv/assets/edit-payout-schedule.537eca9bac08a738533bd644e9dd2280.png)
Modifier la fréquence des virements
## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Gestion des comptes connectés dans le Dashboard


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
Prérequis
Créer un compte connecté
Personnaliser votre formulaire d’inscription
Créer un lien de compte connecté
Ajouter des fonds à votre solde
Vérifier votre compte bancaire
Ajouter des fonds
Consulter vos fonds
Délai de règlement
Payer vos utilisateurs
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

