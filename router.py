def classify_query(query):
    query = query.lower()

    if any(word in query for word in ["compare", "difference", "summarize", "analyze"]):
        return "SYNTHESIS"

    elif any(word in query for word in ["what", "when", "who", "define"]):
        return "FACTUAL"

    else:
        return "OUT_OF_SCOPE"