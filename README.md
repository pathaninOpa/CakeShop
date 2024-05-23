# CakeShop
Simple cake shop website with integration of MongoDB

# #Getting Started
*Dont for get to change to your mongodb username and password in .env file and dont forget to change it back to <password> before git push/pull*

# -requirement
|->react
|->node.js
|->pymongo
|->fastapi
|->axios
|->pydantic

# -start_up
|->front end
  |->cd to client
  |->npm run dev
|->back end
  |->activate .venv if have
  |->cd to server
  |->python -m uvicorn main:app --reload
