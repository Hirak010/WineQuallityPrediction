from WineQualityPrediction import logger
from WineQualityPrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from WineQualityPrediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from WineQualityPrediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from WineQualityPrediction.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


