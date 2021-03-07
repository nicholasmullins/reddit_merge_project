import logging
import time
import os

log = logging.getLogger(__name__)


def run(context):
	if element_exists(context, 'txt_allow_camera_location'):
		context.perform_gesture('tap', 'btn_allow_all_the_time')
		context.perform_gesture('tap', 'btn_next')
		if element_exists(context, 'btn_camera_capture'):
			context.perform_gesture('tap', 'btn_camera_capture')
		else:
			context.verify(labels=["btn_video_capture"])

def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0