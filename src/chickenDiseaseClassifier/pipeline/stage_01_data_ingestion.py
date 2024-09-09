from chickenDiseaseClassifier.config.configuration import ConfigurationManager
from chickenDiseaseClassifier.components.data_ingestion import DataIngestion
from chickenDiseaseClassifier import logger

STAGE_NAME = "Data ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self) -> None:
        config  =ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f" >>>>>> Stage {STAGE_NAME} started")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f" >>>>>> {STAGE_NAME} completed successfully \n\n x================x")
    except Exception as e:
        logger.exception(e)
        raise e 

