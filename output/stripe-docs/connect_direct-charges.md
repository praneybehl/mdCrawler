Accéder directement au contenu
Paiements directs
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
Configurations des frais pour les comptes connectés
Rapports pour les frais de paiement direct
Partager les moyens de paiement entre plusieurs comptes
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
# Créer des paiements directs
## Créez des paiements directement sur le compte connecté et prélevez des frais.
Créez des _paiements directs_ lorsque des clients effectuent des transactions directement avec un compte connecté, souvent sans connaître l’existence de votre plateforme. Grâce aux paiements directs :
  * Le paiement apparaît comme un débit sur le compte connecté, et non sur le compte de votre plateforme.
  * Le solde du compte connecté augmente à chaque prélèvement.
  * Le solde de votre compte augmente avec les commissions de la plateforme sur chaque paiement.


Ce type de paiement est le mieux adapté aux plateformes SaaS. Par exemple, Shopify fournit des outils pour créer des vitrines en ligne et Thinkific permet aux enseignants de proposer des cours en ligne.
#### Remarque
Nous vous recommandons d’utiliser les paiements directs pour les comptes connectés qui ont accès à l’intégralité du Dashboard Stripe.
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
Une session Checkout contrôle ce que le client voit dans le formulaire de paiement, tel que les postes, le montant de la commande et la devise. Ajoutez à votre site Web un bouton de paiement qui appelle un endpoint côté serveur pour créer une session Checkout.
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
 -H"Stripe-Account: 
{{CONNECTED_ACCOUNT_ID}}
" \
 -d"line_items[0][price_data][currency]"=usd \
 -d"line_items[0][price_data][product_data][name]"=T-shirt \
 -d"line_items[0][price_data][unit_amount]"=1000 \
 -d"line_items[0][quantity]"=1 \
 -d"payment_intent_data[application_fee_amount]"=123 \
 -dmode=payment \
 --data-urlencodesuccess_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}"

