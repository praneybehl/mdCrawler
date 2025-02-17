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
Aperçu
Démarrer avec Connect
Principes de base de l'intégration
Exemples d'intégration
Inscrire des comptes
Configurer les dashboards des comptes
Accepter des paiements
Créer un paiement
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
AccueilPlateformes et places de marchéAccept payments
# Créer des abonnements avec Stripe Billing
## Grâce à Connect, vous pouvez créer des abonnements pour vos clients ou des comptes connectés.
Les SaaS (Software as a Service) et les places de marché ont recours à Stripe Connect pour acheminer les paiements entre leur plateforme, les clients et les comptes connectés. Vous pouvez utiliser Connect pour acheminer des paiements ou des virements et Stripe Billing pour prendre en charge votre modèle de revenus récurrents.
## Cas d’usage![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez créer des abonnements pour des comptes Connect, avec plusieurs approches d’encaissement des paiements prises en charge. Vous pouvez créer des abonnements pour les clients de vos comptes connectés en utilisant des paiements directs ou indirects, pour que vos clients finaux puissent traiter des transactions directement avec votre plateforme et débiter vos comptes connectés de frais d’utilisation de votre plateforme.
Client
Plateforme
Compte connecté
Les cas d’usage suivants expliquent comment utiliser Stripe Billing pour créer des abonnements depuis les clients finaux aux comptes connectés, pour facturer les clients finaux de la plateforme et les comptes connectés.
Cas d’usage| Description  
---|---  
Abonner le client final au compte connecté| Créez des abonnements à vos comptes connectés pour les clients finaux, ce qui permet de collecter les paiements de plusieurs façons. Dans cet exemple, les tarifs se trouvent sur le compte connecté.  
Créer des abonnements pour facturer les clients finaux de la plateforme| Les places de marché peuvent proposer des abonnements sans faire intervenir votre compte connecté. Dans cet exemple, les tarifs se trouvent sur la plateforme.  
Créer des abonnements pour facturer des comptes connectés| Les plateformes peuvent créer des abonnements pour leurs comptes connectés. Dans cet exemple, les tarifs se trouvent sur la plateforme.  
### Restrictions![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Les restrictions suivantes s’appliquent à l’utilisation de Connect pour les abonnements :
  * Votre plateforme ne peut pas modifier ni annuler un abonnement qu’elle n’a pas créé.
  * Votre plateforme ne peut pas ajouter un `application_fee_amount` à une facture qu’elle n’a pas créée, ou à une facture contenant des postes qu’elle n’a pas créés.
  * Les abonnements ne sont pas automatiquement annulés lorsque vous vous déconnectez de la plateforme. Vous devez annuler l’abonnement après votre déconnexion. Vous pouvez utiliser des webhooks pour surveiller l’activité du compte connecté.


## Créer des abonnements pour le client final d’un compte connecté![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Si vous développez une plateforme, vous pouvez créer des abonnements pour les clients de vos comptes connectés. Vous pouvez éventuellement prélever une commission de plateforme à chaque paiement.
Client
Plateforme
Compte connecté
Dans cet exemple, une plateforme de publication en ligne permet aux clients de s’abonner à leurs auteurs préférés et de leur verser un abonnement mensuel afin de recevoir des articles de blog premium.
## Avant de commencer![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Avant de pouvoir créer des abonnements pour vos clients ou vos comptes connectés, vous devez :
  1. Créer un compte connecté pour chaque personne qui reçoit de l’argent sur votre plateforme. Dans notre exemple de publication en ligne, un compte connecté représente un auteur.
  2. Créer un modèle tarifaire. Pour cet exemple, nous créons un modèle tarifaire à taux fixe pour débiter des frais aux clients de manière récurrente, mais les tarifs par utilisateur et à l’usage sont également pris en charge.
  3. Créez un objet Customer avec le moyen de paiement souhaité pour chaque personne qui s’abonne à un compte connecté. Dans notre exemple de publication en ligne, vous créez un objet Customer pour chaque lecteur qui s’abonne à un auteur.


