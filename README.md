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
