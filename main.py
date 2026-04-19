from src.ingestion import build_index, model
from src.router import classify_query
from src.retriever import retrieve
from src.generator import generate_answer

index, chunks = build_index()

def agentic_rag(query):
    query_type = classify_query(query)

    if query_type == "OUT_OF_SCOPE":
        return generate_answer(query, [], query_type)

    retrieved = retrieve(query, model, index, chunks)
    answer = generate_answer(query, retrieved, query_type)

    return answer

# test
query = input("Ask: ")
print(agentic_rag(query))