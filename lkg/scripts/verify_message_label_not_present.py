import logging

log = logging.getLogger(__name__)

def run(context):
    context.verify(labels=["inp_send_a_message"], label_count=0)