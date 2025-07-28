Skip to main content
Version: v7.0.0
On this page
## Basic Login Form​
To craft a basic form, start by creating your form schema
```
import{ z }from'zod';const loginSchema = z.object({ username: z.string().email({ message:'Invalid username'}), password: z.string().min(1,{ message:'Password is required'}), remember: z.boolean(),});
```

Define the schema type:
```
typeLogin= z.infer<typeof loginSchema>;
```

Create form and import `SubmitHandler` from `react-hook-form`
```
import{SubmitHandler}from'react-hook-form';exportdefaultfunctionSignInForm(){const onSubmit:SubmitHandler<Login>=(data)=>{console.log(data);};return(<Form<Login>// schema typevalidationSchema={loginSchema}   resetValues={reset}   onSubmit={onSubmit}>{({ register, formState:{ errors }})=>(<divclassName="space-y-5"><Inputtype="email"size="lg"label="Email"placeholder="Enter your email"color="info"className="[&>label>span]:font-medium"inputClassName="text-sm"{...register('username')}error={errors.username?.message}/><Passwordlabel="Password"placeholder="Enter your password"size="lg"className="[&>label>span]:font-medium"inputClassName="text-sm"color="info"{...register('password')}error={errors.password?.message}/><ButtonclassName="w-full"type="submit"size="lg"color="info"><span>Sign in</span>{' '}<PiArrowRightBoldclassName="ms-2 mt-0.5 h-6 w-6"/></Button></div>)}</Form>);}
```

This sets you up with a basic login form structure using `react-hook-form` and `zod` for schema validation.
  * Basic Login Form


