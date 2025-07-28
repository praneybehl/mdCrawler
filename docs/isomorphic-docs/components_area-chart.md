Skip to main content
Version: v7.0.0
On this page
## Area Chart​
### Preview​
![Product Modern Card preview](https://isomorphic-doc.vercel.app/assets/images/area-chart-58d0e867b8ace1f7c5af9c849d16b3d4.png)
### Code​
apps/isomorphic/src/app/shared/analytics-dashboard/acquisition.tsx
```
'use client';import{AreaChart,Area,XAxis,YAxis,CartesianGrid,Tooltip,ResponsiveContainer,}from'recharts';import{CustomTooltip}from'@/components/charts/custom-tooltip';exportdefaultfunctionAreaChart(){return(<ResponsiveContainerwidth="100%"height="100%"><AreaChartdata={data}margin={{     left:-30,}}><XAxisdataKey="day"tickLine={false}/><YAxistickLine={false}/><Tooltipcontent={<CustomTooltip/>}/><Areatype="natural"dataKey="bounceRate"stackId="acquisitionStackID"stroke="#015DE1"fill="#015DE1"strokeWidth={1.5}fillOpacity={0.7}/><Areatype="natural"dataKey="pageSession"stackId="acquisitionStackID"stroke="#69B2F8"fill="#69B2F8"strokeWidth={1.5}fillOpacity={0.7}/></AreaChart></ResponsiveContainer>);}
```

  * Area Chart
    * Preview
    * Code


