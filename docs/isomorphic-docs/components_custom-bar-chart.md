Skip to main content
Version: v7.0.0
On this page
## Custom Shape Bar Chart​
### Preview​
![Stacked Area Chart preview](https://isomorphic-doc.vercel.app/assets/images/custom-bar-chart-c0a48db21a5753fad32ac01e275588b0.png)
### Code​
apps/isomorphic/src/app/shared/chart-widgets/custom-shape-bar-chart.tsx
```
'use client';import{BarChart,Bar,Cell,XAxis,YAxis,CartesianGrid,ResponsiveContainer,}from'recharts';exportdefaultfunctionCustomShapeBarChart(){return(<ResponsiveContainerwidth="100%"height="100%"><BarChartdata={data}barSize={32}margin={{     left:-20,}}><CartesianGridstrokeDasharray="3 3"/><XAxistickLine={false}dataKey="name"/><YAxistickLine={false}/><BardataKey="uv"fill="#8884d8"shape={<TriangleBar/>}label={{ position:'top'}}>{data.map((entry, index)=>(<Cellkey={`cell-${index}`}fill={colors[index %20]}/>))}</Bar></BarChart></ResponsiveContainer>);}
```

  * Custom Shape Bar Chart
    * Preview
    * Code


