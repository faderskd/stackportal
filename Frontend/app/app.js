'use strict';

// Declare app level module which depends on views, and components
var module = angular.module('myApp', [
  'ngRoute',
  'myApp.Questions',
  'myApp.view2',
  'myApp.version'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/Questions'});
}]);

module.service('GlobalService', function($http) {
  var apiUrl = 'http://188.166.59.78/api';

  this.GetQuestions = function() {
    return $http.get(apiUrl + '/questions');
    $http.get(apiUrl + '/questions/?format=json').
        success(function(data) {
          return data;
        });
  }
});

module.run(function($rootScope, GlobalService) {
  return $rootScope.GlobalService = GlobalService;
}
);