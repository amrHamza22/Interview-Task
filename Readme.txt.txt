- absolute difference script is used directly and the script prompts length and list as mentioned in the task. 

- Flask is used in task_state_api so you must install it via : pip install flask 

- the db is sqlite3 you can view it through DB browser you can find it here https://sqlitebrowser.org/

- the API route is http://127.0.0.1:5000/ChangeState/<taskid> (port is default 5000 modify if another app is working on it)

- the db has 5 dummy tasks with various states and I've commented the lines used for data insertion and database creation 

- state is changed throught POST request with a raw body that contain the target state only 
(I've used postman and just wrote the state in a raw form of the request body)

- get request works fine, put request only change Title which is provided in json form {"Title":etc..), 
  delete request works fine as well.



