Skip to main content
Version: v7.0.0
On this page
## Messages​
We've gathered all the validation message in to `apps/isomorphic/src/config/messages.ts` file. You can add your own validation messages and updated existing message from this file.
apps/isomorphic/src/config/messages.ts
```
exportconst messages ={ emailIsRequired:"Email address is required", invalidEmail:"Invalid email address", passwordRequired:"Password is required", passwordLengthMin:"Password must be at least 6 characters", nameIsRequired:"Name is required",// More messages...};
```

### Usage​
apps/isomorphic/src/utils/common-rules.ts
```
import{ z }from"zod";import{ messages }from"@/config/messages";exportconst validateEmail = z.string().min(1,{ message: messages.emailIsRequired}).email({ message: messages.invalidEmail});
```

  * Messages
    * Usage


