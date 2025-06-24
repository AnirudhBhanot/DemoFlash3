# Prompt Engineering Bias Fixes Summary

## Overview
Fixed prompt engineering biases across the FLASH platform to ensure framework selection is based on contextual relevance rather than tradition or perceived prestige.

## Files Updated

### 1. `/Users/sf/Desktop/FLASH/mckinsey_grade_analyzer.py`
- Renamed class from `McKinseyGradeAnalyzer` to `StrategicAnalysisEngine`
- Changed system prompt from "McKinsey Senior Partner" to "strategic analysis expert"
- Updated prompts to emphasize context-specific selection of analytical tools
- Changed language from "classic framework" to "framework specifically adapted for your industry context"

### 2. `/Users/sf/Desktop/FLASH/intelligent_framework_selector.py`
- Changed "Successfully used by similar companies" to "Successfully applied in similar contexts"
- Updated "Classic framework adapted for your specific industry" to "Framework specifically adapted for your industry context"

### 3. `/Users/sf/Desktop/FLASH/framework_intelligence/framework_selection_engine.py`
- Removed all arbitrary scoring bonuses for "classic" frameworks
- Eliminated the weighted multipliers that favored traditional frameworks (1.05-1.1x boost)
- Changed approach to evaluate all frameworks based purely on contextual relevance
- Removed special boosts and penalties based on framework origin

### 4. `/Users/sf/Desktop/FLASH/api_michelin_strategic.py`
- Changed system prompt from "McKinsey senior consultant" to "strategic analysis expert"
- Added emphasis on "context-relevant insights" in the prompt

### 5. `/Users/sf/Desktop/FLASH/enhanced_phase3_analyzer.py`
- Updated module description to use "research-backed methods" instead of "McKinsey-grade"
- Changed class imports and references from `McKinseyGradeAnalyzer` to `StrategicAnalysisEngine`
- Updated prompts to request "comprehensive" analysis using "context-appropriate methods"

### 6. `/Users/sf/Desktop/FLASH/strategic_context_engine.py`
- Changed module description from "McKinsey-grade analysis" to "comprehensive strategic analysis"
- Maintained emphasis on "research-backed framework intelligence"

### 7. `/Users/sf/Desktop/FLASH/analyze_phd_enhancements_and_interconnections.py`
- Renamed "McKinsey_Analysis" to "Strategic_Analysis"
- Changed description from "McKinsey-Grade Strategic Analysis" to "Research-Based Strategic Analysis"
- Emphasized "deep research validation" instead of simulating specific firm experience

## Key Changes Made

1. **Neutral Language**: Replaced all references to specific consulting firms with neutral terms like "strategic analysis expert" or "business strategy specialist"

2. **Context-Based Selection**: Emphasized selection based on relevance to specific situation rather than framework tradition or prestige

3. **Merit-Based Evaluation**: Removed all arbitrary scoring bonuses for "classic" or "traditional" frameworks - all frameworks now compete on merit

4. **Innovation Focus**: Language now encourages selection of the most relevant analytical tools regardless of their origin or age

5. **Research Emphasis**: Shifted focus from firm prestige to research validation and empirical evidence

## Impact

These changes ensure that:
- Framework selection is unbiased and based on contextual fit
- Innovation and newer frameworks have equal opportunity for selection
- The system values relevance over tradition
- Users receive recommendations based on what works best for their specific situation, not based on historical preferences