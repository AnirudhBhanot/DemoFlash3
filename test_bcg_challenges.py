#!/usr/bin/env python3
"""
Test what challenges are identified for BCG test company
"""

import asyncio
import logging
from strategic_context_engine import StrategicContextEngine
from framework_intelligence.integrated_framework_selector import IntegratedFrameworkSelector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_bcg_challenges():
    """Test challenge identification"""
    
    # Create test data for BCG Matrix company
    startup_data = {
        "startup_name": "BCGMatrixTest",
        "funding_stage": "series_a",
        "sector": "saas_b2b",
        "team_size_full_time": 35,
        "annual_revenue_usd": 10000000,
        "revenue_growth_rate_percent": 200,  # High growth
        "monthly_burn_usd": 700000,
        "burn_rate_usd": 700000,
        "cash_on_hand_usd": 20000000,
        "total_capital_raised_usd": 25000000,
        "runway_months": 28,
        "customer_count": 200,
        "market_share_percentage": 5,  # Decent market share
        "customer_acquisition_cost_usd": 2500,
        "lifetime_value_usd": 50000,
        "ltv_cac_ratio": 20,  # Excellent LTV/CAC
        "monthly_active_users": 10000,
        "net_dollar_retention_percent": 130,
        "b2b_or_b2c": "b2b",
        "geographical_focus": "global",
        "proprietary_tech": True,
        "founders_industry_experience_years": 15,
        "has_strategic_partnerships": True,
        "competitors_named_count": 10,
        "competitor_count": 10,
        "market_size_usd": 10000000000,
        "market_growth_rate_annual": 50,
        "product_stage": "scaling",
        "patents_filed": 5,
        "investor_tier_primary": "tier_1"
    }
    
    # Build context
    context_engine = StrategicContextEngine()
    context = await context_engine.build_company_context(startup_data)
    
    logger.info(f"Company: {context.company_name}")
    logger.info(f"Stage: {context.stage}")
    logger.info(f"Team Size: {context.key_metrics.get('team_size', 'NOT FOUND')}")
    logger.info(f"\nKey Challenges Identified:")
    for i, challenge in enumerate(context.key_challenges, 1):
        logger.info(f"  {i}. {challenge}")
    
    # Convert to academic context
    selector = IntegratedFrameworkSelector()
    academic_context = selector._convert_to_academic_context(context)
    
    logger.info(f"\nAcademic Context:")
    logger.info(f"  Team Size: {academic_context.team_size}")
    logger.info(f"  Primary Problems: {[p.value for p in academic_context.primary_problems]}")
    
    # Test BCG Matrix scoring directly
    from framework_intelligence.framework_selection_engine import AdvancedFrameworkSelector
    academic_selector = AdvancedFrameworkSelector()
    bcg_score = academic_selector._score_framework("bcg_matrix", academic_context)
    
    logger.info(f"\nBCG Matrix Scoring:")
    logger.info(f"  Fit Score: {bcg_score.fit_score:.1f}")
    logger.info(f"  Stage Fit: {bcg_score.stage_fit}")
    logger.info(f"  Problem Fit: {bcg_score.problem_fit}")
    logger.info(f"  Team Fit: {bcg_score.team_fit}")
    logger.info(f"  Data Fit: {bcg_score.data_fit}")
    logger.info(f"  Rationale: {bcg_score.rationale}")

if __name__ == "__main__":
    asyncio.run(test_bcg_challenges())