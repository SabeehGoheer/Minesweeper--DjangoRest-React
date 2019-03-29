import React from "react";
import axios from "axios";
import swal from "sweetalert";
import Row from "./row";
class BoardMap extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      rows: [],
      cells: []
    };
  }

  componentDidMount() {
    this.handleServerRequests("get");
  }

  componentDidUpdate() {
    if (this.props.gameStatus === "restart") {
      this.props.updateGameStatus("running");
      this.handleServerRequests("put", 1, "to_destroy");
    }
  }

  startGame() {
    this.handleServerRequests("post");
  }

  makeRows(cellsData) {
    let board = [];

    for (let row = 0; row < this.props.gridSize; row++) {
      board.push([]);
      for (let col = 0; col < this.props.gridSize; col++) {
        board[row].push(cellsData[row * this.props.gridSize + col]);
      }
    }

    this.setState({
      rows: board
    });
    if (this.props.gameStatus === "waiting")
      this.props.updateGameStatus("running");
  }

  openCell = cell => {
    if (this.props.gameStatus === "running") {
      this.handleServerRequests("put", cell.id, "is_revealed");
    }
  };

  flagCell = cell => {
    if (
      this.props.gameStatus === "running" &&
      (cell.is_flagged || this.props.flagCount > 0)
    ) {
      this.handleServerRequests("put", cell.id, "is_flagged");
    }
  };

  cellOpenedActions(data) {
    if (data.gameStatus === "finished") {
      swal("Game Over", "", "error");
      this.setState({
        cells: data.boardMap
      });
      this.makeRows(data.boardMap);
      this.props.updateGameStatus(data.gameStatus);
    } else {
      this.setState({
        cells: data.boardMap
      });
      this.makeRows(data.boardMap);
      this.props.updateFlagCount(data.flaggedCells);
      this.props.checkWinner(data.flaggedCells, data.revealedCells);
    }
  }

  handleServerRequests(requestType, cellId, flag) {
    switch (requestType) {
      case "post":
        return axios
          .post("http://localhost:8000/api/", {
            gridSize: this.props.gridSize,
            numberOfBombs: this.props.numberOfBombs
          })
          .then(res => {
            this.setState({
              cells: res.data
            });
            this.makeRows(res.data);
          })
          .catch(err => {
            console.log(err);
          });
      case "get":
        return axios.get("http://localhost:8000/api/").then(res => {
          if (res.data.boardMap == "") this.startGame();
          else {
            if (res.data.gameStatus == "finished") {
              swal("Game is already finished.", "", "error");
              this.setState({
                cells: res.data.boardMap
              });
              this.makeRows(res.data.boardMap);
              this.props.updateGameStatus(res.data.gameStatus);
            } else {
              this.setState({
                cells: res.data.boardMap
              });
              this.makeRows(res.data.boardMap);
            }
          }
        });
      case "put":
        return axios
          .put("http://localhost:8000/api/" + cellId + "/", {
            flag: flag,
            gridSize: this.props.gridSize
          })
          .then(res => {
            if (flag == "to_destroy") this.startGame();
            else this.cellOpenedActions(res.data);
          })
          .catch(err => {
            console.log(err);
          });
    }
  }

  render() {
    let rows = this.state.rows.map((row, index) => {
      return (
        <Row
          cells={row}
          key={index}
          openCell={this.openCell}
          flagCell={this.flagCell}
        />
      );
    });
    return <div className="board-map">{rows}</div>;
  }
}

export default BoardMap;
