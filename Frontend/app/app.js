'use strict';

// Declare app level module which depends on views, and components
var module = angular.module('myApp', [
  'ngRoute',
  'myApp.Questions',
  'myApp.Question',
  'myApp.version',
    'myApp.Login'
]).
config(['$routeProvider', '$httpProvider', function($routeProvider, $httpProvider) {
  $routeProvider.otherwise({redirectTo: '/Questions'});
      $httpProvider.defaults.withCredentials = true;
      //$httpProvider.defaults.useXDomain = true;
      //$httpProvider.defaults.headers.post['Content-Type'] = ''
      //    + 'application/x-www-form-urlencoded; charset=UTF-8';
}]);

module.service('GlobalService', function($http, $cookies) {
  var apiUrl = 'http://188.166.59.78/api';

  this.GetQuestions = function() {
    return $http.get(apiUrl + '/questions/');
  };

  this.Login = function(username, password) {
    return $http.post(apiUrl + '/login/', {username: username, password: password});
  };

  this.PostAnswer = function(questionId, content) {
    return $http.post(apiUrl + '/answers/', {csrfmiddlewaretoken: $cookies.get("csrftoken"), question: questionId, content: content});
  };

  this.GetQuestionsFromCategory = function (name) {
    return $http.get(apiUrl + '/questions/search/?category=' + name + '');

  };
  this.GetQuestionsFromTag = function (name) {
    return $http.get(apiUrl + '/questions/search/?tag=' + name + '');

  };

  this.GetQuestion = function(id) {
    return $http.get(apiUrl + '/questions/' + id + '/');
  };

  this.GetAnswer = function(id) {
    return $http.get(apiUrl + '/answers/' + id + '/');
  };

  this.GetComment = function(id) {
    return $http.get(apiUrl + '/comments/' + id + '/');
  };

  this.GetCategories = function () {
    return $http.get(apiUrl + '/categories/');
  };

  this.GetTags = function() {
    return $http.get(apiUrl + '/tags/');
  };
});

module.run(function($rootScope, GlobalService) {
  return $rootScope.GlobalService = GlobalService;
}
);

$(function () {
  $("#filter").click(function () {
    alert('clicked!');
  });
});