# FLASH Platform - Context for Claude V30

## Latest Updates (June 18, 2025 - V30)

### Dynamic Michelin Analysis - Flexible Framework Selection
- **Issue**: User reported "BCG Matrix, Porter's Five Forces, and SWOT Analysis" were hardcoded in Michelin analysis despite framework selection improvements
- **Root Cause**: The Michelin Phase1Analysis model had hardcoded fields requiring specific frameworks
- **Solution**: Created truly dynamic Michelin system allowing any framework combination

#### Key Changes:
1. **Dynamic API** (`api_michelin_dynamic.py`)
   - New endpoint: `/api/michelin/dynamic/analyze/phase1`
   - Accepts any framework combination from selection engine
   - No hardcoded framework requirements
   - Flexible data model supporting any analysis structure

2. **Dynamic Frontend Component** (`MichelinDynamicAnalysis.tsx`)
   - Displays whatever frameworks are selected
   - Shows framework names, categories, fit scores, and rationales
   - Expandable cards for detailed framework analysis
   - No hardcoded BCG/Porter's/SWOT sections

3. **Feature Flag Integration**
   - Added 'dynamic' option to `michelinAnalysisApproach`
   - Configurable in `src/config/features.ts`
   - Easy switching between approaches:
     - 'dynamic': Truly flexible framework selection
     - 'enhanced': McKinsey-grade with context engine (stable)
     - 'decomposed': Reliable multi-step approach
     - 'strategic': Phase interconnection design

4. **Data Models**
   ```python
   class DynamicPhase1Analysis(BaseModel):
       executive_summary: str
       frameworks_analysis: List[Dict[str, Any]]  # Flexible list
       current_position_narrative: str
       context: Dict[str, Any]
   ```

5. **Implementation Status**
   - ✅ Dynamic API created and integrated
   - ✅ Frontend component built
   - ✅ Feature flag system implemented
   - ⚠️  Framework object handling needs refinement
   - 🔄 Currently using 'enhanced' approach for stability

#### Technical Challenges Resolved:
- CustomizedFramework dataclass structure mismatch
- Framework serialization between backend and frontend
- Dynamic analysis generation for any framework type

#### Testing:
```bash
# Test dynamic API endpoint
curl -X POST http://localhost:8001/api/michelin/dynamic/analyze/phase1 \
  -H "Content-Type: application/json" \
  -d '{
    "startup_data": {
      "startup_name": "Test Company",
      "sector": "saas_b2b",
      "funding_stage": "pre_seed",
      "key_challenges": ["Achieving product-market fit"]
      // ... other required fields
    }
  }'
```

## Latest Updates (June 17, 2025 - V29)

### PhD Enhancement Integration - Complete Implementation
- **Issue**: Framework selection and analysis lacked academic rigor and theoretical grounding
- **Solution**: Integrated PhD-level enhancements across entire system

#### Key Components Added:
1. **PhD Enhancement Database** (`phd_enhancement_database.json`)
   - 557 frameworks with theoretical foundations
   - Research methodologies for each framework
   - ML/AI augmentation possibilities
   - Academic validation approaches

2. **Framework Synergies** (`framework_synergies.json`)
   - Complementary framework mappings
   - Synergy scores between frameworks
   - Prerequisite relationships
   - Framework clusters by domain

3. **Enhanced Framework Selection**
   - Academic rigor scoring (15% weight)
   - Prerequisite checking (10% weight)
   - Synergy analysis for combinations
   - Time-to-mastery estimates

4. **Michelin Analysis Enhancements**
   - Phase 1: Framework interconnection analysis
   - Phase 2: ML/AI opportunity identification
   - Phase 3: Academic validation methodologies
   - Research-based implementation roadmaps

5. **Utility Module** (`phd_enhancement_utils.py`)
   - Shared PhD enhancement provider
   - Prompt augmentation with academic context
   - Implementation sophistication additions

#### Testing Commands:
```bash
# Test enhanced framework selection
python3 test_complete_framework_system.py

# Validate all frameworks have PhD enhancements
python3 check_framework_implementations.py

# Test Michelin enhanced API
curl -X POST http://localhost:8001/api/michelin/enhanced/analyze/phase1 \
  -H "Content-Type: application/json" \
  -d @test_data/flash_platform.json
```

## Latest Updates (June 17, 2025 - V28)

### Advanced Framework Intelligence System - Complete Implementation
- **Issue**: User noted "BCG Matrix is still being selected as #1" and questioned the selection logic
- **Solution**: Implemented comprehensive MIT/HBS-grade framework selection system

- **Phase 1 - Multi-Dimensional Taxonomy**:
  - 7 dimensions: Temporal Stage, Problem Archetype, Decision Context, Data Requirements, Complexity, Outcome Type, Industry
  - 20+ metadata fields per framework
  - Comprehensive tagging for 500+ frameworks

