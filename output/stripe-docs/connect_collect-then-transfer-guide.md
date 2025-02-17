Accéder directement au contenu
Encaisser des paiements et effectuer des virements
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
# Encaisser des paiements, puis effectuer des virements
## Encaissez les paiements de vos clients puis effectuez les virements vers vos marchands ou fournisseurs de services.
Web
iOS
Android
React Native
Sans code
Ce guide vous explique comment accepter les paiements et transférer des fonds vers les comptes bancaires de vos prestataires de services ou marchands. À des fins d’illustration, nous allons créer une place de marché de location immobilière qui met en relation des propriétaires et des locataires potentiels. Nous vous montrerons comment accepter les paiements des locataires (clients) et régler les propriétaires (utilisateurs de votre plateforme).
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
Lorsqu’un utilisateur (vendeur ou fournisseur de services) s’inscrit sur votre place de marché, vous devez créer un compte correspondant à cet utilisateur (appelé _compte connecté_). Sans cela, vous ne pourrez pas accepter de paiements de la part du compte bancaire de cet utilisateur ni lui transférer de fonds. Les comptes connectés représentent vos utilisateurs dans l’API Stripe et collectent les informations nécessaires pour vérifier leur identité. Dans notre exemple de location immobilière, le compte connecté représente le propriétaire.
### Créer un compte connecté et préremplir les informations![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Utilisez l’API `/v1/accounts` pour créer un compte connecté en spécifiant les propriétés du compte connecté ou le type de compte.
Avec les propriétés du contrôleur
Avec le type de compte
Command Line
cURL
```

curlhttps://api.stripe.com/v1/accounts \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -d"controller[losses][payments]"=application \
 -d"controller[fees][payer]"=application \
 -d"controller[stripe_dashboard][type]"=express

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
La réponse à votre requête Account Links inclut une valeur pour la clé `url`. Redirigez l’utilisateur vers ce lien pour le faire entrer dans le flux. Les URL provenant de l’API Account Links sont temporaires et ne peuvent être utilisées qu’une seule fois, car elles donnent accès aux informations personnelles de l’utilisateur du compte connecté. Procédez à l’authentification de l’utilisateur dans votre application avant de le rediriger vers cette URL. Si vous souhaitez préremplir les informations, vous devez le faire avant de générer le lien de compte. Une fois le lien de compte créé, les opérations de lecture comme d’écriture ne seront plus possibles pour ce compte connecté.
#### Conseil en matière de sécurité
N’envoyez pas d’URL de lien de compte par e-mail, SMS ou autre moyen de paiement en dehors de l’application de votre plateforme. Fournissez-les plutôt au titulaire du compte authentifié dans votre application.
### Gérer la redirection de l’utilisateur vers votre plateforme![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Connect Onboarding vous demande de transmettre à la fois une `return_url` et une `refresh_url` afin de gérer tous les cas de redirection des utilisateurs vers votre plateforme. Il est important que vous les implémentiez correctement afin d’offrir à vos utilisateurs une expérience optimale.
#### Remarque
Vous pouvez fonctionner en HTTP pour vos `return_url` et `refresh_url` lorsque vous êtes en mode test (par exemple, pour les tests avec votre localhost), mais notez que le mode production n’accepte que le protocole HTTPS. Veillez à remplacer les URL de test par des URL HTTPS avant le lancement en mode production.
#### return_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe déclenche une redirection vers cette URL une fois que l’utilisateur a terminé son inscription Connect Onboarding. Ceci ne veut pas dire que toutes les informations ont été recueillies ni qu’il ne reste pas des conditions à remplir pour le compte, mais simplement que l’entrée de votre client dans le flux et sa sortie se sont déroulées correctement.
Aucun état n’est transmis par cette URL. Une fois que l’utilisateur est redirigé vers votre `return_url`, vérifiez l’état du paramètre `details_submitted` sur son compte de l’une des manières suivantes :
  * En écoutant les webhooks `account.updated`
  * Appeler l’API Accounts et inspecter l’objet renvoyé


#### refresh_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe redirige votre utilisateur vers la `refresh_url` dans les cas suivants :
  * Le lien a expiré (quelques minutes se sont écoulées depuis sa création).
  * L’utilisateur a déjà utilisé l’URL (il a actualisé la page ou cliqué sur le bouton Précédent ou Suivant de son navigateur).
  * Votre plateforme n’est plus en mesure d’accéder au compte.
  * Le compte a été rejeté.


Pour une expérience optimale, votre URL `refresh_url` doit déclencher une méthode permettant à votre serveur d’appeler à nouveau Account Links avec les mêmes paramètres, et de rediriger l’utilisateur vers le flux Connect Onboarding.
### Gérer les utilisateurs dont l’inscription n’est pas terminée![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Un utilisateur redirigé vers votre `return_url` peut ne pas avoir terminé son inscription. Utilisez l’endpoint `/v1/accounts` pour récupérer ses données de compte et vérifier le paramètre `charges_enabled`. Si l’inscription du compte n’a pas été finalisée, affichez des invites pour encourager l’utilisateur à poursuivre son inscription. Il pourra achever l’activation de son compte grâce à un nouveau lien de compte (généré par votre intégration). Vous pourrez vérifier l’état du paramètre `details_submitted` sur son compte pour voir s’il a terminé son inscription.
## Activer des moyens de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Accédez aux paramètres des moyens de paiement de votre Dashboard et activez ceux que vous souhaitez prendre en charge. Les paiements par carte bancaire, Google Pay et Apple Pay sont activés par défaut, mais vous pouvez activer et désactiver les moyens de paiement de votre choix selon vos besoins.
Avant que le formulaire de paiement ne s’affiche, Stripe évalue la devise, les restrictions relatives aux moyens de paiement ainsi que d’autres paramètres pour dresser la liste des moyens de paiement pris en charge. Ceux qui augmentent le taux de conversion et qui sont les plus pertinents selon la devise et le lieu de résidence du client sont automatiquement présentés en priorité. Les moyens de paiement de moindre priorité ne sont visibles qu’au sein d’un menu de débordement.
## Accepter un paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Utilisez Stripe Checkout pour accepter des paiements. Checkout prend en charge de nombreux moyens de paiement et affiche automatiquement les plus pertinents pour votre client. Vous pouvez accepter des paiements avec Checkout à l’aide d’une page hébergée par Stripe ou ajouter un formulaire de paiement intégré préconfiguré directement sur votre site Web. Vous pouvez également créer un flux personnalisé (à l’aide du Payment Element) pour accepter plusieurs moyens de paiement avec une seule intégration front-end.
Page hébergée par Stripe
Formulaire intégré
Flux personnalisé
### Créer une session Checkout Client and Server![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Une session Checkout détermine ce que votre client voit sur la page de paiement hébergée par Stripe, tel que les postes de la facture, le montant et la devise de la commande, ainsi que les moyens de paiement acceptés.
Ajoutez à votre site Web un bouton de paiement qui appelle un endpoint côté serveur afin de créer une session Checkout.
checkout.html
```

