
# [Sharesafely](https://sharesafelycld.azurewebsites.net/)

This project was inspired by [@Gwyneth Pena's](https://twitter.com/madebygps)  5 [Projects to Get Azure AZ-104 Skills (Cloud Administrator)](https://www.youtube.com/watch?v=Qd0YI9ZMHHs&t=9s).    
Get project Repo [Git](https://github.com/rcoffie/cloud-projects/blob/main/az-104/readme.md)  
More details Details on [ShareSafely](https://github.com/rcoffie/cloud-projects/blob/main/az-104/sharesafely.md)  

## Homepage Screenshot


![home](https://github.com/rcoffie/ShareSafely/assets/34107104/23cc088e-3f00-4184-9cf7-03c2e25b7efa)


## This Web App was build with [Django](https://www.djangoproject.com/) on the backend 


![django](https://github.com/rcoffie/ShareSafely/assets/34107104/3be3d05a-b211-49f9-9898-4e7b9bff3735)


## This Web App was build with [Bootstrap](https://getbootstrap.com/) on the Frontend


![bootstrap](https://github.com/rcoffie/ShareSafely/assets/34107104/46bcbd31-222c-45f4-a1f8-862574997859)


## Development

To deploy this project run

* Create project folder 
```bash
  mkdir project_folder && cd project_folder 
```


* create your enviroment on unic/macos

```bash
  python3 -m pip install --user virtualenv
  python3 -m venv env
  source env/bin/activate
```

* create your enviroment on Windows

```bash
  python -m pip install --user virtualenv
  python -m venv env
  .\env\Scripts\activate
```

* Clone project from GitHub 

```bash
  git clone https://github.com/rcoffie/ShareSafely.git
```
* Install packages  

```bash
  pip install requirements.txt 
```


* Run migration

```bash
  python manage.py makemigrations 
```

* Run Migrate

```bash
  python manage.py migrate  
```

* Runserver

```bash
  python mange.py runserver 
```
