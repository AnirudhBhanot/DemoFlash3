#!/usr/bin/env python3
"""
Update framework database with enhanced use cases
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from framework_intelligence.framework_database import FRAMEWORKS

# Enhanced use cases to add
use_case_updates = {
  "bcg_matrix": {
    "framework_name": "BCG Growth-Share Matrix",
    "current_use_cases": [
      "Evaluating product/business portfolio",
      "Resource allocation decisions",
      "Strategic positioning analysis",
      "Growth strategy planning",
      "Investment prioritization"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Prioritizing investment between high-growth/low-share vs low-growth/high-share products",
      "Quarterly portfolio review to rebalance resource allocation"
    ]
  },
  "porters_five_forces": {
    "framework_name": "Porter's Five Forces",
    "current_use_cases": [
      "Analyzing industry attractiveness",
      "Understanding competitive dynamics",
      "Making market entry decisions",
      "Developing competitive strategy",
      "Assessing profit potential"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "swot_analysis": {
    "framework_name": "SWOT Analysis",
    "current_use_cases": [
      "Starting strategic planning process",
      "Evaluating competitive position",
      "Making major business decisions",
      "Entering new markets",
      "Launching new products"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "blue_ocean_strategy": {
    "framework_name": "Blue Ocean Strategy",
    "current_use_cases": [
      "Seeking breakthrough innovation",
      "Escaping intense competition",
      "Creating new market categories",
      "Differentiating from competitors",
      "Pursuing growth in mature markets"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "bcg_growth_share_matrix": {
    "framework_name": "BCG Growth-Share Matrix",
    "current_use_cases": [
      "Managing product/business portfolio",
      "Allocating resources across units",
      "Making investment decisions",
      "Planning divestments",
      "Balancing portfolio risk"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Prioritizing investment between high-growth/low-share vs low-growth/high-share products",
      "Quarterly portfolio review to rebalance resource allocation"
    ]
  },
  "ansoff_matrix": {
    "framework_name": "Ansoff Matrix",
    "current_use_cases": [
      "Planning growth strategies",
      "Evaluating expansion options",
      "Risk assessment for growth",
      "Strategic planning sessions",
      "Market entry decisions"
    ],
    "enhanced_use_cases": [
      "Choosing between geographic expansion vs product line extension",
      "Deciding whether to build, buy, or partner for new capabilities",
      "Prioritizing organic growth vs acquisition opportunities",
      "Entering adjacent markets while maintaining core business",
      "Scaling from $1M to $10M ARR"
    ]
  },
  "design_thinking": {
    "framework_name": "Design Thinking",
    "current_use_cases": [
      "Solving complex problems",
      "Creating user-centered solutions",
      "Driving innovation initiatives",
      "Improving customer experience",
      "Developing new products/services"
    ],
    "enhanced_use_cases": [
      "Redesigning onboarding to reduce 50% drop-off rate",
      "Creating new product category that doesn't exist yet",
      "Solving complex workflow problems for enterprise users",
      "Improving NPS score from 20 to 50+",
      "Designing for accessibility and inclusion"
    ]
  },
  "lean_startup": {
    "framework_name": "Lean Startup",
    "current_use_cases": [
      "Launching new ventures",
      "Developing new products",
      "Testing business models",
      "Reducing market risk",
      "Rapid innovation cycles"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building MVP to test core value proposition",
      "Iterating pricing model based on early customer data"
    ]
  },
  "lean_canvas": {
    "framework_name": "Lean Canvas",
    "current_use_cases": [
      "When starting a new venture or product",
      "For rapid business model iteration",
      "To document and test key assumptions",
      "For early-stage startup planning",
      "When pivoting business model"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building MVP to test core value proposition",
      "Iterating pricing model based on early customer data"
    ]
  },
  "customer_development": {
    "framework_name": "Customer Development",
    "current_use_cases": [
      "Before building product features",
      "When validating problem-solution fit",
      "For understanding customer needs deeply",
      "During early-stage product development",
      "When entering new market segments"
    ],
    "enhanced_use_cases": [
      "Identifying unmet needs in existing market",
      "Designing solution for specific job-to-be-done",
      "Differentiating from competitors on job performance",
      "Understanding why customers switch to competitors"
    ]
  },
  "jobs_to_be_done": {
    "framework_name": "Jobs to be Done (JTBD)",
    "current_use_cases": [
      "Understanding customer needs",
      "Identifying innovation opportunities",
      "Improving existing products",
      "Market segmentation",
      "Competitive positioning"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months"
    ]
  },
  "stage_gate_process": {
    "framework_name": "Stage-Gate Process",
    "current_use_cases": [
      "Managing innovation projects",
      "Reducing project risk",
      "Allocating R&D resources",
      "Go/no-go decisions",
      "Complex product development"
    ],
    "enhanced_use_cases": [
      "Managing multiple innovation projects with limited resources",
      "Deciding which projects to kill vs accelerate",
      "Balancing incremental vs breakthrough innovation",
      "Aligning innovation pipeline with strategic goals",
      "Reducing time-to-market by 30%"
    ]
  },
  "open_innovation": {
    "framework_name": "Open Innovation",
    "current_use_cases": [
      "Accelerating innovation",
      "Accessing external expertise",
      "Reducing R&D costs",
      "Entering new markets",
      "Building ecosystems"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "aarrr_metrics": {
    "framework_name": "AARRR Metrics (Pirate Metrics)",
    "current_use_cases": [
      "Setting up growth metrics",
      "Optimizing conversion funnel",
      "Identifying growth bottlenecks",
      "Measuring startup performance",
      "Growth team focus"
    ],
    "enhanced_use_cases": [
      "Achieving viral coefficient > 1.0 for consumer app",
      "Building referral program that drives 40% of growth",
      "Optimizing sharing mechanics for maximum reach"
    ]
  },
  "growth_loops": {
    "framework_name": "Growth Loops",
    "current_use_cases": [
      "Building sustainable growth",
      "Reducing acquisition costs",
      "Creating viral products",
      "Scaling user base",
      "Product-led growth"
    ],
    "enhanced_use_cases": [
      "Building self-reinforcing acquisition channels",
      "Creating content loop that drives SEO traffic",
      "Designing product features that increase user engagement",
      "Connecting user actions to acquisition metrics",
      "Scaling from 10K to 100K users"
    ]
  },
  "product_led_growth": {
    "framework_name": "Product-Led Growth (PLG)",
    "current_use_cases": [
      "B2B SaaS companies",
      "Reducing sales costs",
      "Scaling efficiently",
      "Bottom-up adoption",
      "Self-serve products"
    ],
    "enhanced_use_cases": [
      "Transitioning from sales-led to product-led growth",
      "Designing free tier that converts to paid",
      "Building in-product upgrade prompts",
      "Reducing time-to-value for new users",
      "Achieving negative churn through expansion revenue"
    ]
  },
  "viral_coefficient": {
    "framework_name": "Viral Coefficient Model",
    "current_use_cases": [
      "Building viral features",
      "Optimizing referral programs",
      "Reducing acquisition costs",
      "Scaling user base",
      "Social product growth"
    ],
    "enhanced_use_cases": [
      "Achieving viral coefficient > 1.0 for consumer app",
      "Building referral program that drives 40% of growth",
      "Optimizing sharing mechanics for maximum reach",
      "Reducing viral cycle time from 7 to 3 days",
      "Leveraging network effects for exponential growth"
    ]
  },
  "land_and_expand": {
    "framework_name": "Land and Expand",
    "current_use_cases": [
      "Enterprise sales",
      "B2B SaaS growth",
      "Account expansion",
      "Reducing sales cycles",
      "Maximizing LTV"
    ],
    "enhanced_use_cases": [
      "Achieving viral coefficient > 1.0 for consumer app",
      "Building referral program that drives 40% of growth",
      "Optimizing sharing mechanics for maximum reach"
    ]
  },
  "unit_economics": {
    "framework_name": "Unit Economics",
    "current_use_cases": [
      "Evaluating business model viability",
      "Pricing decisions",
      "Growth planning",
      "Investor discussions",
      "Profitability analysis"
    ],
    "enhanced_use_cases": [
      "Determining sustainable customer acquisition spend",
      "Setting pricing to achieve positive unit economics",
      "Identifying unprofitable customer segments to avoid",
      "Projecting path to profitability based on current metrics",
      "Optimizing gross margins through operational efficiency"
    ]
  },
  "ltv_cac_ratio": {
    "framework_name": "LTV/CAC Ratio Analysis",
    "current_use_cases": [
      "Evaluating marketing efficiency",
      "Investment decisions",
      "Growth sustainability",
      "Channel optimization",
      "Business model validation"
    ],
    "enhanced_use_cases": [
      "Evaluating performance of different acquisition channels",
      "Setting marketing budget based on payback period",
      "Improving retention to increase LTV by 50%",
      "Deciding whether to raise prices vs reduce CAC",
      "Achieving LTV:CAC ratio > 3:1"
    ]
  },
  "burn_rate_runway": {
    "framework_name": "Burn Rate and Runway Analysis",
    "current_use_cases": [
      "Startup financial planning",
      "Fundraising decisions",
      "Cost management",
      "Scenario planning",
      "Board reporting"
    ],
    "enhanced_use_cases": [
      "Extending runway from 12 to 18 months",
      "Deciding between growth and profitability",
      "Planning headcount based on burn rate targets",
      "Preparing for fundraising with 6 months runway",
      "Managing cash during economic downturn"
    ]
  },
  "saas_metrics": {
    "framework_name": "SaaS Metrics Framework",
    "current_use_cases": [
      "Running SaaS business",
      "Investor reporting",
      "Performance optimization",
      "Benchmarking",
      "Growth planning"
    ],
    "enhanced_use_cases": [
      "Determining sustainable customer acquisition spend",
      "Setting pricing to achieve positive unit economics",
      "Identifying unprofitable customer segments to avoid"
    ]
  },
  "break_even_analysis": {
    "framework_name": "Break-Even Analysis",
    "current_use_cases": [
      "Pricing decisions",
      "New product launches",
      "Business planning",
      "Investment evaluation",
      "Cost structure analysis"
    ],
    "enhanced_use_cases": [
      "Determining sustainable customer acquisition spend",
      "Setting pricing to achieve positive unit economics",
      "Identifying unprofitable customer segments to avoid"
    ]
  },
  "lean_methodology": {
    "framework_name": "Lean Methodology",
    "current_use_cases": [
      "Process optimization",
      "Cost reduction",
      "Quality improvement",
      "Efficiency gains",
      "Waste elimination"
    ],
    "enhanced_use_cases": [
      "Reducing operational costs by 30%",
      "Eliminating waste in production process",
      "Improving delivery time from 10 to 3 days",
      "Implementing continuous improvement culture",
      "Scaling operations without proportional cost increase"
    ]
  },
  "six_sigma": {
    "framework_name": "Six Sigma",
    "current_use_cases": [
      "Quality improvement initiatives",
      "Defect reduction",
      "Process standardization",
      "Customer satisfaction improvement",
      "Cost reduction through quality"
    ],
    "enhanced_use_cases": [
      "Reducing defect rate below 0.1%",
      "Improving customer satisfaction scores to 95%+",
      "Standardizing processes across multiple locations",
      "Achieving ISO certification requirements",
      "Reducing variance in service delivery"
    ]
  },
  "agile_methodology": {
    "framework_name": "Agile Methodology",
    "current_use_cases": [
      "Software development projects",
      "Complex project management",
      "Rapid iteration needs",
      "Changing requirements",
      "Cross-functional collaboration"
    ],
    "enhanced_use_cases": [
      "Transitioning from waterfall to agile development",
      "Improving release frequency from quarterly to weekly",
      "Building cross-functional product teams",
      "Implementing CI/CD pipeline",
      "Reducing time from idea to production"
    ]
  },
  "supply_chain_optimization": {
    "framework_name": "Supply Chain Optimization",
    "current_use_cases": [
      "Reducing supply chain costs",
      "Improving delivery performance",
      "Managing inventory levels",
      "Risk mitigation",
      "Sustainability initiatives"
    ],
    "enhanced_use_cases": [
      "Reducing operational costs by 30%",
      "Eliminating waste in production process",
      "Improving delivery time from 10 to 3 days"
    ]
  },
  "total_quality_management": {
    "framework_name": "Total Quality Management (TQM)",
    "current_use_cases": [
      "Organization-wide quality improvement",
      "Cultural transformation",
      "Customer satisfaction focus",
      "Long-term excellence",
      "Competitive advantage through quality"
    ],
    "enhanced_use_cases": [
      "Reducing operational costs by 30%",
      "Eliminating waste in production process",
      "Improving delivery time from 10 to 3 days"
    ]
  },
  "marketing_mix_4ps": {
    "framework_name": "Marketing Mix (4Ps)",
    "current_use_cases": [
      "Developing marketing strategy",
      "Product launches",
      "Market entry planning",
      "Marketing audit",
      "Competitive positioning"
    ],
    "enhanced_use_cases": [
      "Sizing addressable market for new product launch"
    ]
  },
  "stp_marketing": {
    "framework_name": "STP Marketing (Segmentation, Targeting, Positioning)",
    "current_use_cases": [
      "Market entry strategy",
      "Product positioning",
      "Marketing effectiveness",
      "Resource allocation",
      "Competitive differentiation"
    ],
    "enhanced_use_cases": [
      "Sizing addressable market for new product launch"
    ]
  },
  "customer_journey_mapping": {
    "framework_name": "Customer Journey Mapping",
    "current_use_cases": [
      "Improving customer experience",
      "Identifying pain points",
      "Optimizing touchpoints",
      "Cross-functional alignment",
      "Digital transformation"
    ],
    "enhanced_use_cases": [
      "Understanding why customers switch to competitors"
    ]
  },
  "content_marketing_framework": {
    "framework_name": "Content Marketing Framework",
    "current_use_cases": [
      "Building brand awareness",
      "Lead generation",
      "Customer education",
      "SEO improvement",
      "Thought leadership"
    ],
    "enhanced_use_cases": [
      "Sizing addressable market for new product launch"
    ]
  },
  "product_market_fit": {
    "framework_name": "Product-Market Fit Framework",
    "current_use_cases": [
      "Startup validation",
      "Product pivot decisions",
      "Growth readiness assessment",
      "Investment discussions",
      "Market expansion"
    ],
    "enhanced_use_cases": [
      "Sizing addressable market for new product launch"
    ]
  },
  "value_chain_analysis": {
    "framework_name": "Value Chain Analysis",
    "current_use_cases": [
      "Cost analysis",
      "Competitive advantage",
      "Process improvement",
      "Strategic planning",
      "Outsourcing decisions"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_technology": {
    "framework_name": "Competitive Positioning Analysis (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_healthcare": {
    "framework_name": "Competitive Positioning Analysis (Healthcare)",
    "current_use_cases": [
      "When operating in healthcare specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_finance": {
    "framework_name": "Competitive Positioning Analysis (Finance)",
    "current_use_cases": [
      "When operating in finance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_retail": {
    "framework_name": "Competitive Positioning Analysis (Retail)",
    "current_use_cases": [
      "When operating in retail specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_manufacturing": {
    "framework_name": "Competitive Positioning Analysis (Manufacturing)",
    "current_use_cases": [
      "When operating in manufacturing specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_education": {
    "framework_name": "Competitive Positioning Analysis (Education)",
    "current_use_cases": [
      "When operating in education specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_energy": {
    "framework_name": "Competitive Positioning Analysis (Energy)",
    "current_use_cases": [
      "When operating in energy specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_transportation": {
    "framework_name": "Competitive Positioning Analysis (Transportation)",
    "current_use_cases": [
      "When operating in transportation specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_hospitality": {
    "framework_name": "Competitive Positioning Analysis (Hospitality)",
    "current_use_cases": [
      "When operating in hospitality specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_media": {
    "framework_name": "Competitive Positioning Analysis (Media)",
    "current_use_cases": [
      "When operating in media specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_telecommunications": {
    "framework_name": "Competitive Positioning Analysis (Telecommunications)",
    "current_use_cases": [
      "When operating in telecommunications specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_pharma": {
    "framework_name": "Competitive Positioning Analysis (Pharma)",
    "current_use_cases": [
      "When operating in pharma specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_automotive": {
    "framework_name": "Competitive Positioning Analysis (Automotive)",
    "current_use_cases": [
      "When operating in automotive specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_aerospace": {
    "framework_name": "Competitive Positioning Analysis (Aerospace)",
    "current_use_cases": [
      "When operating in aerospace specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_agriculture": {
    "framework_name": "Competitive Positioning Analysis (Agriculture)",
    "current_use_cases": [
      "When operating in agriculture specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_construction": {
    "framework_name": "Competitive Positioning Analysis (Construction)",
    "current_use_cases": [
      "When operating in construction specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_logistics": {
    "framework_name": "Competitive Positioning Analysis (Logistics)",
    "current_use_cases": [
      "When operating in logistics specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_ecommerce": {
    "framework_name": "Competitive Positioning Analysis (Ecommerce)",
    "current_use_cases": [
      "When operating in ecommerce specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_saas": {
    "framework_name": "Competitive Positioning Analysis (Saas)",
    "current_use_cases": [
      "When operating in saas specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_consulting": {
    "framework_name": "Competitive Positioning Analysis (Consulting)",
    "current_use_cases": [
      "When operating in consulting specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_insurance": {
    "framework_name": "Competitive Positioning Analysis (Insurance)",
    "current_use_cases": [
      "When operating in insurance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_real_estate": {
    "framework_name": "Competitive Positioning Analysis (Real Estate)",
    "current_use_cases": [
      "When operating in real estate specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_gaming": {
    "framework_name": "Competitive Positioning Analysis (Gaming)",
    "current_use_cases": [
      "When operating in gaming specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_sports": {
    "framework_name": "Competitive Positioning Analysis (Sports)",
    "current_use_cases": [
      "When operating in sports specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_entertainment": {
    "framework_name": "Competitive Positioning Analysis (Entertainment)",
    "current_use_cases": [
      "When operating in entertainment specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_startups": {
    "framework_name": "Competitive Positioning Analysis (Startups)",
    "current_use_cases": [
      "When operating in startups focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_enterprises": {
    "framework_name": "Competitive Positioning Analysis (Enterprises)",
    "current_use_cases": [
      "When operating in enterprises focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_smes": {
    "framework_name": "Competitive Positioning Analysis (Smes)",
    "current_use_cases": [
      "When operating in smes focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_nonprofits": {
    "framework_name": "Competitive Positioning Analysis (Nonprofits)",
    "current_use_cases": [
      "When operating in nonprofits focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_government": {
    "framework_name": "Competitive Positioning Analysis (Government)",
    "current_use_cases": [
      "When operating in government focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_b2b": {
    "framework_name": "Competitive Positioning Analysis (B2B)",
    "current_use_cases": [
      "When operating in b2b focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_b2c": {
    "framework_name": "Competitive Positioning Analysis (B2C)",
    "current_use_cases": [
      "When operating in b2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_d2c": {
    "framework_name": "Competitive Positioning Analysis (D2C)",
    "current_use_cases": [
      "When operating in d2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_marketplaces": {
    "framework_name": "Competitive Positioning Analysis (Marketplaces)",
    "current_use_cases": [
      "When operating in marketplaces focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_platforms": {
    "framework_name": "Competitive Positioning Analysis (Platforms)",
    "current_use_cases": [
      "When operating in platforms focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_digital": {
    "framework_name": "Competitive Positioning Analysis (Digital)",
    "current_use_cases": [
      "When operating in digital focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_mobile": {
    "framework_name": "Competitive Positioning Analysis (Mobile)",
    "current_use_cases": [
      "When operating in mobile focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_cloud": {
    "framework_name": "Competitive Positioning Analysis (Cloud)",
    "current_use_cases": [
      "When operating in cloud focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_ai_ml": {
    "framework_name": "Competitive Positioning Analysis (Ai Ml)",
    "current_use_cases": [
      "When operating in ai ml focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_blockchain": {
    "framework_name": "Competitive Positioning Analysis (Blockchain)",
    "current_use_cases": [
      "When operating in blockchain focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_remote": {
    "framework_name": "Competitive Positioning Analysis (Remote)",
    "current_use_cases": [
      "When operating in remote focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_hybrid": {
    "framework_name": "Competitive Positioning Analysis (Hybrid)",
    "current_use_cases": [
      "When operating in hybrid focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_global": {
    "framework_name": "Competitive Positioning Analysis (Global)",
    "current_use_cases": [
      "When operating in global focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_local": {
    "framework_name": "Competitive Positioning Analysis (Local)",
    "current_use_cases": [
      "When operating in local focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_positioning_emerging_markets": {
    "framework_name": "Competitive Positioning Analysis (Emerging Markets)",
    "current_use_cases": [
      "When operating in emerging markets focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "market_entry_technology": {
    "framework_name": "Market Entry Strategy (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_healthcare": {
    "framework_name": "Market Entry Strategy (Healthcare)",
    "current_use_cases": [
      "When operating in healthcare specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_finance": {
    "framework_name": "Market Entry Strategy (Finance)",
    "current_use_cases": [
      "When operating in finance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_retail": {
    "framework_name": "Market Entry Strategy (Retail)",
    "current_use_cases": [
      "When operating in retail specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_manufacturing": {
    "framework_name": "Market Entry Strategy (Manufacturing)",
    "current_use_cases": [
      "When operating in manufacturing specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_education": {
    "framework_name": "Market Entry Strategy (Education)",
    "current_use_cases": [
      "When operating in education specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_energy": {
    "framework_name": "Market Entry Strategy (Energy)",
    "current_use_cases": [
      "When operating in energy specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_transportation": {
    "framework_name": "Market Entry Strategy (Transportation)",
    "current_use_cases": [
      "When operating in transportation specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_hospitality": {
    "framework_name": "Market Entry Strategy (Hospitality)",
    "current_use_cases": [
      "When operating in hospitality specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_media": {
    "framework_name": "Market Entry Strategy (Media)",
    "current_use_cases": [
      "When operating in media specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_telecommunications": {
    "framework_name": "Market Entry Strategy (Telecommunications)",
    "current_use_cases": [
      "When operating in telecommunications specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_pharma": {
    "framework_name": "Market Entry Strategy (Pharma)",
    "current_use_cases": [
      "When operating in pharma specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_automotive": {
    "framework_name": "Market Entry Strategy (Automotive)",
    "current_use_cases": [
      "When operating in automotive specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_aerospace": {
    "framework_name": "Market Entry Strategy (Aerospace)",
    "current_use_cases": [
      "When operating in aerospace specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_agriculture": {
    "framework_name": "Market Entry Strategy (Agriculture)",
    "current_use_cases": [
      "When operating in agriculture specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_construction": {
    "framework_name": "Market Entry Strategy (Construction)",
    "current_use_cases": [
      "When operating in construction specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_logistics": {
    "framework_name": "Market Entry Strategy (Logistics)",
    "current_use_cases": [
      "When operating in logistics specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_ecommerce": {
    "framework_name": "Market Entry Strategy (Ecommerce)",
    "current_use_cases": [
      "When operating in ecommerce specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_saas": {
    "framework_name": "Market Entry Strategy (Saas)",
    "current_use_cases": [
      "When operating in saas specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_consulting": {
    "framework_name": "Market Entry Strategy (Consulting)",
    "current_use_cases": [
      "When operating in consulting specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_insurance": {
    "framework_name": "Market Entry Strategy (Insurance)",
    "current_use_cases": [
      "When operating in insurance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_real_estate": {
    "framework_name": "Market Entry Strategy (Real Estate)",
    "current_use_cases": [
      "When operating in real estate specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_gaming": {
    "framework_name": "Market Entry Strategy (Gaming)",
    "current_use_cases": [
      "When operating in gaming specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_sports": {
    "framework_name": "Market Entry Strategy (Sports)",
    "current_use_cases": [
      "When operating in sports specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_entertainment": {
    "framework_name": "Market Entry Strategy (Entertainment)",
    "current_use_cases": [
      "When operating in entertainment specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_startups": {
    "framework_name": "Market Entry Strategy (Startups)",
    "current_use_cases": [
      "When operating in startups focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_enterprises": {
    "framework_name": "Market Entry Strategy (Enterprises)",
    "current_use_cases": [
      "When operating in enterprises focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_smes": {
    "framework_name": "Market Entry Strategy (Smes)",
    "current_use_cases": [
      "When operating in smes focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_nonprofits": {
    "framework_name": "Market Entry Strategy (Nonprofits)",
    "current_use_cases": [
      "When operating in nonprofits focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_government": {
    "framework_name": "Market Entry Strategy (Government)",
    "current_use_cases": [
      "When operating in government focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_b2b": {
    "framework_name": "Market Entry Strategy (B2B)",
    "current_use_cases": [
      "When operating in b2b focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_b2c": {
    "framework_name": "Market Entry Strategy (B2C)",
    "current_use_cases": [
      "When operating in b2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_d2c": {
    "framework_name": "Market Entry Strategy (D2C)",
    "current_use_cases": [
      "When operating in d2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_marketplaces": {
    "framework_name": "Market Entry Strategy (Marketplaces)",
    "current_use_cases": [
      "When operating in marketplaces focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_platforms": {
    "framework_name": "Market Entry Strategy (Platforms)",
    "current_use_cases": [
      "When operating in platforms focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_digital": {
    "framework_name": "Market Entry Strategy (Digital)",
    "current_use_cases": [
      "When operating in digital focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_mobile": {
    "framework_name": "Market Entry Strategy (Mobile)",
    "current_use_cases": [
      "When operating in mobile focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_cloud": {
    "framework_name": "Market Entry Strategy (Cloud)",
    "current_use_cases": [
      "When operating in cloud focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_ai_ml": {
    "framework_name": "Market Entry Strategy (Ai Ml)",
    "current_use_cases": [
      "When operating in ai ml focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_blockchain": {
    "framework_name": "Market Entry Strategy (Blockchain)",
    "current_use_cases": [
      "When operating in blockchain focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_remote": {
    "framework_name": "Market Entry Strategy (Remote)",
    "current_use_cases": [
      "When operating in remote focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_hybrid": {
    "framework_name": "Market Entry Strategy (Hybrid)",
    "current_use_cases": [
      "When operating in hybrid focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_global": {
    "framework_name": "Market Entry Strategy (Global)",
    "current_use_cases": [
      "When operating in global focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_local": {
    "framework_name": "Market Entry Strategy (Local)",
    "current_use_cases": [
      "When operating in local focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "market_entry_emerging_markets": {
    "framework_name": "Market Entry Strategy (Emerging Markets)",
    "current_use_cases": [
      "When operating in emerging markets focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Launching in a new geographic market",
      "Entering a regulated industry for the first time",
      "Deciding on direct sales vs channel partnership strategy",
      "Timing market entry to maximize first-mover advantage",
      "Choosing initial target customer segment in new market"
    ]
  },
  "strategic_alliance_technology": {
    "framework_name": "Strategic Alliance Framework (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_healthcare": {
    "framework_name": "Strategic Alliance Framework (Healthcare)",
    "current_use_cases": [
      "When operating in healthcare specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_finance": {
    "framework_name": "Strategic Alliance Framework (Finance)",
    "current_use_cases": [
      "When operating in finance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_retail": {
    "framework_name": "Strategic Alliance Framework (Retail)",
    "current_use_cases": [
      "When operating in retail specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_manufacturing": {
    "framework_name": "Strategic Alliance Framework (Manufacturing)",
    "current_use_cases": [
      "When operating in manufacturing specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_education": {
    "framework_name": "Strategic Alliance Framework (Education)",
    "current_use_cases": [
      "When operating in education specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_energy": {
    "framework_name": "Strategic Alliance Framework (Energy)",
    "current_use_cases": [
      "When operating in energy specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_transportation": {
    "framework_name": "Strategic Alliance Framework (Transportation)",
    "current_use_cases": [
      "When operating in transportation specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_hospitality": {
    "framework_name": "Strategic Alliance Framework (Hospitality)",
    "current_use_cases": [
      "When operating in hospitality specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_media": {
    "framework_name": "Strategic Alliance Framework (Media)",
    "current_use_cases": [
      "When operating in media specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_telecommunications": {
    "framework_name": "Strategic Alliance Framework (Telecommunications)",
    "current_use_cases": [
      "When operating in telecommunications specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_pharma": {
    "framework_name": "Strategic Alliance Framework (Pharma)",
    "current_use_cases": [
      "When operating in pharma specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_automotive": {
    "framework_name": "Strategic Alliance Framework (Automotive)",
    "current_use_cases": [
      "When operating in automotive specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_aerospace": {
    "framework_name": "Strategic Alliance Framework (Aerospace)",
    "current_use_cases": [
      "When operating in aerospace specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_agriculture": {
    "framework_name": "Strategic Alliance Framework (Agriculture)",
    "current_use_cases": [
      "When operating in agriculture specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_construction": {
    "framework_name": "Strategic Alliance Framework (Construction)",
    "current_use_cases": [
      "When operating in construction specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_logistics": {
    "framework_name": "Strategic Alliance Framework (Logistics)",
    "current_use_cases": [
      "When operating in logistics specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_ecommerce": {
    "framework_name": "Strategic Alliance Framework (Ecommerce)",
    "current_use_cases": [
      "When operating in ecommerce specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_saas": {
    "framework_name": "Strategic Alliance Framework (Saas)",
    "current_use_cases": [
      "When operating in saas specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_consulting": {
    "framework_name": "Strategic Alliance Framework (Consulting)",
    "current_use_cases": [
      "When operating in consulting specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_insurance": {
    "framework_name": "Strategic Alliance Framework (Insurance)",
    "current_use_cases": [
      "When operating in insurance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_real_estate": {
    "framework_name": "Strategic Alliance Framework (Real Estate)",
    "current_use_cases": [
      "When operating in real estate specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_gaming": {
    "framework_name": "Strategic Alliance Framework (Gaming)",
    "current_use_cases": [
      "When operating in gaming specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_sports": {
    "framework_name": "Strategic Alliance Framework (Sports)",
    "current_use_cases": [
      "When operating in sports specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_entertainment": {
    "framework_name": "Strategic Alliance Framework (Entertainment)",
    "current_use_cases": [
      "When operating in entertainment specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_startups": {
    "framework_name": "Strategic Alliance Framework (Startups)",
    "current_use_cases": [
      "When operating in startups focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_enterprises": {
    "framework_name": "Strategic Alliance Framework (Enterprises)",
    "current_use_cases": [
      "When operating in enterprises focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_smes": {
    "framework_name": "Strategic Alliance Framework (Smes)",
    "current_use_cases": [
      "When operating in smes focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_nonprofits": {
    "framework_name": "Strategic Alliance Framework (Nonprofits)",
    "current_use_cases": [
      "When operating in nonprofits focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_government": {
    "framework_name": "Strategic Alliance Framework (Government)",
    "current_use_cases": [
      "When operating in government focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_b2b": {
    "framework_name": "Strategic Alliance Framework (B2B)",
    "current_use_cases": [
      "When operating in b2b focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_b2c": {
    "framework_name": "Strategic Alliance Framework (B2C)",
    "current_use_cases": [
      "When operating in b2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_d2c": {
    "framework_name": "Strategic Alliance Framework (D2C)",
    "current_use_cases": [
      "When operating in d2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_marketplaces": {
    "framework_name": "Strategic Alliance Framework (Marketplaces)",
    "current_use_cases": [
      "When operating in marketplaces focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Sizing addressable market for new product launch"
    ]
  },
  "strategic_alliance_platforms": {
    "framework_name": "Strategic Alliance Framework (Platforms)",
    "current_use_cases": [
      "When operating in platforms focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_digital": {
    "framework_name": "Strategic Alliance Framework (Digital)",
    "current_use_cases": [
      "When operating in digital focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_mobile": {
    "framework_name": "Strategic Alliance Framework (Mobile)",
    "current_use_cases": [
      "When operating in mobile focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_cloud": {
    "framework_name": "Strategic Alliance Framework (Cloud)",
    "current_use_cases": [
      "When operating in cloud focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_ai_ml": {
    "framework_name": "Strategic Alliance Framework (Ai Ml)",
    "current_use_cases": [
      "When operating in ai ml focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_blockchain": {
    "framework_name": "Strategic Alliance Framework (Blockchain)",
    "current_use_cases": [
      "When operating in blockchain focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_remote": {
    "framework_name": "Strategic Alliance Framework (Remote)",
    "current_use_cases": [
      "When operating in remote focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_hybrid": {
    "framework_name": "Strategic Alliance Framework (Hybrid)",
    "current_use_cases": [
      "When operating in hybrid focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_global": {
    "framework_name": "Strategic Alliance Framework (Global)",
    "current_use_cases": [
      "When operating in global focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_local": {
    "framework_name": "Strategic Alliance Framework (Local)",
    "current_use_cases": [
      "When operating in local focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_alliance_emerging_markets": {
    "framework_name": "Strategic Alliance Framework (Emerging Markets)",
    "current_use_cases": [
      "When operating in emerging markets focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Sizing addressable market for new product launch"
    ]
  },
  "disruption_strategy_technology": {
    "framework_name": "Disruption Strategy (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_healthcare": {
    "framework_name": "Disruption Strategy (Healthcare)",
    "current_use_cases": [
      "When operating in healthcare specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_finance": {
    "framework_name": "Disruption Strategy (Finance)",
    "current_use_cases": [
      "When operating in finance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_retail": {
    "framework_name": "Disruption Strategy (Retail)",
    "current_use_cases": [
      "When operating in retail specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_manufacturing": {
    "framework_name": "Disruption Strategy (Manufacturing)",
    "current_use_cases": [
      "When operating in manufacturing specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_education": {
    "framework_name": "Disruption Strategy (Education)",
    "current_use_cases": [
      "When operating in education specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_energy": {
    "framework_name": "Disruption Strategy (Energy)",
    "current_use_cases": [
      "When operating in energy specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_transportation": {
    "framework_name": "Disruption Strategy (Transportation)",
    "current_use_cases": [
      "When operating in transportation specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_hospitality": {
    "framework_name": "Disruption Strategy (Hospitality)",
    "current_use_cases": [
      "When operating in hospitality specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_media": {
    "framework_name": "Disruption Strategy (Media)",
    "current_use_cases": [
      "When operating in media specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_telecommunications": {
    "framework_name": "Disruption Strategy (Telecommunications)",
    "current_use_cases": [
      "When operating in telecommunications specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_pharma": {
    "framework_name": "Disruption Strategy (Pharma)",
    "current_use_cases": [
      "When operating in pharma specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_automotive": {
    "framework_name": "Disruption Strategy (Automotive)",
    "current_use_cases": [
      "When operating in automotive specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_aerospace": {
    "framework_name": "Disruption Strategy (Aerospace)",
    "current_use_cases": [
      "When operating in aerospace specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_agriculture": {
    "framework_name": "Disruption Strategy (Agriculture)",
    "current_use_cases": [
      "When operating in agriculture specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_construction": {
    "framework_name": "Disruption Strategy (Construction)",
    "current_use_cases": [
      "When operating in construction specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_logistics": {
    "framework_name": "Disruption Strategy (Logistics)",
    "current_use_cases": [
      "When operating in logistics specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_ecommerce": {
    "framework_name": "Disruption Strategy (Ecommerce)",
    "current_use_cases": [
      "When operating in ecommerce specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_saas": {
    "framework_name": "Disruption Strategy (Saas)",
    "current_use_cases": [
      "When operating in saas specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_consulting": {
    "framework_name": "Disruption Strategy (Consulting)",
    "current_use_cases": [
      "When operating in consulting specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_insurance": {
    "framework_name": "Disruption Strategy (Insurance)",
    "current_use_cases": [
      "When operating in insurance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_real_estate": {
    "framework_name": "Disruption Strategy (Real Estate)",
    "current_use_cases": [
      "When operating in real estate specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_gaming": {
    "framework_name": "Disruption Strategy (Gaming)",
    "current_use_cases": [
      "When operating in gaming specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_sports": {
    "framework_name": "Disruption Strategy (Sports)",
    "current_use_cases": [
      "When operating in sports specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_entertainment": {
    "framework_name": "Disruption Strategy (Entertainment)",
    "current_use_cases": [
      "When operating in entertainment specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_startups": {
    "framework_name": "Disruption Strategy (Startups)",
    "current_use_cases": [
      "When operating in startups focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_enterprises": {
    "framework_name": "Disruption Strategy (Enterprises)",
    "current_use_cases": [
      "When operating in enterprises focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_smes": {
    "framework_name": "Disruption Strategy (Smes)",
    "current_use_cases": [
      "When operating in smes focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_nonprofits": {
    "framework_name": "Disruption Strategy (Nonprofits)",
    "current_use_cases": [
      "When operating in nonprofits focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_government": {
    "framework_name": "Disruption Strategy (Government)",
    "current_use_cases": [
      "When operating in government focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_b2b": {
    "framework_name": "Disruption Strategy (B2B)",
    "current_use_cases": [
      "When operating in b2b focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_b2c": {
    "framework_name": "Disruption Strategy (B2C)",
    "current_use_cases": [
      "When operating in b2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_d2c": {
    "framework_name": "Disruption Strategy (D2C)",
    "current_use_cases": [
      "When operating in d2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_marketplaces": {
    "framework_name": "Disruption Strategy (Marketplaces)",
    "current_use_cases": [
      "When operating in marketplaces focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_platforms": {
    "framework_name": "Disruption Strategy (Platforms)",
    "current_use_cases": [
      "When operating in platforms focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_digital": {
    "framework_name": "Disruption Strategy (Digital)",
    "current_use_cases": [
      "When operating in digital focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_mobile": {
    "framework_name": "Disruption Strategy (Mobile)",
    "current_use_cases": [
      "When operating in mobile focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_cloud": {
    "framework_name": "Disruption Strategy (Cloud)",
    "current_use_cases": [
      "When operating in cloud focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_ai_ml": {
    "framework_name": "Disruption Strategy (Ai Ml)",
    "current_use_cases": [
      "When operating in ai ml focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_blockchain": {
    "framework_name": "Disruption Strategy (Blockchain)",
    "current_use_cases": [
      "When operating in blockchain focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_remote": {
    "framework_name": "Disruption Strategy (Remote)",
    "current_use_cases": [
      "When operating in remote focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_hybrid": {
    "framework_name": "Disruption Strategy (Hybrid)",
    "current_use_cases": [
      "When operating in hybrid focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_global": {
    "framework_name": "Disruption Strategy (Global)",
    "current_use_cases": [
      "When operating in global focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_local": {
    "framework_name": "Disruption Strategy (Local)",
    "current_use_cases": [
      "When operating in local focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "disruption_strategy_emerging_markets": {
    "framework_name": "Disruption Strategy (Emerging Markets)",
    "current_use_cases": [
      "When operating in emerging markets focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Responding to digital transformation in traditional industry",
      "Cannibalizing existing products with innovative offerings",
      "Building new business model while maintaining legacy revenue",
      "Identifying opportunities to disrupt incumbent players",
      "Protecting against disruption from startups"
    ]
  },
  "platform_strategy_technology": {
    "framework_name": "Platform Strategy (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_healthcare": {
    "framework_name": "Platform Strategy (Healthcare)",
    "current_use_cases": [
      "When operating in healthcare specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_finance": {
    "framework_name": "Platform Strategy (Finance)",
    "current_use_cases": [
      "When operating in finance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_retail": {
    "framework_name": "Platform Strategy (Retail)",
    "current_use_cases": [
      "When operating in retail specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_manufacturing": {
    "framework_name": "Platform Strategy (Manufacturing)",
    "current_use_cases": [
      "When operating in manufacturing specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_education": {
    "framework_name": "Platform Strategy (Education)",
    "current_use_cases": [
      "When operating in education specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_energy": {
    "framework_name": "Platform Strategy (Energy)",
    "current_use_cases": [
      "When operating in energy specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_transportation": {
    "framework_name": "Platform Strategy (Transportation)",
    "current_use_cases": [
      "When operating in transportation specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_hospitality": {
    "framework_name": "Platform Strategy (Hospitality)",
    "current_use_cases": [
      "When operating in hospitality specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_media": {
    "framework_name": "Platform Strategy (Media)",
    "current_use_cases": [
      "When operating in media specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_telecommunications": {
    "framework_name": "Platform Strategy (Telecommunications)",
    "current_use_cases": [
      "When operating in telecommunications specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_pharma": {
    "framework_name": "Platform Strategy (Pharma)",
    "current_use_cases": [
      "When operating in pharma specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_automotive": {
    "framework_name": "Platform Strategy (Automotive)",
    "current_use_cases": [
      "When operating in automotive specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_aerospace": {
    "framework_name": "Platform Strategy (Aerospace)",
    "current_use_cases": [
      "When operating in aerospace specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_agriculture": {
    "framework_name": "Platform Strategy (Agriculture)",
    "current_use_cases": [
      "When operating in agriculture specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_construction": {
    "framework_name": "Platform Strategy (Construction)",
    "current_use_cases": [
      "When operating in construction specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_logistics": {
    "framework_name": "Platform Strategy (Logistics)",
    "current_use_cases": [
      "When operating in logistics specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_ecommerce": {
    "framework_name": "Platform Strategy (Ecommerce)",
    "current_use_cases": [
      "When operating in ecommerce specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_saas": {
    "framework_name": "Platform Strategy (Saas)",
    "current_use_cases": [
      "When operating in saas specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_consulting": {
    "framework_name": "Platform Strategy (Consulting)",
    "current_use_cases": [
      "When operating in consulting specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_insurance": {
    "framework_name": "Platform Strategy (Insurance)",
    "current_use_cases": [
      "When operating in insurance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_real_estate": {
    "framework_name": "Platform Strategy (Real Estate)",
    "current_use_cases": [
      "When operating in real estate specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_gaming": {
    "framework_name": "Platform Strategy (Gaming)",
    "current_use_cases": [
      "When operating in gaming specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_sports": {
    "framework_name": "Platform Strategy (Sports)",
    "current_use_cases": [
      "When operating in sports specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_entertainment": {
    "framework_name": "Platform Strategy (Entertainment)",
    "current_use_cases": [
      "When operating in entertainment specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_startups": {
    "framework_name": "Platform Strategy (Startups)",
    "current_use_cases": [
      "When operating in startups focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_enterprises": {
    "framework_name": "Platform Strategy (Enterprises)",
    "current_use_cases": [
      "When operating in enterprises focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_smes": {
    "framework_name": "Platform Strategy (Smes)",
    "current_use_cases": [
      "When operating in smes focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_nonprofits": {
    "framework_name": "Platform Strategy (Nonprofits)",
    "current_use_cases": [
      "When operating in nonprofits focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_government": {
    "framework_name": "Platform Strategy (Government)",
    "current_use_cases": [
      "When operating in government focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_b2b": {
    "framework_name": "Platform Strategy (B2B)",
    "current_use_cases": [
      "When operating in b2b focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_b2c": {
    "framework_name": "Platform Strategy (B2C)",
    "current_use_cases": [
      "When operating in b2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_d2c": {
    "framework_name": "Platform Strategy (D2C)",
    "current_use_cases": [
      "When operating in d2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_marketplaces": {
    "framework_name": "Platform Strategy (Marketplaces)",
    "current_use_cases": [
      "When operating in marketplaces focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Sizing addressable market for new product launch"
    ]
  },
  "platform_strategy_platforms": {
    "framework_name": "Platform Strategy (Platforms)",
    "current_use_cases": [
      "When operating in platforms focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_digital": {
    "framework_name": "Platform Strategy (Digital)",
    "current_use_cases": [
      "When operating in digital focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_mobile": {
    "framework_name": "Platform Strategy (Mobile)",
    "current_use_cases": [
      "When operating in mobile focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_cloud": {
    "framework_name": "Platform Strategy (Cloud)",
    "current_use_cases": [
      "When operating in cloud focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_ai_ml": {
    "framework_name": "Platform Strategy (Ai Ml)",
    "current_use_cases": [
      "When operating in ai ml focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_blockchain": {
    "framework_name": "Platform Strategy (Blockchain)",
    "current_use_cases": [
      "When operating in blockchain focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_remote": {
    "framework_name": "Platform Strategy (Remote)",
    "current_use_cases": [
      "When operating in remote focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_hybrid": {
    "framework_name": "Platform Strategy (Hybrid)",
    "current_use_cases": [
      "When operating in hybrid focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_global": {
    "framework_name": "Platform Strategy (Global)",
    "current_use_cases": [
      "When operating in global focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_local": {
    "framework_name": "Platform Strategy (Local)",
    "current_use_cases": [
      "When operating in local focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "platform_strategy_emerging_markets": {
    "framework_name": "Platform Strategy (Emerging Markets)",
    "current_use_cases": [
      "When operating in emerging markets focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Sizing addressable market for new product launch"
    ]
  },
  "ecosystem_strategy_technology": {
    "framework_name": "Ecosystem Strategy (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_healthcare": {
    "framework_name": "Ecosystem Strategy (Healthcare)",
    "current_use_cases": [
      "When operating in healthcare specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_finance": {
    "framework_name": "Ecosystem Strategy (Finance)",
    "current_use_cases": [
      "When operating in finance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_retail": {
    "framework_name": "Ecosystem Strategy (Retail)",
    "current_use_cases": [
      "When operating in retail specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_manufacturing": {
    "framework_name": "Ecosystem Strategy (Manufacturing)",
    "current_use_cases": [
      "When operating in manufacturing specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_education": {
    "framework_name": "Ecosystem Strategy (Education)",
    "current_use_cases": [
      "When operating in education specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_energy": {
    "framework_name": "Ecosystem Strategy (Energy)",
    "current_use_cases": [
      "When operating in energy specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_transportation": {
    "framework_name": "Ecosystem Strategy (Transportation)",
    "current_use_cases": [
      "When operating in transportation specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_hospitality": {
    "framework_name": "Ecosystem Strategy (Hospitality)",
    "current_use_cases": [
      "When operating in hospitality specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_media": {
    "framework_name": "Ecosystem Strategy (Media)",
    "current_use_cases": [
      "When operating in media specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_telecommunications": {
    "framework_name": "Ecosystem Strategy (Telecommunications)",
    "current_use_cases": [
      "When operating in telecommunications specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_pharma": {
    "framework_name": "Ecosystem Strategy (Pharma)",
    "current_use_cases": [
      "When operating in pharma specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_automotive": {
    "framework_name": "Ecosystem Strategy (Automotive)",
    "current_use_cases": [
      "When operating in automotive specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_aerospace": {
    "framework_name": "Ecosystem Strategy (Aerospace)",
    "current_use_cases": [
      "When operating in aerospace specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_agriculture": {
    "framework_name": "Ecosystem Strategy (Agriculture)",
    "current_use_cases": [
      "When operating in agriculture specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_construction": {
    "framework_name": "Ecosystem Strategy (Construction)",
    "current_use_cases": [
      "When operating in construction specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_logistics": {
    "framework_name": "Ecosystem Strategy (Logistics)",
    "current_use_cases": [
      "When operating in logistics specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_ecommerce": {
    "framework_name": "Ecosystem Strategy (Ecommerce)",
    "current_use_cases": [
      "When operating in ecommerce specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_saas": {
    "framework_name": "Ecosystem Strategy (Saas)",
    "current_use_cases": [
      "When operating in saas specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_consulting": {
    "framework_name": "Ecosystem Strategy (Consulting)",
    "current_use_cases": [
      "When operating in consulting specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_insurance": {
    "framework_name": "Ecosystem Strategy (Insurance)",
    "current_use_cases": [
      "When operating in insurance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_real_estate": {
    "framework_name": "Ecosystem Strategy (Real Estate)",
    "current_use_cases": [
      "When operating in real estate specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_gaming": {
    "framework_name": "Ecosystem Strategy (Gaming)",
    "current_use_cases": [
      "When operating in gaming specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_sports": {
    "framework_name": "Ecosystem Strategy (Sports)",
    "current_use_cases": [
      "When operating in sports specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_entertainment": {
    "framework_name": "Ecosystem Strategy (Entertainment)",
    "current_use_cases": [
      "When operating in entertainment specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_startups": {
    "framework_name": "Ecosystem Strategy (Startups)",
    "current_use_cases": [
      "When operating in startups focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_enterprises": {
    "framework_name": "Ecosystem Strategy (Enterprises)",
    "current_use_cases": [
      "When operating in enterprises focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_smes": {
    "framework_name": "Ecosystem Strategy (Smes)",
    "current_use_cases": [
      "When operating in smes focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_nonprofits": {
    "framework_name": "Ecosystem Strategy (Nonprofits)",
    "current_use_cases": [
      "When operating in nonprofits focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_government": {
    "framework_name": "Ecosystem Strategy (Government)",
    "current_use_cases": [
      "When operating in government focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_b2b": {
    "framework_name": "Ecosystem Strategy (B2B)",
    "current_use_cases": [
      "When operating in b2b focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_b2c": {
    "framework_name": "Ecosystem Strategy (B2C)",
    "current_use_cases": [
      "When operating in b2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_d2c": {
    "framework_name": "Ecosystem Strategy (D2C)",
    "current_use_cases": [
      "When operating in d2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_marketplaces": {
    "framework_name": "Ecosystem Strategy (Marketplaces)",
    "current_use_cases": [
      "When operating in marketplaces focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Sizing addressable market for new product launch"
    ]
  },
  "ecosystem_strategy_platforms": {
    "framework_name": "Ecosystem Strategy (Platforms)",
    "current_use_cases": [
      "When operating in platforms focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_digital": {
    "framework_name": "Ecosystem Strategy (Digital)",
    "current_use_cases": [
      "When operating in digital focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_mobile": {
    "framework_name": "Ecosystem Strategy (Mobile)",
    "current_use_cases": [
      "When operating in mobile focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_cloud": {
    "framework_name": "Ecosystem Strategy (Cloud)",
    "current_use_cases": [
      "When operating in cloud focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_ai_ml": {
    "framework_name": "Ecosystem Strategy (Ai Ml)",
    "current_use_cases": [
      "When operating in ai ml focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_blockchain": {
    "framework_name": "Ecosystem Strategy (Blockchain)",
    "current_use_cases": [
      "When operating in blockchain focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_remote": {
    "framework_name": "Ecosystem Strategy (Remote)",
    "current_use_cases": [
      "When operating in remote focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_hybrid": {
    "framework_name": "Ecosystem Strategy (Hybrid)",
    "current_use_cases": [
      "When operating in hybrid focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_global": {
    "framework_name": "Ecosystem Strategy (Global)",
    "current_use_cases": [
      "When operating in global focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_local": {
    "framework_name": "Ecosystem Strategy (Local)",
    "current_use_cases": [
      "When operating in local focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "ecosystem_strategy_emerging_markets": {
    "framework_name": "Ecosystem Strategy (Emerging Markets)",
    "current_use_cases": [
      "When operating in emerging markets focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Sizing addressable market for new product launch"
    ]
  },
  "value_migration_technology": {
    "framework_name": "Value Migration Analysis (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_healthcare": {
    "framework_name": "Value Migration Analysis (Healthcare)",
    "current_use_cases": [
      "When operating in healthcare specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_finance": {
    "framework_name": "Value Migration Analysis (Finance)",
    "current_use_cases": [
      "When operating in finance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_retail": {
    "framework_name": "Value Migration Analysis (Retail)",
    "current_use_cases": [
      "When operating in retail specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_manufacturing": {
    "framework_name": "Value Migration Analysis (Manufacturing)",
    "current_use_cases": [
      "When operating in manufacturing specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_education": {
    "framework_name": "Value Migration Analysis (Education)",
    "current_use_cases": [
      "When operating in education specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_energy": {
    "framework_name": "Value Migration Analysis (Energy)",
    "current_use_cases": [
      "When operating in energy specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_transportation": {
    "framework_name": "Value Migration Analysis (Transportation)",
    "current_use_cases": [
      "When operating in transportation specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_hospitality": {
    "framework_name": "Value Migration Analysis (Hospitality)",
    "current_use_cases": [
      "When operating in hospitality specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_media": {
    "framework_name": "Value Migration Analysis (Media)",
    "current_use_cases": [
      "When operating in media specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_telecommunications": {
    "framework_name": "Value Migration Analysis (Telecommunications)",
    "current_use_cases": [
      "When operating in telecommunications specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_pharma": {
    "framework_name": "Value Migration Analysis (Pharma)",
    "current_use_cases": [
      "When operating in pharma specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_automotive": {
    "framework_name": "Value Migration Analysis (Automotive)",
    "current_use_cases": [
      "When operating in automotive specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_aerospace": {
    "framework_name": "Value Migration Analysis (Aerospace)",
    "current_use_cases": [
      "When operating in aerospace specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_agriculture": {
    "framework_name": "Value Migration Analysis (Agriculture)",
    "current_use_cases": [
      "When operating in agriculture specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_construction": {
    "framework_name": "Value Migration Analysis (Construction)",
    "current_use_cases": [
      "When operating in construction specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_logistics": {
    "framework_name": "Value Migration Analysis (Logistics)",
    "current_use_cases": [
      "When operating in logistics specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_ecommerce": {
    "framework_name": "Value Migration Analysis (Ecommerce)",
    "current_use_cases": [
      "When operating in ecommerce specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_saas": {
    "framework_name": "Value Migration Analysis (Saas)",
    "current_use_cases": [
      "When operating in saas specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_consulting": {
    "framework_name": "Value Migration Analysis (Consulting)",
    "current_use_cases": [
      "When operating in consulting specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_insurance": {
    "framework_name": "Value Migration Analysis (Insurance)",
    "current_use_cases": [
      "When operating in insurance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_real_estate": {
    "framework_name": "Value Migration Analysis (Real Estate)",
    "current_use_cases": [
      "When operating in real estate specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_gaming": {
    "framework_name": "Value Migration Analysis (Gaming)",
    "current_use_cases": [
      "When operating in gaming specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_sports": {
    "framework_name": "Value Migration Analysis (Sports)",
    "current_use_cases": [
      "When operating in sports specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_entertainment": {
    "framework_name": "Value Migration Analysis (Entertainment)",
    "current_use_cases": [
      "When operating in entertainment specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_startups": {
    "framework_name": "Value Migration Analysis (Startups)",
    "current_use_cases": [
      "When operating in startups focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_enterprises": {
    "framework_name": "Value Migration Analysis (Enterprises)",
    "current_use_cases": [
      "When operating in enterprises focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_smes": {
    "framework_name": "Value Migration Analysis (Smes)",
    "current_use_cases": [
      "When operating in smes focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_nonprofits": {
    "framework_name": "Value Migration Analysis (Nonprofits)",
    "current_use_cases": [
      "When operating in nonprofits focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_government": {
    "framework_name": "Value Migration Analysis (Government)",
    "current_use_cases": [
      "When operating in government focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_b2b": {
    "framework_name": "Value Migration Analysis (B2B)",
    "current_use_cases": [
      "When operating in b2b focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_b2c": {
    "framework_name": "Value Migration Analysis (B2C)",
    "current_use_cases": [
      "When operating in b2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_d2c": {
    "framework_name": "Value Migration Analysis (D2C)",
    "current_use_cases": [
      "When operating in d2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_marketplaces": {
    "framework_name": "Value Migration Analysis (Marketplaces)",
    "current_use_cases": [
      "When operating in marketplaces focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Sizing addressable market for new product launch"
    ]
  },
  "value_migration_platforms": {
    "framework_name": "Value Migration Analysis (Platforms)",
    "current_use_cases": [
      "When operating in platforms focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_digital": {
    "framework_name": "Value Migration Analysis (Digital)",
    "current_use_cases": [
      "When operating in digital focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_mobile": {
    "framework_name": "Value Migration Analysis (Mobile)",
    "current_use_cases": [
      "When operating in mobile focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_cloud": {
    "framework_name": "Value Migration Analysis (Cloud)",
    "current_use_cases": [
      "When operating in cloud focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_ai_ml": {
    "framework_name": "Value Migration Analysis (Ai Ml)",
    "current_use_cases": [
      "When operating in ai ml focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_blockchain": {
    "framework_name": "Value Migration Analysis (Blockchain)",
    "current_use_cases": [
      "When operating in blockchain focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_remote": {
    "framework_name": "Value Migration Analysis (Remote)",
    "current_use_cases": [
      "When operating in remote focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_hybrid": {
    "framework_name": "Value Migration Analysis (Hybrid)",
    "current_use_cases": [
      "When operating in hybrid focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_global": {
    "framework_name": "Value Migration Analysis (Global)",
    "current_use_cases": [
      "When operating in global focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_local": {
    "framework_name": "Value Migration Analysis (Local)",
    "current_use_cases": [
      "When operating in local focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "value_migration_emerging_markets": {
    "framework_name": "Value Migration Analysis (Emerging Markets)",
    "current_use_cases": [
      "When operating in emerging markets focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Sizing addressable market for new product launch"
    ]
  },
  "strategic_options_technology": {
    "framework_name": "Strategic Options Framework (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_healthcare": {
    "framework_name": "Strategic Options Framework (Healthcare)",
    "current_use_cases": [
      "When operating in healthcare specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_finance": {
    "framework_name": "Strategic Options Framework (Finance)",
    "current_use_cases": [
      "When operating in finance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_retail": {
    "framework_name": "Strategic Options Framework (Retail)",
    "current_use_cases": [
      "When operating in retail specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_manufacturing": {
    "framework_name": "Strategic Options Framework (Manufacturing)",
    "current_use_cases": [
      "When operating in manufacturing specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_education": {
    "framework_name": "Strategic Options Framework (Education)",
    "current_use_cases": [
      "When operating in education specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_energy": {
    "framework_name": "Strategic Options Framework (Energy)",
    "current_use_cases": [
      "When operating in energy specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_transportation": {
    "framework_name": "Strategic Options Framework (Transportation)",
    "current_use_cases": [
      "When operating in transportation specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_hospitality": {
    "framework_name": "Strategic Options Framework (Hospitality)",
    "current_use_cases": [
      "When operating in hospitality specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_media": {
    "framework_name": "Strategic Options Framework (Media)",
    "current_use_cases": [
      "When operating in media specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_telecommunications": {
    "framework_name": "Strategic Options Framework (Telecommunications)",
    "current_use_cases": [
      "When operating in telecommunications specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_pharma": {
    "framework_name": "Strategic Options Framework (Pharma)",
    "current_use_cases": [
      "When operating in pharma specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_automotive": {
    "framework_name": "Strategic Options Framework (Automotive)",
    "current_use_cases": [
      "When operating in automotive specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_aerospace": {
    "framework_name": "Strategic Options Framework (Aerospace)",
    "current_use_cases": [
      "When operating in aerospace specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_agriculture": {
    "framework_name": "Strategic Options Framework (Agriculture)",
    "current_use_cases": [
      "When operating in agriculture specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_construction": {
    "framework_name": "Strategic Options Framework (Construction)",
    "current_use_cases": [
      "When operating in construction specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_logistics": {
    "framework_name": "Strategic Options Framework (Logistics)",
    "current_use_cases": [
      "When operating in logistics specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_ecommerce": {
    "framework_name": "Strategic Options Framework (Ecommerce)",
    "current_use_cases": [
      "When operating in ecommerce specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_saas": {
    "framework_name": "Strategic Options Framework (Saas)",
    "current_use_cases": [
      "When operating in saas specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_consulting": {
    "framework_name": "Strategic Options Framework (Consulting)",
    "current_use_cases": [
      "When operating in consulting specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_insurance": {
    "framework_name": "Strategic Options Framework (Insurance)",
    "current_use_cases": [
      "When operating in insurance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_real_estate": {
    "framework_name": "Strategic Options Framework (Real Estate)",
    "current_use_cases": [
      "When operating in real estate specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_gaming": {
    "framework_name": "Strategic Options Framework (Gaming)",
    "current_use_cases": [
      "When operating in gaming specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_sports": {
    "framework_name": "Strategic Options Framework (Sports)",
    "current_use_cases": [
      "When operating in sports specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_entertainment": {
    "framework_name": "Strategic Options Framework (Entertainment)",
    "current_use_cases": [
      "When operating in entertainment specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_startups": {
    "framework_name": "Strategic Options Framework (Startups)",
    "current_use_cases": [
      "When operating in startups focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_enterprises": {
    "framework_name": "Strategic Options Framework (Enterprises)",
    "current_use_cases": [
      "When operating in enterprises focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_smes": {
    "framework_name": "Strategic Options Framework (Smes)",
    "current_use_cases": [
      "When operating in smes focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_nonprofits": {
    "framework_name": "Strategic Options Framework (Nonprofits)",
    "current_use_cases": [
      "When operating in nonprofits focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_government": {
    "framework_name": "Strategic Options Framework (Government)",
    "current_use_cases": [
      "When operating in government focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_b2b": {
    "framework_name": "Strategic Options Framework (B2B)",
    "current_use_cases": [
      "When operating in b2b focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_b2c": {
    "framework_name": "Strategic Options Framework (B2C)",
    "current_use_cases": [
      "When operating in b2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_d2c": {
    "framework_name": "Strategic Options Framework (D2C)",
    "current_use_cases": [
      "When operating in d2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_marketplaces": {
    "framework_name": "Strategic Options Framework (Marketplaces)",
    "current_use_cases": [
      "When operating in marketplaces focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Sizing addressable market for new product launch"
    ]
  },
  "strategic_options_platforms": {
    "framework_name": "Strategic Options Framework (Platforms)",
    "current_use_cases": [
      "When operating in platforms focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_digital": {
    "framework_name": "Strategic Options Framework (Digital)",
    "current_use_cases": [
      "When operating in digital focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_mobile": {
    "framework_name": "Strategic Options Framework (Mobile)",
    "current_use_cases": [
      "When operating in mobile focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_cloud": {
    "framework_name": "Strategic Options Framework (Cloud)",
    "current_use_cases": [
      "When operating in cloud focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_ai_ml": {
    "framework_name": "Strategic Options Framework (Ai Ml)",
    "current_use_cases": [
      "When operating in ai ml focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_blockchain": {
    "framework_name": "Strategic Options Framework (Blockchain)",
    "current_use_cases": [
      "When operating in blockchain focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_remote": {
    "framework_name": "Strategic Options Framework (Remote)",
    "current_use_cases": [
      "When operating in remote focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_hybrid": {
    "framework_name": "Strategic Options Framework (Hybrid)",
    "current_use_cases": [
      "When operating in hybrid focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_global": {
    "framework_name": "Strategic Options Framework (Global)",
    "current_use_cases": [
      "When operating in global focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_local": {
    "framework_name": "Strategic Options Framework (Local)",
    "current_use_cases": [
      "When operating in local focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategic_options_emerging_markets": {
    "framework_name": "Strategic Options Framework (Emerging Markets)",
    "current_use_cases": [
      "When operating in emerging markets focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Sizing addressable market for new product launch"
    ]
  },
  "competitive_dynamics_technology": {
    "framework_name": "Competitive Dynamics (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_healthcare": {
    "framework_name": "Competitive Dynamics (Healthcare)",
    "current_use_cases": [
      "When operating in healthcare specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_finance": {
    "framework_name": "Competitive Dynamics (Finance)",
    "current_use_cases": [
      "When operating in finance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_retail": {
    "framework_name": "Competitive Dynamics (Retail)",
    "current_use_cases": [
      "When operating in retail specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_manufacturing": {
    "framework_name": "Competitive Dynamics (Manufacturing)",
    "current_use_cases": [
      "When operating in manufacturing specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_education": {
    "framework_name": "Competitive Dynamics (Education)",
    "current_use_cases": [
      "When operating in education specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_energy": {
    "framework_name": "Competitive Dynamics (Energy)",
    "current_use_cases": [
      "When operating in energy specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_transportation": {
    "framework_name": "Competitive Dynamics (Transportation)",
    "current_use_cases": [
      "When operating in transportation specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_hospitality": {
    "framework_name": "Competitive Dynamics (Hospitality)",
    "current_use_cases": [
      "When operating in hospitality specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_media": {
    "framework_name": "Competitive Dynamics (Media)",
    "current_use_cases": [
      "When operating in media specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_telecommunications": {
    "framework_name": "Competitive Dynamics (Telecommunications)",
    "current_use_cases": [
      "When operating in telecommunications specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_pharma": {
    "framework_name": "Competitive Dynamics (Pharma)",
    "current_use_cases": [
      "When operating in pharma specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_automotive": {
    "framework_name": "Competitive Dynamics (Automotive)",
    "current_use_cases": [
      "When operating in automotive specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_aerospace": {
    "framework_name": "Competitive Dynamics (Aerospace)",
    "current_use_cases": [
      "When operating in aerospace specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_agriculture": {
    "framework_name": "Competitive Dynamics (Agriculture)",
    "current_use_cases": [
      "When operating in agriculture specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_construction": {
    "framework_name": "Competitive Dynamics (Construction)",
    "current_use_cases": [
      "When operating in construction specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_logistics": {
    "framework_name": "Competitive Dynamics (Logistics)",
    "current_use_cases": [
      "When operating in logistics specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_ecommerce": {
    "framework_name": "Competitive Dynamics (Ecommerce)",
    "current_use_cases": [
      "When operating in ecommerce specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_saas": {
    "framework_name": "Competitive Dynamics (Saas)",
    "current_use_cases": [
      "When operating in saas specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_consulting": {
    "framework_name": "Competitive Dynamics (Consulting)",
    "current_use_cases": [
      "When operating in consulting specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_insurance": {
    "framework_name": "Competitive Dynamics (Insurance)",
    "current_use_cases": [
      "When operating in insurance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_real_estate": {
    "framework_name": "Competitive Dynamics (Real Estate)",
    "current_use_cases": [
      "When operating in real estate specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_gaming": {
    "framework_name": "Competitive Dynamics (Gaming)",
    "current_use_cases": [
      "When operating in gaming specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_sports": {
    "framework_name": "Competitive Dynamics (Sports)",
    "current_use_cases": [
      "When operating in sports specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_entertainment": {
    "framework_name": "Competitive Dynamics (Entertainment)",
    "current_use_cases": [
      "When operating in entertainment specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_startups": {
    "framework_name": "Competitive Dynamics (Startups)",
    "current_use_cases": [
      "When operating in startups focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_enterprises": {
    "framework_name": "Competitive Dynamics (Enterprises)",
    "current_use_cases": [
      "When operating in enterprises focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_smes": {
    "framework_name": "Competitive Dynamics (Smes)",
    "current_use_cases": [
      "When operating in smes focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_nonprofits": {
    "framework_name": "Competitive Dynamics (Nonprofits)",
    "current_use_cases": [
      "When operating in nonprofits focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_government": {
    "framework_name": "Competitive Dynamics (Government)",
    "current_use_cases": [
      "When operating in government focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_b2b": {
    "framework_name": "Competitive Dynamics (B2B)",
    "current_use_cases": [
      "When operating in b2b focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_b2c": {
    "framework_name": "Competitive Dynamics (B2C)",
    "current_use_cases": [
      "When operating in b2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_d2c": {
    "framework_name": "Competitive Dynamics (D2C)",
    "current_use_cases": [
      "When operating in d2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_marketplaces": {
    "framework_name": "Competitive Dynamics (Marketplaces)",
    "current_use_cases": [
      "When operating in marketplaces focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_platforms": {
    "framework_name": "Competitive Dynamics (Platforms)",
    "current_use_cases": [
      "When operating in platforms focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_digital": {
    "framework_name": "Competitive Dynamics (Digital)",
    "current_use_cases": [
      "When operating in digital focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_mobile": {
    "framework_name": "Competitive Dynamics (Mobile)",
    "current_use_cases": [
      "When operating in mobile focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_cloud": {
    "framework_name": "Competitive Dynamics (Cloud)",
    "current_use_cases": [
      "When operating in cloud focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_ai_ml": {
    "framework_name": "Competitive Dynamics (Ai Ml)",
    "current_use_cases": [
      "When operating in ai ml focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_blockchain": {
    "framework_name": "Competitive Dynamics (Blockchain)",
    "current_use_cases": [
      "When operating in blockchain focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_remote": {
    "framework_name": "Competitive Dynamics (Remote)",
    "current_use_cases": [
      "When operating in remote focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_hybrid": {
    "framework_name": "Competitive Dynamics (Hybrid)",
    "current_use_cases": [
      "When operating in hybrid focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_global": {
    "framework_name": "Competitive Dynamics (Global)",
    "current_use_cases": [
      "When operating in global focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_local": {
    "framework_name": "Competitive Dynamics (Local)",
    "current_use_cases": [
      "When operating in local focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "competitive_dynamics_emerging_markets": {
    "framework_name": "Competitive Dynamics (Emerging Markets)",
    "current_use_cases": [
      "When operating in emerging markets focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Entering a market dominated by 3-5 major players",
      "Defending against a new low-cost competitor",
      "Deciding whether to compete on price vs differentiation",
      "Evaluating acquisition targets to strengthen competitive position",
      "Responding to competitor's new product launch"
    ]
  },
  "strategy_execution_technology": {
    "framework_name": "Strategy Execution Framework (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_healthcare": {
    "framework_name": "Strategy Execution Framework (Healthcare)",
    "current_use_cases": [
      "When operating in healthcare specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_finance": {
    "framework_name": "Strategy Execution Framework (Finance)",
    "current_use_cases": [
      "When operating in finance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_retail": {
    "framework_name": "Strategy Execution Framework (Retail)",
    "current_use_cases": [
      "When operating in retail specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_manufacturing": {
    "framework_name": "Strategy Execution Framework (Manufacturing)",
    "current_use_cases": [
      "When operating in manufacturing specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_education": {
    "framework_name": "Strategy Execution Framework (Education)",
    "current_use_cases": [
      "When operating in education specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_energy": {
    "framework_name": "Strategy Execution Framework (Energy)",
    "current_use_cases": [
      "When operating in energy specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_transportation": {
    "framework_name": "Strategy Execution Framework (Transportation)",
    "current_use_cases": [
      "When operating in transportation specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_hospitality": {
    "framework_name": "Strategy Execution Framework (Hospitality)",
    "current_use_cases": [
      "When operating in hospitality specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_media": {
    "framework_name": "Strategy Execution Framework (Media)",
    "current_use_cases": [
      "When operating in media specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_telecommunications": {
    "framework_name": "Strategy Execution Framework (Telecommunications)",
    "current_use_cases": [
      "When operating in telecommunications specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_pharma": {
    "framework_name": "Strategy Execution Framework (Pharma)",
    "current_use_cases": [
      "When operating in pharma specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_automotive": {
    "framework_name": "Strategy Execution Framework (Automotive)",
    "current_use_cases": [
      "When operating in automotive specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_aerospace": {
    "framework_name": "Strategy Execution Framework (Aerospace)",
    "current_use_cases": [
      "When operating in aerospace specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_agriculture": {
    "framework_name": "Strategy Execution Framework (Agriculture)",
    "current_use_cases": [
      "When operating in agriculture specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_construction": {
    "framework_name": "Strategy Execution Framework (Construction)",
    "current_use_cases": [
      "When operating in construction specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_logistics": {
    "framework_name": "Strategy Execution Framework (Logistics)",
    "current_use_cases": [
      "When operating in logistics specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_ecommerce": {
    "framework_name": "Strategy Execution Framework (Ecommerce)",
    "current_use_cases": [
      "When operating in ecommerce specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_saas": {
    "framework_name": "Strategy Execution Framework (Saas)",
    "current_use_cases": [
      "When operating in saas specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_consulting": {
    "framework_name": "Strategy Execution Framework (Consulting)",
    "current_use_cases": [
      "When operating in consulting specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_insurance": {
    "framework_name": "Strategy Execution Framework (Insurance)",
    "current_use_cases": [
      "When operating in insurance specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_real_estate": {
    "framework_name": "Strategy Execution Framework (Real Estate)",
    "current_use_cases": [
      "When operating in real estate specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_gaming": {
    "framework_name": "Strategy Execution Framework (Gaming)",
    "current_use_cases": [
      "When operating in gaming specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_sports": {
    "framework_name": "Strategy Execution Framework (Sports)",
    "current_use_cases": [
      "When operating in sports specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_entertainment": {
    "framework_name": "Strategy Execution Framework (Entertainment)",
    "current_use_cases": [
      "When operating in entertainment specific",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_startups": {
    "framework_name": "Strategy Execution Framework (Startups)",
    "current_use_cases": [
      "When operating in startups focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_enterprises": {
    "framework_name": "Strategy Execution Framework (Enterprises)",
    "current_use_cases": [
      "When operating in enterprises focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_smes": {
    "framework_name": "Strategy Execution Framework (Smes)",
    "current_use_cases": [
      "When operating in smes focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_nonprofits": {
    "framework_name": "Strategy Execution Framework (Nonprofits)",
    "current_use_cases": [
      "When operating in nonprofits focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_government": {
    "framework_name": "Strategy Execution Framework (Government)",
    "current_use_cases": [
      "When operating in government focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_b2b": {
    "framework_name": "Strategy Execution Framework (B2B)",
    "current_use_cases": [
      "When operating in b2b focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_b2c": {
    "framework_name": "Strategy Execution Framework (B2C)",
    "current_use_cases": [
      "When operating in b2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_d2c": {
    "framework_name": "Strategy Execution Framework (D2C)",
    "current_use_cases": [
      "When operating in d2c focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_marketplaces": {
    "framework_name": "Strategy Execution Framework (Marketplaces)",
    "current_use_cases": [
      "When operating in marketplaces focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Sizing addressable market for new product launch"
    ]
  },
  "strategy_execution_platforms": {
    "framework_name": "Strategy Execution Framework (Platforms)",
    "current_use_cases": [
      "When operating in platforms focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_digital": {
    "framework_name": "Strategy Execution Framework (Digital)",
    "current_use_cases": [
      "When operating in digital focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_mobile": {
    "framework_name": "Strategy Execution Framework (Mobile)",
    "current_use_cases": [
      "When operating in mobile focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_cloud": {
    "framework_name": "Strategy Execution Framework (Cloud)",
    "current_use_cases": [
      "When operating in cloud focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_ai_ml": {
    "framework_name": "Strategy Execution Framework (Ai Ml)",
    "current_use_cases": [
      "When operating in ai ml focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_blockchain": {
    "framework_name": "Strategy Execution Framework (Blockchain)",
    "current_use_cases": [
      "When operating in blockchain focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_remote": {
    "framework_name": "Strategy Execution Framework (Remote)",
    "current_use_cases": [
      "When operating in remote focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_hybrid": {
    "framework_name": "Strategy Execution Framework (Hybrid)",
    "current_use_cases": [
      "When operating in hybrid focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_global": {
    "framework_name": "Strategy Execution Framework (Global)",
    "current_use_cases": [
      "When operating in global focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_local": {
    "framework_name": "Strategy Execution Framework (Local)",
    "current_use_cases": [
      "When operating in local focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off"
    ]
  },
  "strategy_execution_emerging_markets": {
    "framework_name": "Strategy Execution Framework (Emerging Markets)",
    "current_use_cases": [
      "When operating in emerging markets focus",
      "For strategy optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Deciding which product lines to sunset when resources are limited",
      "Allocating R&D budget across products with different growth rates",
      "Identifying which business units to sell or spin off",
      "Sizing addressable market for new product launch"
    ]
  },
  "innovation_pipeline_technology": {
    "framework_name": "Innovation Pipeline (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_healthcare": {
    "framework_name": "Innovation Pipeline (Healthcare)",
    "current_use_cases": [
      "When operating in healthcare specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_finance": {
    "framework_name": "Innovation Pipeline (Finance)",
    "current_use_cases": [
      "When operating in finance specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_retail": {
    "framework_name": "Innovation Pipeline (Retail)",
    "current_use_cases": [
      "When operating in retail specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_manufacturing": {
    "framework_name": "Innovation Pipeline (Manufacturing)",
    "current_use_cases": [
      "When operating in manufacturing specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_education": {
    "framework_name": "Innovation Pipeline (Education)",
    "current_use_cases": [
      "When operating in education specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_energy": {
    "framework_name": "Innovation Pipeline (Energy)",
    "current_use_cases": [
      "When operating in energy specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_transportation": {
    "framework_name": "Innovation Pipeline (Transportation)",
    "current_use_cases": [
      "When operating in transportation specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_hospitality": {
    "framework_name": "Innovation Pipeline (Hospitality)",
    "current_use_cases": [
      "When operating in hospitality specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_media": {
    "framework_name": "Innovation Pipeline (Media)",
    "current_use_cases": [
      "When operating in media specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_telecommunications": {
    "framework_name": "Innovation Pipeline (Telecommunications)",
    "current_use_cases": [
      "When operating in telecommunications specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_pharma": {
    "framework_name": "Innovation Pipeline (Pharma)",
    "current_use_cases": [
      "When operating in pharma specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_automotive": {
    "framework_name": "Innovation Pipeline (Automotive)",
    "current_use_cases": [
      "When operating in automotive specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_aerospace": {
    "framework_name": "Innovation Pipeline (Aerospace)",
    "current_use_cases": [
      "When operating in aerospace specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_agriculture": {
    "framework_name": "Innovation Pipeline (Agriculture)",
    "current_use_cases": [
      "When operating in agriculture specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_construction": {
    "framework_name": "Innovation Pipeline (Construction)",
    "current_use_cases": [
      "When operating in construction specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_logistics": {
    "framework_name": "Innovation Pipeline (Logistics)",
    "current_use_cases": [
      "When operating in logistics specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_ecommerce": {
    "framework_name": "Innovation Pipeline (Ecommerce)",
    "current_use_cases": [
      "When operating in ecommerce specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_saas": {
    "framework_name": "Innovation Pipeline (Saas)",
    "current_use_cases": [
      "When operating in saas specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_consulting": {
    "framework_name": "Innovation Pipeline (Consulting)",
    "current_use_cases": [
      "When operating in consulting specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_insurance": {
    "framework_name": "Innovation Pipeline (Insurance)",
    "current_use_cases": [
      "When operating in insurance specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_real_estate": {
    "framework_name": "Innovation Pipeline (Real Estate)",
    "current_use_cases": [
      "When operating in real estate specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_gaming": {
    "framework_name": "Innovation Pipeline (Gaming)",
    "current_use_cases": [
      "When operating in gaming specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_sports": {
    "framework_name": "Innovation Pipeline (Sports)",
    "current_use_cases": [
      "When operating in sports specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_entertainment": {
    "framework_name": "Innovation Pipeline (Entertainment)",
    "current_use_cases": [
      "When operating in entertainment specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_startups": {
    "framework_name": "Innovation Pipeline (Startups)",
    "current_use_cases": [
      "When operating in startups focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_enterprises": {
    "framework_name": "Innovation Pipeline (Enterprises)",
    "current_use_cases": [
      "When operating in enterprises focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_smes": {
    "framework_name": "Innovation Pipeline (Smes)",
    "current_use_cases": [
      "When operating in smes focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_nonprofits": {
    "framework_name": "Innovation Pipeline (Nonprofits)",
    "current_use_cases": [
      "When operating in nonprofits focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_government": {
    "framework_name": "Innovation Pipeline (Government)",
    "current_use_cases": [
      "When operating in government focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_b2b": {
    "framework_name": "Innovation Pipeline (B2B)",
    "current_use_cases": [
      "When operating in b2b focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_b2c": {
    "framework_name": "Innovation Pipeline (B2C)",
    "current_use_cases": [
      "When operating in b2c focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_d2c": {
    "framework_name": "Innovation Pipeline (D2C)",
    "current_use_cases": [
      "When operating in d2c focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_marketplaces": {
    "framework_name": "Innovation Pipeline (Marketplaces)",
    "current_use_cases": [
      "When operating in marketplaces focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Sizing addressable market for new product launch",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_platforms": {
    "framework_name": "Innovation Pipeline (Platforms)",
    "current_use_cases": [
      "When operating in platforms focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_digital": {
    "framework_name": "Innovation Pipeline (Digital)",
    "current_use_cases": [
      "When operating in digital focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_mobile": {
    "framework_name": "Innovation Pipeline (Mobile)",
    "current_use_cases": [
      "When operating in mobile focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_cloud": {
    "framework_name": "Innovation Pipeline (Cloud)",
    "current_use_cases": [
      "When operating in cloud focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_ai_ml": {
    "framework_name": "Innovation Pipeline (Ai Ml)",
    "current_use_cases": [
      "When operating in ai ml focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_blockchain": {
    "framework_name": "Innovation Pipeline (Blockchain)",
    "current_use_cases": [
      "When operating in blockchain focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_remote": {
    "framework_name": "Innovation Pipeline (Remote)",
    "current_use_cases": [
      "When operating in remote focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_hybrid": {
    "framework_name": "Innovation Pipeline (Hybrid)",
    "current_use_cases": [
      "When operating in hybrid focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_global": {
    "framework_name": "Innovation Pipeline (Global)",
    "current_use_cases": [
      "When operating in global focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_local": {
    "framework_name": "Innovation Pipeline (Local)",
    "current_use_cases": [
      "When operating in local focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_pipeline_emerging_markets": {
    "framework_name": "Innovation Pipeline (Emerging Markets)",
    "current_use_cases": [
      "When operating in emerging markets focus",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Sizing addressable market for new product launch",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "disruptive_innovation_technology": {
    "framework_name": "Disruptive Innovation (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "disruptive_innovation_healthcare": {
    "framework_name": "Disruptive Innovation (Healthcare)",
    "current_use_cases": [
      "When operating in healthcare specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "disruptive_innovation_finance": {
    "framework_name": "Disruptive Innovation (Finance)",
    "current_use_cases": [
      "When operating in finance specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "disruptive_innovation_retail": {
    "framework_name": "Disruptive Innovation (Retail)",
    "current_use_cases": [
      "When operating in retail specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "disruptive_innovation_manufacturing": {
    "framework_name": "Disruptive Innovation (Manufacturing)",
    "current_use_cases": [
      "When operating in manufacturing specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_culture_technology": {
    "framework_name": "Innovation Culture (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_metrics_technology": {
    "framework_name": "Innovation Metrics (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_ecosystem_technology": {
    "framework_name": "Innovation Ecosystem (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "reverse_innovation_technology": {
    "framework_name": "Reverse Innovation (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "frugal_innovation_technology": {
    "framework_name": "Frugal Innovation (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_adoption_technology": {
    "framework_name": "Innovation Adoption (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_portfolio_technology": {
    "framework_name": "Innovation Portfolio (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  },
  "innovation_process_technology": {
    "framework_name": "Innovation Process (Technology)",
    "current_use_cases": [
      "When operating in technology specific",
      "For innovation optimization",
      "Strategic planning and execution",
      "Performance improvement initiatives",
      "Competitive advantage development"
    ],
    "enhanced_use_cases": [
      "Testing product-market fit with less than $50K budget",
      "Validating B2B SaaS idea before writing code",
      "Pivoting based on customer feedback after 3 months",
      "Building innovation pipeline for next 3 years"
    ]
  }
}

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
    
    print(f"\nTotal frameworks updated: {updated_count}")
    
    # Save the updated database
    # This would need to be implemented to persist changes

if __name__ == "__main__":
    update_framework_use_cases()
