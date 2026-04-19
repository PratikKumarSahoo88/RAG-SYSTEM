def retrieve(query, model, index, chunks, k=3):
    query_vec = model.encode([query])
    distances, indices = index.search(query_vec, k)

    results = [chunks[i] for i in indices[0]]
    return results