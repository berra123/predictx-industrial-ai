import random


def get_component_health(prediction):

    machine_health = prediction["health"]

    motor = max(
        0,
        min(
            100,
            machine_health + random.randint(-5, 5)
        )
    )

    gearbox = max(
        0,
        min(
            100,
            machine_health + random.randint(-8, 3)
        )
    )

    bearing = max(
        0,
        min(
            100,
            machine_health - random.randint(5, 20)
        )
    )

    drum = max(
        0,
        min(
            100,
            machine_health + random.randint(-3, 4)
        )
    )

    return {
        "motor": motor,
        "gearbox": gearbox,
        "bearing": bearing,
        "drum": drum
    }