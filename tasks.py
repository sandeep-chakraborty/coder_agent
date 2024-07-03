from crewai import Task
from textwrap import dedent


class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def architecture_task(self, agent, tools, user_input):
        return Task(
            description=dedent(f"""
            Design the high-level structure for a new CrewAI agent to solve: {user_input}. 
            Your final answer must include a clear overview and major components involved.
            {self.__tip_section()}
            You have access to tools which can search the internet, read files, write files, and create directories.
            """),
            expected_output='A document outlining the high-level design of the new CrewAI agent.',
            tools=tools,
            agent=agent,
        )

    def implementation_task(self, agent, tools, context):
        return Task(
            description=dedent(f"""
            Implement the design specifications for the new CrewAI agent.
            Your final answer must include the code implementing the agent.                          
            {self.__tip_section()}
            You have access to tools which can read files, write files, and create directories.
            """),
            expected_output='Python code implementing the new CrewAI agent.',
            tools=tools,
            agent=agent,
            context=context
        )

    def testing_task(self, agent, tools, context):
        return Task(
            description=dedent(f"""
            Write and run test cases for the new CrewAI agent. 
            Your final answer must include test scripts and test results.                          
            {self.__tip_section()}
            You have access to tools which can read files, write files, and create directories.
            """),
            expected_output='Test scripts and test document for the new CrewAI agent.',
            tools=tools,
            agent=agent,
            context=context
        )

    def reviewing_task(self, agent, tools, context):
        return Task(
             description=dedent(f"""
            Review the design and implementation of the new CrewAI agent.
            Your final answer must include feedback and necessary revisions.
            You should also provide steps to run the agent as a documentation for users.
            {self.__tip_section()}
            You have access to tools which can read files, write files, and create directories.
            """),
            expected_output='Feedback and revisions for each step of the process, along with a final document for running the agent.',
            tools=tools,
            agent=agent,
            context=context
        )
