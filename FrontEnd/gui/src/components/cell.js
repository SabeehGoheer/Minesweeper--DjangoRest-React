import React from "react";

const Cell = props => {
  let renderCell = () => {
    if (props.data.is_revealed) {
      if (props.data.is_mine === true) {
        // To show bombs
        return (
          <div className="cell open">
            <span>
              <i className="bomb icon" />
            </span>
          </div>
        );
      } else if (props.data.neighbour_mine_count === 0) {
        // To show opened cell without count
        return <div className="cell open" />;
      } // To show opened cell with counts
      else
        return (
          <div className="cell open count">
            {props.data.neighbour_mine_count}
          </div>
        );
    } else if (props.data.is_flagged === true) {
      // To show flags
      return (
        <div
          className="cell"
          onContextMenu={e => {
            e.preventDefault();
            props.flagCell(props.data);
          }}
        >
          <span>
            <i className="flag checkered icon" />
          </span>
        </div>
      );
    } else {
      // To show hidden fields
      return (
        <div
          className="cell"
          onContextMenu={e => {
            e.preventDefault();
            props.flagCell(props.data);
          }}
          onClick={() => props.openCell(props.data)}
        />
      );
    }
  };

  return renderCell();
};

export default Cell;
