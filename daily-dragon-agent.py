import os

from dotenv import load_dotenv

from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from vocabulary_tool import get_words, add_word, remove_word

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    print('No OpenAI API key set.\nAdd your OpenAI API key to the .env file.')
    exit(1)

model = ChatOpenAI(model="gpt-4.1-nano")

vocabulary_tools = [
    get_words,
    add_word,
    remove_word
]

system_prompt = SystemMessage("You are an API client. Smart with handling issues with REST API.")

agent = create_react_agent(
    model=model,
    prompt=system_prompt,
    tools=vocabulary_tools
)

inputs = {
    "messages": [
        ("user", "list 5 random words from the vocabulary and create sentences with them")
    ]
}

result = agent.invoke(inputs)
for message in result["messages"]:
    print(message.pretty_repr())
