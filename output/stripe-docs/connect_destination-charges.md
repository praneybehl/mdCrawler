Accéder directement au contenu
Paiement indirect
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
Créer un paiement
Paiements directs
Paiement indirect
Paiements et transferts distincts
Définir des libellés de relevé bancaire
Définir les codes de catégories de marchands (CCM)
Gérer plusieurs devises
Créer des liens de paiement avec Connect
Utiliser Radar avec Connect
Créer des abonnements
Créer des factures
Configurations de moyens de paiement multiples
Intégrer le composant des paramètres des moyens de paiement
Solde du compte


Effectuer des virements vers des comptes
Gérer votre plateforme Connect
Formulaires fiscaux pour votre plateforme Connect
Utiliser les types de comptes connectés
Intégration avec Accounts v2
Canada
Français (France)
AccueilPlateformes et places de marchéAccept paymentsCreate a charge
# Créer des paiements indirects
## Créez des paiements sur votre compte de plateforme, percevez les frais et transférez immédiatement les fonds restants vers vos comptes connectés.
Créez des _paiements indirects_ lorsque les clients effectuent des transactions sur votre plateforme pour des produits ou des services proposés par vos comptes connectés et transférez immédiatement des fonds vers vos comptes connectés. Avec ce type de paiement :
  * Vous créez un paiement sur le compte de votre plateforme.
  * Vous déterminez si ces fonds sont à transférer partiellement ou en totalité dans votre compte connecté.
  * Le solde de votre compte sera débité du coût de la commission Stripe, des remboursements et des contestations de paiement.


Ce type de paiement est le mieux adapté aux places de marché telles qu’Airbnb (location de logements) ou Lyft (covoiturage).
Les paiements indirects ne sont pris en charge que si votre plateforme et le compte connecté se trouvent dans le même pays. Pour la prise en charge des paiements transfrontaliers, vous devez indiquer le marchand de règlement au compte connecté en utilisant le paramètre on_behalf_of sur le Payment Intent ou d’autres scénarios de transferts transfrontaliers valides.
#### Remarque
Nous vous recommandons d’utiliser les paiements indirects pour les comptes connectés qui ont accès au Dashboard Express ou aucun accès au Dashboard.
Web
iOS
Android
React Native
Page hébergée par Stripe
Formulaire intégré
Flux personnalisé
Redirigez vers une page de paiement hébergée par Stripe à l’aide de Stripe Checkout. Comparez cette intégration aux autres types d’intégration de Stripe.
![Aperçu de Checkout](https://b.stripecdn.com/docs-statics-srv/assets/b2c79a23390b89a7b589d29387f3e2b2.png)
### Effort d'intégration
Low-code
### Type d'intégration
Redirection vers la page de paiement hébergée par Stripe
### Personnalisation de l'interface utilisateur
Personnalisation limitée
Essayer
Tout d’abord, inscrivez-vous pour créer un Compte Stripe.
Utilisez nos bibliothèques officielles pour accéder à l’API Stripe depuis votre application :
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

## Créer une session Checkout
Côté client
Côté serveur
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Une session Checkout contrôle ce que le client voit dans le formulaire de paiement, tel que les postes, le montant de la commande, la devise et les moyens de paiement acceptés. Ajoutez à votre site Web un bouton de paiement qui appelle un endpoint côté serveur pour créer une session Checkout.
checkout.html
```

<html><head><title>Checkout</title></head><body><formaction="/create-checkout-session"method="POST"><buttontype="submit">Checkout</button></form></body></html>

```

Destination
Pour le compte de
Sur votre serveur, créez une session Checkout et redirigez votre client vers l’URL renvoyée dans la réponse.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/checkout/sessions \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -d"line_items[0][price_data][currency]"=usd \
 -d"line_items[0][price_data][product_data][name]"=T-shirt \
 -d"line_items[0][price_data][unit_amount]"=1000 \
 -d"line_items[0][quantity]"=1 \
 -d"payment_intent_data[application_fee_amount]"=123 \
 -d"payment_intent_data[transfer_data][destination]"=
{{CONNECTED_ACCOUNT_ID}}
 \
 -dmode=payment \
 --data-urlencodesuccess_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}"

