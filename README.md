
                                                                                                


 i R- Q j


    Tiangolo    
 @ @FastAPI ̍\ z                i   v    :  @   j



Tiangolo    

https://fastapi.tiangolo.com/ja/deployment/docker/


.
       app
            __init__.py
            main.py
       Dockerfile
       requirements.txt



                                                                                                


       Section 1 DockerImage ̍쐬      


  STEP 1  ޗ  t H   _   쐬    

$mkdir C:\Users\maete\Documents\fastAPI_Tiangolo_1



  STEP 2 requirements.txt   쐬    

type nul > C:\Users\maete\Documents\fastAPI_Tiangolo_1\requirements.txt

 ȉ    L ڂ   


################################
fastapi>=0.68.0,<0.69.0
pydantic>=1.8.0,<2.0.0
uvicorn>=0.15.0,<0.16.0
################################



  STEP 2 Dockerfile    쐬    

type nul > C:\Users\maete\Documents\fastAPI_Tiangolo_1\Dockerfile


 t @ C     蓮 ŊJ   Ĉȉ    L ڂ   B

# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


#ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]





       Section 5  v   W F N g t H   _  api t H   _   쐬    main.py      B       


$mkdir C:\Users\maete\Documents\fastAPI_Tiangolo_1\app


   ɁAVScode   J   āA ȉ    L ڂ  āAmain.py Ƃ   app t H   _ ̒    ɕۑ     B

##################################################################################

from typing import Union


from fastapi import FastAPI, File, UploadFile, Form
import os


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    a = os.getcwd()
    a2 = len(q)
    return {"item_id": item_id, "q": q, "current_path":a, "length":a2}


####################################################################################

   ɁAapi ̒    ɁA__init__.py      B



       Section 9 docker build     s           

#    ܂łɁA ޗ  t H   _ ̒  ɕύX         Ă  邽 ߁A       ܂߂āA R   e i   X V    
#        s    ƁAStatus   AExited    Up ɕύX     B


# docker image build [ I v V    ] Dockerfile ̃p X

$docker image build -t fast_image_1 C:\Users\maete\Documents\fastAPI_Tiangolo_1\Dockerfile 


OR

$cd C:\Users\maete\Documents\fastAPI_Tiangolo_1
$docker image build -t myimage . --no-cache



       Section 9  R   e i   쐬 E N             


$docker run -d --name mycontainer -p 80:80 myimage


       Section 10 @    m F       

http://localhost:80/docs

http://localhost:80

http://localhost:80/items/5?q=somequery

http://localhost:80/items/100?q=all

#protein ̔z  

http://localhost:80/items/10?q=MAEGEITTFTALTEKFNLPPGNYKKPKLLYCSNGGHFLRILPDGTVDGTRDRSDQH




       Section 11   n         

$cd C:\Users\maete


 @  R   e i ̌ n  
docker ps -a
docker container stop fastapi_folder-demo-app-1
docker container stop fastapi_folder-demo-app-1
docker container rm fastapi_folder-demo-app-1
docker container rm fastapi_folder-demo-app-1


 A C   [ W ̌ n  
docker image ls
docker image rm mysql
 B l b g   [ N ̌ n  
docker network ls
 C {     [   ̌ n  
docker volume ls
docker volume rm apa000vol1

 D   [ J  PC ̃t H   _ ̍폜

rd /s /q C:\Users\maete\Documents\fastAPI_Tiangolo_1




 i I   j

