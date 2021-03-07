import logging
import time
import os

log = logging.getLogger(__name__)


def run(context):
    if element_exists(context, 'btn_allow'):
        context.perform_gesture('tap', 'btn_allow')
        context.verify(labels=["ttl_video_post"])
    else:
        context.verify(labels=["ttl_video_post"])

def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0