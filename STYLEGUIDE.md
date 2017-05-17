
# JavaScript file contents
All imports should be internally in approximate alphabetical order.

```javascript
'use strict';

import React, { Component, ...}                         // React imports

import _ from 'lodash';                                 // Other 3rd party imports

import * as accountActions from ...                     // Action constructors

import service from './services/service'                // Services

import MyComponent from './components/MyComponent'      // Components

import '../styles/customComponentStyle.css';            // CSS-modules -type imports 
```

# Components
Stateless functions preferred. Reason: [React Reusable Components](https://facebook.github.io/react/docs/reusable-components.html#stateless-functions) and [Stateless functional components](https://medium.com/@housecor/react-stateless-functional-components-nine-wins-you-might-have-overlooked-997b0d933dbc#.gaa5rsnph).

## Stateless functions

```javascript
/*
 *  Explanation (optional)
 */
const DummyComponent = (props) => (
    <div></div>
);

DummyComponent.propTypes = {
    myFunction: PropTypes.func.isRequired
};

// Function declarations outside the component for performance benefits:
// https://medium.com/@esamatti/react-js-pure-render-performance-anti-pattern-fb88c101332f#.2gc1t1jk9.
// Declare with 'const'.
const handleOnClick = (event, props) => {
    ...
};

export default ContactDetails;
```

## ES6 Class

Use when component-level state is required.

```javascript
class SmartComponent extends Component {
    static contextTypes = {};

    static propTypes = {};

    constructor(props) {
        super(props);

        // No binds necessary in the constructor func if es6 function declarations (fat arrows) are used
    }

    /* Component lifecycle methods */

    myFunction = async () => {

    }

    render() {
        return null;
    }
}

export default SmartComponent;
```

# React.createClass
Do not use.
