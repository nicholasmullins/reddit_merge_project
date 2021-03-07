import logging
import time
import os

log = logging.getLogger(__name__)


def run(context):
    if element_exists(context, 'btn_moderate'):
        context.perform_gesture('tap', 'icn_more_menu')
        context.perform_gesture('tap', 'mi_delete_post')
    else:
    	context.perform_gesture('tap', 'icn_expand_post')
    	context.perform_gesture('tap', 'icn_more_menu')
        context.perform_gesture('tap', 'mi_delete_post')

def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0


