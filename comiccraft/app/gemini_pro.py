import google.generativeai as genai, os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_story(outline, character):
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    combined = ""
    for p in outline:
        prompt = f"Write narration and dialogue for: {p['title']} - {p['scene_description']} with hero {character}. Short 2 lines."
        try:
            res = model.generate_content(prompt)
            combined += f"Panel {p['panel']}: {res.text}\n\n"
        except:
            combined += f"Panel {p['panel']}: {character} says 'What an adventure in {p['scene_description']}!'\n\n"
    return combined