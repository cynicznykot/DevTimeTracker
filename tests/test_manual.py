from src.core.detectors import detect_editor, extract_filename, detect_language

test_cases = [
    ("main.py - PyCharm", "PyCharm", "main.py", "Python"),
    ("index.js — Visual Studio Code", "VS Code", "index.js", "JavaScript"),
    ("Program.cs - Microsoft Visual Studio", "Visual Studio", "Program.cs", "C#"),
    ("Dockerfile - VS Code", "VS Code", "Dockerfile", "Dockerfile"),
    ("Makefile - VS Code", "VS Code", "Makefile", "Makefile"),
    ("CMakeLists.txt - VS Code", "VS Code", "CMakeLists.txt", "CMake"),
    ("Untitled-1 - PyCharm", "PyCharm", None, None),
    ("Calculator", None, None, None),
]

print("🧪 Testing detectors.py")
print("=" * 60)

all_passed = True

for title, exp_editor, exp_file, exp_lang in test_cases:
    editor = detect_editor(title)
    filename = extract_filename(title)
    language = detect_language(title)

    editor_ok = editor == exp_editor
    file_ok = filename == exp_file
    lang_ok = language == exp_lang

    if not (editor_ok and file_ok and lang_ok):
        all_passed = False

    print(f"\n 📄 Title: {title}")
    print(f" {'✅' if editor_ok else '❌'} Editor: {editor} (Expectation: {exp_editor})")
    print(f" {'✅' if file_ok else '❌'} File: {filename} (Expectation: {exp_file})")
    print(f" {'✅' if lang_ok else '❌'} Language: {language} (Expectation: {exp_lang})")

print("\n" + "=" * 60)

if all_passed:
    print("✅ ALL TESTS WENT COMPLETE!")
else:
    print("❌ HAVE ERRORS!")