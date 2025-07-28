Skip to main content
Version: v7.0.0
On this page
## Radar Chart​
### Preview​
![radar chart preview](https://isomorphic-doc.vercel.app/assets/images/radar-chart-f3fcaae29feea1974d39a0b630e6b2a4.png)
### Code​
apps/isomorphic/src/app/shared/chart-widgets/simple-radar-chart.tsx
```
'use client';import{Radar,RadarChart,PolarGrid,PolarAngleAxis,PolarRadiusAxis,ResponsiveContainer,}from'recharts';exportdefaultfunctionSimpleRadarChart(){return(<ResponsiveContainerwidth="100%"height="100%"><RadarChartclassName={cn(     tickStyles.base,     tickStyles.two,     tickStyles.three,     tickStyles.four,     tickStyles.five,     tickStyles.six,     className)}cx="50%"cy="50%"outerRadius="80%"data={data}><PolarGridclassName="stroke-gray-200"/><PolarAngleAxisdataKey={dataKey}/><PolarRadiusAxis/><Radarname="Mike"dataKey={radarKey}stroke={stroke}fill={fill}strokeWidth={1.5}className="fill-opacity-60 dark:fill-opacity-20"/></RadarChart></ResponsiveContainer>);}
```

  * Radar Chart
    * Preview
    * Code


