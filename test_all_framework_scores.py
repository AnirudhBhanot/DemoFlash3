#!/usr/bin/env python3
"""
Test all framework scores to see why BCG isn't #1
"""

import asyncio
import logging
from strategic_context_engine import StrategicContextEngine
from framework_intelligence.integrated_framework_selector import IntegratedFrameworkSelector
from framework_intelligence.framework_selection_engine import AdvancedFrameworkSelector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_all_scores():
    """Test all framework scores"""
    
    # Create test data
    startup_data = {
        "startup_name": "BCGPerfectFit",
        "funding_stage": "series_b",
        "sector": "saas_b2b",
        "team_size_full_time": 50,
        "annual_revenue_usd": 25000000,
        "revenue_growth_rate_percent": 150,
        "monthly_burn_usd": 1000000,
        "burn_rate_usd": 1000000,
        "cash_on_hand_usd": 40000000,
        "total_capital_raised_usd": 50000000,
        "runway_months": 40,
        "customer_count": 500,
        "market_share_percentage": 8,
        "customer_acquisition_cost_usd": 2000,
        "lifetime_value_usd": 60000,
        "ltv_cac_ratio": 30,
        "monthly_active_users": 25000,
        "net_dollar_retention_percent": 140,
        "b2b_or_b2c": "b2b",
        "geographical_focus": "global",
        "proprietary_tech": True,
        "founders_industry_experience_years": 20
    }
    
    # Build context
    context_engine = StrategicContextEngine()
    strategic_context = await context_engine.build_company_context(startup_data)
    
    # Convert to academic context
    selector = IntegratedFrameworkSelector()
    academic_context = selector._convert_to_academic_context(strategic_context)
    
    # Get framework recommendations
    academic_selector = AdvancedFrameworkSelector()
    recommendations = academic_selector.select_frameworks(academic_context, max_recommendations=10)
    
    logger.info(f"Company: {academic_context.company_name}")
    logger.info(f"Stage: {academic_context.stage.value}")
    logger.info(f"Problems: {[p.value for p in academic_context.primary_problems]}")
    logger.info(f"Available Data: {[d.value for d in academic_context.available_data]}")
    
    logger.info(f"\nTop 10 Framework Scores:")
    for i, rec in enumerate(recommendations[:10], 1):
        logger.info(f"{i}. {rec.framework_id:30} Score: {rec.fit_score:6.1f}")
        logger.info(f"   Stage: {rec.stage_fit:3.0f} Problem: {rec.problem_fit:5.1f} Data: {rec.data_fit:5.1f} Team: {rec.team_fit:3.0f}")

if __name__ == "__main__":
    asyncio.run(test_all_scores())