// Decorate react-burger-menu

import React from 'react';
import PropTypes from 'prop-types';
import { scaleRotate as Menu } from 'react-burger-menu';
import { decorator as reduxBurgerMenu } from 'redux-burger-menu';
import { connect } from 'react-redux';
import { action as toggleMenu } from 'redux-burger-menu';
import { NavLink, Route, Switch } from 'react-router-dom';

// export default reduxBurgerMenu(Menu);
const BoundMenu = reduxBurgerMenu(Menu);
import '../styles/burger-menu.css';

class BurgerMenu extends React.Component {
  closeMenu = () => {
    this.props.dispatch(toggleMenu(false));
  };

  render() {
    return (
      <BoundMenu
        ref={_ => (this._BurgerMenu = _)}
        className="burger-menu-wrapper"
        pageWrapId="page-wrap"
        outerContainerId="body"
        right
      >
        <NavLink
          to="/"
          onClick={() => {
            this.closeMenu();
            this.scrollToTop();
          }}
          // className={styles.ownName}
        >
          Niklas Lindroos
        </NavLink>
        <hr />
        <NavLink
          to="/about"
          onClick={this.closeMenu}
          // className={styles.link}
        >
          About
        </NavLink>
      </BoundMenu>
    );
  }
}

BurgerMenu.propTypes = {
  dispatch: PropTypes.func.isRequired,
};

const mapDispatchToProps = dispatch => {
  return {
    dispatch,
  };
};

export default connect(
  () => ({}),
  mapDispatchToProps
)(BurgerMenu);
