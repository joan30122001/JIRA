from docx import Document

def extract_steps_from_word(file):
    doc = Document(file)
    steps = []
    for para in doc.paragraphs:
        if para.text.strip():
            steps.append({"title": para.text, "description": "Step description can go here."})
    return steps
