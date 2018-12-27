import { combineReducers } from 'redux';
import { reducer as burgerMenu } from 'redux-burger-menu';

import contentful from './contentfulReducer';

const rootReducer = combineReducers({
  burgerMenu,
  contentful,
});

export default rootReducer;
