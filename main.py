from fastapi import FastAPI, Request
from fastapi.responses import Response
from rembg import remove
from PIL import Image
import io

app = FastAPI()

@app.post("/remove-background")
async def remove_background_binary(request: Request):
    # อ่าน binary จาก body โดยตรง
    input_bytes = await request.body()
    input_image = Image.open(io.BytesIO(input_bytes)).convert("RGBA")

    # ลบพื้นหลัง
    output_image = remove(input_image)

    # บันทึกลง buffer
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    buf.seek(0)

    # ส่งกลับเป็น binary
    return Response(content=buf.getvalue(), media_type="image/png")
