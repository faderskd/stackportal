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
                    $rootScope.GlobalService.GetUsers().then(function(response)
                    {
                        var i;
                        for (i = 0; i < response.data.length; i++)
                            if (response.data[i].username == $scope.model.username)
                            {
                                $cookies.put("username", response.data[i].username);
                                $cookies.put("userId", response.data[i].id);
                            }
                    });
                    $location.path("/");
                },function(response){
                    // error case
                    $scope.errors = response.data;
                });
        }
    });
