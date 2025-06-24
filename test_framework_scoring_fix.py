#!/usr/bin/env python3
"""Test framework scoring to ensure differentiation"""

import asyncio
import logging
from enhanced_framework_selector import EnhancedFrameworkSelector

# Set up logging to see debug output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def test_framework_scoring():
    """Test that frameworks get different scores"""
    
    selector = EnhancedFrameworkSelector()
    
    # Test with pre-seed startup
    startup_data = {
        "startup_name": "TestStartup",
        "sector": "saas_b2b",
        "stage": "pre_seed",
        "revenue": 0,
        "growth_rate": 0,
        "burn_rate": 50000,
        "ltv_cac_ratio": 0,
        "net_revenue_retention": 0,
        "team_size": 3,
        "runway_months": 12,
        "key_challenges": [
            "Finding product-market fit",
            "Customer acquisition",
            "Limited resources"
        ]
    }
    
    print("\n=== Testing Pre-seed Startup ===")
    result = await selector.select_frameworks_for_startup(startup_data, max_frameworks=5)
    
    if result["success"]:
        print(f"\nSelected {len(result['frameworks'])} frameworks:")
        scores_seen = set()
        for fw in result["frameworks"]:
            score = fw['fit_score']
            scores_seen.add(score)
            print(f"- {fw['name']}: Score = {score:.1f}")
        
        print(f"\nUnique scores: {len(scores_seen)}")
        if len(scores_seen) == 1:
            print("❌ ERROR: All frameworks have the same score!")
        else:
            print("✅ SUCCESS: Frameworks have different scores")
    else:
        print(f"❌ Error: {result['error']}")
    
    # Test with Series A startup
    startup_data_series_a = {
        "startup_name": "GrowthStartup",
        "sector": "marketplace",
        "stage": "series_a",
        "revenue": 5000000,
        "growth_rate": 200,
        "burn_rate": 500000,
        "ltv_cac_ratio": 3.5,
        "net_revenue_retention": 120,
        "team_size": 50,
        "runway_months": 18,
        "key_challenges": [
            "Scaling operations",
            "Intense competition",
            "Unit economics optimization"
        ]
    }
    
    print("\n\n=== Testing Series A Startup ===")
    result_a = await selector.select_frameworks_for_startup(startup_data_series_a, max_frameworks=5)
    
    if result_a["success"]:
        print(f"\nSelected {len(result_a['frameworks'])} frameworks:")
        scores_seen_a = set()
        for fw in result_a["frameworks"]:
            score = fw['fit_score']
            scores_seen_a.add(score)
            print(f"- {fw['name']}: Score = {score:.1f}")
        
        print(f"\nUnique scores: {len(scores_seen_a)}")
        if len(scores_seen_a) == 1:
            print("❌ ERROR: All frameworks have the same score!")
        else:
            print("✅ SUCCESS: Frameworks have different scores")
    else:
        print(f"❌ Error: {result_a['error']}")

if __name__ == "__main__":
    asyncio.run(test_framework_scoring())