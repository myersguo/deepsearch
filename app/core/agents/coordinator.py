from langchain_core.prompts import PromptTemplate
from langchain.agents import create_react_agent
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from app.core.llm import get_llm
from langchain_core.messages import HumanMessage, SystemMessage
import os
import jinja2
from  app.core.types import State
from app.core.agents.base import BaseAgent
from langgraph.types import Command



class CoordinatorAgent(BaseAgent):
    def __init__(self):
        self.llm = get_llm()
        
        # Load prompt template
        template_path = os.path.join(os.path.dirname(__file__), "../prompts/coordinator.md")
        with open(template_path, "r") as f:
            template_content = f.read()
            
        self.prompt_template = jinja2.Template(template_content)
        
    async def process(self, state: State) -> Command:
        locale = state.get("locale", "en")
        prompt_content = self.prompt_template.render(query=state.get("query"), locale=locale)
        chain =  self.llm | JsonOutputParser()
        messages = [SystemMessage(content=prompt_content), HumanMessage(content=state.get("query"))]
        result = await chain.ainvoke(messages)
        
        # Use the detected locale from the LLM response, or fall back to the current locale
        detected_locale = result.get("locale", locale)
        
        return Command(
            goto="researcher_node" if result.get("coordinator") == "requires_research" else "END",
            update={"coordinator": result.get("coordinator"),
                    "response": result.get("response"),
                    "locale": detected_locale
                   }
        )
