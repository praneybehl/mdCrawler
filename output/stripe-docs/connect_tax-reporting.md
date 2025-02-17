Accéder directement au contenu
Présentation
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
Effectuer des virements vers des comptes
Gérer votre plateforme Connect
Formulaires fiscaux pour votre plateforme Connect
Présentation
Commencez à utiliser l'outil de déclaration fiscale///
Guide de communication et de support concernant les formulaires fiscaux 1099
Paramètres des formulaires fiscaux
Méthodes de calcul
Informations d'identité sur les formulaires fiscaux
Envoyer les formulaires fiscaux
Envoi des formulaires fiscaux aux États
Identifier les formulaires comportant des informations manquantes
Créer et modifier des formulaires fiscaux
Dépôt des formulaires fiscaux
Envoyer des formulaires fiscaux via le Dashboard Express
Corriger les formulaires fiscaux
Fractionner des formulaires fiscaux
Passage d'un exercice fiscal à un autre
Rapports fiscaux pour plateforme (hors États-Unis)


Utiliser les types de comptes connectés
Intégration avec Accounts v2
Canada
Français (France)
AccueilPlateformes et places de marchéTax forms for your Connect platform
# Déclarations fiscales aux États-Unis pour les plateformes Connect
## Découvrez comment déclarer les paiements annuels de vos comptes connectés établis aux États-Unis.
Stripe Connect permet aux plateformes de fournir un service de paiement de bout-en-bout et fluide pour leurs comptes connectés. Ce service peut engendrer certaines responsabilités, notamment le reporting des informations fiscales.
#### Obtention de vos formulaires fiscaux 1099
Si vous travaillez pour une plateforme qui vous paie via Stripe et que vous souhaitez en savoir plus sur vos formulaires 1099 et sur la manière de les obtenir, consultez la page dédiée aux formulaires fiscaux 1099 sur le site du service Support de Stripe.
Stripe émet des formulaires 1099-K pour vos comptes connectés qui contiennent des transactions pour lesquelles `controller.fees.payer` = `account` ou `application_unified_accounts_beta`.
Dans le cas des transactions pour lesquelles `controller.fees.payer` = `application`, si vos comptes connectés paient les frais de traitement de ces transactions à Stripe, ils pourraient être inclus dans un formulaire 1099 émis par Stripe.
Pour tous les autres types de comptes qui réalisent des transactions, Stripe n’émettra pas de formulaire 1099-K à vos comptes connectés (par exemple, lorsque `controller.fees.payer` = `application_custom` ou `application_express` ou `application` pour lesquels vous payez les frais de traitement). Envisagez plutôt d’émettre un formulaire 1099 pour déclarer les revenus et les transactions de paiement. Il existe plusieurs types de formulaires 1099 : pour choisir le formulaire approprié, prenez en compte les types de paiements que vous effectuez sur votre compte connecté.
#### Remarque
Stripe vous recommande de contacter un conseiller fiscal pour avoir une idée précise des formulaires fiscaux à soumettre et des informations à fournir.
## 1099-NEC![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Utilisez le formulaire 1099-NEC pour déclarer la rémunération des non-salariés.
Le compte doit répondre à tous les critères suivants dans l’année calendaire antérieure :
  * Établi aux États-Unis ou contribuable américain
  * $600 or more in payments


## 1099-MISC![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Utilisez le formulaire 1099-MISC pour déclarer les autres formes de paiements réalisées dans le cadre de votre activité.
Le compte doit répondre à tous les critères suivants dans l’année calendaire antérieure :
  * Établi aux États-Unis ou contribuable américain
  * $600 or more in payments or $10 in royalties


## 1099-K![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Utilisez le formulaire 1099-K pour déclarer les transactions de paiement.
Le compte doit répondre à tous les critères suivants dans l’année calendaire antérieure :
  * Établi aux États-Unis ou contribuable américain
  * More than $5,000 in gross volume
  * Plus de 0 transactions


## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Démarrez avec le produit de déclaration fiscale 1099 de Stripe
  * Configurez vos paramètres de formulaire fiscal


#### Remarque
Vous avez besoin d’aide pour le calcul des taxes sur les ventes, de la TVA ou de la TPS ? Consultez Stripe Tax.
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
1099-NEC
1099-MISC
1099-K
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

