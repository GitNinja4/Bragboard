#!/bin/bash

echo "🔨 Installing Python dependencies..."
cd server
pip install -r requirements.txt
cd ..

echo "📦 Installing Node dependencies..."
cd client
npm install
npm run build
cd ..

echo "✅ Build completed successfully!"
