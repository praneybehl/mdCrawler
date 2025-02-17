Accéder directement au contenu
Inscription via l'API
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
# Inscription des utilisateurs via l'API
## Créez votre propre flux d'inscription des utilisateurs à l'aide des API de Stripe.
Avec l’API Onboarding, vous utilisez l’API Accounts pour créer un flux d’inscription, une fonctionnalité de reporting et des canaux de communication pour vos utilisateurs. Stripe peut être totalement invisible pour le titulaire du compte. Cependant, votre plateforme est responsable de toutes les interactions avec vos comptes et de la collecte de toutes les informations nécessaires à leur vérification.
#### Responsabilités supplémentaires
Avec l’inscription via l’API, votre flux personnalisé doit répondre à toutes les exigences légales et réglementaires en vigueur dans les régions où vous exercez vos activités. Vous devez également consacrer des ressources au suivi des modifications apportées à ces exigences et recueillir des informations mises à jour de manière continue, au moins une fois tous les six mois. Si vous souhaitez mettre en place un flux d’inscription personnalisé, Stripe vous conseille vivement d’utiliser l’inscription intégrée.
Inscrire un nouvel utilisateur
Réinscrire un utilisateur existant
Récupérer le compte connecté
Afficher l’interface utilisateur pour collecter les `requirements` de votre utilisateur
Créer un compte connecté
Si `requirements.currently_due` n’est pas vide
Présenter des formulaires pour collecter les informations et valider des champs
Mettre à jour le compte connecté avec les informations collectées
## Définir des exigences![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Les facteurs suivants affectent les exigences d’inscription pour vos comptes connectés :
  * Pays d’origine des comptes connectés
  * Le type de contrat de service applicable aux comptes connectés
  * Fonctionnalités demandées pour les comptes connectés
  * Type (par exemple particulier ou entreprise) et structure de l’entreprise (par exemple, société anonyme ou société de personnes)


Utilisez le formulaire interactif pour voir comment la modification de ces facteurs affecte les exigences.
### Formulaire d'exigences![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
## Créer des formulaires pour collecter des informations
Côté client
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Il est recommandé d’organiser les paramètres requis en groupes logiques ou en formulaires dans votre flux d’inscription. Vous pouvez coder un mappage entre les paramètres Stripe et les regroupements logiques. Les regroupements logiques suggérés pour les paramètres sont indiqués dans la première colonne de l’exemple de tableau des exigences.
Après avoir encodé les paramètres requis au sein de votre application, générez des interfaces utilisateur pour les paramètres correspondant à ces exigences. Pour chaque paramètre, créez un formulaire d’interface utilisateur qui comprend :
  * Libellé de paramètre, localisé dans chaque pays et langue pris en charge
  * Description des paramètres, localisée dans chaque pays et langue pris en charge
  * Champs de saisie des paramètres avec logique de validation des données et chargement de documents au besoin


Il est important de structurer votre logique d’application pour prendre en compte la possibilité d’ajouter des paramètres ultérieurement. Par exemple, Stripe peut introduire de nouveaux paramètres, de nouvelles vérifications ou de nouveaux seuils que vous devez intégrer dans vos flux d’inscription au fil du temps.
Si vous modifiez l’un des facteurs qui déterminent les exigences relatives à vos comptes connectés, vous devez également adapter vos formulaires de collecte. Le pays et le type de contrat de service sont immuables, tandis que les fonctionnalités et le type d’activité sont modifiables.
  * Pour modifier un champ immuable tel que le pays ou le type de contrat de service, créez un nouveau compte connecté avec les nouvelles valeurs. Cela génère de nouvelles exigences que vous devez intégrer à vos flux de collecte.
  * Pour modifier un champ modifiable, comme les fonctions ou le type d’entité, mettez à jour le compte connecté. Cela génère de nouvelles exigences que vous devez intégrer à vos flux de collecte.


