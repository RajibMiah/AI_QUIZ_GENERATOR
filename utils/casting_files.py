from PIL import Image

import re


def generate_pil_image(images):
    ptl_images = []

    for img in images:
        ptl_images.append(Image.open(img))

    return ptl_images;

import re

import re

def normalize_math(text):

    # --- Fractions ---
    text = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', text)

    # --- Integrals / sums ---
    text = re.sub(r'\\int', 'integral', text)
    text = re.sub(r'\\sum', 'sum', text)

    # --- Roots ---
    text = re.sub(r'\\sqrt\{([^}]+)\}', r'sqrt(\1)', text)

    # --- Greek letters ---
    greek = {
        r'\\alpha': 'alpha',
        r'\\beta': 'beta',
        r'\\gamma': 'gamma',
        r'\\pi': 'pi',
        r'\\theta': 'theta',
    }
    for k, v in greek.items():
        text = re.sub(k, v, text)

    # --- Core math symbols ---
    text = text.replace('×', '*')
    text = text.replace('÷', '/')
    text = text.replace('≤', '<=')
    text = text.replace('≥', '>=')
    text = text.replace('≠', '!=')

    # --- Real number spaces ---
    text = re.sub(r'\bR\^2\b', '2D real coordinate space (R²)', text)
    text = re.sub(r'\bR\b', 'real number set', text)

    # --- Set membership ---
    text = re.sub(r'∈', 'belongs to', text)

    # --- Coordinate interpretation ---
    def coord_expander(match):
        x, y = match.group(1), match.group(2)
        return f"Point ({x},{y}) in 2D Cartesian coordinate system"

    text = re.sub(r'\((\d+)\s*,\s*(\d+)\)', coord_expander, text)

    # --- Math delimiters ---
    text = re.sub(r'\$(.*?)\$', r'\1', text)
    text = re.sub(r'\$\$(.*?)\$\$', r'\1', text, flags=re.DOTALL)

    return text

    return text

def make_plain_text(text):
    # Remove headers (#, ##, ###, etc.)
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    
    # Remove bold and italic (*, **, _, __)
    text = re.sub(r'(\*\*|\*|__|_)', '', text)
    
    # Remove inline code (`code`)
    text = re.sub(r'`([^`]*)`', r'\1', text)
    
    # Remove links [text](url) → text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    
    # Remove images ![alt](url) → alt
    text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', text)
    
    # Remove blockquotes (>)
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    
    # Remove unordered list markers (-, *, +)
    text = re.sub(r'^[-*+]\s+', '', text, flags=re.MULTILINE)
    
    # Remove ordered list numbers (1. 2. etc.)
    text = re.sub(r'^\d+\.\s+', '', text, flags=re.MULTILINE)

    # --- Math normalization ---
    text = normalize_math(text)
    
    return text