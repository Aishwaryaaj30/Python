Duplicate File Remover 

#Overview

Duplicate File Remover is a Python automation script that scans a directory and its subdirectories to find duplicate files using an **MD5 checksum algorithm**. The script identifies files with identical content and deletes the duplicate copies while keeping one original file.

This helps free disk space and keeps directories organized.

---

# Features

* Scan directories recursively
* Detect duplicate files using MD5 hash
* Display duplicate files
* Automatically delete duplicate copies
* Command line argument support
* Simple and efficient Python automation script

---

# Technologies Used

* Python
* `os` module
* `sys` module
* `hashlib` module
* `time` module

---

#Project Structure

DuplicateFileRemover
│
├── DeleteDuplicateFile.py
└── README.md


---

#How the Script Works

1. The program scans the specified directory.
2. It generates an **MD5 checksum** for each file.
3. Files with the same checksum are considered duplicates.
4. The program keeps one file and deletes the remaining duplicate files.

---

#Command Line Options

| Command | Description   |
| ------- | ------------- |
| `--h`   | Display help  |
| `--u`   | Display usage |

Example:

python DeleteDuplicateFile.py --h

---

#Example Output

Deleted File : copy1.txt
Deleted File : copy2.txt
Total Deleted file : 2

---

#Applications

* Remove duplicate documents
* Clean duplicate images and videos
* Save storage space
* File system organization

---

This project is created for educational and learning purposes.