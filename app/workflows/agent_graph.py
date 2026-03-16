from app.agents.analysis_agent import analysis_agent
from app.agents.data_agent import data_agent
from app.agents.planner_agent import planner_agent
from app.agents.summary_agent import summary_agent

def run_multiagent_workflow(
        question:str,
        file_path:str='data/sales_data.csv'
        ) ->dict:
    
    plan=planner_agent(question)
    df=data_agent(file_path)
    analysis=analysis_agent(df)
    answer=summary_agent(question,analysis)

    return {
        "plan":plan,
        "analysis":analysis,
        "answer":answer
    }
    
from app.agents.planner_agent import planner_agent
from app.agents.data_agent import data_agent
from app.agents.analysis_agent import analysis_agent
from app.agents.summary_agent import summary_agent
from app.utils.logger import logger


def run_multiagent_workflow(
    question: str,
    file_path: str = "data/sales_data.csv"
) -> dict:
    logger.info(f"Starting workflow for question: {question}")

    plan = planner_agent(question)
    logger.info("Planner agent completed")

    df = data_agent(file_path)
    logger.info(f"Data agent loaded dataset with shape: {df.shape}")

    analysis = analysis_agent(df)
    logger.info("Analysis agent completed")

    answer = summary_agent(question, analysis)
    logger.info("Summary agent completed")

    return {
        "plan": plan,
        "analysis": analysis,
        "answer": answer
    }