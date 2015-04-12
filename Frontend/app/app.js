'use strict';

// Declare app level module which depends on views, and components
var module = angular.module('myApp', [
  'ngRoute',
  'myApp.Questions',
  'myApp.Question',
  'myApp.version'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/Questions'});
}]);

module.service('GlobalService', function($http) {
  var apiUrl = 'http://188.166.59.78/api';

  this.GetQuestions = function() {
    return $http.get(apiUrl + '/questions/');
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
});

module.run(function($rootScope, GlobalService) {
  return $rootScope.GlobalService = GlobalService;
}
);