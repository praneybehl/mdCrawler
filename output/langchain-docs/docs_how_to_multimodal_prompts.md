Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Here we demonstrate how to use prompt templates to format multimodal inputs to models.
In this example we will ask a model to describe an image.
```
import base64import httpximage_url ="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")
```

```
from langchain_core.prompts import ChatPromptTemplatefrom langchain_openai import ChatOpenAImodel = ChatOpenAI(model="gpt-4o")
```

**API Reference:**ChatPromptTemplate | ChatOpenAI
```
prompt = ChatPromptTemplate.from_messages([("system","Describe the image provided"),("user",[{"type":"image_url","image_url":{"url":"data:image/jpeg;base64,{image_data}"},}],),])
```

```
chain = prompt | model
```

```
response = chain.invoke({"image_data": image_data})print(response.content)
```

```
The image depicts a sunny day with a beautiful blue sky filled with scattered white clouds. The sky has varying shades of blue, ranging from a deeper hue near the horizon to a lighter, almost pale blue higher up. The white clouds are fluffy and scattered across the expanse of the sky, creating a peaceful and serene atmosphere. The lighting and cloud patterns suggest pleasant weather conditions, likely during the daytime hours on a mild, sunny day in an outdoor natural setting.
```

We can also pass in multiple images.
```
prompt = ChatPromptTemplate.from_messages([("system","compare the two pictures provided"),("user",[{"type":"image_url","image_url":{"url":"data:image/jpeg;base64,{image_data1}"},},{"type":"image_url","image_url":{"url":"data:image/jpeg;base64,{image_data2}"},},],),])
```

```
chain = prompt | model
```

```
response = chain.invoke({"image_data1": image_data,"image_data2": image_data})print(response.content)
```

```
The two images provided are identical. Both images feature a wooden boardwalk path extending through a lush green field under a bright blue sky with some clouds. The perspective, colors, and elements in both images are exactly the same.
```

#### Was this page helpful?
