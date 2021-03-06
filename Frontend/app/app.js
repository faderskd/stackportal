'use strict';

// Declare app level module which depends on views, and components
var module = angular.module('myApp', [
    'ngRoute',
    'ngCookies',
    'myApp.Questions',
    'myApp.Question',
    'myApp.version',
    'myApp.Auth',
    'ui.bootstrap'
]).
    config(['$routeProvider', '$httpProvider', function ($routeProvider, $httpProvider) {
        $routeProvider.otherwise({redirectTo: '/Questions'});
        $httpProvider.defaults.withCredentials = true;
        //$httpProvider.defaults.useXDomain = true;
        //$httpProvider.defaults.headers.post['Content-Type'] = ''
        //    + 'application/x-www-form-urlencoded; charset=UTF-8';
    }]);

module.service('GlobalService', function ($http, $cookies) {
    var apiUrl = 'http://127.0.0.1:8000/api';

    this.Login = function (username, password) {
        return $http.post(apiUrl + '/login/', {username: username, password: password});
    };

    this.Logout = function () {
        return $http.get(apiUrl + '-auth/logout/');
    };


    this.Register = function (username, email, password) {
        var json = {
            username: username,
            password: password,
            email: email
        };
        var data = $.param({
            csrfmiddlewaretoken: $cookies.get("csrftoken"),
            _content_type: 'application/json',
            _content: JSON.stringify(json)
        });
        return $http({
            method: 'POST',
            url: apiUrl + '/users/',
            data: data,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        });
    };

    this.PostAnswer = function (questionId, content) {
        var json = {
            content: content,
            question: questionId
        };
        var data = $.param({
            csrfmiddlewaretoken: $cookies.get("csrftoken"),
            _content_type: 'application/json',
            _content: JSON.stringify(json)
        });
        return $http({
            method: 'POST',
            url: apiUrl + '/answers/',
            data: data,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        });
    };

    this.PostComment = function (questionId, answerId, content) {
        var json = {
            content: content,
            question: questionId,
            answer: answerId
        };
        var data = $.param({
            csrfmiddlewaretoken: $cookies.get("csrftoken"),
            _content_type: 'application/json',
            _content: JSON.stringify(json)
        });
        return $http({
            method: 'POST',
            url: apiUrl + '/comments/',
            data: data,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        });
    };

     this.PostQuestion = function (title, content, category, tags) {
        var json = {
            title: title,
            content: content,
            category: category,
            tags: tags
        };
        var data = $.param({
            csrfmiddlewaretoken: $cookies.get("csrftoken"),
            _content_type: 'application/json',
            _content: JSON.stringify(json)
        });
        return $http({
            method: 'POST',
            url: apiUrl + '/questions/',
            data: data,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        });
    };

    this.AddTag = function (name) {
        var json = {
            name: name
        };
        var data = $.param({
            csrfmiddlewaretoken: $cookies.get("csrftoken"),
            _content_type: 'application/json',
            _content: JSON.stringify(json)
        });
        return $http({
            method: 'POST',
            url: apiUrl + '/tags/',
            data: data,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        });
    };

    this.GetUsers = function () {
        return $http.get(apiUrl + '/users/');
    };

    this.GetQuestions = function () {
        return $http.get(apiUrl + '/questions/');
    };

    this.GetQuestionsFromCategory = function (name) {
        return $http.get(apiUrl + '/questions/search/?category=' + name + '');
    };

    this.GetQuestionsFromTag = function (name) {
        return $http.get(apiUrl + '/questions/search/?tag=' + name + '');
    };

    this.GetQuestion = function (id) {
        return $http.get(apiUrl + '/questions/' + id + '/');
    };

    this.LikeQuestion = function (id) {
        var data = $.param({csrfmiddlewaretoken: $cookies.get("csrftoken"), _method: "PUT"});
        return $http({
            method: 'POST',
            url: apiUrl + '/questions/' + id + '/like/',
            data: data,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        });
    };

    this.DislikeQuestion = function (id) {
        var data = $.param({csrfmiddlewaretoken: $cookies.get("csrftoken"), _method: "PUT"});
        return $http({
            method: 'POST',
            url: apiUrl + '/questions/' + id + '/dislike/',
            data: data,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        });
    };

    this.GetAnswer = function (id) {
        return $http.get(apiUrl + '/answers/' + id + '/');
    };

    this.LikeAnswer = function (id) {
        var data = $.param({csrfmiddlewaretoken: $cookies.get("csrftoken"), _method: "PUT"});
        return $http({
            method: 'POST',
            url: apiUrl + '/answers/' + id + '/like/',
            data: data,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        });
    };

    this.DislikeAnswer = function (id) {
        var data = $.param({csrfmiddlewaretoken: $cookies.get("csrftoken"), _method: "PUT"});
        return $http({
            method: 'POST',
            url: apiUrl + '/answers/' + id + '/dislike/',
            data: data,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        });
    };

    this.MarkAnswer = function (id) {
        var data = $.param({csrfmiddlewaretoken: $cookies.get("csrftoken"), _method: "PUT"});
        return $http({
            method: 'POST',
            url: apiUrl + '/answers/' + id + '/solve/',
            data: data,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        });
    };

    this.GetComment = function (id) {
        return $http.get(apiUrl + '/comments/' + id + '/');
    };

    this.GetCategories = function () {
        return $http.get(apiUrl + '/categories/');
    };

    this.GetTags = function () {
        return $http.get(apiUrl + '/tags/');
    };
});

