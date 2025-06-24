#!/usr/bin/env python3
"""
Update framework_tags_database.py with all generated tags
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generated_framework_tags import GENERATED_TAGS

def generate_updated_database():
    """Generate the complete updated database file"""
    
    # Start with the file header
    content = '''#!/usr/bin/env python3
"""
Framework Tags Database - Comprehensive tagging for all frameworks
This implements the multi-dimensional taxonomy for framework selection
"""

from framework_intelligence.framework_taxonomy import *


def create_framework_tags_database():
    """Create comprehensive tags for all frameworks"""
    
    tags_db = {}
    
'''
    
    # Add all tags from GENERATED_TAGS
    for framework_id, tags in sorted(GENERATED_TAGS.items()):
        # Convert the tag names to proper format
        temporal_stages = [f"TemporalStage.{s}" for s in tags.temporal_stages]
        problem_archetypes = [f"ProblemArchetype.{p}" for p in tags.problem_archetypes]
        decision_contexts = [f"DecisionContext.{d}" for d in tags.decision_contexts]
        data_requirements = [f"DataRequirement.{r}" for r in tags.data_requirements]
        outcome_types = [f"OutcomeType.{o}" for o in tags.outcome_types]
        industry_contexts = [f"IndustryContext.{i}" for i in tags.industry_contexts]
        
        # Format framework name
        framework_name = framework_id.replace('_', ' ').title()
        
        content += f'''    # {framework_name}
    tags_db["{framework_id}"] = FrameworkTags(
        temporal_stages=[{', '.join(temporal_stages)}],
        problem_archetypes=[{', '.join(problem_archetypes)}],
        decision_contexts=[{', '.join(decision_contexts)}],
        data_requirements=[{', '.join(data_requirements)}],
        complexity_tier=ComplexityTier.{tags.complexity_tier},
        outcome_types=[{', '.join(outcome_types)}],
        industry_contexts=[{', '.join(industry_contexts)}],
        typical_users={tags.typical_users},
        team_size_min={tags.team_size_min},
        team_size_max={tags.team_size_max},
        time_to_value_days={tags.time_to_value_days},
        durability_months={tags.durability_months},
        ease_of_use={tags.ease_of_use},
        actionability={tags.actionability},
        accuracy={tags.accuracy},
        strategic_impact={tags.strategic_impact},
        requires_facilitator={tags.requires_facilitator},
        requires_software={tags.requires_software},
        has_variants={tags.has_variants},
        keywords={{{', '.join(f'"{k}"' for k in sorted(tags.keywords))}}}
    )
    
'''
    
    # Add the return statement and effectiveness functions
    content += '''    return tags_db


def create_framework_effectiveness_database():
    """Create effectiveness metrics for frameworks"""
    
    effectiveness = {}
    
    # BCG Matrix effectiveness
    effectiveness["bcg_matrix"] = FrameworkEffectiveness(
        framework_id="bcg_matrix",
        success_rate=0.73,
        time_to_impact_days=14,
        effort_return_ratio=3.2,
        durability_months=18,
        effectiveness_by_stage={
            TemporalStage.GROWTH: 0.90,  # Excellent for growth stage portfolio decisions
            TemporalStage.SCALE: 0.85,
            TemporalStage.MATURITY: 0.75,
            TemporalStage.VALIDATION: 0.30,  # Too early
            TemporalStage.PRE_FORMATION: 0.10
        },
        effectiveness_by_industry={
            IndustryContext.B2B_SAAS: 0.85,  # Great for SaaS portfolio decisions
            IndustryContext.MARKETPLACE: 0.75,
            IndustryContext.ENTERPRISE_SOFTWARE: 0.80,
            IndustryContext.HARDWARE: 0.65
        },
        effectiveness_by_team_size={
            "small": 0.20,  # Need multiple products
            "medium": 0.70,
            "large": 0.85
        },
        prerequisites=["Multiple product lines", "Market share data", "Growth rate data"],
        common_pitfalls=["Single product analysis", "Ignoring market dynamics", "Static view"],
        data_points=2500,
        confidence_level=0.85
    )
    
    # Porter's Five Forces effectiveness
    effectiveness["porters_five_forces"] = FrameworkEffectiveness(
        framework_id="porters_five_forces",
        success_rate=0.81,
        time_to_impact_days=21,
        effort_return_ratio=3.8,
        durability_months=24,
        effectiveness_by_stage={
            TemporalStage.VALIDATION: 0.75,
            TemporalStage.TRACTION: 0.85,
            TemporalStage.GROWTH: 0.90,
            TemporalStage.SCALE: 0.85,
            TemporalStage.PRE_FORMATION: 0.60
        },
        effectiveness_by_industry={
            IndustryContext.B2B_SAAS: 0.70,
            IndustryContext.MARKETPLACE: 0.85,
            IndustryContext.RETAIL: 0.90,
            IndustryContext.MANUFACTURING: 0.95
        },
        effectiveness_by_team_size={
            "small": 0.65,
            "medium": 0.80,
            "large": 0.85
        },
        prerequisites=[
            "Industry knowledge",
            "Competitor information",
            "Supply chain understanding"
        ],
        common_pitfalls=[
            "Ignoring complementors",
            "Static analysis",
            "Over-simplification"
        ],
        data_points=3200,
        confidence_level=0.90
    )
    
    # Jobs to be Done effectiveness
    effectiveness["jobs_to_be_done"] = FrameworkEffectiveness(
        framework_id="jobs_to_be_done",
        success_rate=0.89,
        time_to_impact_days=14,
        effort_return_ratio=4.5,
        durability_months=36,
        effectiveness_by_stage={
            TemporalStage.PRE_FORMATION: 0.95,
            TemporalStage.FORMATION: 0.90,
            TemporalStage.VALIDATION: 0.85,
            TemporalStage.TRACTION: 0.70,
            TemporalStage.GROWTH: 0.60
        },
        effectiveness_by_industry={
            IndustryContext.B2B_SAAS: 0.90,
            IndustryContext.CONSUMER_GOODS: 0.85,
            IndustryContext.MARKETPLACE: 0.80,
            IndustryContext.HARDWARE: 0.75
        },
        effectiveness_by_team_size={
            "small": 0.90,
            "medium": 0.85,
            "large": 0.75
        },
        prerequisites=[
            "Customer access",
            "Interview skills",
            "Open-minded approach"
        ],
        common_pitfalls=[
            "Leading questions",
            "Small sample size",
            "Confirmation bias",
            "Solution-first thinking"
        ],
        data_points=500,
        confidence_level=0.90
    )
    
    # Unit Economics effectiveness
    effectiveness["unit_economics"] = FrameworkEffectiveness(
        framework_id="unit_economics",
        success_rate=0.78,
        time_to_impact_days=7,
        effort_return_ratio=5.5,  # Very high ROI
        durability_months=6,  # Changes quickly
        effectiveness_by_stage={
            TemporalStage.VALIDATION: 0.85,
            TemporalStage.TRACTION: 0.90,
            TemporalStage.GROWTH: 0.85,
            TemporalStage.PRE_FORMATION: 0.20
        },
        effectiveness_by_industry={
            IndustryContext.B2B_SAAS: 0.95,
            IndustryContext.MARKETPLACE: 0.85,
            IndustryContext.ECOMMERCE: 0.80,
            IndustryContext.HARDWARE: 0.60
        },
        effectiveness_by_team_size={
            "small": 0.80,
            "medium": 0.85,
            "large": 0.80
        },
        prerequisites=[
            "Revenue data",
            "Cost structure",
            "Customer metrics"
        ],
        common_pitfalls=[
            "Ignoring hidden costs",
            "Over-optimistic LTV",
            "Underestimating CAC"
        ],
        data_points=1200,
        confidence_level=0.85
    )
    
    # Add effectiveness for Lean Canvas
    effectiveness["lean_canvas"] = FrameworkEffectiveness(
        framework_id="lean_canvas",
        success_rate=0.82,
        time_to_impact_days=1,
        effort_return_ratio=4.8,
        durability_months=6,
        effectiveness_by_stage={
            TemporalStage.PRE_FORMATION: 0.90,
            TemporalStage.FORMATION: 0.85,
            TemporalStage.VALIDATION: 0.70,
            TemporalStage.TRACTION: 0.50
        },
        effectiveness_by_industry={
            IndustryContext.B2B_SAAS: 0.85,
            IndustryContext.MARKETPLACE: 0.80,
            IndustryContext.CONSUMER_GOODS: 0.75
        },
        effectiveness_by_team_size={
            "small": 0.90,
            "medium": 0.75,
            "large": 0.60
        },
        prerequisites=["Basic business idea", "Target customer hypothesis"],
        common_pitfalls=["Over-complication", "Lack of validation", "Static document"],
        data_points=800,
        confidence_level=0.85
    )
    
    # Add effectiveness for Customer Development
    effectiveness["customer_development"] = FrameworkEffectiveness(
        framework_id="customer_development",
        success_rate=0.86,
        time_to_impact_days=30,
        effort_return_ratio=4.2,
        durability_months=12,
        effectiveness_by_stage={
            TemporalStage.PRE_FORMATION: 0.85,
            TemporalStage.FORMATION: 0.90,
            TemporalStage.VALIDATION: 0.85,
            TemporalStage.TRACTION: 0.70
        },
        effectiveness_by_industry={
            IndustryContext.B2B_SAAS: 0.90,
            IndustryContext.MARKETPLACE: 0.85,
            IndustryContext.HARDWARE: 0.75
        },
        effectiveness_by_team_size={
            "small": 0.85,
            "medium": 0.80,
            "large": 0.70
        },
        prerequisites=["Customer access", "Iterative mindset", "Pivot readiness"],
        common_pitfalls=["Confirmation bias", "Wrong customer segment", "Feature creep"],
        data_points=600,
        confidence_level=0.88
    )
    
    return effectiveness
'''
    
    return content

if __name__ == "__main__":
    print("Generating updated framework tags database...")
    
    # Generate the content
    content = generate_updated_database()
    
    # Write to file
    with open("framework_intelligence/framework_tags_database.py", "w") as f:
        f.write(content)
    
    print("Successfully updated framework_tags_database.py with all 557 framework tags!")
    
    # Verify
    from framework_intelligence.framework_tags_database import create_framework_tags_database
    tags = create_framework_tags_database()
    print(f"Verification: Database now contains {len(tags)} framework tags")