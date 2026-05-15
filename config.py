"""
Configuration management for YouTube Video Automation
Handles all API keys and settings safely
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for all API keys and settings"""
    
    # API Keys (from GitHub Secrets or .env)
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    SYNTHESIA_API_KEY = os.getenv("SYNTHESIA_API_KEY")
    D_ID_API_KEY = os.getenv("D_ID_API_KEY")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    YOUTUBE_CREDENTIALS = os.getenv("YOUTUBE_CREDENTIALS")
    
    # API Endpoints
    DEEPSEEK_API_URL = "https://api.deepseek.com/v1"
    ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1"
    SYNTHESIA_API_URL = "https://api.synthesia.io/v1"
    D_ID_API_URL = "https://api.d-id.com/api/v1"
    NEWS_API_URL = "https://newsapi.org/v2"
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    
    # Settings
    VIDEO_DURATION = 60  # seconds
    VOICE_GENDER = "male"
    VIDEO_LANGUAGE = "en"
    UPLOAD_SCHEDULE = "0 0 */3 * *"  # Every 3 days
    
    @staticmethod
    def validate():
        """Validate that all required API keys are present"""
        required_keys = [
            "DEEPSEEK_API_KEY",
            "ELEVENLABS_API_KEY",
            "SYNTHESIA_API_KEY",
            "D_ID_API_KEY",
            "YOUTUBE_CREDENTIALS"
        ]
        
        missing_keys = []
        for key in required_keys:
            if not getattr(Config, key):
                missing_keys.append(key)
        
        if missing_keys:
            raise ValueError(f"Missing API keys: {', '.join(missing_keys)}")
        
        return True

if __name__ == "__main__":
    Config.validate()
    print("✅ All API keys configured correctly!")
