#!/usr/bin/env python3
"""
Comprehensive use case generator for all 557 frameworks
This ensures every framework has specific, actionable use cases
"""

import json

def generate_comprehensive_use_cases():
    """Generate use cases for all framework patterns"""
    
    # Comprehensive use case patterns
    use_case_patterns = {
        # BCG Matrix and variants
        "bcg": [
            "Quarterly portfolio review to reallocate resources across product lines",
            "Deciding which products to sunset when facing budget constraints", 
            "Identifying cash cows to fund new growth initiatives",
            "Evaluating acquisition targets based on portfolio fit",
            "Planning divestment of low-growth, low-share business units"
        ],
        
        # Porter's Five Forces
        "porter": [
            "Assessing market attractiveness before $1M+ investment decision",
            "Developing competitive strategy against new market entrants",
            "Negotiating with suppliers when switching costs are high",
            "Deciding whether to vertically integrate or outsource",
            "Evaluating threat of substitute products/services"
        ],
        
        # SWOT Analysis
        "swot": [
            "Annual strategic planning kickoff session",
            "Pre-merger due diligence assessment",
            "Competitive positioning for investor pitch",
            "Identifying quick wins and major risks",
            "Building consensus on strategic priorities"
        ],
        
        # Ansoff Matrix
        "ansoff": [
            "Choosing between market penetration vs product development",
            "Planning international expansion strategy",
            "Evaluating diversification opportunities",
            "Setting 3-year growth strategy",
            "Allocating resources across growth vectors"
        ],
        
        # Value Chain
        "value_chain": [
            "Identifying cost reduction opportunities across operations",
            "Finding differentiation opportunities in each activity",
            "Outsourcing vs insourcing decisions",
            "Digital transformation prioritization",
            "Competitive advantage analysis"
        ],
        
        # Blue Ocean
        "blue_ocean": [
            "Creating new market category",
            "Escaping price-based competition",
            "Redefining industry boundaries",
            "Finding uncontested market space",
            "Making competition irrelevant"
        ],
        
        # Lean Canvas
        "lean_canvas": [
            "Documenting business model for seed funding pitch",
            "Weekly iteration based on customer feedback",
            "Aligning founding team on key assumptions",
            "Identifying riskiest assumptions to test",
            "Pivoting business model after validation"
        ],
        
        # Customer Development
        "customer_development": [
            "Validating problem-solution fit with 50+ interviews",
            "Testing willingness to pay before building",
            "Finding and engaging early adopters",
            "Refining value proposition iteratively",
            "Deciding when to pivot vs persevere"
        ],
        
        # Jobs to be Done
        "jobs_to_be_done|jtbd": [
            "Discovering unmet needs competitors miss",
            "Prioritizing features by job importance",
            "Expanding TAM by addressing new jobs",
            "Creating resonant marketing messages",
            "Understanding hire/fire decisions"
        ],
        
        # Design Thinking
        "design_thinking": [
            "Redesigning UX to increase NPS by 30 points",
            "Creating breakthrough products for unmet needs",
            "Solving complex B2B workflow problems",
            "Building deep user empathy through research",
            "Innovating within regulatory constraints"
        ],
        
        # Lean Startup
        "lean_startup": [
            "Validating B2B SaaS with <$10K investment",
            "Building MVP in 4 weeks to test hypothesis",
            "Pivoting based on validated learning",
            "Achieving product-market fit in 6 months",
            "Iterating to sustainable unit economics"
        ],
        
        # Stage Gate
        "stage_gate": [
            "Managing portfolio of 10+ innovation projects",
            "Allocating R&D budget by risk/return",
            "Killing projects that miss gate criteria",
            "Fast-tracking high-potential initiatives",
            "Balancing incremental vs breakthrough"
        ],
        
        # Open Innovation
        "open_innovation": [
            "Building ecosystem of external partners",
            "Crowdsourcing solutions to R&D challenges",
            "Licensing technology to/from others",
            "Creating innovation challenges/hackathons",
            "Accelerating innovation through partnerships"
        ],
        
        # Growth Loops
        "growth_loop": [
            "Designing viral mechanics to reduce CAC 50%",
            "Building content strategy that compounds",
            "Creating user-generated content engine",
            "Connecting usage to acquisition metrics",
            "Optimizing referral program mechanics"
        ],
        
        # Product-Led Growth
        "product_led_growth|plg": [
            "Transitioning from sales-led to PLG motion",
            "Designing freemium tier for 3%+ conversion",
            "Reducing time-to-value to under 5 minutes",
            "Building in-product upgrade experiences",
            "Achieving negative churn via expansion"
        ],
        
        # Viral Coefficient
        "viral": [
            "Achieving K-factor > 1.0 for consumer app",
            "Optimizing sharing mechanics for reach",
            "Reducing viral cycle time by 50%",
            "Building network effects into product",
            "Creating FOMO-driven growth loops"
        ],
        
        # Land and Expand
        "land_and_expand": [
            "Penetrating enterprise with small initial deal",
            "Expanding from single team to entire org",
            "Increasing ACV by 10x over 2 years",
            "Building champions for internal selling",
            "Systematizing account expansion playbook"
        ],
        
        # Unit Economics
        "unit_economics": [
            "Determining path to profitability timeline",
            "Setting sustainable pricing strategy",
            "Identifying unprofitable segments to avoid",
            "Optimizing CAC payback period",
            "Modeling different growth scenarios"
        ],
        
        # LTV/CAC
        "ltv_cac|ltv/cac": [
            "Channel-level ROI optimization",
            "Setting acquisition spend guardrails",
            "Improving retention to double LTV",
            "Achieving 3:1 ratio in 12 months",
            "Balancing growth vs efficiency"
        ],
        
        # Burn Rate
        "burn_rate|runway": [
            "Extending runway from 12 to 18 months",
            "Right-sizing team for current stage",
            "Preparing metrics for next funding round",
            "Managing through market downturn",
            "Default alive vs default dead planning"
        ],
        
        # SaaS Metrics
        "saas_metrics": [
            "Building investor-ready metrics dashboard",
            "Diagnosing leaky bucket problems",
            "Benchmarking against industry standards",
            "Forecasting ARR growth accurately",
            "Optimizing rule of 40 performance"
        ],
        
        # Break-Even Analysis
        "break_even": [
            "Determining minimum viable scale",
            "Evaluating different pricing models",
            "Planning path to cash flow positive",
            "Analyzing fixed vs variable costs",
            "Setting revenue targets by quarter"
        ],
        
        # Lean Methodology
        "lean_methodology": [
            "Cutting operational costs by 30%",
            "Eliminating waste from core processes",
            "Building continuous improvement culture",
            "Scaling ops without scaling costs",
            "Improving efficiency metrics 2x"
        ],
        
        # Six Sigma
        "six_sigma": [
            "Achieving 99.9% quality standards",
            "Reducing defect rates by 90%",
            "Standardizing across locations",
            "Meeting compliance requirements",
            "Building data-driven culture"
        ],
        
        # Agile
        "agile_methodology": [
            "Transforming 100+ person organization",
            "Shipping weekly instead of quarterly",
            "Building autonomous product teams",
            "Implementing CI/CD practices",
            "Improving velocity by 40%"
        ],
        
        # Supply Chain
        "supply_chain": [
            "Reducing inventory costs by 25%",
            "Building supply chain resilience",
            "Optimizing supplier relationships",
            "Implementing just-in-time practices",
            "Managing global supply complexity"
        ],
        
        # Total Quality Management
        "tqm|total_quality": [
            "Building quality-first culture",
            "Reducing customer complaints 80%",
            "Implementing ISO standards",
            "Creating quality metrics dashboard",
            "Achieving operational excellence"
        ],
        
        # Marketing Mix 4Ps
        "4ps|marketing_mix": [
            "Launching product in new market",
            "Repositioning for premium segment",
            "Optimizing channel strategy",
            "Building integrated campaign",
            "Maximizing marketing ROI"
        ],
        
        # STP Marketing
        "stp_marketing": [
            "Identifying highest-value segments",
            "Focusing limited resources effectively",
            "Differentiating from 5+ competitors",
            "Building clear positioning statement",
            "Expanding from 1 to 3 segments"
        ],
        
        # Customer Journey
        "customer_journey": [
            "Reducing churn at key touchpoints",
            "Optimizing trial-to-paid conversion",
            "Identifying moments of delight",
            "Fixing broken experiences",
            "Personalizing by segment"
        ],
        
        # Content Marketing
        "content_marketing": [
            "Building organic traffic engine",
            "Creating thought leadership position",
            "Generating 100+ qualified leads/month",
            "Building community around content",
            "Measuring content ROI"
        ],
        
        # Brand Positioning
        "brand_positioning": [
            "Differentiating in crowded market",
            "Building premium brand perception",
            "Aligning brand with company values",
            "Creating emotional connection",
            "Measuring brand equity growth"
        ],
        
        # Kano Model
        "kano_model": [
            "Prioritizing features for next release",
            "Identifying must-haves vs delighters",
            "Reducing feature bloat by 50%",
            "Creating competitive differentiation",
            "Maximizing customer satisfaction"
        ],
        
        # RICE Prioritization
        "rice_prioritization": [
            "Planning quarterly roadmap",
            "Allocating engineering resources",
            "Balancing features vs tech debt",
            "Maximizing impact per sprint",
            "Aligning PM and engineering"
        ],
        
        # Product-Market Fit
        "product_market_fit|pmf": [
            "Measuring PMF quantitatively",
            "Iterating to strong PMF signal",
            "Knowing when to scale",
            "Finding PMF in new segment",
            "Maintaining PMF while scaling"
        ],
        
        # MVP Framework
        "mvp_framework": [
            "Defining truly minimal MVP",
            "Testing core value prop only",
            "Building MVP in 4 weeks",
            "Learning maximum with minimum",
            "Iterating based on MVP data"
        ],
        
        # Product Lifecycle
        "product_lifecycle": [
            "Planning sunset of legacy products",
            "Maximizing mature product profits",
            "Timing new product launches",
            "Managing portfolio lifecycle",
            "Extending product longevity"
        ],
        
        # Leadership frameworks
        "leadership|situational|transformational|servant": [
            "Leading through hypergrowth",
            "Building remote-first culture",
            "Managing organizational change",
            "Developing future leaders",
            "Aligning around new vision"
        ],
        
        # McKinsey 7S
        "mckinsey_7s|7s": [
            "Diagnosing organizational issues",
            "Planning major transformation",
            "Aligning all organizational elements",
            "Post-merger integration",
            "Building high-performance culture"
        ],
        
        # Organizational Culture
        "organizational_culture": [
            "Defining core values operationally",
            "Scaling culture 10x",
            "Merging different cultures",
            "Building innovation culture",
            "Measuring culture health"
        ],
        
        # Balanced Scorecard
        "balanced_scorecard": [
            "Aligning metrics with strategy",
            "Building exec dashboard",
            "Cascading goals organization-wide",
            "Balancing leading/lagging indicators",
            "Driving strategic execution"
        ],
        
        # OKR Framework
        "okr_framework": [
            "Implementing OKRs company-wide",
            "Aligning teams on outcomes",
            "Quarterly planning process",
            "Driving ambitious goals",
            "Measuring what matters"
        ],
        
        # Competitive Positioning (by industry)
        "competitive_positioning": [
            "Entering market against incumbents",
            "Building defensible market position",
            "Differentiating in commodity market",
            "Responding to new competitors",
            "Creating switching costs"
        ],
        
        # Market Entry (by industry)
        "market_entry": [
            "Launching with zero brand awareness",
            "Choosing go-to-market strategy",
            "Building distribution from scratch",
            "Timing market entry optimally",
            "Selecting beachhead segment"
        ],
        
        # Strategic Alliance (by industry)
        "strategic_alliance": [
            "Partnering for market access",
            "Building ecosystem strategy",
            "Structuring win-win partnerships",
            "Managing partner relationships",
            "Leveraging complementary assets"
        ],
        
        # Disruption Strategy (by industry)
        "disruption_strategy": [
            "Attacking incumbents from below",
            "Creating new market category",
            "Building asymmetric advantages",
            "Timing disruption correctly",
            "Defending against disruption"
        ],
        
        # Platform Strategy (by industry)
        "platform_strategy": [
            "Building two-sided marketplace",
            "Solving chicken-egg problem",
            "Creating network effects",
            "Monetizing platform effectively",
            "Defending platform position"
        ],
        
        # Ecosystem Strategy (by industry)
        "ecosystem_strategy": [
            "Orchestrating partner network",
            "Creating shared value",
            "Building platform ecosystem",
            "Managing ecosystem dynamics",
            "Capturing ecosystem value"
        ],
        
        # Value Migration (by industry)
        "value_migration": [
            "Identifying value shifts early",
            "Repositioning for new value",
            "Abandoning commoditized areas",
            "Moving up/down value chain",
            "Capturing migrating profits"
        ],
        
        # Strategic Options (by industry)
        "strategic_options": [
            "Evaluating build vs buy vs partner",
            "Analyzing strategic alternatives",
            "Making irreversible decisions",
            "Planning multiple scenarios",
            "Choosing optimal path forward"
        ],
        
        # Innovation Pipeline (by industry)
        "innovation_pipeline": [
            "Building 3-year innovation roadmap",
            "Balancing innovation portfolio",
            "Accelerating time-to-market",
            "Managing innovation funnel",
            "Measuring innovation ROI"
        ]
    }
    
    return use_case_patterns