### Inclure le consentement aux Conditions d’utilisation du service Stripe![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Avant leur activation, vos comptes connectés doivent accepter les Conditions d’utilisation du service de Stripe. Vous pouvez inclure les Conditions d’utilisation du service de Stripe aux vôtres.
## Créer un compte connecté
Côté serveur
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Créez un compte connecté dans lequel votre plateforme est responsable des soldes négatifs. Stripe perçoit des frais sur le compte de votre plateforme et vos comptes connectés n’ont pas accès à un Dashboard hébergé par Stripe. Demandez toutes les fonctionnalités dont vos comptes connectés ont besoin. Incluez le type d’entreprise et toute autre information correspondant à vos besoins si vous pouvez pré-remplir les champs correspondants.
Vous pouvez également créer un compte connecté dont le `type` est défini sur `custom`, avec les fonctionnalités de votre souhait.
Si vous ne spécifiez pas le pays ni le contrat de type de service, les valeurs par défaut suivantes leur sont attribuées :
  * Le `country` par défaut est le même pays que celui de votre plateforme.
  * Le contrat de type de service (`tos_acceptance.service_agreement`) est défini sur `full` par défaut.


Avec les propriétés du contrôleur
Avec un type de compte
Command Line
cURL
```

curlhttps://api.stripe.com/v1/accounts \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -d"controller[losses][payments]"=application \
 -d"controller[fees][payer]"=application \
 -d"controller[stripe_dashboard][type]"=none \
 -d"controller[requirement_collection]"=application \
 -d"capabilities[card_payments][requested]"=true \
 -d"capabilities[transfers][requested]"=true \
 -dbusiness_type=individual \
 -dcountry=US

```

## Déterminer les informations à collecter
Côté serveur
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
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
Pour mettre en œuvre votre stratégie d’inscription, vérifiez le hash requirements du compte connecté que vous avez créé. Le hash requirements fournit une liste complète des paramètres que vous devez recueillir pour activer le compte connecté.
  * Pour l’inscription progressive, examinez le champ `currently_due` dans le hash requirements et créez un flux d’inscription qui collecte uniquement les paramètres répertoriés.
  * Pour l’inscription complète, vérifiez le champ `eventually_due` dans le hash requirements et créez un flux d’inscription des utilisateurs qui collecte tous les paramètres répertoriés.


```

{
 ...
 "requirements":{"alternatives":[],"current_deadline":null,"currently_due":["business_profile.product_description","business_profile.support_phone","business_profile.url","external_account","tos_acceptance.date","tos_acceptance.ip"],"disabled_reason":"requirements.past_due","errors":[],"eventually_due":["business_profile.product_description","business_profile.support_phone","business_profile.url","external_account","tos_acceptance.date","tos_acceptance.ip"],"past_due":[],"pending_verification":[]},
 ...
}

```

## Mettre à jour le compte connecté
Côté serveur
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Mettez à jour l’objet Connected Account avec de nouvelles informations à chaque étape du flux d’inscription des utilisateurs pour permettre à Stripe de valider les informations dès qu’elles sont ajoutées. Une fois que Stripe a confirmé l’acceptation de nos conditions d’utilisation du service, toute modification apportée au compte connecté déclenche une revérification. Par exemple, si vous modifiez le nom et l’identifiant du compte connecté, Stripe procède à une nouvelle vérification.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/accounts/
{{CONNECTED_ACCOUNT_ID}}
 \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 --data-urlencode"business_profile[url]"="https://furever.dev" \
 -d"tos_acceptance[date]"=1609798905 \
 -d"tos_acceptance[ip]"="8.8.8.8"

