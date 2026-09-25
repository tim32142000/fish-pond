import plotly.graph_objects as go
import streamlit as st

from simulation import create_fish, step_fish

FISH_COUNT = 10
TIME_STEP = 0.2
PADDING = 5

st.set_page_config(page_title="Fish Pond", layout="centered")

st.title("Fish Pond")


if "fish" not in st.session_state:
    st.session_state.fish = create_fish(FISH_COUNT)


def create_pond_figure():
    fish = st.session_state.fish

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=[f.x for f in fish],
            y=[f.y for f in fish],
            mode="text",
            text=["🐟"] * len(fish),
            textfont={"size": 24},
            hoverinfo="skip",
        )
    )

    fig.update_xaxes(
        range=[-PADDING, 100 + PADDING],
        visible=False,
        fixedrange=True,
    )

    fig.update_yaxes(
        range=[-PADDING, 100 + PADDING],
        visible=False,
        fixedrange=True,
        scaleanchor="x",
        scaleratio=1,
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,
        height=500,
    )

    return fig


@st.fragment(run_every=TIME_STEP)
def pond():
    step_fish(st.session_state.fish)

    st.plotly_chart(
        create_pond_figure(),
        width="stretch",
        config={"displayModeBar": False},
    )


pond()
