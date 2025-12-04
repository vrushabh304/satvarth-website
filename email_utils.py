# email_utils.py
from flask_mail import Message
from flask import jsonify

def send_contact_email(mail, recipient, data):
    """
    Handles the logic of building and sending the email.
    Args:
        mail: The Flask-Mail instance
        recipient: The email address to send to
        data: A dictionary containing form data (name, email, phone, etc.)
    """
    try:
        # 1. Prepare the subject
        msg_subject = f"Contact Form: {data.get('subject', 'New Submission')}"
        
        # 2. Create the message object
        msg = Message(subject=msg_subject, recipients=[recipient])
        
        # 3. Create the email body
        msg.body = f"""
        New Contact Form Submission
        ---------------------------
        Name:    {data.get('name')}
        Email:   {data.get('email')}
        Phone:   {data.get('phone')}
        Subject: {data.get('subject')}
        
        Message:
        {data.get('message')}
        """
        
        # 4. Send the email
        mail.send(msg)
        
        return {'success': True, 'message': 'Thank you! Your message has been sent successfully.'}

    except Exception as e:
        print(f"Email Error: {e}")  # Print error to console for debugging
        return {'success': False, 'message': 'Error sending message. Please try again later.'}