'use strict';

angular.module('myApp.Login', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/Login', {
            templateUrl: 'Login/Login.html',
            controller: 'LoginCtrl'
        });
    }])
    .controller('LoginCtrl', function ($scope, $location, $rootScope) {
        $scope.model = {'username':'','password':''};
        $scope.complete = false;
        $scope.login = function(){
            $scope.errors = [];
            //Validate.form_validation(formData,$scope.errors);
            //if(!formData.$invalid){
            $rootScope.GlobalService.Login($scope.model.username, $scope.model.password)
                .then(function(response){
                    $location.path("/");
                },function(response){
                    // error case
                    $scope.errors = response.data;
                });
        }
    });
