'use strict';

angular.module('myApp.Login', ['ngRoute', 'ngCookies'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/Login', {
            templateUrl: 'Login/Login.html',
            controller: 'LoginCtrl'
        });
    }])
    .controller('LoginCtrl', function ($scope, $location, $rootScope, $cookies) {
        $scope.model = {'username':'','password':''};
        $scope.complete = false;
        $scope.login = function(){
            $scope.errors = [];
            //Validate.form_validation(formData,$scope.errors);
            //if(!formData.$invalid){
            $rootScope.GlobalService.Login($scope.model.username, $scope.model.password)
                .then(function(response){
                    //$cookies.put('sessionId', response.data.sessionid);
                    //$cookies.put('csrftoken', response.data.csrf_token);
                    $location.path("/");
                },function(response){
                    // error case
                    $scope.errors = response.data;
                });
        }
    });
