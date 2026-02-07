# FileOrganizer
File Organiser
A simple yet powerful Python script that brings order to your chaos by organizing your Downloads folder (or any target directory) based on file extensions.

🚀 Features
Automatically sorts files into the following categories:

Images: .jpg, .jpeg, .png, .gif, .svg
Documents: .pdf, .docx, .txt, .xlsx, .pptx
Videos: .mp4, .mov, .avi, .mkv
Music: .mp3, .wav, .flac
Archives: .zip, .rar, .7z
Installers: .exe, .msi
🛠️ Usage
Clone the repository:

git clone https://github.com/sameer-codes01/FileOrganizer.git
cd file-organiser
Run the script:

python file.py
The script will scan your ~/Downloads folder and move files into subfolders named after their category (e.g., Downloads/Images, Downloads/Documents).

⚙️ Customization
You can easily add new file types or categories by editing the file_types dictionary in file.py:

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    # Add your own:
    "Code": [".py", ".js", ".html", ".css"],
}
📋 Requirements
Python 3.x
No external dependencies required (uses standard os and shutil libraries).