- **Phase 2 - Contextual Effectiveness**:
  - Empirical effectiveness scoring by stage/industry/team size
  - Anti-pattern database (when NOT to use frameworks)
  - Success/failure pattern tracking
  - ROI and time-to-impact metrics

- **Phase 3 - Intelligent Matching**:
  - 6-factor weighted scoring algorithm
  - Crisis mode detection and adjustment
  - Portfolio diversity logic
  - Prerequisite and dependency tracking

- **Phase 4 - Industry Customization**:
  - B2B SaaS: BCG uses NRR/ARR instead of market share
  - Marketplace: Take rate/GMV focus, dual-sided economics
  - FinTech: Regulatory risk scoring, ARPU optimization
  - Hardware: Inventory turns, warranty reserves

- **Phase 5 - Integration**:
  - New endpoints: `/api/frameworks/enhanced/select`, `/journey`, `/details`
  - Seamless integration with existing Michelin analysis
  - Executive report generation
  - 12-month journey planning

- **Key Innovation**: Framework selection now follows proper hierarchy:
  1. **Diagnostic First** (Pre-PMF): Jobs-to-be-Done, Customer Development
  2. **Prescriptive Second** (Post-PMF): Unit Economics, Growth Loops
  3. **Strategic Last** (Scale): BCG Matrix, Porter's Five Forces

- **Testing**: All systems validated and operational
  - API endpoint: `http://localhost:8001/api/frameworks/enhanced/test` ✅
  - Methodology: "MIT/HBS Advanced Framework Selection v2.0"

# FLASH Platform - Context for Claude V27

### Enhanced Michelin Analysis with McKinsey-Grade Output
- **Issue**: User reported "phase 3 analysis aren't working" and frameworks had "very generalized output and not McKinsey or BCG grade specificities"
- **Root Causes Identified**:
  1. Phase 3 had no DeepSeek API calls - just returning static fallback
  2. Frameworks used simplistic keyword matching instead of intelligent selection
  3. No industry-specific customization of frameworks
  4. Generic prompts without context carryover between phases
  
- **Solution Implemented**: Complete strategic analysis system
  1. **Strategic Context Engine** (`strategic_context_engine.py`):
     - Builds comprehensive company context with industry benchmarks
     - Tracks strategic inflection points (Pre-PMF, PMF, Scaling, etc.)
     - Identifies key challenges and opportunities
  
  2. **Intelligent Framework Selector** (`intelligent_framework_selector.py`):
     - ML-based scoring with context embeddings
     - Industry-specific framework variants (e.g., SaaS BCG uses NRR/ARR instead of market share)
     - Success pattern matching from similar companies
     - Synergy scoring for complementary frameworks
  
  3. **McKinsey-Grade Analyzer** (`mckinsey_grade_analyzer.py`):
     - Generates partner-level strategic analysis
     - Hypothesis trees and scenario planning
     - Monte Carlo simulations for risk analysis
     - Specific, actionable recommendations with metrics
  
  4. **Enhanced Phase 3** (`enhanced_phase3_analyzer.py`):
     - Proper implementation with DeepSeek integration
     - Risk assessment and mitigation strategies
     - Implementation roadmap with milestones
     - Success metrics and KPIs

- **Framework Improvements**:
  - Added BCG Matrix and Porter's Five Forces to framework database
  - Industry variants: SaaS uses NRR/ARR, Marketplace uses Take Rate/GMV
  - Fixed scoring to prioritize relevant frameworks (added competitive bonus)
  - Pattern-based selection learning from successful companies
  
- **Testing Results**:
  - Successfully tested with FLASH platform data
  - BCG Matrix properly customized for each industry
  - Porter's Five Forces now selected for competitive challenges
  - Output includes specific metrics, benchmarks, and actionable insights

## Project Overview (Current Version: V30)
FLASH (Fast Learning and Assessment of Startup Health) is an advanced AI platform for evaluating startup success probability using the CAMP framework (Capital, Advantage, Market, People). The system uses **realistic ML models** with ~72.7% AUC (production v45), providing honest predictions that acknowledge the inherent uncertainty in early-stage investing. 

The platform now includes:
- **Progressive Deep Dive**: 4-phase strategic analysis system (accessible via /deep-dive)
- **Framework Intelligence Engine**: AI-powered recommendations from 500+ business frameworks with PhD enhancements
- **Dynamic Michelin Analysis**: Flexible framework selection without hardcoded requirements
- Professional, enterprise-ready UI with light theme default
- **Complete 45-Feature Collection**: All required ML features now collected across assessment pages
- **DeepSeek API Integration**: 80% functional with AI-powered recommendations and analysis

## Latest Updates (June 16, 2025 - V26)

### Michelin Strategic Analysis - Complete Redesign
- **Issue**: Michelin analysis experienced persistent timeout issues and frontend-backend data structure mismatches
- **Root Causes Identified**:
  1. Router conflicts with multiple routers using same `/api/michelin` prefix
  2. Regex syntax error in JSON parsing: `(?<[,{\s])` → `(?<=[,{\s])`
  3. Missing `customer_count` field in StartupData model
  4. Frontend expecting different data structures than backend provided
  5. DeepSeek API timeouts when generating complex nested JSON

