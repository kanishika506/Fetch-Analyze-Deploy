from fastapi import fastAPI
app=fastAPI()

@app.get("/")
def home():
    return {"message":"hello , am home!"}

@app.get("/status")
def status():
    return{"database":"connected", "server":"online"}