from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template("""
You are an AI Research Assistant.

Answer ONLY using the provided context.

If the answer is not available in the context, respond:
"I couldn't find this information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
""")