from langgraph.prebuilt import create_react_agent
from langchain_core.tools import Tool
from app.core.llm import get_llm
from app.core.search_engine import SearchEngine
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langgraph.types import Command
from app.core.agents.base import BaseAgent
from app.core.types import State
import os
import jinja2


class ResearcherAgent(BaseAgent):
    def __init__(self):
        self.llm = get_llm()
        self.search_engine = SearchEngine()

        template_path = os.path.join(
            os.path.dirname(__file__), "../prompts/researcher.md"
        )
        with open(template_path, "r") as f:
            template_content = f.read()

        self.prompt_template = jinja2.Template(template_content)

    def _search(self, query: str) -> str:
        try:
            results = self.search_engine.search(query, 20)
            return "\n".join([res["content"] for res in results["results"]])
        except Exception as e:
            raise ValueError(f"Search failed: {e}") from e

    async def process(self, state: State) -> Command:
        query = state.get("query")
        prompt_content = self.prompt_template.render(query=query)

        search_tool = Tool(
            name="web_search_tool",
            func=self._search,
            description="Useful for when you need to search the web for information about the user query",
        )

        agent = create_react_agent(
            model=self.llm,
            tools=[search_tool],
        )

        messages = [
            SystemMessage(content=prompt_content),
            HumanMessage(content=query),
        ]

        search_result = await agent.ainvoke({"messages": messages})
        result_messages = search_result.get("messages", [])
        ret = self.parse_message(result_messages)

        return Command(goto="reporter_node", update={"search_result": ret})

    def parse_message(self, messages):
        ret = {}
        for message in messages:
            if isinstance(message, AIMessage):
                ret["response"] = message.content
            elif isinstance(message, ToolMessage):
                ret["search_result"] = message.content
        return ret
