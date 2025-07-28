Skip to main content
Version: v7.0.0
On this page
## Bar Chart​
### Preview​
![Product Modern Card preview](https://isomorphic-doc.vercel.app/components/bar-chart)
### Code​
apps/isomorphic/src/app/shared/chart-widgets/simple-bar-chart.tsx
```
'use client';import{BarChart,Bar,XAxis,YAxis,CartesianGrid,Tooltip,Legend,ResponsiveContainer,}from'recharts';import{CustomTooltip}from'@/components/charts/custom-tooltip';import{RoundedTopBarFill}from'@/components/charts/rounded-topbar';exportdefaultfunctionSimpleBarChart(){return(<ResponsiveContainerwidth="100%"height="100%"><BarChartdata={data}barSize={isMediumScreen ?18:24}margin={{     left:-10,}}className="[&_.recharts-cartesian-grid-vertical]:opacity-0"><CartesianGridstrokeDasharray="3 3"/><XAxistickLine={false}dataKey="name"/><YAxistickLine={false}/><Tooltipcontent={<CustomTooltip/>}/><Legend/><BardataKey="pv"fill="#5a5fd7"shape={<RoundedTopBarFill/>}/><BardataKey="uv"fill="#10b981"shape={<RoundedTopBarFill/>}/></BarChart></ResponsiveContainer>);}
```

  * Bar Chart
    * Preview
    * Code


