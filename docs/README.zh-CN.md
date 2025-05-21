# DeepSearch V2

DeepSearch V2 是一个基于 FastAPI 和 LangChain 构建的智能搜索和问答系统。该系统采用多智能体架构，通过协调器、研究者和报告者三个智能体的协作，为用户提供高质量的搜索结果和回答。

## 功能特点

- 🤖 多智能体协作系统
  - 协调器智能体：负责理解用户意图并协调其他智能体
  - 研究者智能体：负责深入研究和信息收集
  - 报告者智能体：负责整理和呈现最终结果
- 🔄 基于 LangGraph 的工作流管理
- 🚀 高性能 FastAPI 后端
- 📝 结构化的响应格式

## 技术栈

- FastAPI
- LangChain
- LangGraph
- OpenAI
- Tavily Search API
- Pydantic
- Uvicorn

## 安装说明

1. 克隆项目并进入项目目录：
```bash
git clone [repository-url]
cd deepsearch
```

2. 创建并激活虚拟环境：
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 配置环境变量：
创建 `.env` 文件并设置必要的环境变量：
```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## 使用方法

1. 启动服务器：
```bash
python main.py
```

2. 服务器将在 `http://localhost:8081` 启动

3. API 端点：
- POST `/api/query`
  - 请求体：
    ```json
    {
        "query": "你的问题"
    }
    ```
  - 响应示例：
    ```json
    {
        "query": "原始问题",
        "response": "智能体生成的回答",
        "workflow_path": ["经过的工作流节点"]
    }
    ```

## 项目结构

```
deepsearch/
├── app/
│   ├── config/
│   ├── core/
│   │   ├── agents/
│   │   └── types.py
├── web/
├── tests/
├── docs/
│   └── README.zh-CN.md
├── main.py
├── requirements.txt
└── README.md
```

## 开发说明

- 项目使用 FastAPI 作为 Web 框架
- 使用 LangGraph 管理工作流
- 采用 Pydantic 进行数据验证
- 支持异步处理请求

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 许可证

[待定]

## 文档

- [English](README.md)
- [中文](docs/README.zh-CN.md) 