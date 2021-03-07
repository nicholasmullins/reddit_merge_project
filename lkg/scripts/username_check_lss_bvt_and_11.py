import logging
import time
import os

log = logging.getLogger(__name__)


def run(context):
	context.perform_gesture('tap', 'btn_menu_view')
	context.perform_gesture_on_coord('swipe_custom', {'start_x': 540, 'start_y': 1600, 'end_x': 540, 'end_y': 1200, 'duration': 2000})

	if element_exists(context, 'ddl_lss_bvt_and_11'):
		context.verify(labels=["ddl_lss_bvt_and_11"])
	else:
		context.perform_gesture('tap', 'ddl_username')
		context.perform_gesture('tap', 'li_lss_bvt_and_11')
		context.perform_gesture('tap', 'btn_menu_view')
		context.verify(labels=["ddl_lss_bvt_and_11"])

def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0