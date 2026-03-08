Process Monitor using Python

#Project Overview

This project is a **Python automation script** that monitors running processes on a system and stores the information in a log file. The script uses the **psutil library** to collect process details such as Process ID, name, username, and memory usage.

The program automatically creates log files at a specified time interval and stores them in a folder.

---

# Features

* Monitor all running system processes
* Capture Process ID (PID)
* Capture Process Name
* Capture Username running the process
* Capture Virtual Memory Size (VMS)
* Automatically generate log files
* Scheduled monitoring using the `schedule` module

---

#Technologies Used

* Python
* `psutil` module
* `schedule` module
* `os` module
* `time` module

---

#Project Structure

ProcessMonitor
│
├── SystemProcessMonitor.py
└── README.md

---

#How the Script Works

1. The user provides:
   * Folder name for log files
   * Time interval in minutes
2. The script scans all running processes.
3. Process information is collected using the `psutil` library.
4. The data is written into a log file.
5. The program repeats the process automatically after the given interval.

---

#How to Run the Program

#Step 1: Install Required Libraries

  pip install psutil schedule

#Step 2: Run the Script

  python SystemProcessMonitor.py

### Step 3: Provide Inputs

  Enter folder name for logs
  Enter time interval (in minutes)

Example:

  Logs
  5

This will create a **log file every 5 minutes** in the `Logs` folder.

---

#Example Log Output

--------------------------------------------------------------------------------
        Marvellous Infosystems Process Log
        Log file is created at : Sun Mar 08 18:00:00 2026
--------------------------------------------------------------------------------

{'pid': 1024, 'name': 'python.exe', 'username': 'user', 'vms': 120.5}

{'pid': 3048, 'name': 'chrome.exe', 'username': 'user', 'vms': 450.3}
--------------------------------------------------------------------------------

---

#Applications

* System process monitoring
* Detecting high memory usage processes
* System administration automation
* Learning Python system programming

---

This project is created for educational purposes.