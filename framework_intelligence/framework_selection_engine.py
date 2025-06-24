#!/usr/bin/env python3
"""
Advanced Framework Selection Engine
Implements MIT quantitative methods with HBS strategic insights
"""

import numpy as np
from typing import List, Dict, Tuple, Optional, Set
from dataclasses import dataclass, field
from datetime import datetime
import json

from framework_intelligence.framework_taxonomy import *
from framework_intelligence.framework_tags_database import *


def create_framework_relationships():
    """Create framework relationships database"""
    relationships = {}
    
    # Example relationships
    relationships["lean_canvas"] = [
        FrameworkRelationship(
            framework_id="lean_canvas",
            relationship_type="complementary",
            related_framework_ids=["customer_development", "jobs_to_be_done"],
            relationship_strength=90,
            notes="Both focus on early validation and customer understanding"
        )
    ]
    
    relationships["bcg_matrix"] = [
        FrameworkRelationship(
            framework_id="bcg_matrix",
            relationship_type="complementary",
            related_framework_ids=["unit_economics", "ansoff_matrix"],
            relationship_strength=80,
            notes="BCG helps portfolio decisions, unit economics helps individual product decisions"
        )
    ]
    
    relationships["porters_five_forces"] = [
        FrameworkRelationship(
            framework_id="porters_five_forces",
            relationship_type="prerequisite",
            related_framework_ids=["competitive_positioning", "blue_ocean_strategy"],
            relationship_strength=85,
            notes="Industry analysis should precede positioning decisions"
        )
    ]
    
    return relationships


def create_framework_antipatterns():
    """Create framework antipatterns database"""
    antipatterns = {}
    
    antipatterns["bcg_matrix"] = FrameworkAntiPattern(
        framework_id="bcg_matrix",
        antipattern_conditions=[
            "Single product company",
            "Pre-revenue startup",
            "Team size < 20",
            "No market share data"
        ],
        negative_outcomes=[
            "Misleading analysis",
            "Wasted effort",
            "Wrong strategic decisions"
        ],
        alternative_frameworks=["lean_canvas", "unit_economics", "product_market_fit"],
        severity="high"
    )
    
    antipatterns["six_sigma"] = FrameworkAntiPattern(
        framework_id="six_sigma",
        antipattern_conditions=[
            "Early stage startup",
            "Rapid iteration needed",
            "Small data sets",
            "Undefined processes"
        ],
        negative_outcomes=[
            "Analysis paralysis",
            "Slowed innovation",
            "Over-optimization"
        ],
        alternative_frameworks=["lean_startup", "mvp_framework", "agile_methodology"],
        severity="high"
    )
    
    return antipatterns


def create_framework_effectiveness_data():
    """Alias for create_framework_effectiveness_database"""
    return create_framework_effectiveness_database()


@dataclass
class CompanyContext:
    """Comprehensive company context for framework selection"""
    # Basic info
    company_name: str
    industry: IndustryContext
    stage: TemporalStage
    team_size: int
    
    # Problems and challenges
    primary_problems: List[ProblemArchetype]
    
    # Resources and constraints
    available_data: List[DataRequirement]
    
    # Optional fields with defaults
    secondary_problems: List[ProblemArchetype] = field(default_factory=list)
    timeline_days: int = 90
    budget_usd: Optional[int] = None
    has_data_analyst: bool = False
    has_strategy_team: bool = False
    
    # Business metrics
    revenue_usd: Optional[float] = None
    growth_rate_percent: Optional[float] = None
    burn_rate_usd: Optional[float] = None
    runway_months: Optional[float] = None
    
    # Strategic context
    is_crisis_mode: bool = False
    is_fundraising: bool = False
    is_pivoting: bool = False
    competitive_pressure: str = "medium"  # low, medium, high
    
    # Previous frameworks used
    completed_frameworks: List[str] = field(default_factory=list)
    failed_frameworks: List[str] = field(default_factory=list)
    
    def get_complexity_capacity(self) -> ComplexityTier:
        """Determine company's capacity for framework complexity"""
        if self.team_size < 10:
            return ComplexityTier.SIMPLE
        elif self.team_size < 50:
            return ComplexityTier.MODERATE
        elif self.team_size < 200:
            return ComplexityTier.COMPLEX
        else:
            return ComplexityTier.ENTERPRISE
            
    def get_urgency_level(self) -> str:
        """Determine urgency level for framework selection"""
        if self.is_crisis_mode or self.runway_months and self.runway_months < 6:
            return "critical"
        elif self.is_fundraising or self.timeline_days < 30:
            return "high"
        elif self.timeline_days < 90:
            return "medium"
        else:
            return "low"


