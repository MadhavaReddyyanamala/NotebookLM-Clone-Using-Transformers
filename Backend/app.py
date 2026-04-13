from pathlib import Path

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline

from pdf_utils import extract_text_from_pdf_bytes

app = FastAPI(title="NotebookLM Clone Backend")

# Allow frontend requests during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_DIR = Path(__file__).parent / "final_model"

if not MODEL_DIR.exists():
    raise RuntimeError(f"Model folder not found at: {MODEL_DIR}")

# Load once when backend starts
summarizer = pipeline(
    "summarization",
    model=str(MODEL_DIR),
    tokenizer=str(MODEL_DIR),
)

def chunk_text(text: str, chunk_size: int = 700) -> list[str]:
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size]).strip()
        if chunk:
            chunks.append(chunk)

    return chunks


def summarize_long_text(text: str) -> str:
    text = text.strip()
    if not text:
        raise ValueError("Empty text received.")

    chunks = chunk_text(text)
    partial_summaries = []

    for chunk in chunks:
        result = summarizer(
            chunk,
            max_length=120,
            min_length=30,
            do_sample=False
        )
        partial_summaries.append(result[0]["summary_text"])

    if len(partial_summaries) == 1:
        return partial_summaries[0]

    combined = " ".join(partial_summaries)
    final_result = summarizer(
        combined,
        max_length=150,
        min_length=40,
        do_sample=False
    )
    return final_result[0]["summary_text"]


@app.get("/")
def home():
    return {"message": "Backend is running"}


@app.post("/summarize-text")
def summarize_text(text: str = Form(...)):
    try:
        summary = summarize_long_text(text)
        return {"summary": summary}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Summarization failed: {exc}") from exc


@app.post("/summarize-pdf")
async def summarize_pdf(file: UploadFile = File(...)):
    try:
        if not file.filename or not file.filename.lower().endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Please upload a PDF file.")

        pdf_bytes = await file.read()
        extracted_text = extract_text_from_pdf_bytes(pdf_bytes)

        if not extracted_text.strip():
            raise HTTPException(status_code=400, detail="No readable text found in PDF.")

        summary = summarize_long_text(extracted_text)

        return {
            "filename": file.filename,
            "summary": summary,
            "extracted_text_preview": extracted_text[:1500]
        }

    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"PDF summarization failed: {exc}") from exc