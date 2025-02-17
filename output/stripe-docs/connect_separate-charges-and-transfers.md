Accéder directement au contenu
Paiements et transferts distincts
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
# Création de paiements et de transferts distincts
## Comment créer des frais sur votre compte Connect et transférer des fonds vers plusieurs comptes connectés.
Créez des _paiements et des transferts distincts_ pour transférer des fonds vers plusieurs comptes connectés, ou lorsqu’un utilisateur spécifique n’est pas connu au moment du paiement. Le paiement sur votre compte de plateforme est dissocié des transferts vers vos comptes connectés. Avec ce type de paiement :
  * Vous créez un paiement sur le compte de votre plateforme et transférez également des fonds à vos comptes connectés. Le paiement apparaît comme tel sur votre compte, et il y a également des transferts vers des comptes connectés (dont vous déterminez le montant), qui sont prélevés du solde de votre compte.
  * Vous pouvez transférer des fonds vers plusieurs comptes connectés.
  * Le solde de votre compte sera débité du coût des frais Stripe, des remboursements et des contestations de paiement.


Ce type de frais convient mieux aux places de marché qui doivent répartir les paiements entre plusieurs parties, comme DoorDash, une plateforme de livraison de plats à domicile.
Stripe prend en charge des paiements et transferts distincts dans les régions suivantes :
Allemagne
Australie
Autriche
Belgique
Brésil
Bulgarie
Canada
Chypre
Croatie
Danemark
Espagne
Estonie
États-Unis
Finlande
France
Grèce
Hongrie
Irlande
Italie
Japon
Lettonie
Liechtenstein
Lituanie
Luxembourg
Malaisie
Malte
Mexique
Norvège
Nouvelle-Zélande
Pays-Bas
Pologne
Portugal
République tchèque
Roumanie
Royaume-Uni
Singapour
Slovaquie
Slovénie
Suède
Suisse
Dans la plupart des cas, votre plateforme et le compte connecté doivent se trouver dans la même région. Toute tentative de transfert de fonds au-delà d’une frontière non autorisée renvoie une erreur. Pour en savoir plus sur la prise en charge interrégionale, veuillez consulter la section transferts internationaux. Vous ne devez utiliser les transferts qu’en combinaison avec les cas d’utilisation autorisés pour les paiements, les recharges et les frais.
#### Remarque
Nous vous recommandons d’utiliser les paiements et transferts distincts pour les comptes connectés qui ont accès au Dashboard Express ou aucun accès au Dashboard.
Web
iOS
Android
React Native
Page hébergée par Stripe
Formulaire intégré
Flux personnalisé
Redirigez vers une page de paiement hébergée par Stripe à l’aide de Stripe Checkout. Voyez comment cette intégration se compare aux autres types d’intégration de Stripe.
![Aperçu de Checkout](https://b.stripecdn.com/docs-statics-srv/assets/b2c79a23390b89a7b589d29387f3e2b2.png)
### Effort d'intégration
Low-code
### Type d'intégration
Redirection vers la page de paiement hébergée par Stripe
### Personnalisation de l'interface utilisateur
Personnalisation limitée
Try it out
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

Sur votre serveur, créez une session Checkout et redirigez votre client vers l’URL renvoyée dans la réponse.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/checkout/sessions \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -d"line_items[0][price_data][currency]"=usd \
 -d"line_items[0][price_data][product_data][name]"="Restaurant delivery service" \
 -d"line_items[0][price_data][unit_amount]"=10000 \
 -d"line_items[0][quantity]"=1 \
 -d"payment_intent_data[transfer_group]"=ORDER100 \
 -dmode=payment \
 --data-urlencodesuccess_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}"

```

  * `line_items` : cet attribut spécifie les articles achetés par votre client. Ces articles sont affichés dans la page Checkout hébergée par Stripe.
  * `payment_intent_data[transfer_group]` : utilisez une chaîne unique comme `transfer_group` pour identifier les objets qui sont associés les uns aux autres. Lorsque Stripe crée automatiquement un paiement pour un PaymentIntent avec une valeur `transfer_group`, la même valeur est affectée au `transfer_group` du paiement.
  * `success_url` : Stripe redirige le client vers l’URL de réussite après un paiement réussi et remplace la chaîne `{CHECKOUT_SESSION_ID}` par l’ID de session Checkout. Vous pouvez l’utiliser pour récupérer la session Checkout et inspecter son état afin de choisir ce que vous voulez montrer au client. Vous pouvez également ajouter vos propres paramètres de requête, qui persistent tout au long du processus de redirection. Consultez la page Personnaliser le comportement de redirection avec une page hébergée par Stripe pour en savoir plus.


Client
Plateforme
Compte connecté
Compte connecté
Débit de 100 $
(70 $) Transfert
Paiement de 70 $
(20 $) Transfert
Paiement de 20 $
(3,20 $) Frais Stripe
Stripe
6,80 $ net
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
## Créer un transfert
Côté serveur
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Sur votre serveur, envoyez des fonds de votre compte vers un compte connecté en créant un transfert et en précisant le `transfer_group` utilisé.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/transfers \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -damount=7000 \
 -dcurrency=usd \
 -ddestination=
{{CONNECTED_ACCOUNT_ID}}
 \
 -dtransfer_group=ORDER100

```

