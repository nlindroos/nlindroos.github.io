'use strict';

import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import { connect } from 'react-redux';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

@connect(state => ({}))
class App extends React.Component {
    static propTypes = {
        children: PropTypes.node
    }

    render () {
        return (
            <MuiThemeProvider muiTheme={getMuiTheme()}>
                <div>
                    <h1>App</h1>
                    <hr />
                    <p>
                        <Link to='/'>home</Link>
                    </p>
                    <p>
                        <Link to='/about'>about</Link>
                    </p>
                    <hr />
                    {this.props.children}
                </div>
            </MuiThemeProvider>
        );
    }
}

export default App;
