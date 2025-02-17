Accéder directement au contenu
Permettre à d'autres entreprises d'accepter directement des paiements
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
# Permettre à d'autres entreprises d'accepter directement des paiements
## Facilitez les paiements directs entre d'autres entreprises et leurs propres clients.
Web
iOS
Android
React Native
Ce guide explique comment autoriser vos utilisateurs à accepter des paiements, transférer une partie des gains de vos utilisateurs vers votre solde et virer le reste sur les comptes bancaires de vos utilisateurs. Pour illustrer ces concepts, nous allons utiliser un exemple de plateforme qui permet aux entreprises de créer leurs propres boutiques en ligne.
## Prérequis![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  1. Register your platform.
  2. Ajoutez des informations sur l’entreprise pour activer votre compte.
  3. Complétez votre profil de plateforme.
  4. Personnalisez vos paramètres de marque. Connect Onboarding nécessite l’ajout d’un nom d’entreprise, d’une icône et d’une couleur de marque.


## Configurer Stripe
Côté serveur
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Installez les bibliothèques officielles de Stripe pour accéder à l’API depuis votre application :
Command Line
Ruby
```

# Available as a gem
sudo gem install stripe

```

Gemfile
Ruby
```

# If you use bundler, you can add this line to your Gemfile
gem 'stripe'

```

