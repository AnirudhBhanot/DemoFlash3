#!/usr/bin/env python3
"""
Generate tags for all frameworks based on their definitions
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from framework_intelligence.framework_database import FRAMEWORKS, FrameworkCategory
from framework_intelligence.framework_taxonomy import *
from framework_intelligence.framework_tags_database import FrameworkTags
import re

def analyze_framework(framework_id, framework):
    """Generate appropriate tags based on framework attributes"""
    
    # Determine temporal stages based on when_to_use and name
    temporal_stages = []
    
    # Check for stage indicators in when_to_use
    when_to_use_text = " ".join(framework.when_to_use).lower()
    description_lower = framework.description.lower()
    name_lower = framework.name.lower()
    
    # Early stage indicators
    if any(term in when_to_use_text or term in description_lower for term in 
           ["early stage", "startup", "new venture", "ideation", "concept", "founding"]):
        temporal_stages.extend([TemporalStage.PRE_FORMATION, TemporalStage.FORMATION])
    
    # Validation stage
    if any(term in when_to_use_text or term in description_lower for term in 
           ["validation", "mvp", "product-market fit", "pilot", "prototype"]):
        temporal_stages.append(TemporalStage.VALIDATION)
    
    # Growth stages
    if any(term in when_to_use_text or term in description_lower for term in 
           ["growth", "scaling", "expansion", "market share"]):
        temporal_stages.extend([TemporalStage.GROWTH, TemporalStage.SCALE])
    
    # Mature stage
    if any(term in when_to_use_text or term in description_lower for term in 
           ["mature", "established", "optimize", "efficiency", "transformation"]):
        temporal_stages.append(TemporalStage.MATURITY)
    
    # If no specific stage found, make it universal
    if not temporal_stages:
        temporal_stages = [TemporalStage.VALIDATION, TemporalStage.TRACTION, TemporalStage.GROWTH]
    
    # Determine problem archetypes
    problem_archetypes = []
    
    problem_map = {
        ProblemArchetype.CUSTOMER_DISCOVERY: ["customer", "user", "needs", "discovery", "research"],
        ProblemArchetype.PRODUCT_MARKET_FIT: ["product-market fit", "pmf", "validation", "traction"],
        ProblemArchetype.BUSINESS_MODEL_DESIGN: ["business model", "revenue", "monetization", "pricing"],
        ProblemArchetype.GROWTH_MECHANICS: ["growth", "acquisition", "retention", "expansion"],
        ProblemArchetype.UNIT_ECONOMICS_OPTIMIZATION: ["unit economics", "ltv", "cac", "margins", "profitability"],
        ProblemArchetype.COMPETITIVE_STRATEGY: ["competitive", "competition", "positioning", "differentiation"],
        ProblemArchetype.MARKET_ANALYSIS: ["market", "industry", "trends", "analysis"],
        ProblemArchetype.PORTFOLIO_OPTIMIZATION: ["portfolio", "resource allocation", "prioritization"],
        ProblemArchetype.INNOVATION_MANAGEMENT: ["innovation", "new products", "r&d", "disruption"],
        ProblemArchetype.OPERATIONAL_EXCELLENCE: ["operations", "efficiency", "process", "optimization", "excellence", "lean", "six sigma", "quality"],
        ProblemArchetype.ORGANIZATIONAL_DESIGN: ["organization", "culture", "team", "alignment", "structure", "design"],
        ProblemArchetype.FINANCIAL_PLANNING: ["financial", "forecast", "budget", "cash flow", "planning", "finance"],
        ProblemArchetype.RISK_MANAGEMENT: ["risk", "mitigation", "compliance", "security"],
        ProblemArchetype.TALENT_MANAGEMENT: ["talent", "hiring", "people", "hr", "human resources", "team building"],
        ProblemArchetype.DIGITAL_TRANSFORMATION: ["digital", "transformation", "technology", "digitization", "automation"],
    }
    
    for archetype, keywords in problem_map.items():
        if any(keyword in when_to_use_text or keyword in description_lower for keyword in keywords):
            problem_archetypes.append(archetype)
    
    if not problem_archetypes:
        problem_archetypes = [ProblemArchetype.COMPETITIVE_STRATEGY]
    
    # Determine decision contexts
    decision_contexts = []
    
    if any(term in when_to_use_text for term in ["explore", "discover", "ideate", "brainstorm"]):
        decision_contexts.append(DecisionContext.EXPLORATORY)
    if any(term in when_to_use_text for term in ["assess", "analyze", "evaluate", "understand"]):
        decision_contexts.append(DecisionContext.DIAGNOSTIC)
    if any(term in when_to_use_text for term in ["recommend", "decide", "choose", "action"]):
        decision_contexts.append(DecisionContext.PRESCRIPTIVE)
    if any(term in when_to_use_text for term in ["forecast", "predict", "project", "scenario"]):
        decision_contexts.append(DecisionContext.PREDICTIVE)
    if any(term in when_to_use_text for term in ["measure", "track", "monitor", "evaluate"]):
        decision_contexts.append(DecisionContext.EVALUATIVE)
    
    if not decision_contexts:
        decision_contexts = [DecisionContext.DIAGNOSTIC, DecisionContext.PRESCRIPTIVE]
    
    # Determine data requirements
    data_requirements = [DataRequirement.QUALITATIVE_ONLY]  # Base requirement
    
    if any(term in when_to_use_text or term in description_lower for term in 
           ["metrics", "data", "numbers", "quantitative", "measure"]):
        data_requirements.append(DataRequirement.BASIC_QUANTITATIVE)
    
    if any(term in when_to_use_text or term in description_lower for term in 
           ["ltv", "cac", "cohort", "retention", "advanced metrics"]):
        data_requirements.append(DataRequirement.ADVANCED_METRICS)
    
    if any(term in when_to_use_text or term in description_lower for term in 
           ["market share", "market size", "tam", "competition"]):
        data_requirements.append(DataRequirement.MARKET_DATA)
    
    # Determine complexity
    complexity_map = {
        "1-2 hours": ComplexityTier.PLUG_AND_PLAY,
        "1-2 days": ComplexityTier.SIMPLE,
        "1-2 weeks": ComplexityTier.MODERATE,
        "2-4 weeks": ComplexityTier.COMPLEX,
        "1-3 months": ComplexityTier.ENTERPRISE,
        "3+ months": ComplexityTier.ENTERPRISE
    }
    
    complexity = ComplexityTier.MODERATE  # Default
    if framework.time_to_implement:
        for time_str, tier in complexity_map.items():
            if time_str in framework.time_to_implement:
                complexity = tier
                break
    
    # Determine outcome types
    outcome_types = []
    outcome_map = {
        OutcomeType.STRATEGIC_CLARITY: ["strategy", "direction", "vision", "clarity"],
        OutcomeType.TACTICAL_ACTIONS: ["actions", "tactics", "implementation", "steps"],
        OutcomeType.FINANCIAL_PROJECTIONS: ["revenue", "profit", "cost", "financial", "projections", "forecast"],
        OutcomeType.OPERATIONAL_IMPROVEMENTS: ["efficiency", "productivity", "optimization", "improvements", "operations"],
        OutcomeType.CUSTOMER_INSIGHTS: ["customer", "user", "insights", "needs"],
        OutcomeType.COMPETITIVE_ADVANTAGE: ["competitive", "advantage", "differentiation"],
        OutcomeType.RISK_MITIGATION: ["risk", "mitigation", "compliance"],
        OutcomeType.INNOVATION_PIPELINE: ["innovation", "new products", "pipeline"],
        OutcomeType.ORGANIZATIONAL_DESIGN: ["culture", "team", "organization", "alignment", "structure"],
        OutcomeType.GROWTH_STRATEGY: ["growth", "scaling", "expansion", "market share"]
    }
    
    for outcome, keywords in outcome_map.items():
        if any(keyword in description_lower or keyword in str(framework.expected_outcomes).lower() 
               for keyword in keywords):
            outcome_types.append(outcome)
    
    if not outcome_types:
        outcome_types = [OutcomeType.STRATEGIC_CLARITY, OutcomeType.TACTICAL_ACTIONS]
    
    # Determine industry contexts
    industry_contexts = []
    
    # Check if it's industry-specific
    industry_map = {
        "saas": IndustryContext.B2B_SAAS,
        "marketplace": IndustryContext.MARKETPLACE,
        "fintech": IndustryContext.FINTECH,
        "healthtech": IndustryContext.HEALTHTECH,
        "healthcare": IndustryContext.HEALTHTECH,
        "edtech": IndustryContext.EDTECH,
        "ecommerce": IndustryContext.ECOMMERCE,
        "retail": IndustryContext.RETAIL,
        "manufacturing": IndustryContext.MANUFACTURING,
        "services": IndustryContext.SERVICES,
        "consumer": IndustryContext.CONSUMER_GOODS,
        "hardware": IndustryContext.HARDWARE,
        "cleantech": IndustryContext.CLEANTECH,
        "biotech": IndustryContext.BIOTECH,
        "enterprise": IndustryContext.ENTERPRISE_SOFTWARE
    }
    
    framework_id_lower = framework_id.lower()
    for industry_key, industry_context in industry_map.items():
        if industry_key in framework_id_lower or industry_key in name_lower:
            industry_contexts.append(industry_context)
    
    # If no specific industry, make it universal
    if not industry_contexts:
        if "All industries" in str(framework.industry_relevance):
            industry_contexts = [IndustryContext.UNIVERSAL]
        else:
            industry_contexts = [IndustryContext.UNIVERSAL]
    
    # Determine team size
    team_size_min = 1
    team_size_max = 10000
    
    # Look for team size indicators
    if "enterprise" in name_lower or "large" in description_lower:
        team_size_min = 100
    elif "startup" in name_lower or "small" in description_lower:
        team_size_max = 50
    
    # Extract from complexity
    if complexity == ComplexityTier.ENTERPRISE:
        team_size_min = 50
    elif complexity == ComplexityTier.PLUG_AND_PLAY:
        team_size_max = 20
    
    # Time to value
    time_to_value_map = {
        "1-2 hours": 1,
        "1-2 days": 2,
        "1 week": 7,
        "2 weeks": 14,
        "1 month": 30,
        "2-4 weeks": 21,
        "1-3 months": 60,
        "3-6 months": 120
    }
    
    time_to_value_days = 14  # Default
    if framework.time_to_implement:
        for time_str, days in time_to_value_map.items():
            if time_str in framework.time_to_implement:
                time_to_value_days = days
                break
    
    # Create keywords
    keywords = set()
    # Extract from name
    keywords.update(framework.name.lower().split())
    # Extract from key components
    for component in framework.key_components[:5]:
        keywords.update(component.lower().split()[:2])
    # Remove common words
    keywords.discard("the")
    keywords.discard("and")
    keywords.discard("of")
    keywords.discard("for")
    keywords.discard("to")
    keywords.discard("a")
    
    # Create tags
    return FrameworkTags(
        temporal_stages=list(set(temporal_stages)),
        problem_archetypes=list(set(problem_archetypes))[:5],  # Limit to 5
        decision_contexts=list(set(decision_contexts)),
        data_requirements=list(set(data_requirements)),
        complexity_tier=complexity,
        outcome_types=list(set(outcome_types))[:3],  # Limit to 3
        industry_contexts=industry_contexts,
        typical_users=["CEO", "Strategy Lead", "Product Manager", "Consultant"],
        team_size_min=team_size_min,
        team_size_max=team_size_max,
        time_to_value_days=time_to_value_days,
        durability_months=12,  # Default
        ease_of_use=70 if complexity in [ComplexityTier.PLUG_AND_PLAY, ComplexityTier.SIMPLE] else 50,
        actionability=80 if DecisionContext.PRESCRIPTIVE in decision_contexts else 60,
        accuracy=70,  # Default
        strategic_impact=80 if framework.category == FrameworkCategory.STRATEGY else 60,
        requires_facilitator=complexity in [ComplexityTier.COMPLEX, ComplexityTier.ENTERPRISE],
        requires_software=False,  # Default, could be enhanced
        has_variants="_" in framework_id and any(ind in framework_id for ind in industry_map.keys()),
        keywords=keywords
    )

def generate_all_tags():
    """Generate tags for all frameworks"""
    
    all_tags = {}
    
    # First, preserve existing tags
    from framework_tags_database import create_framework_tags_database
    existing_tags = create_framework_tags_database()
    all_tags.update(existing_tags)
    
    # Generate tags for frameworks that don't have them
    for framework_id, framework in FRAMEWORKS.items():
        if framework_id not in all_tags:
            try:
                tags = analyze_framework(framework_id, framework)
                all_tags[framework_id] = tags
                print(f"Generated tags for: {framework_id}")
            except Exception as e:
                print(f"Error generating tags for {framework_id}: {e}")
    
    return all_tags

if __name__ == "__main__":
    print("Generating tags for all frameworks...")
    all_tags = generate_all_tags()
    print(f"\nTotal frameworks with tags: {len(all_tags)}")
    
    # Save to file
    with open("generated_framework_tags.py", "w") as f:
        f.write("# Auto-generated framework tags\n")
        f.write("from framework_taxonomy import *\n\n")
        f.write("GENERATED_TAGS = {\n")
        
        for fid, tags in sorted(all_tags.items()):
            f.write(f'    "{fid}": FrameworkTags(\n')
            f.write(f'        temporal_stages={[s.name for s in tags.temporal_stages]},\n')
            f.write(f'        problem_archetypes={[p.name for p in tags.problem_archetypes]},\n')
            f.write(f'        decision_contexts={[d.name for d in tags.decision_contexts]},\n')
            f.write(f'        data_requirements={[r.name for r in tags.data_requirements]},\n')
            f.write(f'        complexity_tier=ComplexityTier.{tags.complexity_tier.name},\n')
            f.write(f'        outcome_types={[o.name for o in tags.outcome_types]},\n')
            f.write(f'        industry_contexts={[i.name for i in tags.industry_contexts]},\n')
            f.write(f'        typical_users={tags.typical_users},\n')
            f.write(f'        team_size_min={tags.team_size_min},\n')
            f.write(f'        team_size_max={tags.team_size_max},\n')
            f.write(f'        time_to_value_days={tags.time_to_value_days},\n')
            f.write(f'        durability_months={tags.durability_months},\n')
            f.write(f'        ease_of_use={tags.ease_of_use},\n')
            f.write(f'        actionability={tags.actionability},\n')
            f.write(f'        accuracy={tags.accuracy},\n')
            f.write(f'        strategic_impact={tags.strategic_impact},\n')
            f.write(f'        requires_facilitator={tags.requires_facilitator},\n')
            f.write(f'        requires_software={tags.requires_software},\n')
            f.write(f'        has_variants={tags.has_variants},\n')
            f.write(f'        keywords={tags.keywords}\n')
            f.write('    ),\n')
        
        f.write("}\n")
    
    print("Tags saved to generated_framework_tags.py")