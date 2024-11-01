from mlProject import logging
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline

Stage_name = "Data Ingestion"
try:
    data_ingestion= DataIngestionPipeline()
    data_ingestion.main()
except Exception as e:
    logging.exception(e)
    raise e 