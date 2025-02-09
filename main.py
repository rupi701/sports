from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.sports import Sport
from setup import get_db

app = FastAPI()

class SportsInput(BaseModel):
    name:str
    channel: str
    price: float
    game: str
    time: float
    Category: float
    transaction_date: str


@app.post("/enter_sports")
def add_sports(frontend_sports: SportsInput, db:Session = Depends(get_db)):
    db_sports = Sport(
        channel=frontend_sports.channel,
        Game= frontend_sports.game,
        time= frontend_sports.time,
        Category= frontend_sports.Category,
    )
    db.add(db_sports)
    db.commit()
    db.refresh(db_sports)
    return db_sports

@app.get("/fetch_sports")
def get_sports(db: Session = Depends(get_db)):
    sport = db.query(Sport).all()
    return sport

@app.get("/fetch_sports/{sports_id}")
def get_sports(sports_id: int, db : Session = Depends(get_db)):
    sports = db.query(Sport).filter(Sport.id == sports_id).first()
    return sports

@app.delete("/delete_sports/{sports_id}")
def delete_data(sports_id: int, db:Session = Depends(get_db)):
    sports = db.query(Sport).filter(Sport.id == sports_id).first()
    db.delete(sports)
    db.commit()
    return "sports data deleted"

@app.put("/change_sports/{sports_id}")
def change_data(sports_id:int, front_sports: SportsInput, db: Session = Depends(get_db)):
    sports= db.query(Sport).filter(Sport.id == sports_id).first()
    sports.name= front_sports.name
    sports.Category = front_sports.Category
    sports.transaction_date = front_sports.transaction_date
    sports.Game = front_sports.game
    db.commit()
    db.refresh(sports)
    return sports