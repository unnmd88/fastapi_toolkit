from fastapi import FastAPI
from src.test_aiohttp import GetDataPeek


app = FastAPI(
    title='Engineering tools'
)

print('tess5')

@app.get('/get_test')
def get_data():
    return 'Tets1'





