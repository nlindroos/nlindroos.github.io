'use strict';

/* eslint-disable import/default */

import React from 'react';

import { browserHistory } from 'react-router';
import { AppContainer } from 'react-hot-loader';
import { render } from 'react-dom';
import { syncHistoryWithStore } from 'react-router-redux';

import configureStore from './store/configureStore';
require('./favicon.ico'); // Tell webpack to load favicon.ico
// Imported with css-loader in styles.scss
// import 'normalize.css/normalize.css';
// import 'flexboxgrid';
import './styles/styles.scss'; // Yep, that's right. You can import SASS/CSS files too! Webpack will run the associated loader and plug this into the page.

import Root from './containers/Root';

const store = configureStore();

// Create an enhanced history that syncs navigation events with the store
const history = syncHistoryWithStore(browserHistory, store);


render(
    <AppContainer>
        <Root store={store} history={history} />
    </AppContainer>,
    document.getElementById('app')
);

if (module.hot) {
    module.hot.accept('./containers/Root', () => {
        const NewRoot = require('./containers/Root').default;
        render(
            <AppContainer>
                <NewRoot store={store} history={history} />
            </AppContainer>,
            document.getElementById('app')
        );
    });
}
