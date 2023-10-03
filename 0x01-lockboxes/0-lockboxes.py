#!/usr/bin/python3
"""Solution to Lockboxes problem"""

def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    # Create a set to keep track of opened boxes
    opened_boxes = {0}
    
    # Iterate through each box and its keys
    for box_index, keys in enumerate(boxes):
        if box_index in opened_boxes:
            # Add keys to the set of opened boxes
            opened_boxes.update(keys)
    
    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)

