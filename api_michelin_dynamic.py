#!/usr/bin/env python3
"""
Dynamic Michelin Analysis - Truly flexible framework selection
No hardcoded BCG/Porter's/SWOT requirements
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging

from enhanced_framework_selector import EnhancedFrameworkSelector
from strategic_context_engine import StrategicContextEngine
from mckinsey_grade_analyzer import StrategicAnalysisEngine
from intelligent_framework_selector import CustomizedFramework
from framework_intelligence.framework_database import get_framework_by_id

logger = logging.getLogger(__name__)
dynamic_router = APIRouter(prefix="/api/michelin/dynamic")

# Flexible data models
class DynamicPhase1Analysis(BaseModel):
    """Dynamic Phase 1 that accepts any frameworks"""
    executive_summary: str
    frameworks_analysis: List[Dict[str, Any]]  # List of framework analyses
    current_position_narrative: str
    context: Dict[str, Any]

class DynamicPhase1Response(BaseModel):
    startup_name: str
    analysis_date: str
    phase1: DynamicPhase1Analysis
    frameworks_selected: List[str]

class DynamicMichelinEngine:
    """Engine for truly dynamic framework analysis"""
    
    def __init__(self):
        self.context_engine = StrategicContextEngine()
        self.framework_selector = EnhancedFrameworkSelector()
        self.analyzer = StrategicAnalysisEngine()
        
    async def analyze_phase1_dynamic(
        self, 
        startup_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Phase 1 with dynamic framework selection"""
        
        logger.info(f"Starting dynamic Phase 1 for {startup_data.get('startup_name')}")
        
        # Build context
        context = await self.context_engine.build_company_context(startup_data)
        
        # Select frameworks based on context
        result = await self.framework_selector.select_frameworks_for_startup(
            startup_data, max_frameworks=3
        )
        
        if result is None:
            raise ValueError("Framework selection returned None")
            
        if not result.get("success", False):
            raise ValueError(f"Framework selection failed: {result.get('error', 'Unknown error')}")
            
        frameworks = result.get("frameworks", [])
        if not frameworks:
            raise ValueError("No frameworks were selected")
            
        logger.info(f"Selected {len(frameworks)} frameworks dynamically")
        logger.info(f"Framework types: {[type(fw).__name__ for fw in frameworks]}")
        if frameworks:
            logger.info(f"First framework keys: {list(frameworks[0].keys()) if isinstance(frameworks[0], dict) else 'Not a dict'}")
        
        # Analyze each framework
        frameworks_analysis = []
        for idx, fw in enumerate(frameworks):
            try:
                logger.info(f"Processing framework {idx}: {fw.get('name') if isinstance(fw, dict) else 'Not a dict'}")
                # Skip if framework is None
                if fw is None:
                    logger.warning("Skipping None framework")
                    continue
                    
                # Handle both dict and CustomizedFramework objects
                if isinstance(fw, dict):
                    # Get the base framework
                    base_fw = get_framework_by_id(fw["id"])
                    if not base_fw:
                        logger.warning(f"Framework {fw['id']} not found in database")
                        continue
                        
                    customized_fw = CustomizedFramework(
                        base_framework=base_fw,
                        customizations=fw.get("customizations", {}),
                        industry_variant=fw.get("industry_variant", "general"),
                        specific_metrics=fw.get("specific_metrics", []),
                        thresholds=fw.get("thresholds", {}),
                        implementation_guide=fw.get("implementation_guide", {}),
                        expected_insights=fw.get("expected_insights", []),
                        phd_enhancement=fw.get("phd_enhancement"),
                        synergistic_frameworks=fw.get("synergistic_frameworks", []),
                        prerequisites=fw.get("prerequisites", []),
                        conflicts=fw.get("conflicts", []),
                        time_to_mastery=fw.get("time_to_mastery", "2-4 weeks")
                    )
                    
                    # For dict, extract fit_score and rationale
                    fit_score = fw.get("fit_score", 0)
                    rationale = fw.get("rationale", [])
                else:
                    customized_fw = fw
                    # For CustomizedFramework, get from academic insights
                    academic_insights = customized_fw.customizations.get("academic_insights", {})
                    fit_score = academic_insights.get("fit_score", 0)
                    rationale = academic_insights.get("rationale", [])
                    
                analysis = await self.analyzer.generate_framework_analysis(
                    customized_fw, context
                )
                
                frameworks_analysis.append({
                    "framework_name": customized_fw.base_framework.name,
                    "framework_id": customized_fw.base_framework.id,
                    "category": customized_fw.base_framework.category.value if hasattr(customized_fw.base_framework.category, 'value') else customized_fw.base_framework.category,
                    "analysis": analysis,
                    "fit_score": fit_score,
                    "rationale": rationale
                })
            except Exception as e:
                logger.error(f"Error analyzing framework: {e}")
                logger.error(f"Framework data: {fw}")
                continue
            
        # Generate executive summary
        executive_summary = await self._generate_dynamic_summary(
            context, frameworks_analysis
        )
        
        # Generate position narrative
        position_narrative = await self._generate_dynamic_narrative(
            context, frameworks_analysis
        )
        
        return {
            "executive_summary": executive_summary,
            "frameworks_analysis": frameworks_analysis,
            "current_position_narrative": position_narrative,
            "context": {
                "industry": context.industry,
                "stage": context.stage,
                "key_challenges": context.key_challenges[:3],
                "strategic_inflection": context.current_inflection.value
            }
        }
        
    async def _generate_dynamic_summary(
        self, 
        context, 
        frameworks_analysis: List[Dict]
    ) -> str:
        """Generate summary based on actual frameworks used"""
        
        framework_names = [f["framework_name"] for f in frameworks_analysis]
        
        summary = f"{context.company_name} is at a critical juncture. "
        summary += f"Our analysis using {', '.join(framework_names)} reveals "
        summary += f"key insights about the company's position in the {context.industry} market. "
        
        # Add key insights from each framework
        for fw in frameworks_analysis[:2]:  # Top 2 insights
            if fw["analysis"].get("key_insight"):
                summary += f"{fw['analysis']['key_insight']} "
                
        return summary
        
    async def _generate_dynamic_narrative(
        self, 
        context, 
        frameworks_analysis: List[Dict]
    ) -> str:
        """Generate narrative based on actual frameworks used"""
        
        narrative = f"Based on our comprehensive analysis using "
        narrative += f"{len(frameworks_analysis)} carefully selected frameworks, "
        narrative += f"{context.company_name} is positioned as a {context.stage} company "
        narrative += f"facing {context.current_inflection.value}. "
        
        # Add framework-specific insights
        for fw in frameworks_analysis:
            narrative += f"\n\nThe {fw['framework_name']} analysis shows: "
            if fw["analysis"].get("position"):
                narrative += fw["analysis"]["position"]
            elif fw["analysis"].get("strategic_implication"):
                narrative += fw["analysis"]["strategic_implication"]
                
        return narrative

# Singleton instance
dynamic_engine = DynamicMichelinEngine()

@dynamic_router.post("/analyze/phase1", response_model=DynamicPhase1Response)
async def analyze_phase1_dynamic(
    startup_data: Dict[str, Any],
    background_tasks: BackgroundTasks
):
    """Dynamic Phase 1 endpoint - no hardcoded frameworks"""
    
    try:
        phase1_data = await dynamic_engine.analyze_phase1_dynamic(startup_data)
        
        frameworks_selected = [
            f["framework_name"] for f in phase1_data["frameworks_analysis"]
        ]
        
        return DynamicPhase1Response(
            startup_name=startup_data.get("startup_name", "Unknown"),
            analysis_date=datetime.now().isoformat(),
            phase1=DynamicPhase1Analysis(**phase1_data),
            frameworks_selected=frameworks_selected
        )
        
    except Exception as e:
        logger.error(f"Dynamic Phase 1 failed: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )

def include_dynamic_michelin_routes(app):
    """Include dynamic Michelin routes in FastAPI app"""
    app.include_router(dynamic_router)
    logger.info("Dynamic Michelin Analysis endpoints enabled - Truly flexible framework selection")