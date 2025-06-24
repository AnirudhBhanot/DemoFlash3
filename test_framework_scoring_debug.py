#!/usr/bin/env python3
"""Debug framework scoring in detail"""

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
    format='%(name)s - %(levelname)s - %(message)s'
)

def test_framework_scoring_debug():
    """Test framework scoring with debug output"""
    
    selector = AdvancedFrameworkSelector()
    
    # Create context for pre-seed startup
    context = CompanyContext(
        company_name="TestStartup",
        industry=IndustryContext.B2B_SAAS,
        stage=TemporalStage.PRE_FORMATION,  # pre_seed maps to this
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
    
    print("\n=== Testing Pre-seed Context ===")
    print(f"Stage: {context.stage}")
    print(f"Industry: {context.industry}")
    print(f"Team size: {context.team_size}")
    print(f"Problems: {[p.value for p in context.primary_problems]}")
    
    # Get recommendations
    recommendations = selector.select_frameworks(context, max_recommendations=20)
    
    print(f"\nReceived {len(recommendations)} recommendations:")
    print("-" * 80)
    
    # Find specific frameworks we care about
    core_frameworks = ['lean_canvas', 'customer_development', 'jobs_to_be_done', 
                      'bcg_matrix', 'porters_five_forces', 'unit_economics']
    
    for i, rec in enumerate(recommendations):
        marker = "⭐" if rec.framework_id in core_frameworks else "  "
        print(f"{marker} [{i+1}] {rec.framework_id}")
        print(f"      Score: {rec.fit_score:.2f}")
        print(f"      Stage fit: {rec.stage_fit}, Problem fit: {rec.problem_fit:.0f}%, "
              f"Data fit: {rec.data_fit:.0f}%, Team fit: {rec.team_fit}")
        if rec.rationale:
            print(f"      Rationale: {rec.rationale[0]}")
        if rec.risks:
            print(f"      Risk: {rec.risks[0]}")
        print()
    
    # Check if core frameworks are in the list
    print("\nCore Framework Analysis:")
    print("-" * 40)
    for fw in core_frameworks:
        found = any(r.framework_id == fw for r in recommendations[:20])
        if found:
            rec = next(r for r in recommendations if r.framework_id == fw)
            idx = recommendations.index(rec)
            print(f"{fw}: ✅ Found at position {idx+1} (score: {rec.fit_score:.2f})")
        else:
            print(f"{fw}: ❌ Missing from top 20")

if __name__ == "__main__":
    test_framework_scoring_debug()