# SocialWardrobe

Created by maksymstepaniuk ([maxstepanyuk](https://github.com/maxstepanyuk) on github). The original repository:  [social-wardrobe-fastapi](https://github.com/maxstepanyuk/social-wardrobe-fastapi)

Before using this in your own works, please ask me first.

Contact me or see what I'm up to - [linktree](https://linktr.ee/purpexe)


# FastAPI

## Python and virtual environments on Debian 12

**Install**

On Debian/Ubuntu systems, you need to install the python3-venv package using the following command.

```bash
sudo apt install python3-venv
# sudo apt install python3.11-venv # in my case
```
After installing the python3-venv package, recreate your virtual environment.

**Create**

```bash
python3 -m venv /the_path/the_environment_name
# python3 -m venv env # in my case
```

`env` - name on the virtual environment

**How to activate and deactivate**

activate:

```bash
source the_environment_name/bin/activate
# source env/bin/activate # in my case
```

dactivate:

Just enter this:

```bash
deactivate
```

## Install requirements

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app #in file "main.py" run "app"
``` 