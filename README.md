# DeepSearch

DeepSearch is an intelligent search and Q&A system built with FastAPI and LangChain. The system employs a multi-agent architecture, utilizing the collaboration between Coordinator, Researcher, and Reporter agents to provide high-quality search results and answers.

## Features

- 🤖 Multi-Agent Collaboration System
  - Coordinator Agent: Understands user intent and coordinates other agents
  - Researcher Agent: Conducts in-depth research and information gathering
  - Reporter Agent: Organizes and presents final results
- 🔄 LangGraph-based Workflow Management
- 🚀 High-performance FastAPI Backend
- 📝 Structured Response Format

## Tech Stack

- FastAPI
- LangChain
- LangGraph
- OpenAI
- Tavily Search API
- Pydantic
- Uvicorn

## Installation

1. Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/myersguo/deepsearch
cd deepsearch
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file and set the necessary environment variables:
```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Usage

1. Start the server:
```bash
python main.py
```

2. The server will start at `http://localhost:8081`

3. API Endpoint:
- POST `/api/query`
  - Request body:
    ```json
    {
        "query": "your question"
    }
    ```
  - Response example:
    ```json
    {
        "query": "original question",
        "response": "agent-generated answer",
        "workflow_path": ["workflow nodes traversed"]
    }
    ```

## Project Structure

```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   └── __init__.py
│   ├── config
│   │   └── settings.py
│   └── core
│       ├── __init__.py
│       ├── agents
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── coordinator.py
│       │   ├── reporter.py
│       │   └── researcher.py
│       ├── llm.py
│       ├── prompts
│       │   ├── __init__.py
│       │   ├── coordinator.md
│       │   ├── reporter.md
│       │   └── researcher.md
│       ├── search_engine.py
│       └── types.py
├── docs
├── main.py
├── requirements.txt
└── web
    ├── package.json
    ├── pnpm-lock.yaml
    ├── public
    │   └── index.html
    ├── src
    │   ├── App.css
    │   ├── App.tsx
    │   ├── components
    │   │   ├── ChatInterface.css
    │   │   ├── ChatInterface.tsx
    │   │   ├── InputArea.css
    │   │   ├── InputArea.tsx
    │   │   ├── MarkdownRenderer.css
    │   │   ├── MarkdownRenderer.tsx
    │   │   ├── Message.css
    │   │   ├── Message.tsx
    │   │   ├── MessageList.css
    │   │   └── MessageList.tsx
    │   ├── index.css
    │   └── index.tsx
    └── tsconfig.json
```

## Development Notes

- FastAPI is used as the web framework
- LangGraph manages the workflow
- Pydantic handles data validation
- Supports asynchronous request processing

## Contributing

Issues and Pull Requests are welcome to help improve the project.

## License

[To be determined]

## Documentation

- [English](README.md)
- [中文](docs/README.zh-CN.md)
