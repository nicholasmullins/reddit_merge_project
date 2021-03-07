import logging
import time
import os

log = logging.getLogger(__name__)


def run(context):
	context.perform_gesture('tap', 'btn_menu')
	context.perform_gesture('swipe_up', '')

	if element_exists(context, 'ddl_lss_bvt_and_11'):
		context.verify(labels=["ddl_lss_bvt_and_11"])
	else:
		context.perform_gesture('tap', 'ddl_username')
		context.perform_gesture('tap', 'li_lss_bvt_and_11')
		context.perform_gesture('tap', 'btn_menu')
		context.verify(labels=["ddl_lss_bvt_and_11"])

def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0