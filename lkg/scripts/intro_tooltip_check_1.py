import logging
import time
import os

log = logging.getLogger(__name__)


def run(context):
    if element_exists(context, 'txt_swipe_to_dismiss'):
        context.perform_gesture_on_coord('swipe_custom', {'start_x': 540, 'start_y': 1800, 'end_x': 540, 'end_y': 1200, 'duration': 1000})
    else:
        context.verify(labels=["icn_reddit_home"])

def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0