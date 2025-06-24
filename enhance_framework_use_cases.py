#!/usr/bin/env python3
"""
Enhance framework use cases with more specific, actionable scenarios
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from framework_intelligence.framework_database import FRAMEWORKS, FrameworkCategory
import json

def analyze_use_case_quality():
    """Analyze the quality and specificity of current use cases"""
    
    generic_phrases = [
        "analyzing", "understanding", "evaluating", "assessing",
        "making decisions", "planning", "developing", "improving"
    ]
    
    quality_issues = {
        "too_generic": [],
        "too_short": [],
        "not_actionable": [],
        "missing_context": []
    }
    
    for framework_id, framework in FRAMEWORKS.items():
        for use_case in framework.when_to_use:
            # Check if too generic
            if any(phrase in use_case.lower() and len(use_case.split()) < 5 
                   for phrase in generic_phrases):
                quality_issues["too_generic"].append({
                    "framework": framework.name,
                    "use_case": use_case
                })
            
            # Check if too short
            if len(use_case.split()) < 4:
                quality_issues["too_short"].append({
                    "framework": framework.name,
                    "use_case": use_case
                })
            
            # Check if not actionable (no verb or action)
            action_verbs = ["decide", "choose", "allocate", "prioritize", "launch", 
                          "enter", "exit", "invest", "divest", "build", "scale"]
            if not any(verb in use_case.lower() for verb in action_verbs):
                quality_issues["not_actionable"].append({
                    "framework": framework.name,
                    "use_case": use_case
                })
    
    return quality_issues

def generate_enhanced_use_cases():
    """Generate enhanced, specific use cases for all frameworks"""
    
    enhancements = {}
    
    # Define use case templates by category
    use_case_templates = {
        FrameworkCategory.STRATEGY: {
            "portfolio": [
                "Deciding which product lines to sunset when resources are limited",
                "Allocating R&D budget across products with different growth rates",
                "Identifying which business units to sell or spin off",
                "Prioritizing investment between high-growth/low-share vs low-growth/high-share products",
                "Quarterly portfolio review to rebalance resource allocation"
            ],
            "competitive": [
                "Entering a market dominated by 3-5 major players",
                "Defending against a new low-cost competitor",
                "Deciding whether to compete on price vs differentiation",
                "Evaluating acquisition targets to strengthen competitive position",
                "Responding to competitor's new product launch"
            ],
            "growth": [
                "Choosing between geographic expansion vs product line extension",
                "Deciding whether to build, buy, or partner for new capabilities",
                "Prioritizing organic growth vs acquisition opportunities",
                "Entering adjacent markets while maintaining core business",
                "Scaling from $1M to $10M ARR"
            ],
            "market_entry": [
                "Launching in a new geographic market",
                "Entering a regulated industry for the first time",
                "Deciding on direct sales vs channel partnership strategy",
                "Timing market entry to maximize first-mover advantage",
                "Choosing initial target customer segment in new market"
            ],
            "disruption": [
                "Responding to digital transformation in traditional industry",
                "Cannibalizing existing products with innovative offerings",
                "Building new business model while maintaining legacy revenue",
                "Identifying opportunities to disrupt incumbent players",
                "Protecting against disruption from startups"
            ]
        },
        FrameworkCategory.INNOVATION: {
            "lean": [
                "Testing product-market fit with less than $50K budget",
                "Validating B2B SaaS idea before writing code",
                "Pivoting based on customer feedback after 3 months",
                "Building MVP to test core value proposition",
                "Iterating pricing model based on early customer data"
            ],
            "design": [
                "Redesigning onboarding to reduce 50% drop-off rate",
                "Creating new product category that doesn't exist yet",
                "Solving complex workflow problems for enterprise users",
                "Improving NPS score from 20 to 50+",
                "Designing for accessibility and inclusion"
            ],
            "stage_gate": [
                "Managing multiple innovation projects with limited resources",
                "Deciding which projects to kill vs accelerate",
                "Balancing incremental vs breakthrough innovation",
                "Aligning innovation pipeline with strategic goals",
                "Reducing time-to-market by 30%"
            ]
        },
        FrameworkCategory.GROWTH: {
            "viral": [
                "Achieving viral coefficient > 1.0 for consumer app",
                "Building referral program that drives 40% of growth",
                "Optimizing sharing mechanics for maximum reach",
                "Reducing viral cycle time from 7 to 3 days",
                "Leveraging network effects for exponential growth"
            ],
            "growth_loops": [
                "Building self-reinforcing acquisition channels",
                "Creating content loop that drives SEO traffic",
                "Designing product features that increase user engagement",
                "Connecting user actions to acquisition metrics",
                "Scaling from 10K to 100K users"
            ],
            "product_led": [
                "Transitioning from sales-led to product-led growth",
                "Designing free tier that converts to paid",
                "Building in-product upgrade prompts",
                "Reducing time-to-value for new users",
                "Achieving negative churn through expansion revenue"
            ]
        },
        FrameworkCategory.FINANCIAL: {
            "unit_economics": [
                "Determining sustainable customer acquisition spend",
                "Setting pricing to achieve positive unit economics",
                "Identifying unprofitable customer segments to avoid",
                "Projecting path to profitability based on current metrics",
                "Optimizing gross margins through operational efficiency"
            ],
            "ltv_cac": [
                "Evaluating performance of different acquisition channels",
                "Setting marketing budget based on payback period",
                "Improving retention to increase LTV by 50%",
                "Deciding whether to raise prices vs reduce CAC",
                "Achieving LTV:CAC ratio > 3:1"
            ],
            "burn_rate": [
                "Extending runway from 12 to 18 months",
                "Deciding between growth and profitability",
                "Planning headcount based on burn rate targets",
                "Preparing for fundraising with 6 months runway",
                "Managing cash during economic downturn"
            ]
        },
        FrameworkCategory.CUSTOMER: {
            "jobs": [
                "Identifying unmet needs in existing market",
                "Designing solution for specific job-to-be-done",
                "Differentiating from competitors on job performance",
                "Expanding TAM by addressing new jobs",
                "Prioritizing features based on job importance"
            ],
            "journey": [
                "Reducing customer churn at critical touchpoints",
                "Optimizing conversion funnel from trial to paid",
                "Identifying moments of delight to amplify",
                "Fixing broken experiences causing support tickets",
                "Personalizing journey for different segments"
            ]
        },
        FrameworkCategory.OPERATIONS: {
            "lean": [
                "Reducing operational costs by 30%",
                "Eliminating waste in production process",
                "Improving delivery time from 10 to 3 days",
                "Implementing continuous improvement culture",
                "Scaling operations without proportional cost increase"
            ],
            "six_sigma": [
                "Reducing defect rate below 0.1%",
                "Improving customer satisfaction scores to 95%+",
                "Standardizing processes across multiple locations",
                "Achieving ISO certification requirements",
                "Reducing variance in service delivery"
            ],
            "agile": [
                "Transitioning from waterfall to agile development",
                "Improving release frequency from quarterly to weekly",
                "Building cross-functional product teams",
                "Implementing CI/CD pipeline",
                "Reducing time from idea to production"
            ]
        }
    }
    
    # Generate enhanced use cases for each framework
    for framework_id, framework in FRAMEWORKS.items():
        category = framework.category
        enhanced_cases = []
        
        # Find matching templates based on framework name and description
        framework_lower = framework.name.lower()
        desc_lower = framework.description.lower()
        
        # Match templates
        for key, templates in use_case_templates.get(category, {}).items():
            if key in framework_lower or key in desc_lower or key in framework_id:
                enhanced_cases.extend(templates[:5])
                break
        
        # If no specific match, use category defaults
        if not enhanced_cases and category in use_case_templates:
            # Get first template set for the category
            first_key = next(iter(use_case_templates[category]))
            enhanced_cases = use_case_templates[category][first_key][:3]
        
        # Add framework-specific cases based on components
        if "customer" in framework_lower:
            enhanced_cases.append("Understanding why customers switch to competitors")
        if "market" in framework_lower:
            enhanced_cases.append("Sizing addressable market for new product launch")
        if "competitive" in framework_lower:
            enhanced_cases.append("Developing competitive response strategy")
        if "innovation" in framework_lower:
            enhanced_cases.append("Building innovation pipeline for next 3 years")
        if "growth" in framework_lower:
            enhanced_cases.append("Scaling from $10M to $100M revenue")
        
        if enhanced_cases:
            enhancements[framework_id] = {
                "framework_name": framework.name,
                "current_use_cases": framework.when_to_use,
                "enhanced_use_cases": enhanced_cases[:5]  # Limit to 5
            }
    
    return enhancements

def create_use_case_update_script(enhancements):
    """Create a script to update the framework database with enhanced use cases"""
    
    script_content = '''#!/usr/bin/env python3
"""
Update framework database with enhanced use cases
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from framework_intelligence.framework_database import FRAMEWORKS

