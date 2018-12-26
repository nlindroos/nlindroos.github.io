import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';
import { reducer as burgerMenu } from 'redux-burger-menu';

import contentful from './contentfulReducer';

const rootReducer = combineReducers({
  routing: routerReducer,
  burgerMenu,
  contentful,
});

export default rootReducer;
