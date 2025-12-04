*Contact Form Setup Instructions (Flask/Python)
### Overview
This contact form system provides a dynamic, asynchronous solution for handling contact form submissions using Flask, Jinja2, and Flask-Mail. It uses AJAX to submit forms without page reloads and integrates securely with Gmail SMTP.

### Files Included
- app.py - Main application server and route handler
- config.py - Configuration file for email credentials
- email_utils.py - Helper logic for constructing and sending emails
- templates/contact.html - The frontend contact form (Jinja2 template)
- requirements.txt - List of Python dependencies
- CONTACT_FORM_SETUP.md - This setup guide

### Quick Setup
### 1. Gmail App Password Setup
    1. Go to your Google Account settings.
    2. Enable 2-Factor Authentication if not already enabled.
    3. Go to Security → 2-Step Verification → App passwords.
    4. Generate a new app password for "Mail" (name it "Flask App").
    5. Copy the 16-character password (remove spaces).

### 2. Install Dependencies
## Open your terminal in the project folder and run:
pip install -r requirements.txt
- (If you haven't created the file yet, run: pip install Flask Flask-Mail)

### 3. Update Configuration
# Edit config.py and replace the placeholder password:

# config.py
MAIL_PASSWORD = 'YOUR_APP_PASSWORD_HERE'

- With your actual 16-character Gmail app password:

MAIL_PASSWORD = 'qnluccxqzixlmtbq' 

### 4. Test the Form
    1. Run the server: python app.py
    2. Open your browser to: http://127.0.0.1:5000/contact
    3. Fill out the form and submit.
    4. Check the on-screen success message and your email inbox.

    ## Configuration Options
        # Email Settings (config.py)
            * MAIL_SERVER - SMTP server (default: smtp.gmail.com)
            * MAIL_PORT - SMTP port (default: 587)
            * MAIL_USERNAME - Your Gmail address (Sender)
            * MAIL_PASSWORD - Your Gmail App Password
            * RECIPIENT_EMAIL - Where to send form submissions

# Application Logic (app.py)
* Route: /contact handles both GET (display) and POST (submission) requests.
* Validation: Basic server-side validation checks for:
    * Name length (min 2 chars)
    * Email format (must contain '@')
    * Message length (min 10 chars)

### Troubleshooting
    ## Common Issues
        1. "AuthenticationError" (535)
            * Cause: You are using your normal Gmail login password.
            * Fix: You must use the 16-character App Password generated in Google Security settings.
            * Fix: Ensure 2-Factor Authentication is enabled on the Gmail account.

        2. "TemplateNotFound: contact.html"
            * Cause: Flask cannot find the HTML file.
            * Fix: Ensure contact.html is inside a folder named templates/ (case-sensitive).

        3. "BuildError: endpoint 'static'"
            * Cause: You likely have a typo in your HTML, such as url_for('staic', ...) instead of static.
            * Fix: Check your <img> and <link> tags in contact.html.

        4. Images Not Loading (404)
            * Cause: Images are not in the correct Flask directory.
            * Fix: Move your images folder inside the static folder.
            * Fix: Use Jinja2 syntax: <img src="{{ url_for('static', filename='images/logo.png') }}">

### Debug Mode
- Debug mode is enabled by default in app.py:


if __name__ == '__main__':
    app.run(debug=True)

- This allows you to see detailed error traces in your terminal/console window.

### Security Best Practices
    1. Environment Variables: In a real production environment, do not hardcode passwords in config.py. Use environment variables (e.g., os.environ.get('MAIL_PASSWORD')).
    2. Turn Off Debug: When going live, set debug=False.
    3. HTTPS: Always serve your Flask app over HTTPS in production.

### Customization
    ## Styling
        * Edit static/css/style.css to change the look.
        * Flask automatically serves files from the static folder.

    ## Email Template
        * Edit email_utils.py to change the layout of the email you receive.
        * You can add HTML to the msg.html property if you want rich-text emails.

### File Structure

your-project-folder/
│
├── app.py                  # Main Server Logic
├── config.py               # Email Credentials
├── email_utils.py          # Email Sending Logic
├── requirements.txt        # Python Dependencies
├── CONTACT_FORM_SETUP.md   # This file
│
├── templates/              # HTML Views
│   ├── contact.html
│   ├── header.html
│   └── footer.html
│
└── static/                 # Public Assets
    ├── css/
    ├── js/
    └── images/
- The contact form is now ready to use! Test it thoroughly locally before deploying to a production server.