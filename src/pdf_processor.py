"""Page-aware PDF extraction."""
from __future__ import annotations
import hashlib
import fitz


def extract_pdf_bytes(raw: bytes, max_pages: int = 100) -> dict:
    if not raw.startswith(b"%PDF"):
        raise ValueError("Not a PDF")
    doc = fitz.open(stream=raw, filetype="pdf")
    if doc.needs_pass:
        raise ValueError("Password-protected PDF")
    if len(doc) > max_pages:
        raise ValueError("PDF page limit exceeded")
    pages = []
    for index, page in enumerate(doc, 1):
        text = " ".join(page.get_text("text").replace("\x00", " ").split())
        pages.append(f"[PAGE {index}]\n{text}")
    result = "\n\n".join(pages)
    return {"text": result, "pages": len(doc), "sha256": hashlib.sha256(raw).hexdigest(),
            "warnings": ["Very little text extracted; OCR may be required"] if len(result.strip()) < 100 else []}
