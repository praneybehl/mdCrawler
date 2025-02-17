Accéder directement au contenu
Virements vers des comptes connectés
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
Virements vers des comptes connectés
Gérer les comptes de virement pour les comptes connectés
Gérer la fréquence des virements
Virements manuels
Annulation de virements
Libellés de relevé bancaire pour les virements
Règlement multidevise
Instant Payouts
Virements internationaux
Virements en cryptomonnaie stable


Gérer votre plateforme Connect
Formulaires fiscaux pour votre plateforme Connect
Utiliser les types de comptes connectés
Intégration avec Accounts v2
Canada
Français (France)
AccueilPlateformes et places de marchéPay out to accounts
# Virements vers des comptes connectés
## Gérez les virements et les comptes externes pour les comptes connectés de votre plateforme.
Par défaut, tout paiement que vous effectuez au nom d’un compte connecté vient s’ajouter au solde de ce dernier et fait l’objet d’un virement quotidien de façon continue. En fonction des paramètres de vos comptes connectés, votre plateforme peut gérer leurs virements comme suit :
  * Établir la fréquence des virements automatiques
  * Effectuer des virements manuels
  * Verser des fonds instantanément
  * Lorsque vous utilisez des paiements indirects ou des paiements et transferts distincts, conserver des fonds sur le solde de votre plateforme


#### Remarque
Dans les versions de Connect antérieures à 2018, les virements était désignés par le terme de « virements bancaires » et utilisaient l’API `transfers`, désormais obsolète. Pour en savoir plus sur les virements bancaires, consultez la documentation de l’ancienne API Transfers.
## Configurations de gestion des virements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Pour les comptes connectés ayant accès au Dashboard Stripe complet ou au Dashboard Express, le titulaire du compte gère ses comptes de virement externes (comptes bancaires et cartes de débit), mais la plateforme peut établir la fréquence des virements. Pour programmer des virements pour un compte qui a accès au Dashboard Stripe complet, la plateforme doit configurer les contrôles de la plateforme pour le compte.
Pour les comptes connectés qui n’ont pas accès à un Dashboard hébergé par Stripe, la plateforme gère leurs comptes de virement externes et peut établir la fréquence de leurs virements.
## Devises de règlement prises en charge![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Choisissez un pays dans la liste déroulante suivante pour connaître les devises que vous pouvez utiliser pour régler des fonds dans ce pays.
#### Remarque
Pour connaître la liste des devises de présentation prises en charge, consultez la documentation sur les devises.
Affichage des devises de règlement prises en charge pour les comptes Stripe créés dans le pays suivant:
Allemagne (DE)Australie (AU)Autriche (AT)Belgique (BE)Brésil (BR)Bulgarie (BG)Canada (CA)Chypre (CY)Croatie (HR)Danemark (DK)Émirats arabes unis (AE)Espagne (ES)Estonie (EE)États-Unis (US)Finlande (FI)France (FR)Gibraltar (GI)Grèce (GR)Hong Kong (HK)Hongrie (HU)Inde (IN)Irlande (IE)Italie (IT)Japon (JP)Lettonie (LV)Liechtenstein (LI)Lituanie (LT)Luxembourg (LU)Malaisie (MY)Malte (MT)Mexique (MX)Norvège (NO)Nouvelle-Zélande (NZ)Pays-Bas (NL)Pologne (PL)Portugal (PT)République tchèque (CZ)Roumanie (RO)Royaume-Uni (GB)Singapour (SG)Slovaquie (SK)Slovénie (SI)Suède (SE)Suisse (CH)Thaïlande (TH)
Chargement d'un tableau des devises de virement Connect
Les plateformes peuvent également permettre à leurs comptes connectés de recevoir des fonds et d’effectuer des virements vers des banques dans certaines devises autres que la devise principale, ou d’effectuer des virements vers des comptes bancaires étrangers dans la devise locale. Dans certains cas, Stripe facture des frais. Pour en savoir plus, consultez la page sur le virement multidevise pour les plateformes et les marketplaces Connect.
### Utiliser des destinations d’événements avec des virements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez suivre toutes les activités de virement sur les comptes connectés à l’aide de destinations d’événements en écoutant ces événements :
  * `payout.created`
  * `payout.updated`
  * `payout.paid`
  * `payout.failed`


Pour la plupart des virements, les notifications d’événement se produisent sur plusieurs jours. Les virements instantanés envoient généralement l’événement `payout.paid` dans les 30 minutes qui suivent.
Lorsqu’un virement n’aboutit pas, un événement `payout.failed` se produit. La propriété `failure_code` de l’événement en indique la raison. Un virement échoué désactive également le compte externe impliqué dans ce virement, déclenchant un événement `account.external_account.updated`. Aucun virement ne peut être effectué sur ce compte externe tant que la plateforme n’a pas mis à jour les comptes externes du compte connecté.
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
Configurations de gestion des virements
Devises de règlement prises en charge
Utiliser des destinations d’événements avec des virements
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

