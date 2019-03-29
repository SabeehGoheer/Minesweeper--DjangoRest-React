import React from "react";
import Cell from "./cell";

const Row = props => {
  let cells = props.cells.map((cell, index) => {
    return (
      <Cell
        data={cell}
        key={index}
        openCell={props.openCell}
        flagCell={props.flagCell}
      />
    );
  });
  return <div className="row">{cells}</div>;
};

export default Row;