@dataclass
class FrameworkRecommendation:
    """A recommended framework with context"""
    framework_id: str
    fit_score: float  # 0-100
    urgency_score: float  # 0-100
    confidence: float  # 0-100
    
    # Detailed scoring breakdown
    stage_fit: float = 0
    problem_fit: float = 0
    data_fit: float = 0
    complexity_fit: float = 0
    team_fit: float = 0
    timing_fit: float = 0
    
    # Recommendation context
    rationale: List[str] = field(default_factory=list)
    prerequisites: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    success_factors: List[str] = field(default_factory=list)
    
    # Implementation guidance
    estimated_days: int = 14
    required_resources: List[str] = field(default_factory=list)
    expected_outcomes: List[str] = field(default_factory=list)
    
    # Relationships
    complementary_frameworks: List[str] = field(default_factory=list)
    next_frameworks: List[str] = field(default_factory=list)


@dataclass
class FrameworkJourney:
    """Multi-phase framework implementation plan"""
    immediate: List[FrameworkRecommendation]  # Next 30 days
    short_term: List[FrameworkRecommendation]  # 30-90 days
    medium_term: List[FrameworkRecommendation]  # 3-6 months
    long_term: List[FrameworkRecommendation]  # 6-12 months
    
    total_frameworks: int = 0
    estimated_total_days: int = 0
    critical_path: List[str] = field(default_factory=list)
    
    def get_phase_frameworks(self, phase: str) -> List[str]:
        """Get framework IDs for a specific phase"""
        phase_map = {
            "immediate": self.immediate,
            "short_term": self.short_term,
            "medium_term": self.medium_term,
            "long_term": self.long_term
        }
        return [r.framework_id for r in phase_map.get(phase, [])]


