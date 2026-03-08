# One Piece Bounty Poster Generator

This is a Flask app made for Slushies YSWS by Hack Club!

## Endpoints

`/` - A form with HTML, put your name and an image URL
`POST /create-bounty` - Generates data for bounty
`/poster/<poster_id>` - You will see your poster here :D

## Installation
I am using UV project manager for this App... I still have a requirements.txt listed due to YSWS requirement.

### Option 1: Using UV (Recommended)

- Install UV if you haven't already:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Clone the repository and enter it:
```
git clone https://github.com/chishxd/op-bounty.git && cd op-bounty
```

- Install dependencies and run:
```
uv sync
uv run python main.py
```

### Option 2: Using pip and venv

- Clone the repository and enter it:
```
git clone https://github.com/chishxd/op-bounty.git && cd op-bounty
```

- Create a virtual environment:
```
python -m venv .venv
```

- Activate the virtual environment:

For UNIX based systems:
```
source .venv/bin/activate
```

For Windows:
```
source .venv\Scripts\activate
```

- Install requirements:
```
pip install -r requirements.txt
```

Finally... You can run the app using:
```
python main.py
```

Then visit http://127.0.0.1:5000
