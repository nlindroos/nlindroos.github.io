'use strict';

angular.module('bioGrid.mainView', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/mainView', {
    templateUrl: 'mainview/main-view.html',
    controller: 'MainController'
  });
}])

.controller('MainController', ['$document', '$rootScope', function($document, $rootScope) {
    $rootScope.title = 'Biogrid';
    $rootScope.navLogoSrc = 'http://transitions1020.com/assets/v1/img/general/nav_logo.png';

    var body = angular.element($document[0].body);
    body.removeClass('filter');

}]);

