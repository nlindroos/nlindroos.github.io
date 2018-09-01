import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';
import { reducer as burgerMenu } from 'redux-burger-menu';

const rootReducer = combineReducers({
  routing: routerReducer,
  burgerMenu,
});

export default rootReducer;
