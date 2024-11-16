import os
from pathlib import Path
import urllib.request as request
import zipfile
from ChickenDiseaseClassifier import logger
import tensorflow as tf 
import time

from ChickenDiseaseClassifier.entity.config_entity import PrepareCallbackConfig


class PrepareCallback:
    def __init__(self, config: PrepareCallbackConfig):
        self.config = config
        
    @property
    def __create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    @property
    def __create_ckpt_callbacks(self):
        filepath = Path(self.config.checkpoint_model_filepath).with_suffix('.keras')
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=str(filepath),
            save_best_only=True,
    )

    
    def get_tb_ckpt_callbacks(self):
        return [self.__create_tb_callbacks, self.__create_ckpt_callbacks]
                                  