def match_framework_to_pattern(framework_id, framework_name, framework_desc):
    """Match a framework to the best use case pattern"""
    
    patterns = generate_comprehensive_use_cases()
    
    # Normalize for matching
    id_lower = framework_id.lower()
    name_lower = framework_name.lower()
    desc_lower = framework_desc.lower()
    
    # Try exact matches first
    for pattern_key, use_cases in patterns.items():
        # Handle multiple keys (e.g., "ltv_cac|ltv/cac")
        keys = pattern_key.split("|")
        
        for key in keys:
            # Check if key appears in framework id, name, or description
            if (key in id_lower or 
                key in name_lower or 
                key in desc_lower or
                (len(key) > 5 and key in id_lower.replace("_", ""))):
                return use_cases
    
    # Try partial matches for compound frameworks
    if "_" in framework_id:
        parts = framework_id.split("_")
        
        # Check each part
        for part in parts:
            if len(part) > 3:  # Skip short words
                for pattern_key, use_cases in patterns.items():
                    if part in pattern_key.split("|")[0]:
                        return use_cases
    
    # Industry-specific framework handling
    industries = ["technology", "healthcare", "finance", "retail", "manufacturing", 
                  "education", "energy", "transportation", "hospitality", "media",
                  "telecommunications", "pharma", "automotive", "aerospace", 
                  "agriculture", "construction", "logistics", "ecommerce", "saas",
                  "consulting", "insurance", "real_estate", "gaming", "sports",
                  "entertainment", "startups", "enterprises", "smes", "nonprofits",
                  "government", "b2b", "b2c", "d2c", "marketplaces", "platforms",
                  "digital", "mobile", "cloud", "ai_ml", "blockchain", "remote",
                  "hybrid", "global", "local", "emerging_markets"]
    
    # Check if it's an industry-specific variant
    for industry in industries:
        if industry in id_lower:
            # Find the base framework type
            base_framework = id_lower.replace(f"_{industry}", "").replace(f"{industry}_", "")
            
            # Try to match the base framework
            for pattern_key, use_cases in patterns.items():
                if base_framework in pattern_key:
                    # Customize use cases for the industry
                    customized = []
                    for use_case in use_cases:
                        # Make it industry-specific
                        customized.append(use_case.replace("market", f"{industry} market")
                                                 .replace("industry", industry)
                                                 .replace("sector", f"{industry} sector"))
                    return customized
    
    # Default use cases based on category
    if "strategy" in framework_id or "strategic" in name_lower:
        return [
            "Making critical strategic decisions under uncertainty",
            "Aligning leadership on strategic priorities", 
            "Evaluating strategic options systematically",
            "Building competitive advantage sustainably",
            "Planning next phase of growth"
        ]
    elif "innovation" in framework_id or "innovation" in name_lower:
        return [
            "Building systematic innovation process",
            "Accelerating innovation cycle time",
            "Balancing innovation portfolio risk",
            "Measuring innovation impact/ROI",
            "Creating innovation culture"
        ]
    elif "growth" in framework_id or "growth" in name_lower:
        return [
            "Scaling from current stage to next",
            "Identifying highest-leverage growth levers",
            "Building predictable growth engine",
            "Optimizing growth efficiency metrics",
            "Achieving sustainable growth rate"
        ]
    elif "financial" in framework_id or "finance" in name_lower:
        return [
            "Making data-driven financial decisions",
            "Optimizing financial performance",
            "Planning for financial sustainability",
            "Managing financial risks effectively",
            "Achieving financial targets"
        ]
    else:
        return [
            f"Solving {framework_name} challenges systematically",
            f"Improving {framework_name} performance significantly", 
            f"Building competitive advantage through {framework_name}",
            f"Scaling {framework_name} practices effectively",
            f"Optimizing {framework_name} for maximum impact"
        ]

