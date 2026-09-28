import google.generativeai as genai
import os, json

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_outline(prompt, character, setting, tone):
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    full_prompt = f"""
    Create 5 panel comic outline. Story: {prompt}, Character: {character}, Setting: {setting}, Tone: {tone}.
    Return ONLY JSON list like: [{{"panel":1, "title":"...", "scene_description":"...", "image_prompt":"{character} in {setting}, comic style"}}]
    """
    try:
        res = model.generate_content(full_prompt)
        text = res.text.replace("```json","").replace("```","").strip()
        return json.loads(text)
    except:
        # Fallback dummy data - API key illana kooda output varum
        return [
            {"panel": i, "title": f"Panel {i}: {character}'s Adventure",
             "scene_description": f"Our hero {character} in {setting}. {prompt}",
             "image_prompt": f"{character} in {setting}, {tone} comic book style, vibrant"}
            for i in range(1,6)
        ]