### Choisir entre les paiements directs et indirects![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez utiliser des paiements directs ou indirects pour fractionner le paiement d’un client entre le compte connecté et votre plateforme.
Si les paiements sont directs, les clients ne sont pas conscients de l’existence de votre plateforme car c’est le nom de l’auteur, et non celui de votre plateforme, qui apparaît sur le libellé de relevé bancaire. Dans notre exemple de publication en ligne, les lecteurs interagissent directement avec les auteurs.
Les paiements directs sont recommandés pour les comptes connectés ayant accès à l’intégralité du Dashboard Stripe, ce qui inclut les comptes Standard.
Si vous souhaitez que votre plateforme soit responsable des frais Stripe, remboursements et contestations de paiement, utilisez les paiements directs. Dans notre exemple de publication en ligne, les clients s’inscrivent à votre plateforme de publication, et non directement à des auteurs spécifiques.
Les paiements indirects sont recommandés pour les comptes connectés avec accès au Dashboard Express ou les comptes connectés sans accès à un tableau de bord hébergé par Stripe, ce qui inclut les comptes Express et Custom.
Pour en savoir plus sur les différents types de paiements Connect, veuillez consulter la section concernant les types de paiements.
### Utiliser les paiements directs pour créer un abonnement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Pour créer un abonnement avec des paiements associés au compte connecté, créez un abonnement en tant que compte connecté. Assurez-vous de définir le client avec un moyen de paiement par défaut, et le tarif du compte connecté. Pour utiliser un client sans moyen de paiement par défaut, définissez `payment_behavior: "default_incomplete"`. En savoir plus sur le comportement de paiement.
Développez `latest_invoice.payment_intent` pour inclure l’Element Payment, qui est nécessaire pour confirmer le paiement. Pour en savoir plus, veuillez consulter Element Payment.
Pour voir un exemple illustrant l’implémentation d’un flux d’inscription pour les abonnements et d’un tunnel de paiement dans votre application, veuillez consulter le guide sur l’intégration des abonnements.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/subscriptions \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -H"Stripe-Account: 
{{CONNECTED_ACCOUNT_ID}}
" \
 -dcustomer=
{{CUSTOMER_ID}}
 \
 -d"items[0][price]"=
{{PRICE_ID}}
 \
 -d"expand[0]"="latest_invoice.payment_intent"

```

### Utiliser les paiements indirects pour créer un abonnement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Pour créer un abonnement avec des paiements associés à la plateforme, ainsi que des transferts automatiques vers un compte connecté, effectuez un appel de création d’abonnement en fournissant l’identifiant du compte connecté comme valeur pour le paramètre `transfer_data[destination]`.
Développez `latest_invoice.payment_intent` pour inclure l’Element Payment, dont vous avez besoin pour confirmer le paiement. Pour en savoir plus, veuillez consulter la section concernant Element Payment.
Vous avez la possibilité de spécifier un paramètre application_fee_percent. Pour en savoir plus, veuillez consulter la section concernant la perception de frais.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/subscriptions \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -dcustomer=
{{CUSTOMER_ID}}
 \
 -d"items[0][price]"=
{{PRICE_ID}}
 \
 -d"expand[0]"="latest_invoice.payment_intent" \
 -d"transfer_data[destination]"=
{{CONNECTED_ACCOUNT_ID}}

```