```

Lors de la mise à jour d’un compte connecté, vous devez gérer les erreurs de vérification ou les codes d’erreur HTTP.
## Gérer les erreurs de vérification
Côté serveur
![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Lors de la soumission des données du compte connecté, Stripe procède à leur vérification. Ce processus peut prendre quelques minutes comme quelques heures, selon la nature de la vérification requise. Au cours de ce processus, les fonctions que vous avez demandées sont en attente.
### État de la vérification![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez récupérer l’état des fonctionnalités de votre compte connecté des manières suivantes :
  * Examen du hash des fonctionnalités de l’objet Account pour la fonctionnalité concernée.
  * Demandez des fonctionnalités directement à partir de l’API Capabilities et examinez l’état de la fonctionnalité concernée.
  * Écoutez les événements `account.updated` dans votre endpoint de webhook et inspectez le hash `capabilities` pour la fonctionnalité correspondante.


Une fois les vérifications terminées, la fonctionnalité devient `active` et le compte connecté peut en bénéficier. Les comptes étant vérifiés régulièrement, une fonctionnalité peut ne plus être `active` si une vérification ultérieure échoue. Écoutez les événements `account.updated` pour détecter les changements d’état des fonctionnalités.
Confirmez que votre intégration Connect est conforme et opérationnelle en vérifiant que les paramètres `charges_enabled` et `payouts_enabled` du compte sont tous deux définis sur « true ». Vous pouvez utiliser l’API ou écouter les événements `account.updated`. Pour plus d’informations sur les autres champs pertinents, vérifiez le hash des exigences du compte. Vous ne pouvez pas confirmer l’intégration sur la base d’une seule valeur, car les états peuvent varier selon l’application et les politiques associées.
  * charges_enabled confirme que votre chemin de paiement complet (paiement et transfert) fonctionne correctement et détermine si les fonctions `card_payments` et `transfers` sont actives.
  * payouts_enabled détermine si votre compte connecté peut effectuer des virements vers un compte externe. En fonction de vos politiques en matière de risques, vous pouvez autoriser votre compte connecté à commencer à effectuer des transactions sans avoir activé les virements. À terme, vous devrez activer les virements pour verser des fonds sur vos comptes connectés.


Vous pouvez partir de la logique suivante pour définir un état récapitulatif à afficher pour votre compte connecté.
Ruby
```

# Set your secret key. Remember to switch to your live secret key in production.# See your keys here: https://dashboard.stripe.com/apikeysStripe.api_key =
'sk_test_Hrs6SAopgFPF0bZXSN3f6ELN'
defaccount_state(account)
 reqs = account.requirements
 if reqs.disabled_reason && reqs.disabled_reason.include?("rejected")"rejected"elsif account.payouts_enabled && account.charges_enabled
  if reqs.pending_verification
   "pending enablement"elsif!reqs.disabled_reason &&!reqs.currently_due
   if!reqs.eventually_due
    "complete"else"enabled"endelse"restricted"endelsif!account.payouts_enabled && account.charges_enabled
  "restricted (payouts disabled)"elsif!account.charges_enabled && account.payouts_enabled
  "restricted (charges disabled)"elsif reqs.past_due
  "restricted (past due)"elsif reqs.pending_verification
  "pending (disabled)"else"restricted"endend
accounts =Stripe::Account.list(limit:10)
accounts.eachdo|account|
  puts "#{account.id} has state: #{account_state(account)}"end

```

#### Remarque
Vous ne pouvez pas utiliser l’API pour répondre aux vérifications des risques de Stripe. Vous pouvez autoriser vos comptes connectés à répondre à l’aide de composants intégrés, d’une procédure d’inscription hébergée par Stripe ou de liens de rectification. Vous avez également la possibilité d’utiliser le Dashboard pour répondre à des vérifications des risques au nom de vos comptes connectés.
Écoutez l’événement account.updated. Si le compte contient des champs `currently_due` à l’arrivée de la date `current_deadline`, la fonctionnalité correspondante est désactivée et ces champs sont ajoutés à `past_due`.
Créez un formulaire donnant des instructions claires que le compte pourra utiliser pour corriger ses informations. Informez le compte, puis soumettez les informations corrigées à l’aide de l’API Accounts.
account.updated event
Si `requirements.currently_due` contient des champs
Dirigez le compte vers le processus d’inscription suffisamment tôt pour que celui-ci soit terminé avant la date current_deadline
Aucune action requise
Si `requirements.past_due` contient des champs
Le compte est peut-être désactivé ; dirigez-le vers le flux d’inscription
Présenter une interface utilisateur générée dynamiquement pour collecter et valider les champs
Mettre à jour le compte en y ajoutant les champs collectés
Si `requirements.currently_due` contient des champs
OuiOuiNonNon
Si vous prévoyez de créer des flux personnalisés pour gérer l’ensemble de vos erreurs de vérification :
  * Consultez les informations concernant toutes les erreurs de vérification possibles et comment les gérer.
  * Tester les états de vérification.


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
Définir des exigences
Créer des formulaires pour collecter des informations
Inclure le consentement aux Conditions d’utilisation du service Stripe
Créer un compte connecté
Déterminer les informations à collecter
Mettre à jour le compte connecté
Gérer les erreurs de vérification
État de la vérification
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

