#!/usr/bin/env python
"""Run the FastAPI server"""
import uvicorn
import os

# Change to server directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("src.main:app", host="0.0.0.0", port=port, reload=False)