```

  * `payment_intent_data[transfer_data][destination]` : ce paramètre indique qu’il s’agit d’un paiement indirect. Un paiement indirect désigne un paiement traité sur la plateforme et pour lequel les fonds sont ensuite immédiatement et automatiquement transférés vers le solde en attente du compte connecté.
  * `line_items` : ce paramètre spécifie les articles achetés par votre client. Ces articles sont affichés dans le formulaire de paiement intégré.
  * `success_url` : Stripe redirige le client vers l’URL de réussite après un paiement réussi et remplace la chaîne `{CHECKOUT_SESSION_ID}` par l’ID de session Checkout. Vous pouvez l’utiliser pour récupérer la session Checkout et inspecter son état afin de choisir ce que vous voulez montrer au client. Vous pouvez également ajouter vos propres paramètres de requête, qui persistent tout au long du processus de redirection. Consultez la page Personnaliser le comportement de redirection avec une page hébergée par Stripe pour en savoir plus.
  * `payment_intent_data[application_fee_amount]` : ce paramètre précise le montant que votre plateforme prévoit de prélever sur la transaction. Une fois le paiement capturé, le montant total du paiement est immédiatement transféré depuis la plateforme vers le compte connecté spécifié par le paramètre `transfer_data[destination]`. Ensuite, le montant `application_fee_amount` est à nouveau transféré vers la plateforme, et les frais Stripe sont déduits de ce montant.


Client
Plateforme
Compte connecté
Paiement de 10 $
Transfert de 10 $
Paiement de 10 $
(1,23 $) Commission de la plateforme
8,77 $ net
Commission de la plateforme de 1,23 $
(0,59 $) Frais Stripe
Stripe
0,64 $ net
Lors du traitement des paiements indirects, Checkout utilise les paramètres de marque du compte de votre plateforme. Pour en savoir plus, consultez la section consacrée à la personnalisation des paramètres de marque.
## Gérer les événements post-paiement
Côté serveur
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe envoie un événement checkout.session.completed à l’issue du paiement. Utilisez un webhook pour recevoir ces événements et exécuter des actions en conséquence, comme l’envoi d’un e-mail de confirmation de commande à votre client, l’enregistrement de la vente dans une base de données ou le lancement d’un flux de livraison.
Nous vous conseillons d’écouter ces événements plutôt que d’attendre un rappel du client. Côté client, il arrive en effet que l’utilisateur ferme la fenêtre de son navigateur ou quitte l’application avant l’exécution du rappel. Avec certains moyens de paiement, la confirmation du paiement peut par ailleurs prendre entre 2 et 14 jours. Configurer votre intégration de manière à ce qu’elle écoute les événements asynchrones vous permettra d’accepter plusieurs moyens de paiement avec une seule intégration.
Stripe recommande de gérer tous les événements suivants lors de la collecte de paiements avec Checkout :
Événement| Description| Étapes suivantes  
---|---|---  
checkout.session.completed| Le client a autorisé le paiement en envoyant le formulaire Checkout.| Attendez que le paiement aboutisse ou échoue.  
checkout.session.async_payment_succeeded| Le paiement du client a abouti.| Traitez la commande de biens ou de services de votre client.  
checkout.session.async_payment_failed| Le paiement a été refusé ou a échoué pour une autre raison.| Contactez le client par e-mail et demandez-lui de passer une nouvelle commande.  
Ces événements incluent tous l’objet Checkout Session. Une fois le paiement effectué, le PaymentIntent passe de état sous-jacent `processing` à `succeeded` ou à un état d’échec.
## Tester l'intégration![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
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
## FacultatifActiver d'autres moyens de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## Percevoir des frais![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez percevoir des frais avec un application_fee_amount ou un transfer_data[amount].
application_fee_amount
transfer_data[amount]
Lorsque vous créez des paiements avec un paramètre `application_fee_amount`, la totalité du montant du paiement est transférée de la plateforme vers le compte `transfer_data[destination]` directement après la capture du paiement. Le montant des commissions, `application_fee_amount` (qui ne peut dépasser le montant du paiement) est ensuite de nouveau transféré, du compte vers la plateforme.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/checkout/sessions \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -d"line_items[0][price_data][currency]"=usd \
 -d"line_items[0][price_data][product_data][name]"=T-shirt \
 -d"line_items[0][price_data][unit_amount]"=1000 \
 -d"line_items[0][quantity]"=1 \
 -d"payment_intent_data[application_fee_amount]"=123 \
 -d"payment_intent_data[transfer_data][destination]"=
{{CONNECTED_ACCOUNT_ID}}
 \
 -dmode=payment \
 --data-urlencodesuccess_url="https://example.com/success"

```

