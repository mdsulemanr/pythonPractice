import os
# from fastmcp
import requests, io, smtplib
from PIL import Image
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

from mcp.server import FastMCP

mcp = FastMCP("image-emailer")

HF_TOKEN = os.environ["HF_TOKEN"]
GMAIL = "mdsulemanr@gmail.com"
APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]


@mcp.tool()
def generate_and_email_image(prompt: str, recipient_email: str) -> str:
    """Generate an image from a prompt and email it to the recipient."""

    # Step 1: Generate image
    api_url = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"
    response = requests.post(api_url,
        headers={"Authorization": f"Bearer {HF_TOKEN}"},
        json={"inputs": prompt})

    image = Image.open(io.BytesIO(response.content))
    image_path = "C:/Users/Dell/Pictures/mcp-mages/generated_image.png"
    image.save(image_path)

    # Step 2: Email it
    msg = MIMEMultipart()
    msg["From"] = GMAIL
    msg["To"] = recipient_email
    msg["Subject"] = "Your AI Generated Image"
    msg.attach(MIMEText(f'Generated from prompt: "{prompt}"', "plain"))

    with open(image_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename=generated_image.png")
        msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL, APP_PASSWORD)
        server.sendmail(GMAIL, recipient_email, msg.as_string())

    return f"Image generated and emailed to {recipient_email}"

if __name__ == "__main__":
    mcp.run()
    # result = generate_and_email_image(
    #     prompt="A Pakistani school boy of class 6th wearing casual dress, holding a medal on the beach",
    #     recipient_email="mdsulemanr@gmail.com"
    # )
    # print(result)