### Mesures supplémentaires à prendre avant de créer un abonnement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Pour créer un paiement indirect, il vous faut définir à la fois le client et le tarif sur le compte de la plateforme. Vous devez avoir créé un compte connecté sur la plateforme. Le client doit exister au sein du compte de la plateforme. Les paiements indirects sont réalisés au nom de la plateforme.
## Créer des abonnements pour facturer les clients finaux de la plateforme![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez utiliser Stripe Billing pour créer des abonnements afin que vos clients finaux puissent effectuer des transactions directement avec votre plateforme sans impliquer vos comptes connectés.
Client
Plateforme
Compte connecté
Dans cet exemple, une place de marché est créée pour permettre aux clients de se faire livrer à la demande par des restaurants. Cette place de marché propose aux clients un abonnement mensuel premium qui les dispense des frais de livraison. Les clients qui s’abonnent à l’offre premium paient directement la place de marché et ne s’abonnent pas à un service de livraison ou à un restaurant particulier.
## Avant de commencer![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Avant de créer des abonnements pour vos clients, vous devez :
  1. Créer un modèle tarifaire. Pour cet exemple, nous créons un modèle tarifaire à taux fixe pour débiter des frais aux clients de manière récurrente, mais les tarifs par utilisateur et à l’usage sont également pris en charge.
  2. Créer un client pour chaque personne que vous souhaitez facturer.


Vous pouvez également créer un compte connecté pour chaque utilisateur qui reçoit de l’argent provenant de votre place de marché. Dans notre exemple de livraison de repas à la demande, un compte connecté représente un restaurant ou un service de livraison. Cependant, cette étape n’est pas nécessaire pour l’inscription de nouveaux clients à votre place de marché.
### Créer un abonnement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Pour créer un abonnement et définir votre plateforme comme destinataire des fonds (sans qu’ils transitent par les comptes connectés), suivez les instructions du guide des abonnements pour créer un abonnement avec Stripe Billing.
### Créer des paiements et transferts distincts![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Si vous souhaitez transférer manuellement une partie des fonds reçus par votre plateforme vers vos comptes connectés, utilisez Paiements et transferts distincts. Dans notre exemple de service de livraison de restauration à la demande, vous pouvez utiliser des frais et des transferts distincts pour verser une commission d’affiliation à un livreur ou à un restaurant ayant recommandé à un client de s’abonner au service de livraison premium.
## Créer des abonnements pour facturer des comptes connectés![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez utiliser Stripe Billing pour créer des abonnements afin de prélever une commission sur vos comptes connectés pour l’utilisation de votre plateforme.
Client
Plateforme
Compte connecté
Cet exemple présente une plateforme logicielle de gestion de salles de sport. En contrepartie d’une commission mensuelle, ces entreprises peuvent utiliser le logiciel pour gérer la planification et les horaires de cours. Les frais d’inscription incombent aux salles de sport, et non à leurs clients.
Le logiciel de gestion de salles de sport simplifie les paiements ponctuels entre les usagers et les entreprises pour chaque cours auquel un usager s’inscrit. Cet abonnement mensuel lie le compte connecté et la plateforme, l’usager de la salle de sport n’est donc pas impliqué dans cette transaction.
Dans le diagramme ci-dessus, la salle de sport représente le compte connecté et l’usager est le client final.
## Avant de commencer![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Avant de créer des abonnements pour vos clients ou vos comptes connectés, vous devez :
  1. Créer un compte connecté pour chaque utilisateur qui reçoit de l’argent sur votre plateforme. Dans cet exemple, le compte connecté représente la salle de sport.
  2. Créer un modèle tarifaire. Pour cet exemple, nous créons un modèle tarifaire à taux fixe pour débiter des frais aux clients de manière récurrente, mais les tarifs par utilisateur et à l’usage sont également pris en charge.
  3. Créer un client sur la plateforme avec le moyen de paiement prévu pour chaque compte connecté que vous souhaitez facturer. Dans l’exemple du logiciel de gestion de salles de sport, vous devez créer un client pour chaque salle de sport :