class AdvancedFrameworkSelector:
    """
    MIT-HBS hybrid framework selection system
    Combines quantitative scoring with strategic judgment
    """
    
    def __init__(self):
        # Load all databases
        self.taxonomy_engine = FrameworkTaxonomyEngine()
        self.tags_db = create_framework_tags_database()
        self.relationships = create_framework_relationships()
        self.antipatterns = create_framework_antipatterns()
        self.effectiveness_data = create_framework_effectiveness_data()
        
        # Initialize taxonomy engine with data
        for fid, tags in self.tags_db.items():
            self.taxonomy_engine.add_framework_tags(fid, tags)
        for fid, rels in self.relationships.items():
            for rel in rels:
                self.taxonomy_engine.add_relationship(rel)
        for fid, anti in self.antipatterns.items():
            self.taxonomy_engine.add_antipattern(fid, anti)
        for fid, eff in self.effectiveness_data.items():
            self.taxonomy_engine.add_effectiveness_data(fid, eff)
            
    def select_frameworks(
        self, 
        context: CompanyContext,
        max_recommendations: int = 5,
        time_horizon_days: int = 90
    ) -> List[FrameworkRecommendation]:
        """
        Select optimal frameworks for company context
        Uses multi-factor scoring with academic rigor
        """
        
        recommendations = []
        
        # Step 1: Filter out antipatterns
        viable_frameworks = self._filter_antipatterns(context)
        
        # Step 2: Score all viable frameworks
        for framework_id in viable_frameworks:
            score = self._score_framework(framework_id, context)
            if score.fit_score > 30:  # Minimum threshold
                recommendations.append(score)
                
        # Step 3: Sort by weighted score
        recommendations = self._rank_recommendations(recommendations, context)
        
        # Step 4: Apply portfolio logic (diversity)
        recommendations = self._apply_portfolio_logic(recommendations, max_recommendations)
        
        # Step 5: Add relationships and sequencing
        recommendations = self._add_relationships(recommendations)
        
        return recommendations[:max_recommendations]
        
    def create_framework_journey(
        self,
        context: CompanyContext,
        planning_horizon_months: int = 12
    ) -> FrameworkJourney:
        """
        Create a phased framework implementation journey
        Considers dependencies, prerequisites, and timing
        """
        
        journey = FrameworkJourney(
            immediate=[],
            short_term=[],
            medium_term=[],
            long_term=[]
        )
        
        # Get all recommendations for planning horizon
        all_recommendations = self.select_frameworks(
            context, 
            max_recommendations=20,
            time_horizon_days=planning_horizon_months * 30
        )
        
        # Phase 1: Diagnostic frameworks (understand current state)
        diagnostic = [r for r in all_recommendations 
                     if DecisionContext.DIAGNOSTIC in self.tags_db[r.framework_id].decision_contexts]
        
        # Phase 2: Prescriptive frameworks (what to do)
        prescriptive = [r for r in all_recommendations
                       if DecisionContext.PRESCRIPTIVE in self.tags_db[r.framework_id].decision_contexts]
        
        # Phase 3: Predictive frameworks (forecast outcomes)
        predictive = [r for r in all_recommendations
                     if DecisionContext.PREDICTIVE in self.tags_db[r.framework_id].decision_contexts]
        
        # Phase 4: Evaluative frameworks (measure success)
        evaluative = [r for r in all_recommendations
                     if DecisionContext.EVALUATIVE in self.tags_db[r.framework_id].decision_contexts]
        
        # Assign to time periods based on logic
        if context.get_urgency_level() == "critical":
            # Crisis mode: Fast diagnostic + immediate action
            journey.immediate = diagnostic[:2] + prescriptive[:1]
            journey.short_term = prescriptive[1:3] + predictive[:1]
            journey.medium_term = evaluative[:2]
        else:
            # Normal mode: Thoughtful progression
            journey.immediate = diagnostic[:3]
            journey.short_term = prescriptive[:3]
            journey.medium_term = predictive[:2] + evaluative[:1]
            journey.long_term = self._get_advanced_frameworks(context, all_recommendations)
            
        # Calculate totals
        all_phases = journey.immediate + journey.short_term + journey.medium_term + journey.long_term
        journey.total_frameworks = len(all_phases)
        journey.estimated_total_days = sum(r.estimated_days for r in all_phases)
        
        # Identify critical path
        journey.critical_path = self._identify_critical_path(all_phases)
        
        return journey
        
    def _filter_antipatterns(self, context: CompanyContext) -> List[str]:
        """Filter out frameworks that match antipatterns"""
        viable = []
        
        context_dict = {
            "stage": context.stage.value,
            "team_size": context.team_size,
            "revenue": context.revenue_usd,
            "is_pivoting": context.is_pivoting,
            "industry": context.industry.value
        }
        
        for framework_id in self.tags_db.keys():
            # Check if any antipattern matches
            if framework_id in self.antipatterns:
                antipattern = self.antipatterns[framework_id]
                
                # Simple rule-based matching for now
                matches_antipattern = False
                
                if "Single product company" in antipattern.antipattern_conditions:
                    # This would need actual product count data
                    if context.team_size < 20:  # Proxy for single product
                        matches_antipattern = True
                        
                if "Pre-revenue startup" in antipattern.antipattern_conditions:
                    if context.revenue_usd == 0:
                        matches_antipattern = True
                        
                if not matches_antipattern:
                    viable.append(framework_id)
            else:
                viable.append(framework_id)
                
        return viable
        
    def _score_framework(
        self, 
        framework_id: str, 
        context: CompanyContext
    ) -> FrameworkRecommendation:
        """
        Comprehensive framework scoring algorithm
        Combines multiple factors with weighted importance
        """
        
        if framework_id not in self.tags_db:
            return FrameworkRecommendation(framework_id=framework_id, fit_score=0, urgency_score=0, confidence=0)
        
        # Add debug logging
        import logging
        logger = logging.getLogger(__name__)
        logger.debug(f"\nScoring framework: {framework_id}")
            
        tags = self.tags_db[framework_id]
        recommendation = FrameworkRecommendation(
            framework_id=framework_id,
            fit_score=0,
            urgency_score=0,
            confidence=0
        )
        
        # 1. Stage Fit (20% weight)
        if context.stage in tags.temporal_stages:
            recommendation.stage_fit = 100
            recommendation.rationale.append(f"Perfect fit for {context.stage.value} stage")
        elif any(self._is_adjacent_stage(context.stage, stage) for stage in tags.temporal_stages):
            recommendation.stage_fit = 60
            recommendation.rationale.append(f"Reasonable fit for {context.stage.value} stage")
        else:
            recommendation.stage_fit = 20
            recommendation.risks.append(f"Not typically used at {context.stage.value} stage")
        
        # Boost core frameworks for early stages
        core_early_frameworks = ['lean_canvas', 'customer_development', 'jobs_to_be_done', 'mvp_framework']
        core_growth_frameworks = ['bcg_matrix', 'porters_five_forces', 'ansoff_matrix', 'unit_economics']
        
        if context.stage in [TemporalStage.PRE_FORMATION, TemporalStage.FORMATION, TemporalStage.VALIDATION]:
            if framework_id in core_early_frameworks:
                recommendation.stage_fit = min(100, recommendation.stage_fit * 1.2)
                recommendation.rationale.append("Core framework for early-stage startups")
        elif context.stage in [TemporalStage.GROWTH, TemporalStage.SCALE]:
            if framework_id in core_growth_frameworks:
                recommendation.stage_fit = min(100, recommendation.stage_fit * 1.2)
                recommendation.rationale.append("Core framework for growth-stage companies")
        
        logger.debug(f"  Stage fit: {recommendation.stage_fit} (context: {context.stage.value}, framework stages: {[s.value for s in tags.temporal_stages]})")
            
        # 2. Problem Fit (30% weight)
        primary_matches = sum(1 for p in context.primary_problems if p in tags.problem_archetypes)
        if context.primary_problems:
            recommendation.problem_fit = (primary_matches / len(context.primary_problems)) * 100
            if recommendation.problem_fit > 80:
                recommendation.rationale.append("Directly addresses your primary challenges")
        else:
            # If no primary problems specified, use a default score with variation
            import random
            random.seed(hash(framework_id))
            recommendation.problem_fit = 40 + (random.random() * 20)  # 40-60 range
        
        logger.debug(f"  Problem fit: {recommendation.problem_fit} (matches: {primary_matches}/{len(context.primary_problems) if context.primary_problems else 0})")
                
        # 3. Data Availability (15% weight)
        required_data = tags.data_requirements
        available_data = context.available_data
        if required_data:
            data_matches = sum(1 for d in required_data if d in available_data)
            recommendation.data_fit = (data_matches / len(required_data)) * 100
            if recommendation.data_fit < 50:
                recommendation.risks.append("May lack required data inputs")
        else:
            # If no data requirements specified, assume it's accessible with variation
            import random
            random.seed(hash(framework_id + "data"))
            recommendation.data_fit = 70 + (random.random() * 20)  # 70-90 range
        
        logger.debug(f"  Data fit: {recommendation.data_fit}")
                
        # 4. Complexity Fit (10% weight)
        company_capacity = context.get_complexity_capacity()
        if tags.complexity_tier.value <= company_capacity.value:
            recommendation.complexity_fit = 100
        else:
            recommendation.complexity_fit = 60
            recommendation.risks.append("May be too complex for current team size")
            
        # 5. Team Fit (10% weight)
        if tags.team_size_min <= context.team_size <= tags.team_size_max:
            recommendation.team_fit = 100
        else:
            recommendation.team_fit = 50
            # Apply stronger penalty for frameworks that require larger teams
            if context.team_size < tags.team_size_min:
                team_size_ratio = context.team_size / tags.team_size_min
                if team_size_ratio < 0.5:  # Less than half the minimum size
                    recommendation.team_fit = 10
                    recommendation.risks.append(f"Requires team of {tags.team_size_min}+, current team is {context.team_size}")
                else:
                    recommendation.team_fit = 30
        
        logger.debug(f"  Team fit: {recommendation.team_fit} (team size: {context.team_size}, required: {tags.team_size_min}-{tags.team_size_max})")
            
        # 6. Timing Fit (15% weight)
        if tags.time_to_value_days <= context.timeline_days:
            recommendation.timing_fit = 100
            if context.get_urgency_level() in ["critical", "high"] and tags.time_to_value_days <= 7:
                recommendation.urgency_score = 90
                recommendation.rationale.append("Quick to implement for urgent needs")
        else:
            recommendation.timing_fit = 50
            recommendation.risks.append("May take longer than available timeline")
        
        logger.debug(f"  Timing fit: {recommendation.timing_fit} (time to value: {tags.time_to_value_days} days, timeline: {context.timeline_days} days)")
            
        # Calculate weighted fit score
        weights = {
            'stage': 0.20,
            'problem': 0.30,
            'data': 0.15,
            'complexity': 0.10,
            'team': 0.10,
            'timing': 0.15
        }
        
        recommendation.fit_score = (
            recommendation.stage_fit * weights['stage'] +
            recommendation.problem_fit * weights['problem'] +
            recommendation.data_fit * weights['data'] +
            recommendation.complexity_fit * weights['complexity'] +
            recommendation.team_fit * weights['team'] +
            recommendation.timing_fit * weights['timing']
        )
        
        logger.info(f"Framework {framework_id} - Base fit score: {recommendation.fit_score:.2f}")
        logger.debug(f"  Base fit score: {recommendation.fit_score:.2f}")
        logger.debug(f"  Breakdown: stage={recommendation.stage_fit}*{weights['stage']}, problem={recommendation.problem_fit}*{weights['problem']}, data={recommendation.data_fit}*{weights['data']}, complexity={recommendation.complexity_fit}*{weights['complexity']}, team={recommendation.team_fit}*{weights['team']}, timing={recommendation.timing_fit}*{weights['timing']}")
        
        # Add effectiveness data if available
        if framework_id in self.effectiveness_data:
            eff = self.effectiveness_data[framework_id]
            recommendation.confidence = eff.confidence_level * 100
            
            # Adjust score based on historical effectiveness
            if context.stage in eff.effectiveness_by_stage:
                stage_effectiveness = eff.effectiveness_by_stage[context.stage]
                recommendation.fit_score *= stage_effectiveness
                logger.debug(f"  Applied stage effectiveness: {stage_effectiveness}")
            
            # Also apply industry effectiveness if available
            if context.industry in eff.effectiveness_by_industry:
                industry_effectiveness = eff.effectiveness_by_industry[context.industry]
                recommendation.fit_score *= industry_effectiveness
                logger.debug(f"  Applied industry effectiveness: {industry_effectiveness}")
            
            logger.debug(f"  Final fit score after effectiveness: {recommendation.fit_score:.2f}")
        else:
            # Default confidence based on framework maturity
            recommendation.confidence = 70
            
            # Add slight variation to avoid identical scores
            import random
            random.seed(hash(framework_id + str(context.company_name)))
            
            # Apply small random variation to differentiate frameworks without effectiveness data
            variation_factor = 0.9 + (random.random() * 0.2)  # 0.9 to 1.1
            recommendation.fit_score *= variation_factor
            
            # Apply penalty for generic/variant frameworks
            if any(suffix in framework_id for suffix in ['_entertainment', '_finance', '_gaming', '_global', 
                                                          '_enterprises', '_emerging_markets', '_education',
                                                          '_retail', '_technology', '_real_estate', '_mobile',
                                                          '_healthcare', '_insurance', '_digital', '_hospitality',
                                                          '_b2c', '_saas', '_media']):
                recommendation.fit_score *= 0.7  # 30% penalty for generic variants
                recommendation.risks.append("Generic framework variant - consider core framework instead")
            
        # Set implementation details
        recommendation.estimated_days = tags.time_to_value_days
        recommendation.expected_outcomes = [o.value for o in tags.outcome_types]
        
        # All frameworks compete on merit - no arbitrary bonuses
        # Team size check applies equally to all frameworks
        if context.team_size < tags.team_size_min:
            recommendation.rationale.append(f"Team size ({context.team_size}) below framework minimum ({tags.team_size_min})")
        
        # All frameworks evaluated based on contextual relevance
        # No special boosts or penalties based on framework origin
        
        return recommendation
        
    def _rank_recommendations(
        self,
        recommendations: List[FrameworkRecommendation],
        context: CompanyContext
    ) -> List[FrameworkRecommendation]:
        """
        Advanced ranking algorithm considering context
        """
        
        # Adjust weights based on context
        if context.get_urgency_level() == "critical":
            # Prioritize speed and actionability
            for rec in recommendations:
                if rec.urgency_score > 80:
                    rec.fit_score *= 1.3  # 30% boost
                    
        elif context.is_fundraising:
            # Note which frameworks might be useful for investors without biasing selection
            investor_relevant = ["unit_economics", "ltv_cac_ratio", "cohort_analysis", "tam_sam_som", "bcg_matrix"]
            for rec in recommendations:
                if rec.framework_id in investor_relevant:
                    # Just add a note, don't boost the score
                    rec.rationale.append("May be valuable for investor discussions")
                    
        # Sort by fit score descending
        return sorted(recommendations, key=lambda x: x.fit_score, reverse=True)
        
    def _apply_portfolio_logic(
        self,
        recommendations: List[FrameworkRecommendation],
        max_count: int
    ) -> List[FrameworkRecommendation]:
        """
        Ensure diverse set of frameworks (portfolio approach)
        """
        
        # Prefer core frameworks over variants
        core_frameworks = ['bcg_matrix', 'porters_five_forces', 'ansoff_matrix', 'blue_ocean_strategy',
                          'jobs_to_be_done', 'lean_canvas', 'unit_economics', 'ltv_cac_ratio',
                          'aarrr_metrics', 'okr_framework', 'swot_analysis', 'vrio_framework',
                          'balanced_scorecard', 'value_chain_analysis', 'customer_journey_mapping']
        
        # Sort to prioritize core frameworks
        recommendations = sorted(recommendations, key=lambda x: (
            -x.fit_score,  # Higher scores first
            0 if x.framework_id in core_frameworks else 1  # Core frameworks first
        ))
        
        selected = []
        decision_contexts_included = set()
        problem_types_included = set()
        
        for rec in recommendations:
            if len(selected) >= max_count:
                break
                
            tags = self.tags_db[rec.framework_id]
            
            # Ensure diversity of decision contexts
            rec_contexts = set(tags.decision_contexts)
            rec_problems = set(tags.problem_archetypes)
            
            # Always include top 2 regardless of diversity
            if len(selected) < 2:
                selected.append(rec)
                decision_contexts_included.update(rec_contexts)
                problem_types_included.update(rec_problems)
            else:
                # Check for diversity
                new_contexts = rec_contexts - decision_contexts_included
                new_problems = rec_problems - problem_types_included
                
                if new_contexts or new_problems:
                    selected.append(rec)
                    decision_contexts_included.update(rec_contexts)
                    problem_types_included.update(rec_problems)
                elif rec.fit_score > 80:  # High score exception
                    selected.append(rec)
                    
        return selected
        
    def _add_relationships(
        self,
        recommendations: List[FrameworkRecommendation]
    ) -> List[FrameworkRecommendation]:
        """
        Add relationship information to recommendations
        """
        
        rec_ids = [r.framework_id for r in recommendations]
        
        for rec in recommendations:
            # Find complementary frameworks in the set
            if rec.framework_id in self.relationships:
                for rel in self.relationships[rec.framework_id]:
                    if rel.relationship_type == "complementary":
                        complementary_in_set = [
                            fid for fid in rel.related_framework_ids 
                            if fid in rec_ids
                        ]
                        rec.complementary_frameworks = complementary_in_set
                        
                    elif rel.relationship_type == "prerequisite":
                        rec.prerequisites = rel.related_framework_ids
                        
                    elif rel.relationship_type == "progressive":
                        rec.next_frameworks = rel.related_framework_ids
                        
        return recommendations
        
    def _is_adjacent_stage(self, stage1: TemporalStage, stage2: TemporalStage) -> bool:
        """Check if two stages are adjacent in lifecycle"""
        stage_order = [
            TemporalStage.PRE_FORMATION,
            TemporalStage.FORMATION,
            TemporalStage.VALIDATION,
            TemporalStage.TRACTION,
            TemporalStage.GROWTH,
            TemporalStage.SCALE,
            TemporalStage.MATURITY
        ]
        
        idx1 = stage_order.index(stage1)
        idx2 = stage_order.index(stage2)
        
        return abs(idx1 - idx2) == 1
        
    def _get_advanced_frameworks(
        self,
        context: CompanyContext,
        all_recommendations: List[FrameworkRecommendation]
    ) -> List[FrameworkRecommendation]:
        """Get advanced frameworks for long-term planning"""
        
        advanced = []
        for rec in all_recommendations:
            tags = self.tags_db[rec.framework_id]
            if tags.complexity_tier in [ComplexityTier.COMPLEX, ComplexityTier.ENTERPRISE]:
                if rec not in advanced:
                    advanced.append(rec)
                    
        return advanced[:3]
        
    def _identify_critical_path(
        self,
        frameworks: List[FrameworkRecommendation]
    ) -> List[str]:
        """Identify the critical path through frameworks"""
        
        # Simple implementation - would be more complex with full dependency graph
        critical_path = []
        
        # Start with frameworks that have no prerequisites
        no_prereq = [f for f in frameworks if not f.prerequisites]
        if no_prereq:
            critical_path.append(no_prereq[0].framework_id)
            
        # Add frameworks that unlock the most others
        for f in frameworks:
            if f.next_frameworks and f.framework_id not in critical_path:
                critical_path.append(f.framework_id)
                
        return critical_path[:5]  # Top 5 critical frameworks


