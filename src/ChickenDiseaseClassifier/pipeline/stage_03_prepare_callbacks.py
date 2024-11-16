from ChickenDiseaseClassifier.components.prepare_callbacks import PrepareCallback
from ChickenDiseaseClassifier.config.configuration import ConfigurationManager
from ChickenDiseaseClassifier.components.prepare_base_model import PrepareBaseModel
from ChickenDiseaseClassifier import logger


STAGE_NAME="Prepare call backs"

class PrepareCallbackPipeline:
    def __init__(self):
        pass


    def main(self):
         
         config = ConfigurationManager()
         prepare_callback_config = config.get_prepare_callback_config()
         prepare_callback= PrepareCallback(config=prepare_callback_config)
         callback_list= prepare_callback.get_tb_ckpt_callbacks()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<" )
        obj = PrepareCallbackPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x" )
    except Exception as e:
        logger.exception(e)
        raise e
