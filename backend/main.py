from fastapi import FastAPI, File
from PIL import Image
import io
from transformers import ViTImageProcessor, ViTForImageClassification

# 设置本地模型路径
model_path = r"C:\models\google-vit-base-patch16-224"

processor = ViTImageProcessor.from_pretrained(model_path)
model = ViTForImageClassification.from_pretrained(model_path)

app = FastAPI()

@app.post("/predict")
async def predict(image: bytes=File(...)):
    img = Image.open(io.BytesIO(image)).convert('RGB')
    inputs = processor(images=img, return_tensors="pt")
    outputs = model(**inputs)
    predicted_label = model.config.id2label[outputs.logits.argmax().item()]
    return {"result": predicted_label}