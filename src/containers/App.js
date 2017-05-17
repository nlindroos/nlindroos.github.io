'use strict';

import React from 'react';
import PropTypes from 'prop-types';
import { Link, IndexLink } from 'react-router';

// This is a class-based component because the current
// version of hot reloading won't hot reload a stateless
// component at the top-level.
class App extends React.Component {
    render() {
        return (
            <div>
                <IndexLink to="/">Home</IndexLink>
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
                </div>
                {this.props.children}
            </div>
        );
    }
}

App.propTypes = {
    children: PropTypes.element
};

export default App;