<html><head><title>Checkout</title></head><body><formaction="/create-checkout-session"method="POST"><buttontype="submit">Checkout</button></form></body></html>

```

Sur votre serveur, effectuez l’appel suivant à l’API Stripe. Après avoir créé une session Checkout, redirigez votre client vers l’URL renvoyée dans la réponse.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/checkout/sessions \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -dmode=payment \
 -d"line_items[0][price]"=
{{PRICE_ID}}
 \
 -d"line_items[0][quantity]"=1 \
 -d"payment_intent_data[application_fee_amount]"=123 \
 -d"payment_intent_data[transfer_data][destination]"=
{{CONNECTED_ACCOUNT_ID}}
 \
 --data-urlencodesuccess_url="https://example.com/success" \
 --data-urlencodecancel_url="https://example.com/cancel"

```

  * `line_items` : cet argument spécifie les articles achetés par votre client. Ces articles sont affichés dans l’interface utilisateur hébergée par Stripe.
  * `success_url` : cet argument assure la redirection de l’utilisateur une fois le paiement effectué.
  * `cancel_url` : cet argument assure la redirection de l’utilisateur dès lors qu’il annule l’opération.
  * `payment_intent_data[application_fee_amount]` : cet argument précise le montant que votre plateforme prévoit de prélever sur la transaction. Une fois le paiement capturé, le montant total du paiement est immédiatement transféré depuis la plateforme vers le compte connecté spécifié par le paramètre `transfer_data[destination]`. Ensuite, le montant `application_fee_amount` est à nouveau transféré vers la plateforme, et les frais Stripe sont déduits de ce montant.
  * `payment_intent_data[transfer_data][destination]` : cet argument indique qu’il s’agit d’un paiement indirect. Un paiement indirect désigne un paiement traité sur la plateforme et pour lequel les fonds sont ensuite immédiatement et automatiquement transférés vers le solde en attente du compte connecté. Dans le cadre de notre exemple de location immobilière, nous voulons créer les conditions permettant au client de payer via la plateforme, et au propriétaire d’être payé par la plateforme.


