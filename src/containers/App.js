'use strict';

import React from 'react';
import PropTypes from 'prop-types';

import { connect } from 'react-redux';
import { Link, IndexLink } from 'react-router';
import { action as toggleMenu } from 'redux-burger-menu/immutable';

import styles from '../styles/burger-menu.css';

import BurgerMenu from '../components/BurgerMenu';

// This is a class-based component because the current
// version of hot reloading won't hot reload a stateless
// component at the top-level.
class App extends React.Component {
    static propTypes = {
        dispatch: PropTypes.func.isRequired,
        children: PropTypes.element
    };

    constructor(props) {
        super(props);
    }

    closeMenu = () => {
        this.props.dispatch(toggleMenu(false));
    }

    render() {
        return (
            <div>
                <BurgerMenu right>
                    <IndexLink to="/" onClick={this.closeMenu} className={styles.link}>Home</IndexLink>
                    <Link to="/about" onClick={this.closeMenu} className={styles.link}>About</Link>
                    <a id="home" className="menu-item" href="/">Old homepage</a>
                    {/*<a id="home" className="menu-item" href="/">Home</a>
                    <a id="about" className="menu-item" href="/about">About</a>*/}
                </BurgerMenu>
                <div className="content">
                {/*<IndexLink to="/">Home</IndexLink>
                {' | '}
                <Link to="/fuel-savings">Demo App</Link>
                {' | '}
                <Link to="/about">About</Link>
                <br/>

                <div className="row">
                    <div className="col-xs-8">
                        <div className="box">
                            <span>hurl</span>
                        </div>
                    </div>
                    <div className="col-xs-4">
                        <div className="box">
                            <span>hurl2</span>
                        </div>
                    </div>
                </div>*/}
                {this.props.children}
                </div>
            </div>
        );
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        dispatch
    };
};

export default connect(() => ({}), mapDispatchToProps)(App);
