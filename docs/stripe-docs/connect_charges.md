Accéder directement au contenu
Créer un paiement
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
AccueilPlateformes et places de marchéAccept payments
# Créer un paiement
## Créer un paiement et répartir les fonds entre votre plateforme et vos marchands ou prestataires de services.
Pour accepter le paiement d’un client, vous devez d’abord créer un paiement. Le type de paiement que vous choisissez de créer (direct, indirect, ou paiements et transferts distincts) détermine la manière dont ces fonds sont répartis entre toutes les parties concernées. Il affecte également la manière dont le débit apparaît sur le relevé bancaire ou de facturation du client (avec les informations de votre plateforme ou celles de votre utilisateur), et détermine le compte qui sera débité pour les remboursements et les contestations de paiement.
## Types de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
De nombreux facteurs entrent en jeu dans le choix d’un type de paiement, comme indiqué dans le tableau ci-dessous. Le modèle économique de votre plateforme est particulièrement important, car il peut affecter la manière dont les fonds transitent par Stripe. Afin de consulter les types de paiement recommandés pour votre activité, référez-vous au profil de votre plateforme.
Type de paiement| Applications| Exemples  
---|---|---  
Paiements directs| 
  * Les clients effectuent directement des transactions avec votre compte connecté, souvent sans connaître l’existence de votre plateforme.
  * La transaction implique un seul utilisateur.
  * Vous souhaitez choisir si les frais Stripe sont débités de vos comptes connectés ou de votre plateforme

| 
  * Une plateforme d’e-commerce comme Shopify et Squarespace
  * Une plateforme comptable qui permet le paiement des factures, comme Freshbooks

  
Paiements indirects| 
  * Les clients effectuent des transactions sur votre plateforme pour des biens ou services proposés par votre compte connecté.
  * La transaction implique un seul utilisateur.
  * Les frais Stripe sont débités de votre compte de plateforme.

| 
  * Un service de chauffeur privé comme Lyft
  * Une plateforme de services comme Thumbtack

  
Paiements et transferts distincts| Dans les cas suivants :
  * La transaction implique plusieurs utilisateurs.
  * Un utilisateur particulier n’est pas connu au moment du paiement.
  * Le transfert ne peut pas être effectué au moment du paiement.
  * Les frais Stripe et les frais de traitement sont débités de votre compte de plateforme.

| 
  * Une place de marché en ligne qui autorise l’utilisation d’un seul panier d’achat pour les biens vendus par plusieurs entreprises

  
Vous pouvez adopter une seule ou plusieurs approches, ou changer de méthode selon les besoins de votre organisation.
### Paiements directs![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Créez un paiement direct sur un compte connecté. Les clients ignorent souvent l’existence de votre plateforme. Vous pouvez ajouter une commission de plateforme au paiement qui est transféré sur le solde du compte de votre plateforme.
Ce type de paiement est le mieux adapté aux plateformes SaaS. Par exemple, Shopify fournit des outils pour créer des vitrines en ligne et Thinkific permet aux enseignants de vendre des cours en ligne.
Avec ce type de paiement :
  * Vous créez un paiement sur le compte de votre utilisateur afin que le paiement apparaisse comme un paiement sur le compte connecté, et non dans le solde de votre compte.
  * Le solde du compte connecté augmente avec chaque paiement.
  * Les fonds sont toujours versés dans le pays du compte connecté.
  * Le solde de votre compte augmente avec les commissions de plateforme sur chaque paiement.
  * Le solde du compte connecté est débité des remboursements et des contestations de paiement.
  * Vous pouvez choisir de faire débiter les frais par Stripe directement des comptes connectés ou de votre compte de plateforme.