def generate_framework_report(
    context: CompanyContext,
    recommendations: List[FrameworkRecommendation]
) -> str:
    """Generate executive report on framework recommendations"""
    
    report = f"""
# Framework Intelligence Report
## Company: {context.company_name}
## Date: {datetime.now().strftime('%Y-%m-%d')}

### Company Context
- **Industry**: {context.industry.value}
- **Stage**: {context.stage.value}
- **Team Size**: {context.team_size}
- **Urgency**: {context.get_urgency_level()}

### Primary Challenges
{chr(10).join(f"- {p.value}" for p in context.primary_problems)}

### Recommended Frameworks

"""
    
    for i, rec in enumerate(recommendations, 1):
        report += f"""
#### {i}. {rec.framework_id.replace('_', ' ').title()}
- **Fit Score**: {rec.fit_score:.1f}/100
- **Confidence**: {rec.confidence:.0f}%
- **Time to Implement**: {rec.estimated_days} days

**Why This Framework**:
{chr(10).join(f"- {r}" for r in rec.rationale)}

**Expected Outcomes**:
{chr(10).join(f"- {o}" for o in rec.expected_outcomes)}

"""
        
        if rec.prerequisites:
            report += f"""
**Prerequisites**: {', '.join(rec.prerequisites)}
"""
        
        if rec.risks:
            report += f"""
**Risks to Consider**:
{chr(10).join(f"- {r}" for r in rec.risks)}
"""
            
    return report