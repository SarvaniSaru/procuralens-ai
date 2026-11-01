from pathlib import Path
from src.pdf_processor import extract_pdf_bytes

def test_samples_extract():
    files=list((Path(__file__).parents[1]/"sample_rfps").glob("*.pdf"))
    assert len(files) >= 4
    for f in files:
        result=extract_pdf_bytes(f.read_bytes())
        assert result["pages"] >= 2 and "[PAGE 1]" in result["text"]
