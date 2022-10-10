LOG_DIR = "logs"

LOG_FILE = "app.log"

ARTIFACTS_DIR = "artifacts"

MODEL_SAVE_FORMAT = ".sav"

MODEL_FILE_NAME = "model"

MODEL_CONFIG_FILE = "config/model.yaml"

SCHEMA_CONFIG_FILE = "config/schema.yaml"

BEST_MODEL_PATH = ARTIFACTS_DIR + "/" + MODEL_FILE_NAME + MODEL_SAVE_FORMAT

BASE_MODEL_SCORE = 0.6

PREPROCESSOR_OBJ_FILE_NAME = ARTIFACTS_DIR + "/" + "tourism_preprocessor.pkl"

TRAIN_TEST_SPLIT_SIZE = 0.2

RANDOM_STATE = 42

TARGET_COLUMN = "ProdTaken"

APP_HOST = "0.0.0.0"

APP_PORT = 8080

IO_FILES_BUCKET = "tourism-io-files"
