Accéder directement au contenu
Démarrage rapide
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
Démarrer avec les composants intégrés Connect
Démarrage rapide
Composants intégrés Connect pris en charge
Personnaliser les composants intégrés Connect
Personnalisation du Dashboard Stripe
Contrôles de la plateforme pour les comptes du Dashboard Stripe
Dashboard Express


Accepter des paiements
Effectuer des virements vers des comptes
Gérer votre plateforme Connect
Formulaires fiscaux pour votre plateforme Connect
Utiliser les types de comptes connectés
Intégration avec Accounts v2
Canada
Français (France)
#### Remarque
Cette page n'est pas encore disponible dans cette langue. Nous faisons tout notre possible pour proposer notre documentation dans davantage de langues et nous vous fournirons la version traduite dès qu'elle sera disponible.
Cette page est optimisée pour les écrans plus larges.Vous préférez peut-être la version texte de ce guide.
Front-end :
HTML
React
Next.js
Vue.js
HTMLReactNext.jsVue.js
Back-end :
Ruby
Node
PHP
Python
Go
.NET
Java
RubyNodePHPPythonGo.NETJava
# Integrate with Connect embedded components 
Affichez le guide en version texte.
#### Remarque
To create an account session, you can use the Stripe SDKs:
  * Ruby `>=13.4.1`
  * Python `>=11.5.0`
  * PHP `>=16.5.0`
  * Node `>=17.6.0`
  * .NET `>=47.3.0`
  * Java `>=28.3.0`
  * Go `>=81.3.0`


