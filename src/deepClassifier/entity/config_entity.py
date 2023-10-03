from dataclasses import dataclasses
from pathlib import path

        
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: path
    source_URL: str
    local_data_file: path
    unzip_dir: path