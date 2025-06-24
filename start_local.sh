#!/bin/bash

echo "🚀 Starting FLASH Platform Locally..."

# Start backend in background
echo "Starting backend API server..."
python api_server_unified.py &
BACKEND_PID=$!

# Wait for backend to start
sleep 5

# Start frontend
echo "Starting frontend..."
cd flash-frontend-apple
npm start &
FRONTEND_PID=$!

echo "✅ FLASH Platform running!"
echo "Backend: http://localhost:8001"
echo "Frontend: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait