from chickenDiseaseClassifier import logger
from chickenDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chickenDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data ingestion Stage"

try:
    logger.info(f" >>>>>>  {STAGE_NAME} Stage started")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f" >>>>>>  {STAGE_NAME} Stage completed \n\n x================x")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Prepare Base Model Pipeline"

try:
    logger.info("*********************")
    logger.info(f" >>>>>>  {STAGE_NAME} Stage started")
    pipeline = PrepareBaseModelTrainingPipeline()
    pipeline.main()
    logger.info(f" >>>>>>  {STAGE_NAME} Stage completed \n\n x=================x")
except Exception as e:
    logger.exception(e)
    raise e