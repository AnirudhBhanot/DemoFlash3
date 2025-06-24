#!/usr/bin/env python3
"""
Final comprehensive test of BCG Matrix selection system
"""

import asyncio
import aiohttp
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_api_endpoint(session, test_case):
    """Test the actual API endpoint"""
    
    url = "http://localhost:8001/api/michelin/enhanced/analyze/phase1"
    
    # Add all required fields
    startup_data = test_case["data"].copy()
    startup_data.update({
        "revenue_growth_rate_percent": 150,
        "monthly_burn_usd": 500000,
        "burn_rate_usd": 500000,
        "cash_on_hand_usd": 10000000,
        "total_capital_raised_usd": 15000000,
        "runway_months": 20,
        "customer_count": 200,
        "customer_acquisition_cost_usd": 2000,
        "lifetime_value_usd": 40000,
        "ltv_cac_ratio": 20,
        "monthly_active_users": 10000,
        "net_dollar_retention_percent": 130,
        "geographical_focus": "global",
        "proprietary_tech": True,
        "founders_industry_experience_years": 10,
        "has_strategic_partnerships": True,
        "competitors_named_count": 8,
        "competitor_count": 8,
        "market_size_usd": 10000000000,
        "market_growth_rate_annual": 45,
        "product_stage": "scaling",
        "patents_filed": 5,
        "investor_tier_primary": "tier_1"
    })
    
    payload = {"startup_data": startup_data}
    
    try:
        async with session.post(url, json=payload) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                logger.error(f"API Error: {response.status}")
                return None
    except Exception as e:
        logger.error(f"Request failed: {e}")
        return None

async def main():
    """Run comprehensive tests"""
    
    test_cases = [
        {
            "name": "Ideal BCG Star Company",
            "data": {
                "startup_name": "IdealStar",
                "funding_stage": "series_b",
                "sector": "saas_b2b",
                "team_size_full_time": 60,
                "annual_revenue_usd": 30000000,
                "market_share_percentage": 12,
                "b2b_or_b2c": "b2b"
            },
            "expected_position": "Star",
            "expected_bcg_rank": "Top 3"
        },
        {
            "name": "Question Mark Startup",
            "data": {
                "startup_name": "QuestionMarkCo",
                "funding_stage": "series_a",
                "sector": "saas_b2b",
                "team_size_full_time": 30,
                "annual_revenue_usd": 5000000,
                "market_share_percentage": 2,
                "b2b_or_b2c": "b2b"
            },
            "expected_position": "Question Mark",
            "expected_bcg_rank": "Top 3"
        },
        {
            "name": "Pre-Seed (No BCG)",
            "data": {
                "startup_name": "EarlyStage",
                "funding_stage": "pre_seed",
                "sector": "saas_b2b",
                "team_size_full_time": 5,
                "annual_revenue_usd": 0,
                "market_share_percentage": 0,
                "b2b_or_b2c": "b2b"
            },
            "expected_position": "N/A",
            "expected_bcg_rank": "Not Selected"
        }
    ]
    
    async with aiohttp.ClientSession() as session:
        logger.info("=== BCG Matrix Selection System - Final Test ===\n")
        
        for test_case in test_cases:
            logger.info(f"Testing: {test_case['name']}")
            logger.info(f"Expected Position: {test_case['expected_position']}")
            logger.info(f"Expected BCG Rank: {test_case['expected_bcg_rank']}")
            
            result = await test_api_endpoint(session, test_case)
            
            if result:
                # Extract relevant data
                phase1 = result.get("phase1", {})
                bcg_analysis = phase1.get("bcg_matrix_analysis", {})
                position = bcg_analysis.get("position", "Not determined")
                
                # Check if BCG was in selected frameworks (from logs)
                logger.info(f"Actual Position: {position}")
                
                # Verify position matches expected
                if test_case["expected_position"] == "N/A":
                    position_correct = position == "Not determined"
                else:
                    position_correct = position == test_case["expected_position"]
                
                logger.info(f"Position Correct: {'✓' if position_correct else '✗'}")
                logger.info("")
            else:
                logger.error("Failed to get API response")
                logger.info("")

if __name__ == "__main__":
    asyncio.run(main())