import logging
import time
import os

log = logging.getLogger(__name__)


def run(context):
    if element_exists(context, 'tgl_rpan_env_off'):
        context.perform_gesture('tap', 'tgl_rpan_env')
    else:
        context.verify(['tgl_rpan_env_on'])

def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0