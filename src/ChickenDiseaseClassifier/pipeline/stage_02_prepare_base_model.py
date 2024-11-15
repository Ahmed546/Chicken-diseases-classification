from ChickenDiseaseClassifier.config.configuration import ConfigurationManager
from ChickenDiseaseClassifier.components.prepare_base_model import PrepareBaseModel
from ChickenDiseaseClassifier import logger


STAGE_NAME="Prepare base model"

class PrepareBaseModleTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
         config = ConfigurationManager()
         prepare_base_model_config = config.get_prepare_base_model_config()
         prepare_base_modle= PrepareBaseModel(config=prepare_base_model_config)
         prepare_base_modle.get_base_model()
         prepare_base_modle.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<" )
        obj = PrepareBaseModleTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x" )
    except Exception as e:
        logger.exception(e)
        raise e
