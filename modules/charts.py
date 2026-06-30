import plotly.express as px
import pandas as pd


def mutation_chart(summary):

    df = pd.DataFrame({
        "Mutation": [
            "Substitution",
            "Insertion",
            "Deletion"
        ],
        "Count": [
            summary["Substitution"],
            summary["Insertion"],
            summary["Deletion"]
        ]
    })

    fig = px.bar(
        df,
        x="Mutation",
        y="Count",
        title="Mutation Distribution",
        text="Count"
    )

    return fig