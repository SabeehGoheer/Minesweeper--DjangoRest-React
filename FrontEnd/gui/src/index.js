import React from "react";
import ReactDOM from "react-dom";
import swal from "sweetalert";
import BoardMap from "./components/boardmap";
import Header from "./components/header";
import "./minsweeper.css";

class Minesweeper extends React.Component {
  state = {
    gridSize: 9,
    numberOfBombs: 14,
    flagCount: 14,
    gameStatus: "waiting"
  };

  updateGameStatus = status => {
    this.setState({
      gameStatus: status
    });
  };
  restart = () => {
    swal("Game is restarted", "", "info");
    this.setState({
      gameStatus: "restart",
      flagCount: this.state.numberOfBombs
    });
  };
  updateFlagCount = count => {
    this.setState({
      flagCount: this.state.numberOfBombs - count
    });
  };
  checkWinner = (flagCount, openedCells) => {
    if (openedCells + flagCount >= this.state.gridSize * this.state.gridSize) {
      swal("Congratulations! You won", "", "success");
      this.setState({
        gameStatus: "finished"
      });
    }
  };
  render() {
    return (
      <div className="minesweeper">
        <Header flagCount={this.state.flagCount} restart={this.restart} />
        <BoardMap
          gridSize={this.state.gridSize}
          numberOfBombs={this.state.numberOfBombs}
          gameStatus={this.state.gameStatus}
          flagCount={this.state.flagCount}
          updateGameStatus={this.updateGameStatus}
          updateFlagCount={this.updateFlagCount}
          checkWinner={this.checkWinner}
        />
      </div>
    );
  }
}

ReactDOM.render(<Minesweeper />, document.querySelector("#root"));
