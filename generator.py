def generate_answer(query, retrieved_chunks, query_type):

    if query_type == "OUT_OF_SCOPE":
        return "The information is not available in the provided documents."

    context = " ".join(retrieved_chunks)

    # simple generation logic (can upgrade to OpenAI later)
    answer = f"Based on documents: {context[:500]}"

    return answer