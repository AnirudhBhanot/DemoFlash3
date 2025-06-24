#!/usr/bin/env python3
"""
Test that lean_canvas is now properly handled
"""

import asyncio
import logging
from strategic_context_engine import StrategicContextEngine
from framework_intelligence.integrated_framework_selector import IntegratedFrameworkSelector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_lean_canvas():
    """Test lean canvas selection for early stage company"""
    
    # Create early stage startup data
    startup_data = {
        "startup_name": "EarlyStartup",
        "funding_stage": "pre_seed",
        "sector": "saas_b2b",
        "team_size_full_time": 3,
        "annual_revenue_usd": 0,
        "revenue_growth_rate_percent": 0,
        "monthly_burn_usd": 10000,
        "burn_rate_usd": 10000,
        "cash_on_hand_usd": 100000,
        "runway_months": 10,
        "market_share_percentage": 0,
        "customer_count": 0,
        "ltv_cac_ratio": 0,
        "b2b_or_b2c": "b2b"
    }
    
    # Build context
    context_engine = StrategicContextEngine()
    context = await context_engine.build_company_context(startup_data)
    
    # Select frameworks
    selector = IntegratedFrameworkSelector()
    frameworks = await selector.select_frameworks(
        strategic_context=context,
        max_frameworks=5,
        use_academic_logic=True
    )
    
    # Check results
    framework_names = [f.base_framework.name for f in frameworks]
    logger.info(f"Selected frameworks for {startup_data['startup_name']}:")
    for i, name in enumerate(framework_names, 1):
        logger.info(f"  {i}. {name}")
    
    # Check if lean canvas was selected
    lean_canvas_selected = any("Lean Canvas" in name for name in framework_names)
    logger.info(f"\nLean Canvas selected: {'YES' if lean_canvas_selected else 'NO'}")
    
    # Check if customer development was selected
    customer_dev_selected = any("Customer Development" in name for name in framework_names)
    logger.info(f"Customer Development selected: {'YES' if customer_dev_selected else 'NO'}")

if __name__ == "__main__":
    asyncio.run(test_lean_canvas())