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
      <BoundMenu
        ref={_ => (this._BurgerMenu = _)}
        className="burger-menu-wrapper"
        pageWrapId="page-wrap"
        outerContainerId="body"
        right
      >
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

export default connect(() => ({}), mapDispatchToProps)(BurgerMenu);
