import plotly.express as px
import pandas as pd

def mutation_heatmap(aligned_ref, aligned_sample):

    data = []

    for i, (r, s) in enumerate(zip(aligned_ref, aligned_sample)):

        if r != s:
            data.append({
                "Position": i + 1,
                "Type": "Match" if r == s else "Mismatch"
            })

    df = pd.DataFrame(data)

    fig = px.scatter(
        df,
        x="Position",
        y="Type",
        color="Type",
        title="Mutation Heatmap"
    )

    return fig