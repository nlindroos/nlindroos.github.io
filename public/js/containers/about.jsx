'use strict';

import React, { PropTypes } from 'react';
import Paper from 'material-ui/Paper';

class About extends React.Component {
    render () {
        return (
            <Paper style={style} zDepth={5} circle={true}>
                <p>Text inside</p>
            </Paper>
        );
    }
}
const style = {
    height: 100,
    width: 100,
    margin: 20,
    textAlign: 'center',
    display: 'inline-block',
};

export default About;
