from chickenDiseaseClassifier import logger
from chickenDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data ingestion Stage"

try:
    logger.info(f" >>>>>> Stage {STAGE_NAME} started")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f" >>>>>> {STAGE_NAME} completed successfully \n\n x================x")
except Exception as e:
    logger.exception(e)
    raise e 