Build a full, working integration using Connect embedded components. Use Connect embedded components to add connected account dashboard functionality to your website in minutes. These libraries and their supporting API help you to get up and running with almost no code, giving your users access to Stripe products directly in your dashboard.
Télécharger l'application complète
Vous ne codez pas ? Utilisez les options no-code de Stripe ou contactez nos partenaires pour obtenir de l'aide.
1Set up the server
### Install the Stripe Ruby library
settings
Install the Stripe Ruby gem and require it in your code. Alternatively, if you’re starting from scratch and need a Gemfile, download the project files using the link in the code editor.
Terminal
Bundler
GitHub
Install the gem:
`gem install stripe -v 13.4.1`
Serveur
### Create an endpoint on your server
settings
Add a new endpoint on your server for your client to call.
Serveur
### Delegate API access to your connected account
settings
To make requests on behalf of your connected account, pass the connected account ID to the AccountSessions API.
Serveur
### Enable specific embedded components for your connected accounts
settings
Specify the embedded components you want to enable for your connected accounts. For the full list of supported embedded components, see Get started with Connect embedded components.
Serveur
### Create an AccountSession
settings
Call the `v1/account_sessions` API from your endpoint to create a new AccountSession.
Serveur
### Return the client secret
settings
Return the `client_secret` property from the AccountSession in the response.
Serveur
2Initialize Connect.js on the client
### Load the Connect.js script
settings
Import the @stripe/connect-js module and call `loadConnectAndInitialize(initParams)` to load the code necessary to connect your client to Stripe. Connect.js loads synchronously and returns a `StripeConnectInstance` to the client.
npm
GitHub
Install the library:
`npm install --save @stripe/connect-js`
Client
### Initialize Connect.js
settings
`loadConnectAndInitialize(initParams)` returns a StripeConnectInstance object, which is used to create a StripeConnectInstance. Initialize the StripeConnectInstance by passing in your publishable key and the `fetchClientSecret` function to fetch a client secret.
Client
### Include Connect embedded components
settings
Add Connect embedded components to the DOM. After initialization, the StripeConnectInstance handles making requests to Stripe and updating the UI of the web components. You can mount or unmount these elements from the DOM at any time and make the inner elements fit seamlessly within your page by wrapping them with your own HTML.
After a successful initialization, StripeConnectInstance manages the context for all the Connect embedded components in your application and uses that client secret and publishable key to contact Stripe.
Client
### Optional: Style Connect embedded components
settings
Customize the appearance of Connect embedded components by passing an `appearance` configuration to StripeConnect upon initialization. Connect embedded components already inherit the font-family of the parent HTML element, but you can make them match with the rest of your application by passing your company’s color scheme.
Client
Cette page vous a-t-elle été utile ?
OuiNon
server.rb
index.html
index.js
Télécharger
```

require 'sinatra'
require 'stripe'
# This is a placeholder - it should be replaced with your secret API key.
# Sign in to see your own test API key embedded in code samples.
# Don’t submit any personally identifiable information in requests made with this key.
Stripe.api_key = 'sk_INSERT_YOUR_SECRET_KEY'
set :static, true
set :port, 4242
set :public_folder, 'dist'
post '/account_session' do
 content_type 'application/json'
 begin
  account_session = Stripe::AccountSession.create({
   account: "{{CONNECTED_ACCOUNT_ID}}",
   components: {
    payments: {
     enabled: true,
     features: {
      refund_management: true,
      dispute_management: true,
      capture_payments: true
     }
    }
   }
  })
  {
   client_secret: account_session[:client_secret]
  }.to_json
 rescue => error
  puts "An error occurred when calling the Stripe API to create an account session: #{error.message}";
  return [500, { error: error.message }.to_json]
 end
end
get '/' do
 send_file File.join(settings.public_folder, 'index.html')
end
source 'https://rubygems.org/'
gem 'sinatra'
gem 'stripe', '13.4.1'
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8" />
  <title>Connect embedded components</title>
  <meta
   name="description"
   content="A demo of Stripe Connect embedded components"
  />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" href="index.css" />
  <script type="module" src="index.js" defer></script>
 </head>
 <body>
  <div id="container"></div>
  <div id="error" hidden>Something went wrong!</div>
 </body>
</html>
import { loadConnectAndInitialize } from "@stripe/connect-js";
const fetchClientSecret = async () => {
 // Fetch the AccountSession client secret
 const response = await fetch('/account_session', { method: "POST" });
 if (!response.ok) {
  // Handle errors on the client side here
  const {error} = await response.json();
  console.log('An error occurred: ', error);
  document.querySelector('#container').setAttribute('hidden', '');
  document.querySelector('#error').removeAttribute('hidden');
  return undefined;
 } else {
  const {client_secret: clientSecret} = await response.json();
  document.querySelector('#container').removeAttribute('hidden');
  document.querySelector('#error').setAttribute('hidden', '');
  return clientSecret;
 }
}
 const instance = loadConnectAndInitialize({
  // This is a placeholder - it should be replaced with your publishable API key.
  // Sign in to see your own test API key embedded in code samples.
  // Don’t submit any personally identifiable information in requests made with this key.
  publishableKey: "pk_INSERT_YOUR_PUBLISHABLE_KEY",
  fetchClientSecret: fetchClientSecret,
  appearance: {
   overlays: 'dialog',
   variables: {
    colorPrimary: '#625afa',
   },
  },
   });
   const container = document.getElementById("container");
   const paymentsComponent = instance.create("payments");
   container.appendChild(paymentsComponent);
* {
 box-sizing: border-box;
}
body {
 font-family: -apple-system, BlinkMacSystemFont, sans-serif;
 font-size: 16px;
 -webkit-font-smoothing: antialiased;
}
.container {
 width: 100%;
 padding: 16px;
 display: flex;
 justify-content: center;
 align-content: center;
 flex-direction: column;
}
{
 "name": "stripe-sample-code",
 "version": "1.0.0",
 "description": "Build a full, working integration using Connect embedded components. Here are some basic scripts you can use to build and run the application.",
 "scripts": {
  "start": "parcel watch",
  "build": "parcel build"
 },
 "author": "",
 "license": "ISC",
 "devDependencies": {
  "parcel": "^2.8.3"
 },
 "source": "public/index.html",
 "dependencies": {
  "@stripe/connect-js": "3.3.20"
 }
}
# Integrate with Connect embedded components
Build a full, working integration using Connect embedded components. Here are some basic
scripts you can use to build and run the application.
## Replace the following variables
Ensure that you have replaced the following placeholders in the downloaded code sample:
- {{CONNECTED_ACCOUNT_ID}}
- pk_INSERT_YOUR_PUBLISHABLE_KEY
- sk_INSERT_YOUR_SECRET_KEY
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
5. Go to [http://localhost:4242/index.html](http://localhost:4242/index.html)

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