## Créer un compte connecté![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Lorsqu’un utilisateur (marchand ou fournisseur de services) s’inscrit sur votre plateforme, créez un compte d’utilisateur (appelé _compte connecté_) afin de pouvoir accepter des paiements de sa part et transférer des fonds vers son compte bancaire. Les comptes connectés représentent vos utilisateurs dans l’API de Stripe et permettent de collecter facilement les informations nécessaires pour vérifier leur identité. Dans notre exemple de création de boutique, le compte connecté représente l’entreprise qui configure sa boutique en ligne.
![Capture d'écran du formulaire Connect Onboarding](https://b.stripecdn.com/docs-statics-srv/assets/Kavholm-Seamless-Standard.78b64d90c0bf87130c8b6ba1ef53df7f.png)
### Créer un compte connecté et préremplir les informations![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Utilisez l’API `/v1/accounts` pour créer un compte connecté. Vous pouvez le créer en utilisant les paramètres par défaut du compte connecté ou en spécifiant le type de compte.
Avec les propriétés par défaut
Avec le type de compte
Command Line
cURL
```

curl -X POST https://api.stripe.com/v1/accounts \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:"

```

Si vous avez déjà collecté des informations pour vos comptes connectés, vous pouvez préremplir ces informations dans l’objet `Account`. Vous pouvez préremplir n’importe quelle information de compte, y compris des informations personnelles et professionnelles, des informations de compte externe, etc.
Connect Onboarding ne demande pas les informations préremplies. Cependant, il demande au titulaire du compte de confirmer les informations préremplies avant d’accepter le contrat d’utilisation du service Connect.
Lorsque vous testez votre intégration, préremplissez les informations du compte à l’aide des données de test.
### Créer un lien de compte![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez créer un lien de compte en appelant l’API Account Links avec les paramètres suivants :
  * `account`
  * `refresh_url`
  * `return_url`
  * `type` = `account_onboarding`


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
 --data-urlencoderefresh_url="https://example.com/reauth" \
 --data-urlencodereturn_url="https://example.com/return" \
 -dtype=account_onboarding

```

### Rediriger votre utilisateur vers l’URL du lien de compte![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
La réponse à votre requête Account Links contient une valeur d’`url` de clé. Redirigez l’utilisateur vers ce lien pour l’introduire dans le flux. Les liens de compte sont temporaires et à usage unique, car ils donnent accès aux informations personnelles du titulaire du compte connecté. Authentifiez l’utilisateur dans votre application avant de le rediriger vers cette URL. Si vous souhaitez préremplir des informations, vous devez le faire avant de générer le lien de compte. Une fois le lien créé, les opérations de lecture comme d’écriture ne seront plus possibles pour ce compte.
#### Conseil en matière de sécurité
N’envoyez pas d’URL de lien de compte par e-mail, SMS ou autre moyen de paiement en dehors de l’application de votre plateforme. Fournissez-les plutôt au titulaire du compte authentifié dans votre application.
### Gérer le retour de l’utilisateur sur votre plateforme![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Connect Onboarding vous demande de transmettre à la fois une `return_url` et une `refresh_url` afin de gérer tous les cas de redirection des utilisateurs vers votre plateforme. Il est important que vous les implémentiez correctement afin d’offrir à vos utilisateurs une expérience optimale.
#### Remarque
Vous pouvez fonctionner en HTTP pour vos `return_url` et `refresh_url` lorsque vous êtes en mode test (par exemple, pour les tests avec votre localhost), mais notez que le mode production n’accepte que le protocole HTTPS. Veillez à remplacer les URL de test par des URL HTTPS avant le lancement en mode production.
#### return_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe déclenche une redirection vers cette URL une fois que l’utilisateur a terminé son inscription Connect Onboarding. Ceci ne veut pas dire que toutes les informations ont été recueillies ni qu’il ne reste pas des conditions à remplir pour le compte, mais simplement que votre client est entré dans le flux et en est sorti sans que des soucis particuliers ne se posent.
Aucun état n’est transmis par cette URL. Une fois que l’utilisateur est redirigé vers votre `return_url`, vérifiez l’état du paramètre `details_submitted` sur son compte de l’une des manières suivantes :
  * Écouter les webhooks `account.updated`
  * Appeler l’API Accounts et inspecter l’objet renvoyé


#### refresh_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Votre utilisateur est redirigé vers l’URL `refresh_url` dans les cas suivants :
  * Le lien a expiré (quelques minutes se sont écoulées depuis la création du lien)
  * L’utilisateur a déjà utilisé le lien (il a actualisé la page ou cliqué sur le bouton Précédent ou Suivant de son navigateur)
  * Votre plateforme n’est plus en mesure d’accéder au compte
  * Le compte a été rejeté


Pour une expérience optimale, votre URL `refresh_url` doit déclencher une méthode permettant à votre serveur d’appeler à nouveau Account Links avec les mêmes paramètres, et de rediriger l’utilisateur vers le flux Connect Onboarding.
### Gérer les utilisateurs n’ayant pas finalisé leur inscription![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Si un utilisateur est redirigé vers votre `return_url`, il peut ne pas avoir finalisé son inscription. Utilisez l’endpoint `/v1/accounts` pour récupérer ses données de compte et vérifier le paramètre `charges_enabled`. Si l’inscription du compte n’a pas été finalisée, affichez des invites pour encourager l’utilisateur à poursuivre son inscription. Il pourra achever l’activation de son compte grâce à un nouveau lien de compte généré par votre intégration. Pour vérifier qu’il a bien finalisé son inscription, examinez l’état du paramètre `details_submitted` sur son compte.
## Activer des moyens de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Accédez aux paramètres des moyens de paiement et activez ceux que vous souhaitez prendre en charge. Les paiements par carte bancaire sont activés par défaut, mais vous pouvez activer et désactiver les moyens de paiement de votre choix en fonction de vos besoins. Ce guide suppose que Bancontact, les cartes bancaires, EPS, iDEAL, Przelewy24, le prélèvement automatique SEPA et Sofort sont activés.
Avant que le formulaire de paiement ne s’affiche, Stripe évalue la devise, les restrictions en matière de moyens de paiement ainsi que d’autres paramètres pour dresser la liste des moyens de paiement pris en charge. Ceux qui augmentent le taux de conversion et qui sont les plus pertinents pour la devise et le lieu de résidence du client sont automatiquement priorisés. Ceux de moindre priorité ne sont accessibles que via un menu déroulant.
#### Version bêta privée
Le **composant intégré des paramètres de moyens de paiement** permet aux comptes connectés de configurer les moyens de paiement qu’ils proposent sans avoir besoin d’accéder au Dashboard Stripe. Demandez un accès et découvrez comment l’intégrer avec Payment Method Configurations.
## Accepter un paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Intégrez Stripe Checkout comme formulaire de paiement directement sur votre site web ou redirigez les utilisateurs vers une page préconfigurée hébergée par Stripe pour accepter les paiements. Checkout prend en charge de nombreux moyens de paiement et affiche automatiquement les plus pertinents pour votre client. Vous pouvez également utiliser l’Element de paiement, un composant d’interface utilisateur préconfiguré intégré sous forme d’iframe dans votre formulaire de paiement, pour accepter plusieurs moyens de paiement avec une seule intégration front-end.
Page hébergée par Stripe
Formulaire intégré
Flux personnalisé
### Créer une session Checkout Client-side Server-side![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Une session Checkout détermine ce que votre client voit sur le formulaire de paiement intégré, notamment les postes de facture, le montant et la devise de la commande, ainsi que les moyens de paiement acceptés. Dans le cas de paiements directs, Checkout utilise les paramètres de branding du compte connecté. Pour en savoir plus, consultez la section Personnaliser l’image de marque.
Les utilisateurs ne sont pas responsables des paiements indirects et des paiements et transferts distincts. En revanche, c’est à eux qu’il revient de gérer les litiges concernant les paiements directs, et non à la plateforme.
Sur votre serveur, effectuez l’appel suivant à l’API Stripe. Après avoir créé une session Checkout, redirigez votre client vers l’URL renvoyée dans la réponse.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/checkout/sessions \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -H"Stripe-Account: 
{{CONNECTED_ACCOUNT_ID}}
" \
 -dmode=payment \
 -d"line_items[0][price]"=
{{PRICE_ID}}
 \
 -d"line_items[0][quantity]"=1 \
 -d"payment_intent_data[application_fee_amount]"=123 \
 --data-urlencodesuccess_url="https://example.com/success" \
 --data-urlencodecancel_url="https://example.com/cancel"

```

  * `line_items` : cet argument représente les postes achetés par votre client, qui apparaîtront dans l’interface utilisateur hébergée.
  * `success_url` : cet argument assure la redirection de l’utilisateur une fois le paiement effectué.
  * `cancel_url` : cet argument assure la redirection de l’utilisateur dès lors qu’il annule l’opération.
  * `Stripe-Account` : cet en-tête indique un paiement direct pour votre compte connecté. Avec les paiements directs, le compte connecté assume les frais Stripe, les remboursements et les contestations de paiement. La marque du compte connecté est utilisée dans Checkout, ce qui donne l’impression aux clients d’être en contact directement avec le marchand et non avec votre plateforme.
  * (Facultatif) `payment_intent_data[application_fee_amount]` : cet argument précise le montant que votre plateforme prévoit de prélever sur la transaction. Après le traitement du paiement sur le compte connecté, le montant `application_fee_amount` est transféré sur la plateforme et les frais Stripe sont déduits du solde du compte connecté.


![Flux de création de compte](https://b.stripecdn.com/docs-statics-srv/assets/direct_charges.a2a8b68037ac95fe22140d6dde9740d3.svg)
### Gérer les événements après le paiement Server-side![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe envoie un événement checkout.session.completed à l’issue du paiement. Utilisez un webhook pour recevoir ces événements et exécuter des actions en conséquence, comme l’envoi d’un e-mail de confirmation de commande à votre client, l’enregistrement de la vente dans une base de données ou le lancement d’un flux de livraison.
Nous vous conseillons d’écouter ces événements plutôt que d’attendre un rappel du client. Côté client, il arrive en effet que l’utilisateur ferme la fenêtre de son navigateur ou quitte l’application avant l’exécution du rappel. Avec certains moyens de paiement, la confirmation du paiement peut par ailleurs prendre entre 2 et 14 jours. Configurer votre intégration de manière à ce qu’elle écoute les événements asynchrones vous permettra d’accepter plusieurs moyens de paiement avec une seule intégration.
En plus de gérer l’événement `checkout.session.completed`, nous vous recommandons de gérer deux autres événements lorsque vous encaissez des paiements avec Checkout :
Événement| Description| Étapes suivantes  
---|---|---  
checkout.session.completed| Le client a autorisé le paiement en envoyant le formulaire Checkout.| Attendez que le paiement aboutisse ou échoue.  
checkout.session.async_payment_succeeded| Le paiement du client a abouti.| Traitez la commande de biens ou de services de votre client.  
checkout.session.async_payment_failed| Le paiement a été refusé, ou il a échoué pour une autre raison.| Contactez votre client par e-mail et demandez-lui de passer une nouvelle commande.  
Ces événements incluent tous l’objet Checkout Session. Une fois le paiement effectué, l’état sous-jacent du PaymentIntent passe de `processing` à `succeeded`.
## Test![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Testez votre flux de création de compte en créant des comptes et en utilisant OAuth. Testez vos paramètres de **moyens de paiement** pour vos comptes connectés en vous connectant à l’un de vos comptes test et en accédant aux paramètres de moyens de paiement. Testez votre tunnel de paiement à l’aide de vos clés et d’un compte test. Vous pouvez utiliser nos cartes de test pour tester votre tunnel de paiement et simuler divers scénarios.
## Virements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Par défaut, les paiements que vous créez pour un compte connecté viennent s’ajouter au solde Stripe de ce compte et sont versés sur une base quotidienne. Les comptes connectés peuvent gérer la fréquence de leurs virements dans leur Dashboard Stripe.
## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Gérer des comptes connectés dans le Dashboard
  * Émettre des remboursements
  * Personnaliser les libellés de relevé bancaire
  * Gérer plusieurs devises


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
Configurer Stripe
Créer un compte connecté
Créer un compte connecté et préremplir les informations
Créer un lien de compte
Rediriger votre utilisateur vers l’URL du lien de compte
Gérer le retour de l’utilisateur sur votre plateforme
Gérer les utilisateurs n’ayant pas finalisé leur inscription
Activer des moyens de paiement
Accepter un paiement
Créer une session Checkout
Gérer les événements après le paiement
Test
Virements
Voir aussi
Produits utilisés
Connect
Checkout
Elements
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

