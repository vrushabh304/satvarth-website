# newsletter_utils.py

from flask_mail import Message

def send_newsletter_email(mail, admin_email, user_email):
    """
    Sends two emails:
    1. To admin -> informing a new subscriber joined.
    2. To user -> thank you email.
    """

    # Email to YOU (admin)
    admin_msg = Message(
        subject="New Newsletter Subscriber",
        recipients=[admin_email],
        body=f"A new user subscribed:\n\nEmail: {user_email}"
    )
    mail.send(admin_msg)

    # Thank-you email to USER
    user_msg = Message(
        subject="Thank You for Subscribing!",
        recipients=[user_email],
        body=(
            "Hi,\n\n"
            "Thank you for subscribing to our newsletter.\n"
            "We will contact you with updates soon.\n\n"
            "Regards,\nSatvarth Team"
        )
    )
    mail.send(user_msg)