### Créer un objet Customer pour représenter le compte connecté![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Si vos comptes connectés utilisent Stripe pour traiter les paiements de leurs clients, ils ont peut-être déjà créé un objet Customer pour chaque client final.
Pour créer un abonnement permettant au compte connecté de payer des frais récurrents sur la plateforme, vous devez d’abord créer un objet Customer distinct représentant ce compte connecté.
Dans l’exemple de la salle de sport, cette entreprise utilise Stripe pour traiter les paiements ponctuels de ses clients. Ils ont déjà créé un objet Customer pour chaque usager de la salle, mais vous devez en créer un autre pour représenter la salle de sport elle-même. Ne créez qu’un seul Customer pour représenter chaque société. À l’inverse, ne créez pas de Customer pour chaque propriétaire, gestionnaire ou opérateur de la société.
### Créer un abonnement pour le compte connecté![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Pour créer un abonnement à l’endroit où votre plateforme reçoit les fonds de vos comptes connectés, suivez les instructions du guide des abonnements pour créer un abonnement avec Stripe Billing. L’objet Customer impliqué dans la transaction représente le compte connecté (et non le client final). Dans notre exemple de salle de sport, le `CUSTOMER_ID` représente l’entreprise, pas l’usager.
## Activer votre intégration pour recevoir des notifications d’événement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe creates event notifications when changes happen in your account, like when a recurring payment succeeds or when a payout fails. To receive these notifications and use them to automate your integration, set up a webhook endpoint. For example, you could provision access to your service when you receive the `invoice.paid` event.
### Event notifications for Connect and subscriptions integrations![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Here are the event notifications that Connect integrations typically use.
Événement| Type de data.object| Description  
---|---|---  
`account.application.deauthorized`| `application`| Se produit lorsqu’un compte connecté se déconnecte de votre plateforme. Vous pouvez l’utiliser pour déclencher un nettoyage sur votre serveur. Disponible pour les comptes connectés ayant accès au Dashboard Stripe, ce qui inclut les comptes Standard.  
`account.external_account.updated`| Un compte externe, tel que `card` ou `bank_account`| Se produit lorsqu’un compte bancaire ou une carte de débit associé(e) à un compte connecté est modifié(e), ce qui peut avoir des conséquences sur les virements. Disponible pour les comptes connectés contrôlés par votre plateforme, comptes Custom et Express compris, et pour les comptes Standard pour lesquels les contrôles de la plateforme sont activés.  
`account.updated`| `account`| Permet de surveiller les évolutions des exigences et les changements d’état qui affectent les comptes connectés. Disponible pour tous les comptes connectés.  
`balance.available`| `balance`| Se produit lorsque votre solde Stripe est mis à jour (par exemple, lorsque des fonds provenant de votre compte bancaire sont disponibles pour être transférés vers votre compte connecté).  
`payment_intent.succeeded`| `payment_intent`| Se produit lorsqu’un Payment Intent aboutit à un paiement réussi. Disponible pour tous les paiements, y compris les paiements directs et indirects.  
`payout.failed`| `payout`| Occurs when a payout fails. When a payout fails, the external account involved is disabled, and no automatic or manual payouts can be processed until the external account is updated.  
`person.updated`| `person`| Si vous utilisez l’API Persons, vous pouvez suivre les évolutions des exigences et les changements d’état des personnes. Disponible pour les comptes connectés contrôlés par votre plateforme, comptes Custom et Express compris, et pour les comptes Standard dont les contrôles de la plateforme sont activés.  
Here are the event notifications that subscriptions integrations typically use.
Événement| Description  
---|---  
`customer.created`| Envoyé lorsqu’un objet Customer a bien été créé.  
`customer.subscription.created`| Envoyé lors de la création de l’abonnement. Le `status` de l’abonnement peut être `incomplete` si l’authentification du client est demandée pour mener à bien le paiement ou si vous définissez `payment_behavior` sur `default_incomplete`. Familiarisez-vous avec le comportement de paiement des abonnements pour en savoir plus.  
`customer.subscription.deleted`| Envoyé lorsque l’abonnement d’un client prend fin.  
`customer.subscription.paused`| Envoyé lorsque le `status` d’un abonnement passe à `paused`. Par exemple, l’événement est envoyé lorsqu’un abonnement est configuré pour être suspendu lorsqu’un essai gratuit prend fin sans moyen de paiement. La facturation n’aura pas lieu tant que l’abonnement n’aura pas repris. Nous n’envoyons pas cet événement si l’encaissement des paiements est suspendu, car des factures continuent d’être créées pendant cette période.  
`customer.subscription.resumed`| Envoyé lors de la reprise d’un abonnement qui était à l’état `paused`. Cela ne s’applique pas lorsque l’encaissement des paiements est réactivé.  
`customer.subscription.trial_will_end`| Envoyé trois jours avant la fin de la période d’essai. Si la période d’essai est inférieure à trois jours, l’événement est déclenché.  
`customer.subscription.updated`| Envoyé lorsqu’un abonnement démarre ou est modifié. Par exemple, le renouvellement d’un abonnement, l’ajout d’un bon de réduction, l’application d’une réduction, l’ajout d’un poste de facture et le changement de plan déclenchent sont des situations qui déclenchent cet événement.  
`entitlements.active_entitlement_summary.updated`| Envoyé lorsque les droits actifs d’un client sont mis à jour. Lorsque vous recevez cet événement, vous pouvez donner ou retirer l’accès aux fonctionnalités de votre produit. En savoir plus sur l’intégration des droits.  
`invoice.created`| Envoyé lorsqu’une facture est créée pour un nouvel abonnement ou un renouvellement. Si Stripe ne reçoit pas une réponse positive à `invoice.created`, la finalisation de toutes les factures avec l’encaissement automatique est retardée de 72 heures au maximum. Renseignez-vous sur la finalisation des factures.
  * Répondez à la notification en envoyant une requête à l’API de finalisation des factures.

  