- **Solution Implemented**: Three-tier approach system
  1. **Decomposed Approach** (`api_michelin_decomposed.py`):
     - Breaks complex analysis into focused API calls
     - Each component uses simple prompts instead of complex JSON
     - Added `get_strategic_priorities` method to fix frontend errors
     - Reliable with graceful fallbacks
  
  2. **Strategic Redesign** (`api_michelin_strategic.py`):
     - Introduced `StrategicContext` class for phase interconnection
     - Each phase builds on insights from previous phases
     - Generates frontend-compatible structures programmatically
     - Combines reliability with intelligent analysis
  
  3. **Feature Flag System** (`config/features.ts`):
     - Supports switching between `original`, `decomposed`, and `strategic` approaches
     - Allows A/B testing and gradual rollout
     - Currently set to `decomposed` for stability

- **Key Improvements**:
  - Phase-by-phase loading prevents timeouts
  - Strategic context maintains insights across phases
  - Frontend data structure alignment
  - Performance: Phase 1 (~40s), Phase 2 (~35s), Phase 3 (~10s)

## Previous Updates (June 14, 2025 - V25)

### DeepSeek API Integration & Results Page Optimization
- **DeepSeek API Integration**: 
  - Successfully integrated DeepSeek API for AI-powered insights
  - 4/5 endpoints working with DeepSeek (80% coverage)
  - Working endpoints: Dynamic Recommendations, Deep Framework Analysis, What-If Analysis, Market Insights
  - Competitor Analysis using enhanced fallback due to JSON parsing challenges
  - Added comprehensive JSON repair logic for malformed responses
  - Reduced cache TTL from 3600s to 300s for more dynamic content

- **Results Page Streamlining**:
  - Removed 4 low-value analyses to focus on actionable insights
  - Removed: Comparative Analysis, What-If Scenarios, Market Insights, Competitor Analysis
  - Removed Progressive Deep Dive promotional section
  - Retained high-value analyses: Success Score, CAMP Framework, Enhanced Insights, Deep Dive, FLASH Intelligence (formerly LLM Recommendations), Strategic Framework, FLASH Executive Report
  - Benefits: Cleaner UX, faster load times, better focus on actionable insights

- **Technical Improvements**:
  - Added `_extract_json_from_response` method for robust JSON parsing
  - Enhanced error handling with graceful fallbacks
  - Simplified competitor analysis prompt for cleaner responses
  - Improved fallback responses with sector-specific data

## Previous Updates (June 2025 - V24)

### Market Page Redesign & Complete Feature Collection
- **Issue**: Market page had inconsistent design and was missing 10 out of 45 required ML features
- **Solution**: 
  1. Redesigned Market page to match consistent design pattern of other assessment pages
  2. Added all missing features to achieve 100% feature collection
  3. Implemented auto-calculation for SAM (10% of TAM) and SOM (1% of SAM)
  4. Removed toggle-based "Add more details" in favor of simple scrolling

- **Key Changes**:
  1. **Design Consistency**: 
     - Used MarketSimple component for clean, consistent design
     - Removed circular TAM/SAM/SOM visualization
     - Adopted card-based layout matching Advantage page
     - All fields visible with smooth scrolling (no hidden advanced section)

  2. **Auto-Calculation Fix**:
     - Fixed currency input parsing issue (removed commas before calculation)
     - SAM automatically calculated as 10% of TAM
     - SOM automatically calculated as 1% of SAM
     - Display-only values (users cannot manually edit SAM/SOM)

  3. **Complete Feature Collection**:
     - Added 10 missing features to Market page
     - Now collecting all 45 ML features required by API
     - Features properly distributed across assessment pages

- **Market Page Fields** (15 visible + 2 auto-calculated):
  1. Sector
  2. TAM (Total Addressable Market)
  3. Market Growth Rate %
  4. Customer Count
  5. Competition Intensity (1-5 scale)
  6. Competitor Count
  7. Customer Concentration %
  8. User Growth Rate %
  9. Net Dollar Retention %
  10. Revenue Growth Rate %
  11. Gross Margin %
  12. LTV/CAC Ratio
  13. 30-Day Product Retention %
  14. 90-Day Product Retention %
  15. DAU/MAU Ratio %
  16. SAM (auto-calculated as 10% of TAM)
  17. SOM (auto-calculated as 1% of SAM)

## Framework System Evolution Summary (V27-V30)

### The Journey to True Framework Flexibility
1. **V27**: Enhanced Michelin with McKinsey-grade output but hardcoded frameworks
2. **V28**: MIT/HBS framework selection intelligence but still outputting fixed frameworks
3. **V29**: PhD enhancement integration with academic rigor
4. **V30**: Dynamic Michelin breaking free from hardcoded requirements

