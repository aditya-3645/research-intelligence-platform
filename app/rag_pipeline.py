from app.prompts.rag_prompt import RAG_PROMPT


def ask_question(retriever, llm, question: str):
    """
    Retrieves relevant documents and generates an answer.
    """

    documents = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in documents]
    )

    prompt = RAG_PROMPT.invoke({
        "context": context,
        "question": question
    })

    response = llm.invoke(prompt)

    return response.content