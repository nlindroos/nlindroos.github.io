'use strict';

// Declare app level module which depends on views, and components
angular.module('bioGrid', [
  'ngRoute',
  'bioGrid.mainView',
  'bioGrid.view2',
  'bioGrid.version'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/mainView'});
}])

.directive('nlScrollListener', function($window, $location) {
    var directiveDefinitionObject = {

        restrict: 'A',
        link: function($scope, elm, attrs) {
            angular.element($window).bind('keydown', function(e) {
            // elm.bind('keydown', function(e) {
                if (e.which ? e.which===40 : false) {
                    if ($location.path() === '/mainView') {
                        $scope.$apply(function() {
                            console.log($location.path());
                            $location.path('view2');
                            console.log(e); 
                        });
                    }
                    else {
                        
                    }
                }
            });

            angular.element($window).bind('click', function() {
                console.log('Reached this point!!!!!!');
            });
        }
    };

    return directiveDefinitionObject;
});

// .controller('BioGridController', ['$scope', '$rootScope', function($scope, $rootScope) {
//     $scope.scoll = scroll;

//     function scroll($event) {
//         console.log('$event', $event);

//     }
// }]);