![](https://b.stripecdn.com/docs-statics-srv/assets/application_fee_amount.837aa2339469b3c1a4319672971c1367.svg)
Checkout utilise les paramètres de marque du compte de votre plateforme pour les paiements indirects. Pour en savoir plus, consultez Personnaliser l’image de marque.
Cette session crée un paiement indirect. Si vous souhaitez choisir à quel moment les transferts ont lieu ou transférer des fonds vers plusieurs bénéficiaires, utilisez plutôt des paiements et transferts distincts. Pour utiliser des paiements distincts, consultez Permettre à d’autres entreprises d’accepter directement des paiements.
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
Testez votre flux de création de comptes en créant des comptes et en utilisant OAuth.
Cartes bancaires
Portefeuilles
Virements avec redirection bancaire
Prélèvements bancaires
Coupons
Numéro de carte| Scénario| Méthode de test  
---|---|---  
4242424242424242| Le paiement par carte bancaire aboutit et ne nécessite pas d’authentification.| Remplissez le formulaire de paiement par carte bancaire en saisissant le numéro de carte ainsi que la date d’expiration, le CVC et le code postal de votre choix.  
4000002500003155| Le paiement par carte bancaire requiert une authentification.| Remplissez le formulaire de paiement par carte bancaire en saisissant le numéro de carte ainsi que la date d’expiration, le CVC et le code postal de votre choix.  
4000000000009995| La carte est refusée avec un code de refus de type `insufficient_funds`.| Remplissez le formulaire de paiement par carte bancaire en saisissant le numéro de carte ainsi que la date d’expiration, le CVC et le code postal de votre choix.  
6205500000000000004| La carte UnionPay a un numéro d’une longueur variable, allant de 13 à 19 chiffres.| Remplissez le formulaire de paiement par carte bancaire en saisissant le numéro de carte ainsi que la date d’expiration, le CVC et le code postal de votre choix.  
Consultez la section consacrée aux tests pour obtenir des informations supplémentaires sur la manière de tester votre intégration.
## Litiges![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Votre plateforme étant l’entité de règlement pour les paiements, elle est à ce titre responsable des litiges. Assurez-vous de prendre connaissance des bonnes pratiques en matière de résolution de litiges.
## Virements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Par défaut, tous les fonds que vous transférez vers un compte connecté s’accumulent sur le solde Stripe et sont virés quotidiennement. Vous pouvez modifier la fréquence de virement depuis la page des détails du compte connecté, en cliquant sur le bouton tout à droite de la section **Solde** et en sélectionnant **Modifier la fréquence des virements**.
## Remboursements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Pour émettre des remboursements, accédez à la page Paiements. Sélectionnez les paiements pour lesquels un remboursement doit être effectué en cochant la case à leur gauche. Après avoir sélectionné un paiement, Stripe affiche un bouton **Rembourser** dans le coin supérieur droit de la page. Cliquez sur le bouton **Rembourser** pour émettre un remboursement aux clients pour tous les paiements que vous venez de sélectionner.
#### Remarque
Les comptes connectés ne peuvent pas initier de remboursements pour les paiements effectués à partir du Dashboard Express. Si vos comptes connectés utilisent le Dashboard Express, vous devez traiter les remboursements pour eux.
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
Gérer la redirection de l’utilisateur vers votre plateforme
Gérer les utilisateurs dont l’inscription n’est pas terminée
Activer des moyens de paiement
Accepter un paiement
Créer une session Checkout
Gérer les événements après le paiement
Test
Litiges
Virements
Remboursements
Voir aussi
Produits utilisés
Connect
Checkout
Payment Links
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

