'use strict';

angular.module('myApp.mainView', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/mainView', {
    templateUrl: 'mainview/main-view.html',
    controller: 'mainCtrl'
  });
}])

.controller('mainCtrl', [function() {

}]);