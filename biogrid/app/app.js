'use strict';

// Declare app level module which depends on views, and components
angular.module('bioGrid', [
  'ngRoute',
  'myApp.mainView',
  'myApp.view2',
  'myApp.version'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/mainView'});
}]);
