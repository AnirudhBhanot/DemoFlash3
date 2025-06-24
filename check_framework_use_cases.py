#!/usr/bin/env python3
"""
Check which frameworks have use cases and which don't
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from framework_intelligence.framework_database import FRAMEWORKS
from collections import defaultdict
import json

def analyze_use_cases():
    """Analyze use case coverage across all frameworks"""
    
    stats = {
        "total_frameworks": len(FRAMEWORKS),
        "with_use_cases": 0,
        "without_use_cases": 0,
        "empty_use_cases": 0,
        "by_category": defaultdict(lambda: {"total": 0, "with_use_cases": 0, "without_use_cases": 0})
    }
    
    missing_use_cases = []
    empty_use_cases = []
    
    for framework_id, framework in FRAMEWORKS.items():
        category = framework.category.value
        stats["by_category"][category]["total"] += 1
        
        # Check if framework has use_cases attribute
        if hasattr(framework, 'use_cases') and framework.use_cases:
            if len(framework.use_cases) > 0 and all(case.strip() for case in framework.use_cases):
                stats["with_use_cases"] += 1
                stats["by_category"][category]["with_use_cases"] += 1
            else:
                stats["empty_use_cases"] += 1
                stats["by_category"][category]["without_use_cases"] += 1
                empty_use_cases.append({
                    "id": framework_id,
                    "name": framework.name,
                    "category": category
                })
        else:
            stats["without_use_cases"] += 1
            stats["by_category"][category]["without_use_cases"] += 1
            missing_use_cases.append({
                "id": framework_id,
                "name": framework.name,
                "category": category,
                "description": framework.description[:100] + "..."
            })
    
    return stats, missing_use_cases, empty_use_cases

def print_report(stats, missing_use_cases, empty_use_cases):
    """Print the analysis report"""
    
    print("=== Framework Use Cases Analysis ===")
    print(f"\nTotal frameworks: {stats['total_frameworks']}")
    print(f"With use cases: {stats['with_use_cases']}")
    print(f"Without use cases: {stats['without_use_cases']}")
    print(f"Empty use cases: {stats['empty_use_cases']}")
    
    print("\n=== By Category ===")
    for category, data in sorted(stats["by_category"].items()):
        print(f"\n{category}:")
        print(f"  Total: {data['total']}")
        print(f"  With use cases: {data['with_use_cases']}")
        print(f"  Without use cases: {data['without_use_cases']}")
    
    if missing_use_cases:
        print(f"\n=== Frameworks Missing Use Cases ({len(missing_use_cases)}) ===")
        for i, fw in enumerate(missing_use_cases[:10], 1):
            print(f"\n{i}. {fw['name']} ({fw['id']})")
            print(f"   Category: {fw['category']}")
            print(f"   Description: {fw['description']}")
        
        if len(missing_use_cases) > 10:
            print(f"\n... and {len(missing_use_cases) - 10} more")
    
    # Save detailed report
    report = {
        "summary": stats,
        "missing_use_cases": missing_use_cases,
        "empty_use_cases": empty_use_cases
    }
    
    with open("framework_use_cases_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print("\nDetailed report saved to framework_use_cases_report.json")

def check_use_case_quality():
    """Check the quality of existing use cases"""
    
    quality_issues = []
    
    for framework_id, framework in FRAMEWORKS.items():
        if hasattr(framework, 'use_cases') and framework.use_cases:
            issues = []
            
            # Check for very short use cases
            short_cases = [case for case in framework.use_cases if len(case) < 20]
            if short_cases:
                issues.append(f"Very short use cases: {short_cases}")
            
            # Check for duplicate use cases
            if len(framework.use_cases) != len(set(framework.use_cases)):
                issues.append("Duplicate use cases found")
            
            # Check for generic use cases
            generic_terms = ["use this", "apply this", "implement this", "framework for"]
            generic_cases = [case for case in framework.use_cases 
                           if any(term in case.lower() for term in generic_terms)]
            if generic_cases:
                issues.append(f"Generic use cases: {generic_cases[:2]}")
            
            if issues:
                quality_issues.append({
                    "framework": framework.name,
                    "id": framework_id,
                    "issues": issues
                })
    
    if quality_issues:
        print(f"\n=== Use Case Quality Issues ({len(quality_issues)}) ===")
        for issue in quality_issues[:5]:
            print(f"\n{issue['framework']} ({issue['id']}):")
            for i in issue['issues']:
                print(f"  - {i}")

if __name__ == "__main__":
    stats, missing_use_cases, empty_use_cases = analyze_use_cases()
    print_report(stats, missing_use_cases, empty_use_cases)
    check_use_case_quality()