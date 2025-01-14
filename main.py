from typing import Dict
from workflow import create_workflow

# Compile the workflow
app = create_workflow()

def run_user_query(query: str) -> Dict[str, str]:
    """Process a user query through the LangGraph workflow.

    Args:
        query (str): The user's query

    Returns:
        Dict[str, str]: A dictionary containing the query's category and response
    """
    results = app.invoke({"query": query})
    return {
        "category": results["category"],
        "response": results["response"]
    }

# Test case: mock inteview
if __name__ == "__main__":
    query = "I need mock interview to practice."
    result = run_user_query(query)
    print(result)
