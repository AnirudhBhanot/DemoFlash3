#!/usr/bin/env python3
"""
Test edge cases for BCG Matrix selection
"""

import asyncio
import logging
import json
from strategic_context_engine import StrategicContextEngine
from framework_intelligence.integrated_framework_selector import IntegratedFrameworkSelector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_edge_cases():
    """Test various edge cases"""
    
    test_cases = [
        {
            "name": "Small Series A (Edge Case)",
            "data": {
                "startup_name": "SmallSeriesA",
                "funding_stage": "series_a",
                "team_size_full_time": 18,  # Just below BCG minimum of 20
                "annual_revenue_usd": 3000000,
                "market_share_percentage": 0.5,
                "sector": "saas_b2b"
            },
            "expected": "Should NOT get BCG Matrix (team too small)"
        },
        {
            "name": "Large Seed (Edge Case)",
            "data": {
                "startup_name": "LargeSeed",
                "funding_stage": "seed",
                "team_size_full_time": 25,  # Above BCG minimum
                "annual_revenue_usd": 1000000,
                "market_share_percentage": 0.1,
                "sector": "saas_b2b"
            },
            "expected": "Should NOT get BCG Matrix (too early stage)"
        },
        {
            "name": "Series C Enterprise",
            "data": {
                "startup_name": "SeriesCEnterprise",
                "funding_stage": "series_c",
                "team_size_full_time": 200,
                "annual_revenue_usd": 100000000,
                "market_share_percentage": 25,
                "sector": "saas_b2b"
            },
            "expected": "Should get BCG Matrix (mature company)"
        },
        {
            "name": "Non-SaaS Series A",
            "data": {
                "startup_name": "MarketplaceA",
                "funding_stage": "series_a",
                "team_size_full_time": 40,
                "annual_revenue_usd": 10000000,
                "market_share_percentage": 5,
                "sector": "marketplace"
            },
            "expected": "Should get BCG Matrix (but with lower effectiveness)"
        }
    ]
    
    # Initialize components
    context_engine = StrategicContextEngine()
    selector = IntegratedFrameworkSelector()
    
    logger.info("Testing BCG Matrix selection edge cases...\n")
    
    for test_case in test_cases:
        logger.info(f"=== Testing: {test_case['name']} ===")
        logger.info(f"Expected: {test_case['expected']}")
        
        # Add required fields
        data = test_case["data"]
        data.update({
            "revenue_growth_rate_percent": 100,
            "monthly_burn_usd": 200000,
            "burn_rate_usd": 200000,
            "cash_on_hand_usd": 5000000,
            "runway_months": 25,
            "ltv_cac_ratio": 3,
            "customer_count": 50,
            "b2b_or_b2c": "b2b"
        })
        
        # Build context
        context = await context_engine.build_company_context(data)
        
        # Convert to academic context
        academic_context = selector._convert_to_academic_context(context)
        
        # Get frameworks
        frameworks = await selector.select_frameworks(
            strategic_context=context,
            max_frameworks=5,
            use_academic_logic=True
        )
        
        # Check if BCG Matrix was selected
        bcg_selected = any(f.base_framework.id == "bcg_matrix" for f in frameworks)
        framework_names = [f.base_framework.name for f in frameworks]
        
        logger.info(f"Team Size: {academic_context.team_size}")
        logger.info(f"Stage: {academic_context.stage.value}")
        logger.info(f"Problems: {[p.value for p in academic_context.primary_problems]}")
        logger.info(f"Selected Frameworks: {framework_names}")
        logger.info(f"BCG Matrix Selected: {'YES' if bcg_selected else 'NO'}")
        logger.info("")

if __name__ == "__main__":
    asyncio.run(test_edge_cases())