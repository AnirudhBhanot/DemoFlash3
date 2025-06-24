#!/usr/bin/env python3
"""
Validate all framework tags for consistency and appropriateness
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from framework_intelligence.framework_database import FRAMEWORKS
from framework_intelligence.framework_tags_database import create_framework_tags_database
from framework_intelligence.framework_taxonomy import *
from collections import defaultdict

def validate_tags():
    """Validate all framework tags"""
    
    # Get all tags
    tags_db = create_framework_tags_database()
    
    # Validation results
    issues = defaultdict(list)
    stats = {
        "total_frameworks": len(FRAMEWORKS),
        "total_tags": len(tags_db),
        "temporal_coverage": defaultdict(int),
        "problem_coverage": defaultdict(int),
        "industry_coverage": defaultdict(int),
        "complexity_distribution": defaultdict(int),
        "team_size_issues": 0,
        "missing_tags": []
    }
    
    # Check all frameworks have tags
    for framework_id in FRAMEWORKS:
        if framework_id not in tags_db:
            stats["missing_tags"].append(framework_id)
            issues[framework_id].append("Missing tags")
    
    # Validate each tag
    for framework_id, tags in tags_db.items():
        # Check temporal stages
        if not tags.temporal_stages:
            issues[framework_id].append("No temporal stages defined")
        else:
            for stage in tags.temporal_stages:
                stats["temporal_coverage"][stage.value] += 1
        
        # Check problem archetypes
        if not tags.problem_archetypes:
            issues[framework_id].append("No problem archetypes defined")
        else:
            for problem in tags.problem_archetypes:
                stats["problem_coverage"][problem.value] += 1
        
        # Check decision contexts
        if not tags.decision_contexts:
            issues[framework_id].append("No decision contexts defined")
        
        # Check data requirements
        if not tags.data_requirements:
            issues[framework_id].append("No data requirements defined")
        
        # Check outcome types
        if not tags.outcome_types:
            issues[framework_id].append("No outcome types defined")
        
        # Check industry contexts
        if not tags.industry_contexts:
            issues[framework_id].append("No industry contexts defined")
        else:
            for industry in tags.industry_contexts:
                stats["industry_coverage"][industry.value] += 1
        
        # Check complexity
        stats["complexity_distribution"][tags.complexity_tier.value] += 1
        
        # Check team size logic
        if tags.team_size_min > tags.team_size_max:
            issues[framework_id].append(f"Team size min ({tags.team_size_min}) > max ({tags.team_size_max})")
            stats["team_size_issues"] += 1
        
        # Check effectiveness metrics
        if tags.ease_of_use < 0 or tags.ease_of_use > 100:
            issues[framework_id].append(f"Invalid ease_of_use: {tags.ease_of_use}")
        if tags.actionability < 0 or tags.actionability > 100:
            issues[framework_id].append(f"Invalid actionability: {tags.actionability}")
        if tags.accuracy < 0 or tags.accuracy > 100:
            issues[framework_id].append(f"Invalid accuracy: {tags.accuracy}")
        if tags.strategic_impact < 0 or tags.strategic_impact > 100:
            issues[framework_id].append(f"Invalid strategic_impact: {tags.strategic_impact}")
        
        # Check time values
        if tags.time_to_value_days <= 0:
            issues[framework_id].append(f"Invalid time_to_value_days: {tags.time_to_value_days}")
        if tags.durability_months <= 0:
            issues[framework_id].append(f"Invalid durability_months: {tags.durability_months}")
    
    return issues, stats

def print_validation_report(issues, stats):
    """Print validation report"""
    
    print("=== Framework Tags Validation Report ===")
    print(f"\nTotal frameworks: {stats['total_frameworks']}")
    print(f"Total tags: {stats['total_tags']}")
    print(f"Missing tags: {len(stats['missing_tags'])}")
    
    if stats['missing_tags']:
        print("\nFrameworks missing tags:")
        for fid in stats['missing_tags'][:10]:
            print(f"  - {fid}")
        if len(stats['missing_tags']) > 10:
            print(f"  ... and {len(stats['missing_tags']) - 10} more")
    
    print("\n=== Temporal Stage Coverage ===")
    for stage, count in sorted(stats['temporal_coverage'].items()):
        print(f"{stage:20} {count:4} frameworks")
    
    print("\n=== Problem Archetype Coverage ===")
    for problem, count in sorted(stats['problem_coverage'].items()):
        print(f"{problem:30} {count:4} frameworks")
    
    print("\n=== Industry Coverage ===")
    for industry, count in sorted(stats['industry_coverage'].items()):
        print(f"{industry:25} {count:4} frameworks")
    
    print("\n=== Complexity Distribution ===")
    for complexity, count in sorted(stats['complexity_distribution'].items()):
        print(f"{complexity:15} {count:4} frameworks")
    
    print(f"\n=== Issues Found ===")
    print(f"Frameworks with issues: {len(issues)}")
    print(f"Team size issues: {stats['team_size_issues']}")
    
    if issues:
        print("\nSample issues:")
        for fid, issue_list in list(issues.items())[:10]:
            print(f"\n{fid}:")
            for issue in issue_list:
                print(f"  - {issue}")


async def run_tests():
    """Run all tests"""
    from framework_intelligence.integrated_framework_selector import IntegratedFrameworkSelector
    from strategic_context_engine import StrategicContextEngine
    
    # Test scenarios
    scenarios = [
        ("Early Stage SaaS", {
            "startup_name": "TestStartup",
            "funding_stage": "pre_seed",
            "sector": "saas_b2b",
            "team_size_full_time": 3,
            "annual_revenue_usd": 0,
            "burn_rate_usd": 10000,
            "runway_months": 12,
            "b2b_or_b2c": "b2b"
        }),
        ("Growth Stage with Portfolio", {
            "startup_name": "GrowthCo",
            "funding_stage": "series_a", 
            "sector": "saas_b2b",
            "team_size_full_time": 25,
            "annual_revenue_usd": 2000000,
            "burn_rate_usd": 200000,
            "runway_months": 18,
            "b2b_or_b2c": "b2b"
        }),
        ("Marketplace Platform", {
            "startup_name": "MarketCo",
            "funding_stage": "seed",
            "sector": "marketplace",
            "team_size_full_time": 10,
            "annual_revenue_usd": 500000,
            "burn_rate_usd": 50000,
            "runway_months": 15,
            "b2b_or_b2c": "b2c"
        })
    ]
    
    for name, data in scenarios:
        print(f"\n--- {name} ---")
        
        # Build context
        context_engine = StrategicContextEngine()
        context = await context_engine.build_company_context(data)
        
        # Select frameworks
        selector = IntegratedFrameworkSelector()
        frameworks = await selector.select_frameworks(
            strategic_context=context,
            max_frameworks=3,
            use_academic_logic=True
        )
        
        print(f"Challenges: {', '.join(context.challenges[:3])}")
        print("Selected frameworks:")
        for i, f in enumerate(frameworks, 1):
            print(f"  {i}. {f.base_framework.name} (score: {f.selection_metadata.get('fit_score', 0):.1f})")

if __name__ == "__main__":
    # Run validation
    issues, stats = validate_tags()
    print_validation_report(issues, stats)
    
    # Run scenario tests
    import asyncio
    print("\n\n=== Testing Framework Selection Scenarios ===")
    asyncio.run(run_tests())