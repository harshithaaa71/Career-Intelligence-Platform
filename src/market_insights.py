import pandas as pd

def get_market_data():

    data = {
        "Skill": [
            "Python",
            "SQL",
            "Power BI",
            "Excel",
            "Tableau",
            "Machine Learning",
            "Statistics"
        ],

        "Demand": [
            95,
            90,
            85,
            80,
            75,
            70,
            65
        ]
    }

    return pd.DataFrame(data)