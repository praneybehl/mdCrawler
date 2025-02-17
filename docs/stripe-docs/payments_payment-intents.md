Accéder directement au contenu
API Payment Intents
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
AperçuDécouvrir tous les produitsPhases de publication
Planifier votre intégration
Configurer Stripe
Créer un compte
Accepter un paiement
Produits et tarifs
Utiliser Stripe sans coder
Aide en matière de réglementation
Dashboard Stripe
Dashboard Web
Dashboard mobile
Pour les développeurs
Commencer le développement
Exemples de projets
À propos des API
Visite guidée de l'API
API Payment Intents
Fonctionnement des PaymentIntents
Mises à jour de l'état des paiements
Capture asynchrone
Comparer à Charges
API Setup Intents
Moyens de paiement
API plus anciennes


Migrer vers Stripe
Migrer les données client
Migrer des données de paiement
Migrer des abonnements
Gérer le risque de fraude
Comprendre la fraude
Radar pour la protection contre la fraude
Gestion des litiges
Vérifier l'identité
Canada
Français (France)
AccueilDémarrerAbout the APIs
# API Payment Intents
## Découvrez comment utiliser l'API Payment Intents pour les paiements Stripe.
Utilisez l’API Payment Intents pour créer une intégration capable de gérer des tunnels de paiement complexes dont l’état change au cours du cycle de vie du PaymentIntent. Il suit un paiement de sa création jusqu’à son paiement et déclenche des étapes d’authentification supplémentaires si nécessaire.
L’API Payment Intents offre notamment les avantages suivants :
  * Gestion de l’authentification automatique
  * Aucun paiement en double
  * Aucun problème relatif à la clé d’idempotence
  * Prise en charge de l’authentification forte du client (SCA) et autres changements réglementaires


## Un ensemble complet d’API![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Utilisez l’API Payment Intents avec les API Setup Intents et Payment Methods. Ces API vous permettent de gérer des paiements dynamiques (notamment avec une authentification supplémentaire de type 3D Secure) et facilitent votre développement à l’international grâce à la prise en charge de nouvelles réglementations et de moyens de paiements locaux.
L’élaboration d’une intégration avec l’API Payment Intents implique deux actions : la création et la confirmation d’un PaymentIntent. Normalement, chaque PaymentIntent est associé au panier ou à une session du client dans votre application. Le PaymentIntent renferme des informations sur la transaction, comme les moyens de paiement pris en charge, le montant à encaisser et la devise souhaitée pour le paiement.
## Créer un PaymentIntent![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Pour commencer, consultez le guide d’acceptation des paiements. Il décrit comment créer un PaymentIntent sur le serveur et transmettre sa clé secrète côté client, pour éviter de transmettre l’objet PaymentIntent dans son intégralité.
Lorsque vous créez le PaymentIntent, vous pouvez choisir certains éléments comme le montant et la devise :
Command Line
cURL
```

curlhttps://api.stripe.com/v1/payment_intents \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -damount=1099 \
 -dcurrency=usd

```

### Bonnes pratiques![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Nous vous recommandons de créer un PaymentIntent dès que le montant est connu, par exemple lorsque le client commence le processus de paiement afin de faciliter le suivi de votre tunnel d’achat. Si nécessaire, vous pourrez mettre à jour le montant du PaymentIntent si celui-ci vient à évoluer. Par exemple, si le client revient en arrière pour ajouter de nouveaux articles au panier, le montant devra être mis à jour lorsque le client recommence le processus de paiement.
  * Si le client interrompt le processus de paiement et le reprend plus tard, essayez d’utiliser le même PaymentIntent au lieu d’en créer un nouveau. Chaque PaymentIntent dispose d’un ID unique que vous pouvez utiliser pour le récupérer si nécessaire. Le modèle de données de votre application vous permet de conserver l’ID du PaymentIntent dans le panier ou la session du client afin de pouvoir le récupérer plus facilement. Si vous réutilisez le même PaymentIntent, l’état de l’objet vous aide à effectuer le suivi des tentatives de paiement échouées pour une session ou un panier donné.
  * N’oubliez pas de fournir une clé d’idempotence afin d’éviter de créer deux PaymentIntents pour le même achat. Cette clé est généralement basée sur l’ID associé au panier ou à la session du client dans votre application.


## Transmettre la clé secrète du client côté client![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
PaymentIntent contient la clé secrète du client, qui est une clé unique associée à un PaymentIntent donné. Côté client dans votre application, la clé secrète est utilisée par Stripe.js comme paramètre pour appeler des fonctions (comme stripe.confirmCardPayment ou stripe.handleCardAction) pour finaliser le paiement.
### Récupérer la clé secrète du client![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Le PaymentIntent contient une clé secrète à utiliser côté client pour finaliser le processus de paiement en toute sécurité. Vous pouvez adopter différentes approches pour transmettre cette clé secrète côté client.
Application monopage
Rendu côté serveur
Récupérez la clé secrète du client à partir d’un endpoint sur votre serveur, à l’aide de la fonction `fetch` du navigateur. Cette approche est recommandée si votre côté client est une application d’une seule page, en particulier si elle repose sur un framework front-end moderne tel que React. Créez l’endpoint de serveur qui gère la clé secrète du client :
main.rb
Ruby
```

get '/secret'do
 intent =# ... Create or retrieve the PaymentIntent{client_secret: intent.client_secret}.to_json
end

```

Récupérez ensuite la clé secrète du client à l’aide JavaScript côté client :
```

(async()=>{const response =awaitfetch('/secret');const{client_secret: clientSecret}=await response.json();// Render the form using the clientSecret})();

```

