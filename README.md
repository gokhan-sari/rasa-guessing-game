# Rasa Guessing Game

### About

This repository contains the animal guessing game developed using [Rasa](https://rasa.com/docs/rasa/).

### To set up your working environment:

1. Create a new virtual environment by choosing a Python interpreter and making a .\\venv directory to hold it:
```
C:\> python3 -m venv ./venv
```

2. Activate the virtual environment:
```
C:\> .\venv\Scripts\activate
```

3. Install Rasa using pip:
```
pip3 install rasa
```

4. Clone the repository and navigate to the project directory:
```
git clone https://github.com/gokhan-sari/rasa-guessing-game.git
```

```
cd rasa-guessing-game
```

5. Run the following command to trains a Rasa model:
```
rasa train
```

6. Run the following commands in different shells to start the chatbot:
```
rasa run actions
```

```
rasa shell
```