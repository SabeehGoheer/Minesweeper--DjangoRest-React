### Minesweeper Game using Django Rest Framework and Reactjs

1. The game state is stored at the server so player can come back and start playing from where he left.
2. All the algorithms and most business logic is written at the backend.
3. Once a cell of minesweeper is clicked, React app sends Cell ID to server API which in return tells the React APP what to do.
4. Similarly Game Over logic is also at the backend.

To start Backend Server: 
1. Activate Virtualenv from Backend Directory: `source env/bin/activate`
2. Move in to 'src' directory and run server using: `python3 manage.py runserver`

Open a differnet terminal window to start React App:
1. Move to FrontEnd/gui Folder
2. `npm install` to get all dependencies
3. `npm start` to start React Server.
4. Visit http://localhost:3000 to play the game.

<img width="880" alt="Screen Shot 2019-03-29 at 8 02 41 PM" src="https://user-images.githubusercontent.com/48612551/55268218-112bd700-525e-11e9-9401-315b39ae7cc8.png">
