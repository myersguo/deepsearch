from typing import Dict, Any, Optional, List
from langgraph.graph import MessagesState



class State(MessagesState):
    next_node: Optional[str] = None  
    query: str
    response: Optional[str] = None
    coordinator: Optional[Dict[str, Any]] = None
    search_result: Optional[Dict[str, Any]] = None
    reporter_result: Optional[Dict[str, Any]] = None
