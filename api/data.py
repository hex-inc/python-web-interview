USERS = [
    {"id": 0, "name": "James Smith"},  # 0
    {"id": 1, "name": "Maria Garcia"},  # 5
    {"id": 2, "name": "Robert Johnson"},  # 15
    {"id": 3, "name": "Jennifer Lee"},  # 4
    {"id": 4, "name": "Michael Graham"},  # 16
    {"id": 5, "name": "Linda Davis"},  # 14
    {"id": 6, "name": "William Jones"},  # 11
    {"id": 7, "name": "Emily Martinez"},  # 10
    {"id": 8, "name": "David Wilson"},  # 12
    {"id": 9, "name": "Jessica Taylor"}  # 13
]

PROJECTS = [
    {"id": 0, "title": "Market Trend Analysis", "creatorId": 1},  # Maria Garcia
    {"id": 1, "title": "Consumer Behavior Study", "creatorId": 1},  # Maria Garcia
    {"id": 2, "title": "Sales Forecast Model", "creatorId": 1},  # Maria Garcia
    {"id": 3, "title": "Operational Efficiency Review", "creatorId": 1},  # Maria Garcia
    {"id": 4, "title": "Investment Portfolio Analysis", "creatorId": 5},  # Linda Davis
    {"id": 5, "title": "Customer Segmentation Insight", "creatorId": 2},  # Robert Johnson
    {"id": 6, "title": "Risk Assessment Report", "creatorId": 2},  # Robert Johnson
    {"id": 7, "title": "Product Development Strategy", "creatorId": 2},  # Robert Johnson
    {"id": 8, "title": "Investment Portfolio Analysis", "creatorId": 2},  # Robert Johnson
    {"id": 9, "title": "Resource Allocation Plan", "creatorId": 2},  # Robert Johnson
    {"id": 10, "title": "Competitive Landscape Mapping", "creatorId": 3},  # Jennifer Lee
    {"id": 11, "title": "User Engagement Metrics", "creatorId": 3},  # Jennifer Lee
    {"id": 12, "title": "Healthcare Outcomes Research", "creatorId": 2},  # Robert Johnson
    {"id": 13, "title": "Market Trend Analysis", "creatorId": 4},  # Michael Graham
    {"id": 14, "title": "Consumer Behavior Study", "creatorId": 4},  # Michael Graham
    {"id": 15, "title": "Sales Forecast Model", "creatorId": 4},  # Michael Graham
    {"id": 16, "title": "Operational Efficiency Review", "creatorId": 4},  # Michael Graham
    {"id": 17, "title": "Revenue Optimization Simulation", "creatorId": 4},  # Michael Graham
    {"id": 18, "title": "Customer Segmentation Insight", "creatorId": 5},  # Linda Davis
    {"id": 19, "title": "Risk Assessment Report", "creatorId": 5},  # Linda Davis
    {"id": 20, "title": "Product Development Strategy", "creatorId": 5},  # Linda Davis
    {"id": 21, "title": "Investment Portfolio Analysis", "creatorId": 5},  # Linda Davis
    {"id": 22, "title": "Resource Allocation Plan", "creatorId": 5},  # Linda Davis
    {"id": 23, "title": "Competitive Landscape Mapping", "creatorId": 6},  # William Jones
    {"id": 24, "title": "User Engagement Metrics", "creatorId": 6},  # William Jones
    {"id": 25, "title": "Healthcare Outcomes Research", "creatorId": 6},  # William Jones
    {"id": 26, "title": "Market Trend Analysis", "creatorId": 6},  # William Jones
    {"id": 27, "title": "Consumer Behavior Study", "creatorId": 6},  # William Jones
    {"id": 28, "title": "Sales Forecast Model", "creatorId": 7},  # Emily Martinez
    {"id": 29, "title": "Operational Efficiency Review", "creatorId": 7},  # Emily Martinez
    {"id": 30, "title": "Revenue Optimization Simulation", "creatorId": 7},  # Emily Martinez
    {"id": 31, "title": "Customer Segmentation Insight", "creatorId": 7},  # Emily Martinez
    {"id": 32, "title": "Risk Assessment Report", "creatorId": 7},  # Emily Martinez
    {"id": 33, "title": "Product Development Strategy", "creatorId": 8},  # David Wilson
    {"id": 34, "title": "Investment Portfolio Analysis", "creatorId": 8},  # David Wilson
    {"id": 35, "title": "Resource Allocation Plan", "creatorId": 8},  # David Wilson
    {"id": 36, "title": "Competitive Landscape Mapping", "creatorId": 8},  # David Wilson
    {"id": 37, "title": "User Engagement Metrics", "creatorId": 8},  # David Wilson
    {"id": 38, "title": "Healthcare Outcomes Research", "creatorId": 8},  # David Wilson
    {"id": 39, "title": "Market Trend Analysis", "creatorId": 9},  # Jessica Taylor
    {"id": 40, "title": "Consumer Behavior Study", "creatorId": 9},  # Jessica Taylor
    {"id": 41, "title": "Sales Forecast Model", "creatorId": 9},  # Jessica Taylor
    {"id": 42, "title": "Operational Efficiency Review", "creatorId": 9},  # Jessica Taylor
    {"id": 43, "title": "Revenue Optimization Simulation", "creatorId": 9},  # Jessica Taylor
    {"id": 44, "title": "Customer Segmentation Insight", "creatorId": 9},  # Jessica Taylor
    {"id": 45, "title": "Risk Assessment Report", "creatorId": 2},  # Robert Johnson
    {"id": 46, "title": "Product Development Strategy", "creatorId": 2},  # Robert Johnson
    {"id": 47, "title": "Investment Portfolio Analysis", "creatorId": 2},  # Robert Johnson
    {"id": 48, "title": "Resource Allocation Plan", "creatorId": 2},  # Robert Johnson
    {"id": 49, "title": "Competitive Landscape Mapping", "creatorId": 9},  # Jessica Taylor
    {"id": 50, "title": "User Engagement Metrics", "creatorId": 3},  # Jennifer Lee
    {"id": 51, "title": "Healthcare Outcomes Research", "creatorId": 2},  # Robert Johnson
    {"id": 52, "title": "Market Trend Analysis", "creatorId": 4},  # Michael Graham
    {"id": 53, "title": "Consumer Behavior Study", "creatorId": 4},  # Michael Graham
    {"id": 54, "title": "Sales Forecast Model", "creatorId": 4},  # Michael Graham
    {"id": 55, "title": "Operational Efficiency Review", "creatorId": 4},  # Michael Graham
    {"id": 56, "title": "Revenue Optimization Simulation", "creatorId": 4},  # Michael Graham
    {"id": 57, "title": "Customer Segmentation Insight", "creatorId": 5},  # Linda Davis
    {"id": 58, "title": "Risk Assessment Report", "creatorId": 5},  # Linda Davis
    {"id": 59, "title": "Product Development Strategy", "creatorId": 5},  # Linda Davis
    {"id": 60, "title": "Investment Portfolio Analysis", "creatorId": 5},  # Linda Davis
    {"id": 61, "title": "Resource Allocation Plan", "creatorId": 5},  # Linda Davis
    {"id": 62, "title": "Competitive Landscape Mapping", "creatorId": 6},  # William Jones
    {"id": 63, "title": "User Engagement Metrics", "creatorId": 6},  # William Jones
    {"id": 64, "title": "Healthcare Outcomes Research", "creatorId": 6},  # William Jones
    {"id": 65, "title": "Market Trend Analysis", "creatorId": 6},  # William Jones
    {"id": 66, "title": "Consumer Behavior Study", "creatorId": 6},  # William Jones
    {"id": 67, "title": "Sales Forecast Model", "creatorId": 7},  # Emily Martinez
    {"id": 68, "title": "Operational Efficiency Review", "creatorId": 7},  # Emily Martinez
    {"id": 69, "title": "Revenue Optimization Simulation", "creatorId": 7},  # Emily Martinez
    {"id": 70, "title": "Customer Segmentation Insight", "creatorId": 7},  # Emily Martinez
    {"id": 71, "title": "Risk Assessment Report", "creatorId": 7},  # Emily Martinez
    {"id": 72, "title": "Product Development Strategy", "creatorId": 8},  # David Wilson
    {"id": 73, "title": "Investment Portfolio Analysis", "creatorId": 8},  # David Wilson
    {"id": 74, "title": "Resource Allocation Plan", "creatorId": 8},  # David Wilson
    {"id": 75, "title": "Competitive Landscape Mapping", "creatorId": 8},  # David Wilson
    {"id": 76, "title": "User Engagement Metrics", "creatorId": 8},  # David Wilson
    {"id": 77, "title": "Healthcare Outcomes Research", "creatorId": 8},  # David Wilson
    {"id": 78, "title": "Market Trend Analysis", "creatorId": 9},  # Jessica Taylor
    {"id": 79, "title": "Consumer Behavior Study", "creatorId": 9},  # Jessica Taylor
    {"id": 80, "title": "Sales Forecast Model", "creatorId": 9},  # Jessica Taylor
    {"id": 81, "title": "Operational Efficiency Review", "creatorId": 9},  # Jessica Taylor
    {"id": 82, "title": "Revenue Optimization Simulation", "creatorId": 9},  # Jessica Taylor
    {"id": 83, "title": "Customer Segmentation Insight", "creatorId": 9},  # Jessica Taylor
    {"id": 84, "title": "Risk Assessment Report", "creatorId": 2},  # Robert Johnson
    {"id": 85, "title": "Product Development Strategy", "creatorId": 2},  # Robert Johnson
    {"id": 86, "title": "Investment Portfolio Analysis", "creatorId": 2},  # Robert Johnson
    {"id": 87, "title": "Resource Allocation Plan", "creatorId": 2},  # Robert Johnson
    {"id": 88, "title": "Competitive Landscape Mapping", "creatorId": 3},  # Jennifer Lee
    {"id": 89, "title": "User Engagement Metrics", "creatorId": 4},  # Michael Graham
    {"id": 90, "title": "Healthcare Outcomes Research", "creatorId": 6},  # William Jones
    {"id": 91, "title": "Market Trend Analysis", "creatorId": 4},  # Michael Graham
    {"id": 92, "title": "Consumer Behavior Study", "creatorId": 4},  # Michael Graham
    {"id": 93, "title": "Sales Forecast Model", "creatorId": 4},  # Michael Graham
    {"id": 94, "title": "Operational Efficiency Review", "creatorId": 4},  # Michael Graham
    {"id": 95, "title": "Revenue Optimization Simulation", "creatorId": 4},  # Michael Graham
    {"id": 96, "title": "Customer Segmentation Insight", "creatorId": 5},  # Linda Davis
    {"id": 97, "title": "Risk Assessment Report", "creatorId": 5},  # Linda Davis
    {"id": 98, "title": "Product Development Strategy", "creatorId": 5},  # Linda Davis
    {"id": 99, "title": "Revenue Optimization Simulation", "creatorId": 1}  # Maria Garcia
]