`invoice.finalized`| Envoyé lorsqu’une facture est finalisée et prête à être payée.
  * Vous pouvez envoyer la facture au client. Familiarisez-vous avec la finalisation des factures pour en savoir plus.
  * Selon vos paramètres, nous débitons automatiquement le moyen de paiement par défaut ou tentons un encaissement. Renseignez-vous sur les e-mails après la finalisation pour en savoir plus.

  
`invoice.finalization_failed`| La facture n’a pas pu être finalisée. Reportez-vous à la page consacrée à la gestion des échecs de finalisation des factures. Davantage d’informations à propos de la finalisation des factures sont disponibles dans le guide de présentation générale des factures.
  * Inspectez e champ `last_finalization_error` de l’objet Invoice pour déterminer la cause de l’erreur.
  * Si vous utilisez Stripe Tax, vérifiez le champ automatic_tax de l’objet Invoice.
  * Si `automatic_tax[status]=requires_location_inputs`, la facture ne peut pas être finalisée et les paiements ne sont pas perçus. Prévenez votre client et collectez la localisation du client demandée.
  * Si `automatic_tax[status]=failed`, relancez la requête plus tard.

  
`invoice.paid`| Envoyé lorsque la facture est réglée. Vous pouvez fournir l’accès à votre produit dès la réception de cet événement et le basculement du `status` de l’abonnement sur `active`.  
`invoice.payment_action_required`| Envoyé lorsque la facture nécessite une authentification du client. Découvrez comment gérer un abonnement quand une action est requise pour la facture.  
`invoice.payment_failed`| Le paiement d’une facture a échoué. L’état du PaymentIntent bascule sur `requires_action`. L’état de l’abonnement reste `incomplete` _seulement_ pour la première facture de l’abonnement. Lorsqu’un paiement échoue, plusieurs actions sont possibles :
  * Prévenez votre client. Apprenez à configurer les paramètres d’abonnement pour activer les relances intelligentes Smart Retries et d’autres fonctionnalités d’encaissement.
  * Si vous utilisez des PaymentIntents, recueillez de nouvelles données de paiement et confirmez le PaymentIntent.
  * Mettez à jour le moyen de paiement par défaut de l’abonnement.

  
