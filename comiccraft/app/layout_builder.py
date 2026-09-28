def build_comic_layout(outline, story_text, image_paths):
    layout = []
    stories = story_text.split("\n\n")
    for i, panel in enumerate(outline):
        layout.append({
            "panel": panel['panel'],
            "title": panel['title'],
            "scene_description": panel['scene_description'],
            "image_path": image_paths[i] if i < len(image_paths) else "",
            "text": stories[i] if i < len(stories) else panel['scene_description']
        })
    return layout