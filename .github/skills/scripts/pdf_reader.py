#!/usr/bin/env python3
"""
PDF Reader Utility for Advanced ML Skills

This module provides functionality to extract text from PDF files and parse
exercise questions from course materials. It handles PDF text extraction and
provides utilities for finding specific questions and sections.

Functions:
    read_pdf_text(pdf_path): Extract all text from a PDF file
    extract_question_text(pdf_text, question_number): Find specific question text
    extract_all_questions(pdf_text): Extract all questions from PDF
    find_exercise_section(pdf_text): Locate programming exercises section
"""

import re
from pathlib import Path


def read_pdf_text(pdf_path):
    """
    Extract text from a PDF file.
    
    Uses PyPDF2 to extract text from the PDF. If PyPDF2 is not available,
    falls back to trying pypdf or raises an error.
    
    Args:
        pdf_path (str or Path): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF
        
    Raises:
        FileNotFoundError: If PDF file does not exist
        ImportError: If no PDF library is available
    """
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        try:
            from pypdf import PdfReader
        except ImportError:
            raise ImportError(
                "No PDF reading library available. Please install PyPDF2 or pypdf:\n"
                "  pip install PyPDF2"
            )
    
    text = []
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text.append(page.extract_text())
    
    return '\n'.join(text)


def extract_question_text(pdf_text, question_number):
    """
    Extract text for a specific question from PDF text.
    
    Searches for a question by number (e.g., "3.4", "1.2") and returns
    the question text along with any subquestions or details.
    
    Args:
        pdf_text (str): Full text extracted from PDF
        question_number (str): Question identifier (e.g., "3.4", "1.2")
        
    Returns:
        str or None: Question text if found, None otherwise
    """
    # Normalize question number format
    question_number = str(question_number).strip()
    
    # Try multiple patterns
    patterns = [
        rf'Exercise\s+{re.escape(question_number)}[:\s]+(.*?)(?=Exercise\s+[\d.]+|$)',
        rf'Question\s+{re.escape(question_number)}[:\s]+(.*?)(?=Question\s+[\d.]+|$)',
        rf'{re.escape(question_number)}\s+[A-Z](.*?)(?=[\d.]+\s+[A-Z]|$)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, pdf_text, re.DOTALL | re.IGNORECASE)
        if match:
            text = match.group(1).strip()
            # Clean up excessive whitespace
            text = re.sub(r'\s+', ' ', text)
            return text
    
    return None


def extract_all_questions(pdf_text):
    """
    Extract all questions from PDF text.
    
    Identifies all question numbers and their associated text from the PDF.
    
    Args:
        pdf_text (str): Full text extracted from PDF
        
    Returns:
        dict: Mapping of question numbers to question text
              e.g., {'1.1': 'question text...', '1.2': 'question text...'}
    """
    questions = {}
    
    # Pattern to find questions: "Exercise X.Y" or "Question X.Y" or "X Y"
    pattern = r'(?:Exercise|Question)\s+([\d.]+)\s*[:\-]?\s*([^\n]*?)(?=(?:Exercise|Question)\s+[\d.]+|$)'
    
    matches = re.finditer(pattern, pdf_text, re.DOTALL | re.IGNORECASE)
    for match in matches:
        q_num = match.group(1)
        q_text = match.group(2).strip()
        # Limit to first 200 chars of question text for the map
        q_text = re.sub(r'\s+', ' ', q_text)[:200]
        questions[q_num] = q_text
    
    return questions


def find_exercise_section(pdf_text):
    """
    Locate the programming exercises section if present.
    
    Searches for section headers like "Programming exercises" and returns
    the text starting from that section.
    
    Args:
        pdf_text (str): Full text extracted from PDF
        
    Returns:
        str: Text from the exercise section onwards, or original text if not found
    """
    patterns = [
        r'Programming exercises',
        r'Programming Exercises',
        r'programming exercises',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, pdf_text, re.IGNORECASE)
        if match:
            return pdf_text[match.start():]
    
    return pdf_text


def extract_theoretical_vs_programming(pdf_text):
    """
    Separate theoretical and programming exercises.
    
    Returns a tuple of (theoretical_questions, programming_questions).
    Looks for section headers to distinguish between exercise types.
    
    Args:
        pdf_text (str): Full text extracted from PDF
        
    Returns:
        tuple: (theoretical_questions_dict, programming_questions_dict)
    """
    theoretical = {}
    programming = {}
    
    # Split by exercise sections
    theoretical_match = re.search(r'(?:Theoretical|Theory)\s+(?:exercises|Exercises)', 
                                  pdf_text, re.IGNORECASE)
    programming_match = re.search(r'Programming\s+(?:exercises|Exercises)', 
                                  pdf_text, re.IGNORECASE)
    
    # Extract questions from appropriate sections
    all_questions = extract_all_questions(pdf_text)
    
    if theoretical_match and programming_match:
        # Split point: if question number appears before programming section, it's theoretical
        programming_start = programming_match.start()
        
        for q_num, q_text in all_questions.items():
            # This is a simplified heuristic; for production use more sophisticated parsing
            if any(re.search(rf'{re.escape(q_num)}', pdf_text[:programming_start])):
                theoretical[q_num] = q_text
            else:
                programming[q_num] = q_text
    else:
        # If we can't distinguish, return all as unknown
        return theoretical, programming
    
    return theoretical, programming


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python pdf_reader.py <pdf_path> [question_number]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    
    try:
        text = read_pdf_text(pdf_path)
        
        if len(sys.argv) > 2:
            # Extract specific question
            question = sys.argv[2]
            q_text = extract_question_text(text, question)
            if q_text:
                print(f"Question {question}:")
                print(q_text)
            else:
                print(f"Question {question} not found")
        else:
            # List all questions
            questions = extract_all_questions(text)
            print("Questions found:")
            for q_num in sorted(questions.keys(), 
                               key=lambda x: tuple(map(int, x.split('.')))):
                print(f"  {q_num}: {questions[q_num][:100]}...")
                
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ImportError as e:
        print(f"Error: {e}")
        sys.exit(1)
