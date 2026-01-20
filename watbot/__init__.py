"""
WATBOT - WhatsApp & Instagram Automation Bot Library
Automate WhatsApp and Instagram with AI-powered responses
"""

from .whatsapp_bot import WhatsAppBot
from .instagram_bot import InstagramBot
from .config import InstagramConfig, WhatsAppConfig, AIConfig

__version__ = "0.1.0"
__author__ = "Nandhan Golla"
__email__ = "Nandhan@example.com"

__all__ = [
    "WhatsAppBot",
    "InstagramBot",
    "WhatsAppConfig",
    "InstagramConfig", 
    "AIConfig",
]