#!/usr/bin/env python3
"""Test scoring for a specific framework"""

import logging
from framework_intelligence.framework_selection_engine import (
    AdvancedFrameworkSelector, 
    CompanyContext,
    TemporalStage,
    IndustryContext,
    ProblemArchetype,
    DataRequirement
)

# Set up detailed logging
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(levelname)s - %(message)s'
)

selector = AdvancedFrameworkSelector()

# Create context
context = CompanyContext(
    company_name="TestStartup",
    industry=IndustryContext.B2B_SAAS,
    stage=TemporalStage.PRE_FORMATION,
    team_size=3,
    primary_problems=[
        ProblemArchetype.PRODUCT_MARKET_FIT,
        ProblemArchetype.CUSTOMER_DISCOVERY,
        ProblemArchetype.BUSINESS_MODEL_DESIGN
    ],
    available_data=[DataRequirement.QUALITATIVE_ONLY],
    timeline_days=90,
    revenue_usd=0,
    growth_rate_percent=0,
    burn_rate_usd=50000,
    runway_months=12
)

# Score specific framework
print("\n=== Scoring customer_development ===")
rec = selector._score_framework("customer_development", context)
print(f"Final score: {rec.fit_score:.2f}")
print(f"Confidence: {rec.confidence}%")
print(f"Rationale: {rec.rationale}")
print(f"Risks: {rec.risks}")

print("\n=== Scoring lean_canvas ===")
rec2 = selector._score_framework("lean_canvas", context)
print(f"Final score: {rec2.fit_score:.2f}")
print(f"Confidence: {rec2.confidence}%")