```

  * `line_items` : Cet attribut représente les articles que votre client est en train d’acheter et apparaît sur la page de paiement hébergée par Stripe.
  * `payment_intent_data[application_fee_amount]` : cet attribut indique le montant que votre plateforme prélève de la transaction en tant que frais de plateforme. Une fois le paiement traité sur le compte connecté, le montant `application_fee_amount` est transféré à la plateforme. Pour plus d’informations, consultez la section encaisser des frais.
  * `success_url` : Stripe redirige le client vers l’URL de réussite après un paiement réussi et remplace la chaîne `{CHECKOUT_SESSION_ID}` par l’ID de session Checkout. Vous pouvez l’utiliser pour récupérer la session Checkout et inspecter son état afin de choisir ce que vous voulez montrer au client. Vous pouvez également ajouter vos propres paramètres de requête, qui persistent tout au long du processus de redirection. Consultez la page Personnaliser le comportement de redirection avec une page hébergée par Stripe pour en savoir plus.
  * `Stripe-Account` : Cet en-tête indique un paiement direct pour votre compte connecté. Checkout reflète l’image de marque du compte connecté, ce qui donne l’impression aux clients d’être directement en contact avec le compte connecté et non avec votre plateforme.


Les paiements que vous créez directement sur le compte connecté sont indiqués uniquement sur ce compte. Ces paiements n’apparaissent pas dans le Dashboard ou dans les exportations de votre plateforme. Pour les comptes connectés que votre plateforme contrôle, les paiements directs sont inclus dans les rapports et dans Sigma. Vous pouvez toujours récupérer ces informations en utilisant l’API Stripe.
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
## Encaisser des commissions![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Votre plateforme peut accepter une commission de plateforme avec les limites suivantes :
  * La valeur de `application_fee_amount` doit être positive et inférieure au montant du paiement. La commission de la plateforme prélevée est plafonnée au montant du paiement.
  * Aucune commission Stripe supplémentaire n’est appliquée à la commission de la plateforme.
  * Conformément aux lois et réglementations du Brésil, les plateformes situées en dehors du Brésil comportant des comptes connectés brésiliens ne pourront pas prélever de commission de plateforme par le biais de Stripe.
  * La devise de `application_fee_amount` dépend de quelques facteurs de plusieurs devises.


L’opération sur solde du paiement inclut une répartition détaillée des commissions de la plateforme et des frais Stripe. Pour faciliter la génération des rapports, un objet Application Fee est créé après le prélèvement des commissions de la plateforme. Utilisez la propriété `amount` sur l’objet Application Fee pour créer des rapports. Vous pouvez ensuite accéder à ces objets à partir de l’endpoint Application Fees.
Les commissions de la plateforme reçues sont ajoutées au solde disponible de votre compte à la même fréquence que les fonds issus des paiements Stripe réguliers. Les commissions de la plateforme peuvent être affichées dans la section Frais perçus du Dashboard.
#### Mise en garde
Par défaut, les commissions de plateforme pour les paiements directs sont créées de façon asynchrone. Si vous développez l’objet `application_fee` lors d’une demande de création de paiement, la commission de plateforme est créée de façon synchrone dans le cadre de cette demande. Ne développez l’objet `application_fee` que si vous devez absolument le faire, car cela augmente la latence de la demande.
Pour accéder aux objets des commissions de la plateforme pour les commissions créées de façon asynchrone, visualisez l’événement webhook application_fee.created.
### Mouvement de fonds avec frais![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Lorsque vous indiquez une commission de plateforme pour un paiement, le montant de la commission est transféré vers le compte Stripe de votre plateforme. Lorsque vous traitez un paiement directement depuis le compte connecté, le montant du paiement, moins les frais Stripe et la commission de la plateforme, est versé sur le compte connecté.
Par exemple, si vous effectuez un paiement de 10 USD avec une commission de la plateforme de 1,23 USD (comme dans l’exemple précédent), le montant de cette commission est transféré sur le compte de votre plateforme. Le compte connecté reçoit directement la somme de 8,18 USD (10 USD - 1,23 USD - 0,59 USD, en cas de facturation de frais Stripe standard pour les États-Unis). 
![Mouvements de fonds pour un paiement avec commission de plateforme](https://b.stripecdn.com/docs-statics-srv/assets/direct_charges_flow.ac943c1635c3c66d1ee5e0020c453744.png)
Si vous traitez des paiements dans plusieurs devises, consultez la rubrique sur la manière dont les devises sont traitées dans Connect.
## Personnaliser l’image de marque![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Votre plateforme et vos comptes connectés peuvent utiliser les paramètres de marque dans le Dashboard pour personnaliser l’image de marque sur la page des paiements. Pour les paiements directs, Chekckout utilise les paramètres de marque du compte connecté.
Vous pouvez également utiliser l’API pour mettre à jour les paramètres de marque :
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

## Effectuer des remboursements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
De la même façon que les plateformes peuvent créer des paiements sur les comptes connectés, elles peuvent également créer des remboursements. Créez un remboursement à l’aide de la clé secrète de votre plateforme en étant identifié avec un compte connecté.
Les commissions de la plateforme ne sont pas automatiquement remboursées lors d’un remboursement. Votre plateforme doit explicitement rembourser la commission de la plateforme, car dans le cas contraire, le compte connecté (le compte sur lequel le paiement a été créé) perd ce montant. Vous pouvez rembourser les commissions de la plateforme en indiquant la valeur **true** pour `refund_application_fee` dans la demande de remboursement :
Command Line
cURL
```

curlhttps://api.stripe.com/v1/refunds \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -H"Stripe-Account: 
{{CONNECTED_ACCOUNT_ID}}
" \
 -dcharge=
{{CHARGE_ID}}
 \
 -drefund_application_fee=true

```

Par défaut, la totalité du paiement est remboursée, mais vous pouvez créer un remboursement partiel en définissant le paramètre `amount` sur un nombre entier positif. Si le remboursement entraîne le remboursement de la totalité du paiement, la totalité de la commission de plateforme est remboursée. Dans le cas contraire, un montant proportionnel de la commission de la plateforme est remboursé. Vous pouvez également indiquer la valeur **false** pour `refund_application_fee` et rembourser la commission de la plateforme séparément.
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
Encaisser des commissions
Mouvement de fonds avec frais
Personnaliser l’image de marque
Effectuer des remboursements
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

