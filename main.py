import warnings
warnings.filterwarnings("ignore")
import os
from crewai import Agent, Task, Crew, Process
from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks
from crewai_tools import  FileReadTool
from tools.file_write import FileWriteTool
from tools.directory_write import DirWriteTool
from tools.search_tools import SearchTools
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key

search_tool = SearchTools.search_internet
file_read_tool = FileReadTool()
file_write_tool = FileWriteTool.file_write_tool
dir_write_tool = DirWriteTool.dir_write_tool

# Tools
architect_tools = [search_tool, file_read_tool, file_write_tool, dir_write_tool]
programmer_tools = [file_read_tool, file_write_tool, dir_write_tool]
tester_tools = [file_read_tool, file_write_tool, dir_write_tool]
reviewer_tools = [file_read_tool, file_write_tool, dir_write_tool]



class CustomCrew:
    def __init__(self, user_input):
        self.user_input = user_input
    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        # Agents
        architect_agent = agents.architect_agent(architect_tools)
        programmer_agent = agents.programmer_agent(programmer_tools)
        tester_agent = agents.tester_agent(tester_tools)
        reviewer_agent = agents.reviewer_agent(reviewer_tools)

        # Tasks
        architecture_task = tasks.architecture_task(architect_agent, architect_tools, self.user_input)
        implementation_task = tasks.implementation_task(programmer_agent, programmer_tools, [architecture_task])
        testing_task = tasks.testing_task(tester_agent, tester_tools, [implementation_task])
        reviewing_task = tasks.reviewing_task(reviewer_agent, reviewer_tools, [architecture_task, implementation_task, testing_task])

        crew = Crew(
            agents=[architect_agent, programmer_agent, tester_agent, reviewer_agent],
            tasks=[architecture_task, implementation_task, testing_task, reviewing_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result



if __name__ == "__main__":
    user_input = input("What crew do you want me to make?\n")
    crew = CustomCrew(user_input)
    result = crew.run()
    
    print("\n\n########################")
    print("## Here is you new agent output:")
    print("########################\n")
    print(result)


#everything works but the OPENAI_API_KEY is wrong i suppose, it says invalid API key