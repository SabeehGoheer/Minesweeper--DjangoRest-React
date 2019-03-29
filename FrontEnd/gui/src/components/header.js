import React from "react";

const Header = props => {
  return (
    <div className="header">
      <div className="restart">
        <button className="ui button restart" onClick={props.restart}>
          Restart
        </button>
      </div>
      <div className="flag-count">
        <span>
          <i className="flag checkered icon" />
        </span>
        {props.flagCount}
      </div>
    </div>
  );
};

export default Header;
