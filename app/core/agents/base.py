
from app.core.types import State
from langgraph.types import Command

class BaseAgent:
    async def process(self, state: State) -> Command:
        raise NotImplementedError
