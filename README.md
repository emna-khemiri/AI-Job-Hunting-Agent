# AI Job Hunting Agent Your - Ultimate Guide to a Career in AI! 🚀
## Overview
This project is an AI-powered mentor designed to simplify and support your journey in:
- **AI Learning**
- **Resume Preparation**
- **Interview Assistance**
- **Job Hunting**


## Motivation
Navigating the rapidly evolving field of Generative AI can be overwhelming due to:
- Scattered, outdated resources
- Time-consuming videos and tutorials
- Depreciated code and tools

This assistant addresses these challenges by offering tailored support, ensuring you stay ahead in this fast-changing domain.

## Key Features
1. **Learning & Content Creation**
   - Tailored learning pathways covering key Generative AI topics.
   - Assistance with creating tutorials, blogs, and posts based on user interests.

2. **Q&A Support**
   - On-demand Q&A sessions for guidance on concepts or coding issues.

3. **Resume Building & Review**
   - Personalized, market-relevant resume crafting.
   - Expert consultations for creating standout resumes.

4. **Interview Preparation**
   - Mock interviews and Q&A sessions on common and technical questions.

5. **Job Search Assistance**
   - Tailored guidance and insights for effective job hunting.

## Tech Stack
- **LangChain**: Workflow construction and query handling.
- **LangGraph**: Flexible workflow graph creation.
- **Gemini LLM**: Language model for response generation.
- **DuckDuckGoSearchResult**: External data sourcing.

## Workflow
Below is a visual representation of the project's workflow:

![Workflow Diagram](https://github.com/emna-khemiri/AI-Job-Hunting-Agent/blob/main/workflow_graph.png)

### Key Components
1. **State Management**: Using `TypedDict` to define and manage the state of user interactions.
2. **Query Categorization**: Classifying queries into Learning, Resume Preparation, Interview, or Job Search.
3. **Subcategorization**: E.g., Learning (Tutorials, Q&A), Interview (Prep, Mock Interviews).
4. **Response Generation**: Tailored outputs based on user queries.
5. **Workflow Graph**: Extensible and dynamic workflows using `LangGraph`.

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/emna-khemiri/AI-Job-Hunting-Agent.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AI-Job-Hunting-Agent
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Usage
- Interact with the assistant by providing queries related to learning, resumes, interviews, or job hunting.
- Use the workflow visualization to explore the assistant’s decision-making process.

## Future Enhancements
- **Knowledge Base**: Resource-rich library with curated links to courses, tutorials, and articles.
- **Multi-Domain Customization**: Expand functionality to other career paths.
- **Advanced Job Search Tools**: Automate job application tracking and enhance networking features.

## Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).



