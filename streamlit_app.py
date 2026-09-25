import random
import time

import plotly.graph_objects as go
import streamlit as st

from simulation import POND_SIZE, Food, create_fish, step_fish

FISH_COUNT = 30
UPDATE_INTERVAL = 0.2
PADDING = 5
MIN_FOOD_INTERVAL = 2.0
MAX_FOOD_INTERVAL = 6.0

st.set_page_config(page_title="Fish Pond", layout="centered")

st.title("Fish Pond")


if "fish" not in st.session_state:
    st.session_state.fish = create_fish(FISH_COUNT)

if "food" not in st.session_state:
    st.session_state.food = None

if "next_food_time" not in st.session_state:
    st.session_state.next_food_time = time.monotonic() + random.uniform(
        MIN_FOOD_INTERVAL,
        MAX_FOOD_INTERVAL,
    )


def schedule_next_food():
    st.session_state.next_food_time = time.monotonic() + random.uniform(
        MIN_FOOD_INTERVAL,
        MAX_FOOD_INTERVAL,
    )


def create_pond_figure():
    fig = go.Figure()

    fish = st.session_state.fish

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

    food = st.session_state.food

    if food is not None:
        fig.add_trace(
            go.Scatter(
                x=[food.x],
                y=[food.y],
                mode="text",
                text=["🍞"],
                textfont={"size": 22},
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


@st.fragment(run_every=UPDATE_INTERVAL)
def pond():
    if (
        st.session_state.food is None
        and time.monotonic() >= st.session_state.next_food_time
    ):
        st.session_state.food = Food(
            x=random.uniform(0, POND_SIZE),
            y=random.uniform(0, POND_SIZE),
        )

    food_eaten = step_fish(
        st.session_state.fish,
        st.session_state.food,
    )

    if food_eaten:
        st.session_state.food = None
        schedule_next_food()

    st.plotly_chart(
        create_pond_figure(),
        width="stretch",
        config={"displayModeBar": False},
    )


pond()
