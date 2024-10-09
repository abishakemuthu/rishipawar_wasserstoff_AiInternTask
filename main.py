from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger

STATE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STATE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STATE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e
