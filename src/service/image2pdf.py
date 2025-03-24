from pathlib import Path
from typing import List
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import io


def images_to_pdf(image_paths: List[Path]) -> bytes:
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    for img_path in image_paths:
        with Image.open(img_path) as img:
            img_width, img_height = img.size
            aspect = img_height / img_width

            new_width = width
            new_height = width * aspect
            if new_height > height:
                new_height = height
                new_width = height / aspect

            x = (width - new_width) / 2
            y = (height - new_height) / 2

            img_buffer = io.BytesIO()
            img.convert("RGB").save(img_buffer, format="JPEG")
            img_buffer.seek(0)

            c.drawImage(
                ImageReader(img_buffer), x, y, width=new_width, height=new_height
            )
            c.showPage()

    c.save()
    buffer.seek(0)
    return buffer.getvalue()


def generate_pdf_from_folder(folder_path: Path, output_pdf_path: Path):
    image_paths = sorted(
        [
            p
            for p in folder_path.iterdir()
            if p.suffix.lower() in [".png", ".jpg", ".jpeg", ".bmp", ".gif"]
        ]
    )

    if not image_paths:
        raise ValueError("No images found in the provided folder.")

    pdf_content = images_to_pdf(image_paths)

    with open(output_pdf_path, "wb") as f:
        f.write(pdf_content)
