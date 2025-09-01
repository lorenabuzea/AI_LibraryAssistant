import json

def load_summaries ( file_path = "app/data/book_summaries.json" ) -> list[dict] :
    with open ( file_path , "r", encoding="utf-8" ) as f :
        summaries = json.load ( f )
    return summaries

def get_summary_by_title ( titile: str ) -> str :
    summaries = load_summaries()
    for book in summaries :
        if book['title'].lower() == titile.lower() :
            return book['summary']
    return f"Summary not found for '{titile}'."