test_data = [
    {"query": "What is AI regulation?", "type": "FACTUAL"},
    {"query": "Compare EU and US AI laws", "type": "SYNTHESIS"},
    {"query": "Who is Elon Musk?", "type": "OUT_OF_SCOPE"},
]


def keyword_overlap(pred, expected):
    pred_words = set(pred.lower().split())
    exp_words = set(expected.lower().split())

    if len(exp_words) == 0:
        return 0

    return len(pred_words & exp_words) / len(exp_words)


import pandas as pd
from main import agentic_rag
from src.router import classify_query

results = []

for item in test_data:
    query = item["query"]
    expected_type = item["type"]
    expected_answer = item["expected"]

    predicted_answer = agentic_rag(query)
    predicted_type = classify_query(query)

    score = keyword_overlap(predicted_answer, expected_answer)

    results.append({
        "query": query,
        "expected_type": expected_type,
        "predicted_type": predicted_type,
        "score": score
    })

# Convert to DataFrame
df = pd.DataFrame(results)

# Save results
df.to_csv("results.csv", index=False)

print(df)
