from src.core.detectors import EXTENSION_TO_LANGUAGE

print("📊 Supported languages:")
print("=" * 40)

# Group of type
languages = {}

for ext, lang in EXTENSION_TO_LANGUAGE.items():
    if lang not in languages:
        languages[lang] = []
    languages[lang].append(ext)

# Displaying Statistics
for lang, exts in sorted(languages.items()):
    print(f"{lang}: {', '.join(exts)}")

print("\n" + "=" * 40)
print(f"Total languages: {len(languages)}")
print(f"Total extensions: {len(EXTENSION_TO_LANGUAGE)}")