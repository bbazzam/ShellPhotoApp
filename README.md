# shelllButtonCam
# ShellPhotoApp

## To Run in venv
```
python3 -m venv proj-env
source proj-env/bin/activate
```

# Build the req
```
pip freeze > requirements.txt
python -m pip install -r requirements.txt
------
pipreqs /path/to/project
pip install -r requirements.txt
```


## Start the application
```
add a config file in the config directory pass it in the run `--config`
source ~/workspace/shellCamera/proj-env/bin/activate
sudo python src/main.py --config "config/shellCamera_actual.yml" 
 ```
