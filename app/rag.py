import os
import chromadb
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chroma_client = chromadb.PersistentClient(path=os.path.join("app", "data", "chroma_db"))

collection = chroma_client.get_or_create_collection(name="book_summaries")

def load_book_summaries() -> list[dict]:
    with open("app/data/book_summaries.json", "r") as f:
        book_summaries = json.load(f)
        print(f"✅ Loaded {len(book_summaries)} book summaries")
    return book_summaries

def get_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding


def populate_chroma(summaries: list[dict]) -> None:
    # Check if collection already has data to avoid duplicates
    existing_count = collection.count()
    if existing_count > 0:
        print(f"Collection already has {existing_count} items. Skipping population.")
        return

    for i, summary in enumerate(summaries):
        collection.add(
            documents=[summary['summary']],
            metadatas=[{
                "title": summary['title'],
                "author": summary.get('author', 'Unknown Author')  # Use .get() with default value
            }],
            ids=[f"book_{i + 1:03d}"],  # Generate IDs automatically
            embeddings=[get_embedding(summary['summary'])]
        )


def search_books(query: str, top_k=1) -> list[dict]:
    query_embedding = get_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    books = []
    for i in range(len(results['ids'][0])):
        book = {
            "id": results['ids'][0][i],
            "summary": results['documents'][0][i],
            "title": results['metadatas'][0][i]['title'],
            "author": results['metadatas'][0][i]['author']
        }
        books.append(book)
    return books