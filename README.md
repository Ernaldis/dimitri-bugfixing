When executing, it is important to complete the following steps:
  - Add a .env file with: 
  ```
  DJ_HOST={database address}
  DJ_USER={datajoint username}
  DJ_PASS={datajoint password}
  ```
  - Change the username `ernaldis` in the schema name, found in line 5 of both python files, to your own username. 
  - Build the included Dockerfile. The compose file expects the image to be called ernaldis/datajoint, though any other tag can be used. Just be sure the tag used matches what the Dockerexpects.
