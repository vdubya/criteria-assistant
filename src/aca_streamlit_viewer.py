import io

import streamlit as st
from lxml import etree
import pdfplumber
from docx import Document


@st.cache_data(show_spinner=False)
def extract_text_pdf(file: io.BytesIO) -> str:
    """Extract text from a PDF file"""
    text = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text.append(page_text)
    return "\n".join(text)


@st.cache_data(show_spinner=False)
def extract_text_docx(file: io.BytesIO) -> str:
    """Extract text from a DOCX file"""
    doc = Document(file)
    return "\n".join(p.text for p in doc.paragraphs)


@st.cache_data(show_spinner=False)
def extract_text_sec(file: io.BytesIO) -> str:
    """Extract text from a UFGS XML SEC file"""
    tree = etree.parse(file)
    return " ".join(tree.itertext())


def highlight_text(text: str, highlights):
    """Apply HTML highlight spans to text for active highlights"""
    import re

    def apply(match, color):
        return f"<mark style='background-color:{color};'>{match.group(0)}</mark>"

    for hl in highlights:
        if not hl.get("enabled", True) or not hl.get("query"):
            continue
        pattern = re.escape(hl["query"])
        text = re.sub(pattern, lambda m: apply(m, hl["color"]), text, flags=re.IGNORECASE)
    return text


def sidebar_controls():
    st.sidebar.header("Document Upload")
    uploaded = st.sidebar.file_uploader("Upload PDF, Word, or SEC XML", type=["pdf", "docx", "xml", "sec"])

    st.sidebar.header("Search/Highlight")
    if "highlights" not in st.session_state:
        st.session_state.highlights = []

    with st.sidebar.form("add_highlight"):
        query = st.text_input("Keyword")
        color = st.color_picker("Color", "#ffff00")
        submitted = st.form_submit_button("Add")
        if submitted and query:
            st.session_state.highlights.append({"query": query, "color": color, "enabled": True})

    if st.session_state.highlights:
        st.sidebar.subheader("Active Highlights")
    for i, hl in enumerate(st.session_state.highlights):
        cols = st.sidebar.columns([1, 2, 1])
        enabled = cols[0].checkbox("", value=hl.get("enabled", True), key=f"enable_{i}")
        query = cols[1].text_input("", value=hl["query"], key=f"query_{i}")
        cols[2].color_picker("", value=hl["color"], key=f"color_{i}")
        hl.update({"enabled": enabled, "query": query, "color": st.session_state[f"color_{i}"]})
    return uploaded


def main():
    st.title("ACA Viewer")
    uploaded = sidebar_controls()

    if uploaded:
        if uploaded.name.lower().endswith(".pdf"):
            text = extract_text_pdf(uploaded)
        elif uploaded.name.lower().endswith(".docx"):
            text = extract_text_docx(uploaded)
        else:
            text = extract_text_sec(uploaded)

        html_text = highlight_text(st.session_state.get("document_text", text), st.session_state.highlights)
        st.session_state.document_text = text
        st.markdown(html_text, unsafe_allow_html=True)

        st.header("Add Comment")
        comment = st.text_area("Selected text")
        note = st.text_input("Comment")
        if st.button("Save Comment") and comment:
            if "comments" not in st.session_state:
                st.session_state.comments = []
            st.session_state.comments.append({"text": comment, "comment": note})

        if st.session_state.get("comments"):
            st.subheader("Comments")
            for c in st.session_state.comments:
                st.write(f"**{c['text']}**: {c['comment']}")


if __name__ == "__main__":
    main()
