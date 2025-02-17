Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Here we demonstrate how to pass multimodal input directly to models. We currently expect all input to be passed in the same format as OpenAI expects. For other model providers that support multimodal input, we have added logic inside the class to convert to the expected format.
In this example we will ask a model to describe an image.
```
image_url ="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
```

```
from langchain_core.messages import HumanMessagefrom langchain_openai import ChatOpenAImodel = ChatOpenAI(model="gpt-4o")
```

**API Reference:**HumanMessage | ChatOpenAI
The most commonly supported way to pass in images is to pass it in as a byte string. This should work for most model integrations.
```
import base64import httpximage_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")
```

```
message = HumanMessage(  content=[{"type":"text","text":"describe the weather in this image"},{"type":"image_url","image_url":{"url":f"data:image/jpeg;base64,{image_data}"},},],)response = model.invoke([message])print(response.content)
```

```
The weather in the image appears to be clear and pleasant. The sky is mostly blue with scattered, light clouds, suggesting a sunny day with minimal cloud cover. There is no indication of rain or strong winds, and the overall scene looks bright and calm. The lush green grass and clear visibility further indicate good weather conditions.
```

We can feed the image URL directly in a content block of type "image_url". Note that only some model providers support this.
```
message = HumanMessage(  content=[{"type":"text","text":"describe the weather in this image"},{"type":"image_url","image_url":{"url": image_url}},],)response = model.invoke([message])print(response.content)
```

```
The weather in the image appears to be clear and sunny. The sky is mostly blue with a few scattered clouds, suggesting good visibility and a likely pleasant temperature. The bright sunlight is casting distinct shadows on the grass and vegetation, indicating it is likely daytime, possibly late morning or early afternoon. The overall ambiance suggests a warm and inviting day, suitable for outdoor activities.
```

We can also pass in multiple images.
```
message = HumanMessage(  content=[{"type":"text","text":"are these two images the same?"},{"type":"image_url","image_url":{"url": image_url}},{"type":"image_url","image_url":{"url": image_url}},],)response = model.invoke([message])print(response.content)
```

```
Yes, the two images are the same. They both depict a wooden boardwalk extending through a grassy field under a blue sky with light clouds. The scenery, lighting, and composition are identical.
```

## Tool calls​
Some multimodal models support tool calling features as well. To call tools using such models, simply bind tools to them in the usual way, and invoke the model using content blocks of the desired type (e.g., containing image data).
```
from typing import Literalfrom langchain_core.tools import tool@tooldefweather_tool(weather: Literal["sunny","cloudy","rainy"])->None:"""Describe the weather"""passmodel_with_tools = model.bind_tools([weather_tool])message = HumanMessage(  content=[{"type":"text","text":"describe the weather in this image"},{"type":"image_url","image_url":{"url": image_url}},],)response = model_with_tools.invoke([message])print(response.tool_calls)
```

**API Reference:**tool
```
[{'name': 'weather_tool', 'args': {'weather': 'sunny'}, 'id': 'call_BSX4oq4SKnLlp2WlzDhToHBr'}]
```

#### Was this page helpful?
  * Tool calls


