from typing import Optional

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run as app_run

from tourism.components.model_predictor import ModelPredictor, TourismData
from tourism.constant import APP_HOST, APP_PORT
from tourism.pipeline.train_pipeline import TrainPipeline

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

# config = read_params()

templates = Jinja2Templates(directory="templates")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# TOURISM_DATA_KEY = "tourism_data"

# TOURISM_VALUE_KEY = "tourism_value"

# utils = MainUtils()


class DataForm:
    def __init__(self, request: Request):
        self.request: Request = request

        self.Age: Optional[float] = None

        self.CityTier: Optional[int] = None

        self.DurationOfPitch: Optional[float] = None

        self.NumberOfPersonVisiting: Optional[int] = None

        self.NumberOfFollowups: Optional[float] = None

        self.PreferredPropertyStar: Optional[float] = None

        self.NumberOfTrips: Optional[float] = None

        self.Passport: Optional[int] = None

        self.PitchSatisfactionScore: Optional[int] = None

        self.OwnCar: Optional[int] = None

        self.NumberOfChildrenVisiting: Optional[float] = None

        self.MonthlyIncome: Optional[float] = None

        self.TypeofContact: Optional[str] = None

        self.Occupation: Optional[str] = None

        self.Gender: Optional[str] = None

        self.ProductPitched: Optional[str] = None

        self.MaritalStatus: Optional[str] = None

        self.Designation: Optional[str] = None

    async def get_tourism_data(self):
        form = await self.request.form()

        self.Age = form.get("Age")

        self.CityTier = form.get("CityTier")

        self.DurationOfPitch = form.get("DurationOfPitch")

        self.NumberOfPersonVisiting = form.get("NumberOfPersonVisiting")

        self.NumberOfFollowups = form.get("NumberOfFollowups")

        self.PreferredPropertyStar = form.get("PreferredPropertyStar")

        self.NumberOfTrips = form.get("NumberOfTrips")

        self.Passport = form.get("Passport")

        self.PitchSatisfactionScore = form.get("PitchSatisfactionScore")

        self.OwnCar = form.get("OwnCar")

        self.NumberOfChildrenVisiting = form.get("NumberOfChildrenVisiting")

        self.MonthlyIncome = form.get("MonthlyIncome")

        self.TypeofContact = form.get("TypeofContact")

        self.Occupation = form.get("Occupation")

        self.Gender = form.get("Gender")

        self.ProductPitched = form.get("ProductPitched")

        self.MaritalStatus = form.get("MaritalStatus")

        self.Designation = form.get("Designation")


@app.get("/")
async def predictGetRouteClient(request: Request):
    try:

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "context": "Fill all the fields for getting accurate results...",
            },
        )

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/")
async def predictPostRouteClient(request: Request):
    try:
        form = DataForm(request)

        await form.get_tourism_data()

        tourism_data = TourismData(
            Age=form.Age,
            CityTier=form.CityTier,
            DurationOfPitch=form.DurationOfPitch,
            NumberOfPersonVisiting=form.NumberOfPersonVisiting,
            NumberOfFollowups=form.NumberOfFollowups,
            PreferredPropertyStar=form.PreferredPropertyStar,
            NumberOfTrips=form.NumberOfTrips,
            Passport=form.Passport,
            PitchSatisfactionScore=form.PitchSatisfactionScore,
            OwnCar=form.OwnCar,
            NumberOfChildrenVisiting=form.NumberOfChildrenVisiting,
            MonthlyIncome=form.MonthlyIncome,
            TypeofContact=form.TypeofContact,
            Occupation=form.Occupation,
            Gender=form.Gender,
            ProductPitched=form.ProductPitched,
            MaritalStatus=form.MaritalStatus,
            Designation=form.Designation,
        )

        tourism_df = tourism_data.get_tourism_as_dict()

        tourism_predictor = ModelPredictor()

        tourism_value = tourism_predictor.predict(X=tourism_df)[0]

        if tourism_value == 1:
            results = "The Tourist bought the package"

        else:
            results = "The Tourist didn't buy the package"
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "context": f"{results}"},
        )

    except Exception as e:
        return {"status": False, "error": f"{e}"}


@app.get("/train")
async def trainRouteClient():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)
