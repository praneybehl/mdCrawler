Skip to main content
Version: v7.0.0
On this page
## Constants​
We've gathered all the global constants into the `apps/isomorphic/src/config/constants.ts` file. These values are used in this whole project where required. You can adjust them to suit your needs.
The constants are using for:
  * `CART_KEY` : Key for the `cart data` to save into localStorage.
  * `DUMMY_ID ` : A dummy ID to generate dynamic route.
  * `CHECKOUT` : Key for the `checkout data` to save into localStorage.
  * `CURRENCY_CODE` : Configuration for the currency code. For example USD, INR etc.
  * `LOCALE` : Configuration for the default Language Translation.
  * `CURRENCY_OPTIONS` : 
    * `formation` : Configuration for the default currency format.
    * `fractions` : Configuration for the default currency fractional point.
  * `ROW_PER_PAGE_OPTIONS`: Configuration for the table that how many row will be rendered per page.


apps/isomorphic/src/config/constants.ts
```
exportconstCART_KEY="isomorphic-cart";exportconstPOS_CART_KEY="isomorphic-pos-cart";exportconstDUMMY_ID="FC6723757651DB74";exportconstCHECKOUT="isomorphic-checkout";exportconstCURRENCY_CODE="USD";exportconstLOCALE="en";exportconstCURRENCY_OPTIONS={ formation:"en-US", fractions:2,};exportconstROW_PER_PAGE_OPTIONS=[{  value:5,  name:"5",},{  value:10,  name:"10",},{  value:15,  name:"15",},{  value:20,  name:"20",},];
```

  * Constants


