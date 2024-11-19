from fastapi import FastAPI
from routes.user_route import router as user_router
from routes.book_route import router as book_router
from routes.membership_route import router as membership_router

# Create an instance of FastAPI
app = FastAPI()

# Register routers
app.include_router(user_router, tags=["Users"])
app.include_router(book_router, tags=["Books"])
app.include_router(membership_router, tags=["Memberships"])

# Entry point to run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main_fastapi_entry:app",
                host="127.0.0.1", port=8000, reload=True)
