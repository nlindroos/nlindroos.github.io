webpackJsonp([0],{92:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{"default":e}}Object.defineProperty(t,"__esModule",{value:!0}),t.changeTitle=void 0;var o=n(17),u=n(93),l=(r(u),n(114)),a=r(l);t.changeTitle=(0,o.createAction)(a["default"].CHANGE_TITLE,function(e){return document.title=e})},114:function(e,t){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t["default"]={CHANGE_TITLE:"CHANGE_TITLE"}},113:function(e,t){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t["default"]={SUCCESS:0,FAIL:1}},93:function(e,t,n){(function(e){"use strict";function r(e){return e&&e.__esModule?e:{"default":e}}Object.defineProperty(t,"__esModule",{value:!0});var o=n(94),u=r(o),l=n(111),a=r(l),i=n(113),c=r(i);t["default"]=function(t){var n=(0,u["default"])(t,(0,o.fetchBackend)(a["default"]));return n.addErrorInterceptor(function(t,n){return e.reject(t)}),n.addResponseInterceptor(function(t,n){var r=t.data,o=t.statusCode;return r.code===c["default"].SUCCESS?t:e.reject(new Error(n.method+" "+n.url+" => "+o+" "+JSON.stringify(r)))}),n}}).call(t,n(1))},115:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{"default":e}}function o(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function u(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function l(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0});var a=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),i=n(2),c=r(i),f=function(e){function t(){return o(this,t),u(this,Object.getPrototypeOf(t).apply(this,arguments))}return l(t,e),a(t,[{key:"render",value:function(){return c["default"].createElement("div",null,"about")}}]),t}(c["default"].Component);t["default"]=f},30:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{"default":e}}function o(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function u(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function l(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0});var a,i,c,f,s=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),d=n(2),p=r(d),y=n(6),b=n(5),h=(a=(0,b.connect)(function(e){return{}}),a((f=c=function(e){function t(){return o(this,t),u(this,Object.getPrototypeOf(t).apply(this,arguments))}return l(t,e),s(t,[{key:"render",value:function(){return p["default"].createElement("div",null,p["default"].createElement("h1",null,"App"),p["default"].createElement("hr",null),p["default"].createElement("p",null,p["default"].createElement(y.Link,{to:"/"},"home")),p["default"].createElement("p",null,p["default"].createElement(y.Link,{to:"/about"},"about")),p["default"].createElement("hr",null),this.props.children)}}]),t}(p["default"].Component),c.propTypes={children:d.PropTypes.node},i=f))||i);t["default"]=h},31:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{"default":e}}function o(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function u(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function l(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0}),t.Home=void 0;var a,i=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),c=n(2),f=r(c),s=n(5),d=n(32),p=r(d),y=n(92),b=t.Home=(0,p["default"])(a=function(e){function t(){return o(this,t),u(this,Object.getPrototypeOf(t).apply(this,arguments))}return l(t,e),i(t,[{key:"componentWillMount",value:function(){this.props.changeTitle("ReactApp")}},{key:"render",value:function(){return f["default"].createElement("div",{style:[h.base,h.larger]},"Hello ReactApp")}}]),t}(f["default"].Component))||a,h={base:{color:"red"},larger:{fontSize:20}};t["default"]=(0,s.connect)(null,{changeTitle:y.changeTitle})(b)},4:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{"default":e}}function o(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function u(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function l(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0});var a=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),i=n(2),c=r(i),f=n(5),s=n(6),d=n(7),p=n(12),y=r(p),b=n(30),h=r(b),_=n(31),v=r(_),m=n(115),E=r(m),O=(0,d.syncHistoryWithStore)(p.hashHistory,y["default"]),w=null,j=function(e){function t(){return o(this,t),u(this,Object.getPrototypeOf(t).apply(this,arguments))}return l(t,e),a(t,[{key:"render",value:function(){return c["default"].createElement(f.Provider,{store:y["default"]},c["default"].createElement("div",null,c["default"].createElement(s.Router,{history:O},c["default"].createElement(s.Route,{path:"/",component:h["default"]},c["default"].createElement(s.IndexRoute,{component:v["default"]}),c["default"].createElement(s.Route,{path:"about",component:E["default"]}))),w))}}]),t}(c["default"].Component);t["default"]=j},0:function(e,t,n){(function(e){"use strict";function t(e){return e&&e.__esModule?e:{"default":e}}var r=n(2),o=t(r),u=n(3),l=n(4),a=t(l);window.handleError=function(e){console.error("error",e,e.stack),alert(e.stack)},e.onPossiblyUnhandledRejection(handleError),window.onerror=function(e,t,n,r,o){handleError(o?o:new Error(e+"("+t+"):"+n+"-"+r))};var i=null;try{i=(0,u.render)(o["default"].createElement(a["default"],null),document.getElementById("app"))}catch(c){handleError(c)}}).call(t,n(1))},16:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.title=t.state=void 0;var r=n(13),o=n(17),u=n(7),l=n(29),a=t.state=(0,l.fromJS)({title:null}),i=t.title=(0,o.handleActions)({CHANGE_TITLE:function(e,t){return t.payload}},a.get("title"));t["default"]=(0,r.combineReducers)({routing:u.routerReducer,title:i})},12:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{"default":e}}function o(e){if(Array.isArray(e)){for(var t=0,n=Array(e.length);t<e.length;t++)n[t]=e[t];return n}return Array.from(e)}Object.defineProperty(t,"__esModule",{value:!0}),t.hashHistory=void 0;var u=n(13),l=n(14),a=r(l),i=n(6),c=n(15),f=n(7),s=n(16),d=r(s),p=t.hashHistory=(0,i.useRouterHistory)(c.createHashHistory)({queryKey:!1}),y=[],b=[a["default"],(0,f.routerMiddleware)(p)];t["default"]=(0,u.createStore)(d["default"],u.compose.apply(void 0,[u.applyMiddleware.apply(void 0,o(b))].concat(o(y))))}});