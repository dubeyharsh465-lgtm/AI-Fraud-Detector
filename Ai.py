from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import base64

app = FastAPI()

# ✅ Enable CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "sk_test_123456789"


# ✅ GET route only for browser testing
@app.get("/api/voice-detection")
def info():
    return {"message": "Use POST request with Base64 MP3 audio"}


# ✅ POST route for real detection
@app.post("/api/voice-detection")
def detect_voice(data: dict, x_api_key: str = Header(None)):

    # 🔐 API Key Validation
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    # Extract fields
    language = data.get("language")
    audio_base64 = data.get("audioBase64")

    if not audio_base64:
        return {"status": "error", "message": "Audio missing"}

    # Decode Base64 audio and save MP3
    audio_bytes = base64.b64decode(audio_base64)

    with open("sample.mp3", "wb") as f:
        f.write(audio_bytes)

    # ⚡ Dummy Prediction (Temporary)
    return {
        "status": "success",
        "language": language,
        "classification": "AI_GENERATED",
        "confidenceScore": 0.85,
        "explanation": "Robotic voice pattern detected"
    }