def generate_all_use_cases():
    """Generate use cases for all 557 frameworks"""
    
    all_use_cases = {}
    
    # Import frameworks
    from framework_intelligence.framework_database import FRAMEWORKS
    
    for framework_id, framework in FRAMEWORKS.items():
        use_cases = match_framework_to_pattern(
            framework_id,
            framework.name,
            framework.description
        )
        
        all_use_cases[framework_id] = {
            "name": framework.name,
            "category": framework.category.value,
            "current_when_to_use": framework.when_to_use,
            "enhanced_use_cases": use_cases
        }
    
    return all_use_cases

if __name__ == "__main__":
    print("Generating comprehensive use cases for all frameworks...")
    
    all_use_cases = generate_all_use_cases()
    
    print(f"Generated use cases for {len(all_use_cases)} frameworks")
    
    # Save to file
    with open("comprehensive_framework_use_cases.json", "w") as f:
        json.dump(all_use_cases, f, indent=2)
    
    print("Saved to comprehensive_framework_use_cases.json")
    
    # Show some examples
    print("\nSample enhanced use cases:")
    
    examples = ["bcg_matrix", "lean_canvas", "competitive_positioning_saas", 
                "innovation_pipeline_technology", "unit_economics"]
    
    for ex in examples:
        if ex in all_use_cases:
            data = all_use_cases[ex]
            print(f"\n{data['name']}:")
            for i, use_case in enumerate(data['enhanced_use_cases'][:3], 1):
                print(f"  {i}. {use_case}")