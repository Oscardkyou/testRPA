TARGET_DIR = "test_dir"

IMAGES = (".jpeg", ".png", ".jpg", ".gif", ".bmp", ".svg", ".tiff", ".heic", ".webp")
TEXT = (".txt", ".rtf", ".md")
VIDEO = (".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".ogg", ".webm")
AUDIO = (".mp3", ".wav", ".m4a", ".flac")
APPLICATIONS = (".exe", ".lnk", ".msi", ".app")
CODE = (".cpp", ".hpp", ".asm", ".js", ".html", ".css", ".scss", ".sass", ".php", ".ts", ".c", ".h", ".pch", ".o", ".a", ".java", ".rb", ".rs", ".py", ".pyw", ".ipynb", ".cs", ".vs", ".xcodeproj")
INSTALL = (".dmg", ".pkg", ".deb", ".rpm")
COMPRESSED = (".zip", ".rar", ".tar", ".gz", ".7z")
DOCUMENTS = (".doc", ".pdf", ".docx", ".ppt", ".pptx", ".odt", ".ods", ".xls", ".xlsx", ".csv", ".dat", ".db", ".dbf", ".log", ".mdb", ".sav", ".sql", ".json", ".xml")
OTHER = ("",)

file_extensions = {
    IMAGES: "Images",
    TEXT: "Text",
    VIDEO: "Video",
    AUDIO: "Audio",
    APPLICATIONS: "Applications",
    CODE: "Code",
    INSTALL: "Install",
    COMPRESSED: "Compressed",
    DOCUMENTS: "Documents",
    OTHER: "Other"
}

MAKEFILE = "makefile"
OTHER_STR = "Other"
ERROR_MSG = f"[{TARGET_DIR} directory not found]\n"

