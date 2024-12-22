# GitHub Commit Email Reminder Script

A simple Python script that checks if you've made any GitHub commits today and sends you an email reminder if you haven't. Built with the intention to help you maintain a daily coding habit and stay accountable.

## Features
- Checks your GitHub commits for the current day
- Sends an email reminder if no commits are found
- Easily customizable email content through `EMAIL_CONFIG` at the top of `app.py`:
  ```python
  EMAIL_CONFIG = {
      'from_name': 'Git Commit Police 👮',  # Change the sender's display name
      'subject': 'GitHub Commit Reminder',   # Change the email subject
      'template': "Just a friendly reminder."  # Change the email message
  }
  ```

## How to use

### 1. Python Setup
Make sure you have Python 3.x installed. You can check by running:
```bash
python3 --version
```

Create and activate a virtual environment (recommended):
```bash
# Create a virtual environment
python3 -m venv venv

# Activate it on macOS/Linux
source venv/bin/activate

# Activate it on Windows
# venv\Scripts\activate
```

Your terminal prompt should change to indicate you're in the virtual environment, like: `(venv) $`

### 2. Install Dependencies
With your virtual environment activated:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Create a `.env` file with your credentials:
```
GITHUB_TOKEN=your_github_token
GITHUB_USERNAME=your_github_username
EMAIL_SENDER=your_gmail_address
EMAIL_PASSWORD=your_gmail_app_password
EMAIL_RECIPIENT=recipient_email_address
```

Required credentials:
- `GITHUB_TOKEN`: Create a personal access token at https://github.com/settings/tokens
  - Select the `repo` scope when creating the token
- `GITHUB_USERNAME`: Your GitHub username
- `EMAIL_SENDER`: Your Gmail address
- `EMAIL_PASSWORD`: Your Gmail app-specific password (Generate at https://myaccount.google.com/apppasswords)
- `EMAIL_RECIPIENT`: Email address where you want to receive notifications

### 4. Run the Script
With your virtual environment still activated:
```bash
python3 app.py
```

To deactivate the virtual environment when you're done:
```bash
deactivate
```

### 5. Automated Daily Checks (Recommended)
For automatic daily checks, deploy to [Render](https://render.com) as a background worker with a cron job scheduled for your preferred time (e.g., 10 PM PST). This ensures you get reminders without having to run the script manually.

## Troubleshooting
Make sure to use an app-specific password for Gmail, as regular passwords won't work with SMTP.
