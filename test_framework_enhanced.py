#!/usr/bin/env python3
"""Test enhanced framework selection with team size constraints"""

import requests
import json

def test_framework_selection(test_name, data):
    """Test framework selection with given data"""
    print(f"\n{'='*60}")
    print(f"Test: {test_name}")
    print(f"{'='*60}")
    
    url = "http://localhost:8001/api/frameworks/enhanced/select"
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        result = response.json()
        print(f"\nSelected {len(result['frameworks'])} frameworks:")
        
        for i, fw in enumerate(result['frameworks'], 1):
            print(f"\n{i}. {fw['name']}")
            print(f"   ID: {fw['id']}")
            print(f"   Score: {fw.get('score', 'N/A')}")
            print(f"   Rationale: {fw.get('rationale', 'N/A')}")
            
            # Check if BCG Matrix is selected for small teams
            if fw['id'] in ['bcg_matrix', 'bcg_growth_share_matrix'] and data['team_size'] < 20:
                print(f"   ⚠️  WARNING: BCG Matrix selected for team size {data['team_size']} (min should be 20)")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# Test 1: Small team (8 people) with unit economics challenges
test_framework_selection(
    "Small Team (8 people) - Unit Economics Challenges",
    {
        "startup_name": "EarlyStartup",
        "stage": "seed",
        "team_size": 8,
        "sector": "saas_b2b",
        "key_challenges": ["unit economics", "customer acquisition", "burn rate"],
        "revenue": 50000,
        "growth_rate": 20,
        "ltv_cac_ratio": 0.8
    }
)

# Test 2: Growth company (50 people) with portfolio challenges
test_framework_selection(
    "Growth Company (50 people) - Portfolio Optimization",
    {
        "startup_name": "StrategicCo",
        "stage": "series_a",
        "team_size": 50,
        "sector": "saas_b2b", 
        "key_challenges": ["resource allocation", "portfolio optimization", "multiple products"],
        "revenue": 5000000,
        "growth_rate": 100
    }
)

# Test 3: Company with competitive challenges
test_framework_selection(
    "Tech Company - Intense Competition",
    {
        "startup_name": "CompetitiveTech",
        "stage": "series_a",
        "team_size": 30,
        "sector": "saas_b2b",
        "key_challenges": ["intense competition", "market differentiation", "competitive positioning"],
        "revenue": 2000000,
        "growth_rate": 60
    }
)

# Test 4: Pre-seed company (5 people) - Should NOT get BCG Matrix
test_framework_selection(
    "Pre-seed Company (5 people) - Early Stage",
    {
        "startup_name": "TinyStartup",
        "stage": "pre_seed",
        "team_size": 5,
        "sector": "marketplace",
        "key_challenges": ["product-market fit", "customer discovery", "mvp development"],
        "revenue": 0
    }
)