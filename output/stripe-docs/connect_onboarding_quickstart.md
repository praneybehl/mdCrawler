Accéder directement au contenu
Guide de démarrage rapide sur l'inscription des utilisateurs
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
Fonctionnement de Connect
Concevoir une intégration
Migrer vers les propriétés du contrôleur de comptes
Prochaines modifications des exigences
Guide de démarrage rapide sur l'inscription des utilisateurs


Principes de base de l'intégration
Exemples d'intégration
Inscrire des comptes
Configurer les dashboards des comptes
Accepter des paiements
Effectuer des virements vers des comptes
Gérer votre plateforme Connect
Formulaires fiscaux pour votre plateforme Connect
Utiliser les types de comptes connectés
Intégration avec Accounts v2
Canada
Français (France)
Cette page est optimisée pour les écrans plus larges.Vous préférez peut-être la version texte de ce guide.
Front-end :
React
Next.js
Vue.js
HTML
ReactNext.jsVue.jsHTML
Back-end :
Ruby
Node
Python
Go
Java
.NET
PHP
RubyNodePythonGoJava.NETPHP
# Inscrire des comptes à votre plateforme Connect
Affichez le guide en version texte.
Créez un compte connecté et collectez ses informations pour activer les paiements. Nous vous recommandons de sélectionner les propriétés avant de télécharger un exemple d’application, car votre intégration changera de manière significative.
Télécharger l'application complète
Vous ne codez pas ? Utilisez les options no-code de Stripe ou contactez nos partenaires pour obtenir de l'aide.
1Sélectionner les propriétés
### Présentation
settings
Votre intégration à Connect change de manière significative en fonction de la façon dont vous créez vos comptes connectés. Nous avons personnalisé les propriétés du compte connecté en fonction de vos choix lors de l’inscription de votre compte de plateforme à Connect. Les changements effectués ici ne mettent pas à jour les paramètres de votre plateforme et ne sont pas reflétés dans le Dashboard Stripe.
See Design an integration to learn more about making these choices.
Serveur
### Choisir comment vos comptes connectés s’inscrivent à Stripe
settings
Le choix de la méthode d’inscription des utilisateurs a une incidence sur la disponibilité des autres options de compte ci-dessous.
Inscription des utilisateurs :
Hébergé
Intégré
API
Redirigez vos comptes connectés vers l’inscription hébergée par Stripe à l’aide d’un lien de compte.
Serveur
### Choisir où vos comptes connectés gèrent leurs paiements et informations de compte
settings
Accès au Dashboard :
Stripe
Express
Aucun
Donnez à vos comptes connectés l’accès au Dashboard Stripe.
Serveur
### Choisir votre type de paiement
settings
Type de paiement :
Paiements directs
Paiements indirects
Paiements et transferts distincts
Créez des paiements directement sur vos comptes connectés.
Serveur
### Déterminer qui paie les frais
settings
Modèle économique :
Vos comptes connectés
Votre plateforme
Stripe prélève des frais à vos comptes connectés.
Serveur
### Déterminer qui est responsable en cas de solde négatif
settings
Responsabilité des soldes négatifs :
Stripe
Plateforme
Votre plateforme n’est pas responsable des soldes négatifs des comptes. Stripe est responsable de la collecte des informations à jour lorsque les exigences doivent être satisfaites ou évoluent.
Serveur
2Configurer les dépendances
### Installer la bibliothèque Stripe Ruby
settings
Installez la gem Ruby de Stripe et exigez-la dans votre code. Si vous partez de zéro et avez besoin d’un Gemfile, téléchargez les fichiers du projet à l’aide du lien dans l’éditeur de code.
Terminal
Bundler
GitHub
Installez le fichier GEM :
`gem install stripe -v 9.1.0`
Serveur
### Configurez votre clé secrète
settings
Ajoutez votre clé secrète à votre serveur.
Serveur
### Configurez votre clé publique
settings
Ajoutez votre clé publique à un fichier `.env`. React la charge automatiquement dans votre application en tant que variable d’environnement.
Client
### Ajouter l’image de marque de la plateforme
settings
Pour utiliser l’inscription hébergée par Stripe, accédez d’abord à vos paramètres d’inscription et personnalisez votre image de marque. Vous devez définir un nom d’entreprise, une icône et une couleur de marque.
Serveur
3Créer un compte connecté
### Ajouter un endpoint pour mettre en place un compte connecté
settings
Définissez sur votre serveur un endpoint que votre client pourra appeler pour gérer la création d’un compte connecté.
Serveur
### Créer un compte connecté
settings
Create a connected account by calling the Stripe API. We’ve configured the attributes used based on the preferences you’ve selected above. You can prefill verification information, the business profile of the user, and other fields on the account if your platform has already collected it.
Serveur
### Appeler l’endpoint pour créer un compte connecté
settings
Appelez l’endpoint que vous avez ajouté ci-dessus pour créer un compte connecté.
Client
4Inscrire le compte connecté
### Présentation
settings
Per your preference selection, you selected Stripe-hosted onboarding. Your platform redirects your connected accounts to a Stripe-hosted, co-branded onboarding interface using an Account Link.
Serveur
### Créez un endpoint lien de compte
settings
Ajoutez un endpoint sur votre serveur pour créer un lien de compte.
Serveur
### Indiquez une URL de redirection
settings
Une fois que votre compte connecté a terminé le flux d’inscription, il est redirigé vers l’URL de redirection. Cela ne signifie pas que toutes les informations ont été collectées ni que le compte connecté a satisfait toutes ses exigences, mais simplement qu’il est entré dans le flux et en est sorti sans aucun souci particulier.
Serveur
### Indiquer une URL d’actualisation
settings
Stripe redirige votre compte connecté vers l’URL d’actualisation lorsque le lien a expiré, qu’il a déjà été utilisé, que votre plateforme ne peut pas accéder au compte connecté ou que le compte est refusé. Faites en sorte que l’URL d’actualisation crée un nouveau lien de compte d’inscription et y redirige votre utilisateur.
Serveur
### Appeler l’endpoint pour créer un lien de compte
settings
Fournissez l’ID du compte connecté.
Client
### Rediriger l’utilisateur vers l’URL
settings
Redirigez l’utilisateur vers Stripe pour qu’il finalise l’inscription. Une fois l’inscription terminée, il est redirigé vers votre application.
Client
### Gérer le retour du compte connecté
settings
Affichez une page utile au compte connecté lorsqu’il quitte le flux d’inscription hébergé par Stripe.
Client
### Gérer l’actualisation du lien de compte
settings
Appelez votre endpoint pour actualiser le lien de compte au niveau de l’URL d’actualisation.
Client
5Étapes suivantes
### Accepter des paiements
settings
Now that you have onboarded a connected account, continue to create direct charges.
Serveur
Cette page vous a-t-elle été utile ?
OuiNon
server.rb
App.jsx
.env
Refresh.jsx
Return.jsx
Home.jsx
Télécharger
```

require 'sinatra'
require 'stripe'
# This is a placeholder - it should be replaced with your secret API key.
# Sign in to see your own test API key embedded in code samples.
# Don’t submit any personally identifiable information in requests made with this key.
Stripe.api_key = 'sk_INSERT_YOUR_SECRET_KEY'
Stripe.api_version = '2023-10-16'
set :static, true
set :port, 4242
set :public_folder, 'dist'
post '/account_link' do
 content_type 'application/json'
 body = JSON.parse(request.body.read)
 connected_account_id = body["account"]
 begin
  account_link = Stripe::AccountLink.create({
   account: connected_account_id,
   return_url: "http://localhost:4242/return/#{connected_account_id}",
   refresh_url: "http://localhost:4242/refresh/#{connected_account_id}",
   type: "account_onboarding",
  })
  {
   url: account_link.url
  }.to_json
 rescue => error
  puts "An error occurred when calling the Stripe API to create an account link: #{error.message}";
  return [500, { error: error.message }.to_json]
 end
end
post '/account' do
 content_type 'application/json'
 begin
  account = Stripe::Account.create
  {
   account: account[:id]
  }.to_json
 rescue => error
  puts "An error occurred when calling the Stripe API to create an account: #{error.message}";
  return [500, { error: error.message }.to_json]
 end
end
get '/*path' do
 send_file File.join(settings.public_folder, 'index.html')
end
source 'https://rubygems.org/'
gem 'sinatra'
gem 'stripe', '13.4.1'
{
 "name": "client",
 "version": "0.1.0",
 "private": true,
 "dependencies": {
  "react": "^18.2.0",
  "react-dom": "^18.2.0",
  "react-router-dom": "^6.4.0",
  "react-scripts": "^3.4.0",
  "@stripe/connect-js": "3.3.5",
  "@stripe/react-connect-js": "3.3.7"
 },
 "homepage": "http://localhost:3000",
 "proxy": "http://localhost:4242",
 "scripts": {
  "start": "parcel watch",
  "build": "parcel build"
 },
 "source": "public/index.html",
 "eslintConfig": {
  "extends": "react-app"
 },
 "browserslist": {
  "production": [
   ">0.2%",
   "not dead",
   "not op_mini all"
  ],
  "development": [
   "last 1 chrome version",
   "last 1 firefox version",
   "last 1 safari version"
  ]
 },
 "devDependencies": {
  "parcel": "^2.8.3"
 }
}
import React from "react";
import Home from "./Home";
import Refresh from "./Refresh";
import Return from "./Return";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./App.css";
const router = createBrowserRouter([
 {
  path: "/",
  element: <Home />,
 },
 {
  path: "/refresh/:connectedAccountId",
  element: <Refresh />,
 },
 {
  path: "/return/:connectedAccountId",
  element: <Return />,
 },
]);
export default function App() {
 return (
  <div>
   <RouterProvider router={router} />
  </div>
 );
}
* {
 box-sizing: border-box;
}
#root {
 width: 100%;
}
body {
 font-family: -apple-system, BlinkMacSystemFont, sans-serif;
 -webkit-font-smoothing: antialiased;
 margin: 0;
}
h2 {
 margin-bottom: 0;
 font-size: 20px;
}
p {
 margin: 0;
 color: #687385;
 padding: 8px 0;
}
.container {
 display: flex;
 flex-direction: column;
 align-items: center;
}
.content {
 display: flex;
 justify-content: center;
 align-items: center;
 flex-direction: column;
 text-align: center;
 width: 420px;
 padding-top: 40px;
 margin-bottom: 110px;
}
.banner {
 width: 100vw;
 height: 64px;
 display: flex;
 flex-direction: column;
 justify-content: center;
 align-items: center;
 background-color: #635BFF;
 color: #ffffff;
}
.banner h2 {
 margin-bottom: 18px;
 margin-top: 18px;
}
.info-callout {
 position: fixed;
 bottom: 40px;
 border-radius: 4px;
 box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.12), 0px 15px 35px 0px rgba(48, 49, 61, 0.08);
 padding: 9px 12px;
 background-color: #ffffff;
}
.dev-callout {
 position: fixed;
 bottom: 110px;
 border-radius: 4px;
 box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.12), 0px 15px 35px 0px rgba(48, 49, 61, 0.08);
 padding: 9px 12px;
 background-color: #ffffff;
}
.bold {
 font-weight: 700;
 font-size: 14px;
}
.error {
 font-weight: 400;
 color: #E61947;
 font-size: 14px;
}
.divider {
 width: 100%;
 height: 1px;
 margin: 24px 24px;
 border-top: 1px solid #D8DEE4;
}
button {
 font-family: -apple-system, BlinkMacSystemFont, sans-serif;
 font-size: 16px;
 font-weight: 600;
 border: 1px solid gray;
 border-radius: 4px;
 margin-top: 32px;
 padding-top: 10px;
 padding-bottom: 10px;
 background-color: #635BFF;
 color: #ffffff;
 width: 420px;
}
button:hover {
 border-color: black;
}
# https://dashboard.stripe.com/apikeys
# Replace this placeholder with your publishable key from https://dashboard.stripe.com/test/apikeys
REACT_APP_STRIPE_PUBLISHABLE_KEY=pk_INSERT_YOUR_PUBLISHABLE_KEY
import React, { useState } from "react";
import { useParams} from 'react-router-dom';
export default function Refresh() {
 const {connectedAccountId} = useParams();
 const [accountLinkCreatePending, setAccountLinkCreatePending] = useState(false);
 const [error, setError] = useState(false);
 React.useEffect(() => {
  if (connectedAccountId) {
   setAccountLinkCreatePending(true);
    fetch("/account_link", {
    method: "POST",
    headers: {
     "Content-Type": "application/json",
    },
    body: JSON.stringify({
     account: connectedAccountId,
    }),
   })
    .then((response) => response.json())
    .then((json) => {
     setAccountLinkCreatePending(false);
     const { url, error } = json;
     if (url) {
      window.location.href = url;
     }
     if (error) {
      setError(true);
     }
    });
  }
 }, [connectedAccountId])
 return (
  <div className="container">
   <div className="banner">
    <h2>Rocket Rides</h2>
   </div>
   <div className="content">
    <h2>Add information to start accepting money</h2>
    <p>Rocket Rides is the world's leading air travel platform: join our team of pilots to help people travel faster.</p>
    {error && <p className="error">Something went wrong!</p>}
   </div>
   <div className="dev-callout">
    {connectedAccountId && <p>Your connected account ID is: <code className="bold">{connectedAccountId}</code></p>}
    {accountLinkCreatePending && <p>Creating a new Account Link...</p>}
   </div>
  </div>
 );
}
import React from "react";
import { useParams} from 'react-router-dom';
export default function Return() {
 const {connectedAccountId} = useParams();
 return (
  <div className="container">
   <div className="banner">
    <h2>Rocket Rides</h2>
   </div>
   <div className="content">
    <h2>Details submitted</h2>
    <p>That's everything we need for now</p>
   </div>
   <div className="info-callout">
    <p>
    This is a sample app for Stripe-hosted Connect onboarding. <a href="https://docs.stripe.com/connect/onboarding/quickstart?connect-onboarding-surface=hosted" target="_blank" rel="noopener noreferrer">View docs</a>
    </p>
   </div>
  </div>
 );
}
import React, { useState } from "react";
export default function Home() {
 const [accountCreatePending, setAccountCreatePending] = useState(false);
 const [accountLinkCreatePending, setAccountLinkCreatePending] = useState(false);
 const [error, setError] = useState(false);
 const [connectedAccountId, setConnectedAccountId] = useState();
 return (
  <div className="container">
   <div className="banner">
    <h2>Rocket Rides</h2>
   </div>
   <div className="content">
    {!connectedAccountId && <h2>Get ready for take off</h2>}
    {!connectedAccountId && <p>Rocket Rides is the world's leading air travel platform: join our team of pilots to help people travel faster.</p>}
    {connectedAccountId && <h2>Add information to start accepting money</h2>}
    {connectedAccountId && <p>Matt's Mats partners with Stripe to help you receive payments and keep your personal bank and details secure.</p>}
    {!accountCreatePending && !connectedAccountId && (
     <button
      onClick={async () => {
       setAccountCreatePending(true);
       setError(false);
       fetch("/account", {
        method: "POST",
       })
        .then((response) => response.json())
        .then((json) => {
         setAccountCreatePending(false);
         const { account, error } = json;
         if (account) {
          setConnectedAccountId(account);
         }
         if (error) {
          setError(true);
         }
        });
      }}
     >
      Create an account!
     </button>
    )}
    {connectedAccountId && !accountLinkCreatePending && (
     <button
      onClick={async () => {
       setAccountLinkCreatePending(true);
       setError(false);
       fetch("/account_link", {
        method: "POST",
        headers: {
         "Content-Type": "application/json",
        },
        body: JSON.stringify({
         account: connectedAccountId,
        }),
       })
        .then((response) => response.json())
        .then((json) => {
         setAccountLinkCreatePending(false);
         const { url, error } = json;
         if (url) {
          window.location.href = url;
         }
         if (error) {
          setError(true);
         }
        });
      }}
     >
      Add information
     </button>
    )}
    {error && <p className="error">Something went wrong!</p>}
    {(connectedAccountId || accountCreatePending || accountLinkCreatePending) && (
     <div className="dev-callout">
      {connectedAccountId && <p>Your connected account ID is: <code className="bold">{connectedAccountId}</code></p>}
      {accountCreatePending && <p>Creating a connected account...</p>}
      {accountLinkCreatePending && <p>Creating a new Account Link...</p>}
     </div>
    )}
    <div className="info-callout">
     <p>
     This is a sample app for Stripe-hosted Connect onboarding. <a href="https://docs.stripe.com/connect/onboarding/quickstart?connect-onboarding-surface=hosted" target="_blank" rel="noopener noreferrer">View docs</a>
     </p>
    </div>
   </div>
  </div>
 );
}
import React from "react";
import {createRoot} from "react-dom/client";
import App from "./App";
const root = createRoot(document.getElementById("root"))
root.render(<App />);
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#000000" />
  <meta
   name="description"
   content="A demo of Stripe Connect embedded components"
  />
  <title>Stripe Connect</title>
 </head>
 <body>
  <noscript>You need to enable JavaScript to run this app.</noscript>
  <div id="root"></div>
  <script type="module" src="../src/index.js" defer></script>
  <!--
   This HTML file is a template.
   If you open it directly in the browser, you will see an empty page.
   You can add webfonts, meta tags, or analytics to this file.
   The build step will place the bundled scripts into the <body> tag.
   To begin the development, run `npm start` or `yarn start`.
   To create a production bundle, use `npm run build` or `yarn build`.
  -->
 </body>
</html>
# Onboard accounts to your Connect platform
Build a Connect integration which creates an account and onboards it to your platform.
Here are some basic scripts you can use to build and run the application.
## Set your Stripe API keys
Ensure that you have replaced the following placeholders in the downloaded code sample:
- sk_INSERT_YOUR_SECRET_KEY
To get Stripe API keys, sign up for a Stripe account at https://dashboard.stripe.com/register
## Run the sample
1. Build the server
~~~
bundle install
~~~
2. Run the server
~~~
ruby server.rb -o 0.0.0.0
~~~
3. Build the client app
~~~
npm install
~~~
4. Run the client app
~~~
npm start
~~~
5. Go to [http://localhost:4242](http://localhost:4242)

```

Copier
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

