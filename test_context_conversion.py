#!/usr/bin/env python3
"""
Test context conversion to understand why different frameworks are selected
"""

import asyncio
import logging
from strategic_context_engine import StrategicContextEngine
from framework_intelligence.integrated_framework_selector import IntegratedFrameworkSelector
from framework_intelligence.framework_taxonomy import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_context_conversion():
    """Test how context is converted between systems"""
    
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
    
    # Build strategic context
    context_engine = StrategicContextEngine()
    strategic_context = await context_engine.build_company_context(startup_data)
    
    logger.info("Strategic Context:")
    logger.info(f"  Company: {strategic_context.company_name}")
    logger.info(f"  Stage: {strategic_context.stage}")
    logger.info(f"  Industry: {strategic_context.industry}")
    logger.info(f"  Key Challenges: {strategic_context.key_challenges[:3]}")
    logger.info(f"  Current Inflection: {strategic_context.current_inflection.value if hasattr(strategic_context, 'current_inflection') else 'None'}")
    
    # Convert to academic context
    selector = IntegratedFrameworkSelector()
    academic_context = selector._convert_to_academic_context(strategic_context)
    
    logger.info("\nAcademic Context:")
    logger.info(f"  Company: {academic_context.company_name}")
    logger.info(f"  Stage: {academic_context.stage.value}")
    logger.info(f"  Industry: {academic_context.industry.value}")
    logger.info(f"  Primary Problems: {[p.value for p in academic_context.primary_problems]}")
    logger.info(f"  Team Size: {academic_context.team_size}")
    logger.info(f"  Available Data: {[d.value for d in academic_context.available_data]}")
    logger.info(f"  Is Crisis Mode: {academic_context.is_crisis_mode}")
    logger.info(f"  Is Fundraising: {academic_context.is_fundraising}")

if __name__ == "__main__":
    asyncio.run(test_context_conversion())