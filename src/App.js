/* eslint-disable import/no-named-as-default */
import { NavLink, Route, Switch } from 'react-router-dom';

import PropTypes from 'prop-types';
import React from 'react';
import { hot } from 'react-hot-loader';

import AboutPage from './components/AboutPage';
import HomePage from './components/HomePage';
import NotFoundPage from './components/NotFoundPage';
import BurgerMenu from './components/BurgerMenu';
// This is a class-based component because the current
// version of hot reloading won't hot reload a stateless
// component at the top-level.
// import './styles/burger-menu.css';

class App extends React.Component {
  render() {
    const activeStyle = { color: 'blue' };
    return (
      <div>
        <BurgerMenu />
        <div id="page-wrap" className="content">
          <NavLink exact to="/" activeStyle={activeStyle}>
            Home
          </NavLink>
          {' | '}
          <NavLink to="/fuel-savings" activeStyle={activeStyle}>
            Demo App
          </NavLink>
          {' | '}
          <NavLink to="/about" activeStyle={activeStyle}>
            About
          </NavLink>
          <Switch>
            <Route exact path="/" component={HomePage} />
            <Route path="/about" component={AboutPage} />
            <Route component={NotFoundPage} />
          </Switch>
        </div>
      </div>
    );
  }
}

App.propTypes = {
  children: PropTypes.element,
};

export default hot(module)(App);
