Browser Use home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/dark.svg)
Search or ask...
Ctrl K
Search...
Navigation
Customize
Output Format
DocumentationCloud API
##### Get Started
  * Introduction
  * Quickstart


##### Customize
  * Supported Models
  * Agent Settings
  * Browser Settings
  * Connect to your Browser
  * Output Format
  * System Prompt
  * Sensitive Data
  * Custom Functions


##### Development
  * Local Setup
  * Telemetry
  * Observability
  * Roadmap


## 
​
Custom output format
With this example you can define what output format the agent should return to you.
Copy
```
from pydantic import BaseModel
# Define the output format as a Pydantic model
class Post(BaseModel):
	post_title: str
	post_url: str
	num_comments: int
	hours_since_post: int

class Posts(BaseModel):
	posts: List[Post]

controller = Controller(output_model=Posts)

async def main():
	task = 'Go to hackernews show hn and give me the first 5 posts'
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(task=task, llm=model, controller=controller)
	history = await agent.run()
	result = history.final_result()
	if result:
		parsed: Posts = Posts.model_validate_json(result)
		for post in parsed.posts:
			print('\n--------------------------------')
			print(f'Title:      {post.post_title}')
			print(f'URL:       {post.post_url}')
			print(f'Comments:     {post.num_comments}')
			print(f'Hours since post: {post.hours_since_post}')
	else:
		print('No result')

if __name__ == '__main__':
	asyncio.run(main())

```

Was this page helpful?
YesNo
Connect to your BrowserSystem Prompt
On this page
  * Custom output format


