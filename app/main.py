from fastapi import FastAPI, status, Response, HTTPException, Depends
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .schemas import Client

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"oh hi"}

@app.get("/clients")  
def get_all_clients(db: Session = Depends(get_db)): 
    clients = db.query(models.Client).all()
    return {"data": clients}

@app.get("/clients/{id}", status_code=status.HTTP_200_OK)
def get_single_client(id: int, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id == id).first()
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} was not found")
    return {"data": client}

@app.post("/clients", status_code=status.HTTP_201_CREATED)
def create_client(new_client: Client, db: Session = Depends(get_db)):
    created_client = models.Client(**new_client.model_dump())
    db.add(created_client)
    db.commit()
    db.refresh(created_client)
    return {"data": created_client}

@app.delete("/clients/{id}", status_code=status.HTTP_204_NO_CONTENT) 
def delete_client(id: int, db: Session = Depends(get_db)): 
    client_to_delete = db.query(models.Client).filter(models.Client.id == id).first()
    if client_to_delete is None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} was not found")
    db.delete(client_to_delete)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/clients/{id}")
def update_client(id: int, client: Client, db: Session = Depends(get_db)):
    client_query = db.query(models.Client).filter(models.Client.id == id)
    client_to_update = client_query.first()
    if client_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} was not found")
    client_query.update(client.model_dump())
    db.commit()
    db.refresh(client_to_update)
    return {"data": client_to_update}
   