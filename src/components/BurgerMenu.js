'use strict';

// Decorate react-burger-menu

import { scaleRotate as Menu } from 'react-burger-menu';
import { decorator as reduxBurgerMenu } from 'redux-burger-menu/immutable';

export default reduxBurgerMenu(Menu);
