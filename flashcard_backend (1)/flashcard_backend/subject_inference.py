
def infer_subject(text: str) -> str:
    text = text.lower()
    keywords = {
        "Physics": ["force", "velocity", "acceleration", "newton", "energy", "mass"],
        "Biology": ["photosynthesis", "cell", "organism", "plant", "biology", "enzyme"],
        "Chemistry": ["atom", "molecule", "reaction", "chemical", "acid", "base"],
        "Mathematics": ["equation", "algebra", "calculus", "integral", "derivative"],
        "History": ["war", "revolution", "ancient", "historical", "empire", "king"]
    }
    for subject, words in keywords.items():
        if any(word in text for word in words):
            return subject
    return "General"
