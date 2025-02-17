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
Gestion des versions
Journal des modifications
Présentation
Acacia
Versions précédentes


Mettre à niveau votre version de l'API
Actualiser votre version du SDK
Outils de développement
SDK
API
Tests
Workbench
Destinations d'événements
CLI Stripe
Shell Stripe
Dashboard des développeurs
Boîte à outils des agents
Stripe pour Visual Studio CodeChargements de fichiersCommentaires
Sécurité
Sécurité
Extensions Stripe
Stripe Apps
Connecteurs Stripe
Partenaires
Partner ecosystemCertification des partenaires
Canada
Français (France)
AccueilOutils de développement
# Changelog
## Suivez les évolutions et mises à niveau de l'API Stripe.
ProduitDerniers changements
## Acacia![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Découvrez ce qui change dans Acacia
### 2025-01-27.acacia![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
#### Informations sur l’entreprise pour les comptes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de la prise en charge du motif d’exemption de propriété à l’API Accounts| Connect  
---|---  
Ajoute une déclaration de directeur à l’API Accounts| Connect  
Ajout d’un justificatif de bénéficiaire effectif comme type de document| Connect  
#### Amélioration des moyens de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de la prise en charge du moyen de paiement local Pay by Bank| Checkout+ 1 de plus  
---|---  
Ajout de la propriété country PayPal aux objets PaymentMethods et Charge| Payments  
#### Améliorations apportées à Checkout![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout d’un champ pour les réductions aux sessions Checkout| Checkout  
---|---  
Ajout du Soudan aux pays d’expédition autorisés pour Checkout| Checkout  
#### Mises à jour supplémentaires![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout d’advice code aux paiements| Payments  
---|---  
Modifier la collecte des numéros de téléphone sur Payment Links| Payment Links  
Mise à disposition générale des composants intégrés pour Issuing et Treasury| Issuing+ 1 de plus  
Ajout de la prise en charge de plusieurs comptes financiers par entreprise| Treasury  
Ajout de la prise en charge de l’encaissement de pourboires en JPY dans Terminal| Terminal  
### 2024-12-18.acacia![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
#### Améliorations apportées aux virements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de la prise en charge des SDK pour les ID de suivi| Payments  
---|---  
Ajout de nouveaux types d’opérations sur solde pour prendre en charge le solde minimum| Payouts  
#### Améliorations Issuing![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Les autorisations Issuing comprennent désormais le numéro d’identification fiscale du marchand| Issuing  
---|---  
Crée des autorisations Issuing lorsque Stripe est indisponible| Issuing  
#### Amélioration des moyens de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout d’informations supplémentaires sur le bénéficiaire pour les paiements par virement bancaire| Payments  
---|---  
Ajout des informations relatives aux financements aux paiements Amazon Pay et Revolut Pay| Payments  
Ajout de la prise en charge du préfixe de la référence du mandat de prélèvement SEPA et Bacs| Checkout+ 1 de plus  
#### Améliorations fiscales![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout du motif de la désactivation aux factures, aux abonnements et aux calendriers| Tax+ 2 de plus  
---|---  
Ajout de la prise en charge de types de numéros fiscaux dans dans 19 nouveaux pays| Tax  
Ajout de la prise en charge de 21 nouveaux pays à l’API Tax Registration| Tax  
#### Améliorations apportées à la facturation![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de la prise en charge du rétablissement des crédits de facturation en cas d’annulation de facture| Billing+ 1 de plus  
---|---  
Modifier des abonnements d’essai créés par Payment Links| Payment Links  
La configuration du portail de facturation renvoie systématiquement la date de fin de période dans les réponses| Billing  
#### Mises à jour supplémentaires![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout d’une requête de signature comme option de remplacement pour l’API Vault and Forward  
---  
Ajout des codes d’avis et de refus des réseaux| Payments  
Prise en charge du réaffichage des moyens de paiement pour les objets Card et Source| Payments  
Ajoute des autorisations au niveau des champs pour le chiffre d’affaires et l’effectif dans le profil d’entreprise d’un compte| Connect  
Ajout de l’ID de transaction réseau aux paiements| Payments  
Ajout d’un champ d’état réglementé aux objets de carte dans plusieurs API| Payments  
### 2024-11-20.acacia![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
#### Prise en charge de nouveaux types de taxes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de la prise en charge du type Taxe sur les services| Tax  
---|---  
Ajoute la prise en charge du numéro fiscal pour la TVA du Liechtenstein| Tax  
#### Améliorations Issuing![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajoute la prise en charge du montant et de la devise du marchand pour les autorisations en mode test| Issuing  
---|---  
Ajout de la prise en charge des étapes de détection de la fraude pour Issuing| Issuing  
#### Plus grande flexibilité en matière de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajoute la prise en charge d’Adaptive Pricing par les sessions Checkout| Checkout  
---|---  
Personnaliser le bouton d’envoi récurrent des liens de paiement et des sessions Checkout| Checkout+ 1 de plus  
Ajout de la prise en charge de fonctionnalités de cartes bancaires avancées dans les sessions Checkout| Checkout  
Permet aux intégrations Link pour carte bancaire uniquement d’accepter des moyens de paiement autres que les cartes bancaires sous la marque de carte Link| Payments  
Ajout d’informations supplémentaires sur le bénéficiaire pour les paiements par virement bancaire| Payments  
#### Amélioration des moyens de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout du champ de code de refus de paiement donné par le réseau pour les remboursements Swish et BLIK| Payments  
---|---  
Ajoute la prise en charge des préfixes de référence sur les mandats de prélèvement automatique SEPA et Bacs dans les sessions Checkout| Checkout  
La spécification du moyen de paiement d’origine des transferts entrants est désormais facultative| Treasury  
Utilisez des méthodes de capture configurables et paramétrez les moyens de paiement sud-coréens en vue d’une utilisation future| Checkout  
#### Mises à jour supplémentaires![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Suivi des virements à l’aide d’un identifiant unique| Payouts  
---|---  
Les propriétés de l’objet Account ont été converties en énumération (au lieu d’une chaîne de caractères précédemment)| Connect  
Les comptes connectés reçoivent un message indiquant qu’ils doivent se connecter pour pouvoir utiliser les composants intégrés| Connect  
Ajout de la prise en charge des signataires autorisés à l’API Person| Connect  
### 2024-10-28.acacia![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
#### Octrois de crédit Billing![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout d’API et de ressources pour l’octroi de crédits| Billing+ 1 de plus  
---|---  
Ajout de la prise en charge des informations sur le montant du crédit avant les taxes sur les factures| Billing+ 1 de plus  
Ajout de la prise en charge des informations sur le montant du crédit avant les taxes sur les avoirs| Billing+ 1 de plus  
#### Nouveaux moyens de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de la prise en charge de nouveaux moyens de paiement en Corée du Sud| Billing+ 5 de plus  
---|---  
Ajout de la prise en charge d’Alma en France| Checkout+ 3 de plus  
#### Destinations d'événements et types d'événements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout d’un endpoint d’API v2 pour les destinations d’événements  
---  
Ajout d’un type d’événement pour la mise à jour des données de réception dans les transactions Issuing| Issuing  
#### Amélioration des moyens de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout d’un champ de métadonnées à l’API Vault and Forward| Payments  
---|---  
Ajout de la prise en charge de la devise polonaise PLN à la configuration des pourboires de Terminal| Terminal  
Prise en charge de l’enregistrement du domaine pour Amazon Pay| Elements  
#### Options supplémentaires d'immatriculation fiscale![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de la prise en charge de nouveaux pays à l’API Tax Registration| Tax  
---|---  
Prise en charge de types de numéros fiscaux dans plusieurs nouveaux pays| Tax  
Ajout de la prise en charge de la perception des frais de livraison aux particuliers| Tax  
Ajout d’une option permettant de valider automatiquement le lieu de la taxe du client lors d’une mise à jour| Tax  
#### Mises à jour supplémentaires![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de la prise en charge de la désactivation de l’authentification utilisateur Stripe pour certains composants intégrés| Connect  
---|---  
Ajout d’un assistant de test qui met à jour l’état d’expédition des cartes physiques| Issuing  
Ajout d’événements de création, de modification et d’échec pour tous les types de remboursements| Payments  
Ajout de groupes de tarification à l’API Accounts| Connect+ 1 de plus  
Ajout de la prise en charge des passages programmés à un abonnement inférieur sur le portail client| Billing  
Profil d’entreprise désormais facultatif pour la configuration du portail client| Billing  
Utilisation du programme Compelling Evidence 3.0 de Visa pour répondre aux litiges admissibles  
Prise en charge de la planification de la finalisation des factures| Invoicing  
### 2024-09-30.acacia![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Derniers changements
#### Ajoute des fonctions d'alerte, de suivi et de reporting à la facturation à l'usage![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de filtres contextuels aux alertes de facturation| Billing  
---|---  
Ajout d’une API Alerts pour la facturation à l’usage| Billing  
Ajout d’un événement pour les alertes de facturation déclenchées| Billing  
Ajout de la prise en charge de l’écoute des alertes de facturation déclenchées| Billing  
Ajout de ressources et d’endpoints pour les alertes de facturation| Billing  
Ajoute la prise en charge des abonnements et des postes d’abonnement dans les alertes de facturation| Billing+ 1 de plus  
Ajout d’endpoints d’API v2 pour les événements de mesure| Billing  
#### Améliorations pour les intégrations et lecteurs Terminal![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Mise à jour de la modélisation du consentement pour l’enregistrement des cartes bancaires avec Terminal| Terminal  
---|---  
Ajout de la prise en charge de la configuration de l’heure de redémarrage| Terminal  
Ajout du lecteur Stripe S700 comme type d’appareil valide| Terminal  
Ajout d’informations complémentaires concernant la collecte hors ligne sur les objets PaymentMethod avec `card_present`| Terminal  
#### Amélioration des moyens de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout d’une option de récupération des tokens CVC dans les tokens de confirmation| Elements  
---|---  
Ajout d’un ID client à l’aperçu des moyens de paiement dans un token de confirmation| Elements  
Ajout de la prise en charge de l’identification du payeur unique pour le moyen de paiement BLIK| Payments  
Ajout de la prise en charge des identifiants de transaction Affirm| Payments  
Ajout de la prise en charge des moyens de paiement en personne, y compris les cartes Interac| Terminal  
Affichage de l’attribut `authorization_code` pour les objets Charge| Payments  
Ajout d’informations de portefeuille pour les paiements et les moyens de paiement de type `card_present`| Terminal  
Ajout du champ country pour les paiements avec Klarna| Payments  
Affichage du type de litige Amazon Pay dans Litiges| Payments  
#### Ajout de la prise en charge de nouveaux moyens de paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de la prise en charge de trois nouveaux moyens de paiement : Multibanco, Twint et Zip| Payment Links  
---|---  
Le moyen de paiement Multibanco peut désormais être utilisé avec la facturation| Billing  
Ajout de Twint à l’API PaymentMethodConfiguration| Payments  
Ajout de Girocard comme marque de cartes et réseau de cartes dans les moyens de paiement| Payments  
#### Ajout des numéros fiscaux pour la Suisse et la Croatie, ainsi que d'exigences facultatives en matière de numéro fiscal![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de l’UID suisse en tant que numéro fiscal client pris en charge| Invoicing+ 1 de plus  
---|---  
Ajout de la prise en charge du numéro d’identification personnel croate| Billing+ 2 de plus  
Ajout de la prise en charge de la demande d’un numéro fiscal client dans Checkout et Payment Links| Checkout+ 1 de plus  
#### Prise en charge du filtrage pour Financial Connections![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de la prise en charge du filtrage par sous-catégorie de comptes dans Financial Connections| Financial Connections  
---|---  
Extension de la prise en charge du filtrage pour les sessions Financial Connections| Financial Connections  
#### Nouveaux codes d'erreur pour des tests plus robustes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout d’un code d’erreur pour les dépassements de la limite du nombre de transactions| Invoicing+ 1 de plus  
---|---  
Ajout d’un nouveau code d’erreur pour les préfixes de mandat non valides pour les paiements par prélèvement automatique Bacs et par prélèvement automatique SEPA| Payments  
#### Ajout d'une nouvelle ressource de modèle de rendu de facture![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de modèles de rendu pour les factures| Invoicing  
---|---  
Ajout de méthodes de récupération et d’archivage des modèles de rendu de factures| Invoicing  
Ajoute la prise en charge de modèles pour les objects Invoice et Customer| Invoicing  
Ajoute la prise en charge des versions de modèle de rendu de factures| Invoicing  
#### Amélioration de la validation des adresses et de la gestion des litiges et de la réglementation pour Issuing![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Mise à jour de la valeur par défaut pour la validation de l’adresse de livraison| Issuing  
---|---  
Ajout d’une validation des adresses pour les cartes physiques| Issuing  
Ajout d’un nouvel événement webhook pour les situations de déduction de fonds dans le cadre d’un litige| Issuing  
#### Traitement des factures simplifié![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de la prise en charge des opérations sur sous-postes de facture groupés| Invoicing  
---|---  
Ajout d’événements webhook pour les factures échues ou en retard| Billing  
Possibilité de finaliser automatiquement les factures| Invoicing  
#### Améliorations fiscales![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de la prise en charge de l’heure de comptabilisation lors de la création d’une transaction fiscale| Tax  
---|---  
Prise en charge ajoutée des paramètres fiscaux et des immatriculations fiscales pour les composants intégrés| Connect+ 1 de plus  
Ajout d’une nouvelle méthode pour récupérer le calcul d’une taxe| Tax  
Ajout de la prise en charge de la spécification d’options fiscales d’État sur les ventes lors de la création d’immatriculations fiscales| Tax  
#### Mises à jour supplémentaires![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Ajout de détails sur la vérification des risques pour les comptes connectés| Connect  
---|---  
Ajout de la prise en charge des types d’e-mail dans les avoirs| Invoicing  
Ajout de la prise en charge du Payment Element dans une session client| Elements  
Ajout de la prise en charge de l’identification du type de dossier des litiges au sujet des paiements par carte| Payments  
Ajout d’une méthode pour mettre à jour les métadonnées des sessions Checkout| Checkout  
Ajout d’un paramètre permettant d’associer des sessions de vérification à des objets Customer| Identity  
Affichage des informations de suivi CHIPS pour les virements et paiements sortants| Treasury  
Ajout de valeurs par défaut raisonnables supplémentaires à l’API v1 Account Link| Connect  
Rend le champ `LineItem.description` facultatif| Checkout  
Ajoute l’attribut `target_frozen_time` pour l’avancement des objets `test_helpers.test_clock`| Billing  
Rend obligatoires les informations d’état des outils d’aide aux tests pour horloge de simulation| Billing  
Ajout d’une nouvelle valeur d’énumération présentant un échec ReceivedDebit en raison d’une transaction internationale| Treasury  
Mise à jour des produits et des prix d’un abonnement désormais facultative| Billing  
Ajout de la prise en charge de `custom_unit_amount` lors de la création d’un produit| Checkout+ 1 de plus  
Ajout d’une prise en charge de la récupération des événements légers| Billing  
## 2024![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2024-06-20
Derniers changements
Un attribut `fuel` de l’objet `Authorization` a été renommé  
---  
Un attribut `purchase_details` de l’objet `Transaction` a été renommé  
Suppression des champs de carburant non documentés  
Suppression des champs de parc non documentés  
Ajout de valeurs d’énumération pour les unités de carburant  
Abandon de `alphanumeric_id` pour la ressource Issuing Authorization  
Ajout de valeurs d’énumération pour les motifs de désactivation  
Abandon du type de fonctionnalité `bank_transfer_payments` au profit de nouveaux types de fonctionnalités  
Ajout de nouvelles valeurs d’énumération pour les motifs liés à l’historique des demandes  
2024-04-10
Derniers changements
Synchronisation automatique de la méthode de capture par défaut pour PaymentIntents lorsqu’aucune méthode n’est précisée  
---  
L’attribut `rendering_options` a été renommé en `rendering` pour les factures  
L’attribut `features` de l’objet `Product` a été renommé  
## 2023![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2023-10-16
Derniers changements
Ajout de nouveaux codes d’erreur relatifs aux exigences de compte à l’API Accounts  
---  
Le libellé de relevé bancaire et le préfixe sont remplis automatiquement dans l’API Accounts  
2023-08-16
Derniers changements
Active les moyens de paiement automatiques par défaut pour PaymentIntents et SetupIntents  
---  
Les paiements ponctuels dans les sessions Checkout prennent en charge les commandes à coût zéro  
Rendu à l’échelle de la plate-forme pour certaines empreintes d’identification des moyens de paiement  
Ajout de codes d’erreur spécifiques pour les paiements Klarna échoués  
Ajout de nouveaux codes d’erreur relatifs à la vérification des directeurs à l’API Accounts  
## 2022![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2022-11-15
Derniers changements
L’objet `Charges` ne développe plus automatiquement les remboursements par défaut.  
---  
L’attribut `charges` a été supprimé de l’objet `PaymentIntent`  
Ajout de nouveaux codes de refus de paiement aux API PaymentIntent et PaymentMethod  
Ajout de nouveaux codes de refus de paiement à l’API SetupIntent  
Ajout d’un nouveau code d’erreur relatif à la structure pour l’API Accounts  
2022-08-01
Derniers changements
La valeur `include_and_require` a été supprimée lors de la création de factures  
---  
Changement du moyen de paiement par défaut au profit de `if_required` lors de la création de client dans une session Checkout  
Reporte la création de PaymentIntent dans le moyen de paiement Checkout Session  
La propriété `setup_intent` a été supprimée des sessions Checkout en mode abonnement  
Remplacement des paramètres relatifs aux postes de facture dans l’endpoint Créer une session Checkout  
Suppression du paramètre des données d’abonnement dans l’endpoint Créer une session Checkout  
Suppression du paramètre de tarif de livraison dans l’endpoint Créer une session Checkout  
Mise à jour des propriétés d’expédition de la session Checkout  
Ajout de l’état d’exemption de 3D Secure pour les paiements par carte  
Nouveau code d’erreur relatif à l’acceptation non valide des Conditions d’utilisation du service dans l’API Accounts  
Nouveaux endpoints pour la gestion de l’état d’expédition des cartes physiques en mode test  
Ajout de `design_rejected` comme motif d’annulation possible pour les cartes émises  
L’attribut `default_currency` a été supprimé de l’objet `Customer`  
## 2020![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2020-08-27
Derniers changements
Suppression de l’attribut `tax_percent`  
---  
Les attributs `phases` ont été renommés dans les planifications d’abonnement  
Le type d’événement qui se déclenche lors des mises à jour automatiques a été renommé  
La propriété `display_items` a été supprimée des sessions Checkout  
Exigences en matière de formats pour les personnes clés associées aux comptes  
Ajout de nouveaux codes d’erreur pour les API Accounts, Persons et Capabilities  
Mise à jour des informations de 3D Secure dans l’objet `Charge`  
Les abonnements clients ne sont plus développés automatiquement par défaut  
Les niveaux de tarification ne se développent plus automatiquement par défaut  
Les sources de clients ne sont plus développées automatiquement par défaut  
Les numéros fiscaux ne sont plus développés automatiquement dans l’objet `Customer`  
Abandon des paramètres d’abonnement `prorate` et `subscription_prorate`  
2020-03-02
Derniers changements
Les factures peuvent désormais être numérotées de manière séquentielle sur l’ensemble de votre compte  
---  
## 2019![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2019-12-03
Derniers changements
Standardisation des ID de postes de facture  
---  
Nouvelle exigence concernant `out_of_band_amount` lors de la création d’avoirs après paiement  
Les soldes clients sont désormais renvoyés lors de l’annulation des factures  
Les champs d’information fiscale abandonnés ont été supprimés de l’objet `Customer`  
2019-11-05
Derniers changements
La nouvelle exigence `requested_capabilities` a été ajoutée à création d’un compte Custom  
---  
Paramètres de planification d’abonnement imbriqués sous `default_settings`  
2019-10-17
Derniers changements
Les propriétés de renouvellement de la planification d’abonnement ont été renommées et mises à jour  
---  
Remplacement du champ `start` des abonnements par `start_date`  
Sur les factures, les abonnements et les planifications d’abonnement, `billing` a été renommé `collection_method`  
La propriété `due_date` des factures automatiques est toujours nulle  
L’attribut `account_balance` de l’objet `Customer` a été renommé `balance`  
2019-10-08
Derniers changements
L’attribut de relation d’un objet `Person` a été renommé  
---  
2019-09-09
Derniers changements
Dans de nombreux pays, il faut désormais spécifier des fonctionnalités au moment de la création du compte  
---  
Ajout de nouvelles valeurs `details_code` pour la vérification des documents d’identité des particuliers  
2019-08-14
Derniers changements
La fonctionnalité `platform_payments` des comptes a été renommée `card_payments`, et la fonctionnalité `transfers` ajoutée doit être spécifiée manuellement  
---  
La configuration d’une personne en tant que responsable de l’ouverture de compte ne lui confère plus automatiquement le statut de dirigeant  
2019-05-16
Derniers changements
Les paiements bancaires de type « pull » ne révèlent plus les remboursements système internes en cas d’échec  
---  
2019-03-14
Derniers changements
Le champ `application_fee` des factures a été renommé `application_fee_amount`  
---  
Les abonnements sont désormais correctement créés, même si le premier paiement échoue  
Les factures fournissent désormais des horodatages pour chaque changement d’état  
Le champ `date` des factures a été renommé `created`  
Les factures précisent désormais la date à laquelle elles sont finalisées, ainsi que d’autres changements d’état  
2019-02-19
Derniers changements
Modification des comportements de libellés des relevé bancaire pour les paiements par carte créés avec un objet Charges  
---  
Plusieurs champs des comptes ont été remaniés pour mieux décrire l’entité juridique, l’état de la vérification et les exigences, ainsi que les paramètres configurables  
Plusieurs champs décrivant les informations de l’entreprise d’un compte ont été déplacés vers le sous-hachage `business_profile`  
La vérification de comptes ou de personnes permet désormais de charger le recto et le verso d’un document  
Les comptes ne fournissent plus de champ `keys`. Les plateformes doivent utiliser leur propre clé API pour s’authentifier au nom de leurs comptes connectés  
Les comptes situés aux États-Unis doivent désormais spécifier les fonctionnalités au moment de la création  
L’attribut `business_id_number` associé à l’entité juridique d’un compte a été renommé `business_registration_number`.  
2019-02-11
Derniers changements
Plusieurs états de Payment Intent ont été renommés  
---  
Le champ `save_source_to_customer` de l’objet Sources a été renommé `save_payment_method`  
Le champ `allowed_source_types` des `sources` a été renommé `payment_method_types`  
Le champ `next_source_action` des Payment Intents a été renommé `next_action`  
Le champ `authorize_with_url` des Payment Intents a été renommé `redirect_to_url`  
## 2018![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2018-11-08
Derniers changements
Le recouvrement automatique des factures est désormais signalé par le champ `auto_advance`  
---  
Les factures ponctuelles ne collectent plus automatiquement le paiement par défaut  
Remplacement du champ `forgiven` des factures par un nouvel état `uncollectible`  
Un code d’erreur de facture a été renommé `invoice_already_finalized`  
Inclusion de plusieurs changements destinés aux utilisateurs de la version bêta privée de l’API Payment Intents  
2018-10-31
Derniers changements
Les descriptions des clients sont désormais limitées en nombre de caractères  
---  
Les noms des produits sont désormais limités en nombre de caractères  
Les descriptions des sous-postes de facture sont désormais limitées en nombre de caractères.  
Le paramètre `billing_reason` de la première facture d’un abonnement est désormais `subscription_create`  
2018-09-24
Derniers changements
L’objet `FileUpload` a été renommé `Files`, et nécessite désormais des clés secrètes pour le téléchargement des fichiers  
---  
2018-09-06
Derniers changements
Les valeurs des unités de gestion des stocks n’ont plus besoin d’être uniques  
---  
2018-08-23
Derniers changements
La période de fin d’un abonnement ne peut plus être configurée lors de son annulation  
---  
Les clients fournissent désormais un objet `tax_info` avec leurs données d’identification fiscale  
Le champ `amount` des niveaux de tarification a été renommé `unit_amount`  
2018-07-27
Derniers changements
Les abonnements ne prennent plus en charge la modification directe du paramètre `source`  
---  
L’horodatage de la requête API est désormais utilisé pour mettre fin à la période d’essai d’un abonnement  
Les bons de réduction utilisent désormais des valeurs décimales plutôt que des valeurs entières pour spécifier l’attribut `percent_off`  
Stripe valide désormais les adresses e-mail lors de la création ou modification de clients  
2018-05-21
Derniers changements
Les produits n’intègrent plus de listes d’unités de gestion des stocks  
---  
Les postes de facture disposent désormais d’ID uniques et ne peuvent pas être utilisés à la place d’un abonnement  
Certains caractères ne sont désormais plus valides pour les identifiants des bons de réduction, des unités de gestion des stocks, des clients, des produits et des offres.  
Les abonnements ne définissent plus par défaut la période d’essai en fonction d’une offre  
Le passage d’un abonnement à une nouvelle offre avec période d’essai entraîne désormais une prolongation de la période d’essai  
2018-02-28
Derniers changements
La modification d’un abonnement résilié à une date ultérieure n’efface plus son état  
---  
2018-02-06
Derniers changements
Les sources fournissent désormais une valeur `recommended` lorsque l’émetteur conseille d’utiliser 3D Secure  
---  
2018-02-05
Derniers changements
Les offres gratuites avec prorata produisent désormais des factures à montant nul  
---  
Possibilité d’établir la première facture complète d’un abonnement à une date ultérieure (et, de manière facultative, d’inclure un essai gratuit)  
Les objets Plan sont désormais liés à des produits précis, et plusieurs champs ont été déplacés vers la ressource produit  
Les objets Product nécessitent désormais un champ `type`, pour différencier leur utilisation des commandes d’unités de gestion des stocks ou des abonnements et offres  
2018-01-23
Derniers changements
Les plateformes Connect peuvent identifier les cartes ou comptes bancaires utilisés sur l’ensemble des comptes connectés puisqu’ils partagent désormais la même empreinte d’identification.  
---  
## 2017![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2017-12-14
Derniers changements
Les sous-postes de facture doivent désormais obligatoirement comporter un champ `description`  
---  
Les échecs de paiement de factures renvoient désormais une erreur `card_error` lorsque le paiement est refusé  
2017-08-15
Derniers changements
Les sources peuvent désormais spécifier qu’une redirection d’authentification n’est pas nécessaire  
---  
2017-06-05
Derniers changements
Les comptes peuvent désormais spécifier la raison pour laquelle un compte n’est pas activé avec le nouveau motif `under_review`  
---  
2017-05-25
Derniers changements
Les événements Connect spécifient désormais le compte connecté d’origine à l’aide du champ `account`  
---  
Le champ `request` de l’objet `Events` spécifie désormais à la fois l’ID et la clé d’idempotence de la requête  
Les événements comportant le champ `previous_attributes` affichent désormais l’intégralité du sous-tableau concerné  
Les comptes doivent désormais spécifier l’un des trois types (Standard, Express ou Custom)  
2017-04-06
Derniers changements
Les transferts sont désormais répartis entre virements et transferts  
---  
2017-02-14
Derniers changements
Les paiements spécifient désormais l’ID de la règle bloquant une transaction, qui peut être développé  
---  
Les paiements spécifient désormais l’ID du litige associé à une transaction, qui peut être développé  
2017-01-27
Derniers changements
Les opérations sur solde ne comprennent plus le champ `sourced_transfers`  
---  
## 2016![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2016-10-19
Derniers changements
Lorsque des autorisations insuffisantes sont utilisées pour effectuer des requêtes à l’API, une erreur HTTP 403 est désormais générée  
---  
2016-07-06
Derniers changements
Listes filtrées des abonnements par abonnement résilié  
---  
2016-06-15
Derniers changements
La désactivation d’un produit ne désactive plus automatiquement ses unités de gestion des stocks  
---  
2016-03-07
Derniers changements
Les devises prises en charge sont définies dans la spécification du pays d’un compte  
---  
2016-02-29
Derniers changements
La création ou la mise à jour d’un compte entraîne désormais la validation du code postal de son entité juridique  
---  
2016-02-23
Derniers changements
Les commandes payées ou traitées, puis annulées ou renvoyées, donnent désormais lieu à un remboursement automatique des paiements associés  
---  
2016-02-22
Derniers changements
Désormais, il n’est plus possible d’ajouter plus de 250 postes de facture à une facture.  
---  
2016-02-19
Derniers changements
Le champ `name` des comptes bancaires a été renommé `account_holder_name`  
---  
2016-02-03
Derniers changements
Les comptes n’affichent plus que les sous-champs spécifiques au pays pour le champ `legal_entity`  
---  
## 2015![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2015-10-16
Derniers changements
La création ou la modification de clients doit désormais inclure une offre si un pourcentage de taxe est spécifié.  
---  
2015-10-12
Derniers changements
L’utilisation de paramètres non valides pour créer des cartes ou des comptes bancaires pour les tokens, les sources ou les comptes bancaires externes génère désormais une erreur HTTP 400  
---  
2015-10-01
Derniers changements
Sur les profils d’utilisateur, « bank account information » a été renommé « external accounts »  
---  
Les comptes comprennent désormais un champ `external_accounts`  
2015-09-23
Derniers changements
Désormais, le champ `charge` reflète toujours le dernier paiement associé à une facture  
---  
Les factures ne comportent plus de propriété `payment`  
La liste des paiements inclut désormais les paiements provenant de toutes les sources de financement  
Les paiements ne prennent en charge qu’un `offset` pour la pagination des listes lors du filtrage par source  
2015-09-08
Derniers changements
Les requêtes associées à une limite de taux renvoient désormais une erreur HTTP 429, et elles n’incluent plus le champ `rate_limit`  
---  
2015-09-03
Derniers changements
Les requêtes qui réutilisent les tokens d’idempotence mais modifient les paramètres de requête génèrent désormais une erreur  
---  
2015-08-19
Derniers changements
Les opérations sur solde associées à des remboursements ou des litiges indiquent désormais l’ID correspondant dans le champ `source`.  
---  
2015-08-07
Derniers changements
Stripe s’assure désormais que le champ `tos_acceptance[date]` des comptes est un horodatage valide.  
---  
2015-07-28
Derniers changements
Les transferts qui sont immédiatement traités déclenchent désormais l’événement `balance.available`  
---  
2015-07-13
Derniers changements
Les comptes comprennent désormais un champ `verification[disabled_reason]` qui explique pourquoi ils ne peuvent pas effectuer de transferts ni de paiements  
---  
2015-07-07
Derniers changements
Les transferts envoyés à la banque qui ne sont pas arrivés sont désormais à l’état `in_transit`  
---  
2015-06-15
Derniers changements
Les comptes dont la fréquence des virements est définie manuellement génèrent désormais une erreur  
---  
2015-04-07
Derniers changements
Mise à jour de la méthode de calcul des périodes de clôture pour les sous-postes de facture au prorata  
---  
Modification de l’ordre de tri des `lines` des factures  
2015-03-24
Derniers changements
Par défaut, les bons de réduction ne s’appliquent plus aux postes de facture avec des montants négatifs  
---  
2015-02-18
Derniers changements
Les paiements réussis prennent désormais un état `succeeded`  
---  
Les paiements ont désormais un champ `source` qui accepte une source ou une carte  
Les clients ont désormais un champ `source` qui accepte une source ou une carte, et met à jour les types d’événements associés  
2015-02-16
Derniers changements
Le type d’événement `transfer.canceled` a été renommé `transfer.reversed`  
---  
2015-02-10
Derniers changements
L’état des litiges comprend désormais la valeur `warning_closed`  
---  
Les transferts nécessitent désormais un solde de compte suffisant en mode test pour améliorer la simulation en mode production  
2015-01-26
Derniers changements
Les événements contenant le champ `previous_attributes` n’affichent plus que les différences entre les objets d’une mise à jour de l’autre.  
---  
Les abonnements n’indiquent désormais plus que l’horodatage pour les API ou les échecs de paiement de factures pour le champ `canceled_at`  
2015-01-11
Derniers changements
Les chargements de fichiers décrivent le type de fichier à l’aide d’un champ et d’un format `type` plus simples  
---  
## 2014![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2014-12-22
Derniers changements
Les cartes utilisent désormais les valeurs `unchecked` et `unavailable` pour décrire les vérifications du code CVC et de l’adresse effectuées par les banques émettrices  
---  
Les tokens avec cartes ne contiennent plus le champ `customer`  
2014-12-17
Derniers changements
Introduction du champ `statement_description` et de la logique de la façon dont les paiements, les factures, les offres et les transferts affichent les libellés de relevé bancaire.  
---  
La création de comptes à l’aide de l’API nécessite la version 2014-12-17 ou plus récente  
2014-12-08
Derniers changements
Les litiges comprennent désormais un objet `evidence_details` pour la documentation des preuves  
---  
2014-11-20
Derniers changements
Les litiges sont désormais signalés comme `won` même quand le paiement est remboursé  
---  
Les postes de factures indiquent désormais les métadonnées de l’abonnement associé, plutôt que de l’offre associée  
2014-11-05
Derniers changements
Modifications des conditions d’état d’activation des comptes pour les paiements et transferts  
---  
2014-10-07
Derniers changements
Il n’est plus possible de récupérer des tokens avec des clés publiables  
---  
Lorsqu’une carte bancaire ou un compte bancaire est créé(e) avec une clé publiable, les empreintes d’identification ne sont pas incluses dans les réponses de l’API  
2014-09-08
Derniers changements
Les comptes bancaires comprennent désormais une énumération `status` qui remplace plusieurs champs  
---  
2014-08-20
Derniers changements
Les litiges ont désormais plusieurs nouveaux états possibles  
---  
Les litiges incluent désormais plusieurs transactions sur solde  
2014-08-04
Derniers changements
Vous pouvez désormais récupérer l’historique des soldes sans dépendre des champs `Transfer`  
---  
2014-07-26
Derniers changements
Les commissions de plateforme incluent désormais une sous-liste de remboursements dans le champ refunds `refunds`  
---  
2014-07-22
Derniers changements
Les sous-postes de facture comprennent désormais les offres d’abonnement et les quantités  
---  
2014-06-17
Derniers changements
Les factures contiennent désormais une sous-liste des remboursements dans le champ `refunds`  
---  
2014-06-13
Derniers changements
Le champ `type` des cartes bancaires a été renommé `brand`  
---  
2014-05-19
Derniers changements
Remplacement du champ `account` des transferts  
---  
2014-03-28
Derniers changements
Les listes ne contiennent plus le champ `count`  
---  
2014-03-13
Derniers changements
Renomme le champ libellé de relevé bancaire  
---  
2014-01-31
Derniers changements
Les objets Customer prennent désormais en charge les abonnements multiples  
---  
Les dates de fin de période d’essai ne sont plus calculées pour les abonnements annulés  
## 2013![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2013-12-03
Derniers changements
Les commissions de plateforme disposent désormais d’un champ `account` pouvant être développé pour obtenir des informations concernant l’utilisateur  
---  
Les remboursements des commissions de plateforme sont désormais proportionnels au montant débité  
2013-10-29
Derniers changements
Les bons de réduction s’appliquent uniquement au solde total d’une facture, et plus aux factures nulles  
---  
2013-08-13
Derniers changements
Les détails des frais ne sont plus affichés dans les paiements, mais dans les opérations sur solde correspondantes  
---  
Les détails des frais ne sont plus affichés dans les virements, mais dans les opérations sur solde correspondantes  
2013-08-12
Derniers changements
Autorise des champs `description` et `email` vides pour plusieurs objets  
---  
2013-07-05
Derniers changements
Les objets Customer comprennent désormais une sous-liste `cards` et un champ `default_card`  
---  
2013-02-13
Derniers changements
Les contestations de paiement sont désormais suivies par l’intermédiaire du champ `stripe_fee` et incluses dans le total des frais  
---  
2013-02-11
Derniers changements
Les paiements de facture en échec renvoient désormais une erreur HTTP  
---  
## 2012![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2012-11-07
Derniers changements
Le champ `disputed` des paiements a été renommé `dispute`  
---  
2012-10-26
Derniers changements
Les factures comprennent désormais une liste des sous-postes de facture  
---  
2012-09-24
Derniers changements
Les réductions ne comportent plus de champ `id` superflu  
---  
2012-07-09
Derniers changements
Les objets Customer n’incluent plus le champ `uncaptured`  
---  
2012-06-18
Derniers changements
Les tokens n’incluent plus les propriétés `amount` et `currency`  
---  
2012-03-25
Derniers changements
Les objets Customer n’incluent plus de champ `next_recurring_charge`  
---  
2012-02-23
Derniers changements
Les champs comportant des valeurs nulles sont désormais inclus dans les réponses de l’API  
---  
## 2011![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
2011-09-15
Derniers changements
Les cartes sont validées différemment lors de la création de tokens  
---  
2011-08-01
Derniers changements
Les objets List fournissent désormais un décompte total des postes et un champ `data`  
---  
2011-06-28
Derniers changements
Les offres ne contiennent plus de champ `identifier`  
---  
2011-06-21
Derniers changements
Les erreurs produisent désormais des exceptions pour les paramètres d’API non reconnus  
---  
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

