#!/bin/bash

echo "🚀 Launching FLASH Platform..."

# Check if ngrok is installed
if ! command -v ngrok &> /dev/null; then
    echo "📦 Installing ngrok..."
    brew install ngrok
fi

# Start backend
echo "🔧 Starting backend API server..."
python3 api_server_unified.py &
BACKEND_PID=$!

# Wait for backend to start
echo "⏳ Waiting for backend to initialize..."
sleep 10

# Start ngrok for backend
echo "🌐 Creating public URL for backend..."
ngrok http 8001 --log=stdout > ngrok.log 2>&1 &
NGROK_PID=$!

# Wait for ngrok to start and extract URL
sleep 5
BACKEND_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o '"public_url":"https://[^"]*' | cut -d'"' -f4 | head -1)

if [ -z "$BACKEND_URL" ]; then
    echo "❌ Failed to get ngrok URL. Check ngrok.log for details."
    kill $BACKEND_PID $NGROK_PID
    exit 1
fi

echo "✅ Backend available at: $BACKEND_URL"

# Update frontend environment
echo "📝 Updating frontend configuration..."
cd flash-frontend-apple
echo "REACT_APP_API_URL=$BACKEND_URL" > .env.local

# Start frontend
echo "🎨 Starting frontend..."
npm start &
FRONTEND_PID=$!

echo ""
echo "=========================================="
echo "✅ FLASH Platform is running!"
echo "=========================================="
echo "🔧 Backend API: $BACKEND_URL"
echo "🎨 Frontend: http://localhost:3000"
echo ""
echo "📤 Share this URL with testers: http://localhost:3000"
echo "   (They'll need to be on your network, or use another ngrok tunnel)"
echo ""
echo "Press Ctrl+C to stop all services"
echo "=========================================="

# Cleanup function
cleanup() {
    echo "🛑 Shutting down services..."
    kill $BACKEND_PID $FRONTEND_PID $NGROK_PID 2>/dev/null
    exit 0
}

# Set up trap for cleanup
trap cleanup INT

# Wait
wait