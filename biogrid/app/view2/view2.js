'use strict';

angular.module('bioGrid.view2', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view2', {
    templateUrl: 'view2/view2.html',
    controller: 'View2Ctrl'
  });
}])

.controller('View2Ctrl', ['$document', '$location', '$rootScope', '$scope', '$timeout', '$window', function($document, $location, $rootScope, $scope, $timeout, $window) {

    var body = angular.element($document[0].body),
        window = angular.element($window),
        maxCount = 5;

    $scope.count = 1;
    $rootScope.loading = true;
    $timeout(function() {
        $rootScope.loading = false;
    }, 2000);

    body.addClass('filter');

    window.bind('keydown', function(e) {
        // Restrict navigation if loading
        if ($rootScope.loading) {
            e.preventDefault();
            return;
        }
        var key = e.which ? e.which : false;
        console.log(key);
        if (key===38) {
            if ($scope.count === 1) {
                $scope.$apply(function() {
                    $rootScope.loading = true;
                    $timeout(function() {
                        $rootScope.loading = false;
                    }, 2000);
                    $location.path('mainView');
                });
            }
            else {
                $scope.$apply(function() {
                    $scope.count--;
                    $rootScope.loading = true;
                    $timeout(function() {
                        $rootScope.loading = false;
                    }, 2000);
                });
            }
        }
        else if (key===40) {
            if ($scope.count !== maxCount) {
                $scope.$apply(function() {
                    $scope.count++;
                    $rootScope.loading = true;
                    $timeout(function() {
                        $rootScope.loading = false;
                    }, 2000);
                });
            }
        }
    });

}]);