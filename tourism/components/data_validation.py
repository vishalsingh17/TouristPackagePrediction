import json
import sys
from typing import Tuple, Union

from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from pandas import DataFrame

from tourism.exception import TourismException
from tourism.logger import logging
from tourism.utils.main_utils import MainUtils


class DataValidation:
    def __init__(self, train_set: DataFrame, test_set: DataFrame):
        self.train_set = train_set

        self.test_set = test_set

        self.validation_status = False

        self.utils = MainUtils()

        self._schema_config = self.utils.read_schema_config_file()

    def validate_schema_columns_length(self, df: DataFrame) -> bool:
        """
        Method Name :   validate_schema_columns
        Description :   This method validates the schema columns for the particular dataframe

        Output      :   True or False value is returned based on the schema
        On Failure  :   Write an exception log and then raise an exception

        Version     :   1.2
        Revisions   :   moved setup to cloud
        """
        try:
            if len(df.columns) == len(self._schema_config["ColumnNames"]):
                validation_status = True

            else:
                validation_status = False

            return validation_status

        except Exception as e:
            raise TourismException(e, sys) from e

    def validate_schema_for_column_names(self, df: DataFrame) -> bool:
        """
        Method Name :   validate_schema for column names
        Description :   This method validates the schema for numerical datatype

        Output      :   True or False value is returned based on the schema
        On Failure  :   Write an exception log and then raise an exception

        Version     :   1.2
        Revisions   :   moved setup to cloud
        """
        try:
            column_list = [
                [j[0] for j in i.items()][0] for i in self._schema_config["ColumnNames"]
            ]

            for column in column_list:
                if column in df.columns:
                    validation_status = True
                else:
                    validation_status = False

            return validation_status

        except Exception as e:
            raise TourismException(e, sys) from e

    def initiate_validate_dataset_schema_column_names(self) -> Tuple[bool, bool]:
        """
        Method Name :   validate_dataset_schema_columns_name
        Description :   This method validates the schema for schema columns for both train and test set

        Output      :   True or False value is returned based on the schema
        On Failure  :   Write an exception log and then raise an exception

        Version     :   1.2
        Revisions   :   moved setup to cloud
        """
        logging.info(
            "Entered validate_dataset_schema_columns method of Data_Validation class"
        )

        try:

            logging.info("Validating dataset schema columns")

            train_schema_status = self.validate_schema_for_column_names(self.train_set)

            logging.info("Validated dataset schema columns name on the train set")

            test_schema_status = self.validate_schema_for_column_names(self.test_set)

            logging.info("Validated dataset schema columns name on the test set")

            logging.info("Validated dataset schema columns")

            return train_schema_status, test_schema_status

        except Exception as e:
            raise TourismException(e, sys) from e

    def initiate_validate_dataset_schema_column_length(self) -> Tuple[bool, bool]:
        """
        Method Name :   validate dataset schema length
        Description :   This method validates the schema for numerical datatype for both train and test set

        Output      :   True or False value is returned based on the schema
        On Failure  :   Write an exception log and then raise an exception

        Version     :   1.2
        Revisions   :   moved setup to cloud
        """
        logging.info(
            "Entered validate_dataset_schema_length method of Data_Validation class"
        )

        try:
            logging.info("Validating dataset schema for column length")

            train_validation_status = self.validate_schema_columns_length(
                self.train_set
            )

            logging.info("Validated dataset schema for column length for train set")

            test_validation_status = self.validate_schema_columns_length(self.test_set)

            logging.info("Validated dataset schema for column length for test set")

            logging.info(
                "Exited validate_dataset_schema_length method of Data_Validation class"
            )

            return train_validation_status, test_validation_status

        except Exception as e:
            raise TourismException(e, sys) from e

    def detect_dataset_drift(
        self, reference: DataFrame, production: DataFrame, get_ratio: bool = False
    ) -> Union[bool, float]:
        """
        Method Name :   detect_dataset_drift
        Description :   This method detects the dataset drift using the reference and production dataframe

        Output      :   Returns bool or float value based on the get_ration parameter
        On Failure  :   Write an exception log and then raise an exception

        Version     :   1.2
        Revisions   :   moved setup to cloud
        """
        try:
            data_drift_profile = Profile(sections=[DataDriftProfileSection()])

            data_drift_profile.calculate(reference, production)

            report = data_drift_profile.json()

            json_report = json.loads(report)

            n_features = json_report["data_drift"]["data"]["metrics"]["n_features"]

            n_drifted_features = json_report["data_drift"]["data"]["metrics"][
                "n_drifted_features"
            ]

            if get_ratio:
                return n_drifted_features / n_features

            else:
                return json_report["data_drift"]["data"]["metrics"]["dataset_drift"]

        except Exception as e:
            raise TourismException(e, sys) from e

    def initiate_data_validation(self) -> bool:
        """
        Method Name :   initiate_data_validation
        Description :   This method initiates the data validation component for the pipeline

        Output      :   Returns bool value based on validation results
        On Failure  :   Write an exception log and then raise an exception

        Version     :   1.2
        Revisions   :   moved setup to cloud
        """
        logging.info("Entered initiate_data_validation method of Data_Validation class")

        try:
            logging.info("Initiated data validation for the dataset")

            drift = self.detect_dataset_drift(
                reference=self.train_set, production=self.test_set
            )

            (
                train_schema_status,
                test_schema_status,
            ) = self.initiate_validate_dataset_schema_column_names()

            logging.info(
                f"Schema train columns name status is {train_schema_status} and schema test columns name status is {test_schema_status}"
            )

            logging.info("Validated dataset schema for columns name")

            (
                train_validation_status,
                test_validation_status,
            ) = self.initiate_validate_dataset_schema_column_length()

            logging.info(
                f"Schema train column length status is {train_validation_status} and schema test column length status is {test_validation_status}"
            )

            logging.info("Validated dataset schema for Length")

            if (
                train_schema_status is True
                and test_schema_status is True
                and train_validation_status is True
                and test_validation_status is True
                and drift is False
            ):

                logging.info("Dataset schema validation completed")

                return True

            else:
                return False

        except Exception as e:
            raise TourismException(e, sys) from e
