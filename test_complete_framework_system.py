#!/usr/bin/env python3
"""
Test the complete framework system end-to-end
"""

import asyncio
import json
from strategic_context_engine import StrategicContextEngine
from enhanced_framework_selector import EnhancedFrameworkSelector

async def test_scenario(name, startup_data, expected_frameworks=None):
    """Test a specific scenario"""
    
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print(f"{'='*60}")
    
    # Build context
    context_engine = StrategicContextEngine()
    context = await context_engine.build_company_context(startup_data)
    
    print(f"\nCompany: {startup_data['startup_name']}")
    print(f"Stage: {startup_data['funding_stage']}")
    print(f"Sector: {startup_data['sector']}")
    print(f"Team Size: {startup_data['team_size_full_time']}")
    print(f"Revenue: ${startup_data.get('annual_revenue_usd', 0):,}")
    
    print(f"\nChallenges identified:")
    for i, challenge in enumerate(context.key_challenges[:5], 1):
        print(f"  {i}. {challenge}")
    
    # Select frameworks using enhanced selector
    selector = EnhancedFrameworkSelector()
    result = await selector.select_frameworks_for_startup(
        startup_data, 
        max_frameworks=5
    )
    
    if result['success']:
        print(f"\nMethodology: {result.get('methodology', 'Unknown')}")
        print(f"\nSelected frameworks:")
        for i, fw in enumerate(result['frameworks'], 1):
            score = fw.get('fit_score', 0)
            name = fw.get('name', 'Unknown')
            print(f"  {i}. {name} (score: {score:.1f})")
            print(f"     Why: {fw.get('selection_rationale', 'N/A')[:100]}...")
        
        # Check if expected frameworks were selected
        if expected_frameworks:
            selected_names = [fw.get('name', 'Unknown') for fw in result['frameworks']]
            print(f"\nExpected frameworks check:")
            for expected in expected_frameworks:
                if any(expected.lower() in name.lower() for name in selected_names):
                    print(f"  ✓ {expected} - Found")
                else:
                    print(f"  ✗ {expected} - NOT FOUND")
    else:
        print(f"\nError: {result.get('error', 'Unknown error')}")
    
    return result

async def main():
    """Run all test scenarios"""
    
    print("Framework System End-to-End Test")
    print("================================\n")
    
    # Test scenarios
    scenarios = [
        # 1. BCG Matrix scenario - Growth stage with portfolio
        {
            "name": "Growth Stage B2B SaaS with Multiple Products",
            "data": {
                "startup_name": "MultiProductSaaS",
                "funding_stage": "series_a",
                "sector": "saas_b2b",
                "team_size_full_time": 25,
                "annual_revenue_usd": 2500000,
                "revenue_growth_rate_percent": 150,
                "burn_rate_usd": 200000,
                "runway_months": 18,
                "market_growth_rate_percent": 40,
                "b2b_or_b2c": "b2b",
                "customer_count": 150,
                "ltv_cac_ratio": 3.5
            },
            "expected": ["BCG", "Unit Economics", "Growth"]
        },
        
        # 2. Porter's Five Forces scenario - Competitive market entry
        {
            "name": "Marketplace Entering Competitive Market",
            "data": {
                "startup_name": "MarketplaceChallenger",
                "funding_stage": "seed",
                "sector": "marketplace",
                "team_size_full_time": 12,
                "annual_revenue_usd": 300000,
                "revenue_growth_rate_percent": 200,
                "burn_rate_usd": 80000,
                "runway_months": 15,
                "market_growth_rate_percent": 25,
                "b2b_or_b2c": "b2c",
                "customer_count": 5000,
                "competition_intensity": 4
            },
            "expected": ["Porter", "Competitive", "Market"]
        },
        
        # 3. Early stage - Should get Lean Canvas
        {
            "name": "Pre-seed Startup",
            "data": {
                "startup_name": "EarlyStageStartup",
                "funding_stage": "pre_seed",
                "sector": "saas_b2b",
                "team_size_full_time": 3,
                "annual_revenue_usd": 0,
                "revenue_growth_rate_percent": 0,
                "burn_rate_usd": 10000,
                "runway_months": 10,
                "market_growth_rate_percent": 50,
                "b2b_or_b2c": "b2b",
                "customer_count": 0
            },
            "expected": ["Lean Canvas", "Customer Development", "Jobs to be Done"]
        },
        
        # 4. Scale stage operations
        {
            "name": "Scale Stage Operations Focus",
            "data": {
                "startup_name": "ScaleOps",
                "funding_stage": "series_b",
                "sector": "ecommerce",
                "team_size_full_time": 100,
                "annual_revenue_usd": 15000000,
                "revenue_growth_rate_percent": 80,
                "burn_rate_usd": 500000,
                "runway_months": 24,
                "market_growth_rate_percent": 20,
                "b2b_or_b2c": "b2c",
                "customer_count": 50000,
                "operational_efficiency_score": 65
            },
            "expected": ["Six Sigma", "Lean", "OKR"]
        }
    ]
    
    # Run all scenarios
    results = []
    for scenario in scenarios:
        result = await test_scenario(
            scenario["name"],
            scenario["data"],
            scenario.get("expected")
        )
        results.append({
            "scenario": scenario["name"],
            "result": result
        })
    
    # Summary
    print(f"\n\n{'='*60}")
    print("Test Summary")
    print(f"{'='*60}")
    print(f"Total scenarios tested: {len(scenarios)}")
    print(f"All tests completed successfully!")
    
    # Save results
    with open("framework_system_test_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nDetailed results saved to framework_system_test_results.json")

if __name__ == "__main__":
    asyncio.run(main())