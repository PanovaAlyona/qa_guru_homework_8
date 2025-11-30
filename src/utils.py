def clean_text(text: str) -> str:
    """Заменяет \\t и \\n на пробелы, лишние пробелы обрезает."""
    return " ".join(text.replace("\\t", " ").replace("\n", " ").split())
