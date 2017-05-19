'use strict';

// Set up your root reducer here...
import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';
import { reducer as burgerMenu } from 'redux-burger-menu/immutable';

const rootReducer = combineReducers({
    burgerMenu,
    routing: routerReducer
});

export default rootReducer;
