Skip to main content
Version: v7.0.0
On this page
## Radial Bar Chart​
### Preview​
![Radial Bar Chart preview](https://isomorphic-doc.vercel.app/assets/images/radial-bar-chart-af0a125fd31fcf94ce53cc581cf865fb.png)
### Code​
apps/isomorphic/src/app/shared/chart-widgets/radial-bar-chart.tsx
```
'use client';import{RadialBarChartasRadialBarChartComponent,RadialBar,Legend,ResponsiveContainer,}from'recharts';exportdefaultfunctionRadialBarChart(){return(<ResponsiveContainerwidth="100%"height="100%"className="[&_.recharts-default-legend]:flex [&_.recharts-default-legend]:flex-wrap [&_.recharts-default-legend]:justify-center @xl:[&_.recharts-default-legend]:flex-col [&_.recharts-legend-wrapper]:!static [&_.recharts-legend-wrapper]:!-mt-[22px] [&_.recharts-legend-wrapper]:!leading-[22px] @xs:[&_.recharts-legend-wrapper]:!mt-0 @xl:[&_.recharts-legend-wrapper]:!absolute @xl:[&_.recharts-legend-wrapper]:!end-0 @xl:[&_.recharts-legend-wrapper]:!start-auto @xl:[&_.recharts-legend-wrapper]:!top-1/2 @xl:[&_.recharts-legend-wrapper]:!-translate-y-1/2 @xl:[&_.recharts-legend-wrapper]:!translate-x-0 @xl:[&_.recharts-legend-wrapper]:!leading-9"><RadialBarChartComponentinnerRadius="20%"outerRadius="110%"barSize={isMobile ?16:24}data={data}className="rtl:[&_.recharts-legend-item>svg]:ml-1"><RadialBarlabel={{ fill:'#ffffff', position:'insideStart'}}backgrounddataKey="sales"className="[&_.recharts-radial-bar-background-sector]:fill-gray-100"/><LegendiconSize={10}layout="vertical"verticalAlign="middle"/></RadialBarChartComponent></ResponsiveContainer>);}
```

  * Radial Bar Chart
    * Preview
    * Code


