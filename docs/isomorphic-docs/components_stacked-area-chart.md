Skip to main content
Version: v7.0.0
On this page
## Stacked Area Chart​
### Preview​
![Stacked Area Chart preview](https://isomorphic-doc.vercel.app/assets/images/stacked-area-chart-3e03e02eace8dfe34ffa59beea4acbfb.png)
### Code​
apps/isomorphic/src/app/shared/chart-widgets/stacked-area-chart.tsx
```
'use client';import{AreaChart,Area,XAxis,YAxis,CartesianGrid,Tooltip,ResponsiveContainer,}from'recharts';import{CustomTooltip}from'@/components/charts/custom-tooltip';exportdefaultfunctionStackedAreaChart(){return(<ResponsiveContainerwidth="100%"height="100%"><AreaChartdata={data}margin={{     left:-20,}}className="[&_.recharts-cartesian-grid-vertical]:opacity-0"><defs><linearGradientid="stackedAreaChart1"x1="0"y1="0"x2="0"y2="1"><stopoffset="5%"stopColor="#3872FA"className="[stop-opacity:0.4] dark:[stop-opacity:0.3]"/><stopoffset="95%"stopColor={'#3872FA'}stopOpacity={0}/></linearGradient><linearGradientid="stackedAreaChart2"x1="0"y1="0"x2="0"y2="1"><stopoffset="5%"stopColor="#10b981"className="[stop-opacity:0.4] dark:[stop-opacity:0.3]"/><stopoffset="95%"stopColor={'#10b981'}stopOpacity={0}/></linearGradient><linearGradientid="stackedAreaChart3"x1="0"y1="0"x2="0"y2="1"><stopoffset="5%"stopColor="#eab308"className="[stop-opacity:0.4] dark:[stop-opacity:0.3]"/><stopoffset="95%"stopColor={'#eab308'}stopOpacity={0}/></linearGradient></defs><CartesianGridstrokeDasharray="3 3"/><XAxisdataKey="name"/><YAxis/><Tooltipcontent={<CustomTooltip/>}/><Areatype="monotone"dataKey="uv"stackId="1"strokeWidth={2}stroke="#3872FA"// fill="#3872FA"fill="url(#stackedAreaChart1)"// fillOpacity={0.5}/><Areatype="monotone"dataKey="pv"stackId="1"strokeWidth={2}stroke="#10b981"// fill="#10b981"fill="url(#stackedAreaChart2)"// fillOpacity={0.5}/><Areatype="monotone"dataKey="amt"stackId="1"stroke="#eab308"strokeWidth={2}// fill="#eab308"fill="url(#stackedAreaChart3)"// fillOpacity={0.5}/></AreaChart></ResponsiveContainer>);}
```

  * Stacked Area Chart
    * Preview
    * Code


