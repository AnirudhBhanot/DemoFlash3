#!/usr/bin/env python3
"""Simple test to debug framework selection"""

import requests
import json

url = "http://localhost:8001/api/frameworks/enhanced/select"

# Minimal test data
data = {
    "startup_name": "TestCo",
    "stage": "seed",
    "team_size": 10,
    "sector": "saas_b2b",
    "key_challenges": ["unit economics"],
    "revenue": 100000,
    "growth_rate": 50
}

print("Sending request...")
print(json.dumps(data, indent=2))

response = requests.post(url, json=data)

print(f"\nStatus: {response.status_code}")
print("\nResponse:")
print(json.dumps(response.json(), indent=2))