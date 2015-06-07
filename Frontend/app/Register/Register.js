'use strict';

angular.module('myApp.Register', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/Register', {
            templateUrl: 'Register/Register.html',
            controller: 'RegisterCtrl'
        });
    }])
    .controller('RegisterCtrl', function ($scope, $location, $rootScope) {
        $scope.model = {'username': '', 'password': '', 'password2': '', 'Email': ''};
        $scope.register = function () {
            $scope.errors = [];
            $scope.errors.username = [];
            $scope.errors.email = [];
            $scope.errors.password = [];
            if ($scope.model.password.length < 6) {
                $scope.errors.password.push('Hasło jest za krótkie');
                return;
            }
            if ($scope.model.password != $scope.model.password2) {
                $scope.errors.password.push('Hasła są różne');
                return;
            }

            $rootScope.GlobalService.Register($scope.model.username, $scope.model.Email, $scope.model.password)
                .then(function (response) {
                    $location.path("/Login");
                }, function (response) {
                    // error case
                    $scope.errors = response.data;
                });
        }
    });
