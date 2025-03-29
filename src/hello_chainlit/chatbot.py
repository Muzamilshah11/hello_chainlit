import os
   # import chainlit as cl
from dotenv import load_dotenv, find_dotenv
from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled


load_dotenv(find_dotenv())

   # Initialize the Gemini model
gemini_api_key = os.getenv("GEMINI_API_KEY")

   # Step 1: Provider
provider = AsyncOpenAI(
      api_key=gemini_api_key,  # Use the actual API key from the environment
      base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
   )

set_tracing_disabled(disabled=True)

   # Step 2: Model
model = OpenAIChatCompletionsModel(
      model= "gemini-2.0-flash",
      openai_client = provider
   )

   # Step 3: Config
run_config = RunConfig(
      model = model,
      model_provider = provider,
      # tracing_enabled = True,
   )

   # Step 4: Agent
agent1 = Agent(
      name = "Muzamil Shah Support Agent",
      instructions = "You are a helpful assistant.",
   )

result = Runner.run_sync(
      agent1,
      input="What is the capital of Pakistan?",
      run_config = run_config,
      # starting_agent = agent1
   )


print(result.final_output)




   # @cl.on_message
   # async def handle_message(message:cl.Message):
   #    await cl.Message(content=f"Agent:   {message.content}").send()