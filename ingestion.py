from sentence_transformers import SentenceTransformer
import faiss
import os

model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start+chunk_size])
        start += chunk_size - overlap
    return chunks

def load_docs(folder="data"):
    texts = []
    for file in os.listdir(folder):
        with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
            texts.append(f.read())
    return texts

def build_index():
    docs = load_docs()
    all_chunks = []

    for doc in docs:
        all_chunks.extend(chunk_text(doc))

    embeddings = model.encode(all_chunks)

    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)

    return index, all_chunks