#### Mise en garde
Vous pouvez utiliser la clé secrète du client pour finaliser le processus de paiement avec le montant spécifié dans le PaymentIntent. Vous ne devez pas l’enregistrer, l’intégrer à une URL ni la dévoiler à d’autres personnes que le client. Veillez à ce que le protocole TLS soit inclus sur toutes les pages qui contiennent la clé secrète du client.
## Après le paiement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Une fois que le client a confirmé le paiement, nous vous recommandons de surveiller les webhooks côté serveur afin de détecter si le paiement aboutit ou échoue.
Un objet `PaymentIntent` peut être associé à plusieurs objets Charge s’il y a eu plusieurs tentatives de paiement, par exemple des relances. Pour chaque paiement, vous pouvez vérifier le résultat et les détails du moyen de paiement utilisé.
## Optimiser les moyens de paiement pour les paiements futurs![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Le paramètre setup_future_usage enregistre les moyens de paiement en vue de leur réutilisation. Pour les cartes, il optimise également les taux d’autorisation conformément à la législation régionale et aux règles des réseaux, comme la SCA. Pour choisir la valeur à utiliser, prenez en compte l’utilisation que vous comptez faire du moyen de paiement.
Utilisation prévue du moyen de paiement| Valeur d’énumération setup_future_usage à utiliser  
---|---  
Paiements effectués pendant une session uniquement| `on_session`  
Paiements effectués hors session uniquement| `off_session`  
Paiements effectués pendant une session et hors session| `off_session`  
Vous pouvez accepter des paiements hors session avec une carte bancaire configurée pour payer pendant une session, mais il est probable que la banque refuse le paiement hors session et requiert l’authentification du titulaire de la carte.
L’exemple suivant montre la marche à suivre pour créer un PaymentIntent et indiquer `setup_future_usage` :
Command Line
cURL
```

curlhttps://api.stripe.com/v1/payment_intents \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -damount=1099 \
 -dcurrency=usd \
 -dsetup_future_usage=off_session

```

#### Mise en garde
Les configurations destinées à prendre en charge les paiements hors session sont plus susceptibles d’entraîner des frictions supplémentaires. Utilisez la configuration en session si vous n’avez pas l’intention d’accepter les paiements hors session avec la carte enregistrée.
## Libellé de relevé bancaire dynamique![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Par défaut, le libellé de votre compte Stripe apparaît sur les relevés de vos clients chaque fois que vous débitez leur carte. Pour afficher un libellé différent pour un paiement donné, incluez le paramètre `statement_descriptor`.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/payment_intents \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -damount=1099 \
 -dcurrency=usd \
 -d"payment_method_types[]"=card \
 -dstatement_descriptor="Custom descriptor"

```

Les libellés de relevé bancaire sont limités à 22 caractères, ne peuvent pas contenir les caractères spéciaux `<`, `>`, `'`, `"`, ni `*` et ne doivent pas être constitués uniquement de chiffres. Lorsque vous utilisez des libellés dynamiques, le texte dynamique est ajouté au préfixe du libellé défini dans le Dashboard Stripe. Un astérisque (`*`) et une espace sont également ajoutés pour séparer la partie par défaut de la partie dynamique du libellé. Ces deux caractères sont décomptés des 22 caractères disponibles.
## Stocker des informations sous forme de métadonnées![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
Stripe vous permet d’ajouter des métadonnées à vos requêtes les plus courantes, notamment au traitement des paiements. Les métadonnées ne sont pas visibles pour vos clients et n’influent aucunement sur un éventuel refus de paiement ou un blocage par notre système de prévention des fraudes.
Grâce aux métadonnées, vous pouvez associer d’autres informations pertinentes à l’activité de Stripe.
Toutes les métadonnées que vous incluez sont visibles dans le Dashboard (par exemple, lorsque vous consultez la page d’un paiement donné) et disponibles dans les rapports les plus courants. Vous pouvez par exemple associer l’ID de commande de votre boutique au PaymentIntent utilisé pour régler cette commande, ce qui facilite le rapprochement des paiements dans Stripe et des commandes dans votre système.
Si vous utilisez Radar for Fraud Teams, il peut être judicieux de transmettre toutes les informations supplémentaires concernant vos clients et leurs commandes en tant que métadonnées. Ensuite, vous pouvez définir des règles Radar basées sur des attributs de métadonnées et disposer de davantage d’informations sur les paiements dans le Dashboard, ce qui peut accélérer votre processus d’examen.
Lorsqu’un PaymentIntent crée un paiement, le PaymentIntent copie ses métadonnées dans le paiement. Les modifications ultérieures apportées aux métadonnées du PaymentIntent ne modifieront pas les métadonnées des paiements précédemment créés par le PaymentIntent.
Command Line
cURL
```

curlhttps://api.stripe.com/v1/payment_intents \
 -u"
sk_test_Hrs6SAopgFPF0bZXSN3f6ELN
:" \
 -damount=1099 \
 -dcurrency=usd \
 -d"payment_method_types[]"=card \
 -d"metadata[order_id]"=6735

```

#### Mise en garde
Veillez à ne pas stocker d’informations confidentielles (informations permettant une identification personnelle, données de carte bancaire, etc.) sous forme de métadonnées ou dans le paramètre `description` du PaymentIntent.
## Voir aussi![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)
  * Accepter un paiement en ligne
  * Accepter un paiement dans une application iOS
  * Accepter un paiement dans une application Android
  * Configurer des paiements futurs


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
Un ensemble complet d’API
Créer un PaymentIntent
Bonnes pratiques
Transmettre la clé secrète du client côté client
Récupérer la clé secrète du client
Après le paiement
Optimiser les moyens de paiement pour les paiements futurs
Libellé de relevé bancaire dynamique
Stocker des informations sous forme de métadonnées
Voir aussi
Guides connexes
Fonctionnement des PaymentIntents
Produits utilisés
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

