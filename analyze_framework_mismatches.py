#!/usr/bin/env python3
"""
Analyze all framework mismatches and generate a report
"""

from framework_intelligence.framework_tags_database import create_framework_tags_database
from framework_intelligence.framework_database import FRAMEWORKS
from framework_intelligence.framework_taxonomy import *
import json

# Get all data
tags_db = create_framework_tags_database()
tagged_frameworks = set(tags_db.keys())
defined_frameworks = set(FRAMEWORKS.keys())

# Find mismatches
missing_definitions = tagged_frameworks - defined_frameworks
missing_tags = defined_frameworks - tagged_frameworks

print(f"=== Framework Database Analysis ===")
print(f"Total frameworks with definitions: {len(defined_frameworks)}")
print(f"Total frameworks with tags: {len(tagged_frameworks)}")
print(f"Frameworks missing definitions: {len(missing_definitions)}")
print(f"Frameworks missing tags: {len(missing_tags)}")

# Analyze frameworks by category
category_count = {}
for fid, framework in FRAMEWORKS.items():
    cat = framework.category.value
    if cat not in category_count:
        category_count[cat] = {"total": 0, "tagged": 0, "untagged": []}
    category_count[cat]["total"] += 1
    if fid in tagged_frameworks:
        category_count[cat]["tagged"] += 1
    else:
        category_count[cat]["untagged"].append(fid)

print("\n=== Frameworks by Category ===")
for cat, data in sorted(category_count.items()):
    print(f"\n{cat}:")
    print(f"  Total: {data['total']}")
    print(f"  Tagged: {data['tagged']}")
    print(f"  Missing tags: {data['total'] - data['tagged']}")
    if data['untagged'] and len(data['untagged']) <= 5:
        print(f"  Untagged frameworks: {', '.join(data['untagged'])}")
    elif data['untagged']:
        print(f"  Untagged frameworks: {', '.join(data['untagged'][:5])}... (+{len(data['untagged'])-5} more)")

# Save detailed report
report = {
    "summary": {
        "total_definitions": len(defined_frameworks),
        "total_tags": len(tagged_frameworks),
        "missing_definitions": list(missing_definitions),
        "missing_tags_count": len(missing_tags)
    },
    "by_category": category_count,
    "missing_tags_sample": list(missing_tags)[:20]
}

with open("framework_mismatch_report.json", "w") as f:
    json.dump(report, f, indent=2)

print(f"\nDetailed report saved to framework_mismatch_report.json")

# Analyze patterns in untagged frameworks
print("\n=== Pattern Analysis ===")
industry_specific = [f for f in missing_tags if any(ind in f for ind in ["_saas", "_fintech", "_marketplace", "_healthtech", "_edtech", "_ecommerce", "_manufacturing", "_retail", "_media", "_gaming", "_mobile", "_enterprise", "_d2c"])]
print(f"Industry-specific variants without tags: {len(industry_specific)}")

print("\nSample industry-specific frameworks needing tags:")
for f in industry_specific[:10]:
    framework = FRAMEWORKS[f]
    print(f"  - {f}: {framework.name} ({framework.category.value})")