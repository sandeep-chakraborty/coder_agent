from crewai import Agent
import os
from textwrap import dedent
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.llms import OpenAI, Ollama
from dotenv import load_dotenv
load_dotenv()
class CustomAgents:
    def __init__(self):
       self.llm =  ChatOpenAI(model_name="gpt-4o", temperature=0.7)
    def architect_agent(self, tools):
        return Agent(
            role="Software Architect",
            backstory=dedent(f"""\
            With years of experience in system design, 
            you excel at breaking down complex problems into manageable solutions,
            providing a solid foundation for implementation."""),
            goal=dedent(f"""\
            Provide a high-level solution overview for a given problem"""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def programmer_agent(self, tools):
        return Agent(
            role="Senior Software Engineer",
            backstory=dedent(f"""
                             You are a Senior Software Engineer at a leading tech think tank.
				Your expertise in programming in python. and do your best to
				produce perfect code you have a keen eye for detail and a knack for translating high-level design solutions into robust,
                efficient code."""),
            goal=dedent(f"""Implement the solution provided by the architect"""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def tester_agent(self, tools):
        return Agent(
            role="Software Tester",
            backstory=dedent(f"""\
            Your passion for quality ensures that every piece of code meets the highest
            standards through rigorous testing."""),
            goal = dedent("""\
            Write and run test cases for the code implemented by the programmer"""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def reviewer_agent(self, tools):
        return Agent(
            role="Software Reviewer",
            backstory=dedent("""\
            With a critical eye, you review each step of the development process, ensuring quality and consistency."""),
            goal=dedent("""\
            Review the work of each agent at each step"""),
            tools=tools,            
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )
