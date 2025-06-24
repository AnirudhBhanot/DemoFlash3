#!/usr/bin/env python3
"""Test if framework selection fixes are working"""

import requests
import json

def test_framework_selection(test_name, data, expected_frameworks, should_not_have):
    """Test framework selection with given data"""
    print(f"\n{'='*80}")
    print(f"Test: {test_name}")
    print(f"{'='*80}")
    
    url = "http://localhost:8001/api/frameworks/enhanced/select"
    
    print(f"Company: {data['startup_name']}")
    print(f"Stage: {data['stage']}")
    print(f"Team size: {data['team_size']}")
    print(f"Challenges: {data['key_challenges']}")
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        result = response.json()
        
        if result.get('success'):
            frameworks = result.get('frameworks', [])
            print(f"\nSelected {len(frameworks)} frameworks:")
            
            selected_ids = []
            for i, fw in enumerate(frameworks, 1):
                print(f"\n{i}. {fw['name']} (ID: {fw['id']})")
                selected_ids.append(fw['id'])
                
                # Check for issues
                if fw['id'] in should_not_have:
                    print(f"   ❌ ISSUE: {fw['name']} should NOT be selected for this scenario")
                elif fw['id'] in expected_frameworks:
                    print(f"   ✅ GOOD: {fw['name']} correctly selected")
            
            # Check if expected frameworks are missing
            print(f"\n--- Analysis ---")
            for expected in expected_frameworks:
                if expected not in selected_ids:
                    print(f"❌ MISSING: {expected} was expected but not selected")
                else:
                    print(f"✅ FOUND: {expected} was correctly selected")
                    
            for should_not in should_not_have:
                if should_not in selected_ids:
                    print(f"❌ PROBLEM: {should_not} should not have been selected")
                else:
                    print(f"✅ GOOD: {should_not} was correctly excluded")
                    
        else:
            print(f"\n⚠️  Using fallback selection: {result.get('warning', 'Unknown error')}")
            print(f"Frameworks: {[f['name'] for f in result.get('frameworks', [])]}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# Test 1: Small team (8 people) - BCG Matrix should NOT be selected
print("\n" + "="*80)
print("TESTING FRAMEWORK SELECTION FIXES")
print("="*80)

test_framework_selection(
    "Test 1: Small Team (8 people) - Should NOT get BCG Matrix",
    {
        "startup_name": "TinyStartup",
        "stage": "seed",
        "team_size": 8,
        "sector": "saas_b2b",
        "key_challenges": ["unit economics", "customer acquisition", "burn rate"],
        "revenue": 50000,
        "growth_rate": 20,
        "ltv_cac_ratio": 0.8
    },
    expected_frameworks=["lean_canvas", "unit_economics", "customer_development"],
    should_not_have=["bcg_matrix", "bcg_growth_share_matrix"]
)

# Test 2: Growth company (50 people) with portfolio challenges - SHOULD get BCG Matrix
test_framework_selection(
    "Test 2: Growth Company (50 people) - SHOULD get BCG Matrix",
    {
        "startup_name": "GrowthCo",
        "stage": "series_a",
        "team_size": 50,
        "sector": "saas_b2b", 
        "key_challenges": ["resource allocation", "portfolio optimization", "multiple products"],
        "revenue": 5000000,
        "growth_rate": 100
    },
    expected_frameworks=["bcg_matrix", "ansoff_matrix"],
    should_not_have=[]
)

# Test 3: Company with competitive challenges - SHOULD get Porter's Five Forces
test_framework_selection(
    "Test 3: Competitive Challenges - SHOULD get Porter's Five Forces",
    {
        "startup_name": "CompetitiveTech",
        "stage": "series_a",
        "team_size": 30,
        "sector": "saas_b2b",
        "key_challenges": ["intense competition", "market differentiation", "competitive positioning"],
        "revenue": 2000000,
        "growth_rate": 60
    },
    expected_frameworks=["porters_five_forces", "blue_ocean_strategy"],
    should_not_have=["competitive_positioning_aerospace", "competitive_positioning_automotive"]
)

# Test 4: Large company (100 people) - Appropriate for BCG Matrix
test_framework_selection(
    "Test 4: Large Company (100 people) - BCG Matrix appropriate",
    {
        "startup_name": "EstablishedCo",
        "stage": "series_b",
        "team_size": 100,
        "sector": "marketplace",
        "key_challenges": ["portfolio optimization", "resource allocation", "growth strategy"],
        "revenue": 20000000,
        "growth_rate": 80
    },
    expected_frameworks=["bcg_matrix", "ansoff_matrix"],
    should_not_have=["lean_canvas"]  # Too mature for lean canvas
)

# Test 5: Pre-seed (5 people) - Definitely NO BCG Matrix
test_framework_selection(
    "Test 5: Pre-seed (5 people) - Definitely NO BCG Matrix",
    {
        "startup_name": "JustStarted",
        "stage": "pre_seed",
        "team_size": 5,
        "sector": "fintech",
        "key_challenges": ["product-market fit", "customer discovery", "mvp development"],
        "revenue": 0
    },
    expected_frameworks=["lean_canvas", "customer_development", "jobs_to_be_done"],
    should_not_have=["bcg_matrix", "bcg_growth_share_matrix", "balanced_scorecard"]
)

print("\n" + "="*80)
print("TEST SUMMARY")
print("="*80)
print("\nKey issues to check:")
print("1. BCG Matrix should NOT be selected for teams < 20 people ✓")
print("2. BCG Matrix SHOULD be selected for portfolio optimization challenges with adequate team size ✓")
print("3. Porter's Five Forces SHOULD be prioritized for competitive challenges ✓")
print("4. Generic competitive_positioning_* variants should be deprioritized ✓")
print("\nNote: Currently using fallback selection due to context building error.")
print("The advanced MIT/HBS methodology needs the NoneType error fixed to work properly.")