Les montants des transferts et des paiements ne doivent pas nécessairement correspondre. Vous pouvez fractionner un paiement en plusieurs transferts ou inclure plusieurs paiements dans un même transfert. L’exemple suivant illustre la création d’un transfert supplémentaire associé au même `transfer_group`.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/transfers \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -damount=2000 \
 -dcurrency=usd \
 -ddestination={{OTHER_CONNECTED_ACCOUNT_ID}} \
 -dtransfer_group=ORDER100

```

### Options de transfert![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez attribuer n’importe quelle valeur à la chaîne `transfer_group`, mais elle doit représenter une seule action commerciale. Vous pouvez également effectuer un transfert sans paiement associé ou sans `transfer_group`, par exemple, lorsque vous devez payer un fournisseur, mais qu’il n’y a pas de paiement client associé.
#### Remarque
Le paramètre `transfer_group` identifie uniquement les objets associés. Il n’affecte aucune fonctionnalité standard. Pour empêcher l’exécution d’un transfert avant que les fonds du paiement associé ne soient disponibles, utilisez l’attribut `source_transaction` du transfert.
By default, a transfer request fails when the amount exceeds the platform’s available account balance. Stripe doesn’t automatically retry failed transfer requests.
You can avoid failed transfer requests for transfers that are associated with charges. When you specify the associated charge as the transfer’s source_transaction, the transfer request automatically succeeds. However, we don’t execute the transfer until the funds from that charge are available in the platform account.
#### Remarque
Si vous utilisez les paiements et transferts distincts, tenez compte de cela lorsque vous planifiez la fréquence de vos virements. Les virements automatiques peuvent interférer avec les transferts qui n’ont pas de `source_transaction` définie.
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
Command Line
cURL
```

curlhttps://api.stripe.com/v1/checkout/sessions \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -d"line_items[0][price_data][currency]"=usd \
 -d"line_items[0][price_data][product_data][name]"="Restaurant delivery service" \
 -d"line_items[0][price_data][unit_amount]"=10000 \
 -d"line_items[0][quantity]"=1 \
 -d"payment_intent_data[on_behalf_of]"=
{{CONNECTED_ACCOUNT_ID}}
 \
 -d"payment_intent_data[transfer_group]"=ORDER100 \
 -dmode=payment \
 --data-urlencodesuccess_url="https://example.com/success"

```

## Encaisser des commissions![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Lorsque vous créez des paiements et transferts distincts, la plateforme peut encaisser des frais en réduisant le montant transféré sur le compte de destination. Par exemple, imaginons une transaction de service de livraison, avec un paiement adressé au restaurant et un autre au livreur :
  1. Le client paie 100 USD.
  2. Stripe prélève des frais de 3,20 USD et ajoute les 96,80 USD restants au solde en attente du compte de la plateforme.
  3. La plateforme transfère 70 USD vers le compte connecté du restaurant et 20 USD vers le compte connecté du chauffeur.
  4. Des frais de plateforme de 6,80 USD restent sur le compte de la plateforme.


![Répartition des frais entre le compte de la plateforme et les transferts pour les comptes connectés](https://b.stripecdn.com/docs-statics-srv/assets/charges_transfers.c54b814c7e6f88993bf259c8a53f03e8.png)
Pour en savoir plus sur le traitement des paiements dans plusieurs devises avec Connect, veuillez consulter la page Gérer plusieurs devises.
## Disponibilité des transferts![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Le comportement par défaut consiste à transférer les fonds à partir du solde disponible du compte de la plateforme. Toute tentative de transfert dont le montant dépasse le solde disponible échoue et entraîne une erreur. Pour éviter ce problème, lorsque vous créez un transfert, associez-le à un paiement existant en spécifiant l’ID du paiement comme paramètre `source_transaction`. En utilisant le paramètre `source_transaction`, la demande de transfert aboutit, quel que soit votre solde disponible, tant que le paiement associé n’est pas encore réglé. Cependant, les fonds ne deviennent disponibles sur le compte de destination que lorsque les fonds du paiement associé peuvent être transférés depuis le compte de la plateforme.
#### Remarque
Si un transfert échoue en raison d’une insuffisance de fonds dans le solde de votre plateforme, l’ajout de fonds ne relance pas automatiquement l’action qui a échoué. Après avoir ajouté des fonds, vous devez à nouveau effectuer les transferts ou les virements ayant échoué.
Si le paiement source a une valeur `transfer_group`, Stripe affecte la même valeur au `transfer_group` du transfert. Si ce n’est pas le cas, Stripe génère une chaîne au format `group_` plus l’ID du PaymentIntent associé (par exemple : `group_pi_2NHDDD589O8KAxCG0179Du2s`), puis affecte cette chaîne en tant que `transfer_group` pour le paiement et le transfert.
#### Remarque
Vous devez spécifier la `source_transaction` lorsque vous créez un transfert. Vous ne pourrez pas mettre à jour cet attribut par la suite.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/transfers \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -damount=7000 \
 -dcurrency=usd \
 -dsource_transaction=
{{CHARGE_ID}}
 \
 -ddestination=
{{CONNECTED_ACCOUNT_ID}}

```

