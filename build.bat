python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
expand frontend.zip -f:* public
del /f frontend.zip
deactivate