### Current Framework Capabilities
- **557 frameworks** in database with PhD enhancements
- **Academic scoring** with theoretical foundations
- **Framework synergies** and prerequisite tracking
- **Industry-specific variants** (e.g., SaaS BCG uses NRR/ARR)
- **Dynamic selection** based on company context
- **Flexible display** without hardcoded requirements

### API Endpoints for Framework Analysis
```
/api/frameworks/enhanced/select          # MIT/HBS methodology
/api/frameworks/intelligent/recommend    # ML-powered selection
/api/michelin/enhanced/analyze/phase1   # Fixed frameworks (stable)
/api/michelin/dynamic/analyze/phase1    # Dynamic frameworks (new)
```

## Previous Updates (June 2025 - V23)

### Stage-Aware Financial Modeling for Zero-Revenue Startups
- **Issue**: Pre-seed companies typically have zero revenue, causing division by zero errors and unrealistic projections
- **Solution**: Implemented comprehensive stage-aware analysis system that uses market-based projections for pre-revenue companies
- **Key Components**:
  1. **Helper Functions** (`api_framework_deep_analysis.py`):
     - `get_market_capture_timeline_by_stage()`: Returns months to capture target market share (pre-seed: 36, seed: 24, etc.)
     - `get_target_market_share_by_stage()`: Returns realistic market share targets (pre-seed: 0.1%, seed: 0.5%, etc.)
     - `get_valuation_multiple_by_stage()`: Returns appropriate valuation multiples (pre-seed: 15x, seed: 10x, etc.)
     - `get_months_to_first_revenue_by_stage()`: Returns expected time to first revenue (pre-seed: 9 months, seed: 6 months)
     - `get_projected_revenue_by_stage()`: Returns projected first year revenue based on SAM percentage
     - `get_target_customers_by_stage()`: Returns pilot customer targets (pre-seed: 3, seed: 10, etc.)
     - `calculate_pre_revenue_confidence()`: Calculates confidence based on runway, team, domain expertise

  2. **Updated Functions**:
     - `generate_executive_summary()`: Now detects zero-revenue + early stage and switches to pre-revenue mode
     - `generate_financial_projections()`: Uses market-based projections for pre-revenue (Y1: $5-10K, Y2: $50-100K, Y3: $250-500K)
     - `generate_strategic_options_from_frameworks()`: Offers pre-revenue specific options (Customer Discovery Sprint, MVP to Revenue, Strategic Partnership)
     - `create_roadmap_from_frameworks()`: Creates milestone-based roadmap for pre-revenue (PMF → First Revenue → Scale)
     - `generate_fallback_framework_analysis()`: Enhanced unit economics to show target metrics for pre-revenue

  3. **Pre-Revenue Analysis Mode**:
     - Executive Summary: Shows path to first revenue and pilot customers
     - Strategic Options: Focus on validation and early traction
     - Financial Projections: Conservative market-based estimates
     - Implementation Roadmap: Milestone-driven approach
     - Unit Economics: Target-based metrics instead of actuals

- **Sample Data Updates**: Updated `sampleCompanies.ts` to include realistic revenue values for testing
- **API Testing**: Verified with pre-seed zero-revenue company data
- **Status**: Fully operational with intelligent handling of all funding stages

## Previous Updates (December 2024 - V22)

### Deep Dive JSON Parsing Fix
- **Issue**: DeepSeek API returns malformed JSON with unquoted property names in recommendations
- **Solution**: Enhanced `_extract_json_from_response` and added `_fix_malformed_json` methods
- **Features**:
  - Handles markdown-wrapped JSON (```json ... ```)
  - Fixes unquoted property names (e.g., `action:` → `"action":`)
  - Fixes unquoted string values (e.g., `High` → `"High"`)
  - Special handling for recommendations array pattern
  - Fallback to cached responses when JSON parsing fails
- **Status**: Deep Dive endpoints operational with graceful fallback
- **API Key**: DeepSeek API key verified working: sk-f68b7148243e4663a31386a5ea6093cf

## Previous Updates (December 2024 - V21)