module.run(function ($rootScope, GlobalService) {
        return $rootScope.GlobalService = GlobalService;
    }
);

$(function () {
    $("#filter").click(function () {
        alert('clicked!');
    });
});


angular.module('myApp.Auth', ['ngCookies'])
    .controller('AuthCtrl', function ($scope, $location, $rootScope, $cookies, $route, $timeout) {
        $scope.model = {'username': '', 'password': ''};
        if ($cookies.get("username") != null)
            $scope.loggedUser = $cookies.get("username");
        $scope.complete = false;
        $scope.login = function () {
            $scope.errors = [];
            //Validate.form_validation(formData,$scope.errors);
            //if(!formData.$invalid){
            $timeout(function () {
                $rootScope.GlobalService.Login($scope.model.username, $scope.model.password)
                    .then(function (response) {
                        $rootScope.GlobalService.GetUsers().then(function (response) {
                            var i;
                            for (i = 0; i < response.data.length; i++)
                                if (response.data[i].username == $scope.model.username) {
                                    $cookies.put("username", response.data[i].username);
                                    $cookies.put("userId", response.data[i].id);
                                }
                            $scope.loggedUser = $cookies.get("username");
                        });
                    }, function (response) {
                        // error case
                        $scope.errors = response.data;
                    });
            });
        };

        $scope.Rmodel = {'username': '', 'password': '', 'password2': '', 'Email': ''};
        $scope.register = function () {
            $scope.Rerrors = [];
            $scope.Rerrors.username = [];
            $scope.Rerrors.email = [];
            $scope.Rerrors.password = [];
            if ($scope.Rmodel.password.length < 6) {
                $scope.Rerrors.password.push('Hasło jest za krótkie');
                return;
            }
            if ($scope.Rmodel.password != $scope.Rmodel.password2) {
                $scope.Rerrors.password.push('Hasła są różne');
                return;
            }

            $rootScope.GlobalService.Register($scope.Rmodel.username, $scope.Rmodel.Email, $scope.Rmodel.password)
                .then(function (response) {
                    $scope.Rmodel.username = "";
                    $scope.Rmodel.Email = "";
                    $scope.Rmodel.password = "";
                    $scope.Rmodel.password2 = "";
                    alert("Dodano nowe konto");
                    $location.path("/Questions");
                }, function (response) {
                    // error case
                    $scope.Rerrors = response.data;
                });
        };
        $scope.logout = function () {
            $timeout(function () {
                angular.forEach($cookies.getAll(), function (v, k) {
                    $cookies.remove(k);
                });
                $rootScope.GlobalService.Logout();
                $scope.loggedUser = $cookies.get("username");
            });
        };
    });
