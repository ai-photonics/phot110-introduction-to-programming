import numpy as np


def add_position(positions, x, y, z, t):
    position = {"x": x, "y": y, "z": z, "t": t}
    positions.append(position)
    return positions


def convert_to_dict(positions):
    # Initialize empty dictionary
    coords = {}
    n_elements = len(positions)
    # Add all the possible coordinates: x, y, z, t
    for k in positions[0].keys():
        coords[k] = np.zeros((n_elements, 1))
    for i, position in enumerate(positions):
        for k, v in position.items():
            coords[k][i] = v

    return coords

