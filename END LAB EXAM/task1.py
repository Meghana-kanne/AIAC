import re
from typing import Dict, Tuple

"""
task1.py

A small utility to convert long clinical doctor's notes into short, structured summaries.
Includes:
- a reusable prompt template (for use with an LLM),
- a mock summarizer function that uses simple, deterministic heuristics,
- docstrings, inline comments, and three test cases that print output.

Note: This is a mock summarizer for demonstration and testing only. It is NOT a replacement
for validated clinical NLP tools or clinical judgment.
"""


# Prompt template that you could send to a language model to get a structured summary.
PROMPT_TEMPLATE = """You are a clinical summarization assistant.
Input: A long unstructured doctor's clinical note.
Output: A concise, structured summary with these sections (omit any empty sections):
- Chief Complaint:
- History of Present Illness (1-2 short sentences):
- Key Vitals (if present):
- Medications (current):
- Allergies:
- Physical Exam (1 line summary):
- Assessment / Impression (single short phrase or ICD-like label if present):
- Plan (1-3 bullet points):
Keep each section short and focused. Use plain language suitable for handoff notes.
Limit overall output to roughly 6-10 short lines.
"""

def _split_sentences(text: str):
    """Very small sentence splitter based on punctuation."""
    # Keep parentheses content intact; simple split on punctuation followed by space/newline
    return [s.strip() for s in re.split(r'(?<=[\.\?\!])\s+', text.strip()) if s.strip()]

def _normalize_heading(h: str) -> str:
    """Map a detected heading token to one of our canonical fields."""
    h = h.lower().strip().rstrip(':').replace('-', ' ').strip()
    if any(k in h for k in ("chief complaint", "cc")):
        return "Chief Complaint"
    if any(k in h for k in ("history of present", "hpi", "history")):
        return "History of Present Illness"
    if any(k in h for k in ("vitals", "vs")):
        return "Key Vitals"
    if any(k in h for k in ("medications", "meds")):
        return "Medications"
    if any(k in h for k in ("allerg", "allergies")):
        return "Allergies"
    if any(k in h for k in ("exam", "physical")):
        return "Physical Exam"
    if any(k in h for k in ("assessment", "impression")):
        return "Assessment / Impression"
    if any(k in h for k in ("plan", "a/p")):
        return "Plan"
    return None

