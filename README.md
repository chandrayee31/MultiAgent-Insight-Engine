
# MultiAgent Insight Engine

A Multi-Agent AI System for Automated Business Data Analysis.

## Overview

MultiAgent Insight Engine demonstrates how multiple AI agents collaborate to analyze business datasets and generate insights automatically.

Agents collaborate in the following workflow:

User Question
↓
Planner Agent
↓
Data Agent
↓
Analysis Agent
↓
Summary Agent
↓
Final Business Insight

## Agents

### Planner Agent
Breaks a user question into structured analysis steps.

### Data Agent
Loads datasets and prepares them for analysis.

### Analysis Agent
Performs statistical analysis such as monthly sales trends and category comparisons.

### Summary Agent
Uses an LLM (Ollama) to generate a human-readable explanation.

## Project Structure

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
