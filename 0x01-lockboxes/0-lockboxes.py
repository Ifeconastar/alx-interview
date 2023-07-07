#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    if len(boxes) == 0:
        return False

    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True

    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key >= 0 and key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
