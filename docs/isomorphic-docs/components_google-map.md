Skip to main content
Version: v7.0.0
On this page
## Google Map​
Enjoy the flexibility of our custom Google Map component! Whether you're showcasing a map, integrating autocomplete, or opting for a map without autocomplete, our component has you covered. Tailor your map experience to suit your needs effortlessly.
## Map Showcase​
```
importAutocompletefrom'@/components/google-map/autocomplete';exportdefaultYourAwesomeComponent(){retun(<AutocompleteapiKey={process.env.NEXT_PUBLIC_GOOGLE_MAP_API_KEYasstring}onPlaceSelect={handlePlaceSelect}mapClassName="rounded-lg"spinnerClassName="grid h-full w-full place-content-center"className="relative h-[500px] w-full flex-grow rounded-lg bg-gray-50"hideInput={true}/>)}
```

## Autocomplete Input​
```
importAutocompletefrom'@/components/google-map/autocomplete';exportdefaultYourAwesomeComponent(){retun(<AutocompleteapiKey={process.env.NEXT_PUBLIC_GOOGLE_MAP_API_KEYasstring}onPlaceSelect={handlePlaceSelect}spinnerClassName="hidden"hideMap={true}inputProps={{    prefix:<PiMapPinclassName="h-5 w-5"/>,    placeholder:'City, Neighborhood, ZIP, Address',    inputClassName:'dark:[&_input::placeholder]:!text-gray-600 [&_input]:pe-3 [&_input]:ps-10',    prefixClassName:'absolute start-3',    className:'[&_label>div]:p-0',    clearable:false,}}mapClassName="rounded-lg"/>)}
```

## API​
Property| Type| Is Required| Default  
---|---|---|---  
apiKey| `string`| `true`  
hideMap| `boolean`| `false`  
hideInput| `boolean`| `false`  
className| `string`| `false`  
mapClassName| `string`| `false`  
spinnerClassName| `string`| `false`  
onPlaceSelect| onPlaceSelect| `false`  
inputProps| https://www.rizzui.com/docs/components/input#input-props| `false`  
### onPlaceSelect​
```
typeonPlaceSelect:(place:Location)=>void;
```

### Location​
```
typeLocation={ address:string; lat:number; lng:number;};
```

  * Google Map
  * Map Showcase
  * Autocomplete Input
  * API
    * onPlaceSelect
    * Location


