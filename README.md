# 🚀 Web Automation Task

This project automates web interactions using **Selenium**, logging into a demo website, filling out a form, and submitting it. The script is scheduled to run automatically every day at **10:00 AM** using **Windows Task Scheduler**.

## 📌 Installation

1. **Extract the project or clone the repository:**
   ```sh
   git clone https://github.com/KozimovBekzodbek/AutomateLoggingToWebsite.git
   cd web-automation
   ```

2. **Create and activate a virtual environment:**
   - **Windows:**
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Schedule the automation task (runs daily at 10:00 AM):**
   ```sh
   python setup.py
   ```

## 🚀 Running the Script

- **Manually execute the script:**
  ```sh
  python program.py
  ```
- **Run the scheduled task manually:**
  ```sh
  schtasks /run /tn "Web Automation Task"
  ```

## ❌ Removing the Scheduled Task

To stop the automatic execution, run:
```sh
schtasks /delete /tn "Web Automation Task" /f
```

## 🛠 Troubleshooting

### ✅ The script runs but only opens and closes the terminal
- Check if the task exists:
  ```sh
  schtasks /query /tn "Web Automation Task"
  ```
- Modify `setup.py` to add a **delay** before execution:
  ```python
  command = f'schtasks /create /tn "{task_name}" /tr "cmd.exe /c timeout 5 && cd /d "{base_dir}" && "{venv_python}" "{script_path}"' /sc daily /st 10:00 /f'
  ```

### ✅ The script fails due to incorrect paths
- Ensure `setup.py` correctly retrieves the script’s directory:
  ```python
  base_dir = os.path.dirname(os.path.abspath(__file__))
  ```

## 📌 Technologies Used
- **Python**
- **Selenium**
- **Windows Task Scheduler**
- **Virtual Environment**

## 👨‍💻 Author
Your Name | [GitHub Profile](https://github.com/KozimovBekzodbek)