![Diagramme des mouvements de fonds des paiements directs](https://b.stripecdn.com/docs-statics-srv/assets/direct_charges.a2a8b68037ac95fe22140d6dde9740d3.svg)
Comment les fonds sont-ils acheminés avec les paiements directs ?
#### Mise en garde
Seuls les comptes connectés dotés de la fonctionnalité card_payments peuvent faire l’objet de paiements directs.
### Paiements indirects![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Créez un paiement sur la plateforme et transférez immédiatement les fonds sur un compte connecté spécifié. Vous décidez si une partie ou la totalité de ces fonds est transférée, et si une commission de plateforme est déduite.
Ce type de paiement est le mieux adapté aux places de marché telles qu’Airbnb (location de logements) ou Lyft (covoiturage).
Avec ce type de paiement :
  * Vous créez un paiement sur le compte de votre plateforme afin que le paiement apparaisse comme un paiement sur votre compte. Ensuite, vous déterminez si ces fonds sont à transférer partiellement ou en totalité à votre compte connecté (voir les diagrammes des mouvements de fonds ci-dessous).
  * Le solde du compte de votre plateforme sera débité du coût des frais Stripe, des remboursements et des contestations de paiement.


![Diagramme des mouvements de soldes des paiements indirects](https://b.stripecdn.com/docs-statics-srv/assets/platform_charges.6a14fd660d7433ba617e816ff09f10b5.svg)
Envoyez le solde déduction faite des frais de plateforme à votre compte connecté.
![Diagramme des mouvements de fonds des paiements indirects](https://b.stripecdn.com/docs-statics-srv/assets/application_fee_amount.837aa2339469b3c1a4319672971c1367.svg)
Envoyez l’intégralité du paiement à votre compte connecté, puis facturez vos frais de plateforme.
#### Mise en garde
Dans la plupart des cas, les paiements indirects ne sont pris en charge que si votre plateforme et le compte connecté se trouvent dans la même région (par exemple, aux États-Unis). Pour la prise en charge interrégionale, vous pouvez indiquer l’entité de règlement au compte connecté à l’aide de l’attribut on_behalf_of sur le paiement. Pour plus d’informations sur la prise en charge interrégionale, consultez la section Transferts internationaux.
### Paiements et transferts distincts![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Créez des paiements sur votre plateforme et répartissez les fonds entre plusieurs comptes connectés, ou retenez-les lorsque vous ne connaissez pas l’utilisateur concerné au moment du paiement. Le paiement sur votre compte de plateforme est dissocié des transferts vers vos comptes connectés.
Ce type de frais convient mieux aux places de marché qui doivent répartir les paiements entre plusieurs parties, comme DoorDash, une plateforme de livraison de plats à domicile.
Pour les comptes Express et Custom, Stripe vous recommande de créer des paiements et transferts distincts si les paiements indirects ne répondent pas aux besoins de votre activité.
Avec ce type de paiement :
  * Pour commencer, vous créez un paiement sur le compte de votre plateforme. Vous créez ensuite un transfert distinct pour transférer des fonds sur votre compte connecté. Le paiement apparaît comme un paiement sur votre compte, et il y a également un transfert vers un compte connecté (dont vous déterminez le montant), qui est prélevé du solde de votre compte.
  * Vous pouvez transférer des fonds vers plusieurs comptes connectés
  * Le solde de votre compte sera débité du coût de la commission Stripe, des remboursements et des contestations de paiement.


![Diagramme des transferts de fonds](https://b.stripecdn.com/docs-statics-srv/assets/charges_transfers.a95f5bf398651fba0fb303e32a742546.svg)
Transférez des fonds vers plusieurs comptes connectés.
#### Mise en garde
Dans la plupart des cas, votre plateforme et le compte connecté doivent se trouver dans la même région. Toute tentative de transfert de fonds au-delà d’une frontière non autorisée renvoie une erreur. Pour plus d’informations sur la prise en charge interrégionale, consultez Transferts internationaux.
L’utilisation de paiements et transferts distincts nécessite une intégration Connect plus complexe.
Utilisez ce type de paiement si votre entreprise a des cas d’usage spécifiques :
  * Une relation de type « one-to-many ». Par exemple, un paiement effectué à un service de livraison doit être réparti entre le magasin (la source des articles livrés) et le livreur.
  * Une relation de type « many-to-one ». Par exemple, un déplacement en covoiturage avec un service de chauffeur privé.
  * Des paiements créés avant que le compte de destination ne soit connu. Par exemple, un service de conciergerie peut traiter un paiement avant de décider à quel concierge affecter cette tâche.
  * Besoin de transférer des fonds avant de recevoir un règlement, ou pendant que le paiement est en attente. Par exemple, un réseau publicitaire doit acheter de l’espace publicitaire avant de pouvoir vendre du temps d’antenne ou avant de recevoir un paiement de la part des clients.
  * Des transferts d’un montant supérieur aux paiements associés. Par exemple, une plateforme octroie une remise au client mais paie le montant total à son utilisateur.


Dans certains cas, le montant du transfert peut être supérieur au montant du paiement, ou le transfert est effectué avant le traitement du paiement. Vous devez surveiller attentivement le solde de votre compte pour vous assurer qu’il dispose de fonds suffisants pour couvrir le montant du transfert. Vous pouvez également associer un transfert à un paiement afin que le transfert n’ait pas lieu tant que les fonds de ce paiement ne sont pas disponibles.
#### paramètre on_behalf_of![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Afin de faire du compte connecté l’entreprise de référence pour le paiement, utilisez le paramètre `on_behalf_of`. Lorsque `on_behalf_of` est défini sur l’ID du compte connecté, Stripe :
  * Règle les paiements dans le pays du compte spécifié, minimisant ainsi les refus et évitant les conversions de devises.
  * Utilise la structure des frais appliquée pour le pays du compte connecté.
  * Utilise le libellé de relevé bancaire du compte connecté.
  * Si le compte relève d’un pays différent de celui de la plateforme, l’adresse et le numéro de téléphone du compte connecté figurent sur le relevé de carte bancaire du client (et non sur celui de la plateforme).
  * Le nombre de jours durant lesquels un solde en attente est bloqué avant d’être versé dépend du paramètre `delay_days` du compte connecté.


## Frais de paiement Stripe![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Les frais de Stripe avec Connect comportent deux éléments : le plan tarifaire qui s’applique au paiement et le compte qui paie les frais Stripe.
Lorsque vous utilisez les paiements directs, vous pouvez choisir comment les frais Stripe sont facturés à vos comptes connectés.
En savoir plus sur les comportements en matière de facturation des frais avec les paiements directs.
Les paiements indirects ainsi que les paiements et transferts distincts utilisent généralement le plan tarifaire de la plateforme et les frais sont évalués sur la plateforme. Lorsque le champ `on_behalf_of` est défini, le pays du compte connecté est utilisé pour déterminer les frais spécifiques au pays facturés au compte de votre plateforme.
Pour plus d’informations sur les frais Connect et sur la manière de demander une tarification personnalisée, veuillez consulter les tarifs Connect.
## Remboursements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Vous pouvez émettre un remboursement pour restituer l’argent dépensé pour le produit retourné ou pour compenser un service insatisfaisant. Vous trouverez ci-dessous une description de la manière dont les remboursements sont traités pour chaque type de paiement :
Types de paiement| Remboursements en attente  
---|---  
**Paiements directs**|  Si le solde du compte connecté est suffisamment négatif au moment de la création, l’état de l’objet `refund` devient `pending`. Lorsque le solde du compte connecté est suffisant, Stripe traite automatiquement tous les remboursements dont l’état est `pending` et met à jour l’état qui devient `successful`.  
**Paiements et transferts distincts**|  Si le solde du compte connecté et le solde du compte de votre plateforme sont suffisamment négatifs au moment de la création, l’état de l’objet `refund` devient `pending`. Lorsque des fonds suffisants deviennent disponibles dans le solde de votre compte connecté ou de votre plateforme, Stripe traite automatiquement tous les remboursements dont l’état est `pending` et met à jour leur état qui devient `successful`.  
**Paiements indirects**|  Si le solde du compte de votre plateforme est suffisamment négatif au moment de la création, l’état de l’objet `refund` devient `pending`. Lorsque des fonds suffisants deviennent disponibles dans le solde de votre plateforme, Stripe traite automatiquement tous les remboursements dont l’état est `pending` et met à jour leur état qui devient `successful`.Si le solde du compte connecté est suffisamment négatif et qu’une demande de remboursement tente également d’annuler le transfert, la demande de remboursement renvoie une erreur, au lieu de créer un remboursement à l’état `pending`.  
## Litiges et contestations de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Dans le cas des litiges portant sur des paiements directs, Stripe débite le montant contesté du solde du compte connecté, et non du solde de votre plateforme. Stripe peut facturer les frais de litige à la plateforme ou au compte connecté, en fonction de la configuration du compte connecté. Pour en savoir plus sur la façon dont nous facturons les frais de litige dans le cadre des paiements directs, consultez la page Comportement des frais sur les comptes connectés.
Pour les litiges associés à des paiements créés sur votre plateforme en utilisant des paiements indirects ou des paiements et transferts distincts, avec ou sans l’attribut `on_behalf_of`, le solde de votre plateforme est automatiquement débité du montant litigieux et des frais. Dans ce cas, votre plateforme peut tenter de récupérer les fonds du compte connecté en annulant le transfert, soit par le biais du Dashboard, soit en créant une annulation de transfert.
#### Mise en garde
Lorsque vous créez des paiements indirects ou des paiements et transferts distincts avec ou sans `on_behalf_of`, les montants remboursés et contestés sont toujours débités du solde de votre plateforme, même lorsque Stripe assume la responsabilité des soldes négatifs de vos comptes connectés.
Si le compte connecté présente un solde négatif, Stripe tente de débiter le compte externe enregistré du compte connecté uniquement si le paramètre `debit_negative_balances` est défini sur `true`.
Pour des détails supplémentaires, consultez les rubriques Litiges et fraudes et Catégories de litiges. Vous pouvez également utiliser Stripe Apps pour la fraude afin d’automatiser la gestion des litiges et traiter les contestations de paiement.
## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Créer des paiements directs
  * Créer des paiements indirects
  * Créer des paiements et transferts distincts
  * Configuration des libellés de relevé bancaire
  * Moyens de paiement pris en charge
  * Intégrer le calcul et la collecte des taxes


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
Types de paiement
Paiements directs
Paiements indirects
Paiements et transferts distincts
Frais de paiement Stripe
Remboursements
Litiges et contestations de paiement
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

