from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.prompts import MessagesPlaceholder, ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

# creating 2 chains reflector chains and generator chain

generation_prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are a twitter influencer assistant tassked with writing excellent twitter posts."
         "Generate the best post possible for teh user's request."
         "If the user provides critique, respond with a revised version of your prevuvios attempts."
        ),
        MessagesPlaceholder(variable_name= "messages"),

    ]
)

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "you are a viral twitter influencer grading a tweet, Generate critique and recommendation for the user's tweet."
            "Always provide detailed recommendation, including requests for length, virality, style, etc."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# 2. create chain out this prompts
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
# llm = ChatOpenAI(model = "gpt-4o")



generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm