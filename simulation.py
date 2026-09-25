import math
import random
from dataclasses import dataclass

POND_SIZE = 100
MAX_SPEED = 1.5

TURN_ANGLE_STDDEV = 0.3
SPEED_CHANGE_STDDEV = 0.24


@dataclass
class Fish:
    x: float
    y: float
    vx: float
    vy: float


def create_fish(count: int) -> list[Fish]:
    fish_list = []

    for _ in range(count):
        angle = random.uniform(0, 2 * math.pi)

        speed = random.uniform(0, MAX_SPEED)

        fish_list.append(
            Fish(
                x=random.uniform(0, POND_SIZE),
                y=random.uniform(0, POND_SIZE),
                vx=math.cos(angle) * speed,
                vy=math.sin(angle) * speed,
            )
        )

    return fish_list


def step_fish(fish_list: list[Fish]) -> None:
    for fish in fish_list:
        speed = math.hypot(fish.vx, fish.vy)
        angle = math.atan2(fish.vy, fish.vx)

        angle += random.gauss(mu=0.0, sigma=TURN_ANGLE_STDDEV)

        speed += random.gauss(mu=0.0, sigma=SPEED_CHANGE_STDDEV)
        speed = max(0, min(MAX_SPEED, speed))

        fish.vx = math.cos(angle) * speed
        fish.vy = math.sin(angle) * speed

        fish.x += fish.vx
        fish.y += fish.vy

        if fish.x < 0:
            fish.x = 0
            fish.vx = abs(fish.vx)

        elif fish.x > POND_SIZE:
            fish.x = POND_SIZE
            fish.vx = -abs(fish.vx)

        if fish.y < 0:
            fish.y = 0
            fish.vy = abs(fish.vy)

        elif fish.y > POND_SIZE:
            fish.y = POND_SIZE
            fish.vy = -abs(fish.vy)