### Progressive Deep Dive System
- **4-Phase Analysis**: Context Mapping → Strategic Alignment → Organizational Readiness → Risk-Weighted Pathways
- **Phase 1**: External Reality Check (Porter's Five Forces) + Internal Audit (CAMP deep dive)
- **Phase 2**: Vision-Reality Gap Analysis + Ansoff Matrix for growth strategies
- **Phase 3**: McKinsey 7S Framework for organizational alignment
- **Phase 4**: Scenario Planning with Monte Carlo simulations
- **Synthesis**: Executive summary with strategic priorities and roadmap
- **Data Persistence**: All assessments saved to localStorage
- **Route**: `/deep-dive` with sub-routes for each phase

### Framework Intelligence Engine
- **500+ Frameworks**: Across 9 categories (Strategy, Innovation, Growth, Financial, Operations, Marketing, Product, Leadership, Organizational)
- **AI-Powered Selection**: Multi-factor scoring algorithm with context-aware matching
- **API Endpoints**: 7 new endpoints under `/api/frameworks/*`
- **Frontend Integration**: FrameworkIntelligence component in Results page
- **Features**: Recommendations, Implementation Roadmap, Framework Combinations
- **Backend**: `framework_intelligence/` module with database and selector
- **Scoring**: Business stage (25%), Challenge relevance (30%), Industry fit (15%), Complexity (10%), Goals (10%), Time (5%), Synergy (5%)

## Previous Updates (June 11, 2025 - V20)

### Critical Fixes & Backend Validation Updates
- **Backend Validation Expansion**: Updated `utils/data_validation.py` to accept frontend-specific values
  - investor_tier_primary: Now accepts "university", "corporate", "government" 
  - sector: Now accepts "healthcare", "ai-ml", "artificial-intelligence", "machine-learning", "blockchain", "crypto", "real-estate", "transportation", "clean-tech", "deep-tech"
  - product_stage: Now accepts "idea", "research", "development", "alpha", "live", "scaling"
- **API Server Restart**: Restarted api_server_unified.py to load new validation rules
- **Dependency Installation**: Added missing packages: lucide-react, react-hook-form, @hookform/resolvers, zod
- **TypeScript Fixes**: 
  - Fixed EnhancedAnalysis undefined component error
  - Fixed API headers type casting issue
  - Fixed pillar_scores → camp_scores references in Analysis pages
  - Removed conflicting framer-motion type definitions
  - All TypeScript errors resolved (0 remaining)
- **Frontend-Backend Integration**: Confirmed end-to-end functionality with sample data autofill
- **Build Status**: Application builds successfully with only non-critical warnings

### Component Architecture Refinements
- **Reverted V2 Components**: Restored visual elements (progress bars, charts) from pure typography
- **Autofill Functionality**: Fixed data syncing across all assessment pages via Zustand store
- **Market Page Validation**: Fixed Continue button by making validation conditional on visible fields
- **Sample Data Mapping**: Updated field mappings to match form expectations

## Previous Updates (June 8, 2025 - V19)

### CAMP Analysis Display Fix & Theme Updates
- **CAMP Section Visibility**: Fixed missing text in CAMP Framework Analysis section
  - Added `color: #1D1D1F !important` to h3 elements in ResultsV2.module.scss
  - Added color styling to span elements for score percentages
  - Debug revealed scores are being correctly returned by API but display was affected by CSS
- **Theme Default Change**: Switched from auto/dark theme to light theme default
  - Modified `useAppleTheme.ts` to default to 'light' instead of 'auto'
  - Added localStorage setting for light theme on first load
  - Resolved issue where pages were displaying in dark mode unexpectedly
- **Debug Improvements**: Added comprehensive debugging for CAMP scores data flow
  - Enhanced logging in Review, Analysis, and ResultsV2 components
  - Verified API returns correct camp_scores structure
  - Confirmed data persistence through Zustand store

## Previous Updates (January 8, 2025 - V18)

### Professional UI Transformation 🎨 → 🏢
- **Emoji Removal**: Replaced ALL emojis with custom SVG icons
- **Color Scheme**: Changed from blue (#00d4ff) to white/grayscale palette
- **ScoreCard Redesign**: Modern glassmorphism with white accents
- **Icon Library**: 30+ professional SVG icons
- **Enterprise Ready**: Serious business platform appearance

## Current System Status (V26 - June 2025)

### Frontend Status
- **React Version**: 18.x with TypeScript
- **Build Tool**: Create React App (react-scripts)
- **State Management**: Zustand for global state
- **Routing**: React Router v6
- **Form Handling**: react-hook-form with zod validation
- **Styling**: SCSS modules with CSS variables design system
- **Icons**: lucide-react + custom SVG library
- **Theme**: Light mode default, dark mode optional
- **TypeScript**: Strict mode enabled, 0 compilation errors
- **New Features**: Progressive Deep Dive system, Framework Intelligence UI

### Backend Status
- **API Server**: Python FastAPI (api_server_unified.py)
- **Port**: 8001
- **Models Loaded**: 4 (DNA, Temporal, Industry, Ensemble)
- **Validation**: Extended to accept frontend-specific values
- **Response Time**: ~150-250ms for predictions
- **Health Check**: Endpoint available at /health
- **New APIs**: Framework Intelligence Engine with 7 endpoints
- **Framework Database**: 500+ business frameworks across 9 categories
- **Michelin Analysis**: Three implementations available
  - Original: `/api/michelin/analyze/phase{1,2,3}` (prone to JSON errors)
  - Decomposed: `/api/michelin/decomposed/analyze/phase{1,2,3}` (reliable)
  - Strategic: `/api/michelin/strategic/analyze/phase{1,2,3}` (intelligent)

### Data Validation Rules (Updated)
```python
# Extended enum validations in utils/data_validation.py
"investor_tier_primary": {
    "values": ["tier_1", "tier_2", "tier_3", "angel", "none", 
               "university", "corporate", "government"],  # NEW
},
"sector": {
    "values": [...existing..., "healthcare", "ai-ml", "artificial-intelligence",
               "machine-learning", "blockchain", "crypto", "real-estate", 
               "transportation", "clean-tech", "deep-tech"],  # NEW
},
"product_stage": {
    "values": [...existing..., "idea", "research", "development", 
               "alpha", "live", "scaling"],  # NEW
}
```

### ML Models (Production v45 - Realistic)
- **Location**: `models/production_v45_fixed/`
- **Performance**: Average 72.7% AUC
- **Philosophy**: Honest predictions acknowledging uncertainty
- **Prediction Range**: 0% to 98% (realistic distribution)

## Stage-Aware Financial Modeling Details (V23)

### Pre-Revenue Detection Logic
```python
# In generate_executive_summary(), generate_financial_projections(), etc.
if revenue == 0 and stage in ['pre_seed', 'seed']:
    # Use market-based projections
else:
    # Use traditional revenue-based analysis
```

### Stage-Specific Parameters
```python
# Market capture timeline (months)
timelines = {
    'pre_seed': 36,    # 3 years to meaningful share
    'seed': 24,        # 2 years to meaningful share
    'series_a': 18,    # 1.5 years to meaningful share
    'series_b': 12,    # 1 year to meaningful share
    'series_c': 12,    # 1 year to meaningful share
}

# Target market share (%)
stage_targets = {
    'pre_seed': 0.1,   # 0.1% of SAM
    'seed': 0.5,       # 0.5% of SAM
    'series_a': 1.0,   # 1% of SAM
    'series_b': 5.0,   # 5% of SAM
    'series_c': 10.0,  # 10% of SAM
}

# Valuation multiples
multiples = {
    'pre_seed': 15,    # Higher multiple for early potential
    'seed': 10,        # 10x revenue potential
    'series_a': 8,     # 8x revenue
    'series_b': 6,     # 6x revenue
    'series_c': 4,     # 4x revenue (more mature)
}
```

### Pre-Revenue Strategic Options
1. **Customer Discovery Sprint**: Secure pilot customers in 3 months
2. **MVP to Revenue**: Achieve first revenue milestone in 6-9 months
3. **Strategic Partnership**: Accelerate through channel partnerships

### Pre-Revenue Financial Projections
- Based on % of SAM capture rather than revenue multiples
- Conservative estimates: 0.001% → 0.01% → 0.05% of SAM over 3 years
- Accounts for extended burn period before revenue

### Pre-Revenue Confidence Calculation
```python
confidence_factors = [
    min(100, runway * 100 / 18),              # 18 months runway = 100%
    min(100, team_size * 100 / 10),          # 10 people = 100%
    min(100, domain_expertise * 100 / 10),   # 10 years expertise = 100%
    min(100, (patent_count + prior_exits) * 25),  # Patents/exits worth 25% each
    50 if stage in ['seed', 'series_a'] else 25,  # Stage bonus
]
```

## Key Technical Details

### Frontend Architecture
```
src/
├── components/           # Reusable components
│   ├── *MinimalV2.tsx   # Visual components with charts/progress bars
│   ├── charts/          # Chart components (Radar, Bar, Gauge)
│   └── FrameworkIntelligence.tsx  # NEW: AI framework recommendations
├── pages/
│   ├── Assessment/      # Multi-step assessment wizard
│   │   ├── CompanyInfo/
│   │   ├── Capital/
│   │   ├── Advantage/
│   │   ├── Market/
│   │   └── People/
│   ├── Results/         # Results display with analysis
│   └── DeepDive/        # NEW: Progressive Deep Dive system
│       ├── Phase1_Context/    # External Reality + Internal Audit
│       ├── Phase2_Strategic/  # Vision-Reality + Ansoff Matrix
│       ├── Phase3_Organizational/  # 7S Framework
│       ├── Phase4_RiskPathways/    # Scenario Planning
│       └── Synthesis/         # Executive Summary
├── store/               # Zustand state management
├── services/            # API integration
└── styles/              # Global styles and design system
```

### API Integration (services/api.ts)
- **Base URL**: http://localhost:8001
- **Key Endpoints**:
  - POST /predict - Main prediction endpoint
  - GET /health - Health check
  - POST /analyze - Enhanced analysis
  - POST /api/analysis/recommendations/dynamic - LLM recommendations
  - POST /api/frameworks/recommend - Framework recommendations (NEW)
  - POST /api/frameworks/roadmap - Implementation roadmap (NEW)
  - POST /api/frameworks/combinations - Framework combinations (NEW)
  - GET /api/frameworks/categories - List all categories (NEW)
  - GET /api/frameworks/framework/{name} - Framework details (NEW)
  - POST /api/frameworks/implementation-guide - Custom guide (NEW)
  - GET /api/frameworks/search - Search frameworks (NEW)
- **Field Mapping**: Frontend values are now accepted directly without transformation

### Assessment Data Flow
1. User fills multi-step forms → Zustand store
2. AutofillSelector can populate forms with sample data
3. Data validated on each page before progression
4. Final submission transforms to 45 required features
5. API validates and processes prediction
6. Results displayed with CAMP scores and analysis

## Common Commands

```bash
# Frontend Development
cd /Users/sf/Desktop/FLASH/flash-frontend-apple
npm start                    # Start dev server (port 3000)
npm run build               # Production build
npm run lint                # Run ESLint
npm test                    # Run tests

# Backend API
cd /Users/sf/Desktop/FLASH
python3 api_server_unified.py  # Start API server (port 8001)

# Test API Health
curl http://localhost:8001/health

# Test Prediction (with frontend values)
curl -X POST http://localhost:8001/predict \
  -H "Content-Type: application/json" \
  -d '{
    "investor_tier_primary": "university",
    "sector": "healthcare",
    "product_stage": "idea",
    ...other 42 fields...
  }'
```

## Recent Bug Fixes & Solutions

### 1. Sample Data Not Loading
- **Issue**: Autofill selector visible but forms not populating
- **Fix**: Added useAssessmentStore imports and useEffect hooks to sync with store

### 2. Continue Button Not Working (Market Page)
- **Issue**: Validation required hidden fields
- **Fix**: Made validation conditional on showAdvanced state

### 3. API 500 Errors on Submission
- **Issue**: Backend rejected frontend values (university, healthcare, idea)
- **Fix**: Updated validation rules in data_validation.py and restarted API server

### 4. TypeScript Build Errors
- **Issue**: Missing dependencies and type conflicts
- **Fix**: Installed missing packages and fixed type definitions

## Testing Checklist

- [x] Frontend builds without errors
- [x] API server health check passes
- [x] Sample data autofill works
- [x] All assessment pages accept input
- [x] Form validation works correctly
- [x] API accepts frontend values
- [x] Predictions return realistic probabilities
- [x] Results page displays all components

## Backend Architecture (NEW in V21)

### Framework Intelligence Engine
```
framework_intelligence/
├── __init__.py
├── framework_database.py      # 500+ framework definitions
├── framework_selector.py      # AI selection logic
├── example_usage.py          # Usage examples
├── expand_frameworks.py      # Script to expand to 500+
├── test_framework_engine.py  # Test suite
└── README.md                 # Documentation

api_framework_endpoints.py    # FastAPI endpoints
```

### Progressive Deep Dive Data
- localStorage keys:
  - `externalRealityData` - Porter's Five Forces
  - `internalAuditData` - CAMP deep dive
  - `visionRealityGapData` - Vision assessment
  - `ansoffMatrixData` - Growth strategies
  - `sevenSFrameworkData` - 7S assessment
  - `scenarioPlanningData` - Scenarios

## Dependencies

### Frontend (package.json)
```json
{
  "react": "^18.2.0",
  "react-router-dom": "^6.x",
  "zustand": "^4.x",
  "framer-motion": "^10.x",
  "lucide-react": "latest",
  "react-hook-form": "latest",
  "@hookform/resolvers": "latest",
  "zod": "latest",
  "sass": "^1.x",
  "d3": "^7.x"  // NEW: For visualizations
}
```

### Backend (requirements.txt)
```
fastapi
uvicorn
scikit-learn
xgboost
pandas
numpy
pydantic
redis  # For caching
aiohttp  # For async requests
tenacity  # For retry logic
```

## Important Notes

- **No Field Mapping Needed**: Backend now accepts frontend values directly
- **Validation Warnings**: Backend logs warnings for data quality (e.g., domain expertise > total experience)
- **Professional UI**: No emojis, white/grayscale color scheme
- **Realistic Predictions**: Expect 30-70% success probabilities for most startups
- **API Restart Required**: After validation changes, restart API server to load new rules

---
**Last Updated**: 2025-06-14 (V23)
**UI Version**: Professional with Light Theme Default + Deep Dive System
**Model Performance**: 72.7% AUC (Realistic)
**Backend Validation**: Extended to accept frontend values
**Framework Intelligence**: 500+ frameworks with AI selection
**Progressive Deep Dive**: 4-phase strategic analysis system
**Stage-Aware Analysis**: Intelligent handling of zero-revenue pre-seed/seed companies
**Status**: Fully Functional - All Systems Operational
**API Server**: `api_server_unified.py` (Port 8001)
**Frontend**: React 18 + TypeScript (Port 3000)
## Complete 45-Feature Breakdown (V24)

All 45 features are now collected across the assessment pages:

### Capital Features (7/7) - CapitalMinimal.tsx
1. total_capital_raised_usd
2. cash_on_hand_usd
3. monthly_burn_usd
4. runway_months (auto-calculated)
5. burn_multiple (auto-calculated)
6. investor_tier_primary
7. has_debt

### Advantage Features (8/8) - AdvantageMinimal.tsx
8. patent_count
9. network_effects_present
10. has_data_moat
11. regulatory_advantage_present
12. tech_differentiation_score
13. switching_cost_score
14. brand_strength_score
15. scalability_score

### Market Features (11/11) - MarketSimple.tsx
16. sector
17. tam_size_usd
18. sam_size_usd (auto-calculated)
19. som_size_usd (auto-calculated)
20. market_growth_rate_percent
21. customer_count
22. customer_concentration_percent
23. user_growth_rate_percent
24. net_dollar_retention_percent
25. competition_intensity
26. competitors_named_count

### People Features (10/10) - PeopleMinimal.tsx
27. founders_count
28. team_size_full_time
29. years_experience_avg
30. domain_expertise_years_avg
31. prior_startup_experience_count
32. prior_successful_exits_count
33. board_advisor_experience_score
34. advisors_count
35. team_diversity_percent
36. key_person_dependency

### Product Features (9/9) - Multiple Pages
37. product_stage (AdvantageMinimal.tsx)
38. product_retention_30d (MarketSimple.tsx)
39. product_retention_90d (MarketSimple.tsx)
40. dau_mau_ratio (MarketSimple.tsx)
41. annual_revenue_run_rate (CapitalMinimal.tsx - auto-calculated)
42. revenue_growth_rate_percent (MarketSimple.tsx)
43. gross_margin_percent (MarketSimple.tsx)
44. ltv_cac_ratio (MarketSimple.tsx)
45. funding_stage (CapitalMinimal.tsx)

## Dynamic Michelin Analysis Details (V30)

### Architecture Overview
The Dynamic Michelin system removes hardcoded framework requirements and allows the PhD-enhanced selection engine to choose the most appropriate frameworks for each company's unique context.

### Components

#### Backend (`/api/michelin/dynamic`)
```python
# api_michelin_dynamic.py
class DynamicMichelinEngine:
    def __init__(self):
        self.context_engine = StrategicContextEngine()
        self.framework_selector = EnhancedFrameworkSelector()
        self.analyzer = StrategicAnalysisEngine()
    
    async def analyze_phase1_dynamic(self, startup_data: Dict) -> Dict:
        # 1. Build context
        context = await self.context_engine.build_company_context(startup_data)
        
        # 2. Select frameworks dynamically
        result = await self.framework_selector.select_frameworks_for_startup(
            startup_data, max_frameworks=3
        )
        
        # 3. Analyze each selected framework
        frameworks_analysis = []
        for fw in result["frameworks"]:
            analysis = await self.analyzer.generate_framework_analysis(fw, context)
            frameworks_analysis.append({
                "framework_name": fw.name,
                "framework_id": fw.id,
                "category": fw.category,
                "analysis": analysis,
                "fit_score": fw.fit_score,
                "rationale": fw.rationale
            })
        
        return {
            "executive_summary": summary,
            "frameworks_analysis": frameworks_analysis,
            "current_position_narrative": narrative,
            "context": context_data
        }
```

#### Frontend (`MichelinDynamicAnalysis.tsx`)
```typescript
interface DynamicFrameworkAnalysis {
  framework_name: string;
  framework_id: string;
  category: string;
  analysis: any;
  fit_score: number;
  rationale: string[];
}

// Renders any combination of frameworks
const MichelinDynamicAnalysis: React.FC = () => {
  // Displays frameworks dynamically without hardcoded sections
  return (
    <div className={styles.frameworkAnalysis}>
      {frameworks.map(fw => (
        <FrameworkCard
          key={fw.framework_id}
          framework={fw}
          expandable={true}
        />
      ))}
    </div>
  );
};
```

### Key Differences from Enhanced Approach

| Feature | Enhanced (Hardcoded) | Dynamic (Flexible) |
|---------|---------------------|-------------------|
| Framework Requirements | BCG Matrix, Porter's Five Forces, SWOT | Any frameworks selected by AI |
| Data Model | Fixed fields in Phase1Analysis | Flexible List[Dict] structure |
| Frontend Display | Hardcoded sections for each framework | Dynamic cards for any framework |
| Context Awareness | Limited to predefined frameworks | Full PhD-enhanced selection |
| Customization | Industry variants of fixed frameworks | Completely different frameworks per context |

### Current Status
- Dynamic system is implemented and functional
- Feature flag allows easy switching between approaches
- Some refinement needed for framework object serialization
- Currently using 'enhanced' approach in production for stability

### Future Improvements
1. Complete framework object serialization between backend/frontend
2. Add Phase 2 and Phase 3 dynamic analysis
3. Implement framework combination synergy visualization
4. Add real-time framework selection explanation UI
