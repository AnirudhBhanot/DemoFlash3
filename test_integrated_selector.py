#!/usr/bin/env python3
"""
Test integrated selector to debug framework selection
"""

import asyncio
import logging
from strategic_context_engine import StrategicContextEngine
from framework_intelligence.integrated_framework_selector import IntegratedFrameworkSelector

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

async def test_integrated_selector():
    """Test the integrated selector with Series A company"""
    
    # Create test data
    startup_data = {
        "startup_name": "SeriesATest",
        "funding_stage": "series_a",
        "sector": "saas_b2b",
        "team_size_full_time": 25,
        "annual_revenue_usd": 5000000,
        "revenue_growth_rate": 150,
        "burn_rate_usd": 500000,
        "cash_on_hand_usd": 6000000,
        "runway_months": 12,
        "market_share_percentage": 2,
        "customer_count": 100,
        "customer_acquisition_cost_usd": 5000,
        "lifetime_value_usd": 50000,
        "monthly_active_users": 5000,
        "b2b_or_b2c": "b2b",
        "geographical_focus": "domestic",
        "proprietary_tech": True,
        "founders_industry_experience_years": 10
    }
    
    # Build context
    context_engine = StrategicContextEngine()
    context = await context_engine.build_company_context(startup_data)
    
    logger.info(f"Context built: {context.company_name}, Stage: {context.stage}")
    
    # Create selector
    selector = IntegratedFrameworkSelector()
    
    # Select frameworks
    frameworks = await selector.select_frameworks(
        strategic_context=context,
        max_frameworks=3,
        use_academic_logic=True
    )
    
    logger.info(f"\nSelected {len(frameworks)} frameworks:")
    for i, fw in enumerate(frameworks, 1):
        logger.info(f"{i}. {fw.base_framework.name} (ID: {fw.base_framework.id})")
        academic_insights = fw.customizations.get("academic_insights", {})
        logger.info(f"   Fit Score: {academic_insights.get('fit_score', 'N/A')}")
        logger.info(f"   Rationale: {academic_insights.get('rationale', [])}")

if __name__ == "__main__":
    asyncio.run(test_integrated_selector())