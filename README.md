# RAG-SYSTEM

# 📘 Agentic RAG System for AI Regulation Q&A

## 🔍 Overview

This project implements an **Agentic Retrieval-Augmented Generation (RAG)** system that answers questions based on a given set of documents related to AI regulation.

Unlike traditional RAG systems that simply retrieve relevant text and generate answers, this system introduces an **agentic layer** that **decides how to respond** to each query before generating an answer.

---

## 🧠 What is RAG?

**Retrieval-Augmented Generation (RAG)** is a technique that improves the accuracy of language models by combining:

* **Retrieval** → Fetching relevant information from a document collection
* **Generation** → Producing answers using the retrieved information

This ensures that answers are **grounded in real data** instead of relying only on the model’s internal knowledge.

---

## ⚡ What is Agentic RAG?

Agentic RAG extends the traditional RAG pipeline by adding **decision-making capability**.

Instead of always retrieving and generating, the system first analyzes the query and decides:

1. Whether the answer exists directly in the documents
2. Whether multiple sources need to be combined
3. Whether the question is outside the scope of the dataset

---

## 🏗️ System Architecture

The system is divided into the following components:

### 1. Ingestion Pipeline

* Loads the provided documents
* Splits them into smaller chunks (chunking)
* Converts text into vector embeddings
* Stores them in a FAISS vector database

**Chunking Strategy:**

* Chunk size: 300 characters
* Overlap: 50 characters
* Reason: Ensures context continuity while maintaining efficient retrieval

---

### 2. Agentic Query Router

A rule-based router classifies each query into one of three types:

* **Factual** → Answer exists directly in the documents
* **Synthesis** → Requires combining multiple pieces of information
* **Out-of-Scope** → Information is not present in the dataset

This routing logic is explicit and inspectable (not a black box).

---

### 3. Retrieval Module

* Converts the query into an embedding
* Searches the FAISS index
* Returns top-k relevant document chunks

---

### 4. Answer Generation

* For **Factual** and **Synthesis** queries:

  * Generates answers using retrieved content
* For **Out-of-Scope** queries:

  * Returns:
    `"The information is not available in the provided documents."`

This prevents hallucination.

---

## 🔄 System Workflow

User Query → Query Classification → Retrieval (if needed) → Answer Generation → Final Response

---

## 📊 Evaluation Framework

The system is evaluated using a custom evaluation pipeline:

### Test Set

* 15 total queries:

  * 5 Factual
  * 5 Synthesis
  * 5 Out-of-Scope

---

### Metrics Used

1. **Routing Accuracy**

   * Whether the query is classified correctly

2. **Retrieval Accuracy**

   * Whether relevant chunks are retrieved

3. **Answer Quality**

   * Measured using keyword overlap:

[
Score = \frac{|Predicted \cap Expected|}{|Expected|}
]

---

### Output

* Results are stored in `results.csv`
* Includes:

  * Query
  * Expected Type
  * Predicted Type
  * Score

---

## ❌ Failure Analysis

The system may fail in the following scenarios:

1. **Incorrect Query Classification**

   * Cause: Simple rule-based routing
   * Improvement: Use hybrid ML + rule-based approach

2. **Irrelevant Retrieval**

   * Cause: Fixed chunk size may break context
   * Improvement: Use semantic chunking

3. **Conflicting Information**

   * Cause: Multiple documents may contradict each other
   * Improvement: Add contradiction detection or confidence scoring

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```

To run evaluation:

```bash
python src/evaluator.py
```

---

## 📌 Conclusion

This project demonstrates how an **agentic approach** can improve traditional RAG systems by:

* Making intelligent decisions before answering
* Reducing hallucinations
* Handling complex queries more effectively

---

## 🧾 Summary

**This system is an Agentic RAG pipeline that classifies queries, retrieves relevant information when needed, synthesizes responses, and avoids answering when data is unavailable.**
