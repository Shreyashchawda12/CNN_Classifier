import os
import sys
import logging

log_dir = "logs"

logging_str = "[%(asctime)s] %(levelname)s:%(module)s:%(message)s"

log_path = os.path.join(log_dir,"running_logs.log")

os.makedirs(log_path,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)
logging.getLogger("deepClassifier")