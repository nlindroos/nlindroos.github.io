// Decorate react-burger-menu

import React from 'react';
import PropTypes from 'prop-types';
import { scaleRotate as Menu } from 'react-burger-menu';
import { connect } from 'react-redux';
import { decorator as reduxBurgerMenu, action as toggleMenu } from 'redux-burger-menu';
import { NavLink } from 'react-router-dom';
import styled from 'react-emotion';

const NavText = styled(NavLink)`
  color: white;
  text-decoration: none;
`;

// export default reduxBurgerMenu(Menu);
const BoundMenu = reduxBurgerMenu(Menu);
import '../styles/burger-menu.css';

class BurgerMenu extends React.Component {
  closeMenu = () => {
    this.props.dispatch(toggleMenu(false));
  };

  render() {
    return (
      <BoundMenu className="burger-menu-wrapper" pageWrapId="main-content" outerContainerId="body" right>
        <NavText
          to="/"
          onClick={() => {
            this.closeMenu();
            this.scrollToTop();
          }}
          // className={styles.ownName}
        >
          Niklas Lindroos
        </NavText>
        <hr />
        <NavText
          to="/about"
          onClick={this.closeMenu}
          // className={styles.link}
        >
          About
        </NavText>

        <NavText to="/about" onClick={this.closeMenu}>
          Recommended reading
        </NavText>
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
