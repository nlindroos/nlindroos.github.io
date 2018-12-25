import { /*  NavLink,  */ Route, Switch } from 'react-router-dom';

import React from 'react';
import { hot } from 'react-hot-loader';
import styled from 'react-emotion';

import Contentful from './services/contentfulClient';
import AboutPage from './views/AboutPage';
import HomePage from './views/HomePage';
import NotFoundPage from './views/NotFoundPage';
import RecommendedReadingPage from './views/RecommendedReadingPage';
import BurgerMenu from './components/BurgerMenu';
// This is a class-based component because the current
// version of hot reloading won't hot reload a stateless
// component at the top-level.
// import './styles/burger-menu.css';

const MainContainer = styled.div`
  max-width: 1080px;
  margin: 0 auto;
  padding: 10px;

  @font-face {
    font-family: allura;
    src: url('../assets/fonts/allura/Allura-Regular.otf');
  }
`;

class App extends React.Component {
  componentDidMount() {
    Contentful.initialise();
  }

  render() {
    // const activeStyle = { color: 'blue' };
    return (
      <React.Fragment>
        <BurgerMenu />

        <MainContainer id="main-content">
          {/* <NavLink exact to="/" activeStyle={activeStyle}>
            Home
          </NavLink>
          {' | '}
          <NavLink to="/fuel-savings" activeStyle={activeStyle}>
            Demo App
          </NavLink>
          {' | '}
          <NavLink to="/about" activeStyle={activeStyle}>
            About
          </NavLink> */}

          <Switch>
            <Route exact path="/" component={HomePage} />
            <Route path="/about" component={AboutPage} />
            <Route path="/recommended" component={RecommendedReadingPage} />
            <Route component={NotFoundPage} />
          </Switch>
        </MainContainer>
      </React.Fragment>
    );
  }
}

export default hot(module)(App);
