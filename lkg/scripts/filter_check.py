import logging
import time
import os

log = logging.getLogger(__name__)


def run(context):
    if element_exists(context, 'ddl_filters_hot_posts'):
        context.perform_gesture('tap', 'ddl_filters_hot_posts')
        context.perform_gesture_if_exists('tap', 'li_new')
    else:
        context.verify(labels=["ddl_filters_new_posts"])
        context.perform_gesture_on_coord('swipe_custom', {'start_x': 540, 'start_y': 885, 'end_x': 540, 'end_y': 1500, 'duration': 1000})

def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0