'use strict';

import React from 'react';
import PropTypes from 'prop-types';
import { Provider } from 'react-redux';
import { Router } from 'react-router';

import routes from '../routes';

const Root = (props) => (
    <Provider store={props.store}>
        <Router history={props.history} routes={routes} />
    </Provider>
);

Root.propTypes = {
    store: PropTypes.object.isRequired,
    history: PropTypes.object.isRequired
};

export default Root;
