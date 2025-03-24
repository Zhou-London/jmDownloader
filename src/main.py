from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from service.image2pdf import generate_pdf_from_folder
from service.jm_service import jmcomic_agent

app = FastAPI()

ASSETS_PATH = Path("assets")


# Return a PDF of album
@app.get("/get/{folder_name}")
async def generate_pdf(folder_name: str):

    # Fetch the file
    try:
        response = jmcomic_agent.fetch(folder_name)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Can not download this album, take up your pants!!: {str(e)}",
        )

    # Check the file
    folder_path = ASSETS_PATH / folder_name
    if not folder_path.exists() or not folder_path.is_dir():
        raise HTTPException(status_code=404, detail="Download Failed!")

    output_pdf_path = folder_path / f"{folder_name}.pdf"

    # Generate PDF
    try:
        generate_pdf_from_folder(folder_path, output_pdf_path)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=f"Convert to Pdf Failed: {str(e)}")

    # Success
    return FileResponse(
        output_pdf_path, media_type="application/pdf", filename=f"{folder_name}.pdf"
    )