`invoice.upcoming`| Envoyé quelques jours avant le renouvellement de l’abonnement. Le nombre de jours dépend de la valeur **Événements de renouvellement à venir** configurée dans le Dashboard. Pour les abonnements existants, la modification du nombre de jours prend effet à la période de facturation suivante. Vous pouvez toujours ajouter des postes de facture supplémentaires si nécessaire.  
`invoice.updated`| Envoyé lorsqu’un paiement aboutit ou échoue. Si le paiement aboutit, l’attribut `paid` est défini sur `true` et le `status` sur `paid`. Si le paiement échoue, `paid` est défini sur `false` et le `status` reste `open`. Les échecs de paiement déclenchent par ailleurs un événement `invoice.payment_failed`.  
`payment_intent.created`| Envoyé lorsqu’un PaymentIntent est créé.  
`payment_intent.succeeded`| Envoyé lorsqu’un PaymentIntent a effectué un paiement avec succès.  
`subscription_schedule.aborted`| Envoyé lorsqu’une planification d’abonnement est annulée car un défaut de paiement a entraîné la résiliation de l’abonnement correspondant.  
`subscription_schedule.canceled`| Envoyé lorsqu’une planification d’abonnement est annulée, ce qui annule également tout abonnement actif associé.  
`subscription_schedule.completed`| Envoyé lorsque toutes les phases d’une planification d’abonnement sont terminées.  
`subscription_schedule.created`| Envoyé lorsqu’une nouvelle planification d’abonnement est créée.  
`subscription_schedule.expiring`| Envoyé 7 jours avant la date d’expiration d’un abonnement.  
`subscription_schedule.released`| Envoyé lorsqu’une planification d’abonnement est publiée, ou interrompue et dissociée de l’abonnement, lequel est conservé.  
`subscription_schedule.updated`| Envoyé lorsqu’une planification d’abonnement est mise à jour.  
  * Créer un endpoint de webhook
  * Écouter des événements avec la CLI Stripe
  * Connecter des webhooks
  * Webhooks d’abonnement


## Tester votre intégration![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Une fois que vous avez créé votre abonnement, testez soigneusement votre intégration avant de la proposer aux clients ou de l’utiliser en mode production. Pour en savoir plus, veuillez consulter la page test pour Stripe Billing.
## Options supplémentaires![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Après avoir créé votre abonnement, vous pouvez entre autres indiquer un application_fee_percent, configurer le portail client, facturer votre client à l’aide du paramètre `on_behalf_of` et surveiller les abonnements avec des webhooks, en plus d’autres options.
### Encaisser des frais sur les abonnements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
### Utiliser des bons de réduction![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
### Utiliser des périodes d'essai![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
### Configurer le portail client![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
### Surveiller les abonnements avec des webhooks![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
### Configurer le compte connecté en tant qu'entité de règlement à l'aide du paramètre on_behalf_of![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
### Comprendre le comportement de déconnexion![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
### Intégrer le calcul et la collecte des taxes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Créer des factures
  * Créer un paiement
  * Partager les clients entre comptes
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
Cas d’usage
Restrictions
Créer des abonnements pour le client final d’un compte connecté
Avant de commencer
Choisir entre les paiements directs et indirects
Utiliser les paiements directs pour créer un abonnement
Utiliser les paiements indirects pour créer un abonnement
Mesures supplémentaires à prendre avant de créer un abonnement
Créer des abonnements pour facturer les clients finaux de la plateforme
Avant de commencer
Créer un abonnement
Créer des paiements et transferts distincts
Créer des abonnements pour facturer des comptes connectés
Avant de commencer
Créer un objet Customer pour représenter le compte connecté
Créer un abonnement pour le compte connecté
Activer votre intégration pour recevoir des notifications d’événement
Event notifications for Connect and subscriptions integrations
Tester votre intégration
Options supplémentaires
Voir aussi
Produits utilisés
Connect
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

