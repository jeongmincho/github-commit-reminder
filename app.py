import os
import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import pytz

# Email Customization Settings
EMAIL_CONFIG = {
    'from_name': 'Git Commit Police 👮',
    'subject': 'GitHub Commit Reminder',
    'template': "Just a friendly reminder that you haven't made any GitHub commits today. It's currently {time}!"
}

def check_github_commits():
    load_dotenv()
    
    # Configuration
    github_token = os.getenv('GITHUB_TOKEN')
    github_username = os.getenv('GITHUB_USERNAME')
    email_sender = os.getenv('EMAIL_SENDER')
    email_password = os.getenv('EMAIL_PASSWORD')
    email_recipient = os.getenv('EMAIL_RECIPIENT')
    
    # Get today's date in ISO format
    eastern = pytz.timezone('America/New_York')
    now = datetime.now(eastern)
    today = now.date().isoformat()
    
    # GitHub API endpoint
    url = f'https://api.github.com/search/commits'
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.cloak-preview'
    }
    params = {
        'q': f'author:{github_username} committer-date:{today}',
        'sort': 'committer-date',
        'order': 'desc'
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        commit_count = response.json()['total_count']
        
        print(f"Commits made today: {commit_count}")
        
        # If no commits found, send email
        if commit_count == 0:
            print("No commits found today. Sending email...")
            msg = MIMEMultipart()
            msg['From'] = f'"{EMAIL_CONFIG["from_name"]}" <{email_sender}>'
            msg['To'] = email_recipient
            msg['Subject'] = EMAIL_CONFIG['subject']
            
            current_time = now.strftime("%I:%M %p")
            body = EMAIL_CONFIG['template'].format(time=current_time)
            msg.attach(MIMEText(body, 'plain'))
            
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email_sender, email_password)
                text = msg.as_string()
                server.sendmail(email_sender, email_recipient, text)
                server.quit()
                print("Email sent successfully!")
            except Exception as e:
                print(f"Error sending email: {str(e)}")
        else:
            print(f"You've made {commit_count} commits today - no reminder needed!")
            
    except requests.exceptions.RequestException as e:
        print(f"Error checking commits: {str(e)}")

if __name__ == "__main__":
    check_github_commits()
