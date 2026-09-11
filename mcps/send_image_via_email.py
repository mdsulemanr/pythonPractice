import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def send_image_via_email(image_path: str, recipient: str):
    sender = "your_gmail@gmail.com"
    app_password = "your_16_char_app_password"  # not your real password

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = "AI Generated Image"
    msg.attach(MIMEText("Here is your generated image!", "plain"))

    # Attach the image
    with open(image_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename=generated_image.png")
        msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, app_password)
        server.sendmail(sender, recipient, msg.as_string())
        print(f"Email sent to {recipient}")