import logging
import os

log_dir = os.path.join(os.path.dirname(__file__), '..', 'reports')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'test.log'), encoding='utf-8'),
        logging.StreamHandler()
    ]
)

log = logging.getLogger()