# Enhanced use cases to add
use_case_updates = '''
    
    script_content += json.dumps(enhancements, indent=2)
    
    script_content += '''

def update_framework_use_cases():
    """Update frameworks with enhanced use cases"""
    
    updated_count = 0
    
    for framework_id, updates in use_case_updates.items():
        if framework_id in FRAMEWORKS:
            framework = FRAMEWORKS[framework_id]
            
            # Combine current and enhanced use cases
            current_cases = set(framework.when_to_use)
            enhanced_cases = updates["enhanced_use_cases"]
            
            # Add enhanced cases that aren't duplicates
            new_cases = []
            for case in enhanced_cases:
                if case not in current_cases and len(case) > 20:  # Only add substantial cases
                    new_cases.append(case)
            
            if new_cases:
                # Keep best current cases and add new ones
                framework.when_to_use = framework.when_to_use[:3] + new_cases[:2]
                updated_count += 1
                print(f"Updated {framework.name} with {len(new_cases)} new use cases")
    
    print(f"\\nTotal frameworks updated: {updated_count}")
    
    # Save the updated database
    # This would need to be implemented to persist changes

if __name__ == "__main__":
    update_framework_use_cases()
'''
    
    with open("update_framework_use_cases.py", "w") as f:
        f.write(script_content)
    
    print("Update script created: update_framework_use_cases.py")

if __name__ == "__main__":
    # Analyze current quality
    quality_issues = analyze_use_case_quality()
    
    print("=== Use Case Quality Analysis ===")
    print(f"Too generic: {len(quality_issues['too_generic'])}")
    print(f"Too short: {len(quality_issues['too_short'])}")
    print(f"Not actionable: {len(quality_issues['not_actionable'])}")
    
    # Show examples
    if quality_issues['too_generic']:
        print("\nExamples of generic use cases:")
        for issue in quality_issues['too_generic'][:3]:
            print(f"  - {issue['framework']}: '{issue['use_case']}'")
    
    # Generate enhancements
    print("\n=== Generating Enhanced Use Cases ===")
    enhancements = generate_enhanced_use_cases()
    
    print(f"Generated enhancements for {len(enhancements)} frameworks")
    
    # Show sample enhancements
    print("\nSample enhancements:")
    for fid, enh in list(enhancements.items())[:3]:
        print(f"\n{enh['framework_name']}:")
        print("  Current:", enh['current_use_cases'][:2])
        print("  Enhanced:", enh['enhanced_use_cases'][:2])
    
    # Save enhancements
    with open("framework_use_case_enhancements.json", "w") as f:
        json.dump(enhancements, f, indent=2)
    
    print("\nEnhancements saved to framework_use_case_enhancements.json")
    
    # Create update script
    create_use_case_update_script(enhancements)