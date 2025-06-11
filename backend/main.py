from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Flutter frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, specify your Flutter app domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data
items = [
    {"id": 1, "name": "Jane"},
    {"id": 2, "name": "Brian"},
    {"id": 3, "name": "Wangui"},
]

# Define an API endpoint
@app.get("/items")
def get_items():
    return items
