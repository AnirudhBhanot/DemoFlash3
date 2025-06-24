#!/usr/bin/env python3
"""Test why all frameworks get score 80.0"""

import asyncio
from enhanced_framework_selector import EnhancedFrameworkSelector

async def test_scoring():
    selector = EnhancedFrameworkSelector()
    
    # Test data with specific challenges
    startup_data = {
        "startup_name": "TestCo",
        "sector": "saas_b2b",
        "stage": "seed",
        "revenue": 100000,
        "growth_rate": 50,
        "burn_rate": 30000,
        "team_size": 10,
        "key_challenges": [
            "Intense competition from Microsoft and Google",
            "Need to optimize unit economics",
            "Building scalable infrastructure"
        ]
    }
    
    result = await selector.select_frameworks_for_startup(startup_data, max_frameworks=5)
    
    print(f"Success: {result['success']}")
    print(f"Methodology: {result.get('methodology', 'Unknown')}")
    print("\nFrameworks selected:")
    
    for i, fw in enumerate(result.get('frameworks', [])):
        print(f"\n{i+1}. {fw['name']}")
        print(f"   Score: {fw.get('fit_score', 'N/A')}")
        print(f"   Category: {fw.get('category', 'N/A')}")
        print(f"   Rationale: {fw.get('rationale', ['N/A'])[0] if fw.get('rationale') else 'N/A'}")

if __name__ == "__main__":
    asyncio.run(test_scoring())