def summarize_clinical_note(note: str) -> Tuple[Dict[str, str], str]:
    """
    Summarize a clinical doctor's note into a short structured summary.

    This mock implementation:
    - Detects basic heading lines (e.g., "Assessment:", "Plan:", "Medications:") and groups content.
    - If headings are missing, uses keyword-based sentence extraction to populate fields.
    - Returns a tuple (summary_dict, formatted_summary_text).

    Parameters:
    - note: The raw clinical note text.

    Returns:
    - (summary_dict, formatted_text)
      summary_dict: mapping of canonical fields to short strings
      formatted_text: human-readable multi-line summary
    """
    # Normalize whitespace and split into lines for heading detection
    lines = [ln.rstrip() for ln in note.splitlines()]
    sections = {}
    current_key = None
    buffer = []

    # Heuristic: detect heading lines and accumulate subsequent lines until next heading
    for ln in lines + [""]:  # sentinel to flush last buffer
        stripped = ln.strip()
        # identify if this line begins with a known heading token (ends with ":" or is uppercase token)
        m = re.match(r'^([A-Za-z \-/]{2,40})(:|\-|\s*$)', stripped)
        heading_found = False
        if m:
            possible = m.group(1)
            canonical = _normalize_heading(possible)
            if canonical:
                # flush previous
                if current_key and buffer:
                    sections[current_key] = "\n".join(buffer).strip()
                    buffer = []
                current_key = canonical
                heading_found = True
                # if there is content on the same line after ":" capture it
                rest = re.split(r'[:\-]\s*', stripped, maxsplit=1)
                if len(rest) > 1 and rest[1].strip():
                    buffer.append(rest[1].strip())
                continue
        # if this line looks like a blank line and we currently have a buffer, keep it (paragraph separation)
        if current_key and not heading_found:
            if stripped == "" and buffer:
                buffer.append("")  # preserve blank as paragraph separator
            else:
                buffer.append(ln)
        else:
            # not under a detected heading; store raw for fallback extraction
            pass

    # flush final buffer
    if current_key and buffer:
        sections[current_key] = "\n".join(buffer).strip()

    # Prepare result fields and simple keyword-based fallback extraction
    result = {
        "Chief Complaint": "",
        "History of Present Illness": "",
        "Key Vitals": "",
        "Medications": "",
        "Allergies": "",
        "Physical Exam": "",
        "Assessment / Impression": "",
        "Plan": "",
    }

    # Fill any detected sections directly
    for k in list(result.keys()):
        if k in sections and sections[k].strip():
            # collapse whitespace and join into short phrases
            txt = re.sub(r'\s+', ' ', sections[k]).strip()
            # if too long, take first sentence
            sents = _split_sentences(txt)
            result[k] = sents[0] if sents else txt

    # If some fields are empty, try keyword sentence extraction from the whole note
    all_text = "\n".join(lines).strip()
    sentences = _split_sentences(all_text)

    def find_by_keywords(keywords):
        for s in sentences:
            low = s.lower()
            for kw in keywords:
                if kw in low:
                    return s
        return ""

    if not result["Chief Complaint"]:
        # often first sentence mentions reason
        result["Chief Complaint"] = sentences[0] if sentences else ""

    if not result["History of Present Illness"]:
        result["History of Present Illness"] = find_by_keywords(["history", "for", "since", "onset", "presenting with", "denies", "reports"]) or ""

    if not result["Key Vitals"]:
        vit = find_by_keywords(["bp ", "blood pressure", "hr ", "pulse", "temp", "temperature", "o2 ", "spo2"])
        result["Key Vitals"] = vit

    if not result["Medications"]:
        meds = find_by_keywords(["medication", "meds", "taking", "prescribed", "started on"])
        result["Medications"] = meds

    if not result["Allergies"]:
        alg = find_by_keywords(["allerg", "no known allergies", "nka", "nkda"])
        if alg:
            result["Allergies"] = alg

    if not result["Physical Exam"]:
        pe = find_by_keywords(["exam", "lungs", "cardiac", "abdomen", "extremities", "normal exam"])
        result["Physical Exam"] = pe

    if not result["Assessment / Impression"]:
        asmt = find_by_keywords(["impression", "assessment", "dx", "diagnos", "likely", "suspect", "probable", "differential"])
        result["Assessment / Impression"] = asmt

    if not result["Plan"]:
        pl = find_by_keywords(["plan", "will ", "restart", "start", "discussed", "recommend", "follow up", "refer"])
        result["Plan"] = pl

    # Final cleanup: shorten to 1-2 short sentences per field
    for k, v in result.items():
        if v:
            sents = _split_sentences(v)
            if len(sents) > 2:
                result[k] = " ".join(sents[:2])
            else:
                result[k] = v

    # Format a concise textual summary
    formatted_lines = []
    for k in result:
        if result[k]:
            formatted_lines.append(f"{k}: {result[k]}")
    formatted_text = "\n".join(formatted_lines)

    return result, formatted_text


# -------------------------
# Test cases and demonstration
# -------------------------
if __name__ == "__main__":
    notes = [
        # Test case 1: note with explicit headings
        """Chief Complaint: Shortness of breath.
History of Present Illness: 65-year-old male with 2 days of progressive dyspnea, worse with exertion, no chest pain. Reports cough and low-grade fever.
Vitals: Temp 100.4 F, HR 110, BP 140/85, SpO2 92% on room air.
Medications: Lisinopril 10 mg daily, Atorvastatin 20 mg nightly.
Allergies: NKDA.
Physical Exam: Tachycardic, bibasilar crackles.
Assessment: Acute decompensated heart failure vs. pneumonia.
Plan: Admit to observation, start diuretics, obtain chest x-ray and BNP, oxygen to keep SpO2 >94%.""",

        # Test case 2: freeform note without headings
        """Patient is a 29 yo female who presents for evaluation of recurrent headaches for the past 3 months. She reports daily morning headaches, occasionally associated with nausea, no focal weakness or vision loss. No known drug allergies. Current meds include OTC ibuprofen as needed. On exam, cranial nerves intact, normal fundi, mild tenderness over bilateral temples. Impression: probable tension-type headaches. Plan to start trial of regular sleep hygiene measures, trial of low-dose amitriptyline at bedtime, and neurology follow-up if no improvement.""",

        # Test case 3: terse ED note
        """40M s/p MVC. Alert, oriented. Vitals: BP 118/72, HR 88, RR 16, SpO2 99%. PE: Abdomen soft, tender RUQ. FAST negative. Labs: Hgb normal, CT abdomen shows small hepatic laceration. Assessment: minor liver laceration. Plan: observation, NPO, serial abdominal exams, repeat H/H q6h, surgery consult recommended if instability."""
    ]

    for i, note in enumerate(notes, 1):
        summary_dict, summary_text = summarize_clinical_note(note)
        print(f"\n--- Test case {i} summary ---")
        print(summary_text)