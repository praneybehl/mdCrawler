Accéder directement au contenu
Stripe-hosted onboarding
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
# Inscription des utilisateurs hébergée par Stripe
## Inscrivez des comptes connectés en les redirigeant vers un flux d'inscription hébergé par Stripe.
L’inscription hébergée par Stripe gère la collecte des informations sur l’entreprise et sur la vérification de l’identité des comptes connectés, réduisant drastiquement les efforts requis de la part de la plateforme. Il s’agit d’un formulaire Web hébergé par Stripe qui s’affiche de manière dynamique selon les fonctionnalités, le pays et le type d’entreprise de chaque compte connecté.
L’inscription hébergée par Stripe prend en charge le partage d’entité juridique, qui permet aux propriétaires de plusieurs comptes Stripe de partager des informations sur leur entreprise. Lors de l’inscription d’un compte, ils peuvent réutiliser les informations d’un compte existant au lieu de les soumettre à nouveau.
![](https://b.stripecdn.com/docs-statics-srv/assets/hosted_onboarding_form.37ff5a6f7d39a33ebda671e33419971c.png)
Le formulaire d’inscription hébergée pour l’exemple d’intégration de Stripe, Rocket Deliveries.
## Personnaliser le formulaire d'inscription
Dashboard
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez personnaliser l’aspect visuel du formulaire avec le nom, la couleur et l’icône de votre marque en accédant à la page des paramètres Connect dans le Dashboard. L’inscription hébergée par Stripe nécessite ces informations. Stripe recommande également de recueillir les informations bancaires de vos comptes connectés lors de leur inscription.
## Créer un compte et pré-remplir les informations
Côté serveur
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Créez un compte connecté avec les propriétés par défaut du contrôleur. Pour en savoir plus sur les propriétés des contrôleurs, consultez la section Concevoir une intégration. Vous pouvez également créer un compte connecté en spécifiant un type de compte.
Avec les propriétés du contrôleur
Avec un type de compte
Command Line
cURL
```

curl -X POST https://api.stripe.com/v1/accounts \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:"

```

Si vous connaissez le pays de votre compte connecté, vous pouvez fournir ces informations au moment de la création du compte. S’il n’est pas fourni, le pays est par défaut le même que celui de votre plateforme.
To request capabilities for your connected account, you can provide that information when you create the account. Stripe’s onboarding UIs automatically collect the requirements for those capabilities. To reduce onboarding effort, request only the capabilities you need. If you omit capabilities, and your connected account has access to the full Stripe Dashboard or the Express Dashboard, capabilities are automatically requested. For accounts with access to the Express dashboard, Stripe-hosted onboarding uses the Configuration settings to request capabilities based on the account’s country.
Si vous disposez d’informations sur le titulaire du compte (comme son nom, son adresse, etc.), vous pouvez les fournir de manière proactive lorsque vous créez ou mettez à jour le compte. L’inscription hébergée par Stripe demande au titulaire du compte de confirmer les informations préremplies avant d’accepter le contrat de service Connect. Le fait de fournir plus d’informations via l’API permet de réduire le nombre d’invites et d’améliorer le flux d’inscription de votre compte connecté.
En outre, si vous inscrivez un compte qui ne dispose pas de son propre site Web et que votre plateforme lui fournit une URL, préremplissez la business_profile.url du compte. Si le compte n’a pas d’URL, vous pouvez préremplir sa business_profile.product_description à la place.
Lorsque vous testez votre intégration, utilisez des données de test pour simuler différents résultats, notamment la vérification d’identité, la vérification des informations de l’entreprise, les échecs de virement, etc.
## Déterminer les informations à collecter![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
En tant que plateforme, vous devez décider entre collecter toutes les informations requises auprès de vos comptes connectés au début du processus (inscription complète), ou les recueillir progressivement (inscription progressive). L’inscription complète collecte les exigences `eventually_due` pour le compte, tandis que l’inscription progressive collecte uniquement les exigences `currently_due`.
Inscription complète| Inscription progressive des utilisateurs  
---|---  
**Avantages**| 
  * Ne comporte habituellement qu’une seule demande d’informations
  * Génère moins de problèmes de réception des virements et de maintien de la capacité de traitement
  * Révèle les potentiels fraudeurs ou les comptes connectés qui refuseraient de fournir les informations requises par la suite

| 
  * Inscription rapide des comptes connectés
  * Génère des taux d’inscription plus élevés

  
**Inconvénients**| 
  * L’inscription des comptes connectés peut prendre plus de temps
  * Certains nouveaux comptes connectés légitimes risquent de quitter la page en raison de la quantité d’informations requises avant de terminer le processus d’inscription

| 
  * La probabilité de perturber l’activité d’un compte connecté existant est plus importante

  
Pour déterminer si vous devez utiliser l’inscription complète ou progressive, consultez les informations requises selon les pays de vos comptes connectés pour comprendre quelles seront les exigences attendues à l’avenir. Stripe s’efforce de minimiser son impact sur les comptes connectés, cependant, les exigences sont susceptibles d’évoluer.
For connected accounts where you’re responsible for requirement collection, you can customize the behavior of future requirements using the `collection_options` parameter. Set `collection_options.future_requirements` to `include` to collect the account’s future requirements.
## Créer un lien de compte
Côté serveur
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Créez un lien de compte en utilisant l’ID du compte connecté et en incluant une URL de rafraîchissement ainsi qu’une URL de redirection. Stripe redirige le compte connecté vers l’URL de rafraîchissement si l’URL du lien de compte a déjà été visitée, a expiré ou n’est pas valide. Stripe redirige les comptes connectés vers l’URL de redirection lorsqu’ils ont terminé ou quitté le flux d’inscription. De plus, en fonction des informations que vous avez besoin de recueillir, vous pouvez transmettre soit `currently_due`, soit `eventually_due` pour le paramètre `collection_options.fields`. Dans cet exemple, l’option `eventually_due` est transmise pour utiliser l’inscription complète. L’option `currently_due` est, quant à elle, transmise pour l’inscription progressive.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/account_links \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -daccount=
{{CONNECTED_ACCOUNT_ID}}
 \
 --data-urlencoderefresh_url="https://example.com/refresh" \
 --data-urlencodereturn_url="https://example.com/return" \
 -dtype=account_onboarding \
 -d"collection_options[fields]"=eventually_due

```

### Rediriger votre compte connecté vers l’URL de lien de compte![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Redirigez le compte connecté vers l’URL de lien de compte pour l’envoyer vers le flux d’inscription. Chaque URL de lien de compte ne peut être utilisée qu’une seule fois car elle donne accès aux informations personnelles du titulaire du compte. Identifiez le compte dans votre application avant de le rediriger vers cette URL.
## Traiter les nouvelles exigences qui arrivent à échéance
Côté serveur
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Set up your integration to listen for changes to account requirements. You can test handling new requirements (and how they might disable charges and payouts) with the test mode trigger cards.
Based on your application’s verification requirements, send the connected account back through onboarding when it has `currently_due` or `eventually_due` requirements. Use these signals to determine when it’s necessary to re-initiate onboarding for a connected account.
You don’t need to worry about determining which requirements are missing. Onboarding collects the necessary information. For example, if there’s a typo preventing verification, onboarding prompts the connected account to upload an identity document (such as a Driver’s License in the United States). If any information is missing, onboarding requests it.
Stripe notifies you about any upcoming requirements updates that affect your connected accounts. You can proactively collect this information by reviewing the future requirements for your accounts.
### Gérer les erreurs de vérification![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Écoutez l’événement account.updated. Si le compte contient des champs `currently_due` à l’arrivée de la date `current_deadline`, la fonctionnalité correspondante est désactivée et ces champs sont ajoutés à `past_due`.
Laissez vos comptes remplir les exigences de vérification en les dirigeant vers le formulaire de l’inscription hébergée par Stripe.
Événement account.updated
Si `requirements.currently_due` contient des champs
Dirigez le compte vers le processus d’inscription suffisamment tôt pour que celui-ci soit terminé avant la date current_deadline
Aucune action requise
Si `requirements.past_due` contient des champs
Le compte est peut-être désactivé ; dirigez-le vers le flux d’inscription
Rediriger vers le formulaire de l’inscription hébergée par Stripe
OuiOuiNonNon
## Gérer le retour du compte connecté vers votre plateforme![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Le lien de compte nécessite une `refresh_url` et une `return_url` pour gérer tous les cas de redirection des comptes connectés vers votre plateforme. Il est important de les mettre en œuvre correctement afin de fournir le meilleur flux d’inscription pour vos comptes connectés.
#### Remarque
Vous pouvez utiliser le protocole HTTP pour vos `refresh_url` et `return_url` lorsque vous êtes en mode test (par exemple, pour tester localement). Cependant, en mode production, seul le protocole HTTPS est accepté. Veillez à remplacer toutes les URL de test par des URL avec le protocole HTTPS avant le lancement en mode production.
### URL d’actualisation![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Votre compte connecté est redirigé vers l’URL `refresh_url` lorsque :
  * Le lien a expiré (quelques minutes se sont écoulées depuis la création du lien).
  * Le lien a déjà été visité (le compte connecté a actualisé la page ou a cliqué sur le bouton **précédent** ou **suivant**).
  * Le lien a été partagé dans une application tierce, comme un client de messagerie, qui tente d’accéder à l’URL pour afficher en un aperçu. De nombreux clients visitent automatiquement les liens, ce qui entraîne leur expiration.


La `refresh_url` doit appeler une méthode sur votre serveur pour créer un nouveau lien de compte avec les mêmes paramètres et rediriger le compte connecté vers la nouvelle URL de lien de compte.
### URL de redirection![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe redirige le compte connecté vers cette URL lorsqu’il termine le flux d’inscription ou qu’il clique sur **Enregistrer pour plus tard** à n’importe quel moment du flux. Cela **ne signifie pas** que toutes les informations ont été recueillies ou que toutes les exigences du compte ont été satisfaites. Cela signifie uniquement que l’entrée et la sortie du flux ont fonctionné correctement.
Aucun état n’est transmis avec cette URL. Une fois qu’un compte connecté est redirigé vers `return_url`, vérifiez si le compte a terminé son inscription. Récupérez le compte et vérifiez l’attribut exigences pour les exigences en attente. Vous pouvez également écouter l’événement `account.updated` envoyé à votre endpoint de webhook et mettre en cache l’état du compte dans votre application. Si le compte n’a pas terminé son inscription, incluez des invites dans votre application pour lui permettre de continuer l’inscription plus tard.
## Gestion des mises à jour initiées par le compte connecté![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
L’inscription hébergée par Stripe prend également en charge les mises à jour initiées par le compte connecté des informations qu’il a déjà fournies. Lorsque vous créez un lien de compte, vous pouvez définir le `type` comme étant soit `account_onboarding`, soit `account_update`.
### Inscription des comptes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Les liens de compte de ce type fournissent un formulaire permettant de saisir des exigences en attente. Utilisez-le lors de l’inscription d’un nouveau compte connecté ou lorsqu’un utilisateur existant a de nouvelles exigences (par exemple, lorsqu’un compte connecté a déjà fourni suffisamment d’informations mais que vous avez demandé une nouvelle fonctionnalité qui nécessite des informations supplémentaires). Dirigez l’utilisateur vers ce type de lien de compte pour recueillir les nouvelles informations dont vous avez besoin.
### Mise à jour du compte![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Les liens de compte de ce type sont activés pour les comptes desquels votre plateforme est responsable de la collecte des exigences. Les liens `account_update` affichent les attributs déjà renseignés sur le compte et permettent à votre compte connecté de modifier les informations précédemment fournies (par exemple, pour mettre à jour leur adresse). Ajoutez une option dans votre application (par exemple, « Modifier mon profil » ou « Mettre à jour mes informations de vérification ») pour permettre aux comptes connectés d’effectuer eux-mêmes les mises à jour.
## Navigateurs pris en charge![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
L’inscription hébergée par Stripe prend en charge :
  * Les 20 dernières versions majeures de Chrome et Firefox
  * Les deux dernières versions majeures de Safari et Edge
  * Les deux dernières versions majeures de Safari mobile sur iOS


L’inscription hébergée par Stripe est uniquement prise en charge dans les navigateurs Web. Elle ne peut pas être utilisée dans des vues Web intégrées à des applications mobiles ou de bureau.
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
Personnaliser le formulaire d'inscription
Créer un compte et pré-remplir les informations
Déterminer les informations à collecter
Créer un lien de compte
Rediriger votre compte connecté vers l’URL de lien de compte
Traiter les nouvelles exigences qui arrivent à échéance
Gérer les erreurs de vérification
Gérer le retour du compte connecté vers votre plateforme
URL d’actualisation
URL de redirection
Gestion des mises à jour initiées par le compte connecté
Inscription des comptes
Mise à jour du compte
Navigateurs pris en charge
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

