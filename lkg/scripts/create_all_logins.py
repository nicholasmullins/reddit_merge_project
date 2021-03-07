'''
    if element_exists(context, 'tab_home'):
        context.perform_gesture('tap', 'tab_home')
'''

import logging
import time
import os

log = logging.getLogger(__name__)

def run(context):
    #Access the app as lss_bvt_and_01
    #Dismiss notifications prompt
    context.perform_gesture_if_exists('tap', 'btn_ok')
    context.perform_gesture_if_exists('tap', 'btn_allow')
        
    #Log in flow #1        
    if element_exists(context, 'btn_goto_log_in'):
        context.perform_gesture('tap', 'btn_goto_log_in')
        login(context)
    else:
        element_exists(context, 'icn_reddit_home')
        context.perform_gesture('tap', 'icn_reddit_home')

    #Log in reddit_lss_11
    open_login(context)

def login(context):
    try:
        if element_exists(context, 'ttl_log_in'):

            # The scripting API supports hybrid element detection mode.
            # In this particular case, default element detection is not sufficient as there is a nested WebView.
            # Using enable_image_mode we can instruct the test.ai system to use AI to detect elements on the screen.


            context.perform_gesture('text_entry_no_submit', 'inp_password', 'endanger bonsai opposite')
            context.perform_gesture('text_entry_no_submit', 'inp_username', 'lss_bvt_and_01')
            context.perform_gesture('tap', 'btn_continue')
            context.perform_gesture('tap', 'btn_menu_view')
            context.perform_gesture_on_coord('tap', {'x': 850, 'y': 1100})
            context.perform_gesture('tap', 'ddl_username')
            context.perform_gesture('tap', 'li_add_account')
            context.perform_gesture('text_entry_no_submit', 'inp_password', 'endanger bonsai opposite')
            context.perform_gesture('text_entry_no_submit', 'inp_username', 'lss_bvt_and_11')
            context.perform_gesture('tap', 'btn_continue')
            context.perform_gesture('tap', 'btn_menu_view')
            context.perform_gesture('tap', 'ddl_username')
            context.perform_gesture('tap', 'li_add_account')
            context.perform_gesture('text_entry_no_submit', 'inp_password', 'endanger bonsai opposite')
            context.perform_gesture('text_entry_no_submit', 'inp_username', 'lss_bvt_and_14')
            context.perform_gesture('tap', 'btn_continue')

    finally:
        context.get_all_elements()

def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0