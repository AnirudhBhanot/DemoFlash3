#!/usr/bin/env python3
"""
Comprehensive update of all framework use cases with specific, actionable scenarios
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from framework_intelligence.framework_database import FRAMEWORKS, FrameworkCategory
import re

def generate_specific_use_cases(framework_id, framework):
    """Generate specific use cases based on framework type and purpose"""
    
    use_cases = []
    name_lower = framework.name.lower()
    desc_lower = framework.description.lower()
    
    # BCG Matrix specific
    if "bcg" in framework_id and "matrix" in name_lower:
        use_cases = [
            "Quarterly portfolio review to reallocate resources across product lines",
            "Deciding which products to sunset when facing budget constraints",
            "Identifying cash cows to fund new growth initiatives",
            "Evaluating acquisition targets based on portfolio fit",
            "Planning divestment of low-growth, low-share business units"
        ]
    
    # Porter's Five Forces
    elif "porter" in framework_id and "five forces" in name_lower:
        use_cases = [
            "Assessing market attractiveness before $1M+ investment decision",
            "Developing competitive strategy against new market entrants",
            "Negotiating with suppliers when switching costs are high",
            "Deciding whether to vertically integrate or outsource",
            "Evaluating threat of substitute products/services"
        ]
    
    # Lean Canvas
    elif "lean_canvas" in framework_id:
        use_cases = [
            "Documenting business model assumptions for seed funding pitch",
            "Weekly iteration of business model based on customer interviews",
            "Aligning founding team on problem-solution fit",
            "Identifying riskiest assumptions to test first",
            "Pivoting business model after failed experiments"
        ]
    
    # Customer Development
    elif "customer_development" in framework_id:
        use_cases = [
            "Validating problem-solution fit through 50+ customer interviews",
            "Testing willingness to pay before building product",
            "Identifying early adopters for beta testing",
            "Refining value proposition based on customer feedback",
            "Deciding when to pivot vs persevere"
        ]
    
    # Jobs to be Done
    elif "jobs_to_be_done" in framework_id or "jtbd" in framework_id:
        use_cases = [
            "Discovering unmet needs competitors haven't addressed",
            "Prioritizing product features based on job importance",
            "Expanding market by addressing adjacent jobs",
            "Creating marketing messages that resonate with job performers",
            "Identifying why customers hire and fire your product"
        ]
    
    # Unit Economics
    elif "unit_economics" in framework_id:
        use_cases = [
            "Determining if business model can ever be profitable",
            "Setting minimum viable pricing for sustainability",
            "Identifying which customer segments to focus on or avoid",
            "Calculating how much to spend on customer acquisition",
            "Projecting path to profitability at different growth rates"
        ]
    
    # Growth frameworks
    elif "growth" in name_lower or "growth" in framework_id:
        if "loop" in name_lower:
            use_cases = [
                "Designing viral mechanics to reduce CAC by 50%",
                "Building content strategy that compounds over time",
                "Creating user-generated content flywheel",
                "Connecting product usage to new user acquisition",
                "Optimizing referral programs for exponential growth"
            ]
        elif "product_led" in framework_id:
            use_cases = [
                "Transitioning from sales-led to product-led GTM",
                "Designing free tier that converts to paid at 3%+",
                "Reducing time-to-value from days to minutes",
                "Building in-product upgrade experiences",
                "Achieving negative net churn through expansion"
            ]
        else:
            use_cases = [
                "Scaling from $1M to $10M ARR efficiently",
                "Choosing between paid acquisition vs organic growth",
                "Building predictable revenue growth engine",
                "Identifying highest-leverage growth experiments",
                "Achieving T2D3 growth trajectory"
            ]
    
    # Financial frameworks
    elif framework.category == FrameworkCategory.FINANCIAL:
        if "ltv" in name_lower or "cac" in name_lower:
            use_cases = [
                "Evaluating ROI of different marketing channels",
                "Setting acquisition spend limits by channel",
                "Improving retention to increase LTV by 2x",
                "Achieving LTV:CAC ratio > 3:1 within 12 months",
                "Deciding between growth and profitability focus"
            ]
        elif "burn" in name_lower or "runway" in name_lower:
            use_cases = [
                "Extending runway from 12 to 18+ months",
                "Planning hiring based on burn rate targets",
                "Preparing for Series A with healthy metrics",
                "Managing cash during market downturns",
                "Balancing growth spend vs runway extension"
            ]
        elif "break" in name_lower and "even" in name_lower:
            use_cases = [
                "Determining minimum viable scale for profitability",
                "Setting revenue targets for sustainability",
                "Identifying fixed vs variable cost optimization",
                "Planning path from negative to positive margins",
                "Evaluating different pricing strategies"
            ]
    
    # Strategy frameworks - Industry specific
    elif "competitive_positioning" in framework_id:
        industry = framework_id.split("_")[-1]
        use_cases = [
            f"Entering {industry} market against established players",
            f"Differentiating in commoditized {industry} sector",
            f"Building defensible moat in {industry}",
            f"Responding to {industry} disruption threats",
            f"Capturing premium pricing in {industry}"
        ]
    
    # Market entry frameworks
    elif "market_entry" in framework_id:
        industry = framework_id.split("_")[-1]
        use_cases = [
            f"Launching in {industry} with zero brand recognition",
            f"Choosing go-to-market strategy for {industry}",
            f"Building distribution channels in {industry}",
            f"Timing {industry} market entry for maximum impact",
            f"Selecting beachhead segment in {industry}"
        ]
    
    # Innovation frameworks
    elif framework.category == FrameworkCategory.INNOVATION:
        if "design_thinking" in framework_id:
            use_cases = [
                "Redesigning user experience to increase NPS by 30 points",
                "Creating breakthrough products for unmet needs",
                "Solving complex B2B workflow challenges",
                "Building empathy with users through research",
                "Innovating in highly regulated industries"
            ]
        elif "lean_startup" in framework_id:
            use_cases = [
                "Validating B2B SaaS idea with <$10K investment",
                "Building MVP in 4 weeks to test core hypothesis",
                "Pivoting based on customer feedback patterns",
                "Achieving product-market fit within 6 months",
                "Iterating business model for unit economics"
            ]
        elif "stage_gate" in framework_id:
            use_cases = [
                "Managing 10+ concurrent innovation projects",
                "Allocating R&D budget across risk levels",
                "Killing projects that miss stage criteria",
                "Accelerating high-potential initiatives",
                "Balancing incremental vs breakthrough innovation"
            ]
    
    # Operations frameworks
    elif framework.category == FrameworkCategory.OPERATIONS:
        if "lean" in name_lower:
            use_cases = [
                "Reducing operational costs by 30% in 6 months",
                "Eliminating waste from manufacturing process",
                "Improving delivery times from weeks to days",
                "Building continuous improvement culture",
                "Scaling operations 10x without 10x costs"
            ]
        elif "six_sigma" in framework_id:
            use_cases = [
                "Achieving 99.9% quality in production",
                "Reducing customer complaints by 80%",
                "Standardizing processes across locations",
                "Meeting regulatory compliance requirements",
                "Improving first-call resolution to 95%"
            ]
        elif "agile" in framework_id:
            use_cases = [
                "Transitioning 100+ person org to agile",
                "Reducing release cycles from months to days",
                "Improving developer productivity by 40%",
                "Building autonomous product teams",
                "Implementing DevOps transformation"
            ]
    
    # Leadership frameworks
    elif framework.category == FrameworkCategory.LEADERSHIP:
        use_cases = [
            "Leading through hypergrowth from 50 to 500 employees",
            "Building high-performance culture remotely",
            "Managing through organizational transformation",
            "Developing next generation of leaders",
            "Aligning teams around new strategic direction"
        ]
    
    # Product frameworks
    elif framework.category == FrameworkCategory.PRODUCT:
        if "kano" in framework_id:
            use_cases = [
                "Prioritizing features for next product release",
                "Identifying delighters vs must-haves",
                "Reducing feature bloat by 50%",
                "Creating differentiation through delighters",
                "Optimizing product-market fit"
            ]
        elif "rice" in framework_id:
            use_cases = [
                "Prioritizing engineering roadmap for Q4",
                "Choosing between competing feature requests",
                "Allocating resources across product teams",
                "Balancing technical debt vs new features",
                "Maximizing impact with limited resources"
            ]
    
    # Marketing frameworks
    elif framework.category == FrameworkCategory.MARKETING:
        if "4ps" in framework_id or "marketing_mix" in framework_id:
            use_cases = [
                "Launching new product in competitive market",
                "Repositioning brand for premium segment",
                "Optimizing pricing strategy for growth",
                "Building distribution strategy from scratch",
                "Creating integrated marketing campaign"
            ]
        elif "stp" in framework_id:
            use_cases = [
                "Identifying most profitable customer segments",
                "Focusing resources on highest-value targets",
                "Differentiating from 5+ direct competitors",
                "Building positioning for Series A pitch",
                "Expanding from one segment to three"
            ]
    
    # Default use cases if none matched
    if not use_cases:
        if framework.category == FrameworkCategory.STRATEGY:
            use_cases = [
                "Making critical strategic decisions with incomplete data",
                "Aligning leadership team on strategic direction",
                "Evaluating build vs buy vs partner options",
                "Planning next phase of company growth",
                "Responding to competitive threats"
            ]
        else:
            use_cases = [
                f"Solving {framework.category.value.lower()} challenges systematically",
                f"Improving {framework.category.value.lower()} performance metrics",
                f"Building competitive advantage through {framework.category.value.lower()}",
                f"Scaling {framework.category.value.lower()} from startup to growth stage",
                f"Optimizing {framework.category.value.lower()} for efficiency"
            ]
    
    return use_cases[:5]  # Return top 5 use cases

def update_framework_database():
    """Update all frameworks with enhanced use cases"""
    
    print("Updating framework use cases...")
    
    # Read the current database file
    db_file = "framework_intelligence/framework_database.py"
    with open(db_file, 'r') as f:
        content = f.read()
    
    updated_count = 0
    
    # For each framework, update its when_to_use field
    for framework_id, framework in FRAMEWORKS.items():
        # Generate new use cases
        new_use_cases = generate_specific_use_cases(framework_id, framework)
        
        if new_use_cases:
            # Find the framework definition in the file
            pattern = rf'"{framework_id}":\s*Framework\([^)]+'
            match = re.search(pattern, content, re.DOTALL)
            
            if match:
                # Extract the framework definition
                framework_def = match.group(0)
                
                # Find the when_to_use field
                when_pattern = r'when_to_use=\[(.*?)\]'
                when_match = re.search(when_pattern, framework_def, re.DOTALL)
                
                if when_match:
                    # Format new use cases
                    formatted_cases = ',\n            '.join([f'"{case}"' for case in new_use_cases])
                    new_when_to_use = f'when_to_use=[\n            {formatted_cases}\n        ]'
                    
                    # Replace in the framework definition
                    new_framework_def = re.sub(when_pattern, new_when_to_use, framework_def, flags=re.DOTALL)
                    
                    # Replace in the content
                    content = content.replace(framework_def, new_framework_def)
                    updated_count += 1
    
    # Write back the updated content
    with open(db_file, 'w') as f:
        f.write(content)
    
    print(f"Updated {updated_count} frameworks with enhanced use cases")
    
    # Verify the updates
    print("\nVerifying updates...")
    
    # Reload the module to check
    import importlib
    import framework_intelligence.framework_database
    importlib.reload(framework_intelligence.framework_database)
    
    # Check a few examples
    from framework_intelligence.framework_database import FRAMEWORKS as UPDATED_FRAMEWORKS
    
    examples = ["bcg_matrix", "porters_five_forces", "lean_canvas", "unit_economics"]
    
    print("\nSample updated use cases:")
    for ex in examples:
        if ex in UPDATED_FRAMEWORKS:
            framework = UPDATED_FRAMEWORKS[ex]
            print(f"\n{framework.name}:")
            for i, use_case in enumerate(framework.when_to_use[:3], 1):
                print(f"  {i}. {use_case}")

if __name__ == "__main__":
    update_framework_database()