Skip to main content
Version: v7.0.0
On this page
## Multi Step Form​
We have a fullscreen multistep form, the multistep form is located at `apps/isomorphic/src/app/multi-step`.
And all the steps components are avilable in `apps/isomorphic/src/app/shared/multi-step/multi-step-1` directory.
## Adding a New Step​
Start by creating a component according to your requirements. Next, seamlessly import the component into the `src/app/shared/multi-step/multi-step-1/index.tsx` file, as shown below:
apps/isomorphic/src/app/shared/multi-step/multi-step-1/index.tsx
```
importStepOnefrom'@/app/shared/multi-step/multi-step-1/step-1';importStepTwofrom'@/app/shared/multi-step/multi-step-1/step-2';importStepThreefrom'@/app/shared/multi-step/multi-step-1/step-3';importStepFourfrom'@/app/shared/multi-step/multi-step-1/step-4';importStepFivefrom'@/app/shared/multi-step/multi-step-1/step-5';importStepSixfrom'@/app/shared/multi-step/multi-step-1/step-6';importStepSevenfrom'@/app/shared/multi-step/multi-step-1/step-7';importCongratulationsfrom'@/app/shared/multi-step/multi-step-1/congratulations';
```

Specify the type and default values for your creation:
apps/isomorphic/src/app/shared/multi-step/multi-step-1/index.tsx
```
typeformDataType={ propertyType:string; placeType:string; address:string|undefined; lat:number|undefined; lng:number|undefined; guests:number|undefined; bedrooms:number|undefined; beds:number|undefined; bedroomLock:string; guestType:string; indoorAmenities:string[]|undefined; outdoorAmenities:string[]|undefined; propertyName:string; propertyDescription:string|undefined; priceRange:number[]|undefined; photos:string|undefined; yourNewInput:string|undefined;};exportconst initialFormData ={ propertyType:'', placeType:'', address:'', lat:undefined, lng:undefined, guests:undefined, bedrooms:undefined, beds:undefined, bedroomLock:'', guestType:'', indoorAmenities:[], outdoorAmenities:[], propertyName:'', propertyDescription:'', priceRange:undefined, photos:'', yourNewInput:undefined,};
```

Now, add your component to the enum list:
apps/isomorphic/src/app/shared/multi-step/multi-step-1/index.tsx
```
exportenumStep{StepOne,StepTwo,StepThree,StepFour,StepFive,StepSix,StepSeven,StepEight,}
```

Complete the process by registering your component in the component mapper:
apps/isomorphic/src/app/shared/multi-step/multi-step-1/index.tsx
```
constMAP_STEP_TO_COMPONENT={[Step.StepOne]:StepOne,[Step.StepTwo]:StepTwo,[Step.StepThree]:StepThree,[Step.StepFour]:StepFour,[Step.StepFive]:StepFive,[Step.StepSix]:StepSix,[Step.StepSeven]:StepSeven,[Step.StepEight]:Congratulations,};
```

Voila! Your Multistep Form Now Includes a New Step!
  * Multi Step Form
  * Adding a New Step


