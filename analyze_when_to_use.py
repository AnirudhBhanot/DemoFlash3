#!/usr/bin/env python3
"""
Analyze when_to_use field coverage and quality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from framework_intelligence.framework_database import FRAMEWORKS
from collections import defaultdict
import json

def analyze_when_to_use():
    """Analyze when_to_use coverage"""
    
    stats = {
        "total_frameworks": len(FRAMEWORKS),
        "with_when_to_use": 0,
        "empty_when_to_use": 0,
        "single_use_case": 0,
        "multiple_use_cases": 0,
        "avg_use_cases": 0,
        "by_category": defaultdict(lambda: {
            "total": 0, 
            "with_when_to_use": 0, 
            "avg_use_cases": 0,
            "total_use_cases": 0
        })
    }
    
    issues = []
    total_use_cases = 0
    
    for framework_id, framework in FRAMEWORKS.items():
        category = framework.category.value
        stats["by_category"][category]["total"] += 1
        
        if framework.when_to_use:
            use_case_count = len(framework.when_to_use)
            total_use_cases += use_case_count
            
            stats["with_when_to_use"] += 1
            stats["by_category"][category]["with_when_to_use"] += 1
            stats["by_category"][category]["total_use_cases"] += use_case_count
            
            if use_case_count == 1:
                stats["single_use_case"] += 1
            else:
                stats["multiple_use_cases"] += 1
            
            # Check for quality issues
            for use_case in framework.when_to_use:
                if len(use_case) < 10:
                    issues.append({
                        "framework": framework.name,
                        "issue": "Very short use case",
                        "use_case": use_case
                    })
                if not use_case.strip():
                    issues.append({
                        "framework": framework.name,
                        "issue": "Empty use case"
                    })
        else:
            stats["empty_when_to_use"] += 1
    
    # Calculate averages
    if stats["with_when_to_use"] > 0:
        stats["avg_use_cases"] = total_use_cases / stats["with_when_to_use"]
    
    for category, data in stats["by_category"].items():
        if data["with_when_to_use"] > 0:
            data["avg_use_cases"] = data["total_use_cases"] / data["with_when_to_use"]
    
    return stats, issues

def print_sample_use_cases():
    """Print some sample use cases for reference"""
    
    print("\n=== Sample When To Use Cases ===")
    
    samples = ["bcg_matrix", "porters_five_forces", "lean_canvas", "jobs_to_be_done", "unit_economics"]
    
    for framework_id in samples:
        if framework_id in FRAMEWORKS:
            framework = FRAMEWORKS[framework_id]
            print(f"\n{framework.name}:")
            if framework.when_to_use:
                for i, use_case in enumerate(framework.when_to_use[:3], 1):
                    print(f"  {i}. {use_case}")
            else:
                print("  No use cases defined")

def generate_enhanced_use_cases():
    """Generate enhanced use cases for frameworks that need them"""
    
    enhancements = []
    
    for framework_id, framework in FRAMEWORKS.items():
        if not framework.when_to_use or len(framework.when_to_use) < 3:
            # Generate more specific use cases based on the framework
            enhanced_cases = generate_use_cases_for_framework(framework)
            
            enhancements.append({
                "framework_id": framework_id,
                "framework_name": framework.name,
                "current_use_cases": framework.when_to_use or [],
                "suggested_additions": enhanced_cases
            })
    
    return enhancements

def generate_use_cases_for_framework(framework):
    """Generate specific use cases based on framework characteristics"""
    
    use_cases = []
    
    # Strategy frameworks
    if framework.category == FrameworkCategory.STRATEGY:
        if "portfolio" in framework.name.lower():
            use_cases.extend([
                "Deciding which products/services to invest in or divest",
                "Allocating resources across multiple business units",
                "Identifying underperforming assets that drain resources",
                "Balancing risk across your product portfolio"
            ])
        elif "competitive" in framework.name.lower():
            use_cases.extend([
                "Entering a new market with established competitors",
                "Defending market position against new entrants",
                "Identifying competitive advantages to leverage",
                "Assessing industry attractiveness before investment"
            ])
        elif "growth" in framework.name.lower():
            use_cases.extend([
                "Exploring new growth opportunities systematically",
                "Deciding between market penetration vs. diversification",
                "Planning international expansion strategies",
                "Identifying adjacent markets to enter"
            ])
    
    # Innovation frameworks
    elif framework.category == FrameworkCategory.INNOVATION:
        if "lean" in framework.name.lower():
            use_cases.extend([
                "Validating business ideas with minimal resources",
                "Testing product-market fit before scaling",
                "Iterating quickly based on customer feedback",
                "Reducing time and cost of product development"
            ])
        elif "design" in framework.name.lower():
            use_cases.extend([
                "Solving complex user experience problems",
                "Creating innovative products that users love",
                "Redesigning services for better customer satisfaction",
                "Building empathy with your target users"
            ])
    
    # Financial frameworks
    elif framework.category == FrameworkCategory.FINANCIAL:
        if "unit economics" in framework.name.lower():
            use_cases.extend([
                "Determining if your business model is sustainable",
                "Setting pricing strategies for profitability",
                "Identifying which customer segments are most profitable",
                "Making decisions about customer acquisition spending"
            ])
        elif "ltv" in framework.name.lower() or "cac" in framework.name.lower():
            use_cases.extend([
                "Evaluating marketing channel effectiveness",
                "Setting customer acquisition budgets",
                "Determining payback periods for investments",
                "Optimizing customer retention strategies"
            ])
    
    return use_cases[:4]  # Return up to 4 use cases

if __name__ == "__main__":
    stats, issues = analyze_when_to_use()
    
    print("=== When To Use Analysis ===")
    print(f"\nTotal frameworks: {stats['total_frameworks']}")
    print(f"With when_to_use: {stats['with_when_to_use']}")
    print(f"Empty when_to_use: {stats['empty_when_to_use']}")
    print(f"Single use case: {stats['single_use_case']}")
    print(f"Multiple use cases: {stats['multiple_use_cases']}")
    print(f"Average use cases per framework: {stats['avg_use_cases']:.1f}")
    
    print("\n=== By Category ===")
    for category, data in sorted(stats["by_category"].items()):
        print(f"\n{category}:")
        print(f"  Total: {data['total']}")
        print(f"  With when_to_use: {data['with_when_to_use']}")
        print(f"  Average use cases: {data['avg_use_cases']:.1f}")
    
    if issues:
        print(f"\n=== Quality Issues ({len(issues)}) ===")
        for issue in issues[:5]:
            print(f"- {issue}")
    
    print_sample_use_cases()
    
    # Generate report
    report = {
        "stats": stats,
        "issues": issues
    }
    
    with open("when_to_use_analysis.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print("\nDetailed analysis saved to when_to_use_analysis.json")