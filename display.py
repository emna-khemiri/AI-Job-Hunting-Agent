
from IPython.display import display, Image, Markdown
from langchain_core.runnables.graph import MermaidDrawMethod # to visualize the graph of langgraph node and edges
from workflow import create_workflow

# Compile the workflow
app = create_workflow()

# Generate the Mermaid graph as PNG binary data
png_data = app.get_graph().draw_mermaid_png(draw_method=MermaidDrawMethod.API)

# Save the binary PNG data to a file
graph_png_path = "workflow_graph.png"
with open(graph_png_path, "wb") as file:
    file.write(png_data)

print(f"Workflow graph has been saved as {graph_png_path}")
