import requests

OLLAMA_URL="http://localhost:11434/api/generate"
MODEL_NAME="llama3"

def summary_agent(question:str,analysis:dict)->str:
    prompt=f"""
    you are a business analyst.

    Question:
    {question}

    Analysis Result:
    --Monthly Sales:{analysis["monthly_sales"]}
    -- Category sales: {analysis["category_sales"]}
    -- Lowest sales month: {analysis["lowest_sales_month"]}
    -- Highest sales month: {analysis["highest_sales_month"]}
    Write a short, clear business-friendly answer.
    Use only the provided analysis.
"""
    payload={
        "model":MODEL_NAME,
        "prompt":prompt,
        "stream":False
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=120)

    if response.status_code != 200:
        raise Exception(f"Ollama request failed: {response.text}")

    result = response.json()
    return result["response"]