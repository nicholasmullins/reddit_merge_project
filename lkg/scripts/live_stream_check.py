import logging
import time
import os

log = logging.getLogger(__name__)


def run(context):
    if element_exists(context, 'ttl_top_broadcast'):
        context.perform_gesture('swipe_up', 'ttl_top_broadcast')
    else:
        context.perform_gesture_if_exists('tap', 'btn_live_stream')

def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0