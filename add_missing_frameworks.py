#!/usr/bin/env python3
"""
Add missing framework definitions to the database
"""

# First, let's check what the framework database structure looks like
from framework_intelligence.framework_database import Framework, FrameworkCategory, ComplexityLevel

# Create the missing frameworks
lean_canvas = Framework(
    id="lean_canvas",
    name="Lean Canvas",
    description="A one-page business model template for documenting key assumptions and hypotheses",
    category=FrameworkCategory.STARTUP,
    subcategory="Business Model Design",
    when_to_use=[
        "When starting a new venture or product",
        "For rapid business model iteration",
        "To document and test key assumptions",
        "For early-stage startup planning",
        "When pivoting business model"
    ],
    key_components=[
        "Problem",
        "Solution", 
        "Key Metrics",
        "Unique Value Proposition",
        "Unfair Advantage",
        "Channels",
        "Customer Segments",
        "Cost Structure",
        "Revenue Streams"
    ],
    application_steps=[
        "Identify top 3 problems worth solving",
        "Define your target customer segments",
        "Craft unique value proposition",
        "Outline solution approach",
        "Identify key metrics to track",
        "Define channels to reach customers",
        "Determine revenue streams",
        "Calculate cost structure",
        "Identify unfair advantages"
    ],
    expected_outcomes=[
        "Clear business model hypothesis",
        "Identified key assumptions to test",
        "Focused product development priorities",
        "Aligned team understanding",
        "Rapid iteration capability"
    ],
    complexity=ComplexityLevel.BASIC,
    time_to_implement="1-2 hours",
    industry_relevance=["All industries"],
    success_metrics=[
        "Assumption validation rate",
        "Time to first customer",
        "Pivot decision speed",
        "Team alignment score"
    ]
)

customer_development = Framework(
    id="customer_development",
    name="Customer Development",
    description="Steve Blank's methodology for discovering and validating customer problems and solutions",
    category=FrameworkCategory.CUSTOMER,
    subcategory="Customer Discovery",
    when_to_use=[
        "Before building product features",
        "When validating problem-solution fit",
        "For understanding customer needs deeply",
        "During early-stage product development",
        "When entering new market segments"
    ],
    key_components=[
        "Customer Discovery",
        "Customer Validation",
        "Customer Creation",
        "Company Building",
        "Hypothesis Testing",
        "Pivot vs Persevere Decisions"
    ],
    application_steps=[
        "State your hypotheses",
        "Get out of the building",
        "Test problem hypotheses with customers",
        "Test solution hypotheses",
        "Verify business model",
        "Prepare to scale or pivot",
        "Validate with paying customers",
        "Build repeatable sales process"
    ],
    expected_outcomes=[
        "Validated customer problems",
        "Confirmed solution fit",
        "Repeatable sales process",
        "Product-market fit signals",
        "Clear customer segments"
    ],
    complexity=ComplexityLevel.INTERMEDIATE,
    time_to_implement="4-12 weeks",
    industry_relevance=["All industries"],
    success_metrics=[
        "Customer interview count",
        "Hypothesis validation rate",
        "Customer conversion rate",
        "Time to product-market fit"
    ]
)

print(f"Created definition for: {lean_canvas.name}")
print(f"Created definition for: {customer_development.name}")

# Now let's see how to add them to the database
import inspect
from framework_intelligence import framework_database

# Find where FRAMEWORKS is defined
source_file = inspect.getsourcefile(framework_database)
print(f"\nFramework database file: {source_file}")

# We need to add these to the FRAMEWORKS dictionary in framework_database.py