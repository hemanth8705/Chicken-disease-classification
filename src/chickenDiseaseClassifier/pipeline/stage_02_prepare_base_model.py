from chickenDiseaseClassifier.config.configuration import ConfigurationManager
from chickenDiseaseClassifier.components.prepare_base_model import PrepareBaseModel
from chickenDiseaseClassifier import logger

STAGE_NAME = "Preparing base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info("*********************")
        logger.info(f">>>>>>>>>>>>>>> Stage {STAGE_NAME} started")
        pipeline = PrepareBaseModelTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} completed \n\n x=======================x")
    except Exception as e:
        logger.exception(e)
        raise e
    
