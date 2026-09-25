import plotly.graph_objects as go
import streamlit as st

from simulation import Food, create_fish, step_fish

POND_SIZE = 100
FISH_COUNT = 5
TIME_STEP = 0.5
PADDING = 5
CLICK_GRID_STEP = 2

st.set_page_config(page_title="Fish Pond", layout="centered")

st.title("Fish Pond")


if "fish" not in st.session_state:
    st.session_state.fish = create_fish(FISH_COUNT)

if "food" not in st.session_state:
    st.session_state.food = None

if "click_count" not in st.session_state:
    st.session_state.click_count = 0


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

    # 最後才加入 click layer

    click_x = []
    click_y = []

    for x in range(0, POND_SIZE + 1, CLICK_GRID_STEP):
        for y in range(0, POND_SIZE + 1, CLICK_GRID_STEP):
            click_x.append(x)
            click_y.append(y)

    fig.add_trace(
        go.Scatter(
            x=click_x,
            y=click_y,
            mode="markers",
            marker={
                "size": 30,
                "symbol": "square",
                "color": "rgba(0,0,0,0.001)",
            },
            hoverinfo="none",
            showlegend=False,
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


def place_food():
    points = st.session_state.pond_chart.selection.points

    if not points:
        return

    point = points[-1]

    st.session_state.click_count += 1

    st.session_state.food = Food(
        x=float(point["x"]),
        y=float(point["y"]),
    )


@st.fragment(run_every=TIME_STEP)
def pond():
    st.write("click count:", st.session_state.click_count)

    food_eaten = step_fish(
        st.session_state.fish,
        st.session_state.food,
    )

    if food_eaten:
        st.session_state.food = None

    st.plotly_chart(
        create_pond_figure(),
        key="pond_chart",
        on_select=place_food,
        selection_mode="points",
        width="stretch",
        config={"displayModeBar": False},
    )


pond()
