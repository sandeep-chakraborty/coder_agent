from crewai import Agent
import os
from textwrap import dedent
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.llms import OpenAI, Ollama
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key
class CustomAgents:
    def __init__(self):
       self.llm =  ChatOpenAI(model_name="gpt-4o", temperature=0.7)
    def architect_agent(self, tools):
        return Agent(
            role="Software Architect",
            backstory=dedent(f"""\
            With extensive experience in AI system design, 
            you specialize in creating and configuring intelligent agents."""),
            goal=dedent(f"""\
           Design the high-level structure of new CrewAI agents."""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def programmer_agent(self, tools):
        return Agent(
            role="Senior Software Engineer",
            backstory=dedent(f"""
                            As a seasoned software engineer, you excel at implementing AI agents based on high-level designs."""),
            goal=dedent(f"""Implement the design specifications for new CrewAI agents."""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def tester_agent(self, tools):
        return Agent(
            role="Software Tester",
            backstory=dedent(f"""\
             Your passion for quality ensures that every agent meets the highest
            standards through rigorous testing."""),
            goal = dedent("""\
           Test the implemented CrewAI agents to ensure they work as expected."""),
            tools=tools,
            allow_code_execution=True,
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def reviewer_agent(self, tools):
        return Agent(
            role="Software Reviewer",
            backstory=dedent("""\
           With a critical eye, you review each agent's implementation, ensuring quality and consistency."""),
            goal=dedent("""\
           Review the design and implementation of CrewAI agents"""),
            tools=tools,            
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )
