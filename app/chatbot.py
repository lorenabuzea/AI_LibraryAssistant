from openai import OpenAI
import os
from app.rag import search_books
from app.tools import get_summary_by_title

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#define tool schema

tools = [
    {
        "type": "function",
        "function":{
            "name": "get_summary_by_title",
            "description": "Get the summary of a book by its title.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the book."
                    }
                },
                "required": ["title"]
            }
        }
    }
]


def chat(user_input: str) -> str:
    try:
        # Step 1: Search for relevant books
        results = search_books(user_input, top_k=3)

        if not results:
            return "I'm sorry, I couldn't find any books in my database that match your interests. Could you try describing what you're looking for differently?"

        # Step 2: Build context with available books
        available_books = []
        for book in results:
            # If 'author' isn't in your JSON, remove or replace this field
            available_books.append(f"- {book['title']}: {book['summary']}")

        books_context = "\n".join(available_books)

        # Step 3: Constrained system prompt
        system_prompt = f"""You are a specialized AI librarian with access to a curated book database. 

IMPORTANT CONSTRAINTS:
- You can ONLY recommend books from the database provided below.
- Never suggest books that are not in this list.
- If asked about books not in the database, politely explain you can only recommend from your available collection.

AVAILABLE BOOKS IN DATABASE:
{books_context}

Your role is to analyze the user's request and recommend the most relevant book(s) from the available options."""

        # Step 4: Query OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Or use gpt-4 if you prefer
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