Une fois les commissions de plateforme perçues, un objet Application Fee est créé. Vous pouvez afficher une liste des commissions de plateforme dans le Dashboard, avec les commissions de plateforme ou dans Sigma. Vous pouvez également utiliser la propriété `amount` de l’objet Application Fee pour établir des rapports détaillés sur les frais.
Lorsque vous utilisez `application_fee_amount`, il convient de savoir les choses suivantes :
  * Le `application_fee_amount` est plafonné au montant total de la transaction.
  * Le montant `application_fee_amount` est toujours calculé dans la même devise que la transaction.
  * La commission de la plateforme est libellée dans la même devise que la devise de règlement du compte connecté. Dans le cas des paiements indirects transfrontaliers, elle peut être différente de la devise de règlement de votre plateforme.
  * Votre plateforme paie les frais Stripe après le transfert du `application_fee_amount` dans votre compte.
  * Aucune commission Stripe supplémentaire n’est appliquée au montant.
  * Votre plateforme peut utiliser le reporting intégré des commissions de plateforme pour rapprocher les commissions encaissées.
  * Dans les Dashboards ou les composants hébergés par Stripe, tels que le composant d’informations de paiement, votre compte connecté peut afficher à la fois le montant total et le montant des commissions de la plateforme.


### Mouvements de fonds![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Avec le code ci-dessus, le montant total du paiement (10 USD) est ajouté au solde en attente du compte connecté. La somme correspondant au paramètre `application_fee_amount` (1,23 USD) est déduite du montant du paiement et transférée sur votre plateforme. Les frais Stripe (0,59 USD) sont déduits du solde du compte de votre plateforme. Le montant de la commission de plateforme moins les frais Stripe (1,23 USD - 0,59 USD = 0,64 USD) reste dans le solde du compte de votre plateforme.
![Mouvements de fonds pour les paiements indirects](https://b.stripecdn.com/docs-statics-srv/assets/destination_charge_app_fee.c9ef81298155b38f986df02d0efa9167.png)
Le montant `application_fee_amount` devient disponible selon la fréquence normale de transfert sur le compte la plateforme, tout comme les fonds provenant des paiements ordinaires Stripe.
## Personnaliser l’image de marque![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Votre plateforme utilise les paramètres de marque du Dashboard pour personnaliser l’image de marque sur la page des paiements. Pour les paiements indirects, Checkout utilise les paramètres de marque du compte de la plateforme. Pour les paiements indirects avec `on_behalf_of`, Checkout utilise les paramètres de marque du compte connecté.
Les plateformes peuvent configurer les paramètres de marque des comptes connectés à l’aide de l’API Update Account :
  * `icon` : s’affiche à côté du nom de l’entreprise dans l’en-tête de la page Checkout.
  * `logo` : utilisé à la place de l’icône et du nom de l’entreprise dans l’en-tête de la page Checkout.
  * `primary_color` : utilisé comme couleur d’arrière-plan sur la page Checkout.
  * `secondary_color` : utilisé comme couleur des boutons sur la page Checkout.


Command Line
cURL
```

curlhttps://api.stripe.com/v1/accounts/
{{CONNECTED_ACCOUNT_ID}}
 \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -d"settings[branding][icon]"=
{{FILE_ID}}
 \
 -d"settings[branding][logo]"=
{{FILE_ID}}
 \
 --data-urlencode"settings[branding][primary_color]"="#663399" \
 --data-urlencode"settings[branding][secondary_color]"="#4BB543"

```

## Sélectionner l’entité de règlement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Le choix de l’entité de règlement dépend des fonctionnalités définies sur un compte et de la manière dont un paiement est créé. L’entité de règlement détermine quelles seront les informations à utiliser pour effectuer le paiement. Elles comprennent le libellé du relevé (celui de la plateforme ou celui du compte connecté) affiché sur la carte de crédit du client ou le relevé bancaire pour ce paiement.
Préciser l’entité de règlement vous permet d’être plus explicite concernant les personnes pour lesquelles les paiements doivent être créés. Par exemple, certaines plateformes préfèrent être l’entité de règlement parce que le client final communique directement avec leur plateforme (comme dans le cas des plateformes à la demande). Cependant, certaines plateformes ont des comptes connectés qui communiquent directement avec les clients finaux (par exemple, une vitrine sur une plateforme d’e-commerce). Dans ce scénario, il est plus logique que le compte connecté soit l’entité de règlement.
Vous pouvez définir le paramètre `on_behalf_of` sur l’ID d’un compte connecté pour faire de ce compte l’entité de règlement pour le paiement. Lorsque vous utilisez `on_behalf_of` :
  * Les paiements sont réglés dans le pays et dans la devise de règlement du compte connecté.
  * La structure des frais appliquée est celle du pays du compte connecté.
  * Le libellé de relevé bancaire du compte connecté apparaît sur le relevé de carte bancaire du client.
  * Si le compte connecté relève d’un autre pays que celui de la plateforme, l’adresse et le numéro de téléphone du compte connecté sont affichés sur le relevé de carte bancaire du client.
  * Le nombre de jours durant lesquels un solde en attente est bloqué avant d’être versé dépend du paramètre delay_days du compte connecté.


Si le paramètre `on_behalf_of` est ignoré, la plateforme est l’entreprise de référence pour le paiement.
#### Mise en garde
Le paramètre `on_behalf_of` est uniquement pris en charge pour les comptes connectés disposant d’une fonctionnalité de paiement comme card_payments. Les comptes soumis au contrat de service pour les bénéficiaires ne peuvent pas demander `card_payments` ou d’autres fonctionnalités de paiement.
## Émettre des remboursements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Si vous utilisez l’API Payment Intents, les remboursements doivent être émis sur le dernier paiement créé.
Les paiements créés sur le compte de la plateforme peuvent être remboursés en utilisant la clé secrète du compte de la plateforme. Lorsque vous remboursez un paiement comportant un `transfer_data[destination]`, par défaut le compte de destination garde les fonds transférés, laissant le compte de la plateforme couvrir le solde négatif du remboursement. Pour récupérer les fonds du compte connecté afin de couvrir le remboursement, définissez le paramètre `reverse_transfer` sur `true` lors de la création du remboursement :
Command Line
curl
```

curlhttps://api.stripe.com/v1/refunds\ -u 
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
: \ -dcharge="{CHARGE_ID}"\ -dreverse_transfer=true \

```

Par défaut, la totalité du paiement est remboursée, mais vous pouvez créer un remboursement partiel en définissant le paramètre `amount` sur un nombre entier positif.
Si le remboursement entraîne le remboursement de la totalité du paiement, la totalité du transfert est annulée. Dans le cas contraire, un montant proportionnel du transfert est annulé.
### Rembourser les commissions de la plateforme![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Lorsque vous remboursez un paiement comportant une commission de la plateforme, par défaut le compte de la plateforme garde les fonds correspondant à la commission. Pour rediriger ces fonds vers le compte connecté, définissez le paramètre refund_application_fee sur `true` lors de la création du remboursement :
Command Line
curl
```

curlhttps://api.stripe.com/v1/refunds\ -u 
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
: \ -dcharge="{CHARGE_ID}"\ -dreverse_transfer=true \ -drefund_application_fee=true \

```

Notez que si vous remboursez la commission de la plateforme pour un paiement indirect, vous devez également annuler le transfert. Si le remboursement se traduit par le remboursement de la totalité du paiement, la totalité de la commission est également remboursée. Dans le cas contraire, un montant proportionnel de la commission est remboursé.
Vous pouvez également indiquer la valeur **false** pour `refund_application_fee` et rembourser la commission de la plateforme séparément via l’API.
### Remboursements ayant échoué![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Si un remboursement échoue ou si vous l’annulez, le montant du remboursement ayant échoué est recrédité sur le solde Stripe de votre compte de plateforme. Créez un transfert pour envoyer les fonds vers le compte connecté, le cas échéant.
## Gérer les litiges![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Pour les paiements indirects, avec ou sans le paramètre `on_behalf_of`, Stripe débite le montant du litige et les frais de votre compte de plateforme.
We recommend setting up a webhook to listen to dispute created events. When that happens, you can attempt to recover funds from the connected account by reversing the transfer through the Dashboard or by creating a transfer reversal.
If the connected account has a negative balance, Stripe attempts to debit its external account if `debit_negative_balances` is set to `true`.
If you challenge the dispute and win, you can transfer the funds that you previously reversed back to the connected account. If your platform has an insufficient balance, the transfer fails. Prevent insufficient balance errors by adding funds to your Stripe balance.
#### Erreur fréquente
Retransferring a previous reversal is subject to cross-border transfer restrictions, meaning you might have no means to repay your connected account. Instead, wait to recover disputed cross-border payment transfers for destination charges with `on_behalf_of` until after a dispute is lost.
## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Gérer plusieurs devises
  * Libellés de relevé bancaire avec Connect


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
Créer une session Checkout
Gérer les événements post-paiement
Tester l'intégration
Percevoir des frais
Mouvements de fonds
Personnaliser l’image de marque
Sélectionner l’entité de règlement
Émettre des remboursements
Rembourser les commissions de la plateforme
Remboursements ayant échoué
Gérer les litiges
Voir aussi
Produits utilisés
Connect
Checkout
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

