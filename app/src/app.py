from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="static/")
app.mount("/static", StaticFiles(directory="static"), name="static")

df = pd.read_pickle("data/ord.pkl")
top15 = list(
    df[df["len"] == 5].iloc[:, 2:].count().sort_values(ascending=False)[:15].index
)


def containsAll(str: str, set: str) -> bool:
    return 0 not in [c in str for c in set]


def check_letters(s: str, len: int = 5) -> list:
    print(s)
    return list(
        df[(df["len"] == len) & (df["ord"].apply(lambda x: containsAll(x, s)))]["ord"]
    )


def check_net_letters(test: str, l: list) -> list:
    not_test = [i for i in top15 if i not in test]
    return [i for i in l if all([not j in i for j in not_test])]


@app.get("/")
def read_form():
    return "Hello wørdle"


@app.get("/w")
def form_post(request: Request):
    return templates.TemplateResponse(
        "form.html",
        context={
            "request": request,
        },
    )


@app.post("/w")
def form_post(request: Request, letters: str = Form(...)):
    letters = letters.lower()
    result = check_letters(letters)
    result2 = check_net_letters(letters, result)
    return templates.TemplateResponse(
        "form.html",
        context={
            "request": request,
            "letters": letters,
            "result": result,
            "result2": result2,
        },
    )
