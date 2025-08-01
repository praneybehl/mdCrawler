Miscellaneous
###  app.Store() 
`app.Store()` returns a concurrent-safe application memory store that you can use to store anything for the duration of the application process (e.g. cache, config flags, etc.).
You can find more details about the available store methods in the `store.Store` documentation but the most commonly used ones are `Get(key)`, `Set(key, value)` and `GetOrSet(key, setFunc)`.
`app.Store().Set("example", 123) v1 := app.Store().Get("example").(int) // 123 v2 := app.Store().GetOrSet("example2", func() any { // this setter is invoked only once unless "example2" is removed // (e.g. suitable for instantiating singletons) return 456 }).(int) // 456`
Keep in mind that the application store is also used internally usually with `pb*` prefixed keys (e.g. the collections cache is stored under the `pbAppCachedCollections` key) and changing these system keys or calling `RemoveAll()`/`Reset()` could have unintended side-effects.
If you want more advanced control you can initialize your own store independent from the application instance via `store.New[K, T](nil)`.
###  Security helpers 
_Below are listed some of the most commonly used security helpers but you can find detailed documentation for all available methods in the`security` subpackage._
#####  Generating random strings 
`secret := security.RandomString(10) // e.g. a35Vdb10Z4 secret := security.RandomStringWithAlphabet(5, "1234567890") // e.g. 33215`
#####  Compare strings with constant time 
`isEqual := security.Equal(hash1, hash2)`
#####  AES Encrypt/Decrypt 
`// must be random 32 characters string const key = "RO8JJBCy1fpNdhIw8SmS6ToK6U7gES8p" encrypted, err := security.Encrypt([]byte("test"), key) if err != nil { return err } decrypted := security.Decrypt(encrypted, key) // []byte("test")`
Prev: Testing Next: Record proxy
