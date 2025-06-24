#!/usr/bin/env python3
"""
PhD Enhancement Utilities - Shared utilities for integrating PhD enhancements
into various Michelin analysis implementations
"""

import json
import logging
import os
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)


class PhDEnhancementProvider:
    """Provides PhD enhancement data for frameworks"""
    
    def __init__(self):
        self.phd_enhancements = self._load_phd_enhancements()
        self.framework_synergies = self._load_framework_synergies()
        
    def _load_phd_enhancements(self) -> Dict[str, Any]:
        """Load PhD enhancement database"""
        try:
            phd_path = os.path.join(os.path.dirname(__file__), 'phd_enhancement_database.json')
            with open(phd_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning("PhD enhancement database not found")
            return {}
        except Exception as e:
            logger.error(f"Error loading PhD enhancements: {e}")
            return {}
    
    def _load_framework_synergies(self) -> Dict[str, Any]:
        """Load framework synergy data"""
        try:
            synergy_path = os.path.join(os.path.dirname(__file__), 'framework_synergies.json')
            with open(synergy_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning("Framework synergies data not found")
            return {"complementary_frameworks": {}, "synergy_scores": {}}
        except Exception as e:
            logger.error(f"Error loading framework synergies: {e}")
            return {"complementary_frameworks": {}, "synergy_scores": {}}
    
    def get_framework_enhancement(self, framework_id: str) -> Optional[Dict[str, Any]]:
        """Get PhD enhancement for a specific framework"""
        return self.phd_enhancements.get(framework_id)
    
    def get_theoretical_foundation(self, framework_id: str) -> Optional[str]:
        """Get theoretical foundation for a framework"""
        enhancement = self.get_framework_enhancement(framework_id)
        if enhancement and 'phd_level_features' in enhancement:
            theory = enhancement['phd_level_features'].get('theoretical_foundation', {})
            return theory.get('primary_theory')
        return None
    
    def get_research_methods(self, framework_id: str) -> List[str]:
        """Get research methods for a framework"""
        enhancement = self.get_framework_enhancement(framework_id)
        if enhancement and 'phd_level_features' in enhancement:
            methods = enhancement['phd_level_features'].get('research_methods', {})
            return methods.get('primary_methodology', [])
        return []
    
    def get_ml_augmentations(self, framework_id: str) -> Dict[str, Any]:
        """Get ML/AI augmentations for a framework"""
        enhancement = self.get_framework_enhancement(framework_id)
        if enhancement and 'phd_level_features' in enhancement:
            return enhancement['phd_level_features'].get('advanced_applications', {}).get(
                'machine_learning_integration', {}
            )
        return {}
    
    def get_synergistic_frameworks(self, framework_id: str) -> List[str]:
        """Get synergistic frameworks"""
        enhancement = self.get_framework_enhancement(framework_id)
        if enhancement and 'phd_level_features' in enhancement:
            return enhancement['phd_level_features'].get('interconnection_intelligence', {}).get(
                'synergistic_frameworks', []
            )
        return self.framework_synergies.get('complementary_frameworks', {}).get(framework_id, [])
    
    def enhance_analysis_prompt(self, prompt: str, framework_id: str) -> str:
        """Enhance analysis prompt with PhD insights"""
        theory = self.get_theoretical_foundation(framework_id)
        methods = self.get_research_methods(framework_id)
        
        if theory or methods:
            enhancement = f"\n\nACADEMIC CONTEXT:\n"
            if theory:
                enhancement += f"- Theoretical Foundation: {theory}\n"
            if methods:
                enhancement += f"- Research Methods: {', '.join(methods)}\n"
            enhancement += "\nPlease incorporate these academic perspectives where relevant.\n"
            return prompt + enhancement
        
        return prompt
    
    def add_implementation_sophistication(
        self, 
        implementation_plan: Dict[str, Any], 
        framework_id: str
    ) -> Dict[str, Any]:
        """Add PhD-level sophistication to implementation plans"""
        enhancement = self.get_framework_enhancement(framework_id)
        
        if enhancement and 'phd_level_features' in enhancement:
            phd_features = enhancement['phd_level_features']
            
            # Add research validation approach
            if 'research_methods' in phd_features:
                implementation_plan['research_validation'] = {
                    'methodology': phd_features['research_methods'].get('primary_methodology', []),
                    'data_collection': phd_features['research_methods'].get('data_collection', []),
                    'validation_metrics': phd_features['research_methods'].get('validation_metrics', [])
                }
            
            # Add quantitative enhancements
            if 'quantitative_enhancements' in phd_features:
                implementation_plan['quantitative_methods'] = {
                    'statistical_techniques': phd_features['quantitative_enhancements'].get(
                        'statistical_techniques', []
                    ),
                    'optimization_approaches': phd_features['quantitative_enhancements'].get(
                        'optimization_approaches', []
                    )
                }
            
            # Add time to mastery
            if 'implementation_sophistication' in phd_features:
                implementation_plan['time_to_mastery'] = phd_features[
                    'implementation_sophistication'
                ].get('time_to_mastery', '2-4 weeks')
        
        return implementation_plan
    
    def get_framework_interconnections(
        self, 
        primary_framework: str, 
        all_frameworks: List[str]
    ) -> Dict[str, Any]:
        """Get interconnections between frameworks"""
        interconnections = {
            'synergistic': [],
            'complementary': [],
            'sequential': [],
            'conflicting': []
        }
        
        enhancement = self.get_framework_enhancement(primary_framework)
        if enhancement and 'phd_level_features' in enhancement:
            intelligence = enhancement['phd_level_features'].get('interconnection_intelligence', {})
            
            # Find synergistic frameworks that are in our list
            for synergistic in intelligence.get('synergistic_frameworks', []):
                if synergistic in all_frameworks:
                    interconnections['synergistic'].append(synergistic)
            
            # Find conflicting approaches
            interconnections['conflicting'] = intelligence.get('conflicting_approaches', [])
        
        # Add from synergy database
        complementary = self.framework_synergies.get('complementary_frameworks', {}).get(
            primary_framework, []
        )
        for comp in complementary:
            if comp in all_frameworks and comp not in interconnections['synergistic']:
                interconnections['complementary'].append(comp)
        
        return interconnections


# Singleton instance
phd_provider = PhDEnhancementProvider()