Vous pouvez obtenir l’ID du paiement à partir du PaymentIntent :
  * Obtenez l’attribut latest_charge du PaymentIntent. Cet attribut est l’ID du paiement le plus récent associé au PaymentIntent.
  * Créez une requête de liste des paiements, en spécifiant le `payment_intent` dans la requête. Cette méthode renvoie l’intégralité des données de tous les paiements associés au PaymentIntent.


Pour utiliser ce paramètre :
  * Le montant du transfert ne doit pas dépasser celui du paiement source
  * Vous pouvez créer plusieurs transferts avec la même `source_transaction`, tant que la somme des transferts ne dépasse pas le montant du paiement source
  * Le transfert prend l’état en attente du paiement associé : si les fonds du paiement deviennent disponibles dans X jours, le règlement que reçoit le compte de destination Stripe pour le transfert devient également disponible dans X jours
  * Stripe crée automatiquement le `transfer_group` pour vous
  * La devise de l’opération sur solde associée au paiement doit correspondre à celle du transfert


Les moyens de paiement asynchrones, comme ACH, peuvent échouer après toute demande de transfert ultérieure. Pour ces paiements, évitez d’utiliser `source_transaction`. Attendez plutôt qu’un événement charge.succeeded soit déclenché avant de transférer les fonds. Si vous devez utiliser `source_transaction` avec ces paiements, activez une fonctionnalité permettant de gérer les échecs de paiement.
Lorsqu’un paiement utilisé comme `source_transaction` échoue, des fonds provenant du solde de compte de votre plateforme sont transférés vers le compte connecté pour couvrir le paiement. Pour récupérer ces fonds, annulez le transfert associé à l’échec de la `source_transaction`.
## Émission de remboursements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Les paiements créés sur votre plateforme peuvent être remboursés à l’aide de la clé secrète de votre plateforme. Cependant, le remboursement d’un paiement n’a aucun impact sur les transferts associés. Il incombe à votre plateforme de rapprocher tout montant qui lui est dû en réduisant le montant des transferts ultérieurs ou en annulant les transferts.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/refunds \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -dcharge=
{{CHARGE_ID}}

```

## Annuler les transferts![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Connect prend en charge la possibilité d’annuler les transferts effectués sur les comptes connectés, totalement ou en partie (en définissant la valeur `amount`). N’utilisez les annulations de transfert que pour les remboursements ou les litiges liés au paiement, ou pour corriger des erreurs de transfert.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/transfers/
{{TRANSFER_ID}}
/reversals \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -damount=7000

```

Les annulations de transferts rajoutent le montant spécifié (ou l’intégralité du montant) au solde disponible de la plateforme, réduisant ainsi le solde disponible du compte connecté. Il n’est possible d’annuler un transfert que si le solde disponible du compte connecté est supérieur au montant de l’annulation ou si les réserves connectées sont activées.
Si l’annulation du transfert nécessite une conversion de devise et que le montant de l’annulation entraîne un solde nul après la conversion, une erreur est renvoyée.
La désactivation des remboursements pour un compte connecté n’empêchera pas le traitement des annulations de transfert.
## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Gérer plusieurs devises
  * Libellés de relevé bancaire avec Connect
  * Comprendre les soldes de compte Connect


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
Créer un transfert
Options de transfert
Tester l'intégration
Sélectionner l’entité de règlement
Encaisser des commissions
Disponibilité des transferts
Émission de remboursements
Annuler les transferts
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

