'use strict';

// Declare app level module which depends on views, and components
var module = angular.module('myApp', [
    'ngRoute',
    'ngCookies',
    'myApp.Questions',
    'myApp.Question',
    'myApp.version',
    'myApp.Register',
    'myApp.Login'
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

    this.GetQuestions = function () {
        return $http.get(apiUrl + '/questions/');
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