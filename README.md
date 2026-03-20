# MultiAgent Insight Engine

### A Multi-Agent AI System for Automated Business Data Analysis

<img src="docs/demo.gif" width="850"/>

</div>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-API-green?logo=fastapi">
  <img alt="Ollama" src="https://img.shields.io/badge/LLM-Ollama-purple">
  <img alt="Multi-Agent" src="https://img.shields.io/badge/Multi--Agent-AI-orange">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-lightgrey">
</p>

## ✨ Key Features

- 🤖 **Multi-Agent Architecture**  
  Separate agents collaborate to solve complex tasks.

- 📊 **Business Data Analysis**  
  Automated analysis of structured datasets.

- 🧠 **LLM-Powered Insights**  
  Uses Ollama to generate human-readable explanations.

- ⚡ **FastAPI Service**  
  Production-ready API endpoints.

- 📈 **Traceable Agent Workflow**  
  Transparent reasoning pipeline.

## Project Structure
```text
multiagent-insight-engine/
│
├── app
│   ├── agents
│   │   ├── planner_agent.py
│   │   ├── data_agent.py
│   │   ├── analysis_agent.py
│   │   └── summary_agent.py
│   ├── workflows
│   │   └── agent_graph.py
│   ├── models
│   │   ├── request_models.py
│   │   └── response_models.py
│   └── main.py
│
├── data
│   └── sales_data.csv
│
├── tests
├── requirements.txt
└── README.md
```

## 🏗️ System Architecture

<p align="center">
  <img src="docs/architecture.png" width="900"/>
</p>

## 🔄 Agent Interaction

<p align="center">
  <img src="docs/agent_interaction.png" width="900"/>
</p>

## 🎬 Demo

<p align="center">
  <img src="docs/demo.gif" width="900"/>
</p>

## 🧩 Agents Overview

| Agent | Responsibility | Output |
|------|------|------|
| Planner Agent | Creates execution plan | Plan |
| Data Agent | Loads dataset | DataFrame |
| Analysis Agent | Performs analysis | Metrics |
| Summary Agent | Generates explanation | Final insight |


## Quick Start

Install dependencies:

pip install -r requirements.txt

Run the API:

uvicorn app.main:app --reload

Open API documentation:

http://localhost:8000/docs

## Example Request

POST /analyze

{
  "question": "Why did sales drop in March?"
}

## Tech Stack

Python  
FastAPI  
Pandas  
Ollama  
Multi-Agent Architecture

## Author

Chandrayee Kumar
